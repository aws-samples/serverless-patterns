#!/bin/bash

set -a

echo "************Creating a 1GB file with Current date & time stamp************"
cd /efs
dd if=/dev/zero of=file.txt.$(date +%Y%m%d%H%M%S) bs=1M count=1024
echo ""

echo "************Updating the Bread Crumb file************"
echo "This is a sample created on EFS Mount & Update by Container at $(date)" >> /efs/sample-file.log
echo "" >>/efs/sample-file.log
