#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[[ $OSTYPE != *"darwin"* ]] && echo "SKIP: not MacOS" && exit

( set -x; python -m mac_youtube.playing )
