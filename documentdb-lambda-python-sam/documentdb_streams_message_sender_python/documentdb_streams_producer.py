import sys
import csv
import json
from datetime import datetime

import boto3
from pymongo import MongoClient


def get_secret(secret_name):
    session = boto3.session.Session()
    region = session.region_name
    print(f"region = {region}")

    client = session.client(service_name="secretsmanager", region_name=region)
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])


def get_today_date():
    return datetime.now().strftime("%m-%d-%Y-%H-%M-%S")


def get_person_from_row(row, message_id):
    return {
        "_id": message_id,
        "Firstname": row[0],
        "Lastname": row[1],
        "Company": row[2],
        "Street": row[3],
        "City": row[4],
        "County": row[5],
        "State": row[6],
        "Zip": row[7],
        "HomePhone": row[8],
        "CellPhone": row[9],
        "Email": row[10],
        "Website": row[11],
    }


def main():
    if len(sys.argv) != 5:
        print(
            "Pass four parameters: 1 - DocumentDB Database Name, "
            "2 - DocumentDB Collection Name, "
            "3 - A string to be used as key for this batch of messages, "
            "4 - Number of Messages in this batch"
        )
        sys.exit(1)

    db_name = sys.argv[1]
    collection_name = sys.argv[2]
    message_key = f"{sys.argv[3]}-{get_today_date()}"
    number_of_messages = int(sys.argv[4])

    credentials = get_secret("AmazonDocumentDBCredentials")
    host = credentials["host"]
    port = credentials["port"]
    username = credentials["username"]
    password = credentials["password"]

    ca_file_path = "/home/ec2-user/mongoshell/global-bundle.pem"

    connection_string = (
        f"mongodb://{username}:{password}@{host}:{port}/sample-database"
        f"?ssl=true&replicaSet=rs0&readpreference=secondaryPreferred"
        f"&tlsCAFile={ca_file_path}&retryWrites=false"
    )

    print(f"Connection String = {connection_string}")

    client = MongoClient(connection_string)
    db = client[db_name]
    collection = db[collection_name]

    people = []
    with open(
        "/home/ec2-user/serverless-patterns/documentdb-lambda-python-sam/python/documentdb_streams_message_sender_python/us-500.csv",
        "r",
    ) as f:
        reader = csv.reader(f)
        for row in reader:
            people.append(row)

    messages_to_send = min(number_of_messages, len(people))

    for i in range(1, messages_to_send + 1):
        person = get_person_from_row(people[i - 1], f"{message_key}-{i}")
        print(f"Now going to insert a row in DynamoDB for messageID = {person['_id']}")
        collection.insert_one(person)
        print(f"Now done inserting a row in DynamoDB for messageID = {person['_id']}")

    client.close()


if __name__ == "__main__":
    main()
