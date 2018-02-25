#!/bin/sh
    cat payload | ./target
    if [ $? -ne 128 -o $? -ne 129 ]; then
        echo "It crashed!"
        sh payload.sh
    fi
