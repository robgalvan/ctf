#!/usr/bin/env python

'''
Tool for writing shellcode. Give it a string to push onto the stack and it
generates the corresponding push instructions.
'''

import sys


def print_word(word):
    print 'push', '0x' + word[::-1].encode('hex')

if len(sys.argv) != 2:
    print 'usage: <program> text'
    sys.exit()

if len(sys.argv[1]) % 4 != 0:
    print 'text must be multiple of 4. pad your slashes or something.'
    sys.exit()

chunks = map(lambda x: sys.argv[1][x:x+4], range(0, len(sys.argv[1]), 4))[::-1]
map(print_word, chunks)