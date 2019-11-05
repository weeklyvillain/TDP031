#!/bin/bash
EXPECTED_NAME=$1
HOSTNAME=`hostname`
exit_code=0

if [ "$HOSTNAME" == "$EXPECTED_NAME" ]; then
    echo "Hostname setup correctly"
else
    echo "Expected hostname to be $EXPECTED_NAME but was $HOSTNAME"
    exit_code=1
fi
exit $exit_code