#!/usr/bin/env python3

import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument('ls', help ='prints out a directory content')
args= parser.parse_args()

dirlist=os.listdir(args.ls)

from pprint import pprint
pprint(dirlist)


