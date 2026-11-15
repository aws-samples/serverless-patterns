#!/bin/bash

# Ask for ALB DNS input
read -p "Enter the Application Load Balancer DNS: " albdns

URL="http://${albdns}/books"


curl -X POST $URL \
-H 'Content-Type: application/json' \
-d '{
"title": "The Great Gatsby",
"author": "F. Scott Fitzgerald3",
"pageCount": 180,
"category": "Fiction"
}'

curl -X POST $URL \
-H 'Content-Type: application/json' \
-d '{
"title": "To Kill a Mockingbird",
"author": "Harper Lee",
"pageCount": 281,
"category": "Classic"
}'

curl -X POST $URL \
-H 'Content-Type: application/json' \
-d '{
"title": "The Catcher in the Rye",
"author": "J.D. Salinger",
"pageCount": 214,
"category": "Literature"
}'


curl -X POST $URL \
-H 'Content-Type: application/json' \
-d '{
"title": "Pride and Prejudice",
"author": "Jane Austen",
"pageCount": 226,
"category": "Romance"
}'


curl -X POST $URL \
-H 'Content-Type: application/json' \
-d '{
"title": "The Great Gatsby3",
"author": "F. Scott Fitzgerald3",
"pageCount": 180,
"category": "Fiction"
}'