#!/bin/bash

# Generate random ID
USER_ID=$(LC_ALL=C tr -dc 'a-zA-Z0-9' </dev/urandom | fold -w 10 | head -n 1)

aws dynamodb put-item --table-name ServerlessLandUsers --item "{\"userId\": {\"S\": \"$USER_ID\"}}"

echo "Added user: $USER_ID"