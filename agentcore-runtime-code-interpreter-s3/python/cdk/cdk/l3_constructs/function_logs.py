import jsii
from aws_cdk import Aspects, CfnResource, IAspect, RemovalPolicy, Stack, aws_logs as logs
from constructs import Construct, IConstruct


class FunctionLogs(Construct):
    """Log group for the AWS Lambda functions that CDK adds to the stack for its custom resources
    (emptying the bucket, restricting the VPC's default security group, setting log retention).

    Lambda would otherwise create a log group for each function on its first run, and stack
    deletion would leave those behind. This log group keeps 7 days of logs and is deleted with the stack.
    The aspect sets each function's LoggingConfig.LogGroup, as described in
    https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-loggroups.html
    cdk.json turns off the @aws-cdk/aws-lambda:useCdkManagedLogGroup feature flag, which would
    otherwise add a retained log group of its own for each Lambda function created with the L2
    Function construct, such as the one behind AwsCustomResource.
    """

    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        log_group = logs.LogGroup(
            self,
            "LogGroup",
            retention=logs.RetentionDays.ONE_WEEK,
            removal_policy=RemovalPolicy.DESTROY,
        )
        Aspects.of(Stack.of(self)).add(_UseLogGroup(log_group))


@jsii.implements(IAspect)
class _UseLogGroup:
    """Points every Lambda function in the stack at one log group."""

    def __init__(self, log_group: logs.ILogGroup) -> None:
        self._log_group = log_group

    def visit(self, node: IConstruct) -> None:
        if isinstance(node, CfnResource) and node.cfn_resource_type == "AWS::Lambda::Function":
            node.add_property_override("LoggingConfig.LogGroup", self._log_group.log_group_name)
