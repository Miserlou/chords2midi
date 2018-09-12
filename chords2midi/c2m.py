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
        parser.add_argument('-b', '--bpm', type=int, default=160, help='Set the BPM (default 160)')
        parser.add_argument('-t', '--octave', type=int, default=4, help='Set the octave (default 4)')
        parser.add_argument('-i', '--input', type=str, default=None, help='Read from an input file.')
        parser.add_argument('-k', '--key', type=str, default='C', help='Set the key (default C)')
        parser.add_argument('-n', '--notes', type=int, default=99, help='Notes in each chord (default all)')
        parser.add_argument('-d', '--duration', type=float, default=1.0, help='Set the chord duraction (default 1)')
        parser.add_argument('-H', '--humanize', type=float, default=0.0, help='Set the amount to "humanize" (strum) a chord, in ticks - try .11 (default 0.0)')
        parser.add_argument('-o', '--output', type=str, help='Set the output file path. Default is the current key and progression in the current location.')
        parser.add_argument('-O', '--offset', type=float, help='Set the amount to offset each chord, in ticks. (default 0.0)')
        parser.add_argument('-v', '--version', action='store_true', default=False,
            help='Display the current version of chords2midi')

        args = parser.parse_args(argv)
        self.vargs = vars(args)

        if self.vargs['version']:
            version = pkg_resources.require("chords2midi")[0].version
            print(version)
            return

        # Support `c2m I III V and `c2m I,III,V` formats.
        if not self.vargs['input']:
            if len(self.vargs['progression']) < 1:
                print("You need to supply a progression! (ex I V vi IV)")
                return
            if len(self.vargs['progression']) < 2:
                progression = self.vargs['progression'][0].split(',')
            else:
                progression = self.vargs['progression']
        else:
            with open(self.vargs['input']) as fn:
                content = ''.join(fn.readlines()).strip()
                content = content.replace('\n', ' ').replace(',', '  ')
                progression = content.split(' ')

        track    = 0
        channel  = 0
        ttime     = 0
        duration = self.vargs['duration'] # In beats
        tempo    = self.vargs['bpm']   # In BPM
        volume   = 100  # 0-127, as per the MIDI standard
        bar = 0
        offset = self.vargs['offset']

        midi = MIDIFile(1)
        midi.addTempo(track, ttime, tempo)

        ##
        # Main generator
        ##

        # We do this to allow blank spaces
        progression_chords = []
        for chord in progression:
            progression_chord = to_chords(chord, self.vargs['key'])
            if progression_chord == []:
                progression_chord = [None]
            progression_chords.append(progression_chord[0])

        for chord in progression_chords:
            if chord is not None:
                humanize_amount = self.vargs['humanize']
                for i, note in enumerate(chord):
                    pitch = pychord.utils.note_to_val(note) + (self.vargs['octave'] * 12)
                    midi.addNote(
                        track=track,
                        channel=channel,
                        pitch=pitch,
                        time=offset + bar + humanize_amount,
                        duration=duration,
                        volume=volume
                    )

                    humanize_amount = humanize_amount + self.vargs['humanize']
                    if i + 1 >= self.vargs['notes']:
                        break
            bar = bar + 1

        ##
        # Output
        ##

        if self.vargs['output']:
            filename = self.vargs['output']
        elif self.vargs['input']:
            filename = self.vargs['input'].replace('.txt', '.mid')
        else:
            filename = self.vargs['key'] + '-'  + '-'.join(progression) + '-' + str(self.vargs['bpm']) + '.mid'
            if os.path.exists(filename):
                filename = self.vargs['key'] + '-' + '-'.join(progression) + '-' + str(self.vargs['bpm']) +  + '-' + str(int(time.time())) + '.mid'

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
