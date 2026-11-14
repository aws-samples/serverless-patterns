#!/bin/bash

# Ask for bookId input
read -p "Enter bookId to delete: " bookId

url="http://localhost:8081/books/${bookId}"

response=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE $url)

if [ $response -eq 204 ]; then
  echo "Book $bookId deleted successfully" 
elif [ $response -eq 404 ]; then
  echo "Error: Book $bookId not found"
else
  echo "Error: Failed to delete book $bookId (Status $response)"  
fi