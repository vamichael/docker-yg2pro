#!/bin/bash



pushd $HOME

grep -rnw $HOME -e $1

popd
