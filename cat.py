#!/usr/bin/env python3
#print ('This script will print out a file\nThis is equivalent to the bash command cat')

#file=open('ex_file.csv', 'r') #open function assumes read mode by default

import argparse
parser=argparse.ArgumentParser()
parser.add_argument('cat', help ='prints out a file')
args= parser.parse_args()
file=open(args.cat)
print(file.read(), end='')
