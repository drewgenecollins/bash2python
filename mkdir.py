#!/usr/bin/env python3

import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument('mkdir', help ='creates a directory in a specified path')
args= parser.parse_args()
newdir=os.mkdir(args.mkdir)



