#!/bin/bash
set -e

# install dependencies
ansible-galaxy install -r requirements.txt --force
mkdir -p lookup_plugins/ansible-vault
git clone https://github.com/jhaals/ansible-vault.git lookup_plugins/ansible-vault
