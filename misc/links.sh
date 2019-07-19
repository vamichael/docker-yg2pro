#!/bin/bash

pushd ${HOME}/stacks

#https://askubuntu.com/questions/322772/how-do-i-add-an-executable-to-my-search-path

ln -s ${HOME}/stacks/misc/upgrade.sh $HOME
ln -s ${HOME}/stacks/misc/up.sh $HOME
ln -s ${HOME}/stacks/misc/down.sh $HOME

popd

