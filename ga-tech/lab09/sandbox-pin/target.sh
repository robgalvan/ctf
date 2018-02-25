#!/bin/bash
PIN=pin-2.14-71313-gcc.4.4.7-linux

$PIN/intel64/bin/pinbin -t $PIN/source/tools/Sandbox/obj-intel64/Sandbox.so -- ./target
