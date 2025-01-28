# Creating script for getting AWS Keys needed to set-up CLI profile on local machine
#!/bin/bash

aws configure set aws_access_key_id $2 --profile $1

aws configure set aws_secret_access_key $3 --profile $1

aws configure set region $4 --profile $1