#!/bin/bash

ROOT=$(git rev-parse --show-toplevel)

$ROOT/bin/init

MMAP_OPTION='vm.mmap_min_addr=0'
if ! grep -q $MMAP_OPTION /etc/sysctl.conf ; then
        sudo sh -c "echo '$MMAP_OPTION' >> /etc/sysctl.conf"
        sudo sysctl -w $MMAP_OPTION
fi

if [[ ! -e vmlinux ]]; then
  echo "Generating vmlinux (kernel image):"
  sudo $ROOT/bin/extract-vmlinux /boot/vmlinuz-$(uname -r) > vmlinux
  $ROOT/bin/ROPgadget --binary vmlinux > vmlinux.gadget

  echo "Kernel symbols:"
  sudo cat /proc/kallsyms | grep prepare_kernel_cred
  sudo cat /proc/kallsyms | grep commit_creds
fi

cat <<EOF
 _          _     ___  
| |    __ _| |__ / _ \ 
| |   / _\` | '_ \ (_) |
| |__| (_| | |_) \__, |
|_____\__,_|_.__/  /_/ 
                    cs6265
EOF

                       
