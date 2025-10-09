#!/bin/bash

# DocumentDB Connection Details
DOCDB_ENDPOINT="DOCDB_CLUSTER_ENDPOINT"
DOCDB_PORT="27017"
DOCDB_USERNAME="DOCDB_CLUSTER_ADMIN_USER"
DOCDB_PASSWORD="DOCDB_CLUSTER_PASSWORD"
TLS_CERT_FILE="/home/ec2-user/mongoshell/global-bundle.pem" # Path to your TLS certificate file if TLS is enabled

# Database and Collection Names
DATABASE_NAME="DOCDB_DATABASE"
COLLECTION_NAME="DOCDB_COLLECTION"

# Connect using Mongo Shell and create database and collection
mongosh --tls --tlsCAFile ${TLS_CERT_FILE} --username ${DOCDB_USERNAME} --password ${DOCDB_PASSWORD} --host ${DOCDB_ENDPOINT} --port ${DOCDB_PORT} --file mongodbcolcreate.js


# Connect to Mongo Shell
# mongosh --tls --tlsCAFile /home/ec2-user/mongoshell/global-bundle.pem --username DOCDB_CLUSTER_ADMIN_USER --password DOCDB_CLUSTER_PASSWORD --host DOCDB_CLUSTER_ENDPOINT --port 27017