import json
import ssl
import pika
import os
import requests

headers = {"X-Aws-Parameters-Secrets-Token": os.environ.get('AWS_SESSION_TOKEN')}


def lambda_handler(event, context):
    messageBody = json.dumps(event['messageBody'])
    host = event['host']
    secret = event['secret']
    appId = event['appId']

    secrets_extension_endpoint = "http://localhost:2773/secretsmanager/get?secretId=" + secret
    r = requests.get(secrets_extension_endpoint, headers=headers)
    creds = json.loads(json.loads(r.text)['SecretString'])


    # SSL Context for TLS configuration of Amazon MQ for RabbitMQ
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

    url = f"amqps://{creds['username']}:{creds['password']}@{host}:5671"
    parameters = pika.URLParameters(url)
    parameters.ssl_options = pika.SSLOptions(context=ssl_context)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    props = pika.BasicProperties(app_id=appId)
    for queueName in  event['queues']:
        channel.queue_declare(queue=queueName)
        channel.basic_publish(exchange='', routing_key=queueName, body=messageBody, properties=props)
        print(" [x] Message sent to queue: ", queueName)
    channel.close()
    connection.close()
    return {
        'statusCode': 200,
        'body': json.dumps(f"Posted {len(event['queues'])} messages!")
    }


