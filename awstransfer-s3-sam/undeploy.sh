#!/bin/bash

echo "Enter a stack name"
read -r STACK_NAME

echo "Enter the desired AWS Region:"
read -r AWS_REGION


# delete the stack2
sam delete --stack-name "$STACK_NAME-2" --region $AWS_REGION

# delete the stack1
sam delete --stack-name "$STACK_NAME-1" --region $AWS_REGION