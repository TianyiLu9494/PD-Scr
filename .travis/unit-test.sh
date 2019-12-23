#!/bin/bash

set -e
errors=0

# Run unit tests
python PD-Scr/PD-Scr_test.py || {
    echo "'python python/PD-Scr/PD-Scr_test.py' failed"
    let errors+=1
}

# Check program style
pylint -E PD-Scr/*.py || {
    echo 'pylint -E PD-Scr/*.py failed'
    let errors+=1
}

[ "$errors" -gt 0 ] && {
    echo "There were $errors errors found"
    exit 1
}

echo "Ok : Python specific tests"
