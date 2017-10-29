#!/bin/bash
set -e

# install dependencies
ansible-galaxy install -r requirements.txt --force
