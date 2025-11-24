#!/bin/bash

if [ $(id -u) -ne 0 ]
  then echo Please run this script as root or using sudo!
  exit
fi

systemctl stop xmas
systemctl disable xmas
rm -f /usr/bin/xmas.py
rm -f /etc/systemd/system/xmas.sesrvice
systemctl daemon-reload
