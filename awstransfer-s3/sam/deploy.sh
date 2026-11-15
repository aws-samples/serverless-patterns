#!/bin/bash

# Take the stack name
echo "Enter a stack name"
read -r STACK_NAME

# Take the desired AWS Region
echo "Enter the desired AWS Region:"
read -r AWS_REGION


USER_NAME="sftpuser"

# Generate key-pair
# AWS Documentation: https://docs.aws.amazon.com/transfer/latest/userguide/configure-sftp-connector.html#format-sftp-connector-key
ssh-keygen -t rsa -b 4096 -m PEM -f $USER_NAME -N ""

# Check if the public key file exists
if [ -f "$USER_NAME.pub" ]; then

    # Store the content of the public key in a variable
    PUBLIC_KEY=$(cat "$USER_NAME.pub")

    # Deploy template-sftp-server.yaml
    sam deploy \
      --template-file template-sftp-server.yaml \
      --stack-name "$STACK_NAME-1" \
      --parameter-overrides "UserName=\"$USER_NAME\"" "SSHPublicKey=\"$PUBLIC_KEY\"" \
      --capabilities CAPABILITY_IAM \
      --region $AWS_REGION

    # Get the stack ID
    STACK_ID=$(aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --query "StackSummaries[?contains(StackName, '$STACK_NAME-1')].StackId" --output text --region $AWS_REGION)

    # Check if the stack ID is empty
    if [ -z "$STACK_ID" ]; then
        echo "Stack not found. Exiting..."
        exit 1
    fi

    # Get the stack outputs
    OUTPUTS=$(aws cloudformation describe-stacks --stack-name "$STACK_ID" --query "Stacks[0].Outputs" --output json --region $AWS_REGION)

    # Get a TransferServerId output value
    TRANSFER_SERVER_ID=$(echo "$OUTPUTS" | jq -r '.[] | select(.OutputKey == "TransferServerId") | .OutputValue')

    # Get a TransferServerEndpoint output value
    TRANSFER_SERVER_ENDPOINT=$(echo "$OUTPUTS" | jq -r '.[] | select(.OutputKey == "TransferServerEndpoint") | .OutputValue')

    # Get a TransferLoggingRoleArn output value
    TRANSFER_LOGGING_ROLE_ARN=$(echo "$OUTPUTS" | jq -r '.[] | select(.OutputKey == "TransferLoggingRoleArn") | .OutputValue')

    # Get a SSHPrivateKey in single line without double quotes
    # AWS Documentation: https://docs.aws.amazon.com/transfer/latest/userguide/sftp-connectors-tutorial.html
    FORMATTED_PK=$(jq -sR . < "$USER_NAME"| sed 's/^"//;s/"$//')

    # Wait for the server to be ready
    STATE="NOT_AVAILABLE"

    # Loop until the server is available
    while [ "$STATE" != "ONLINE" ]; do
        # Get the server state using the AWS CLI
        STATE=$(aws transfer describe-server --server-id "$TRANSFER_SERVER_ID" --query "Server.State" --output text)

        # Print the server state
        echo "Server state: $STATE"

        # Wait for 1 minute before checking again
        sleep 60
    done

    # Print a message when the server is available
    echo "Server is online! Proceesing with the next steps..."

    # Get the TrustedHostKey from the TransferServer
    # AWS Documentation: https://docs.aws.amazon.com/transfer/latest/userguide/API_SftpConnectorConfig.html
    TRUSTED_HOST_KEY=$(ssh-keyscan $TRANSFER_SERVER_ENDPOINT)

    # Deploy template-sftp-connector.yaml
    sam deploy \
    --template-file template-sftp-connector.yaml \
    --stack-name "$STACK_NAME-2" \
    --parameter-overrides "TransferServerEndpoint=\"sftp://$TRANSFER_SERVER_ENDPOINT\"" "UserName=\"$USER_NAME\"" "TransferLoggingRoleArn=\"$TRANSFER_LOGGING_ROLE_ARN\"" "SSHPrivateKey=\"$FORMATTED_PK\"" "TrustedHostKeys=\"$TRUSTED_HOST_KEY\"" \
    --capabilities CAPABILITY_IAM \
    --region $AWS_REGION

else
    echo "Public key file not found. Exiting..."
    exit 1
fi
