![chords2midi](https://i.imgur.com/rvXoXOf.png)
# chord2midi

Given it a chord progression, get a MIDI file!

## Installation

    $ pip install chord2midi

## Usage

    $ c2m I V vi IV --key C
    $ ls
    C-I-V-vi-IV.mid

Further options:

```
usage: c2m.py [-h] [-i] [-b BPM] [-t OCTAVE] [-k KEY] [-d DURATION] [-v]
              [U [U ...]]

chords2midi - Create MIDI files from written chord progressions.

positional arguments:
  U                     Please supply chord progression!. See --help for more
                        options.

optional arguments:
  -h, --help            show this help message and exit
  -i, --install         Install into Ableton directory
  -b BPM, --bpm BPM     Set the BPM (default 160)
  -t OCTAVE, --octave OCTAVE
                        Set the octave (default 4)
  -k KEY, --key KEY     Set the key (default C)
  -d DURATION, --duration DURATION
                        Set the chord duraction (default 1)
  -v, --version         Display the current version of chords2midi
```

Rich Jones, 2018. MIT.
