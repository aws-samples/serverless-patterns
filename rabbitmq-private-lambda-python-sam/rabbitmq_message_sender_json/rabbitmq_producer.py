import ssl
import sys
import json
import csv
import time
import os
from datetime import datetime

import pika
import boto3


def get_secret():
    secret_name = "AmazonRabbitMQCredentials"
    region = os.environ.get('AWS_REGION', os.environ.get('AWS_DEFAULT_REGION', 'us-west-2'))
    client = boto3.client('secretsmanager', region_name=region)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])
    return secret['username'], secret['password']


def read_data_file():
    data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'us-500.csv')
    people = []
    with open(data_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            people.append(row)
    return people


def get_person_from_row(row):
    return {
        'firstname': row[0],
        'lastname': row[1],
        'company': row[2],
        'street': row[3],
        'city': row[4],
        'county': row[5],
        'state': row[6],
        'zip': row[7],
        'homePhone': row[8],
        'cellPhone': row[9],
        'email': row[10],
        'website': row[11],
    }


def get_today_date():
    return datetime.now().strftime("%m-%d-%Y-%H-%M-%S")


def send_messages(endpoint, username, password, virtual_host, exchange, queue, seeder_key, num_messages):
    people = read_data_file()
    num_to_send = min(num_messages, len(people))

    ssl_context = ssl.create_default_context()
    ssl_options = pika.SSLOptions(ssl_context)

    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(
        host=endpoint,
        port=5671,
        virtual_host=virtual_host,
        credentials=credentials,
        ssl_options=ssl_options,
    )

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)
    channel.queue_declare(queue=queue, durable=True)
    channel.queue_bind(queue=queue, exchange=exchange, routing_key=f"{exchange}-{queue}")

    for i in range(1, num_to_send + 1):
        person = get_person_from_row(people[i])
        person_json = json.dumps(person)

        headers = {
            'MessageBatchIdentifier': seeder_key,
            'MessageNumberInBatch': i,
        }

        properties = pika.BasicProperties(
            app_id='rabbitmq.producer.PythonRabbitMQProducer',
            cluster_id=endpoint,
            content_encoding='UTF-8',
            content_type='text/plain',
            correlation_id=f"{seeder_key}-{i}",
            delivery_mode=2,
            expiration='60000',
            headers=headers,
            message_id=f"{seeder_key}:{i}",
            priority=1,
            timestamp=int(time.time()),
            type='PythonRabbitMQProducer',
            user_id=username,
        )

        channel.basic_publish(
            exchange=exchange,
            routing_key=f"{exchange}-{queue}",
            body=person_json.encode('utf-8'),
            properties=properties,
        )
        print(f"Sent out one message - Number {i} at time = {int(time.time() * 1000)}")

    connection.close()


def main():
    if len(sys.argv) < 7:
        print("Usage: python rabbitmq_producer.py <endpoint> <virtual_host> <exchange> <queue> <seeder_key> <num_messages>")
        sys.exit(1)

    endpoint = sys.argv[1]
    virtual_host = sys.argv[2]
    exchange = sys.argv[3]
    queue = sys.argv[4]
    seeder_key = sys.argv[5] + "-" + get_today_date()
    num_messages = int(sys.argv[6])

    username, password = get_secret()
    send_messages(endpoint, username, password, virtual_host, exchange, queue, seeder_key, num_messages)


if __name__ == '__main__':
    main()
