#!/bin/sh

ROOT=$(dirname "$0")/..

$ROOT/bin/init

# disable randomization
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

cat <<EOF
 _          _    ____  
| |    __ _| |__|___ \ 
| |   / _\` | '_ \ __) |
| |__| (_| | |_) / __/ 
|_____\__,_|_.__/_____|
                    cs6265
EOF
