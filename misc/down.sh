#!/bin/bash

pushd ${USERDIR}/stacks/media
echo ${PWD}
docker-compose down

pushd ${USERDIR}/stacks/homeautomation
echo ${PWD}
docker-compose down

pushd ${USERDIR}/stacks/network
echo ${PWD}
docker-compose down

popd
