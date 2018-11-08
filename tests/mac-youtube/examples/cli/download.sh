#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[[ $OSTYPE != *"darwin"* ]] && echo "SKIP: not MacOS" && exit

set -- "https://www.youtube.com/watch?v=7M-jsjLB20Y"
( set -x; python -m mac_youtube.download "$@" )
