#!/bin/bash

# Ask for ALB DNS input
read -p "Enter the Application Load Balancer DNS: " albdns

URL="http://${albdns}/books"

curl $URL \
-H 'Content-Type: application/json' | jq
