#!/bin/bash

containerid="$1"
if [ -z "$containerid" ]
then
   echo "Missing continer ID"
   cmd="docker container ls"
   containerid=$( docker container ls --filter name='^/pihole$' | grep pihole | head -n1 | awk '{print $1;}')
    echo "pihole id: " $containerid
fi 


  #  sudo -E $HOME/stopdns.sh
  #  docker container stop $containerid
  #  docker container rm $containerid
  #  $HOME/up.sh

containerid=$( docker container ls --filter name='^/pihole$' | grep pihole | head -n1 | awk '{print $1;}')
echo "new id: $containerid"
docker container stop $containerid
sleep 3
sudo -E $HOME/stacks/misc/scripts/stopdns.sh
sleep 10
#sudo -E $HOME/stacks/misc/scripts/startdns.sh
#sleep 10
docker container start $containerid
sleep 1
sudo -E $HOME/stacks/misc/scripts/startdns.sh

if [ -z "$containerid" ]
then
    echo "you dumbass"
    exit
fi

