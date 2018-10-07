#!/usr/bin/env bash
{ set +x; } 2>/dev/null

url="https://raw.githubusercontent.com/python-tests/run/master/run.sh"
( set -x -o pipefail; curl -fLs "$url" | bash -s )
