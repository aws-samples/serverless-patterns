import json
from dataclasses import dataclass
from typing import Generator

import boto3
import moto
import pytest
from boto3.dynamodb.table import TableResource
from boto3.resources.base import ServiceResource
from botocore.client import BaseClient

STAGE = "dev"
TABLE_NAME = f"citation-mapping-table-{STAGE}"
EVENT_BUS_NAME = f"event-bus-{STAGE}"
HOME_REGION = "us-west-2"
KB_MAPPING_LIST = {"documentation": "test-1234", "documentation1": "test-1234"}


@dataclass
class BotoClientMock:
    """Contains a generic mocked Boto Client."""

    client: BaseClient


@pytest.fixture(autouse=True)
def set_env_vars(monkeypatch):
    monkeypatch.setenv("CITATION_MAPPING_TABLE_NAME", TABLE_NAME)
    monkeypatch.setenv("AWS_REGION", HOME_REGION)
    monkeypatch.setenv("SNS_TOPIC", "arn:aws:sns:us-west-2:123456789012:operational-issues")
    monkeypatch.setenv("EVENT_BUS_NAME", EVENT_BUS_NAME)
    monkeypatch.setenv("KB_MAPPING_LIST", json.dumps(KB_MAPPING_LIST))


@pytest.fixture(scope="function")
def sns_mock() -> Generator[BotoClientMock, None, None]:
    """Return a class containing a mocked boto sns Client."""
    with moto.mock_aws():
        mock_sns_client = boto3.client("sns", region_name="us-west-2")
        mock_sns_client.create_topic(Name="operational-issues")
        yield BotoClientMock(client=mock_sns_client)


@pytest.fixture
def mock_events():
    with moto.mock_aws():
        events = boto3.client("events", region_name="us-west-2")
        try:
            # Create event bus
            events.create_event_bus(Name=EVENT_BUS_NAME)
        except events.exceptions.ResourceAlreadyExistsException:
            pass

        yield events


@dataclass
class DynamoDBMock:
    """Contains a Moto DynamoDB Mock object with a boto resource and boto table interface."""

    resource: ServiceResource
    client: BaseClient
    table: TableResource = None

    # def __post_init__(self):
    #     """Initialize the DynamoDB Mock Object."""
    #     self.table = self.resource.Table(TABLE_NAME)


@pytest.fixture(scope="class", autouse=True)
def sts_mock() -> Generator[BaseClient, None, None]:
    """Mock the STS Service."""
    with moto.mock_aws():
        mock_sts_client = boto3.client("sts", HOME_REGION)
        yield mock_sts_client


@pytest.fixture(scope="function")
def dynamodb_mock():
    """Mock the DynamoDB Service."""
    with moto.mock_aws():
        mock_dynamodb_resource = boto3.resource("dynamodb", region_name="us-west-2")
        mock_dynamodb_client = boto3.client("dynamodb", region_name="us-west-2")

        # Check if table exists and delete it if it does
        try:
            existing_table = mock_dynamodb_resource.Table(TABLE_NAME)
            existing_table.delete()
            existing_table.wait_until_not_exists()
        except mock_dynamodb_client.exceptions.ResourceNotFoundException:
            pass
        # Create the table with GSI
        table = mock_dynamodb_resource.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {"AttributeName": "SourceSystem", "KeyType": "HASH"},
                {"AttributeName": "S3ObjectURI", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "SourceSystem", "AttributeType": "S"},
                {"AttributeName": "S3ObjectURI", "AttributeType": "S"},
                {"AttributeName": "Status", "AttributeType": "S"},
            ],
            GlobalSecondaryIndexes=[
                {
                    "IndexName": "StatusIndex",
                    "KeySchema": [{"AttributeName": "Status", "KeyType": "HASH"}],
                    "Projection": {"ProjectionType": "ALL"},
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 500,
                        "WriteCapacityUnits": 500,
                    },
                }
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 500, "WriteCapacityUnits": 500},
        )

        # Wait for table to be active
        table.meta.client.get_waiter("table_exists").wait(TableName=TABLE_NAME)

        yield DynamoDBMock(resource=mock_dynamodb_resource, client=mock_dynamodb_client, table=table)


@pytest.fixture(scope="function")
def seed_mapping_data(dynamodb_mock):
    items = [
        {"S3ObjectURI": "s3://documentation/content/almsc/faq1.md", "SourceSystem": "GITHUB", "Status": "PENDING"},
        {"S3ObjectURI": "s3://documentation/content/almsc/faq2.md", "SourceSystem": "GITHUB", "Status": "PENDING"},
        {"S3ObjectURI": "s3://documentation/content/almsc/faq3.md", "SourceSystem": "GITHUB", "Status": "PENDING"},
        {"S3ObjectURI": "s3://documentation/content/almsc/faq4.md", "SourceSystem": "GITHUB", "Status": "PENDING"},
        {
            "S3ObjectURI": "s3://documentation/content/almsc/faq5.md",
            "SourceSystem": "GITHUB",
            "Status": "MAPPING_COMPLETED",
        },
    ]
    with dynamodb_mock.table.batch_writer() as batch:
        for item in items:
            batch.put_item(
                Item={"SourceSystem": item["SourceSystem"], "S3ObjectURI": item["S3ObjectURI"], "Status": item["Status"]}
            )
    yield
