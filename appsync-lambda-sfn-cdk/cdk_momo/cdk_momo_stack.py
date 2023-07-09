from os import path

from aws_cdk import (
    Stack,
    aws_appsync as appsync,
    aws_dynamodb as dynamodb,
    aws_iam as role,
    aws_stepfunctions as sf,
    aws_stepfunctions_tasks as sf_tasks,

    aws_lambda as lambda_, CfnOutput, Duration

)

from constructs import Construct

dirname = path.dirname(__file__)


class CdkMomoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        with open(path.join(dirname, "schema.txt"), 'r') as file:
            data_schema = file.read().replace('\n', '')

        # dynamodb service role

        general_role = role.Role(self, 'dynamodbRole',
                                 assumed_by=role.ServicePrincipal("appsync.amazonaws.com"))
        states_role = role.Role(self, 'statesRole',
                                assumed_by=role.ServicePrincipal("states.amazonaws.com"))
        general_role.add_to_policy(
            role.PolicyStatement(  # Restrict to listing and describing tables
                actions=["states:StartSyncExecution"],
                resources=["*"])

        )

        general_role.add_managed_policy(role.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"))
        states_role.add_managed_policy(role.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"))
        general_role.add_managed_policy(role.ManagedPolicy.from_aws_managed_policy_name("AWSLambda_FullAccess"))
        general_role \
            .add_managed_policy(role.ManagedPolicy
                                .from_aws_managed_policy_name("service-role/AWSAppSyncPushToCloudWatchLogs"))

        api = appsync.CfnGraphQLApi(
            self, "cdkMomoApi", name="cdkMomoApi",
            authentication_type='API_KEY',
            log_config=appsync.CfnGraphQLApi.LogConfigProperty(
                cloud_watch_logs_role_arn=general_role.role_arn,
                exclude_verbose_content=False,
                field_log_level='ALL'

            ),

            xray_enabled=True
        )

        graphql_schema = appsync.CfnGraphQLSchema(self, "CdkMomoGraphQLSchema",
                                                  api_id=api.attr_api_id,

                                                  definition=data_schema
                                                  )

        cdk_momo_table = dynamodb.Table(self, "CdkMomoTable",
                                        table_name="CdkMomoTable",
                                        partition_key=dynamodb.Attribute(
                                            name='id',
                                            type=dynamodb.AttributeType.STRING,

                                        ),

                                        billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,

                                        )
        fail_step = sf.Fail(self, 'Fail', cause="Failed to Update Apartment Status", error="ConditionalFailedException")

        # Define Step function tasks
        change_apartment_status = sf_tasks.DynamoUpdateItem(
            self, "Change Apartment Status",
            key={
                'id': sf_tasks.DynamoAttributeValue.from_string(sf.JsonPath.string_at("$.details.accountId")),

            },
            table=cdk_momo_table,
            condition_expression="attribute_exists(id)",
            update_expression="SET bookedStatus = :bookedStatus",
            expression_attribute_values={
                ":bookedStatus": sf_tasks.DynamoAttributeValue.from_string('Booked')
            },
            result_path="$.updateResult",

        ).add_catch(handler=fail_step)

        wait_step = sf.Wait(self, 'Wait', time=sf.WaitTime.duration(Duration.seconds(30)))

        get_status = sf_tasks.DynamoGetItem(
            self, "Get Booking Status",
            table=cdk_momo_table,
            key={
                'id': sf_tasks.DynamoAttributeValue.from_string(sf.JsonPath.string_at("$.details.accountId")),

            },
            result_path='$.getItem'
        ).add_catch(handler=fail_step)
        apartment_not_paid = sf_tasks.DynamoUpdateItem(
            self, 'Not Paid(Revert Apartment Status)',
            key={
                'id': sf_tasks.DynamoAttributeValue.from_string(sf.JsonPath.string_at("$.getItem.Item.id.S")),

            },
            table=cdk_momo_table,
            condition_expression="attribute_exists(id)",
            update_expression="SET bookedStatus = :bookedStatus",
            expression_attribute_values={
                ":bookedStatus": sf_tasks.DynamoAttributeValue.from_string('Pending')
            },
            result_path="$.notPaid",

        )
        apartment_paid = sf.Pass(self, 'Apartment Paid', comment="Apartment Paid")

        definition = change_apartment_status.next(wait_step) \
            .next(get_status) \
            .next(sf.Choice(self, "Has the Apartment been Paid ?", comment="Has the Apartment been Paid ?")
                  .when(sf.Condition.string_equals(sf.JsonPath.string_at("$.getItem.Item.id.S"), '1234567') and
                        sf.Condition.string_equals(sf.JsonPath.string_at("$.getItem.Item.bookedStatus.S"), 'Paid'),
                        apartment_paid
                        )
                  .otherwise(apartment_not_paid))

        step = sf.StateMachine(self, 'MomoStateMachine',

                               definition=definition,

                               state_machine_name="MomoStateMachine",
                               state_machine_type=sf.StateMachineType.STANDARD
                               )

        # Create the AWS Lambda function to subscribe to Amazon SQS queue
        # The source code is in './lambda' directory
        lambda_function = lambda_.Function(
            self, "LambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="start_step_function.handler",
            code=lambda_.Code.from_asset(path.join(dirname, "lambda")),
        )

        cdk_momo_data_source = appsync.CfnDataSource(self, "CDKMOMODatasource", api_id=api.attr_api_id,
                                                     name="CdkMomoDataSource", type='AWS_LAMBDA',
                                                     lambda_config=appsync.CfnDataSource.LambdaConfigProperty(
                                                         lambda_function_arn=lambda_function.function_arn
                                                     ),
                                                     service_role_arn=general_role.role_arn)

        add_demo_resolver = appsync.CfnResolver(
            self,
            "AddStepFunctionsExecutionResolver",
            api_id=api.attr_api_id,
            type_name="Mutation",
            field_name="addStepFunctionExecution",
            data_source_name=cdk_momo_data_source.attr_name

        )

        step.grant_start_execution(lambda_function)
        add_demo_resolver.add_depends_on(graphql_schema)
        lambda_function.add_environment('STEP_FNS_ARN', step.state_machine_arn)
        cdk_momo_table.grant_full_access(lambda_function)
        CfnOutput(self, "LambdaFunctionName",
                  value=lambda_function.function_name,
                  export_name='FunctionName',
                  description='Function name')
        CfnOutput(self, "AppSync Url",
                  value=api.attr_graph_ql_url,
                  export_name='AppsyncUrl',
                  description='AppsyncUrl')

        CfnOutput(self, "database arn",
                  value=cdk_momo_table.table_arn,
                  export_name='DynamoDbArn',
                  description='DynamoDBArn')

        CfnOutput(self, "step functions arn",
                  value=step.state_machine_arn,
                  export_name='StepFunctionArn',
                  description='StepFunctionArn')
