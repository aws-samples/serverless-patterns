from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr
import logging

logger = logging.getLogger("dynamodb_resource")


class Objects:
    def __init__(self, db_client, table_name):
        self.dyn_client = db_client
        self.table = self.dyn_client.Table(table_name)

    def add_key(self, item, attributes):
        update_expression = "SET {}".format(
            ",".join(f"#{key}=:{key}" for key in attributes)
        )
        attribute_values = {f":{key}": value for key, value in attributes.items()}
        attribute_names = {f"#{key}": key for key in attributes}
        print(attribute_values)

        try:
            response = self.table.update_item(
                Key={
                    "object_arn": item.object_arn,
                },
                UpdateExpression=update_expression,
                ExpressionAttributeValues=attribute_values,
                ExpressionAttributeNames=attribute_names,
            )
            return response

        except ClientError as err:
            print(err)
            raise