from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    Duration,
    RemovalPolicy,
    aws_dynamodb as ddb,
    aws_appsync as appsync,
    aws_lambda as lambda_,
    aws_s3 as s3,
)
from constructs import Construct

class NotesAppSyncStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # S3 bucket
        attachments_bucket = s3.Bucket(
            self, "NoteAttachmentsBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            public_read_access=False,
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=False,
                block_public_policy=False,
                ignore_public_acls=False,
                restrict_public_buckets=False
            ),
            cors=[
                s3.CorsRule(
                    allowed_headers=["*"],
                    allowed_methods=[
                        s3.HttpMethods.PUT,
                        s3.HttpMethods.POST,
                        s3.HttpMethods.DELETE,
                        s3.HttpMethods.GET
                    ],
                    allowed_origins=["*"],
                    max_age=3000
                )
            ]
        )

        # DynamoDB table
        table = ddb.Table(
            self,
            "DynamoDBNotesTable",
            partition_key=ddb.Attribute(name="NoteId", type=ddb.AttributeType.STRING),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.RETAIN,
        )

        # Lambda function for S3 operations
        s3_lambda = lambda_.Function(
            self,
            "S3OperationsFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="handler.handler",
            code=lambda_.Code.from_asset("PresignerLambda"),
            timeout=Duration.seconds(30),
            environment={
                "BUCKET_NAME": attachments_bucket.bucket_name,
                "TABLE_NAME": table.table_name,
            },
        )

        # Grant Lambda permissions
        attachments_bucket.grant_read_write(s3_lambda)
        table.grant_read_write_data(s3_lambda)

        # AppSync GraphQL API
        api = appsync.GraphqlApi(
            self,
            "Api",
            name="MyAppSyncApi",
            definition=appsync.Definition.from_file("graphql/schema.graphql"),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.API_KEY
                )
            ),
        )

        # API Key for Output
        api_key = appsync.CfnApiKey(self, "AppSyncApiKey", api_id=api.api_id)

        # Data Sources
        ddb_ds = appsync.DynamoDbDataSource(
            self,
            "AppSyncNotesTableDataSource",
            api=api,
            table=table,
            description="The Notes Table AppSync Data Source",
        )

        lambda_ds = appsync.LambdaDataSource(
            self,
            "S3OperationsDataSource",
            api=api,
            lambda_function=s3_lambda,
            description="Lambda for S3 presigned URL operations",
        )

        # Simple resolvers for allNotes and deleteNote
        ddb_ds.create_resolver(
            "AppSyncAllNotesQueryResolver",
            type_name="Query",
            field_name="allNotes",
            request_mapping_template=appsync.MappingTemplate.from_file("resolvers/Query.allNotes.req.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("resolvers/Query.allNotes.res.vtl"),
        )

        ddb_ds.create_resolver(
            "AppSyncDeleteNoteMutationResolver",
            type_name="Mutation",
            field_name="deleteNote",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_delete_item("NoteId", "NoteId"),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item(),
        )

        # Pipeline Function: Generate presigned URL for upload
        generate_upload_url_fn = appsync.AppsyncFunction(
            self,
            "GenerateUploadUrlFunction",
            name="GenerateUploadUrlFunction",
            api=api,
            data_source=lambda_ds,
            request_mapping_template=appsync.MappingTemplate.from_file("resolvers/functions/generateUploadUrl.req.vtl"),
            response_mapping_template=appsync.MappingTemplate.lambda_result(),
        )

        # Pipeline Function: Save note to DynamoDB
        save_note_to_ddb_fn = appsync.AppsyncFunction(
            self,
            "SaveNoteToDynamoDBFunction",
            name="SaveNoteToDynamoDBFunction",
            api=api,
            data_source=ddb_ds,
            request_mapping_template=appsync.MappingTemplate.from_file("resolvers/functions/saveNoteToDynamoDB.req.vtl"),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item(),
        )

        # Pipeline Function: Get note from DynamoDB
        get_note_from_ddb_fn = appsync.AppsyncFunction(
            self,
            "GetNoteFromDynamoDBFunction",
            name="GetNoteFromDynamoDBFunction",
            api=api,
            data_source=ddb_ds,
            request_mapping_template=appsync.MappingTemplate.dynamo_db_get_item("NoteId", "NoteId"),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item(),
        )

        # Pipeline Function: Generate presigned URL for download (conditional)
        generate_download_url_fn = appsync.AppsyncFunction(
            self,
            "GenerateDownloadUrlFunction",
            name="GenerateDownloadUrlFunction",
            api=api,
            data_source=lambda_ds,
            request_mapping_template=appsync.MappingTemplate.from_file("resolvers/functions/generateDownloadUrl.req.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("resolvers/functions/generateDownloadUrl.res.vtl"),
        )

        # Pipeline Resolver: saveNote (generate URL -> save to DDB)
        appsync.Resolver(
            self,
            "SaveNotePipelineResolver",
            api=api,
            type_name="Mutation",
            field_name="saveNote",
            pipeline_config=[generate_upload_url_fn, save_note_to_ddb_fn],
            request_mapping_template=appsync.MappingTemplate.from_file("resolvers/functions/saveNotePipeline.req.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("resolvers/functions/saveNotePipeline.res.vtl"),
        )

        # Pipeline Resolver: getNote (get from DDB -> generate download URL if attachment exists)
        appsync.Resolver(
            self,
            "GetNotePipelineResolver",
            api=api,
            type_name="Query",
            field_name="getNote",
            pipeline_config=[get_note_from_ddb_fn, generate_download_url_fn],
            request_mapping_template=appsync.MappingTemplate.from_file("resolvers/functions/getNotePipeline.req.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("resolvers/functions/getNotePipeline.res.vtl"),
        )

        # Outputs
        CfnOutput(self, "GraphQLApiEndpoint", value=api.graphql_url, description="GraphQL endpoint URL")
        CfnOutput(self, "APIKey", value=api_key.attr_api_key, description="API Key")
        CfnOutput(self, "BucketName", value=attachments_bucket.bucket_name, description="S3 Bucket for attachments")
        CfnOutput(self, "TableName", value=table.table_name, description="DynamoDB Table name")


app = App()
NotesAppSyncStack(app, "NotesAppSyncStack")
app.synth()