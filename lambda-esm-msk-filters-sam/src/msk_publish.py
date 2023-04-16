import json
import KafkaClient from kafka
import SimpleProducer from kafka
import KafkaProducer from kafka

def lambda_handler(event, context):
    kafka = KafkaClient("XXXX.XXX.XX.XX:XXXX")
    print(kafka)
    producer = SimpleProducer(kafka, async = True)
    print(producer)
    task_op = {
        "message": "Hello world"
    }
    print(json.dumps(task_op))
    producer.send_messages("topic_atx_ticket_update",json.dumps(task_op).encode('utf-8'))
    print(producer.send_messages)
    return ("Messages Sent to Kafka Topic")