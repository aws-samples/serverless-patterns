#!/bin/bash

# Connect to Mongo Shell
mongosh --tls --tlsCAFile /home/ec2-user/mongoshell/global-bundle.pem --username DOCDB_CLUSTER_ADMIN_USER --password DOCDB_CLUSTER_PASSWORD --host DOCDB_CLUSTER_ENDPOINT --port 27017