#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import os
import sys
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
from threading import Event, Thread
from datetime import datetime
from queue import Queue

lib_folder = Path(__file__).parent / "lib"
sys.path.insert(0,str(lib_folder))

import requests
import boto3

LAMBDA_EXTENSION_NAME = os.path.basename(__file__)
HOST_NAME = "sandbox"
# LOCAL_DEBUGGING_IP = "0.0.0.0"
HOST_PORT = 8080
LAMBDA_AGENT_IDENTIFIER_HEADER_KEY = "Lambda-Extension-Identifier"
s3_bucket = (os.environ['S3_BUCKET_NAME'])
s3 = boto3.resource('s3')
extension_id = ""
pending_queue = Queue()

class TelemetryHTTPHandler(BaseHTTPRequestHandler): 
    def do_POST(self):
        try:
            cl = self.headers.get("Content-Length")
            if cl:
                data_len = int(cl)
            else:
                data_len = 0
            content = self.rfile.read(data_len)
            self.send_response(200)
            self.end_headers()
            msg = json.loads(content.decode("utf-8"))
            print(f"Incoming message ={msg}")
            pending_queue.put(msg)
        except Exception as e:
            print(f"Error processing message: {e}")

def push_log_to_s3(msg):
    s3_filename = (os.environ['AWS_LAMBDA_FUNCTION_NAME'])+'-'+(datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f'))+'.log'
    try:
        response = s3.Bucket(s3_bucket).put_object(Key=s3_filename, Body=str(msg))
        # print(f"ResponseS3 = {response}")
    except Exception as e:
        raise Exception(f"Error sending log to S3 {e}") from e


def register_extension():
    print(f"[{LAMBDA_EXTENSION_NAME}] Registering...", flush=True)
    headers = {
        'Lambda-Extension-Name': LAMBDA_EXTENSION_NAME,
    }
    payload = {
        'events': [
            'INVOKE',
            'SHUTDOWN'
        ],
    }
    response = requests.post(
        url=f"http://{os.environ['AWS_LAMBDA_RUNTIME_API']}/2020-01-01/extension/register",
        json=payload,
        headers=headers
    )
    print(response)
    ext_id = response.headers[LAMBDA_AGENT_IDENTIFIER_HEADER_KEY]
    print(f"[{LAMBDA_EXTENSION_NAME}] Registered with ID: {ext_id}", flush=True)

    return ext_id


def process_events(ext_id):
    headers = {
        LAMBDA_AGENT_IDENTIFIER_HEADER_KEY: ext_id
    }
    while True:
        print(f"[{LAMBDA_EXTENSION_NAME}] Waiting for event...", flush=True)
        response = requests.get(
            url=f"http://{os.environ['AWS_LAMBDA_RUNTIME_API']}/2020-01-01/extension/event/next",
            headers=headers,
            timeout=None
        )
        event = json.loads(response.text)
        if event['eventType'] == 'SHUTDOWN':
            print(f"[{LAMBDA_EXTENSION_NAME}] Received SHUTDOWN event. Exiting.", flush=True)
            sys.exit(0)
        else:
            execute_custom_processing(event)

def execute_custom_processing(event):
    # perform custom per-event processing here
    print(f"[{LAMBDA_EXTENSION_NAME}] Received event: {json.dumps(event)}", flush=True)
    while not pending_queue.empty():
        msg = pending_queue.get_nowait()
        push_log_to_s3(msg)

def subscribe_telemetry_api(ext_id):
    print(f"Start telemetry api subscription")
    TIMEOUT_MS = 1000 # Maximum time (in milliseconds) that a batch is buffered.
    MAX_BYTES = 262144 # Maximum size in bytes that the logs are buffered in memory.
    MAX_ITEMS = 10000 # Maximum number of events that are buffered in memory.

    subscription_body = {
        "schemaVersion": "2022-07-01",
        "destination":{
            "protocol": "HTTP",
            "URI": f"http://{HOST_NAME}:{HOST_PORT}",
        },
        "types": ["platform", "function"],
        "buffering": {
            "timeoutMs": TIMEOUT_MS,
            "maxBytes": MAX_BYTES,
            "maxItems": MAX_ITEMS
        }

    }
    endpoint =  f"http://{os.environ['AWS_LAMBDA_RUNTIME_API']}/2022-07-01/telemetry"
    req = urllib.request.Request(endpoint)
    req.method = 'PUT'
    req.add_header(LAMBDA_AGENT_IDENTIFIER_HEADER_KEY, ext_id)   
    req.add_header("Content-Type", "application/json")
    data = json.dumps(subscription_body).encode("utf-8")
    req.data = data
    resp = urllib.request.urlopen(req)    
    print(f"Subscription response code = {resp.status}")

def serve(started_event, server):
    # Notify that this thread is up and running
    started_event.set()
    try:
        print(f"extension.http_listener: Running HTTP Server on {HOST_NAME}:{HOST_PORT}")
        server.serve_forever()
    except:
        print(f"extension.http_listener: Error in HTTP server {sys.exc_info()[0]}", flush=True)
    finally:
        if server:
            server.shutdown()

def start_listener():
    webServer = HTTPServer((HOST_NAME, HOST_PORT), TelemetryHTTPHandler)

    started_event = Event()
    server_thread = Thread(target=serve, daemon=True, args=(started_event, webServer,))
    server_thread.start()
    rc = started_event.wait(timeout = 9)
    if rc is not True:
        raise Exception("server_thread has timed out before starting")

def main():
    #Prepare S3 bucket
    s3_bucket = (os.environ['S3_BUCKET_NAME'])
    s3 = boto3.resource('s3')
    #Start HTTP listener to listen to Telemetry API
    start_listener()
    # Register Extension API and Subscribe to Telemetry API with HTTP Listener which created previously 
    extension_id = register_extension()
    subscribe_telemetry_api(extension_id)
    #While HTTP Listener listen to Teleymetry API and put log to the queue, 
    #process events will check the queue and put the log to S3 and then send signal to Extension API for next event 
    process_events(extension_id)
    

if __name__ == "__main__":
    main()    