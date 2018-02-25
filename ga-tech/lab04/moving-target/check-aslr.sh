#!/bin/bash

gcc -m32 -std=gnu99 -fPIE -pie -fno-stack-protector -g -O0 -o pie pie.c

{
  for i in {1..10000}; do
    ./pie
  done
} > addresses

python3 plot.py addresses > data
gnuplot plot.gp
