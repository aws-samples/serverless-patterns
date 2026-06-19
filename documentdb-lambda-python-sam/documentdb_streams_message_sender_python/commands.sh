#!/bin/bash

# Pass a random string as the first command-line argument to this shell script. It will be used to uniquely identify a batch of messages
# Pass an integer as the second command-line argument to this shell script < 500. For example if you want to send 100 messages, pass 100
# Example sh commands.sh firstbatch 100

PYTHON3_VERSION /home/ec2-user/serverless-patterns/documentdb-lambda-python-sam/documentdb_streams_message_sender_python/documentdb_streams_producer.py DOCDB_DATABASE DOCDB_COLLECTION $1 $2
