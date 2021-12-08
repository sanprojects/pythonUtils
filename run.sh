#!/usr/bin/env bash

#set -o errexit
set -o pipefail
set -o nounset
# set -x # show running commands

help() {
    echo "Usage: $0 COMMAND" >&2
    echo "Commands:"
    declare -F | sed "s/declare -f/ /g"
}

install() {
    pip3 install -r requirements.txt
}

updateRequirements() {
  pip3 freeze > requirements.txt && cat  requirements.txt
}

tests() {
  pytest
}


${1:-help} "${@:2}" || help