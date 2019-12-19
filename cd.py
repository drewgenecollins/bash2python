#!/usr/bin/env python3

import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument('cd', help ='changes directory to a specified path')
args= parser.parse_args()
os.chdir(args.cd)


#There are two best practices to follow when using this method:

#Catch the exception (WindowsError, OSError) on invalid path. If the exception is thrown, do not perform any recursive operations, especially destructive ones. They will operate on the old path and not the new one.

#Return to your old directory when you're done. This can be done in an exception-safe manner by wrapping your chdir call in a context manager, like Brian M. Hunt did in his answer.

