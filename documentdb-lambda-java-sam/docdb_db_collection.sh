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

# MongoDB connection string
MONGO_CONNECTION_STRING="mongodb://${DOCDB_USERNAME}:${DOCDB_PASSWORD}@${DOCDB_ENDPOINT}:${DOCDB_PORT}/${DATABASE_NAME}?tls=true&tlsCAFile=${TLS_CERT_FILE}&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false"

# Create Database and Collection
echo "Connecting to DocumentDB and creating database: ${DATABASE_NAME} and collection: ${COLLECTION_NAME}..."

mongosh "${MONGO_CONNECTION_STRING}" --eval "
    use(\"${DATABASE_NAME}\");
    db.createCollection(\"${COLLECTION_NAME}\");
    print('Database and collection created successfully.');
"

if [ $? -eq 0 ]; then
    echo "Script executed successfully."
else
    echo "Error during script execution."
fi