![chords2midi](https://i.imgur.com/rvXoXOf.png)
# chords2midi

Given it a chord progression, get a MIDI file!

Take your MIDI file, drop it into your favorite DAW and [make a beat!](https://clyp.it/drltahki) Or [two](https://clyp.it/f0g1ko5b).

## Installation

    $ pip install chords2midi

## Usage

    $ c2m I V vi IV --key C
    $ ls
    C-I-V-vi-IV.mid

More usage:

    $ c2m I V vi iii IV I IV V --key D --bpm 128 --octave 5 --duration .25 # Pachabel's Canon in D, Staccato EDM Version
    $ ls
    D-I-V-vi-iii-IV-I-IV-V-128.mid

You can also use named chords directly:

    $ c2m Am Em F G --bpm 80
    $ ls
    Am-Em-F-G-80.mid

You can place rests with `X`:

    $ c2m I X V X vi X IV

You can also reverse formats, so you can easily transpose into a different key:

    $ c2m C D E --key C --reverse
    I II III

Further options:

```
usage: c2m.py [-h] [-B] [-b BPM] [-t OCTAVE] [-i INPUT] [-k KEY] [-n NOTES]
              [-d DURATION] [-D] [-H HUMANIZE] [-o OUTPUT] [-O OFFSET]
              [-p PATTERN] [-r] [-v]
              [U [U ...]]

chords2midi - Create MIDI files from written chord progressions.

positional arguments:
  U                     Please supply chord progression!. See --help for more
                        options.

optional arguments:
  -h, --help            show this help message and exit
  -B, --bassline        Throw an extra bassline on the pattern
  -b BPM, --bpm BPM     Set the BPM (default 80)
  -t OCTAVE, --octave OCTAVE
                        Set the octave(s) (ex: 3,4) (default 4)
  -i INPUT, --input INPUT
                        Read from an input file.
  -k KEY, --key KEY     Set the key (default C)
  -n NOTES, --notes NOTES
                        Notes in each chord (default all)
  -d DURATION, --duration DURATION
                        Set the chord duraction (default 1)
  -D, --directory       Output the contents to the directory of the input
                        progression.
  -H HUMANIZE, --humanize HUMANIZE
                        Set the amount to "humanize" (strum) a chord, in ticks
                        - try .11 (default 0.0)
  -o OUTPUT, --output OUTPUT
                        Set the output file path. Default is the current key
                        and progression in the current location.
  -O OFFSET, --offset OFFSET
                        Set the amount to offset each chord, in ticks.
                        (default 0.0)
  -p PATTERN, --pattern PATTERN
                        Set the pattern. Available patterns: basic2, basic4,
                        hiphop, basic, alt, alt4, alt2
  -r, --reverse         Reverse a progression from C-D-E format into I-II-III
                        format
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

    $ c2m I IV V IV

Flamenco:

    $ c2m vi V VI V

Gently weeps:

    $  c2m ii I V6 VIIb VI

Sad:

    $ c2m vi IV I V

Neo-soul:

    $ c2m ii7 V9 I7

Hot Chip:

    $ c2m Cm Bb Fm Cm Eb Bb G Cm --bpm 125 --pattern alt2

House:

    $ c2m I VII V VI

EDM:

   $ c2m VI IV I V

   or

   $ c2m VI IV V I // or basically any order of these chords

Country:

    $ c2m I vi IV V
    $ c2m I ii V I
    $ c2m I IV I vi V IV I

Frank Ocean:

    $ c2m IV7 ii7 iii7 vi IV7 iii7 III7 ii
    $ c2m iv III VIII i

Alice Deejay:

   $ c2m E D#m G#m F# --bpm 137

The Chad Basic Music Theory Producer:

   $ c2m vi IV III V

And [lots more](https://www.hooktheory.com/theorytab/common-chord-progressions)!

## Playback

If you're on OSX:

    $ brew install timidity
    $ timidity your-midi.mid

## Related

 * [UltimateTemplate](https://github.com/Miserlou/UltimateTemplate) - Production-ready Ableton Live project templates.
 * [ADGMaker](https://github.com/Miserlou/ADGMaker) - Make Ableton ADG instruments from Free Philharmonia Orchestra samples

Rich Jones, 2018. MIT.
