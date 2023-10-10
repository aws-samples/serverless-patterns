#!/bin/sh -l
echo "New files $1"
echo "Modfied Files $2"

node /usr/src/app/cfn-nag-action/src/index.js $1 $2
exitcode=$?

echo "::set-output name=failed::$exitcode"

# Exit with value from node
exit $exitcode

