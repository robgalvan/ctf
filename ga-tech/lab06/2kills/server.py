#!/usr/bin/python2
import os
import subprocess as sp
import signal

SIZE = 0x1000
ROOT = os.path.dirname(__file__)

def execute_process(target):
    target = os.path.join(ROOT, target)
    p = sp.Popen(target, stdin = sp.PIPE, \
                                stdout = sp.PIPE)
    p.stdout.readline() # Get...
    p.stdin.write(payload)
    p.stdout.readline() # Input...
    out = p.stdout.readline().strip()
    return out

if __name__ == '__main__':
    print "Kill two binaries with one ROP"
    print "(neeed to read 'MSG' in target)"
    signal.alarm(5)
    payload = os.read(0, SIZE)

    out1 = execute_process(os.path.join(ROOT, 'target1'))
    out2 = execute_process(os.path.join(ROOT, 'target2'))

    if (out1 == "READ_THIS_FIRST" \
        and out2 == "YOU_SHOULD_READ_THIS_TOO"):
        print "Wow...!\nThis is your flag...\n"
        os.system("cat /proc/flag")
    else:
        print "Failed..."

