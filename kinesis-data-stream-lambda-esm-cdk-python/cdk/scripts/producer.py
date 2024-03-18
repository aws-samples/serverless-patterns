import datetime
import json
import random
import uuid
import boto3


# Change the stream name per your testing requirements
STREAM_NAME = "stream-lambda-esm-filter"
MAX_RECORDS = 10

def get_data():

    return {
        "EVENT_TIME": datetime.datetime.now().isoformat(),
        "SENSOR_ID": "{}".format(uuid.uuid4()),
        "VALUE": round(random.random() * 100, 2),
        "STATUS": random.choice(["OK", "FAIL", "WARN"])
    }


def generate(stream_name, kinesis_client):
    for _ in range(0, MAX_RECORDS):
        data = get_data()
        print(data)
        
        kinesis_client.put_record(
            StreamName=stream_name, Data=json.dumps(data),
            PartitionKey="myPartitionKey" #random.choice(["pk1", "pk2", "pk3", "pk4"])
        )


if __name__ == "__main__":
    generate(STREAM_NAME, boto3.client("kinesis"))
