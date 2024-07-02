#!/bin/bash
aws sqs send-message-batch \
    --queue-url <insert queue URL>\
    --entries file://send-messages-batch-1.json

aws sqs send-message-batch \
    --queue-url <insert queue URL> \
    --entries file://send-messages-batch-2.json