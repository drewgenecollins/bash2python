#!/usr/bin/env python3

import argparse
from shutil import move

parser=argparse.ArgumentParser()
parser.add_argument('src', help ='copy file from source')
parser.add_argument('dst', help ='copy file to destination')
args= parser.parse_args()
move(args.src,args.dst)



