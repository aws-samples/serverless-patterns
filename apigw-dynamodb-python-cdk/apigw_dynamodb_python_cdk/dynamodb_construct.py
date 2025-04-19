import aws_cdk as cdk
from constructs import Construct
import aws_cdk.aws_dynamodb as dynamodb


class DynamoDBConstruct(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create DynamoDB table
        self.table = dynamodb.Table(
            self, "MyTable",
            partition_key=dynamodb.Attribute(name="ID", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="FirstName", type=dynamodb.AttributeType.STRING),
            removal_policy=cdk.RemovalPolicy.DESTROY,  # NOT recommended for production code
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )
