from constructs import Construct
from aws_cdk import (
    Stack,
    Duration,
    CfnParameter,
    CfnOutput,
    aws_iam as iam,
    aws_lambda_python_alpha as lambda_alpha_,
    aws_lambda as _lambda,
    aws_pipes as pipes,
    aws_events as events,
    aws_events_targets as targets,
    aws_logs as logs,
    aws_sqs as sqs,
)
from aws_cdk.aws_secretsmanager import Secret


class KafkaConfluentValidateStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get the Kafka bootstrap server URL from parameter
        self.bootstrap_server = CfnParameter(
            self,
            "bootstrapserver",
            type="String",
            description="Kafka cluster bootstrap server URL.",
        )

        # Get the Kafka topic name from parameter
        self.topic_name = CfnParameter(
            self,
            "topicname",
            type="String",
            description="Topic to poll with EventBridge Pipe.",
        )

        # Get the Kafka topic name from parameter
        self.secret_arn = CfnParameter(
            self,
            "secretarn",
            type="String",
            description="ARN of the Confluent basic auth secret.",
        )

        # Get Confluent secret
        confluent_secret = Secret.from_secret_complete_arn(
            self, "ImportedSecret", self.secret_arn.value_as_string
        )

        # Get Confluent Schema Registry secret
        confluent_schema_registry_secret = Secret.from_secret_name_v2(
            self,
            "confluent_schema_registry_secret",
            "confluent-schema-registry-secret",
        )

        # Add DLQ for failed messages
        dlq = sqs.Queue(
            self,
            "dlq",
            visibility_timeout=Duration.seconds(300),
        )

        # Lambda layer for Powertools for AWS Lambda (Python)
        powertools_layer = _lambda.LayerVersion.from_layer_version_arn(
            self,
            id="lambda-powertools",
            layer_version_arn=f"arn:aws:lambda:{Stack.of(self).region}:017000801446:layer:AWSLambdaPowertoolsPythonV2:41",
        )

        # Lambda function for schema validation with Confluent Schema Registry
        kafka_confluent_validate_function = lambda_alpha_.PythonFunction(
            self,
            "kafka_confluent_valdiate",
            entry="./src",
            index="main.py",
            handler="lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            layers=[powertools_layer],
            environment={
                "LOG_LEVEL": "DEBUG",  # adjust for production
                "POWERTOOLS_LOGGER_LOG_EVENT": "true",  # adjust for production
                "POWERTOOLS_SERVICE_NAME": "kafka_confluent_validate",
                "DLQ_URL": dlq.queue_url,
            },
            tracing=_lambda.Tracing.ACTIVE,
        )

        # Grant the Lambda function permission to send messages to the DLQ
        dlq.grant_send_messages(kafka_confluent_validate_function)

        # Grant the Lambda function read permissions on the Schema Registry secret
        confluent_schema_registry_secret.grant_read(kafka_confluent_validate_function)

        # EventBridge event bus as an example target for the EventBridge pipe
        event_bus = events.EventBus(self, "Event Bus")

        # CloudWatch Logs log group as target for the EventBridge event bus rule
        log_group = logs.LogGroup(self, "Log Group")

        # EventBridge event bus rule that publishes all events to the CloudWatch Logs log group
        events.Rule(
            self,
            "rule",
            event_bus=event_bus,
            event_pattern=events.EventPattern(
                account=[Stack.of(self).account],
            ),
            targets=[targets.CloudWatchLogGroup(log_group)],
        )

        # IAM role for the EventBridge pipe
        pipe_role = iam.Role(
            self,
            "pipes-role",
            assumed_by=iam.ServicePrincipal("pipes.amazonaws.com"),
        )

        # Grant the pipe role permissions to access source, enrichment, and target
        confluent_secret.grant_read(pipe_role)
        kafka_confluent_validate_function.grant_invoke(pipe_role)
        event_bus.grant_put_events_to(pipe_role)

        # Define the EventBridge pipe
        pipe = pipes.CfnPipe(
            self,
            "pipe",
            role_arn=pipe_role.role_arn,
            source=self.bootstrap_server.value_as_string,
            source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                self_managed_kafka_parameters=pipes.CfnPipe.PipeSourceSelfManagedKafkaParametersProperty(
                    topic_name=self.topic_name.value_as_string,
                    credentials=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty(
                        basic_auth=confluent_secret.secret_arn,
                    ),
                    maximum_batching_window_in_seconds=5,
                    batch_size=10,  # Adjust depending on pipe source and target
                    starting_position="LATEST",
                ),
            ),
            enrichment=kafka_confluent_validate_function.function_arn,
            target=event_bus.event_bus_arn,
        )

        # Add CloudFormation outputs
        CfnOutput(self, "EventBridge Pipe", value=pipe.attr_arn)
        CfnOutput(
            self,
            "Enrichment Lambda function name",
            value=kafka_confluent_validate_function.function_name,
        )
        CfnOutput(
            self,
            "Enrichment Lambda function CloudWatch log group name",
            value=kafka_confluent_validate_function.log_group.log_group_name,
        )
        CfnOutput(self, "Enrichment Lambda DLQ", value=dlq.queue_name)
        CfnOutput(self, "Target service bus name", value=event_bus.event_bus_name)
        CfnOutput(
            self, "Target CloudWatch log group name", value=log_group.log_group_name
        )
