#!/bin/bash

URL=http://www.capstone-engine.org/download/3.0.4/ubuntu-14.04/
ROOT=$(git rev-parse --show-toplevel)

$ROOT/bin/init

install_capstone() {  
  if [ $(dpkg-query -W -f='${Status}' libcapstone3 2>/dev/null | \
	grep -c "ok installed") -eq 0 ];
  then

    if [[ $(uname -m) == "x86_64" ]]; then
      wget $URL/libcapstone3_3.0.4-0.1ubuntu1_amd64.deb -O libcapstone3.deb
      wget $URL/python-capstone_3.0.4-0.1ubuntu1_amd64.deb -O python-capstone.deb

    else
      wget $URL/libcapstone3_3.0.4-0.1ubuntu1_i386.deb -O libcapstone3.deb
      wget $URL/python-capstone_3.0.4-0.1ubuntu1_i386.deb -O python-capstone.deb
    fi

    sudo dpkg -i libcapstone3.deb
    sudo dpkg -i python-capstone.deb

    rm libcapstone3.deb
    rm python-capstone.deb

  fi
}

install_capstone

# install libseccomp
sudo apt-get install libseccomp-dev

# enable randomization
echo 3 | sudo tee /proc/sys/kernel/randomize_va_space

cat <<EOF
 _          _    ____  
| |    __ _| |__| ___| 
| |   / _\` | '_ \___ \ 
| |__| (_| | |_) |__) |
|_____\__,_|_.__/____/ 
                    cs6265
EOF

                       
