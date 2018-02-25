#!/bin/bash

ROOT=$(git rev-parse --show-toplevel)

$ROOT/bin/init

cat <<EOF
 _          _      ___  
| |    __ _| |__  ( _ ) 
| |   / _\` | '_ \ / _ \ 
| |__| (_| | |_) | (_) |
|_____\__,_|_.__/ \___/ 
                    cs6265
EOF

                       
