# c2m.py - chords2midi

import argparse
import os
import pychord
import time

from midiutil import MIDIFile
from mingus.core.progressions import to_chords

####################################################################
# Data
####################################################################

####################################################################
# Main
####################################################################

class Chords2Midi(object):
    """
    Read CLI input, create MIDI files.

    """

    def handle(self, argv=None):
        """
        Main function.

        Parses command, load settings and dispatches accordingly.

        """
        help_message = "Please supply chord progression!. See --help for more options."
        parser = argparse.ArgumentParser(description='chords2midi - Create MIDI files from written chord progressions.\n')
        parser.add_argument('progression', metavar='U', type=str, nargs='*', help=help_message)
        parser.add_argument('-i', '--install', action='store_true', help='Install into Ableton directory', default=False)
        parser.add_argument('-b', '--bpm', type=int, default=160, help='Set the BPM (default 160)')
        parser.add_argument('-t', '--octave', type=int, default=4, help='Set the octave (default 4)')
        parser.add_argument('-k', '--key', type=str, default='C', help='Set the key (default C)')
        parser.add_argument('-d', '--duration', type=float, default=1.0, help='Set the chord duraction (default 1)')
        parser.add_argument('-o', '--output', type=str, help='Set the output file path. Default is the current key and progression in the current location.')
        parser.add_argument('-v', '--version', action='store_true', default=False,
            help='Display the current version of chords2midi')

        args = parser.parse_args(argv)
        self.vargs = vars(args)

        if self.vargs['version']:
            version = pkg_resources.require("chords2midi")[0].version
            print(version)
            return

        # Support `c2m I III V and `c2m I,III,V` formats.
        if len(self.vargs['progression']) < 1:
            print("You need to supply a progression! (ex I V vi IV)")
            return
        if len(self.vargs['progression']) < 2:
            progression = self.vargs['progression'][0].split(',')
        else:
            progression = self.vargs['progression']

        track    = 0
        channel  = 0
        ttime     = 0
        duration = self.vargs['duration'] # In beats
        tempo    = self.vargs['bpm']   # In BPM
        volume   = 100  # 0-127, as per the MIDI standard

        midi = MIDIFile(1)
        midi.addTempo(track, ttime, tempo)

        bar = 0
        progression_cords = to_chords(progression, self.vargs['key'])
        for chord in progression_cords:
            for note in chord:
                pitch = pychord.utils.note_to_val(note) + (self.vargs['octave'] * 12)
                midi.addNote(track, channel, pitch, bar, duration, volume)
            bar = bar + 1

        if self.vargs['output']:
            filename = self.vargs['output']
        else:
            filename = self.vargs['key'] + '-' + '-'.join(progression) + '.mid'
            if os.path.exists(filename):
                filename = self.vargs['key'] + '-' + '-'.join(progression) + '-' + str(int(time.time())) + '.mid'

        with open(filename, "wb") as output_file:
            midi.writeFile(output_file)


def handle(): # pragma: no cover
    """
    Main program execution handler.
    """
    try:
        c2m_obj = Chords2Midi()
        c2m_obj.handle()
    except (KeyboardInterrupt, SystemExit): # pragma: no cover
        return
    except Exception as e:
        print(e)

if __name__ == '__main__': # pragma: no cover
    handle()
