#!/home/vagrant/cs6265/lab05/puzzle/python2.7

import sys
import subprocess as sp
import os

TARGET_STRING = 'ROP_ATTACK_SUCCESS'

if __name__ == '__main__':
    print 'Your mission is to make a ROP chain that prints "%s"' % TARGET_STRING
    payload = raw_input()
    p = sp.Popen(['./target', payload], stdout = sp.PIPE)
    #p = sp.Popen(['gdb', './target'], stdout = sp.PIPE)
    print p.stdout.readline(),
    if (p.stdout.readline().strip() == TARGET_STRING):
        os.system("/bin/cat /proc/flag")
    else:
        print "Failed.."
