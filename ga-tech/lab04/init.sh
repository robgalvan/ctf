#!/bin/sh

ROOT=$(git rev-parse --show-toplevel)

$ROOT/bin/init

ARCH=$(uname -m)

if [ "$ARCH" = "x86_64" ]; then
    wget http://www.capstone-engine.org/download/3.0.4/ubuntu-14.04/libcapstone3_3.0.4-0.1ubuntu1_amd64.deb -O libcapstone3.deb
    wget http://www.capstone-engine.org/download/3.0.4/ubuntu-14.04/python-capstone_3.0.4-0.1ubuntu1_amd64.deb -O python-capstone.deb
else
    wget http://www.capstone-engine.org/download/3.0.4/ubuntu-14.04/libcapstone3_3.0.4-0.1ubuntu1_i386.deb -O libcapstone3.deb
    wget http://www.capstone-engine.org/download/3.0.4/ubuntu-14.04/python-capstone_3.0.4-0.1ubuntu1_i386.deb -O python-capstone.deb
fi

sudo dpkg -i libcapstone3.deb
sudo dpkg -i python-capstone.deb
rm libcapstone3.deb
rm python-capstone.deb

# disable randomization
echo 3 | sudo tee /proc/sys/kernel/randomize_va_space

cat <<EOF
 _          _     _  _   
| |    __ _| |__ | || |  
| |   / _\` | '_ \| || |_ 
| |__| (_| | |_) |__   _|
|_____\__,_|_.__/   |_|  
                    cs6265
EOF
