#!/bin/bash

if [ $(id -u) -ne 0 ]
  then echo Please run this script as root or using sudo!
  exit
fi

systemctl disable xmas
rm -f xmas.py /usr/bin
rm -f xmas.service /etc/systemd/system/
