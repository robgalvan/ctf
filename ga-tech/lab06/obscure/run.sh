#!/bin/bash
BASEDIR=$(dirname $0)

cat $BASEDIR/target.asm
qemu-arm -R 20M -L /usr/arm-linux-gnueabi/ $BASEDIR/target
