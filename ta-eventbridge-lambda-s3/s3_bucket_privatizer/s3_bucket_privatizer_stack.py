from aws_cdk import Stack, Duration, aws_lambda, aws_iam, aws_logs, CfnParameter
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_sns as sns
from constructs import Construct


class S3BucketPrivatizerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Parameters
        notification_email_address = CfnParameter(self, "notification_email_address", type="String", min_length=7,
                                                  description="The E-mail address subscribed to notifications when an S3 bucket is detected as open to the public.")
        profiling = CfnParameter(self, "profiling", type="String", allowed_values=["TRUE", "FALSE"], default="FALSE",
                                 description="Enable Profiling on Lambda functions: TRUE or FALSE. Default: FALSE")
        tracing = CfnParameter(self, "tracing", type="String", allowed_values=["TRUE", "FALSE"], default="FALSE",
                               description="Enable tracing on Lambda functions: TRUE or FALSE. Default: FALSE")
        trusted_advisor_refresh_minutes = CfnParameter(self, "trusted_advisor_refresh_minutes", type="Number",
                                                       default=6, min_value=5, max_value=1440,
                                                       description="Number of minutes to schedule a trusted advisor refresh. Default: 6")
        enable_profiling = profiling.value_as_string == 'TRUE'
        enable_tracing = aws_lambda.Tracing.ACTIVE
        if tracing.value_as_string != 'TRUE':
            enable_tracing = aws_lambda.Tracing.DISABLED

        # Layers
        dependencies_layer = aws_lambda.LayerVersion(self, "dependenciesLayer",
                                                    code=aws_lambda.Code.from_asset(
                                                        "lambda_functions/dependencies_layer/"),
                                                    compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_8],
                                                    )
        # create SNS target
        email_notification_topic = sns.Topic(self, 'taEmailNotificationTopic',
                                           display_name='taEmailNotificationTopic',
                                           topic_name='taEmailNotificationTopic')
        # add subscription
        sns.Subscription(self, 'emailSubscription',
                         protocol=sns.SubscriptionProtocol.EMAIL,
                         endpoint=notification_email_address.value_as_string,
                         topic=email_notification_topic)

        default_event_bus = events.EventBus.from_event_bus_name(self, 'default', 'default')
        ta_event_pattern = events.EventPattern(
            source=['aws.trustedadvisor'],
            detail_type=['Trusted Advisor Check Item Refresh Notification']
            , detail={'check-name': ['Amazon S3 Bucket Permissions'], 'status': ['WARN', 'ERROR']}
        )
        # Lambda function to trigger when TA check flagged
        ta_check_s3_open_lambda_function_code = aws_lambda.AssetCode('lambda_functions/s3openbucket')
        ta_check_s3_open_lambda_function = aws_lambda.Function(self, 'ta_s3_open_bucket',
                                                               code=ta_check_s3_open_lambda_function_code,
                                                               runtime=aws_lambda.Runtime.PYTHON_3_8,
                                                               handler='s3openbucket.lambda_handler',
                                                               description='Function Triggered from Trusted Advisor '
                                                                           'to Block public access to an S3 Bucket',
                                                               function_name='ta-check-s3-open-lambda-function',
                                                               memory_size=128,
                                                               profiling=enable_profiling,
                                                               tracing=enable_tracing,
                                                               log_retention=aws_logs.RetentionDays.ONE_WEEK,
                                                               timeout=Duration.seconds(10),
                                                               environment={'topic_arn': email_notification_topic.topic_arn},
                                                               initial_policy=[aws_iam.PolicyStatement(
                                                                   actions=['s3:GetBucketPolicy',
                                                                            's3:DeleteBucketPolicy',
                                                                            's3:PutBucketPolicy',
                                                                            's3:GetAccountPublicAccessBlock',
                                                                            's3:GetBucketPublicAccessBlock',
                                                                            's3:PutAccountPublicAccessBlock',
                                                                            's3:PutBucketPublicAccessBlock',
                                                                            's3:GetBucketAcl',
                                                                            's3:GetObjectAcl',
                                                                            's3:PutBucketAcl',
                                                                            's3:PutObjectAcl'],
                                                                   effect=aws_iam.Effect.ALLOW,
                                                                   resources=['*']),
                                                                   aws_iam.PolicyStatement(
                                                                       actions=['SNS:Publish'],
                                                                       effect=aws_iam.Effect.ALLOW,
                                                                       resources=[email_notification_topic.topic_arn])]
                                                               )
        events.Rule(self, 's3PublicBucketRule',
                    description='Blocks Public access on an S3 bucket once detected by Trusted Advisor',
                    event_pattern=ta_event_pattern,
                    event_bus=default_event_bus,
                    targets=[targets.LambdaFunction(ta_check_s3_open_lambda_function)]
                    )
        # Refresh TA check every X minutes
        # Lambda function to trigger when TA check flagged
        ta_refresh_lambda_function_code = aws_lambda.AssetCode('lambda_functions/refreshTrustedAdvisorCheck')
        ta_refresh_lambda_function = aws_lambda.Function(self, 'refresh_ta_check',
                                                         code=ta_refresh_lambda_function_code,
                                                         runtime=aws_lambda.Runtime.PYTHON_3_8,
                                                         handler='refreshTrustedAdvisorCheck.lambda_handler',
                                                         description='Refreshes Trusted Advisor checks',
                                                         function_name='ta-refresh-ta-check-lambda-function',
                                                         memory_size=128,
                                                         profiling=enable_profiling,
                                                         tracing=enable_tracing,
                                                         log_retention=aws_logs.RetentionDays.ONE_WEEK,
                                                         timeout=Duration.seconds(5),
                                                         initial_policy=[aws_iam.PolicyStatement(
                                                             actions=['support:DescribeTrustedAdvisorChecks',
                                                                      'support:RefreshTrustedAdvisorCheck',
                                                                      'support:DescribeTrustedAdvisorCheckResult'],
                                                             effect=aws_iam.Effect.ALLOW,
                                                             resources=['*'])]
                                                         )
        ta_refresh_lambda_function.add_layers(dependencies_layer)
        events.Rule(self, 'refreshTAS3BucketPermissionsRule',
                    schedule=events.Schedule.rate(Duration.minutes(trusted_advisor_refresh_minutes.value_as_number)),
                    rule_name='refreshTAS3BucketPermissionsRule',
                    targets=[targets.LambdaFunction(ta_refresh_lambda_function)])
