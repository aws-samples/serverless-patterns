# API Gateway + Lambda SnapStart + DynamoDB (Python CDK)

This pattern demonstrates how to create a REST API using API Gateway, AWS Lambda and DynamoDB.
It's built with [Python 3.12](https://www.python.org/downloads/release/python-3128/), together with
[AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html) as the Infrastructure as Code solution. This pattern also implements the usage of [AWS Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)
to improve initialization performance of the Lambda, in case that there are libraries requiring more time to load into memory.

## Architecture

- API Gateway REST API (`prod` stage)
- AWS Lambda (Python 3.12)
- Lambda SnapStart enabled on published versions
- Lambda `live` alias integrated with API Gateway
- DynamoDB table with partition key `id`

## Endpoints

- `POST /cars`
- `GET /cars/{carId}`
- `PUT /cars/{carId}`
- `DELETE /cars/{carId}`

## Requirements

- Python 3.12+
- AWS CDK v2
- AWS credentials configured

## Deploy

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk bootstrap
cdk deploy
```

## Test

Get endpoint URL from stack outputs (`CarEndpoint`), then run:

```bash
ENDPOINT="<put-the-CarEndpoint-output-URL-here>"

curl --location --request POST "$ENDPOINT/cars" \
  --header 'Content-Type: application/json' \
  --data-raw '{"make":"Porsche","model":"992","year":"2022","color":"White"}'
```