#!/bin/bash

set -a

echo "hello world from the shell script in ${ENV} environment for ${ORGANIZATION} Org"
echo " "
echo "Executing ls command at : $(date)"
ls -l