#!/bin/bash

cp xmas.py /usr/local/bin

# Make sure there is script reference in rc.local, before the exit call.
if ! grep -q xmas.py /etc/rc.local ; then
    sed -i 's/^exit 0/\/usr\/local\/bin\/xmas.py \&\nexit 0/' /etc/rc.local
fi
