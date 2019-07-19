#!/bin/bash

#docker-compose -f ${USERDIR}/stacks/media-services.yml up -d
#-f docker-compose.yml

pushd ${USERDIR}/stacks/network
echo ${PWD}
docker-compose pull
docker-compose up -d

pushd ${USERDIR}/stacks/homeautomation
echo ${PWD}
docker-compose pull
docker-compose up -d

pushd ${USERDIR}/stacks/media
echo ${PWD}
docker-compose pull
docker-compose up -d

popd
