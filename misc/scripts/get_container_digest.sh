#!/bin/bash

CONTAINER_NAME=$1

fullimage=$(docker container ls | grep $CONTAINER_NAME | awk '{print $2}')
image=$(echo $fullimage | awk '{split($0,a,":"); print a[1]}')
tag=$(echo $fullimage | awk '{split($0,a,":"); print a[2]}')

if [ "$tag" == "" ]
then
    tag="latest"
fi

digest=$(docker images --digests | grep $image)
digest=$(echo $digest | grep $tag)
digest=$(echo $digest | awk '{print $1}{print $2}{print $3}')

echo $digest
