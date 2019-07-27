#!/bin/bash

if [ -z "$SERVER_IP" ] || [ "$EUID" -ne 0 ]
then
      echo "YOU MUST START THIS SCRIPT WITH 'sudo -E $0'"
      exit
fi

echo "SERVER_IP: $SERVER_IP"

echo "nameserver $SERVER_IP"  >  /etc/resolv.conf
echo "nameserver 1.1.1.1" >> /etc/resolv.conf
#echo "nameserver 8.8.8.8"  >  /etc/resolv.conf
sudo systemctl enable systemd-resolved.service
sudo systemctl start systemd-resolved

