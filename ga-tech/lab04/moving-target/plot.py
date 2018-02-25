#!/usr/bin/env python3

import sys

from collections import Counter

bag = []
for i in range(8):
    bag.append(Counter())

for l in open(sys.argv[1]):
    l = l.strip()
    if l == "":
        continue
    assert(l.startswith("0x"))

    l = l[2:]
    for i in range(8):
        bag[i][l[i]] += 1

for b in range(0xf+1):
    for i in range(8):
        cnt = bag[i]["%x" % b]
        print("%s " % min(cnt, 1500) , end="")
    print()
