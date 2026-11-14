#!/bin/bash

URL="http://localhost:8081/books"


curl $URL \
-H 'Content-Type: application/json' | jq
