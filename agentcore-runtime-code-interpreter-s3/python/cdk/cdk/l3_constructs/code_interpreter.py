from aws_cdk import aws_bedrockagentcore as agentcore, aws_ec2 as ec2, aws_iam as iam, custom_resources as cr
from constructs import Construct

from l3_constructs.document_file_system import DocumentFileSystem


class CodeInterpreter(Construct):
    """Custom Amazon Bedrock AgentCore Code Interpreter in VPC network mode, which S3 Files
    mounts require. Its execution role can mount the S3 Files access point read-only and read
    the same files directly from the bucket. Its security group allows only NFS traffic to the
    file system's mount targets and HTTPS to Amazon S3 through a gateway endpoint that serves
    only the document bucket. See
    https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-filesystem-configurations.html"""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        vpc: ec2.IVpc,
        file_system: DocumentFileSystem,
    ) -> None:
        super().__init__(scope, construct_id)

        security_group = ec2.SecurityGroup(
            self,
            "SecurityGroup",
            vpc=vpc,
            description="AgentCore Code Interpreter sessions",
            allow_all_outbound=False,
        )
        security_group.connections.allow_to(
            file_system.mount_target_security_group,
            ec2.Port.tcp(2049),
            "NFS to S3 Files mount targets",
        )

        self.code_interpreter = agentcore.CodeInterpreterCustom(
            self,
            "CodeInterpreter",
            description="Sandboxed Python execution for analyzing files from Amazon S3 Files",
            network_configuration=agentcore.CodeInterpreterNetworkConfiguration.using_vpc(
                self,
                vpc=vpc,
                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
                security_groups=[security_group],
            ),
        )

        # The mount permissions from the AgentCore guide above, without s3files:ClientWrite: ClientMount
        # alone gives read-only access. See "S3 Files actions for clients" in
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-security-iam.html
        iam.Grant.add_to_principal(
            grantee=self.code_interpreter,
            actions=["s3files:ClientMount", "s3files:GetAccessPoint"],
            resource_arns=[file_system.file_system_arn],
            conditions={"ArnEquals": {"s3files:AccessPointArn": file_system.access_point_arn}},
        )

        # The S3 Files mount client reads files that S3 Files didn't import (128 KiB and larger by
        # default) directly from the bucket. Without S3 access, each such read waits for an S3 timeout
        # before it falls back to NFS. These read-only statements follow "IAM role for attaching your
        # file system to AWS compute resources", limited to the file system's prefix:
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-iam-compute-role
        read_statements = [
            iam.PolicyStatement(
                actions=["s3:GetObject", "s3:GetObjectVersion"],
                resources=[file_system.bucket.arn_for_objects(f"{file_system.prefix}*")],
            ),
            iam.PolicyStatement(
                actions=["s3:ListBucket"],
                resources=[file_system.bucket.bucket_arn],
                conditions={"StringLike": {"s3:prefix": [f"{file_system.prefix}*"]}},
            ),
        ]
        for statement in read_statements:
            self.code_interpreter.grant_principal.add_to_principal_policy(statement)

        # The subnets have no route to the internet, so the mount client reaches Amazon S3 through a
        # gateway endpoint: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html
        # Its policy allows only the reads above, and only for the Code Interpreter's role, so code in a
        # session can't use the endpoint to reach other buckets, even with other credentials. Gateway
        # endpoint policies must use Principal "*" with an aws:PrincipalArn condition:
        # https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies-gateway
        s3_endpoint = vpc.add_gateway_endpoint(
            "S3Endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3,
            subnets=[ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)],
        )
        execution_role_arn = self.code_interpreter.execution_role.role_arn
        for statement in read_statements:
            endpoint_statement = statement.copy(principals=[iam.AnyPrincipal()])
            endpoint_statement.add_condition("ArnEquals", {"aws:PrincipalArn": execution_role_arn})
            s3_endpoint.add_to_policy(endpoint_statement)

        # Security group rules reach a gateway endpoint through the AWS-managed prefix list for Amazon S3,
        # whose name is the endpoint's service name (com.amazonaws.<region>.s3). CloudFormation can't
        # return the prefix list ID, so this custom resource looks it up when the stack is created:
        # https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html
        s3_prefix_list = cr.AwsCustomResource(
            self,
            "S3PrefixList",
            on_create=cr.AwsSdkCall(
                service="EC2",
                action="describeManagedPrefixLists",
                parameters={"Filters": [{
                    "Name": "prefix-list-name",
                    "Values": [s3_endpoint.node.default_child.service_name],
                }]},
                physical_resource_id=cr.PhysicalResourceId.from_response("PrefixLists.0.PrefixListId"),
                output_paths=["PrefixLists.0.PrefixListId"],
            ),
            # DescribeManagedPrefixLists doesn't support resource-level permissions.
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE),
        )
        security_group.add_egress_rule(
            ec2.Peer.prefix_list(s3_prefix_list.get_response_field("PrefixLists.0.PrefixListId")),
            ec2.Port.tcp(443),
            "HTTPS to Amazon S3 through the gateway endpoint",
        )

    @property
    def code_interpreter_id(self) -> str:
        return self.code_interpreter.code_interpreter_id

    def grant_sessions(self, grantee: iam.IGrantable) -> iam.Grant:
        """Allow the grantee to start, use and stop sessions on this Code Interpreter."""
        return self.code_interpreter.grant(
            grantee,
            "bedrock-agentcore:StartCodeInterpreterSession",
            "bedrock-agentcore:InvokeCodeInterpreter",
            "bedrock-agentcore:StopCodeInterpreterSession",
        )
