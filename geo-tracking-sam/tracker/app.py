from datetime import datetime
import json
import os

import boto3

# Update this to match the name of your Tracker resource
#TRACKER_NAME = "FilterDemoDistance"

"""
This Lambda function receives a payload from your location services APP and updates to
Amazon Location Service via the BatchUpdateDevicePosition API.

Parameter 'event' is the payload.

In this sample, we assume that the payload has a single top-level key 'payload' and a nested key
'location' with keys 'lat' and 'long'. We also assume that the name of the device is nested in
the payload as 'deviceid'. Finally, the timestamp of the payload is present as 'timestamp'. For
example:

>>> event
{
  "deviceId": "ltgAj8Tjc",
  "filtering": "Distance",
  "accuracy": 0
  "location": {
    "latitude": 39.234025770276254,
    "longitude": -94.55351482022044
  },
  "timestamp": "2022-08-26T15:39:18"
}

If your data doesn't match this schema, please modify this to match your app
format for the data before delivering it to this Lambda function, or you can modify the code below to
match it.
"""
def lambda_handler(event, context):
    if event["filtering"] == "Distance":
        TRACKER_NAME = "DistanceFilteringTracker"
        accuracy = 0
    elif event["filtering"] == "Time":
        TRACKER_NAME = "TimeFilteringTracker"
        accuracy = 0
    else:
        TRACKER_NAME = "AccuracyFilteringTracker"
        accuracy = event["accuracy"]
    update = {
      "DeviceId": event["deviceId"],
      "SampleTime": event["timestamp"],
      "Accuracy": {
          "Horizontal": accuracy
      },
      "Position": [
        event["location"]["longitude"],
        event["location"]["latitude"]
        ],
      "PositionProperties": {
        "Filtering": event["filtering"]
      }
    }
    client = boto3.client("location")
    response = client.batch_update_device_position(TrackerName=TRACKER_NAME, Updates=[update])