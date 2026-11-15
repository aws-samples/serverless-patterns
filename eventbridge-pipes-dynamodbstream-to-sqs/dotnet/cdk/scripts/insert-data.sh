
#!/bin/bash

# Usage: This script inserts 10 items into the DyanmoDB table with a random primary key.

# Set the number of dynamodb items to create
COUNT=10

# Loop through and generate the specified number dynamodb items
for i in $(seq 1 $COUNT)
do
    ITEM_KEY=$RANDOM
    echo "Inserting item with PK of $ITEM_KEY"
    aws dynamodb put-item --table-name dynamo-pipes-to-sqs --item "{\"PK\":{\"S\":\"$ITEM_KEY\"}}"
done