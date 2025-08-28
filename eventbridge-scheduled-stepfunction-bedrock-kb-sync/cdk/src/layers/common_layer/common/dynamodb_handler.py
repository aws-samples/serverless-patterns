import logging
import time
from dataclasses import dataclass
from typing import Dict, List

import boto3
from boto3.dynamodb.conditions import AttributeNotExists, Key
from botocore.exceptions import ClientError
from schema import Schema

from .utils import MAPPING_STATUS

ITEM_SCHEMA = Schema(
    {
        "S3BucketName": str,
        "MappingSourceUrl": str,
        "MappingProductNames": str,
        "MappingStatus": str,
        "CreatedBy": str,
        "CreatedAt": str,
    }
)

log = logging.getLogger()
log.setLevel(logging.INFO)

PART_KEY_NAME = "SourceSystem"
SORT_KEY_NAME = "S3ObjectURI"
PART_STATUS_KEY_NAME = "MappingStatus"


class DynamoDBException(Exception):
    """Generic Error for signifying DynamoDB lookup errors"""


@dataclass
class ItemTypes:
    """Contains Allowed SOURCE SYSTEM Types in the CITATION MAPPING table"""

    GIT_HUB = "GITHUB"
    SITE_CORE = "SITECORE"


class DynamoDBHandler:
    """Contains methods to help interface with Authorization DynamoDB Table"""

    def __init__(
        self,
        table_name: str,
        dynamodb_table=None,
        dynamodb_resource: boto3.resource = None,
        dynamodb_client: boto3.client = None,
        session: boto3.Session = None,
    ) -> None:
        self._dynamodb_table = dynamodb_table
        self._dynamodb_resource = dynamodb_resource
        self._dynamodb_client = dynamodb_client
        self._session = session
        self.table_name = table_name

    @property
    def dynamodb_resource(self):
        if self._dynamodb_resource is None:
            session = self._session or boto3.Session()
            self._dynamodb_resource = session.resource("dynamodb", "us-west-2")
        return self._dynamodb_resource

    @property
    def dynamodb_client(self):
        if self._dynamodb_client is None:
            session = self._session or boto3.Session()
            self._dynamodb_client = session.client("dynamodb", "us-west-2")
        return self._dynamodb_client

    @property
    def dynamodb_table(self):
        return self.dynamodb_resource.Table(self.table_name)

    def get_all_pending_status(self, status: str) -> [dict]:
        """Returns the items from citation metadata table"""

        response = self.dynamodb_table.query(
            IndexName="StatusIndex",
            KeyConditionExpression=Key(PART_STATUS_KEY_NAME).eq(status),
            ProjectionExpression="SourceSystem, S3ObjectURI",
        )

        data = response["Items"]
        # LastEvaluatedKey indicates that there are more results
        while "LastEvaluatedKey" in response:
            response = self.dynamodb_table.query(
                IndexName="StatusIndex",
                ExclusiveStartKey=response["LastEvaluatedKey"],
                KeyConditionExpression=Key(PART_STATUS_KEY_NAME).eq(status),
                ProjectionExpression="SourceSystem, S3ObjectURI",
            )
            data.extend(response["Items"])
        return data

    def get_item(self, part_key: str, sort_key: str):
        """Returns item matching partition and sort key."""
        response = self.dynamodb_table.get_item(Key={PART_KEY_NAME: part_key, SORT_KEY_NAME: sort_key}, ConsistentRead=True)
        if not (item := response.get("Item")):
            raise Exception(
                f"No item found in table: {self.dynamodb_table.table_name} with part_key"
                f" {part_key} and sort_key {sort_key}."
            )
        log.debug("Result after Get Item: %s", item)
        return item

    # def delete_item(self, part_key: str, sort_key: str):
    #     """Delete item from dynamodb table"""
    #     try:
    #         self.dynamodb_table.delete_item(
    #             Key={PART_KEY_NAME: part_key, SORT_KEY_NAME: sort_key},
    #             ConditionExpression=Key(PART_KEY_NAME).eq(part_key) & Key(SORT_KEY_NAME).eq(sort_key),
    #         )
    #     except self.dynamodb_table.meta.client.exceptions.ConditionalCheckFailedException:
    #         return {"Status": "Success", "detail": "Permission already removed"}
    #     return {"Status": "Success", "detail": "Permission Deleted"}

    # def delete_item_by_list(self, item_list: list, part_key: str = ItemTypes.GIT_HUB):
    #     with self.dynamodb_table.batch_writer() as batch:
    #         for item_key in item_list:
    #             item_key[PART_KEY_NAME] = part_key
    #             batch.delete_item(Key=item_key)
    #     return {"Status": "Success", "detail": f"{len(item_list)} Permission(s) Deleted"}

    def put_item(self, item: dict, schema: Schema = ITEM_SCHEMA):
        """Validate the request body against the schema, Then create a new item in the auth api table."""
        item["CreatedAt"] = str(time.time())
        schema.validate(item)

        try:
            self.dynamodb_table.put_item(
                Item=item,
                ConditionExpression=AttributeNotExists(Key(PART_KEY_NAME)) & AttributeNotExists(Key(SORT_KEY_NAME)),
            )
        except ClientError as err:
            log.debug(err)
            if err.response["Error"]["Code"] == "ConditionalCheckFailedException":
                log.info("Item already exists. No changes made.")
                raise DynamoDBException("Item already exists. No changes made.")
            raise err
        log.debug(
            "Added Item with Partition Key: %s and Sort key %s to the API Auth Table",
            item[PART_KEY_NAME],
            item[SORT_KEY_NAME],
        )
        return {"Status": "Success", "detail": "Assignment created"}

    def batch_write_items(self, items: List[Dict]) -> tuple:
        """
        Write multiple items to DynamoDB using batch write.

        Args:
            items: List of dictionaries containing item attributes

        Returns:
            Tuple of (successful_writes, failed_items)
        """
        BATCH_SIZE = 25  # DynamoDB batch write limit
        success_count = 0
        failed_items = []

        # Process items in batches
        for i in range(0, len(items), BATCH_SIZE):
            batch = items[i : i + BATCH_SIZE]
            try:
                # Prepare batch write items
                batch_items = {self.table_name: [{"PutRequest": {"Item": item}} for item in batch]}

                # Perform batch write
                response = self.dynamodb_resource.batch_write_item(RequestItems=batch_items)

                # Handle unprocessed items
                unprocessed = response.get("UnprocessedItems", {}).get(self.table_name, [])
                success_count += len(batch) - len(unprocessed)

                if unprocessed:
                    log.warning(f"Unprocessed items in batch: {len(unprocessed)}")

                    # Retry unprocessed items with exponential backoff
                    retry_count = 0
                    while unprocessed and retry_count < 3:
                        retry_count += 1
                        log.info(f"Retrying {len(unprocessed)} items, attempt {retry_count}")

                        retry_batch = {self.table_name: unprocessed}
                        response = self.dynamodb_resource.batch_write_item(RequestItems=retry_batch)
                        unprocessed = response.get("UnprocessedItems", {}).get(self.table_name, [])

                        if not unprocessed:
                            success_count += len(retry_batch[self.table_name])

                    # Add any remaining unprocessed items to failed items
                    if unprocessed:
                        failed_items.extend([item["PutRequest"]["Item"] for item in unprocessed])

            except ClientError as e:
                log.error(f"Error in batch write: {str(e)}")
                failed_items.extend(batch)
                continue

        return success_count, failed_items

    def mapping_update_status(
        self,
        new_status: MAPPING_STATUS,
        part_key: str,
        sort_key: str,
        comment: str = None,
    ):
        """
        Generic Method for Mapping Status
        """

        if not isinstance(new_status, MAPPING_STATUS):
            raise TypeError("Status must be an instance of MAPPING_STATUS Enum")

        mapping_item = self.get_item(part_key=part_key, sort_key=sort_key)

        mapping_item["UpdatedAt"] = str(time.time())

        if not comment:
            comment = "Metadata file created"

        self.dynamodb_table.update_item(
            Key={PART_KEY_NAME: mapping_item[PART_KEY_NAME], SORT_KEY_NAME: mapping_item[SORT_KEY_NAME]},
            UpdateExpression="SET #st=:status, #ua = :update_at, #rs = :comment",
            ExpressionAttributeValues={
                ":status": new_status.value,
                ":update_at": mapping_item["UpdatedAt"],
                ":comment": comment,
            },
            ExpressionAttributeNames={"#st": "MappingStatus", "#ua": "UpdateAt", "#rs": "Comment"},
            ReturnValues="UPDATED_NEW",
        )
