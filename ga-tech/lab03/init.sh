#!/bin/sh

ROOT=$(git rev-parse --show-toplevel)

$ROOT/bin/init

# disable randomization
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

cat <<EOF
 _          _    _____ 
| |    __ _| |__|___ / 
| |   / _\` | '_ \ |_ \ 
| |__| (_| | |_) |__) |
|_____\__,_|_.__/____/ 
                    cs6265
EOF
