#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files.
For each file it computes a variety of statistics, and then
prints a summary of the statistics as output.

The goal is to provide a solid foundation for new bioinformatics command line tools,
and is an ideal starting place for new projects.'''


setup(
    name='PD-Scr',
    version='0.1.0.0',
    author='TianyiLu',
    author_email='tianyi9494@gmail.com',
    packages=['PD-Scr'],
    package_dir={'PD-Scr': 'PD-Scr'},
    entry_points={
        'console_scripts': ['PD-Scr = PD-Scr.PD-Scr:main']
    },
    url='https://github.com/TianyiLu9494/PD-Scr',
    license='LICENSE',
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython"],
)
