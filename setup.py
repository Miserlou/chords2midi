import os
import sys
from setuptools import setup

# Set external files
try:
    from pypandoc import convert
    README = convert('README.md', 'rst')     
except ImportError:
    README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name='chords2midi',
    version='0.9.0',
    packages=['chords2midi'],
    install_requires=required,
    include_package_data=True,
    license='MIT License',
    description='Create MIDI files from chord progressions', 
    long_description=README,
    url='https://github.com/Miserlou/chords2midi',
    author='Rich Jones',
    author_email='miserlou@gmail.com',
    entry_points={
        'console_scripts': [
            'c2m=chords2midi.c2m:handle',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
