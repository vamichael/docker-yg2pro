#!/bin/bash
pushd ~/stacks/network/traefik/acme
rm acme.json
touch acme.json
chmod 600 acme.json
popd

