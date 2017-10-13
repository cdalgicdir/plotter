#! /usr/bin/env python
# encoding: UTF-8
# author: Cahit Dalgicdir
# license: MIT

"""
    plotter
    ============
    Plotter script using Matplotlib
    Needs: 
        1-) filenames
            Two column files
    Output:
        Matplotlib plots
    Usage:
        plotter file1 file2
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser(description='Plotter using matplotlib')
parser.add_argument('--label_fs', action='store', dest='label_fontsize', default=13,
        type=float, help='Fontsize for labels')
parser.add_argument('filenames', metavar='N', type=str, nargs='+',
       help='Filenames to be plotted')
parser.add_argument('--multi', action='store_true', dest='multi', default=False,
        help='Multiple plots in one figure area')
parser.add_argument('--3d', action='store_true', dest='m3d', default=False,
        help='3d plots')
parser.add_argument('--pdf', action='store', dest='pdf', default=None,
        help='Save to pdf')
parser.add_argument('--png', action='store', dest='png', default=None,
        help='Save to png')
parser.add_argument('--save', action='store', dest='save', default=None,
        help='Save to python file ')

args = parser.parse_args()
# args.multi
# args.m2d
# args.pdf
# args.png
# args.save
doplot = True
if args.pdf is not None:
    doplot = False
    savefile = args.pdf
elif args.png is not None:
    doplot = False
    savefile = args.png
elif args.save is not None:
    doplot = False
    savefile = args.save

plt.style.use('presentation')
mpl.rcParams['mathtext.default'] = 'regular'

if len(args.filenames) >= 1:
    flist = args.filenames
else:
    print('Filename not given! Exiting... ')
    sys.exit(1)

for f in flist:
    data = np.loadtxt(f, comments=['@','#'])
    plt.plot(data[:,0], data[:,1], label=f)

plt.legend(labelspacing=0.2, fancybox=True, fontsize=13)
plt.grid(alpha=0.25)
plt.tight_layout()
if doplot:
    plt.show()
