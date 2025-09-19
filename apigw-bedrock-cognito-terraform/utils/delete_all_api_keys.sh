for api_key_id in $(aws apigateway get-api-keys --query 'items[*].id' --output text); do
    echo  "Deleting API key $api_key_id"
    aws apigateway delete-api-key --api-key $api_key_id
done