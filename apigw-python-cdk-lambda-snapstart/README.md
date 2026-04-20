# Amazon API Gateway + AWS Lambda SnapStart + Amazon DynamoDB

This pattern demonstrates how to create a REST API using Amazon API Gateway, AWS Lambda and Amazon DynamoDB.
It's built with [Python 3.12](https://www.python.org/downloads/release/python-3128/), together with
[AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html) as the Infrastructure as Code solution. This pattern also implements the usage of [AWS Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)
to improve initialization performance of the Lambda function.

## Architecture

- API Gateway REST API (`prod` stage)
- AWS Lambda functon(Python 3.12)
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

To deploy this stack, run the following commands from the root of the `serverless-patterns` repository:

```bash
# Move to the pattern directory and create a Python virtual environment
cd apigw-python-cdk-lambda-snapstart
python3 -m venv .venv
source .venv/bin/activate

# Install the AWS CDK for Python
pip3 install -r requirements.txt

# Install AWS Lambda Powertools library for the CarHandler Lambda
pip3 install -r CarHandler/requirements.txt -t CarHandler/

# Bootstrap your environment and deploy
cdk bootstrap
cdk deploy
```

## Test

Get endpoint URL from stack outputs (`CarEndpoint`), then run:

```bash
ENDPOINT="<put-the-CarEndpoint-output-URL-here>"

# Create a car (use the returned "id" in the response for GET/PUT/DELETE below)
curl --location --request POST "$ENDPOINT/cars" \
  --header 'Content-Type: application/json' \
  --data-raw '{"make":"Porsche","model":"992","year":"2022","color":"White"}'

# Get a car by id
curl --location "$ENDPOINT/cars/<car-id>"

# Update a car
curl --location --request PUT "$ENDPOINT/cars/<car-id>" \
  --header 'Content-Type: application/json' \
  --data-raw '{"make":"Porsche","model":"992","year":"2023","color":"Racing Yellow"}'

# Delete a car
curl --location --request DELETE "$ENDPOINT/cars/<car-id>"
```