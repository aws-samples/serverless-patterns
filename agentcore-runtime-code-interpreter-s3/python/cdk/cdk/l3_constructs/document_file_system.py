from aws_cdk import Aws, aws_ec2 as ec2, aws_iam as iam, aws_s3 as s3, aws_s3files as s3files
from constructs import Construct


class DocumentFileSystem(Construct):
    """Amazon S3 Files file system that exposes one prefix of the bucket as a shared
    file system, with a mount target in each VPC subnet and an access point that
    Code Interpreter sessions mount."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        bucket: s3.IBucket,
        prefix: str,
        vpc: ec2.IVpc,
    ) -> None:
        super().__init__(scope, construct_id)

        # Role that S3 Files assumes to synchronize the file system with the bucket, as described in
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html
        sync_role = iam.Role(
            self,
            "SyncRole",
            assumed_by=iam.ServicePrincipal(
                "elasticfilesystem.amazonaws.com",
                conditions={
                    "StringEquals": {"aws:SourceAccount": Aws.ACCOUNT_ID},
                    "ArnLike": {"aws:SourceArn": f"arn:{Aws.PARTITION}:s3files:{Aws.REGION}:{Aws.ACCOUNT_ID}:file-system/*"},
                },
            ),
        )
        sync_role.add_to_policy(iam.PolicyStatement(
            actions=["s3:ListBucket", "s3:ListBucketVersions"],
            resources=[bucket.bucket_arn],
        ))
        sync_role.add_to_policy(iam.PolicyStatement(
            actions=["s3:AbortMultipartUpload", "s3:DeleteObject*", "s3:GetObject*", "s3:List*", "s3:PutObject*"],
            resources=[bucket.arn_for_objects("*")],
        ))
        sync_role.add_to_policy(iam.PolicyStatement(
            actions=[
                "events:DeleteRule", "events:DisableRule", "events:EnableRule",
                "events:PutRule", "events:PutTargets", "events:RemoveTargets",
            ],
            resources=[f"arn:{Aws.PARTITION}:events:{Aws.REGION}:{Aws.ACCOUNT_ID}:rule/DO-NOT-DELETE-S3-Files*"],
            conditions={"StringEquals": {"events:ManagedBy": "elasticfilesystem.amazonaws.com"}},
        ))
        sync_role.add_to_policy(iam.PolicyStatement(
            actions=["events:DescribeRule", "events:ListRuleNamesByTarget", "events:ListRules", "events:ListTargetsByRule"],
            resources=[f"arn:{Aws.PARTITION}:events:{Aws.REGION}:{Aws.ACCOUNT_ID}:rule/*"],
        ))

        file_system = s3files.CfnFileSystem(
            self,
            "FileSystem",
            bucket=bucket.bucket_arn,
            prefix=prefix,
            role_arn=sync_role.role_arn,
        )
        # S3 Files uses the role as soon as the file system exists, and a permissions problem leaves the file
        # system MISCONFIGURED (see the status table in
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-file-systems-creating.html).
        # The role_arn reference only orders the Role itself; this also orders its inline policy.
        file_system.node.add_dependency(sync_role)

        # NFS clients reach the file system on TCP 2049 through these mount targets. See "Security groups" in
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html
        self.mount_target_security_group = ec2.SecurityGroup(
            self,
            "MountTargetSecurityGroup",
            vpc=vpc,
            description="S3 Files mount targets",
            allow_all_outbound=False,
        )
        for index, subnet in enumerate(vpc.isolated_subnets):
            s3files.CfnMountTarget(
                self,
                f"MountTarget{index + 1}",
                file_system_id=file_system.attr_file_system_id,
                subnet_id=subnet.subnet_id,
                security_groups=[self.mount_target_security_group.security_group_id],
            )

        # Every file operation through the access point runs as this POSIX user and group, whatever
        # user the session's code runs as. A non-root user is enough to read the files: S3 Files gives
        # objects from the bucket root:root ownership and 644 permissions, which anyone can read. See
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-posix-permissions.html
        # The access point sets no root directory, so it exposes the whole file system: the bucket prefix. See
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-access-points-creating.html
        access_point = s3files.CfnAccessPoint(
            self,
            "AccessPoint",
            file_system_id=file_system.attr_file_system_id,
            posix_user=s3files.CfnAccessPoint.PosixUserProperty(uid="1000", gid="1000"),
        )

        self.bucket = bucket
        self.prefix = prefix
        self.file_system_arn = file_system.attr_file_system_arn
        self.access_point_arn = access_point.attr_access_point_arn
