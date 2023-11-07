import os
from pathlib import Path

from aws_cdk import (BundlingOptions, BundlingOutput, CfnOutput, CfnParameter,
                     DockerVolume, Duration, Stack)
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_glue as glue
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as f
from aws_cdk import aws_logs as logs
from aws_cdk import aws_pipes as pipes
from aws_cdk import aws_sqs as sqs
from constructs import Construct


class KafkaGlueValidateStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get the Kafka ARN for serverless MSK cluster
        self.msk_arn = CfnParameter(
            self,
            "clusterarn",
            type="String",
            description="MSK Cluster arn",
        )

        # Get the Kafka topic name from parameter
        self.topic_name = CfnParameter(
            self,
            "topicname",
            type="String",
            description="Topic to poll with EventBridge Pipe.",
        )

        # Create a Glue schema registry for the AVSC schema
        pipes_example_registry = glue.CfnRegistry(
            self,
            "PipesExample",
            name="PipesExample",
            description="Sample Schema",
        )

        schema_file = open("shared/customer_schema.avsc", "r")
        avro_schema = schema_file.read()
        schema_file.close()
        
        # Add the Customer schema to the schema registry
        customer_schema = glue.CfnSchema(
            self,
            "SampleSchema",
            compatibility="FULL",
            data_format="AVRO",
            name="CustomerSchema",
            schema_definition=avro_schema,
            registry=glue.CfnSchema.RegistryProperty(
                arn=pipes_example_registry.attr_arn,
            ),
        )

        # Add DLQ for failed messages
        dlq = sqs.Queue(
            self,
            "dlq",
            visibility_timeout=Duration.seconds(300),
        )

         # Lambda function for schema validation
        kafka_glue_validate_function = f.Function(
            self,
            "KafkaGlueValidator",
            handler="software.amazon.samples.eventbridge.App::handleRequest",
            runtime=f.Runtime.JAVA_17,
            code=self.build_mvn_package(),
            timeout=Duration.seconds(60),
            log_retention=logs.RetentionDays.ONE_DAY,
            memory_size=2048,
            tracing=f.Tracing.ACTIVE,
            snap_start=f.SnapStartConf.ON_PUBLISHED_VERSIONS,
            environment={
                "LOG_LEVEL": "INFO",  # adjust for production
                "POWERTOOLS_LOGGER_LOG_EVENT": "true",  # adjust for production
                "POWERTOOLS_SERVICE_NAME": "kafka_glue_validate",
                "DLQ_URL": dlq.queue_url,
                "REGISTRY_NAME" : pipes_example_registry.name,
                "SCHEMA_NAME": customer_schema.name,
                "TOPIC": self.topic_name.value_as_string
            }
        )

        
        snap_version = f.Version(
            self,
            "KafkaGlueValidatorSnap",
            lambda_= kafka_glue_validate_function
        )

        kafka_glue_validate_function.role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AWSGlueSchemaRegistryReadonlyAccess'))

        

        # Grant the Lambda function permission to send messages to the DLQ
        dlq.grant_send_messages(kafka_glue_validate_function)

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
        kafka_glue_validate_function.grant_invoke(pipe_role)
        event_bus.grant_put_events_to(pipe_role)
        pipe_role.add_managed_policy(policy=iam.ManagedPolicy.from_aws_managed_policy_name('AmazonMSKReadOnlyAccess'))
        pipe_role.add_managed_policy(policy=iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaMSKExecutionRole'))
        pipe_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=['*'],
            actions=[
                "kafka-cluster:*"
            ]
        ))
        


        # Define the EventBridge pipe
        pipe = pipes.CfnPipe(
            self,
            "pipe",
            role_arn=pipe_role.role_arn,
            source=self.msk_arn.value_as_string,
            source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                managed_streaming_kafka_parameters=pipes.CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty(
                    topic_name=self.topic_name.value_as_string, batch_size=10, consumer_group_id='group'
                ),
            ),
            enrichment=snap_version.function_arn,
            target=event_bus.event_bus_arn,
        )


        # Add CloudFormation outputs
        CfnOutput(self, "EventBridge Pipe", value=pipe.attr_arn)
        CfnOutput(
            self,
            "Enrichment Lambda function name",
            value=kafka_glue_validate_function.function_name,
        )
        CfnOutput(
            self,
            "Enrichment Lambda function CloudWatch log group name",
            value=kafka_glue_validate_function.log_group.log_group_name,
        )
        CfnOutput(self, "Enrichment Lambda DLQ", value=dlq.queue_name)
        CfnOutput(self, "Target service bus name", value=event_bus.event_bus_name)
        CfnOutput(
            self, "Target CloudWatch log group name", value=log_group.log_group_name
        )

    def build_mvn_package(self):
        home = str(Path.home())

        m2_home = os.path.join(home, ".m2/")

        code = f.Code.from_asset(
            path=os.path.join(".", "src", "java", "schemavalidator"),
            bundling=BundlingOptions(
                image=f.Runtime.JAVA_17.bundling_image,
                command=[
                    "/bin/sh",
                    "-c",
                    "mvn clean install -Dmaven.test.skip=true && cp /asset-input/target/schemavalidator.jar /asset-output/",
                ],
                user="root",
                output_type=BundlingOutput.ARCHIVED,
                volumes=[DockerVolume(host_path=m2_home, container_path="/root/.m2/")],
            ),
        )
        return code
