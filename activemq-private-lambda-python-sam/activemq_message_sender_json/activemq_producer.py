import csv
import io
import json
import sys
import time
from datetime import datetime
from pathlib import Path

import boto3
import requests
import stomp


def get_region():
    session = boto3.session.Session()
    if session.region_name:
        return session.region_name
    token = requests.put(
        "http://169.254.169.254/latest/api/token",
        headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
        timeout=2,
    ).text
    az = requests.get(
        "http://169.254.169.254/latest/meta-data/placement/availability-zone",
        headers={"X-aws-ec2-metadata-token": token},
        timeout=2,
    ).text
    return az[:-1]


def get_credentials():
    secret_name = "AmazonActiveMQCredentials"
    region = get_region()
    print(f"region = {region}")
    client = boto3.client(service_name="secretsmanager", region_name=region)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])
    return secret["username"], secret["password"]


def read_data_file():
    data_file = Path(__file__).parent / "us-500.csv"
    people = []
    with open(data_file, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            people.append(row)
    return people


def get_person_from_row(row):
    return {
        "firstname": row[0],
        "lastname": row[1],
        "company": row[2],
        "street": row[3],
        "city": row[4],
        "county": row[5],
        "state": row[6],
        "zip": row[7],
        "homePhone": row[8],
        "cellPhone": row[9],
        "email": row[10],
        "website": row[11],
    }


class ReceiptListener(stomp.ConnectionListener):
    def __init__(self):
        self.receipts = {}

    def on_receipt(self, frame):
        receipt_id = frame.headers.get("receipt-id")
        if receipt_id:
            self.receipts[receipt_id] = True


def send_messages(endpoint, username, password, queue_name, seeder_key, number_of_messages):
    people = read_data_file()
    num_to_send = min(number_of_messages, len(people) - 1)

    host_port_pairs = []
    for ep in endpoint.replace("failover:(", "").replace(")", "").split(","):
        ep = ep.strip().replace("stomp+ssl://", "").replace("ssl://", "")
        host, port = ep.split(":")
        host_port_pairs.append((host, int(port)))

    conn = stomp.Connection(host_and_ports=host_port_pairs)
    conn.set_ssl(for_hosts=host_port_pairs)
    listener = ReceiptListener()
    conn.set_listener("receipt", listener)
    conn.connect(username, password, wait=True)

    today = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    message_key = f"{seeder_key}-{today}"

    for i in range(1, num_to_send + 1):
        person = get_person_from_row(people[i])
        person_json = json.dumps(person)
        receipt_id = f"msg-{i}"
        headers = {
            "correlation-id": f"{message_key}-{i}",
            "type": "TextMessage",
            "persistent": "true",
            "receipt": receipt_id,
            "MessageBatchIdentifier": message_key,
            "MessageNumberInBatch": str(i),
        }
        conn.send(destination=f"/queue/{queue_name}", body=person_json, headers=headers)

        timeout = 10
        start = time.time()
        while receipt_id not in listener.receipts:
            if time.time() - start > timeout:
                print(f"WARNING: No receipt for message {i} after {timeout}s")
                break
            time.sleep(0.01)

        current_time = int(time.time() * 1000)
        print(f"Sent out one message - Number {i} at time = {current_time}")

    conn.disconnect()


def main():
    if len(sys.argv) != 5:
        print("Usage: python activemq_producer.py <endpoint> <queue_name> <seeder_key> <number_of_messages>")
        sys.exit(1)

    endpoint = sys.argv[1]
    queue_name = sys.argv[2]
    seeder_key = sys.argv[3]
    number_of_messages = int(sys.argv[4])

    username, password = get_credentials()
    send_messages(endpoint, username, password, queue_name, seeder_key, number_of_messages)


if __name__ == "__main__":
    main()
