#!/bin/bash

if [ $(id -u) -ne 0 ]
  then echo Please run this script as root or using sudo!
  exit
fi

cp xmas.py /usr/bin
cp xmas.service /etc/systemd/system/

systemctl enable xmas
systemctl start xmas

