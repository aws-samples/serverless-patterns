    #Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#SPDX-License-Identifier: MIT-0

import json
import aurora_dsql_psycopg2 as dsql
import os

cluster_endpoint = os.environ['cluster_endpoint']
region = os.environ['AWS_REGION']

def lambda_handler(event, context):
    config = {
        'host': cluster_endpoint,
        'region': region,
        'user': "admin",
    }

    # Make a connection to the cluster
    conn = dsql.connect(**config)

    try:
        with conn.cursor() as cur:
            conn.commit()
    except Exception as e:
        conn.close()
        raise e

    conn.set_session(autocommit=True)

    cur = conn.cursor()
    
    cur.execute("DROP TABLE IF EXISTS users")
    
    cur.execute(b"""
        CREATE TABLE IF NOT EXISTS users(
            id uuid NOT NULL DEFAULT gen_random_uuid(),
            name varchar(30) NOT NULL,
            city varchar(80) NOT NULL,
            telephone varchar(20) DEFAULT NULL,
            PRIMARY KEY (id))"""
        )

    # Insert some rows
    cur.execute("INSERT INTO users(name, city, telephone) VALUES('John', 'LA', '555-555-0150')")

    # Read back what we have inserted
    cur.execute("SELECT * FROM users")
    row = cur.fetchone()
    print(row)

    # return JSON back to API Gateway
    return {
        'statusCode': 200,
        'body': json.dumps({
            'id': str(row[0]),
            'name': row[1],
            'city': row[2],
            'telephone': row[3]
        })
    }