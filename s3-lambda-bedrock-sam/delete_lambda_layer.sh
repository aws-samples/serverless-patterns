#!/bin/bash

# Take Lambda Layer Name
read -p "Enter the name of the Layer: " layer_name

# Take Lambda Layer version
read -p "Enter the version of the Layer: " layer_version

# Take AWS Region
read -p "Enter the AWS Region: " aws_region

# Delete the layer:
echo "Deleting the layer version. Please wait ..."
aws lambda delete-layer-version --layer-name $layer_name --version-number $layer_version --region $aws_region
