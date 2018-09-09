![chords2midi](https://i.imgur.com/rvXoXOf.png)
# chord2midi

Given it a chord progression, get a MIDI file!

Take your MIDI file, drop it into your favorite DAW and [make a beat!](https://clyp.it/drltahki)

## Installation

    $ pip install chord2midi

## Usage

    $ c2m I V vi IV --key C
    $ ls
    C-I-V-vi-IV.mid

More usage:

    $ c2m I V vi iii IV I IV V --key D --bpm 120 --octave 5 --duration .25 # Pachabel's Canon in D, Staccato EDM Version


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

## Common Progressions

The classic:

     $ c2m I V vi IV

50's progression:

     $ c2m I vi IV V

12 bar blues:

    $ c2m I I I I IV IV I I V V I I
   
or:

    $ c2m I I I I IV IV I I V VI I V  

Smoke on the water:

    $ c2m ii IV V

Wild thing:

    $ c2m I IV  V IV

Flamenco:

    $ c2m vi V VI V

Gently weeps:

    $  c2m ii I V6 VIIb VI

Sad:

    $ c2m vi IV I V

And, loads and loads more.

Rich Jones, 2018. MIT.
