'''
# Amazon Redshift Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_redshift as redshift
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Redshift construct libraries](https://constructs.dev/search?q=redshift)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Redshift resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Redshift.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-redshift-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Redshift](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Redshift.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnCluster",
):
    '''Specifies a cluster. A *cluster* is a fully managed data warehouse that consists of a set of compute nodes.

    To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to `Amazon Redshift Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html>`_ in the *Amazon Redshift Cluster Management Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster = redshift.CfnCluster(self, "MyCfnCluster",
            cluster_type="clusterType",
            db_name="dbName",
            master_username="masterUsername",
            master_user_password="masterUserPassword",
            node_type="nodeType",
        
            # the properties below are optional
            allow_version_upgrade=False,
            aqua_configuration_status="aquaConfigurationStatus",
            automated_snapshot_retention_period=123,
            availability_zone="availabilityZone",
            availability_zone_relocation=False,
            availability_zone_relocation_status="availabilityZoneRelocationStatus",
            classic=False,
            cluster_identifier="clusterIdentifier",
            cluster_parameter_group_name="clusterParameterGroupName",
            cluster_security_groups=["clusterSecurityGroups"],
            cluster_subnet_group_name="clusterSubnetGroupName",
            cluster_version="clusterVersion",
            defer_maintenance=False,
            defer_maintenance_duration=123,
            defer_maintenance_end_time="deferMaintenanceEndTime",
            defer_maintenance_start_time="deferMaintenanceStartTime",
            destination_region="destinationRegion",
            elastic_ip="elasticIp",
            encrypted=False,
            endpoint=redshift.CfnCluster.EndpointProperty(
                address="address",
                port="port"
            ),
            enhanced_vpc_routing=False,
            hsm_client_certificate_identifier="hsmClientCertificateIdentifier",
            hsm_configuration_identifier="hsmConfigurationIdentifier",
            iam_roles=["iamRoles"],
            kms_key_id="kmsKeyId",
            logging_properties=redshift.CfnCluster.LoggingPropertiesProperty(
                bucket_name="bucketName",
        
                # the properties below are optional
                s3_key_prefix="s3KeyPrefix"
            ),
            maintenance_track_name="maintenanceTrackName",
            manual_snapshot_retention_period=123,
            number_of_nodes=123,
            owner_account="ownerAccount",
            port=123,
            preferred_maintenance_window="preferredMaintenanceWindow",
            publicly_accessible=False,
            resource_action="resourceAction",
            revision_target="revisionTarget",
            rotate_encryption_key=False,
            snapshot_cluster_identifier="snapshotClusterIdentifier",
            snapshot_copy_grant_name="snapshotCopyGrantName",
            snapshot_copy_manual=False,
            snapshot_copy_retention_period=123,
            snapshot_identifier="snapshotIdentifier",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_type: builtins.str,
        db_name: builtins.str,
        master_username: builtins.str,
        master_user_password: builtins.str,
        node_type: builtins.str,
        allow_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        aqua_configuration_status: typing.Optional[builtins.str] = None,
        automated_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_relocation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        availability_zone_relocation_status: typing.Optional[builtins.str] = None,
        classic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        cluster_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        cluster_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_version: typing.Optional[builtins.str] = None,
        defer_maintenance: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        defer_maintenance_duration: typing.Optional[jsii.Number] = None,
        defer_maintenance_end_time: typing.Optional[builtins.str] = None,
        defer_maintenance_start_time: typing.Optional[builtins.str] = None,
        destination_region: typing.Optional[builtins.str] = None,
        elastic_ip: typing.Optional[builtins.str] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        hsm_client_certificate_identifier: typing.Optional[builtins.str] = None,
        hsm_configuration_identifier: typing.Optional[builtins.str] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        logging_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.LoggingPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        maintenance_track_name: typing.Optional[builtins.str] = None,
        manual_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        number_of_nodes: typing.Optional[jsii.Number] = None,
        owner_account: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        resource_action: typing.Optional[builtins.str] = None,
        revision_target: typing.Optional[builtins.str] = None,
        rotate_encryption_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        snapshot_cluster_identifier: typing.Optional[builtins.str] = None,
        snapshot_copy_grant_name: typing.Optional[builtins.str] = None,
        snapshot_copy_manual: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        snapshot_copy_retention_period: typing.Optional[jsii.Number] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_type: The type of the cluster. When cluster type is specified as. - ``single-node`` , the *NumberOfNodes* parameter is not required. - ``multi-node`` , the *NumberOfNodes* parameter is required. Valid Values: ``multi-node`` | ``single-node`` Default: ``multi-node``
        :param db_name: The name of the first database to be created when the cluster is created. To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to `Create a Database <https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html>`_ in the Amazon Redshift Database Developer Guide. Default: ``dev`` Constraints: - Must contain 1 to 64 alphanumeric characters. - Must contain only lowercase letters. - Cannot be a word that is reserved by the service. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param master_username: The user name associated with the admin user account for the cluster that is being created. Constraints: - Must be 1 - 128 alphanumeric characters or hyphens. The user name can't be ``PUBLIC`` . - Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen. - The first character must be a letter. - Must not contain a colon (:) or a slash (/). - Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param master_user_password: The password associated with the admin user account for the cluster that is being created. Constraints: - Must be between 8 and 64 characters in length. - Must contain at least one uppercase letter. - Must contain at least one lowercase letter. - Must contain one number. - Can be any printable ASCII character (ASCII code 33-126) except ``'`` (single quote), ``"`` (double quote), ``\\`` , ``/`` , or ``@`` .
        :param node_type: The node type to be provisioned for the cluster. For information about node types, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* . Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge`` | ``ra3.xlplus`` | ``ra3.4xlarge`` | ``ra3.16xlarge``
        :param allow_version_upgrade: If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster. Default: ``true``
        :param aqua_configuration_status: This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).
        :param automated_snapshot_retention_period: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with `CreateClusterSnapshot <https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSnapshot.html>`_ in the *Amazon Redshift API Reference* . Default: ``1`` Constraints: Must be a value from 0 to 35.
        :param availability_zone: The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency. Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint. Example: ``us-east-2d`` Constraint: The specified Availability Zone must be in the same region as the current endpoint.
        :param availability_zone_relocation: The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.
        :param availability_zone_relocation_status: Describes the status of the Availability Zone relocation operation.
        :param classic: A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.
        :param cluster_identifier: A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console. Constraints: - Must contain from 1 to 63 alphanumeric characters or hyphens. - Alphabetic characters must be lowercase. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. - Must be unique for all clusters within an AWS account . Example: ``myexamplecluster``
        :param cluster_parameter_group_name: The name of the parameter group to be associated with this cluster. Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_ Constraints: - Must be 1 to 255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param cluster_security_groups: A list of security groups to be associated with this cluster. Default: The default cluster security group for Amazon Redshift.
        :param cluster_subnet_group_name: The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
        :param cluster_version: The version of the Amazon Redshift engine software that you want to deploy on the cluster. The version selected runs on all the nodes in the cluster. Constraints: Only version 1.0 is currently available. Example: ``1.0``
        :param defer_maintenance: A Boolean indicating whether to enable the deferred maintenance window.
        :param defer_maintenance_duration: An integer indicating the duration of the maintenance window in days. If you specify a duration, you can't specify an end time. The duration must be 45 days or less.
        :param defer_maintenance_end_time: A timestamp for the end of the time period when we defer maintenance.
        :param defer_maintenance_start_time: A timestamp indicating the start time for the deferred maintenance window.
        :param destination_region: The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        :param elastic_ip: The Elastic IP (EIP) address for the cluster. Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`_ in the Amazon Redshift Cluster Management Guide.
        :param encrypted: If ``true`` , the data in the cluster is encrypted at rest. Default: false
        :param endpoint: The connection endpoint.
        :param enhanced_vpc_routing: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`_ in the Amazon Redshift Cluster Management Guide. If this option is ``true`` , enhanced VPC routing is enabled. Default: false
        :param hsm_client_certificate_identifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        :param hsm_configuration_identifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        :param iam_roles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to `Quotas and limits <https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html>`_ in the *Amazon Redshift Cluster Management Guide* .
        :param kms_key_id: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
        :param logging_properties: Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.
        :param maintenance_track_name: An optional parameter for the name of the maintenance track for the cluster. If you don't provide a maintenance track name, the cluster is assigned to the ``current`` track.
        :param manual_snapshot_retention_period: The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots. The value must be either -1 or an integer between 1 and 3,653.
        :param number_of_nodes: The number of compute nodes in the cluster. This parameter is required when the *ClusterType* parameter is specified as ``multi-node`` . For information about determining how many nodes you need, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* . If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster. Default: ``1`` Constraints: Value must be at least 1 and no more than 100.
        :param owner_account: The AWS account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
        :param port: The port number on which the cluster accepts incoming connections. The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default: ``5439`` Valid Values: ``1150-65535``
        :param preferred_maintenance_window: The weekly time range (in UTC) during which automated cluster maintenance can occur. Format: ``ddd:hh24:mi-ddd:hh24:mi`` Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see `Maintenance Windows <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`_ in Amazon Redshift Cluster Management Guide. Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun Constraints: Minimum 30-minute window.
        :param publicly_accessible: If ``true`` , the cluster can be accessed from a public network.
        :param resource_action: The Amazon Redshift operation to be performed. Supported operations are ``pause-cluster`` and ``resume-cluster`` .
        :param revision_target: Describes a ``RevisionTarget`` object.
        :param rotate_encryption_key: Rotates the encryption keys for a cluster.
        :param snapshot_cluster_identifier: The name of the cluster the source snapshot was created from. This parameter is required if your user or role has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        :param snapshot_copy_grant_name: The name of the snapshot copy grant.
        :param snapshot_copy_manual: Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.
        :param snapshot_copy_retention_period: The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region . By default, this only changes the retention period of copied automated snapshots. If you decrease the retention period for automated snapshots that are copied to a destination AWS Region , Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period. Constraints: Must be at least 1 and no more than 35 for automated snapshots. If you specify the ``manual`` option, only newly copied manual snapshots will have the new retention period. If you specify the value of -1 newly copied manual snapshots are retained indefinitely. Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.
        :param snapshot_identifier: The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive. You must specify this parameter or ``snapshotArn`` , but not both. Example: ``my-snapshot-id``
        :param tags: A list of tag instances.
        :param vpc_security_group_ids: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster. Default: The default VPC security group is associated with the cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6d25f70797e3ae67b635ec776926582ff0be975c8173c4af217f7f6e3bd404b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            cluster_type=cluster_type,
            db_name=db_name,
            master_username=master_username,
            master_user_password=master_user_password,
            node_type=node_type,
            allow_version_upgrade=allow_version_upgrade,
            aqua_configuration_status=aqua_configuration_status,
            automated_snapshot_retention_period=automated_snapshot_retention_period,
            availability_zone=availability_zone,
            availability_zone_relocation=availability_zone_relocation,
            availability_zone_relocation_status=availability_zone_relocation_status,
            classic=classic,
            cluster_identifier=cluster_identifier,
            cluster_parameter_group_name=cluster_parameter_group_name,
            cluster_security_groups=cluster_security_groups,
            cluster_subnet_group_name=cluster_subnet_group_name,
            cluster_version=cluster_version,
            defer_maintenance=defer_maintenance,
            defer_maintenance_duration=defer_maintenance_duration,
            defer_maintenance_end_time=defer_maintenance_end_time,
            defer_maintenance_start_time=defer_maintenance_start_time,
            destination_region=destination_region,
            elastic_ip=elastic_ip,
            encrypted=encrypted,
            endpoint=endpoint,
            enhanced_vpc_routing=enhanced_vpc_routing,
            hsm_client_certificate_identifier=hsm_client_certificate_identifier,
            hsm_configuration_identifier=hsm_configuration_identifier,
            iam_roles=iam_roles,
            kms_key_id=kms_key_id,
            logging_properties=logging_properties,
            maintenance_track_name=maintenance_track_name,
            manual_snapshot_retention_period=manual_snapshot_retention_period,
            number_of_nodes=number_of_nodes,
            owner_account=owner_account,
            port=port,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            resource_action=resource_action,
            revision_target=revision_target,
            rotate_encryption_key=rotate_encryption_key,
            snapshot_cluster_identifier=snapshot_cluster_identifier,
            snapshot_copy_grant_name=snapshot_copy_grant_name,
            snapshot_copy_manual=snapshot_copy_manual,
            snapshot_copy_retention_period=snapshot_copy_retention_period,
            snapshot_identifier=snapshot_identifier,
            tags=tags,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6df99dcbb5445a88a0bb9445a37f1ba9bcd5cf462c2a8d8f24a91415f085d07a)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3cd522d882ff9ce54b9361b6991edd7e86d6cb4b5b0fd3d4f0ff14a1dc41eb7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDeferMaintenanceIdentifier")
    def attr_defer_maintenance_identifier(self) -> builtins.str:
        '''A unique identifier for the maintenance window.

        :cloudformationAttribute: DeferMaintenanceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeferMaintenanceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointAddress")
    def attr_endpoint_address(self) -> builtins.str:
        '''The connection endpoint for the Amazon Redshift cluster.

        For example: ``examplecluster.cg034hpkmmjt.us-east-1.redshift.amazonaws.com`` .

        :cloudformationAttribute: Endpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointPort")
    def attr_endpoint_port(self) -> builtins.str:
        '''The port number on which the Amazon Redshift cluster accepts connections.

        For example: ``5439`` .

        :cloudformationAttribute: Endpoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for the cluster.

        You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.

        Example: ``myexamplecluster``

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="clusterType")
    def cluster_type(self) -> builtins.str:
        '''The type of the cluster.

        When cluster type is specified as.
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterType"))

    @cluster_type.setter
    def cluster_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b228c18c00d6efcc3f5f513f526c5588459dbc4716e98017abe3c85b8869edcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterType", value)

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> builtins.str:
        '''The name of the first database to be created when the cluster is created.'''
        return typing.cast(builtins.str, jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9a6569f04f712a8617c29ce39f051b6b7718c2759016fd8c2a5129f2c3a9fc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="masterUsername")
    def master_username(self) -> builtins.str:
        '''The user name associated with the admin user account for the cluster that is being created.'''
        return typing.cast(builtins.str, jsii.get(self, "masterUsername"))

    @master_username.setter
    def master_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d32dd6d1faa4bf4d38fbc9173d77c54548a2fb5386ec97451b20f4a4e928001a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUsername", value)

    @builtins.property
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> builtins.str:
        '''The password associated with the admin user account for the cluster that is being created.'''
        return typing.cast(builtins.str, jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15113bc0292eb3a900fcad9d620cd08c320a19dfce07db8d055112a353c48cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> builtins.str:
        '''The node type to be provisioned for the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd39ef012e3b964f5c72dcc3385a8861f7af2aed9a450ea99e69c540c77b2af3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

    @builtins.property
    @jsii.member(jsii_name="allowVersionUpgrade")
    def allow_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "allowVersionUpgrade"))

    @allow_version_upgrade.setter
    def allow_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7ca48fbd412a24c0cb2a878179eca6e182ee7d8c69be5b4dbcc9862b44f73c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="aquaConfigurationStatus")
    def aqua_configuration_status(self) -> typing.Optional[builtins.str]:
        '''This parameter is retired.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aquaConfigurationStatus"))

    @aqua_configuration_status.setter
    def aqua_configuration_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cdce8be072a8ad4655038a048a780e28c874f470b860ba5efeeb19c470e71b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aquaConfigurationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="automatedSnapshotRetentionPeriod")
    def automated_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days that automated snapshots are retained.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automatedSnapshotRetentionPeriod"))

    @automated_snapshot_retention_period.setter
    def automated_snapshot_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed5582d6104bfbddace4e373fcab8d459431100b894b1a16de7955842e400de2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatedSnapshotRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c65bcbcfa0b5c942ee2dc4ddc36123d19ebb2e20f61c7d530335b08b87aa98e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneRelocation")
    def availability_zone_relocation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "availabilityZoneRelocation"))

    @availability_zone_relocation.setter
    def availability_zone_relocation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1b7e4b7b94737e4e8b1853309ee5372d1269f37dcf09d4ee449f352e5c55c0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneRelocation", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneRelocationStatus")
    def availability_zone_relocation_status(self) -> typing.Optional[builtins.str]:
        '''Describes the status of the Availability Zone relocation operation.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneRelocationStatus"))

    @availability_zone_relocation_status.setter
    def availability_zone_relocation_status(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6634fb9f81aef0b48d0404fc2c8ec19d02a04b1a9d7c65863692e53f28a978b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneRelocationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="classic")
    def classic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A boolean value indicating whether the resize operation is using the classic resize process.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "classic"))

    @classic.setter
    def classic(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86549952f63853b3a6d50c0ea714bcad7fc4bcbeea239762fe3bc3035e81531)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classic", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d01d7ad2f21e729a4d05a6c6c40c03bbeff0a26976f99e7487e40fe7c6aec7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group to be associated with this cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterParameterGroupName"))

    @cluster_parameter_group_name.setter
    def cluster_parameter_group_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b14873e72b628e6b816d839111208ef6aa6af543ebe87c8be7b488ef5566b602)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroups")
    def cluster_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security groups to be associated with this cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clusterSecurityGroups"))

    @cluster_security_groups.setter
    def cluster_security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a651f09ef507bb8529243e4a1dc4c6db1ed0753b890fafe63aa18f8ed2fed90c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSubnetGroupName")
    def cluster_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of a cluster subnet group to be associated with this cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterSubnetGroupName"))

    @cluster_subnet_group_name.setter
    def cluster_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a6de3cf6594b7e052bda7985e485f86e4d3c373ccc8db3221e45f5e1dd17325)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterVersion")
    def cluster_version(self) -> typing.Optional[builtins.str]:
        '''The version of the Amazon Redshift engine software that you want to deploy on the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterVersion"))

    @cluster_version.setter
    def cluster_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55a998895e7e966b871bd67fe918e51ba3671e2c2b298eb8eb34d7f51d07206e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterVersion", value)

    @builtins.property
    @jsii.member(jsii_name="deferMaintenance")
    def defer_maintenance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean indicating whether to enable the deferred maintenance window.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deferMaintenance"))

    @defer_maintenance.setter
    def defer_maintenance(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4237433b5883296c8faff34d0e01925a666684fbee40ec2906e948a41d50e503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferMaintenance", value)

    @builtins.property
    @jsii.member(jsii_name="deferMaintenanceDuration")
    def defer_maintenance_duration(self) -> typing.Optional[jsii.Number]:
        '''An integer indicating the duration of the maintenance window in days.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deferMaintenanceDuration"))

    @defer_maintenance_duration.setter
    def defer_maintenance_duration(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38793f2500254714c6067bec6f72a5a038c50d8bc9b6b03b375518dce428a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferMaintenanceDuration", value)

    @builtins.property
    @jsii.member(jsii_name="deferMaintenanceEndTime")
    def defer_maintenance_end_time(self) -> typing.Optional[builtins.str]:
        '''A timestamp for the end of the time period when we defer maintenance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deferMaintenanceEndTime"))

    @defer_maintenance_end_time.setter
    def defer_maintenance_end_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__707a603887573fd509d9f52453e8a586dcbece345650487f919175b7a32ce0f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferMaintenanceEndTime", value)

    @builtins.property
    @jsii.member(jsii_name="deferMaintenanceStartTime")
    def defer_maintenance_start_time(self) -> typing.Optional[builtins.str]:
        '''A timestamp indicating the start time for the deferred maintenance window.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deferMaintenanceStartTime"))

    @defer_maintenance_start_time.setter
    def defer_maintenance_start_time(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd9fc695606c0a941294d8fb46b82ad186d9cc0f1ceecc9efea154fa51e57d2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferMaintenanceStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="destinationRegion")
    def destination_region(self) -> typing.Optional[builtins.str]:
        '''The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationRegion"))

    @destination_region.setter
    def destination_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9affeaf50223bc3ddba02727393f5841690e26871908e7f312f79f76ce20857c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationRegion", value)

    @builtins.property
    @jsii.member(jsii_name="elasticIp")
    def elastic_ip(self) -> typing.Optional[builtins.str]:
        '''The Elastic IP (EIP) address for the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticIp"))

    @elastic_ip.setter
    def elastic_ip(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af4905b0871175bb94d0e68d7844830025c4dfe81acb2f97d60012f417d079f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticIp", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , the data in the cluster is encrypted at rest.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b1075c71946fea633b06672f811d3ed06a3627779b2123983ff2dbad9432e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EndpointProperty"]]:
        '''The connection endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EndpointProperty"]], jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EndpointProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91af587b7f602d533107461b26deea688b9ac30f8cff34b2f281da70b5f20be0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedVpcRouting")
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''An option that specifies whether to create the cluster with enhanced VPC routing enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enhancedVpcRouting"))

    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f39b0b2b5df52249767c8cb6463c876078868c14687667fd735f0b6d22fb18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedVpcRouting", value)

    @builtins.property
    @jsii.member(jsii_name="hsmClientCertificateIdentifier")
    def hsm_client_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmClientCertificateIdentifier"))

    @hsm_client_certificate_identifier.setter
    def hsm_client_certificate_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5024cde1beb60571770fd7108dbe12a4a475dfeac6bf7a1e1027e2081e58e486)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmClientCertificateIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="hsmConfigurationIdentifier")
    def hsm_configuration_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmConfigurationIdentifier"))

    @hsm_configuration_identifier.setter
    def hsm_configuration_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23dbabcc0b1bd43d467873c3ad184988bc516c60957ee94cf9abaf50268fff8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmConfigurationIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoles")
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "iamRoles"))

    @iam_roles.setter
    def iam_roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772c14b10e457f7456acacbd7c571e904d8d7e32ccc4be7e64dfdc23417fd3e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoles", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b9e3255675fa581da5945ef20b026be1c2c1fc9d1bad30a7bf9c5e63e884f60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="loggingProperties")
    def logging_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.LoggingPropertiesProperty"]]:
        '''Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.LoggingPropertiesProperty"]], jsii.get(self, "loggingProperties"))

    @logging_properties.setter
    def logging_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.LoggingPropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faccaac60f090449dba9f2adeeb99fa490f6f2532ea91a0f5372422d57002f26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingProperties", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceTrackName")
    def maintenance_track_name(self) -> typing.Optional[builtins.str]:
        '''An optional parameter for the name of the maintenance track for the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceTrackName"))

    @maintenance_track_name.setter
    def maintenance_track_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdec41d5a2f886a294c35cbf10b6f505571be31e2c00a5a1c57a87a34cf49426)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceTrackName", value)

    @builtins.property
    @jsii.member(jsii_name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The default number of days to retain a manual snapshot.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "manualSnapshotRetentionPeriod"))

    @manual_snapshot_retention_period.setter
    def manual_snapshot_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47928702ad781fa3915ff0f5068c3b692ff5d8d891b871ca8319d3632cdffe22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manualSnapshotRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfNodes")
    def number_of_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of compute nodes in the cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfNodes"))

    @number_of_nodes.setter
    def number_of_nodes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b646aacda3a7612936e7568c66769cf203d6286890366d0346d5c38410b0d8b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfNodes", value)

    @builtins.property
    @jsii.member(jsii_name="ownerAccount")
    def owner_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account used to create or copy the snapshot.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerAccount"))

    @owner_account.setter
    def owner_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52bf6c5c1ccac8e9a203c7d7459384ca20fe2bd847c219060b148ce817130552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerAccount", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number on which the cluster accepts incoming connections.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a336566c0c0ca699ff01424a213ca87bb14f46bd413f3548c40bf33f2efa36b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range (in UTC) during which automated cluster maintenance can occur.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9692ea98b60bb6630f40e5fdbf329c062ea1111b09de0a06388619337bba7451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , the cluster can be accessed from a public network.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da6f0bb2273ecadf755efeb5a905c9ee82720866a8ce8f61a2c6d3d21eb9300b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="resourceAction")
    def resource_action(self) -> typing.Optional[builtins.str]:
        '''The Amazon Redshift operation to be performed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceAction"))

    @resource_action.setter
    def resource_action(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb4e2cacc7f73b63f83b3db029d401ee0e2b0f5ba058212b603e71548aac621)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceAction", value)

    @builtins.property
    @jsii.member(jsii_name="revisionTarget")
    def revision_target(self) -> typing.Optional[builtins.str]:
        '''Describes a ``RevisionTarget`` object.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionTarget"))

    @revision_target.setter
    def revision_target(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a194ca9d86844bb3b3e45b505b5c6b5cfc6e7394cda5b168c597edf84cd5a57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revisionTarget", value)

    @builtins.property
    @jsii.member(jsii_name="rotateEncryptionKey")
    def rotate_encryption_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Rotates the encryption keys for a cluster.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "rotateEncryptionKey"))

    @rotate_encryption_key.setter
    def rotate_encryption_key(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bf5df20a75b52e1cdb3d7517d4cb1b82f3940133ad5667db9df487314abf2a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotateEncryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotClusterIdentifier")
    def snapshot_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster the source snapshot was created from.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotClusterIdentifier"))

    @snapshot_cluster_identifier.setter
    def snapshot_cluster_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e02d3c6ace6da2f11c5895ef3151ab4e22925463fd7aa7f5ae7818e0ad18d5ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotCopyGrantName")
    def snapshot_copy_grant_name(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot copy grant.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotCopyGrantName"))

    @snapshot_copy_grant_name.setter
    def snapshot_copy_grant_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b48178e0c2c9351bf3494f98a7ba9056b7d4796545f2aee976d0338e14e8eb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotCopyGrantName", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotCopyManual")
    def snapshot_copy_manual(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "snapshotCopyManual"))

    @snapshot_copy_manual.setter
    def snapshot_copy_manual(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88f25e386153f816099eeca0eba6c12a2141a4398dd600a4a5bcfba56a506c9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotCopyManual", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotCopyRetentionPeriod")
    def snapshot_copy_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region .'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotCopyRetentionPeriod"))

    @snapshot_copy_retention_period.setter
    def snapshot_copy_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87d1d0fe426ee03be5f64341988115cbe1d5afd95c0b6861542b95a8abb56740)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotCopyRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotIdentifier")
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot from which to create the new cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdentifier"))

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cba9391bc97d92920ae3a792b5478605ed68dd5607ac8946d0f1a69fcb651dfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tag instances.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5764b8f0fdd9373a15be01abce350629381e233414237e16a244d4691af89468)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__596c101c9c404cca151b1203ca97bd2d503f355f47622224daa47f385e650be8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnCluster.EndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "port": "port"},
    )
    class EndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a connection endpoint.

            :param address: The DNS address of the cluster. This property is read only.
            :param port: The port that the database engine is listening on. This property is read only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                endpoint_property = redshift.CfnCluster.EndpointProperty(
                    address="address",
                    port="port"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f4b31c37417a3cee773773bc1a0a140f366a4e0e7ed41054ce4a4eb796ba219)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The DNS address of the cluster.

            This property is read only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html#cfn-redshift-cluster-endpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The port that the database engine is listening on.

            This property is read only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html#cfn-redshift-cluster-endpoint-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnCluster.LoggingPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "s3_key_prefix": "s3KeyPrefix"},
    )
    class LoggingPropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            s3_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

            :param bucket_name: The name of an existing S3 bucket where the log files are to be stored. Constraints: - Must be in the same region as the cluster - The cluster must have read bucket and put object permissions
            :param s3_key_prefix: The prefix applied to the log file names. Constraints: - Cannot exceed 512 characters - Cannot contain spaces( ), double quotes ("), single quotes ('), a backslash (), or control characters. The hexadecimal codes for invalid characters are: - x00 to x20 - x22 - x27 - x5c - x7f or larger

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                logging_properties_property = redshift.CfnCluster.LoggingPropertiesProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    s3_key_prefix="s3KeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7aec990e988274953eb37b89aa72be860b6d20fca7dd87507fb1bd44a65b7b9)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if s3_key_prefix is not None:
                self._values["s3_key_prefix"] = s3_key_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of an existing S3 bucket where the log files are to be stored.

            Constraints:

            - Must be in the same region as the cluster
            - The cluster must have read bucket and put object permissions

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The prefix applied to the log file names.

            Constraints:

            - Cannot exceed 512 characters
            - Cannot contain spaces( ), double quotes ("), single quotes ('), a backslash (), or control characters. The hexadecimal codes for invalid characters are:
            - x00 to x20
            - x22
            - x27
            - x5c
            - x7f or larger

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-s3keyprefix
            '''
            result = self._values.get("s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnClusterParameterGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterParameterGroup",
):
    '''Describes a parameter group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster_parameter_group = redshift.CfnClusterParameterGroup(self, "MyCfnClusterParameterGroup",
            description="description",
            parameter_group_family="parameterGroupFamily",
        
            # the properties below are optional
            parameter_group_name="parameterGroupName",
            parameters=[redshift.CfnClusterParameterGroup.ParameterProperty(
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        parameter_group_family: builtins.str,
        parameter_group_name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnClusterParameterGroup.ParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: The description of the parameter group.
        :param parameter_group_family: The name of the cluster parameter group family that this cluster parameter group is compatible with. You can create a custom parameter group and then associate your cluster with it. For more information, see `Amazon Redshift parameter groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_ .
        :param parameter_group_name: The name of the cluster parameter group.
        :param parameters: An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request. For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional. For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.
        :param tags: The list of tags for the cluster parameter group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4414ca463de61620f73bf7c02eb829639136d7dcc505964ba4d9e9618286c69)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterParameterGroupProps(
            description=description,
            parameter_group_family=parameter_group_family,
            parameter_group_name=parameter_group_name,
            parameters=parameters,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33c3f5debe7a54728cc11b0bbd4cd3ef9a8b793416272ffb149cec7294e16c50)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b7d74938a95ad8692c806f56ca7eec2add84b72ad04dfdd43dbf75c8f82078c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the parameter group.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa01b978d978b525b22dfcc1d5e7ed1fdba8f3423e58633da46999cf64b6145e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupFamily")
    def parameter_group_family(self) -> builtins.str:
        '''The name of the cluster parameter group family that this cluster parameter group is compatible with.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupFamily"))

    @parameter_group_family.setter
    def parameter_group_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31d55e60eeba305c90c4c7a8c50b43e6bf8362044925cc46818a03d69862ee99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupFamily", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster parameter group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterGroupName"))

    @parameter_group_name.setter
    def parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71389da0b60c4def288c7b3fb2b371fda4f4162f1eb827248ad420d596ae579c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnClusterParameterGroup.ParameterProperty"]]]]:
        '''An array of parameters to be modified.

        A maximum of 20 parameters can be modified in a single request.
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnClusterParameterGroup.ParameterProperty"]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnClusterParameterGroup.ParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f6965bfa88c2fcb264091e20f622accf9bf23be5cacdb3362545db9e6c9696c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tags for the cluster parameter group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9d60dbe1f8113e3b7f1c5d9cd93fced6c4ccd359227db112e355b0839bdd7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnClusterParameterGroup.ParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''Describes a parameter in a cluster parameter group.

            :param parameter_name: The name of the parameter.
            :param parameter_value: The value of the parameter. If ``ParameterName`` is ``wlm_json_configuration`` , then the maximum size of ``ParameterValue`` is 8000 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                parameter_property = redshift.CfnClusterParameterGroup.ParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__240e23a4f4e09dcaf1a5943661993a46709536c604817503e522b63ccc6ccf48)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''The name of the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html#cfn-redshift-clusterparametergroup-parameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The value of the parameter.

            If ``ParameterName`` is ``wlm_json_configuration`` , then the maximum size of ``ParameterValue`` is 8000 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html#cfn-redshift-clusterparametergroup-parameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "parameter_group_family": "parameterGroupFamily",
        "parameter_group_name": "parameterGroupName",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnClusterParameterGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        parameter_group_family: builtins.str,
        parameter_group_name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClusterParameterGroup.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterParameterGroup``.

        :param description: The description of the parameter group.
        :param parameter_group_family: The name of the cluster parameter group family that this cluster parameter group is compatible with. You can create a custom parameter group and then associate your cluster with it. For more information, see `Amazon Redshift parameter groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_ .
        :param parameter_group_name: The name of the cluster parameter group.
        :param parameters: An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request. For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional. For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.
        :param tags: The list of tags for the cluster parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_parameter_group_props = redshift.CfnClusterParameterGroupProps(
                description="description",
                parameter_group_family="parameterGroupFamily",
            
                # the properties below are optional
                parameter_group_name="parameterGroupName",
                parameters=[redshift.CfnClusterParameterGroup.ParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c09351f48d96a72274bd7deddd60b35ff3d97dffac06fef8da0c50669179bc)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameter_group_family", value=parameter_group_family, expected_type=type_hints["parameter_group_family"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "parameter_group_family": parameter_group_family,
        }
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_group_family(self) -> builtins.str:
        '''The name of the cluster parameter group family that this cluster parameter group is compatible with.

        You can create a custom parameter group and then associate your cluster with it. For more information, see `Amazon Redshift parameter groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parametergroupfamily
        '''
        result = self._values.get("parameter_group_family")
        assert result is not None, "Required property 'parameter_group_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parametergroupname
        '''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnClusterParameterGroup.ParameterProperty]]]]:
        '''An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.

        For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.

        For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnClusterParameterGroup.ParameterProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tags for the cluster parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_type": "clusterType",
        "db_name": "dbName",
        "master_username": "masterUsername",
        "master_user_password": "masterUserPassword",
        "node_type": "nodeType",
        "allow_version_upgrade": "allowVersionUpgrade",
        "aqua_configuration_status": "aquaConfigurationStatus",
        "automated_snapshot_retention_period": "automatedSnapshotRetentionPeriod",
        "availability_zone": "availabilityZone",
        "availability_zone_relocation": "availabilityZoneRelocation",
        "availability_zone_relocation_status": "availabilityZoneRelocationStatus",
        "classic": "classic",
        "cluster_identifier": "clusterIdentifier",
        "cluster_parameter_group_name": "clusterParameterGroupName",
        "cluster_security_groups": "clusterSecurityGroups",
        "cluster_subnet_group_name": "clusterSubnetGroupName",
        "cluster_version": "clusterVersion",
        "defer_maintenance": "deferMaintenance",
        "defer_maintenance_duration": "deferMaintenanceDuration",
        "defer_maintenance_end_time": "deferMaintenanceEndTime",
        "defer_maintenance_start_time": "deferMaintenanceStartTime",
        "destination_region": "destinationRegion",
        "elastic_ip": "elasticIp",
        "encrypted": "encrypted",
        "endpoint": "endpoint",
        "enhanced_vpc_routing": "enhancedVpcRouting",
        "hsm_client_certificate_identifier": "hsmClientCertificateIdentifier",
        "hsm_configuration_identifier": "hsmConfigurationIdentifier",
        "iam_roles": "iamRoles",
        "kms_key_id": "kmsKeyId",
        "logging_properties": "loggingProperties",
        "maintenance_track_name": "maintenanceTrackName",
        "manual_snapshot_retention_period": "manualSnapshotRetentionPeriod",
        "number_of_nodes": "numberOfNodes",
        "owner_account": "ownerAccount",
        "port": "port",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "resource_action": "resourceAction",
        "revision_target": "revisionTarget",
        "rotate_encryption_key": "rotateEncryptionKey",
        "snapshot_cluster_identifier": "snapshotClusterIdentifier",
        "snapshot_copy_grant_name": "snapshotCopyGrantName",
        "snapshot_copy_manual": "snapshotCopyManual",
        "snapshot_copy_retention_period": "snapshotCopyRetentionPeriod",
        "snapshot_identifier": "snapshotIdentifier",
        "tags": "tags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        cluster_type: builtins.str,
        db_name: builtins.str,
        master_username: builtins.str,
        master_user_password: builtins.str,
        node_type: builtins.str,
        allow_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        aqua_configuration_status: typing.Optional[builtins.str] = None,
        automated_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_relocation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        availability_zone_relocation_status: typing.Optional[builtins.str] = None,
        classic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        cluster_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        cluster_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_version: typing.Optional[builtins.str] = None,
        defer_maintenance: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        defer_maintenance_duration: typing.Optional[jsii.Number] = None,
        defer_maintenance_end_time: typing.Optional[builtins.str] = None,
        defer_maintenance_start_time: typing.Optional[builtins.str] = None,
        destination_region: typing.Optional[builtins.str] = None,
        elastic_ip: typing.Optional[builtins.str] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        hsm_client_certificate_identifier: typing.Optional[builtins.str] = None,
        hsm_configuration_identifier: typing.Optional[builtins.str] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        logging_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.LoggingPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        maintenance_track_name: typing.Optional[builtins.str] = None,
        manual_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        number_of_nodes: typing.Optional[jsii.Number] = None,
        owner_account: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        resource_action: typing.Optional[builtins.str] = None,
        revision_target: typing.Optional[builtins.str] = None,
        rotate_encryption_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        snapshot_cluster_identifier: typing.Optional[builtins.str] = None,
        snapshot_copy_grant_name: typing.Optional[builtins.str] = None,
        snapshot_copy_manual: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        snapshot_copy_retention_period: typing.Optional[jsii.Number] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param cluster_type: The type of the cluster. When cluster type is specified as. - ``single-node`` , the *NumberOfNodes* parameter is not required. - ``multi-node`` , the *NumberOfNodes* parameter is required. Valid Values: ``multi-node`` | ``single-node`` Default: ``multi-node``
        :param db_name: The name of the first database to be created when the cluster is created. To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to `Create a Database <https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html>`_ in the Amazon Redshift Database Developer Guide. Default: ``dev`` Constraints: - Must contain 1 to 64 alphanumeric characters. - Must contain only lowercase letters. - Cannot be a word that is reserved by the service. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param master_username: The user name associated with the admin user account for the cluster that is being created. Constraints: - Must be 1 - 128 alphanumeric characters or hyphens. The user name can't be ``PUBLIC`` . - Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen. - The first character must be a letter. - Must not contain a colon (:) or a slash (/). - Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param master_user_password: The password associated with the admin user account for the cluster that is being created. Constraints: - Must be between 8 and 64 characters in length. - Must contain at least one uppercase letter. - Must contain at least one lowercase letter. - Must contain one number. - Can be any printable ASCII character (ASCII code 33-126) except ``'`` (single quote), ``"`` (double quote), ``\\`` , ``/`` , or ``@`` .
        :param node_type: The node type to be provisioned for the cluster. For information about node types, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* . Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge`` | ``ra3.xlplus`` | ``ra3.4xlarge`` | ``ra3.16xlarge``
        :param allow_version_upgrade: If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster. Default: ``true``
        :param aqua_configuration_status: This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).
        :param automated_snapshot_retention_period: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with `CreateClusterSnapshot <https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSnapshot.html>`_ in the *Amazon Redshift API Reference* . Default: ``1`` Constraints: Must be a value from 0 to 35.
        :param availability_zone: The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency. Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint. Example: ``us-east-2d`` Constraint: The specified Availability Zone must be in the same region as the current endpoint.
        :param availability_zone_relocation: The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.
        :param availability_zone_relocation_status: Describes the status of the Availability Zone relocation operation.
        :param classic: A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.
        :param cluster_identifier: A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console. Constraints: - Must contain from 1 to 63 alphanumeric characters or hyphens. - Alphabetic characters must be lowercase. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. - Must be unique for all clusters within an AWS account . Example: ``myexamplecluster``
        :param cluster_parameter_group_name: The name of the parameter group to be associated with this cluster. Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_ Constraints: - Must be 1 to 255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param cluster_security_groups: A list of security groups to be associated with this cluster. Default: The default cluster security group for Amazon Redshift.
        :param cluster_subnet_group_name: The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
        :param cluster_version: The version of the Amazon Redshift engine software that you want to deploy on the cluster. The version selected runs on all the nodes in the cluster. Constraints: Only version 1.0 is currently available. Example: ``1.0``
        :param defer_maintenance: A Boolean indicating whether to enable the deferred maintenance window.
        :param defer_maintenance_duration: An integer indicating the duration of the maintenance window in days. If you specify a duration, you can't specify an end time. The duration must be 45 days or less.
        :param defer_maintenance_end_time: A timestamp for the end of the time period when we defer maintenance.
        :param defer_maintenance_start_time: A timestamp indicating the start time for the deferred maintenance window.
        :param destination_region: The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        :param elastic_ip: The Elastic IP (EIP) address for the cluster. Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`_ in the Amazon Redshift Cluster Management Guide.
        :param encrypted: If ``true`` , the data in the cluster is encrypted at rest. Default: false
        :param endpoint: The connection endpoint.
        :param enhanced_vpc_routing: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`_ in the Amazon Redshift Cluster Management Guide. If this option is ``true`` , enhanced VPC routing is enabled. Default: false
        :param hsm_client_certificate_identifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        :param hsm_configuration_identifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        :param iam_roles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to `Quotas and limits <https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html>`_ in the *Amazon Redshift Cluster Management Guide* .
        :param kms_key_id: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
        :param logging_properties: Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.
        :param maintenance_track_name: An optional parameter for the name of the maintenance track for the cluster. If you don't provide a maintenance track name, the cluster is assigned to the ``current`` track.
        :param manual_snapshot_retention_period: The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots. The value must be either -1 or an integer between 1 and 3,653.
        :param number_of_nodes: The number of compute nodes in the cluster. This parameter is required when the *ClusterType* parameter is specified as ``multi-node`` . For information about determining how many nodes you need, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* . If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster. Default: ``1`` Constraints: Value must be at least 1 and no more than 100.
        :param owner_account: The AWS account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
        :param port: The port number on which the cluster accepts incoming connections. The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default: ``5439`` Valid Values: ``1150-65535``
        :param preferred_maintenance_window: The weekly time range (in UTC) during which automated cluster maintenance can occur. Format: ``ddd:hh24:mi-ddd:hh24:mi`` Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see `Maintenance Windows <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`_ in Amazon Redshift Cluster Management Guide. Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun Constraints: Minimum 30-minute window.
        :param publicly_accessible: If ``true`` , the cluster can be accessed from a public network.
        :param resource_action: The Amazon Redshift operation to be performed. Supported operations are ``pause-cluster`` and ``resume-cluster`` .
        :param revision_target: Describes a ``RevisionTarget`` object.
        :param rotate_encryption_key: Rotates the encryption keys for a cluster.
        :param snapshot_cluster_identifier: The name of the cluster the source snapshot was created from. This parameter is required if your user or role has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        :param snapshot_copy_grant_name: The name of the snapshot copy grant.
        :param snapshot_copy_manual: Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.
        :param snapshot_copy_retention_period: The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region . By default, this only changes the retention period of copied automated snapshots. If you decrease the retention period for automated snapshots that are copied to a destination AWS Region , Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period. Constraints: Must be at least 1 and no more than 35 for automated snapshots. If you specify the ``manual`` option, only newly copied manual snapshots will have the new retention period. If you specify the value of -1 newly copied manual snapshots are retained indefinitely. Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.
        :param snapshot_identifier: The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive. You must specify this parameter or ``snapshotArn`` , but not both. Example: ``my-snapshot-id``
        :param tags: A list of tag instances.
        :param vpc_security_group_ids: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster. Default: The default VPC security group is associated with the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_props = redshift.CfnClusterProps(
                cluster_type="clusterType",
                db_name="dbName",
                master_username="masterUsername",
                master_user_password="masterUserPassword",
                node_type="nodeType",
            
                # the properties below are optional
                allow_version_upgrade=False,
                aqua_configuration_status="aquaConfigurationStatus",
                automated_snapshot_retention_period=123,
                availability_zone="availabilityZone",
                availability_zone_relocation=False,
                availability_zone_relocation_status="availabilityZoneRelocationStatus",
                classic=False,
                cluster_identifier="clusterIdentifier",
                cluster_parameter_group_name="clusterParameterGroupName",
                cluster_security_groups=["clusterSecurityGroups"],
                cluster_subnet_group_name="clusterSubnetGroupName",
                cluster_version="clusterVersion",
                defer_maintenance=False,
                defer_maintenance_duration=123,
                defer_maintenance_end_time="deferMaintenanceEndTime",
                defer_maintenance_start_time="deferMaintenanceStartTime",
                destination_region="destinationRegion",
                elastic_ip="elasticIp",
                encrypted=False,
                endpoint=redshift.CfnCluster.EndpointProperty(
                    address="address",
                    port="port"
                ),
                enhanced_vpc_routing=False,
                hsm_client_certificate_identifier="hsmClientCertificateIdentifier",
                hsm_configuration_identifier="hsmConfigurationIdentifier",
                iam_roles=["iamRoles"],
                kms_key_id="kmsKeyId",
                logging_properties=redshift.CfnCluster.LoggingPropertiesProperty(
                    bucket_name="bucketName",
            
                    # the properties below are optional
                    s3_key_prefix="s3KeyPrefix"
                ),
                maintenance_track_name="maintenanceTrackName",
                manual_snapshot_retention_period=123,
                number_of_nodes=123,
                owner_account="ownerAccount",
                port=123,
                preferred_maintenance_window="preferredMaintenanceWindow",
                publicly_accessible=False,
                resource_action="resourceAction",
                revision_target="revisionTarget",
                rotate_encryption_key=False,
                snapshot_cluster_identifier="snapshotClusterIdentifier",
                snapshot_copy_grant_name="snapshotCopyGrantName",
                snapshot_copy_manual=False,
                snapshot_copy_retention_period=123,
                snapshot_identifier="snapshotIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88d0d566c2d2524449f4cc4b794952814b68b5dcd5494f1bcdf5b417ee87ed01)
            check_type(argname="argument cluster_type", value=cluster_type, expected_type=type_hints["cluster_type"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument master_username", value=master_username, expected_type=type_hints["master_username"])
            check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument allow_version_upgrade", value=allow_version_upgrade, expected_type=type_hints["allow_version_upgrade"])
            check_type(argname="argument aqua_configuration_status", value=aqua_configuration_status, expected_type=type_hints["aqua_configuration_status"])
            check_type(argname="argument automated_snapshot_retention_period", value=automated_snapshot_retention_period, expected_type=type_hints["automated_snapshot_retention_period"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument availability_zone_relocation", value=availability_zone_relocation, expected_type=type_hints["availability_zone_relocation"])
            check_type(argname="argument availability_zone_relocation_status", value=availability_zone_relocation_status, expected_type=type_hints["availability_zone_relocation_status"])
            check_type(argname="argument classic", value=classic, expected_type=type_hints["classic"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument cluster_parameter_group_name", value=cluster_parameter_group_name, expected_type=type_hints["cluster_parameter_group_name"])
            check_type(argname="argument cluster_security_groups", value=cluster_security_groups, expected_type=type_hints["cluster_security_groups"])
            check_type(argname="argument cluster_subnet_group_name", value=cluster_subnet_group_name, expected_type=type_hints["cluster_subnet_group_name"])
            check_type(argname="argument cluster_version", value=cluster_version, expected_type=type_hints["cluster_version"])
            check_type(argname="argument defer_maintenance", value=defer_maintenance, expected_type=type_hints["defer_maintenance"])
            check_type(argname="argument defer_maintenance_duration", value=defer_maintenance_duration, expected_type=type_hints["defer_maintenance_duration"])
            check_type(argname="argument defer_maintenance_end_time", value=defer_maintenance_end_time, expected_type=type_hints["defer_maintenance_end_time"])
            check_type(argname="argument defer_maintenance_start_time", value=defer_maintenance_start_time, expected_type=type_hints["defer_maintenance_start_time"])
            check_type(argname="argument destination_region", value=destination_region, expected_type=type_hints["destination_region"])
            check_type(argname="argument elastic_ip", value=elastic_ip, expected_type=type_hints["elastic_ip"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument enhanced_vpc_routing", value=enhanced_vpc_routing, expected_type=type_hints["enhanced_vpc_routing"])
            check_type(argname="argument hsm_client_certificate_identifier", value=hsm_client_certificate_identifier, expected_type=type_hints["hsm_client_certificate_identifier"])
            check_type(argname="argument hsm_configuration_identifier", value=hsm_configuration_identifier, expected_type=type_hints["hsm_configuration_identifier"])
            check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument logging_properties", value=logging_properties, expected_type=type_hints["logging_properties"])
            check_type(argname="argument maintenance_track_name", value=maintenance_track_name, expected_type=type_hints["maintenance_track_name"])
            check_type(argname="argument manual_snapshot_retention_period", value=manual_snapshot_retention_period, expected_type=type_hints["manual_snapshot_retention_period"])
            check_type(argname="argument number_of_nodes", value=number_of_nodes, expected_type=type_hints["number_of_nodes"])
            check_type(argname="argument owner_account", value=owner_account, expected_type=type_hints["owner_account"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument resource_action", value=resource_action, expected_type=type_hints["resource_action"])
            check_type(argname="argument revision_target", value=revision_target, expected_type=type_hints["revision_target"])
            check_type(argname="argument rotate_encryption_key", value=rotate_encryption_key, expected_type=type_hints["rotate_encryption_key"])
            check_type(argname="argument snapshot_cluster_identifier", value=snapshot_cluster_identifier, expected_type=type_hints["snapshot_cluster_identifier"])
            check_type(argname="argument snapshot_copy_grant_name", value=snapshot_copy_grant_name, expected_type=type_hints["snapshot_copy_grant_name"])
            check_type(argname="argument snapshot_copy_manual", value=snapshot_copy_manual, expected_type=type_hints["snapshot_copy_manual"])
            check_type(argname="argument snapshot_copy_retention_period", value=snapshot_copy_retention_period, expected_type=type_hints["snapshot_copy_retention_period"])
            check_type(argname="argument snapshot_identifier", value=snapshot_identifier, expected_type=type_hints["snapshot_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_type": cluster_type,
            "db_name": db_name,
            "master_username": master_username,
            "master_user_password": master_user_password,
            "node_type": node_type,
        }
        if allow_version_upgrade is not None:
            self._values["allow_version_upgrade"] = allow_version_upgrade
        if aqua_configuration_status is not None:
            self._values["aqua_configuration_status"] = aqua_configuration_status
        if automated_snapshot_retention_period is not None:
            self._values["automated_snapshot_retention_period"] = automated_snapshot_retention_period
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if availability_zone_relocation is not None:
            self._values["availability_zone_relocation"] = availability_zone_relocation
        if availability_zone_relocation_status is not None:
            self._values["availability_zone_relocation_status"] = availability_zone_relocation_status
        if classic is not None:
            self._values["classic"] = classic
        if cluster_identifier is not None:
            self._values["cluster_identifier"] = cluster_identifier
        if cluster_parameter_group_name is not None:
            self._values["cluster_parameter_group_name"] = cluster_parameter_group_name
        if cluster_security_groups is not None:
            self._values["cluster_security_groups"] = cluster_security_groups
        if cluster_subnet_group_name is not None:
            self._values["cluster_subnet_group_name"] = cluster_subnet_group_name
        if cluster_version is not None:
            self._values["cluster_version"] = cluster_version
        if defer_maintenance is not None:
            self._values["defer_maintenance"] = defer_maintenance
        if defer_maintenance_duration is not None:
            self._values["defer_maintenance_duration"] = defer_maintenance_duration
        if defer_maintenance_end_time is not None:
            self._values["defer_maintenance_end_time"] = defer_maintenance_end_time
        if defer_maintenance_start_time is not None:
            self._values["defer_maintenance_start_time"] = defer_maintenance_start_time
        if destination_region is not None:
            self._values["destination_region"] = destination_region
        if elastic_ip is not None:
            self._values["elastic_ip"] = elastic_ip
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if enhanced_vpc_routing is not None:
            self._values["enhanced_vpc_routing"] = enhanced_vpc_routing
        if hsm_client_certificate_identifier is not None:
            self._values["hsm_client_certificate_identifier"] = hsm_client_certificate_identifier
        if hsm_configuration_identifier is not None:
            self._values["hsm_configuration_identifier"] = hsm_configuration_identifier
        if iam_roles is not None:
            self._values["iam_roles"] = iam_roles
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if logging_properties is not None:
            self._values["logging_properties"] = logging_properties
        if maintenance_track_name is not None:
            self._values["maintenance_track_name"] = maintenance_track_name
        if manual_snapshot_retention_period is not None:
            self._values["manual_snapshot_retention_period"] = manual_snapshot_retention_period
        if number_of_nodes is not None:
            self._values["number_of_nodes"] = number_of_nodes
        if owner_account is not None:
            self._values["owner_account"] = owner_account
        if port is not None:
            self._values["port"] = port
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if resource_action is not None:
            self._values["resource_action"] = resource_action
        if revision_target is not None:
            self._values["revision_target"] = revision_target
        if rotate_encryption_key is not None:
            self._values["rotate_encryption_key"] = rotate_encryption_key
        if snapshot_cluster_identifier is not None:
            self._values["snapshot_cluster_identifier"] = snapshot_cluster_identifier
        if snapshot_copy_grant_name is not None:
            self._values["snapshot_copy_grant_name"] = snapshot_copy_grant_name
        if snapshot_copy_manual is not None:
            self._values["snapshot_copy_manual"] = snapshot_copy_manual
        if snapshot_copy_retention_period is not None:
            self._values["snapshot_copy_retention_period"] = snapshot_copy_retention_period
        if snapshot_identifier is not None:
            self._values["snapshot_identifier"] = snapshot_identifier
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def cluster_type(self) -> builtins.str:
        '''The type of the cluster. When cluster type is specified as.

        - ``single-node`` , the *NumberOfNodes* parameter is not required.
        - ``multi-node`` , the *NumberOfNodes* parameter is required.

        Valid Values: ``multi-node`` | ``single-node``

        Default: ``multi-node``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustertype
        '''
        result = self._values.get("cluster_type")
        assert result is not None, "Required property 'cluster_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_name(self) -> builtins.str:
        '''The name of the first database to be created when the cluster is created.

        To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to `Create a Database <https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html>`_ in the Amazon Redshift Database Developer Guide.

        Default: ``dev``

        Constraints:

        - Must contain 1 to 64 alphanumeric characters.
        - Must contain only lowercase letters.
        - Cannot be a word that is reserved by the service. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-dbname
        '''
        result = self._values.get("db_name")
        assert result is not None, "Required property 'db_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_username(self) -> builtins.str:
        '''The user name associated with the admin user account for the cluster that is being created.

        Constraints:

        - Must be 1 - 128 alphanumeric characters or hyphens. The user name can't be ``PUBLIC`` .
        - Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
        - The first character must be a letter.
        - Must not contain a colon (:) or a slash (/).
        - Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-masterusername
        '''
        result = self._values.get("master_username")
        assert result is not None, "Required property 'master_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_user_password(self) -> builtins.str:
        '''The password associated with the admin user account for the cluster that is being created.

        Constraints:

        - Must be between 8 and 64 characters in length.
        - Must contain at least one uppercase letter.
        - Must contain at least one lowercase letter.
        - Must contain one number.
        - Can be any printable ASCII character (ASCII code 33-126) except ``'`` (single quote), ``"`` (double quote), ``\\`` , ``/`` , or ``@`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-masteruserpassword
        '''
        result = self._values.get("master_user_password")
        assert result is not None, "Required property 'master_user_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_type(self) -> builtins.str:
        '''The node type to be provisioned for the cluster.

        For information about node types, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* .

        Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge`` | ``ra3.xlplus`` | ``ra3.4xlarge`` | ``ra3.16xlarge``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-nodetype
        '''
        result = self._values.get("node_type")
        assert result is not None, "Required property 'node_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.

        When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.

        Default: ``true``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-allowversionupgrade
        '''
        result = self._values.get("allow_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def aqua_configuration_status(self) -> typing.Optional[builtins.str]:
        '''This parameter is retired.

        It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-aquaconfigurationstatus
        '''
        result = self._values.get("aqua_configuration_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automated_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days that automated snapshots are retained.

        If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with `CreateClusterSnapshot <https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSnapshot.html>`_ in the *Amazon Redshift API Reference* .

        Default: ``1``

        Constraints: Must be a value from 0 to 35.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-automatedsnapshotretentionperiod
        '''
        result = self._values.get("automated_snapshot_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster.

        For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.

        Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.

        Example: ``us-east-2d``

        Constraint: The specified Availability Zone must be in the same region as the current endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zone_relocation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzonerelocation
        '''
        result = self._values.get("availability_zone_relocation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def availability_zone_relocation_status(self) -> typing.Optional[builtins.str]:
        '''Describes the status of the Availability Zone relocation operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzonerelocationstatus
        '''
        result = self._values.get("availability_zone_relocation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def classic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A boolean value indicating whether the resize operation is using the classic resize process.

        If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-classic
        '''
        result = self._values.get("classic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the cluster.

        You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.

        Constraints:

        - Must contain from 1 to 63 alphanumeric characters or hyphens.
        - Alphabetic characters must be lowercase.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.
        - Must be unique for all clusters within an AWS account .

        Example: ``myexamplecluster``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusteridentifier
        '''
        result = self._values.get("cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group to be associated with this cluster.

        Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_

        Constraints:

        - Must be 1 to 255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusterparametergroupname
        '''
        result = self._values.get("cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security groups to be associated with this cluster.

        Default: The default cluster security group for Amazon Redshift.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustersecuritygroups
        '''
        result = self._values.get("cluster_security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cluster_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of a cluster subnet group to be associated with this cluster.

        If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustersubnetgroupname
        '''
        result = self._values.get("cluster_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_version(self) -> typing.Optional[builtins.str]:
        '''The version of the Amazon Redshift engine software that you want to deploy on the cluster.

        The version selected runs on all the nodes in the cluster.

        Constraints: Only version 1.0 is currently available.

        Example: ``1.0``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusterversion
        '''
        result = self._values.get("cluster_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def defer_maintenance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean indicating whether to enable the deferred maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenance
        '''
        result = self._values.get("defer_maintenance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def defer_maintenance_duration(self) -> typing.Optional[jsii.Number]:
        '''An integer indicating the duration of the maintenance window in days.

        If you specify a duration, you can't specify an end time. The duration must be 45 days or less.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenanceduration
        '''
        result = self._values.get("defer_maintenance_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def defer_maintenance_end_time(self) -> typing.Optional[builtins.str]:
        '''A timestamp for the end of the time period when we defer maintenance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenanceendtime
        '''
        result = self._values.get("defer_maintenance_end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def defer_maintenance_start_time(self) -> typing.Optional[builtins.str]:
        '''A timestamp indicating the start time for the deferred maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenancestarttime
        '''
        result = self._values.get("defer_maintenance_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_region(self) -> typing.Optional[builtins.str]:
        '''The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-destinationregion
        '''
        result = self._values.get("destination_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elastic_ip(self) -> typing.Optional[builtins.str]:
        '''The Elastic IP (EIP) address for the cluster.

        Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`_ in the Amazon Redshift Cluster Management Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-elasticip
        '''
        result = self._values.get("elastic_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , the data in the cluster is encrypted at rest.

        Default: false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-encrypted
        '''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EndpointProperty]]:
        '''The connection endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-endpoint
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EndpointProperty]], result)

    @builtins.property
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''An option that specifies whether to create the cluster with enhanced VPC routing enabled.

        To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`_ in the Amazon Redshift Cluster Management Guide.

        If this option is ``true`` , enhanced VPC routing is enabled.

        Default: false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-enhancedvpcrouting
        '''
        result = self._values.get("enhanced_vpc_routing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def hsm_client_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-hsmclientcertificateidentifier
        '''
        result = self._values.get("hsm_client_certificate_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hsm_configuration_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-hsmconfigurationidentifier
        '''
        result = self._values.get("hsm_configuration_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

        You must supply the IAM roles in their Amazon Resource Name (ARN) format.

        The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to `Quotas and limits <https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html>`_ in the *Amazon Redshift Cluster Management Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-iamroles
        '''
        result = self._values.get("iam_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.LoggingPropertiesProperty]]:
        '''Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-loggingproperties
        '''
        result = self._values.get("logging_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.LoggingPropertiesProperty]], result)

    @builtins.property
    def maintenance_track_name(self) -> typing.Optional[builtins.str]:
        '''An optional parameter for the name of the maintenance track for the cluster.

        If you don't provide a maintenance track name, the cluster is assigned to the ``current`` track.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-maintenancetrackname
        '''
        result = self._values.get("maintenance_track_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manual_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The default number of days to retain a manual snapshot.

        If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.

        The value must be either -1 or an integer between 1 and 3,653.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-manualsnapshotretentionperiod
        '''
        result = self._values.get("manual_snapshot_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def number_of_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of compute nodes in the cluster.

        This parameter is required when the *ClusterType* parameter is specified as ``multi-node`` .

        For information about determining how many nodes you need, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* .

        If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.

        Default: ``1``

        Constraints: Value must be at least 1 and no more than 100.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-numberofnodes
        '''
        result = self._values.get("number_of_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def owner_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account used to create or copy the snapshot.

        Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-owneraccount
        '''
        result = self._values.get("owner_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number on which the cluster accepts incoming connections.

        The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.

        Default: ``5439``

        Valid Values: ``1150-65535``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range (in UTC) during which automated cluster maintenance can occur.

        Format: ``ddd:hh24:mi-ddd:hh24:mi``

        Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see `Maintenance Windows <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`_ in Amazon Redshift Cluster Management Guide.

        Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

        Constraints: Minimum 30-minute window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , the cluster can be accessed from a public network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def resource_action(self) -> typing.Optional[builtins.str]:
        '''The Amazon Redshift operation to be performed.

        Supported operations are ``pause-cluster`` and ``resume-cluster`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-resourceaction
        '''
        result = self._values.get("resource_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision_target(self) -> typing.Optional[builtins.str]:
        '''Describes a ``RevisionTarget`` object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-revisiontarget
        '''
        result = self._values.get("revision_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rotate_encryption_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Rotates the encryption keys for a cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-rotateencryptionkey
        '''
        result = self._values.get("rotate_encryption_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def snapshot_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster the source snapshot was created from.

        This parameter is required if your user or role has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotclusteridentifier
        '''
        result = self._values.get("snapshot_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_copy_grant_name(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot copy grant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopygrantname
        '''
        result = self._values.get("snapshot_copy_grant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_copy_manual(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopymanual
        '''
        result = self._values.get("snapshot_copy_manual")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def snapshot_copy_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region .

        By default, this only changes the retention period of copied automated snapshots.

        If you decrease the retention period for automated snapshots that are copied to a destination AWS Region , Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period.

        Constraints: Must be at least 1 and no more than 35 for automated snapshots.

        If you specify the ``manual`` option, only newly copied manual snapshots will have the new retention period.

        If you specify the value of -1 newly copied manual snapshots are retained indefinitely.

        Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopyretentionperiod
        '''
        result = self._values.get("snapshot_copy_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot from which to create the new cluster.

        This parameter isn't case sensitive. You must specify this parameter or ``snapshotArn`` , but not both.

        Example: ``my-snapshot-id``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotidentifier
        '''
        result = self._values.get("snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tag instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.

        Default: The default VPC security group is associated with the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnClusterSecurityGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSecurityGroup",
):
    '''Specifies a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.

    For information about managing security groups, go to `Amazon Redshift Cluster Security Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html>`_ in the *Amazon Redshift Cluster Management Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster_security_group = redshift.CfnClusterSecurityGroup(self, "MyCfnClusterSecurityGroup",
            description="description",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description for the security group.
        :param tags: Specifies an arbitrary set of tags (key–value pairs) to associate with this security group. Use tags to manage your resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b22efcbba45de188c12e3a4ec10ac826aa23627c8a9c1ab33ac3ab92f1db7ca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterSecurityGroupProps(description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf91138ab4de58056c692e7a90e9c37175b85888798658fb335eb1fda9dc46ef)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c67faf71bfcbce5abc9c55181019e84dee71de571bd99a7bb417425f307fe805)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description for the security group.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b860785f063213d814fda288a338005f7a7bdf25187251589ec205640c547a66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies an arbitrary set of tags (key–value pairs) to associate with this security group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__defdac711f3e7a77b19ec04bc132d682928b4f21ff6be172e15e2ac9f0cd6e8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.implements(_IInspectable_c2943556)
class CfnClusterSecurityGroupIngress(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSecurityGroupIngress",
):
    '''Adds an inbound (ingress) rule to an Amazon Redshift security group.

    Depending on whether the application accessing your cluster is running on the Internet or an Amazon EC2 instance, you can authorize inbound access to either a Classless Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2 security group. You can add as many as 20 ingress rules to an Amazon Redshift security group.

    If you authorize access to an Amazon EC2 security group, specify *EC2SecurityGroupName* and *EC2SecurityGroupOwnerId* . The Amazon EC2 security group and Amazon Redshift cluster must be in the same AWS Region .

    If you authorize access to a CIDR/IP address range, specify *CIDRIP* . For an overview of CIDR blocks, see the Wikipedia article on `Classless Inter-Domain Routing <https://docs.aws.amazon.com/http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

    You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to `Working with Security Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html>`_ in the *Amazon Redshift Cluster Management Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster_security_group_ingress = redshift.CfnClusterSecurityGroupIngress(self, "MyCfnClusterSecurityGroupIngress",
            cluster_security_group_name="clusterSecurityGroupName",
        
            # the properties below are optional
            cidrip="cidrip",
            ec2_security_group_name="ec2SecurityGroupName",
            ec2_security_group_owner_id="ec2SecurityGroupOwnerId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_security_group_name: builtins.str,
        cidrip: typing.Optional[builtins.str] = None,
        ec2_security_group_name: typing.Optional[builtins.str] = None,
        ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_security_group_name: The name of the security group to which the ingress rule is added.
        :param cidrip: The IP range to be added the Amazon Redshift security group.
        :param ec2_security_group_name: The EC2 security group to be added the Amazon Redshift security group.
        :param ec2_security_group_owner_id: The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter. The AWS Access Key ID is not an acceptable value. Example: ``111122223333`` Conditional. If you specify the ``EC2SecurityGroupName`` property, you must specify this property.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41697fee2951713c64e294c4e4850203dbc7d20174c1fed5347f5918875e54ff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterSecurityGroupIngressProps(
            cluster_security_group_name=cluster_security_group_name,
            cidrip=cidrip,
            ec2_security_group_name=ec2_security_group_name,
            ec2_security_group_owner_id=ec2_security_group_owner_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5daaf061a9776bc828b5e17868e3a5341ceac5a9921dfd313ea5696175e61dc)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d33bff3b3590906995d56f375a2e2ff36b57c39243b7809fae2071ef39734a92)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupName")
    def cluster_security_group_name(self) -> builtins.str:
        '''The name of the security group to which the ingress rule is added.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterSecurityGroupName"))

    @cluster_security_group_name.setter
    def cluster_security_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__450127f44d7b9d46222076daeb75aef61dc74ee7b8c0361931cbc378b77f2b61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSecurityGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="cidrip")
    def cidrip(self) -> typing.Optional[builtins.str]:
        '''The IP range to be added the Amazon Redshift security group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrip"))

    @cidrip.setter
    def cidrip(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc70f827b8b8bd4fd90e9971cafaa821209d83d7fb903364e18ca0bd12bb4fa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrip", value)

    @builtins.property
    @jsii.member(jsii_name="ec2SecurityGroupName")
    def ec2_security_group_name(self) -> typing.Optional[builtins.str]:
        '''The EC2 security group to be added the Amazon Redshift security group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2SecurityGroupName"))

    @ec2_security_group_name.setter
    def ec2_security_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__305455f9fef2cb5c555b60efcd3ef9258c1c90d3a8215d9e5d93dbcc7b9829a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2SecurityGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="ec2SecurityGroupOwnerId")
    def ec2_security_group_owner_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2SecurityGroupOwnerId"))

    @ec2_security_group_owner_id.setter
    def ec2_security_group_owner_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea6866c86f6e401834ff96949921e03d99488382c3dc85fdb956991534d7d684)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2SecurityGroupOwnerId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSecurityGroupIngressProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_security_group_name": "clusterSecurityGroupName",
        "cidrip": "cidrip",
        "ec2_security_group_name": "ec2SecurityGroupName",
        "ec2_security_group_owner_id": "ec2SecurityGroupOwnerId",
    },
)
class CfnClusterSecurityGroupIngressProps:
    def __init__(
        self,
        *,
        cluster_security_group_name: builtins.str,
        cidrip: typing.Optional[builtins.str] = None,
        ec2_security_group_name: typing.Optional[builtins.str] = None,
        ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterSecurityGroupIngress``.

        :param cluster_security_group_name: The name of the security group to which the ingress rule is added.
        :param cidrip: The IP range to be added the Amazon Redshift security group.
        :param ec2_security_group_name: The EC2 security group to be added the Amazon Redshift security group.
        :param ec2_security_group_owner_id: The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter. The AWS Access Key ID is not an acceptable value. Example: ``111122223333`` Conditional. If you specify the ``EC2SecurityGroupName`` property, you must specify this property.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_security_group_ingress_props = redshift.CfnClusterSecurityGroupIngressProps(
                cluster_security_group_name="clusterSecurityGroupName",
            
                # the properties below are optional
                cidrip="cidrip",
                ec2_security_group_name="ec2SecurityGroupName",
                ec2_security_group_owner_id="ec2SecurityGroupOwnerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e72baf9a2078a5fc775c4d9a3b9a1dcd173a15a5e17511d8332cdbd8704787a)
            check_type(argname="argument cluster_security_group_name", value=cluster_security_group_name, expected_type=type_hints["cluster_security_group_name"])
            check_type(argname="argument cidrip", value=cidrip, expected_type=type_hints["cidrip"])
            check_type(argname="argument ec2_security_group_name", value=ec2_security_group_name, expected_type=type_hints["ec2_security_group_name"])
            check_type(argname="argument ec2_security_group_owner_id", value=ec2_security_group_owner_id, expected_type=type_hints["ec2_security_group_owner_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_security_group_name": cluster_security_group_name,
        }
        if cidrip is not None:
            self._values["cidrip"] = cidrip
        if ec2_security_group_name is not None:
            self._values["ec2_security_group_name"] = ec2_security_group_name
        if ec2_security_group_owner_id is not None:
            self._values["ec2_security_group_owner_id"] = ec2_security_group_owner_id

    @builtins.property
    def cluster_security_group_name(self) -> builtins.str:
        '''The name of the security group to which the ingress rule is added.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-clustersecuritygroupname
        '''
        result = self._values.get("cluster_security_group_name")
        assert result is not None, "Required property 'cluster_security_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidrip(self) -> typing.Optional[builtins.str]:
        '''The IP range to be added the Amazon Redshift security group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-cidrip
        '''
        result = self._values.get("cidrip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_security_group_name(self) -> typing.Optional[builtins.str]:
        '''The EC2 security group to be added the Amazon Redshift security group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-ec2securitygroupname
        '''
        result = self._values.get("ec2_security_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_security_group_owner_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter.

        The AWS Access Key ID is not an acceptable value.

        Example: ``111122223333``

        Conditional. If you specify the ``EC2SecurityGroupName`` property, you must specify this property.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-ec2securitygroupownerid
        '''
        result = self._values.get("ec2_security_group_owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterSecurityGroupIngressProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSecurityGroupProps",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "tags": "tags"},
)
class CfnClusterSecurityGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterSecurityGroup``.

        :param description: A description for the security group.
        :param tags: Specifies an arbitrary set of tags (key–value pairs) to associate with this security group. Use tags to manage your resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_security_group_props = redshift.CfnClusterSecurityGroupProps(
                description="description",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cec630b207d9099c41b9e111a98fa64b023d8033b4d94d7ed94a660cba9bd2d7)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''A description for the security group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html#cfn-redshift-clustersecuritygroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies an arbitrary set of tags (key–value pairs) to associate with this security group.

        Use tags to manage your resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html#cfn-redshift-clustersecuritygroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterSecurityGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnClusterSubnetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSubnetGroup",
):
    '''Specifies an Amazon Redshift subnet group.

    You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud ( Amazon VPC ) when creating Amazon Redshift subnet group.

    For information about subnet groups, go to `Amazon Redshift Cluster Subnet Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html>`_ in the *Amazon Redshift Cluster Management Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster_subnet_group = redshift.CfnClusterSubnetGroup(self, "MyCfnClusterSubnetGroup",
            description="description",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description for the subnet group.
        :param subnet_ids: An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
        :param tags: Specifies an arbitrary set of tags (key–value pairs) to associate with this subnet group. Use tags to manage your resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__586021bde6b1b8994209ba685b5235bc28948707297a01dceac93f542c3474a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterSubnetGroupProps(
            description=description, subnet_ids=subnet_ids, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4678321f8dafb0155a5d7f2280c259134e10caeb8b0316bf25b7f635300db0)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d89491d283cad8a318fc40039d9bee0dcd132fe85c1ad67b9a1cdb2b3e7ae33)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterSubnetGroupName")
    def attr_cluster_subnet_group_name(self) -> builtins.str:
        '''The name of the cluster subnet group.

        :cloudformationAttribute: ClusterSubnetGroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterSubnetGroupName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description for the subnet group.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6179b77c5cb42be7c2cabba28e3458abc09417919b74082d51e7593e0e912a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''An array of VPC subnet IDs.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ff71bbb1e980605e8312fa79d3ec8776207253d24115be955dea5799064105b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies an arbitrary set of tags (key–value pairs) to associate with this subnet group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0234790a32423c903d2d0b04af30d14f6232a9d29765580ce78154e1956f53c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnClusterSubnetGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterSubnetGroup``.

        :param description: A description for the subnet group.
        :param subnet_ids: An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
        :param tags: Specifies an arbitrary set of tags (key–value pairs) to associate with this subnet group. Use tags to manage your resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_subnet_group_props = redshift.CfnClusterSubnetGroupProps(
                description="description",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7629b191964d0b486283403d34c774eed1fd92a00727981a023ae6012064b43)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "subnet_ids": subnet_ids,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''A description for the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''An array of VPC subnet IDs.

        A maximum of 20 subnets can be modified in a single request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies an arbitrary set of tags (key–value pairs) to associate with this subnet group.

        Use tags to manage your resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEndpointAccess(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAccess",
):
    '''Creates a Redshift-managed VPC endpoint.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_endpoint_access = redshift.CfnEndpointAccess(self, "MyCfnEndpointAccess",
            cluster_identifier="clusterIdentifier",
            endpoint_name="endpointName",
            subnet_group_name="subnetGroupName",
            vpc_security_group_ids=["vpcSecurityGroupIds"],
        
            # the properties below are optional
            resource_owner="resourceOwner"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_identifier: builtins.str,
        endpoint_name: builtins.str,
        subnet_group_name: builtins.str,
        vpc_security_group_ids: typing.Sequence[builtins.str],
        resource_owner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_identifier: The cluster identifier of the cluster associated with the endpoint.
        :param endpoint_name: The name of the endpoint.
        :param subnet_group_name: The subnet group name where Amazon Redshift chooses to deploy the endpoint.
        :param vpc_security_group_ids: The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
        :param resource_owner: The AWS account ID of the owner of the cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adead910756274e2bd16ee0b3769d492024abb4cf55d5583a9333d89a1943c75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointAccessProps(
            cluster_identifier=cluster_identifier,
            endpoint_name=endpoint_name,
            subnet_group_name=subnet_group_name,
            vpc_security_group_ids=vpc_security_group_ids,
            resource_owner=resource_owner,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b18a7291d940515b72b89f09ad9d7dce3b9a26f99a3a7370573478d5e080b721)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e87b4e358c9074a491173a7bab1e4f3fc3b6265fd5a882c6f514b3ef2b843ec)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAddress")
    def attr_address(self) -> builtins.str:
        '''The DNS address of the endpoint.

        :cloudformationAttribute: Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointCreateTime")
    def attr_endpoint_create_time(self) -> builtins.str:
        '''The time (UTC) that the endpoint was created.

        :cloudformationAttribute: EndpointCreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointStatus")
    def attr_endpoint_status(self) -> builtins.str:
        '''The status of the endpoint.

        :cloudformationAttribute: EndpointStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrPort")
    def attr_port(self) -> jsii.Number:
        '''The port number on which the cluster accepts incoming connections.

        :cloudformationAttribute: Port
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrPort"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcEndpoint")
    def attr_vpc_endpoint(self) -> _IResolvable_da3f097b:
        '''The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.

        :cloudformationAttribute: VpcEndpoint
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVpcEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcEndpointNetworkInterfaces")
    def attr_vpc_endpoint_network_interfaces(self) -> _IResolvable_da3f097b:
        '''One or more network interfaces of the endpoint.

        Also known as an interface endpoint.

        :cloudformationAttribute: VpcEndpoint.NetworkInterfaces
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVpcEndpointNetworkInterfaces"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcEndpointVpcEndpointId")
    def attr_vpc_endpoint_vpc_endpoint_id(self) -> builtins.str:
        '''The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.

        :cloudformationAttribute: VpcEndpoint.VpcEndpointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcEndpointVpcEndpointId"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcEndpointVpcId")
    def attr_vpc_endpoint_vpc_id(self) -> builtins.str:
        '''The VPC identifier that the endpoint is associated.

        :cloudformationAttribute: VpcEndpoint.VpcId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcEndpointVpcId"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcSecurityGroups")
    def attr_vpc_security_groups(self) -> _IResolvable_da3f097b:
        '''The security groups associated with the endpoint.

        :cloudformationAttribute: VpcSecurityGroups
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVpcSecurityGroups"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''The cluster identifier of the cluster associated with the endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__598e9e6d4735cbbfcb104ab4427ff7d119cd8cd64e92591cb873a7be4fb53765)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> builtins.str:
        '''The name of the endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "endpointName"))

    @endpoint_name.setter
    def endpoint_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1190e8d5a0ada81ea332ba42ab4ff9e194abb7bb642a0812316fc5a559f435d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''The subnet group name where Amazon Redshift chooses to deploy the endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "subnetGroupName"))

    @subnet_group_name.setter
    def subnet_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7f534ad279e98a0ece57c6f3178362d5fda74cca1f75270242f4184a2e05e43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        '''The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6601a60835f68eef555c454dfd6e418359ca5e88b148c65f784029c6b7404ecd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="resourceOwner")
    def resource_owner(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of the owner of the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceOwner"))

    @resource_owner.setter
    def resource_owner(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f37292ea99cc675208c9bc19ed54b302762c47c1c291b6034a1554bca882d54e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceOwner", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAccess.NetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "network_interface_id": "networkInterfaceId",
            "private_ip_address": "privateIpAddress",
            "subnet_id": "subnetId",
        },
    )
    class NetworkInterfaceProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            network_interface_id: typing.Optional[builtins.str] = None,
            private_ip_address: typing.Optional[builtins.str] = None,
            subnet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a network interface.

            :param availability_zone: The Availability Zone.
            :param network_interface_id: The network interface identifier.
            :param private_ip_address: The IPv4 address of the network interface within the subnet.
            :param subnet_id: The subnet identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                network_interface_property = redshift.CfnEndpointAccess.NetworkInterfaceProperty(
                    availability_zone="availabilityZone",
                    network_interface_id="networkInterfaceId",
                    private_ip_address="privateIpAddress",
                    subnet_id="subnetId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f524f99b7fb2ef102b93f5f0c5150e30d39dbec01779ff6af2bf97d2cd554c3)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
                check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if network_interface_id is not None:
                self._values["network_interface_id"] = network_interface_id
            if private_ip_address is not None:
                self._values["private_ip_address"] = private_ip_address
            if subnet_id is not None:
                self._values["subnet_id"] = subnet_id

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The Availability Zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html#cfn-redshift-endpointaccess-networkinterface-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_interface_id(self) -> typing.Optional[builtins.str]:
            '''The network interface identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html#cfn-redshift-endpointaccess-networkinterface-networkinterfaceid
            '''
            result = self._values.get("network_interface_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_ip_address(self) -> typing.Optional[builtins.str]:
            '''The IPv4 address of the network interface within the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html#cfn-redshift-endpointaccess-networkinterface-privateipaddress
            '''
            result = self._values.get("private_ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subnet_id(self) -> typing.Optional[builtins.str]:
            '''The subnet identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html#cfn-redshift-endpointaccess-networkinterface-subnetid
            '''
            result = self._values.get("subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAccess.VpcEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_interfaces": "networkInterfaces",
            "vpc_endpoint_id": "vpcEndpointId",
            "vpc_id": "vpcId",
        },
    )
    class VpcEndpointProperty:
        def __init__(
            self,
            *,
            network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpointAccess.NetworkInterfaceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vpc_endpoint_id: typing.Optional[builtins.str] = None,
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.

            :param network_interfaces: One or more network interfaces of the endpoint. Also known as an interface endpoint.
            :param vpc_endpoint_id: The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.
            :param vpc_id: The VPC identifier that the endpoint is associated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                vpc_endpoint_property = redshift.CfnEndpointAccess.VpcEndpointProperty(
                    network_interfaces=[redshift.CfnEndpointAccess.NetworkInterfaceProperty(
                        availability_zone="availabilityZone",
                        network_interface_id="networkInterfaceId",
                        private_ip_address="privateIpAddress",
                        subnet_id="subnetId"
                    )],
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2902c21df11cec99eebf3ccc4387bf8bdee8b12365a0c5b6de7e74f80a688c02)
                check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
                check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if network_interfaces is not None:
                self._values["network_interfaces"] = network_interfaces
            if vpc_endpoint_id is not None:
                self._values["vpc_endpoint_id"] = vpc_endpoint_id
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def network_interfaces(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEndpointAccess.NetworkInterfaceProperty"]]]]:
            '''One or more network interfaces of the endpoint.

            Also known as an interface endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html#cfn-redshift-endpointaccess-vpcendpoint-networkinterfaces
            '''
            result = self._values.get("network_interfaces")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEndpointAccess.NetworkInterfaceProperty"]]]], result)

        @builtins.property
        def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
            '''The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html#cfn-redshift-endpointaccess-vpcendpoint-vpcendpointid
            '''
            result = self._values.get("vpc_endpoint_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The VPC identifier that the endpoint is associated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html#cfn-redshift-endpointaccess-vpcendpoint-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAccess.VpcSecurityGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "status": "status",
            "vpc_security_group_id": "vpcSecurityGroupId",
        },
    )
    class VpcSecurityGroupProperty:
        def __init__(
            self,
            *,
            status: typing.Optional[builtins.str] = None,
            vpc_security_group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The security groups associated with the endpoint.

            :param status: The status of the endpoint.
            :param vpc_security_group_id: The identifier of the VPC security group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                vpc_security_group_property = redshift.CfnEndpointAccess.VpcSecurityGroupProperty(
                    status="status",
                    vpc_security_group_id="vpcSecurityGroupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__23ce7ea4c053267c6ffadf93ea9fe0811193cc5da011801b19256affd33ddb77)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument vpc_security_group_id", value=vpc_security_group_id, expected_type=type_hints["vpc_security_group_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if status is not None:
                self._values["status"] = status
            if vpc_security_group_id is not None:
                self._values["vpc_security_group_id"] = vpc_security_group_id

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html#cfn-redshift-endpointaccess-vpcsecuritygroup-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_security_group_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the VPC security group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html#cfn-redshift-endpointaccess-vpcsecuritygroup-vpcsecuritygroupid
            '''
            result = self._values.get("vpc_security_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSecurityGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAccessProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_identifier": "clusterIdentifier",
        "endpoint_name": "endpointName",
        "subnet_group_name": "subnetGroupName",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
        "resource_owner": "resourceOwner",
    },
)
class CfnEndpointAccessProps:
    def __init__(
        self,
        *,
        cluster_identifier: builtins.str,
        endpoint_name: builtins.str,
        subnet_group_name: builtins.str,
        vpc_security_group_ids: typing.Sequence[builtins.str],
        resource_owner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpointAccess``.

        :param cluster_identifier: The cluster identifier of the cluster associated with the endpoint.
        :param endpoint_name: The name of the endpoint.
        :param subnet_group_name: The subnet group name where Amazon Redshift chooses to deploy the endpoint.
        :param vpc_security_group_ids: The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
        :param resource_owner: The AWS account ID of the owner of the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_endpoint_access_props = redshift.CfnEndpointAccessProps(
                cluster_identifier="clusterIdentifier",
                endpoint_name="endpointName",
                subnet_group_name="subnetGroupName",
                vpc_security_group_ids=["vpcSecurityGroupIds"],
            
                # the properties below are optional
                resource_owner="resourceOwner"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb4208897e368488438ba6d463b7b2649df77c181ed9a0aabd7edf470cf9972e)
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
            check_type(argname="argument resource_owner", value=resource_owner, expected_type=type_hints["resource_owner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_identifier": cluster_identifier,
            "endpoint_name": endpoint_name,
            "subnet_group_name": subnet_group_name,
            "vpc_security_group_ids": vpc_security_group_ids,
        }
        if resource_owner is not None:
            self._values["resource_owner"] = resource_owner

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''The cluster identifier of the cluster associated with the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-clusteridentifier
        '''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_name(self) -> builtins.str:
        '''The name of the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-endpointname
        '''
        result = self._values.get("endpoint_name")
        assert result is not None, "Required property 'endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_group_name(self) -> builtins.str:
        '''The subnet group name where Amazon Redshift chooses to deploy the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-subnetgroupname
        '''
        result = self._values.get("subnet_group_name")
        assert result is not None, "Required property 'subnet_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        '''The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        assert result is not None, "Required property 'vpc_security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resource_owner(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of the owner of the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-resourceowner
        '''
        result = self._values.get("resource_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointAccessProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEndpointAuthorization(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAuthorization",
):
    '''Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_endpoint_authorization = redshift.CfnEndpointAuthorization(self, "MyCfnEndpointAuthorization",
            account="account",
            cluster_identifier="clusterIdentifier",
        
            # the properties below are optional
            force=False,
            vpc_ids=["vpcIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account: builtins.str,
        cluster_identifier: builtins.str,
        force: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account: The AWS account ID of either the cluster owner (grantor) or grantee. If ``Grantee`` parameter is true, then the ``Account`` value is of the grantor.
        :param cluster_identifier: The cluster identifier.
        :param force: Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
        :param vpc_ids: The virtual private cloud (VPC) identifiers to grant access to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a697bf6f03512c68c5e0bbce590548dfbef060e4ff37182e32221fef8c520a4b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointAuthorizationProps(
            account=account,
            cluster_identifier=cluster_identifier,
            force=force,
            vpc_ids=vpc_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e6beb6eda837ba911711251dade90e261ec5ed724ec65800b20c4a2b32c9449)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87cae2a0280923f1f80cdc272ebcb6a4e8967b591629416b23fb11f9a4d0a22d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAllowedAllVpCs")
    def attr_allowed_all_vp_cs(self) -> _IResolvable_da3f097b:
        '''Indicates whether all VPCs in the grantee account are allowed access to the cluster.

        :cloudformationAttribute: AllowedAllVPCs
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAllowedAllVpCs"))

    @builtins.property
    @jsii.member(jsii_name="attrAllowedVpCs")
    def attr_allowed_vp_cs(self) -> typing.List[builtins.str]:
        '''The VPCs allowed access to the cluster.

        :cloudformationAttribute: AllowedVPCs
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAllowedVpCs"))

    @builtins.property
    @jsii.member(jsii_name="attrAuthorizeTime")
    def attr_authorize_time(self) -> builtins.str:
        '''The time (UTC) when the authorization was created.

        :cloudformationAttribute: AuthorizeTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAuthorizeTime"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterStatus")
    def attr_cluster_status(self) -> builtins.str:
        '''The status of the cluster.

        :cloudformationAttribute: ClusterStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointCount")
    def attr_endpoint_count(self) -> jsii.Number:
        '''The number of Redshift-managed VPC endpoints created for the authorization.

        :cloudformationAttribute: EndpointCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrEndpointCount"))

    @builtins.property
    @jsii.member(jsii_name="attrGrantee")
    def attr_grantee(self) -> builtins.str:
        '''The AWS account ID of the grantee of the cluster.

        :cloudformationAttribute: Grantee
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGrantee"))

    @builtins.property
    @jsii.member(jsii_name="attrGrantor")
    def attr_grantor(self) -> builtins.str:
        '''The AWS account ID of the cluster owner.

        :cloudformationAttribute: Grantor
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGrantor"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the authorization action.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> builtins.str:
        '''The AWS account ID of either the cluster owner (grantor) or grantee.'''
        return typing.cast(builtins.str, jsii.get(self, "account"))

    @account.setter
    def account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f81bbdc996078876480c43faffb9de86d575fc88c6b656e90a94b8c10a590bec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''The cluster identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0292d1d6b28ec2ce775f401aaaa3a27fe8c4924b8f4243147138b636fdbe11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="force")
    def force(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to force the revoke action.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "force"))

    @force.setter
    def force(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3418ce19499db041cb3822978572e2eeb561625f2fdc69d4a3663277a760194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "force", value)

    @builtins.property
    @jsii.member(jsii_name="vpcIds")
    def vpc_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The virtual private cloud (VPC) identifiers to grant access to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcIds"))

    @vpc_ids.setter
    def vpc_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a14605f174b24a5f18a5630ff894d214b1bfc4e05f8b83234828a27504c0c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcIds", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAuthorizationProps",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "cluster_identifier": "clusterIdentifier",
        "force": "force",
        "vpc_ids": "vpcIds",
    },
)
class CfnEndpointAuthorizationProps:
    def __init__(
        self,
        *,
        account: builtins.str,
        cluster_identifier: builtins.str,
        force: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpointAuthorization``.

        :param account: The AWS account ID of either the cluster owner (grantor) or grantee. If ``Grantee`` parameter is true, then the ``Account`` value is of the grantor.
        :param cluster_identifier: The cluster identifier.
        :param force: Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
        :param vpc_ids: The virtual private cloud (VPC) identifiers to grant access to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_endpoint_authorization_props = redshift.CfnEndpointAuthorizationProps(
                account="account",
                cluster_identifier="clusterIdentifier",
            
                # the properties below are optional
                force=False,
                vpc_ids=["vpcIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea42c43e99e9da3eea3440151d10e74f104e3b13161b1b46186517cdfb455151)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
            check_type(argname="argument vpc_ids", value=vpc_ids, expected_type=type_hints["vpc_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "cluster_identifier": cluster_identifier,
        }
        if force is not None:
            self._values["force"] = force
        if vpc_ids is not None:
            self._values["vpc_ids"] = vpc_ids

    @builtins.property
    def account(self) -> builtins.str:
        '''The AWS account ID of either the cluster owner (grantor) or grantee.

        If ``Grantee`` parameter is true, then the ``Account`` value is of the grantor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-account
        '''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''The cluster identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-clusteridentifier
        '''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def force(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to force the revoke action.

        If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-force
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def vpc_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The virtual private cloud (VPC) identifiers to grant access to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-vpcids
        '''
        result = self._values.get("vpc_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointAuthorizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEventSubscription(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnEventSubscription",
):
    '''The ``AWS::Redshift::EventSubscription`` resource creates an Amazon Redshift Event Subscription.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_event_subscription = redshift.CfnEventSubscription(self, "MyCfnEventSubscription",
            subscription_name="subscriptionName",
        
            # the properties below are optional
            enabled=False,
            event_categories=["eventCategories"],
            severity="severity",
            sns_topic_arn="snsTopicArn",
            source_ids=["sourceIds"],
            source_type="sourceType",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        subscription_name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        severity: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param subscription_name: The name of the event subscription to be created. Constraints: - Cannot be null, empty, or blank. - Must contain from 1 to 255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param enabled: A boolean value; set to ``true`` to activate the subscription, and set to ``false`` to create the subscription but not activate it.
        :param event_categories: Specifies the Amazon Redshift event categories to be published by the event notification subscription. Values: configuration, management, monitoring, security, pending
        :param severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription. Values: ERROR, INFO
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        :param source_ids: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified. Example: my-cluster-1, my-cluster-2 Example: my-snapshot-20131010
        :param source_type: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account . You must specify a source type in order to specify source IDs. Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.
        :param tags: A list of tag instances.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2321a5fed3334265b97838abad90fad948fa6670da0259ba7e0d24e88326fdd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventSubscriptionProps(
            subscription_name=subscription_name,
            enabled=enabled,
            event_categories=event_categories,
            severity=severity,
            sns_topic_arn=sns_topic_arn,
            source_ids=source_ids,
            source_type=source_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a03817fc18a5081cfca50722e5b1bcd4346b2500146a8d3c9fb58b226dab6fe4)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5380330c3f2bfa84f009dcca8a5550163665b16f1e8cc20ab09ad3a87750572d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCustomerAwsId")
    def attr_customer_aws_id(self) -> builtins.str:
        '''The AWS account associated with the Amazon Redshift event notification subscription.

        :cloudformationAttribute: CustomerAwsId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCustomerAwsId"))

    @builtins.property
    @jsii.member(jsii_name="attrCustSubscriptionId")
    def attr_cust_subscription_id(self) -> builtins.str:
        '''The name of the Amazon Redshift event notification subscription.

        :cloudformationAttribute: CustSubscriptionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCustSubscriptionId"))

    @builtins.property
    @jsii.member(jsii_name="attrEventCategoriesList")
    def attr_event_categories_list(self) -> typing.List[builtins.str]:
        '''The list of Amazon Redshift event categories specified in the event notification subscription.

        Values: Configuration, Management, Monitoring, Security, Pending

        :cloudformationAttribute: EventCategoriesList
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrEventCategoriesList"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceIdsList")
    def attr_source_ids_list(self) -> typing.List[builtins.str]:
        '''A list of the sources that publish events to the Amazon Redshift event notification subscription.

        :cloudformationAttribute: SourceIdsList
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSourceIdsList"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the Amazon Redshift event notification subscription.

        Constraints:

        - Can be one of the following: active | no-permission | topic-not-exist
        - The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrSubscriptionCreationTime")
    def attr_subscription_creation_time(self) -> builtins.str:
        '''The date and time the Amazon Redshift event notification subscription was created.

        :cloudformationAttribute: SubscriptionCreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSubscriptionCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionName")
    def subscription_name(self) -> builtins.str:
        '''The name of the event subscription to be created.'''
        return typing.cast(builtins.str, jsii.get(self, "subscriptionName"))

    @subscription_name.setter
    def subscription_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a6536d2dfac6abba560620e836213d5803aa8693e746ce5cbe8466802804ab2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A boolean value;'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea0cdf4a4de28abdd520f9b940b88096f2cf47a52a4e567f3499f9de63decbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventCategories")
    def event_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the Amazon Redshift event categories to be published by the event notification subscription.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventCategories"))

    @event_categories.setter
    def event_categories(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d52d3ea63d12acdf3723584b75502be9430562d66c6d2064ab04e9cc95304748)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventCategories", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Redshift event severity to be published by the event notification subscription.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08ce190a2e94a8276e315d45400484671c991298d1b7d3b8f33ad62f868b3578)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__120fc22c19a6b33fb57b31a06d8c453b9211739cf86ffc8e6ec5d9a28b6f82ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIds")
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of one or more identifiers of Amazon Redshift source objects.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIds"))

    @source_ids.setter
    def source_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4608ccfe8b64fe9afee3e34458b1bc213f6339b18a11a53005b3c43906eca137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> typing.Optional[builtins.str]:
        '''The type of source that will be generating the events.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e1fdab050622407fbbf867b34ce949080facef4619e33c1535fd1e620441ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tag instances.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f8d017fb369cae60fd6db670e2d0711cfe832e31a2eb08dc7c90f07ddc39eaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnEventSubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "subscription_name": "subscriptionName",
        "enabled": "enabled",
        "event_categories": "eventCategories",
        "severity": "severity",
        "sns_topic_arn": "snsTopicArn",
        "source_ids": "sourceIds",
        "source_type": "sourceType",
        "tags": "tags",
    },
)
class CfnEventSubscriptionProps:
    def __init__(
        self,
        *,
        subscription_name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        severity: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventSubscription``.

        :param subscription_name: The name of the event subscription to be created. Constraints: - Cannot be null, empty, or blank. - Must contain from 1 to 255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param enabled: A boolean value; set to ``true`` to activate the subscription, and set to ``false`` to create the subscription but not activate it.
        :param event_categories: Specifies the Amazon Redshift event categories to be published by the event notification subscription. Values: configuration, management, monitoring, security, pending
        :param severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription. Values: ERROR, INFO
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        :param source_ids: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified. Example: my-cluster-1, my-cluster-2 Example: my-snapshot-20131010
        :param source_type: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account . You must specify a source type in order to specify source IDs. Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.
        :param tags: A list of tag instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_event_subscription_props = redshift.CfnEventSubscriptionProps(
                subscription_name="subscriptionName",
            
                # the properties below are optional
                enabled=False,
                event_categories=["eventCategories"],
                severity="severity",
                sns_topic_arn="snsTopicArn",
                source_ids=["sourceIds"],
                source_type="sourceType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__882750ef34f06482c6644922124100661565513fabbad49eed142788cd66cfa8)
            check_type(argname="argument subscription_name", value=subscription_name, expected_type=type_hints["subscription_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument event_categories", value=event_categories, expected_type=type_hints["event_categories"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument source_ids", value=source_ids, expected_type=type_hints["source_ids"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscription_name": subscription_name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if event_categories is not None:
            self._values["event_categories"] = event_categories
        if severity is not None:
            self._values["severity"] = severity
        if sns_topic_arn is not None:
            self._values["sns_topic_arn"] = sns_topic_arn
        if source_ids is not None:
            self._values["source_ids"] = source_ids
        if source_type is not None:
            self._values["source_type"] = source_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def subscription_name(self) -> builtins.str:
        '''The name of the event subscription to be created.

        Constraints:

        - Cannot be null, empty, or blank.
        - Must contain from 1 to 255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-subscriptionname
        '''
        result = self._values.get("subscription_name")
        assert result is not None, "Required property 'subscription_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A boolean value;

        set to ``true`` to activate the subscription, and set to ``false`` to create the subscription but not activate it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def event_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the Amazon Redshift event categories to be published by the event notification subscription.

        Values: configuration, management, monitoring, security, pending

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-eventcategories
        '''
        result = self._values.get("event_categories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def severity(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Redshift event severity to be published by the event notification subscription.

        Values: ERROR, INFO

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-severity
        '''
        result = self._values.get("severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.

        The ARN is created by Amazon SNS when you create a topic and subscribe to it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of one or more identifiers of Amazon Redshift source objects.

        All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.

        Example: my-cluster-1, my-cluster-2

        Example: my-snapshot-20131010

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-sourceids
        '''
        result = self._values.get("source_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_type(self) -> typing.Optional[builtins.str]:
        '''The type of source that will be generating the events.

        For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account . You must specify a source type in order to specify source IDs.

        Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-sourcetype
        '''
        result = self._values.get("source_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tag instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnScheduledAction(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnScheduledAction",
):
    '''Creates a scheduled action.

    A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the ``ResizeCluster`` API operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_scheduled_action = redshift.CfnScheduledAction(self, "MyCfnScheduledAction",
            scheduled_action_name="scheduledActionName",
        
            # the properties below are optional
            enable=False,
            end_time="endTime",
            iam_role="iamRole",
            schedule="schedule",
            scheduled_action_description="scheduledActionDescription",
            start_time="startTime",
            target_action=redshift.CfnScheduledAction.ScheduledActionTypeProperty(
                pause_cluster=redshift.CfnScheduledAction.PauseClusterMessageProperty(
                    cluster_identifier="clusterIdentifier"
                ),
                resize_cluster=redshift.CfnScheduledAction.ResizeClusterMessageProperty(
                    cluster_identifier="clusterIdentifier",
        
                    # the properties below are optional
                    classic=False,
                    cluster_type="clusterType",
                    node_type="nodeType",
                    number_of_nodes=123
                ),
                resume_cluster=redshift.CfnScheduledAction.ResumeClusterMessageProperty(
                    cluster_identifier="clusterIdentifier"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        scheduled_action_name: builtins.str,
        enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        end_time: typing.Optional[builtins.str] = None,
        iam_role: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        scheduled_action_description: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        target_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledAction.ScheduledActionTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param scheduled_action_name: The name of the scheduled action.
        :param enable: If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about ``state`` of the scheduled action, see ``ScheduledAction`` .
        :param end_time: The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.
        :param iam_role: The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see `Using Identity-Based Policies for Amazon Redshift <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html>`_ in the *Amazon Redshift Cluster Management Guide* .
        :param schedule: The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Format of at expressions is " ``at(yyyy-mm-ddThh:mm:ss)`` ". For example, " ``at(2016-03-04T17:27:00)`` ". Format of cron expressions is " ``cron(Minutes Hours Day-of-month Month Day-of-week Year)`` ". For example, " ``cron(0 10 ? * MON *)`` ". For more information, see `Cron Expressions <https://docs.aws.amazon.com//AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`_ in the *Amazon CloudWatch Events User Guide* .
        :param scheduled_action_description: The description of the scheduled action.
        :param start_time: The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.
        :param target_action: A JSON format string of the Amazon Redshift API operation with input parameters. " ``{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}}`` ".
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b090f5bcac0321af743a2821b9b20cd050f984204fe9b5d4288918250e146d1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduledActionProps(
            scheduled_action_name=scheduled_action_name,
            enable=enable,
            end_time=end_time,
            iam_role=iam_role,
            schedule=schedule,
            scheduled_action_description=scheduled_action_description,
            start_time=start_time,
            target_action=target_action,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f309d088dd02a60f73f2f52762d748233f12e881a051aee387a69f7a54940d38)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5bed46ce545be8a344aa860129865dc4fdbf8bf1a4e1729c699750cc1b8853c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrNextInvocations")
    def attr_next_invocations(self) -> typing.List[builtins.str]:
        '''List of times when the scheduled action will run.

        :cloudformationAttribute: NextInvocations
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNextInvocations"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the scheduled action.

        For example, ``DISABLED`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="scheduledActionName")
    def scheduled_action_name(self) -> builtins.str:
        '''The name of the scheduled action.'''
        return typing.cast(builtins.str, jsii.get(self, "scheduledActionName"))

    @scheduled_action_name.setter
    def scheduled_action_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__872bb8f14b5c5de39d86d09c67159a166a6945e80b42d8739ecc9b58ae6ddbd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledActionName", value)

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If true, the schedule is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enable"))

    @enable.setter
    def enable(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d91d9501f12e1db3372aea6023ac844c09772ef705ec20f4e25cb2a1b9febd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> typing.Optional[builtins.str]:
        '''The end time in UTC when the schedule is no longer active.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c0fa066a9596f001c1203f3253634dbe6d284bc1f95dcb4ad5fd93b943f900)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="iamRole")
    def iam_role(self) -> typing.Optional[builtins.str]:
        '''The IAM role to assume to run the scheduled action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRole"))

    @iam_role.setter
    def iam_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e240c42ffd0653ef9c64e552ae856adb8e46ef1e7445e0c799b2d0fb51a73b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRole", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> typing.Optional[builtins.str]:
        '''The schedule for a one-time (at format) or recurring (cron format) scheduled action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__366bc157c377add120d344d662266845f682e125b0b0becc420c2ad8f012b7f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledActionDescription")
    def scheduled_action_description(self) -> typing.Optional[builtins.str]:
        '''The description of the scheduled action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduledActionDescription"))

    @scheduled_action_description.setter
    def scheduled_action_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94211d9fae42e57e02c956e8f7d0b69f6fe20e2302f5eb33117e7999a3762703)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledActionDescription", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> typing.Optional[builtins.str]:
        '''The start time in UTC when the schedule is active.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f13602601a3ed50e4b17c16a24c1a91206f10e208fad90a5e8f6ad4590662c8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="targetAction")
    def target_action(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.ScheduledActionTypeProperty"]]:
        '''A JSON format string of the Amazon Redshift API operation with input parameters.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.ScheduledActionTypeProperty"]], jsii.get(self, "targetAction"))

    @target_action.setter
    def target_action(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.ScheduledActionTypeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37dee953d9dbcdfb3a7265aa1538c058a9dde8ebabb0b409a0151155cacc75c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetAction", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnScheduledAction.PauseClusterMessageProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_identifier": "clusterIdentifier"},
    )
    class PauseClusterMessageProperty:
        def __init__(self, *, cluster_identifier: builtins.str) -> None:
            '''Describes a pause cluster operation.

            For example, a scheduled action to run the ``PauseCluster`` API operation.

            :param cluster_identifier: The identifier of the cluster to be paused.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-pauseclustermessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                pause_cluster_message_property = redshift.CfnScheduledAction.PauseClusterMessageProperty(
                    cluster_identifier="clusterIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d9de594935dd2c45b02090ed3f1a15ec7c1dd2188d0620a5fd7867737ec5417)
                check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_identifier": cluster_identifier,
            }

        @builtins.property
        def cluster_identifier(self) -> builtins.str:
            '''The identifier of the cluster to be paused.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-pauseclustermessage.html#cfn-redshift-scheduledaction-pauseclustermessage-clusteridentifier
            '''
            result = self._values.get("cluster_identifier")
            assert result is not None, "Required property 'cluster_identifier' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PauseClusterMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnScheduledAction.ResizeClusterMessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_identifier": "clusterIdentifier",
            "classic": "classic",
            "cluster_type": "clusterType",
            "node_type": "nodeType",
            "number_of_nodes": "numberOfNodes",
        },
    )
    class ResizeClusterMessageProperty:
        def __init__(
            self,
            *,
            cluster_identifier: builtins.str,
            classic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            cluster_type: typing.Optional[builtins.str] = None,
            node_type: typing.Optional[builtins.str] = None,
            number_of_nodes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes a resize cluster operation.

            For example, a scheduled action to run the ``ResizeCluster`` API operation.

            :param cluster_identifier: The unique identifier for the cluster to resize.
            :param classic: A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.
            :param cluster_type: The new cluster type for the specified cluster.
            :param node_type: The new node type for the nodes you are adding. If not specified, the cluster's current node type is used.
            :param number_of_nodes: The new number of nodes for the cluster. If not specified, the cluster's current number of nodes is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                resize_cluster_message_property = redshift.CfnScheduledAction.ResizeClusterMessageProperty(
                    cluster_identifier="clusterIdentifier",
                
                    # the properties below are optional
                    classic=False,
                    cluster_type="clusterType",
                    node_type="nodeType",
                    number_of_nodes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eebc6afccb22ead40bc9246f8233bd603d435e1b55a37a3aec3f29c6ec7e14e0)
                check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
                check_type(argname="argument classic", value=classic, expected_type=type_hints["classic"])
                check_type(argname="argument cluster_type", value=cluster_type, expected_type=type_hints["cluster_type"])
                check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
                check_type(argname="argument number_of_nodes", value=number_of_nodes, expected_type=type_hints["number_of_nodes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_identifier": cluster_identifier,
            }
            if classic is not None:
                self._values["classic"] = classic
            if cluster_type is not None:
                self._values["cluster_type"] = cluster_type
            if node_type is not None:
                self._values["node_type"] = node_type
            if number_of_nodes is not None:
                self._values["number_of_nodes"] = number_of_nodes

        @builtins.property
        def cluster_identifier(self) -> builtins.str:
            '''The unique identifier for the cluster to resize.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-clusteridentifier
            '''
            result = self._values.get("cluster_identifier")
            assert result is not None, "Required property 'cluster_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def classic(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A boolean value indicating whether the resize operation is using the classic resize process.

            If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-classic
            '''
            result = self._values.get("classic")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def cluster_type(self) -> typing.Optional[builtins.str]:
            '''The new cluster type for the specified cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-clustertype
            '''
            result = self._values.get("cluster_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def node_type(self) -> typing.Optional[builtins.str]:
            '''The new node type for the nodes you are adding.

            If not specified, the cluster's current node type is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-nodetype
            '''
            result = self._values.get("node_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def number_of_nodes(self) -> typing.Optional[jsii.Number]:
            '''The new number of nodes for the cluster.

            If not specified, the cluster's current number of nodes is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-numberofnodes
            '''
            result = self._values.get("number_of_nodes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResizeClusterMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnScheduledAction.ResumeClusterMessageProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_identifier": "clusterIdentifier"},
    )
    class ResumeClusterMessageProperty:
        def __init__(self, *, cluster_identifier: builtins.str) -> None:
            '''Describes a resume cluster operation.

            For example, a scheduled action to run the ``ResumeCluster`` API operation.

            :param cluster_identifier: The identifier of the cluster to be resumed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resumeclustermessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                resume_cluster_message_property = redshift.CfnScheduledAction.ResumeClusterMessageProperty(
                    cluster_identifier="clusterIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf516288cb4d8f79c051b1547fbb68f2eb5395600f53e173adbf24e5978510e6)
                check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_identifier": cluster_identifier,
            }

        @builtins.property
        def cluster_identifier(self) -> builtins.str:
            '''The identifier of the cluster to be resumed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resumeclustermessage.html#cfn-redshift-scheduledaction-resumeclustermessage-clusteridentifier
            '''
            result = self._values.get("cluster_identifier")
            assert result is not None, "Required property 'cluster_identifier' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResumeClusterMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnScheduledAction.ScheduledActionTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pause_cluster": "pauseCluster",
            "resize_cluster": "resizeCluster",
            "resume_cluster": "resumeCluster",
        },
    )
    class ScheduledActionTypeProperty:
        def __init__(
            self,
            *,
            pause_cluster: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledAction.PauseClusterMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resize_cluster: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledAction.ResizeClusterMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resume_cluster: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledAction.ResumeClusterMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The action type that specifies an Amazon Redshift API operation that is supported by the Amazon Redshift scheduler.

            :param pause_cluster: An action that runs a ``PauseCluster`` API operation.
            :param resize_cluster: An action that runs a ``ResizeCluster`` API operation.
            :param resume_cluster: An action that runs a ``ResumeCluster`` API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                scheduled_action_type_property = redshift.CfnScheduledAction.ScheduledActionTypeProperty(
                    pause_cluster=redshift.CfnScheduledAction.PauseClusterMessageProperty(
                        cluster_identifier="clusterIdentifier"
                    ),
                    resize_cluster=redshift.CfnScheduledAction.ResizeClusterMessageProperty(
                        cluster_identifier="clusterIdentifier",
                
                        # the properties below are optional
                        classic=False,
                        cluster_type="clusterType",
                        node_type="nodeType",
                        number_of_nodes=123
                    ),
                    resume_cluster=redshift.CfnScheduledAction.ResumeClusterMessageProperty(
                        cluster_identifier="clusterIdentifier"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d636da52cf59446f020e242a88d41b50e55ef8273a113c78f968a7fe23c05cdb)
                check_type(argname="argument pause_cluster", value=pause_cluster, expected_type=type_hints["pause_cluster"])
                check_type(argname="argument resize_cluster", value=resize_cluster, expected_type=type_hints["resize_cluster"])
                check_type(argname="argument resume_cluster", value=resume_cluster, expected_type=type_hints["resume_cluster"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pause_cluster is not None:
                self._values["pause_cluster"] = pause_cluster
            if resize_cluster is not None:
                self._values["resize_cluster"] = resize_cluster
            if resume_cluster is not None:
                self._values["resume_cluster"] = resume_cluster

        @builtins.property
        def pause_cluster(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.PauseClusterMessageProperty"]]:
            '''An action that runs a ``PauseCluster`` API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html#cfn-redshift-scheduledaction-scheduledactiontype-pausecluster
            '''
            result = self._values.get("pause_cluster")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.PauseClusterMessageProperty"]], result)

        @builtins.property
        def resize_cluster(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.ResizeClusterMessageProperty"]]:
            '''An action that runs a ``ResizeCluster`` API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html#cfn-redshift-scheduledaction-scheduledactiontype-resizecluster
            '''
            result = self._values.get("resize_cluster")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.ResizeClusterMessageProperty"]], result)

        @builtins.property
        def resume_cluster(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.ResumeClusterMessageProperty"]]:
            '''An action that runs a ``ResumeCluster`` API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html#cfn-redshift-scheduledaction-scheduledactiontype-resumecluster
            '''
            result = self._values.get("resume_cluster")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledAction.ResumeClusterMessageProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduledActionTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnScheduledActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "scheduled_action_name": "scheduledActionName",
        "enable": "enable",
        "end_time": "endTime",
        "iam_role": "iamRole",
        "schedule": "schedule",
        "scheduled_action_description": "scheduledActionDescription",
        "start_time": "startTime",
        "target_action": "targetAction",
    },
)
class CfnScheduledActionProps:
    def __init__(
        self,
        *,
        scheduled_action_name: builtins.str,
        enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        end_time: typing.Optional[builtins.str] = None,
        iam_role: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        scheduled_action_description: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        target_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledAction.ScheduledActionTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScheduledAction``.

        :param scheduled_action_name: The name of the scheduled action.
        :param enable: If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about ``state`` of the scheduled action, see ``ScheduledAction`` .
        :param end_time: The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.
        :param iam_role: The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see `Using Identity-Based Policies for Amazon Redshift <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html>`_ in the *Amazon Redshift Cluster Management Guide* .
        :param schedule: The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Format of at expressions is " ``at(yyyy-mm-ddThh:mm:ss)`` ". For example, " ``at(2016-03-04T17:27:00)`` ". Format of cron expressions is " ``cron(Minutes Hours Day-of-month Month Day-of-week Year)`` ". For example, " ``cron(0 10 ? * MON *)`` ". For more information, see `Cron Expressions <https://docs.aws.amazon.com//AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`_ in the *Amazon CloudWatch Events User Guide* .
        :param scheduled_action_description: The description of the scheduled action.
        :param start_time: The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.
        :param target_action: A JSON format string of the Amazon Redshift API operation with input parameters. " ``{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}}`` ".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_scheduled_action_props = redshift.CfnScheduledActionProps(
                scheduled_action_name="scheduledActionName",
            
                # the properties below are optional
                enable=False,
                end_time="endTime",
                iam_role="iamRole",
                schedule="schedule",
                scheduled_action_description="scheduledActionDescription",
                start_time="startTime",
                target_action=redshift.CfnScheduledAction.ScheduledActionTypeProperty(
                    pause_cluster=redshift.CfnScheduledAction.PauseClusterMessageProperty(
                        cluster_identifier="clusterIdentifier"
                    ),
                    resize_cluster=redshift.CfnScheduledAction.ResizeClusterMessageProperty(
                        cluster_identifier="clusterIdentifier",
            
                        # the properties below are optional
                        classic=False,
                        cluster_type="clusterType",
                        node_type="nodeType",
                        number_of_nodes=123
                    ),
                    resume_cluster=redshift.CfnScheduledAction.ResumeClusterMessageProperty(
                        cluster_identifier="clusterIdentifier"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b8f33670db3a11840dd3dde7157d6c714dfbdf357d1a2d7ffab1191d271b169)
            check_type(argname="argument scheduled_action_name", value=scheduled_action_name, expected_type=type_hints["scheduled_action_name"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument scheduled_action_description", value=scheduled_action_description, expected_type=type_hints["scheduled_action_description"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument target_action", value=target_action, expected_type=type_hints["target_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scheduled_action_name": scheduled_action_name,
        }
        if enable is not None:
            self._values["enable"] = enable
        if end_time is not None:
            self._values["end_time"] = end_time
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if schedule is not None:
            self._values["schedule"] = schedule
        if scheduled_action_description is not None:
            self._values["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            self._values["start_time"] = start_time
        if target_action is not None:
            self._values["target_action"] = target_action

    @builtins.property
    def scheduled_action_name(self) -> builtins.str:
        '''The name of the scheduled action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-scheduledactionname
        '''
        result = self._values.get("scheduled_action_name")
        assert result is not None, "Required property 'scheduled_action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If true, the schedule is enabled.

        If false, the scheduled action does not trigger. For more information about ``state`` of the scheduled action, see ``ScheduledAction`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-enable
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''The end time in UTC when the schedule is no longer active.

        After this time, the scheduled action does not trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-endtime
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role(self) -> typing.Optional[builtins.str]:
        '''The IAM role to assume to run the scheduled action.

        This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see `Using Identity-Based Policies for Amazon Redshift <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html>`_ in the *Amazon Redshift Cluster Management Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-iamrole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''The schedule for a one-time (at format) or recurring (cron format) scheduled action.

        Schedule invocations must be separated by at least one hour.

        Format of at expressions is " ``at(yyyy-mm-ddThh:mm:ss)`` ". For example, " ``at(2016-03-04T17:27:00)`` ".

        Format of cron expressions is " ``cron(Minutes Hours Day-of-month Month Day-of-week Year)`` ". For example, " ``cron(0 10 ? * MON *)`` ". For more information, see `Cron Expressions <https://docs.aws.amazon.com//AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`_ in the *Amazon CloudWatch Events User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduled_action_description(self) -> typing.Optional[builtins.str]:
        '''The description of the scheduled action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-scheduledactiondescription
        '''
        result = self._values.get("scheduled_action_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''The start time in UTC when the schedule is active.

        Before this time, the scheduled action does not trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-starttime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_action(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScheduledAction.ScheduledActionTypeProperty]]:
        '''A JSON format string of the Amazon Redshift API operation with input parameters.

        " ``{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}}`` ".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-targetaction
        '''
        result = self._values.get("target_action")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScheduledAction.ScheduledActionTypeProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduledActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterParameterGroup",
    "CfnClusterParameterGroupProps",
    "CfnClusterProps",
    "CfnClusterSecurityGroup",
    "CfnClusterSecurityGroupIngress",
    "CfnClusterSecurityGroupIngressProps",
    "CfnClusterSecurityGroupProps",
    "CfnClusterSubnetGroup",
    "CfnClusterSubnetGroupProps",
    "CfnEndpointAccess",
    "CfnEndpointAccessProps",
    "CfnEndpointAuthorization",
    "CfnEndpointAuthorizationProps",
    "CfnEventSubscription",
    "CfnEventSubscriptionProps",
    "CfnScheduledAction",
    "CfnScheduledActionProps",
]

publication.publish()

def _typecheckingstub__f6d25f70797e3ae67b635ec776926582ff0be975c8173c4af217f7f6e3bd404b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_type: builtins.str,
    db_name: builtins.str,
    master_username: builtins.str,
    master_user_password: builtins.str,
    node_type: builtins.str,
    allow_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    aqua_configuration_status: typing.Optional[builtins.str] = None,
    automated_snapshot_retention_period: typing.Optional[jsii.Number] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    availability_zone_relocation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    availability_zone_relocation_status: typing.Optional[builtins.str] = None,
    classic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cluster_identifier: typing.Optional[builtins.str] = None,
    cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    cluster_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    cluster_subnet_group_name: typing.Optional[builtins.str] = None,
    cluster_version: typing.Optional[builtins.str] = None,
    defer_maintenance: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    defer_maintenance_duration: typing.Optional[jsii.Number] = None,
    defer_maintenance_end_time: typing.Optional[builtins.str] = None,
    defer_maintenance_start_time: typing.Optional[builtins.str] = None,
    destination_region: typing.Optional[builtins.str] = None,
    elastic_ip: typing.Optional[builtins.str] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    hsm_client_certificate_identifier: typing.Optional[builtins.str] = None,
    hsm_configuration_identifier: typing.Optional[builtins.str] = None,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    logging_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.LoggingPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maintenance_track_name: typing.Optional[builtins.str] = None,
    manual_snapshot_retention_period: typing.Optional[jsii.Number] = None,
    number_of_nodes: typing.Optional[jsii.Number] = None,
    owner_account: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    resource_action: typing.Optional[builtins.str] = None,
    revision_target: typing.Optional[builtins.str] = None,
    rotate_encryption_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    snapshot_cluster_identifier: typing.Optional[builtins.str] = None,
    snapshot_copy_grant_name: typing.Optional[builtins.str] = None,
    snapshot_copy_manual: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    snapshot_copy_retention_period: typing.Optional[jsii.Number] = None,
    snapshot_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df99dcbb5445a88a0bb9445a37f1ba9bcd5cf462c2a8d8f24a91415f085d07a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3cd522d882ff9ce54b9361b6991edd7e86d6cb4b5b0fd3d4f0ff14a1dc41eb7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b228c18c00d6efcc3f5f513f526c5588459dbc4716e98017abe3c85b8869edcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9a6569f04f712a8617c29ce39f051b6b7718c2759016fd8c2a5129f2c3a9fc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d32dd6d1faa4bf4d38fbc9173d77c54548a2fb5386ec97451b20f4a4e928001a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15113bc0292eb3a900fcad9d620cd08c320a19dfce07db8d055112a353c48cba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd39ef012e3b964f5c72dcc3385a8861f7af2aed9a450ea99e69c540c77b2af3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ca48fbd412a24c0cb2a878179eca6e182ee7d8c69be5b4dbcc9862b44f73c1(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cdce8be072a8ad4655038a048a780e28c874f470b860ba5efeeb19c470e71b0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed5582d6104bfbddace4e373fcab8d459431100b894b1a16de7955842e400de2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c65bcbcfa0b5c942ee2dc4ddc36123d19ebb2e20f61c7d530335b08b87aa98e0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b7e4b7b94737e4e8b1853309ee5372d1269f37dcf09d4ee449f352e5c55c0c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6634fb9f81aef0b48d0404fc2c8ec19d02a04b1a9d7c65863692e53f28a978b6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86549952f63853b3a6d50c0ea714bcad7fc4bcbeea239762fe3bc3035e81531(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d01d7ad2f21e729a4d05a6c6c40c03bbeff0a26976f99e7487e40fe7c6aec7e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b14873e72b628e6b816d839111208ef6aa6af543ebe87c8be7b488ef5566b602(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a651f09ef507bb8529243e4a1dc4c6db1ed0753b890fafe63aa18f8ed2fed90c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a6de3cf6594b7e052bda7985e485f86e4d3c373ccc8db3221e45f5e1dd17325(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55a998895e7e966b871bd67fe918e51ba3671e2c2b298eb8eb34d7f51d07206e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4237433b5883296c8faff34d0e01925a666684fbee40ec2906e948a41d50e503(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38793f2500254714c6067bec6f72a5a038c50d8bc9b6b03b375518dce428a13(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__707a603887573fd509d9f52453e8a586dcbece345650487f919175b7a32ce0f1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd9fc695606c0a941294d8fb46b82ad186d9cc0f1ceecc9efea154fa51e57d2b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9affeaf50223bc3ddba02727393f5841690e26871908e7f312f79f76ce20857c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af4905b0871175bb94d0e68d7844830025c4dfe81acb2f97d60012f417d079f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b1075c71946fea633b06672f811d3ed06a3627779b2123983ff2dbad9432e7(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91af587b7f602d533107461b26deea688b9ac30f8cff34b2f281da70b5f20be0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.EndpointProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f39b0b2b5df52249767c8cb6463c876078868c14687667fd735f0b6d22fb18(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5024cde1beb60571770fd7108dbe12a4a475dfeac6bf7a1e1027e2081e58e486(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23dbabcc0b1bd43d467873c3ad184988bc516c60957ee94cf9abaf50268fff8d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772c14b10e457f7456acacbd7c571e904d8d7e32ccc4be7e64dfdc23417fd3e0(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b9e3255675fa581da5945ef20b026be1c2c1fc9d1bad30a7bf9c5e63e884f60(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faccaac60f090449dba9f2adeeb99fa490f6f2532ea91a0f5372422d57002f26(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.LoggingPropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdec41d5a2f886a294c35cbf10b6f505571be31e2c00a5a1c57a87a34cf49426(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47928702ad781fa3915ff0f5068c3b692ff5d8d891b871ca8319d3632cdffe22(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b646aacda3a7612936e7568c66769cf203d6286890366d0346d5c38410b0d8b3(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52bf6c5c1ccac8e9a203c7d7459384ca20fe2bd847c219060b148ce817130552(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a336566c0c0ca699ff01424a213ca87bb14f46bd413f3548c40bf33f2efa36b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9692ea98b60bb6630f40e5fdbf329c062ea1111b09de0a06388619337bba7451(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da6f0bb2273ecadf755efeb5a905c9ee82720866a8ce8f61a2c6d3d21eb9300b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb4e2cacc7f73b63f83b3db029d401ee0e2b0f5ba058212b603e71548aac621(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a194ca9d86844bb3b3e45b505b5c6b5cfc6e7394cda5b168c597edf84cd5a57(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bf5df20a75b52e1cdb3d7517d4cb1b82f3940133ad5667db9df487314abf2a2(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02d3c6ace6da2f11c5895ef3151ab4e22925463fd7aa7f5ae7818e0ad18d5ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b48178e0c2c9351bf3494f98a7ba9056b7d4796545f2aee976d0338e14e8eb3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f25e386153f816099eeca0eba6c12a2141a4398dd600a4a5bcfba56a506c9c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d1d0fe426ee03be5f64341988115cbe1d5afd95c0b6861542b95a8abb56740(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cba9391bc97d92920ae3a792b5478605ed68dd5607ac8946d0f1a69fcb651dfc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5764b8f0fdd9373a15be01abce350629381e233414237e16a244d4691af89468(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__596c101c9c404cca151b1203ca97bd2d503f355f47622224daa47f385e650be8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f4b31c37417a3cee773773bc1a0a140f366a4e0e7ed41054ce4a4eb796ba219(
    *,
    address: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7aec990e988274953eb37b89aa72be860b6d20fca7dd87507fb1bd44a65b7b9(
    *,
    bucket_name: builtins.str,
    s3_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4414ca463de61620f73bf7c02eb829639136d7dcc505964ba4d9e9618286c69(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    parameter_group_family: builtins.str,
    parameter_group_name: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClusterParameterGroup.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33c3f5debe7a54728cc11b0bbd4cd3ef9a8b793416272ffb149cec7294e16c50(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b7d74938a95ad8692c806f56ca7eec2add84b72ad04dfdd43dbf75c8f82078c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa01b978d978b525b22dfcc1d5e7ed1fdba8f3423e58633da46999cf64b6145e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d55e60eeba305c90c4c7a8c50b43e6bf8362044925cc46818a03d69862ee99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71389da0b60c4def288c7b3fb2b371fda4f4162f1eb827248ad420d596ae579c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f6965bfa88c2fcb264091e20f622accf9bf23be5cacdb3362545db9e6c9696c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnClusterParameterGroup.ParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9d60dbe1f8113e3b7f1c5d9cd93fced6c4ccd359227db112e355b0839bdd7b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240e23a4f4e09dcaf1a5943661993a46709536c604817503e522b63ccc6ccf48(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c09351f48d96a72274bd7deddd60b35ff3d97dffac06fef8da0c50669179bc(
    *,
    description: builtins.str,
    parameter_group_family: builtins.str,
    parameter_group_name: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClusterParameterGroup.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88d0d566c2d2524449f4cc4b794952814b68b5dcd5494f1bcdf5b417ee87ed01(
    *,
    cluster_type: builtins.str,
    db_name: builtins.str,
    master_username: builtins.str,
    master_user_password: builtins.str,
    node_type: builtins.str,
    allow_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    aqua_configuration_status: typing.Optional[builtins.str] = None,
    automated_snapshot_retention_period: typing.Optional[jsii.Number] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    availability_zone_relocation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    availability_zone_relocation_status: typing.Optional[builtins.str] = None,
    classic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cluster_identifier: typing.Optional[builtins.str] = None,
    cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    cluster_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    cluster_subnet_group_name: typing.Optional[builtins.str] = None,
    cluster_version: typing.Optional[builtins.str] = None,
    defer_maintenance: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    defer_maintenance_duration: typing.Optional[jsii.Number] = None,
    defer_maintenance_end_time: typing.Optional[builtins.str] = None,
    defer_maintenance_start_time: typing.Optional[builtins.str] = None,
    destination_region: typing.Optional[builtins.str] = None,
    elastic_ip: typing.Optional[builtins.str] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    hsm_client_certificate_identifier: typing.Optional[builtins.str] = None,
    hsm_configuration_identifier: typing.Optional[builtins.str] = None,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    logging_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.LoggingPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maintenance_track_name: typing.Optional[builtins.str] = None,
    manual_snapshot_retention_period: typing.Optional[jsii.Number] = None,
    number_of_nodes: typing.Optional[jsii.Number] = None,
    owner_account: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    resource_action: typing.Optional[builtins.str] = None,
    revision_target: typing.Optional[builtins.str] = None,
    rotate_encryption_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    snapshot_cluster_identifier: typing.Optional[builtins.str] = None,
    snapshot_copy_grant_name: typing.Optional[builtins.str] = None,
    snapshot_copy_manual: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    snapshot_copy_retention_period: typing.Optional[jsii.Number] = None,
    snapshot_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b22efcbba45de188c12e3a4ec10ac826aa23627c8a9c1ab33ac3ab92f1db7ca(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf91138ab4de58056c692e7a90e9c37175b85888798658fb335eb1fda9dc46ef(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c67faf71bfcbce5abc9c55181019e84dee71de571bd99a7bb417425f307fe805(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b860785f063213d814fda288a338005f7a7bdf25187251589ec205640c547a66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__defdac711f3e7a77b19ec04bc132d682928b4f21ff6be172e15e2ac9f0cd6e8c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41697fee2951713c64e294c4e4850203dbc7d20174c1fed5347f5918875e54ff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_security_group_name: builtins.str,
    cidrip: typing.Optional[builtins.str] = None,
    ec2_security_group_name: typing.Optional[builtins.str] = None,
    ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5daaf061a9776bc828b5e17868e3a5341ceac5a9921dfd313ea5696175e61dc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d33bff3b3590906995d56f375a2e2ff36b57c39243b7809fae2071ef39734a92(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450127f44d7b9d46222076daeb75aef61dc74ee7b8c0361931cbc378b77f2b61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc70f827b8b8bd4fd90e9971cafaa821209d83d7fb903364e18ca0bd12bb4fa7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__305455f9fef2cb5c555b60efcd3ef9258c1c90d3a8215d9e5d93dbcc7b9829a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea6866c86f6e401834ff96949921e03d99488382c3dc85fdb956991534d7d684(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e72baf9a2078a5fc775c4d9a3b9a1dcd173a15a5e17511d8332cdbd8704787a(
    *,
    cluster_security_group_name: builtins.str,
    cidrip: typing.Optional[builtins.str] = None,
    ec2_security_group_name: typing.Optional[builtins.str] = None,
    ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cec630b207d9099c41b9e111a98fa64b023d8033b4d94d7ed94a660cba9bd2d7(
    *,
    description: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586021bde6b1b8994209ba685b5235bc28948707297a01dceac93f542c3474a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e4678321f8dafb0155a5d7f2280c259134e10caeb8b0316bf25b7f635300db0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d89491d283cad8a318fc40039d9bee0dcd132fe85c1ad67b9a1cdb2b3e7ae33(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6179b77c5cb42be7c2cabba28e3458abc09417919b74082d51e7593e0e912a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff71bbb1e980605e8312fa79d3ec8776207253d24115be955dea5799064105b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0234790a32423c903d2d0b04af30d14f6232a9d29765580ce78154e1956f53c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7629b191964d0b486283403d34c774eed1fd92a00727981a023ae6012064b43(
    *,
    description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adead910756274e2bd16ee0b3769d492024abb4cf55d5583a9333d89a1943c75(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_identifier: builtins.str,
    endpoint_name: builtins.str,
    subnet_group_name: builtins.str,
    vpc_security_group_ids: typing.Sequence[builtins.str],
    resource_owner: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b18a7291d940515b72b89f09ad9d7dce3b9a26f99a3a7370573478d5e080b721(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e87b4e358c9074a491173a7bab1e4f3fc3b6265fd5a882c6f514b3ef2b843ec(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__598e9e6d4735cbbfcb104ab4427ff7d119cd8cd64e92591cb873a7be4fb53765(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1190e8d5a0ada81ea332ba42ab4ff9e194abb7bb642a0812316fc5a559f435d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7f534ad279e98a0ece57c6f3178362d5fda74cca1f75270242f4184a2e05e43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6601a60835f68eef555c454dfd6e418359ca5e88b148c65f784029c6b7404ecd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f37292ea99cc675208c9bc19ed54b302762c47c1c291b6034a1554bca882d54e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f524f99b7fb2ef102b93f5f0c5150e30d39dbec01779ff6af2bf97d2cd554c3(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    network_interface_id: typing.Optional[builtins.str] = None,
    private_ip_address: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2902c21df11cec99eebf3ccc4387bf8bdee8b12365a0c5b6de7e74f80a688c02(
    *,
    network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpointAccess.NetworkInterfaceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23ce7ea4c053267c6ffadf93ea9fe0811193cc5da011801b19256affd33ddb77(
    *,
    status: typing.Optional[builtins.str] = None,
    vpc_security_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4208897e368488438ba6d463b7b2649df77c181ed9a0aabd7edf470cf9972e(
    *,
    cluster_identifier: builtins.str,
    endpoint_name: builtins.str,
    subnet_group_name: builtins.str,
    vpc_security_group_ids: typing.Sequence[builtins.str],
    resource_owner: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a697bf6f03512c68c5e0bbce590548dfbef060e4ff37182e32221fef8c520a4b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account: builtins.str,
    cluster_identifier: builtins.str,
    force: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    vpc_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e6beb6eda837ba911711251dade90e261ec5ed724ec65800b20c4a2b32c9449(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87cae2a0280923f1f80cdc272ebcb6a4e8967b591629416b23fb11f9a4d0a22d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f81bbdc996078876480c43faffb9de86d575fc88c6b656e90a94b8c10a590bec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0292d1d6b28ec2ce775f401aaaa3a27fe8c4924b8f4243147138b636fdbe11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3418ce19499db041cb3822978572e2eeb561625f2fdc69d4a3663277a760194(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a14605f174b24a5f18a5630ff894d214b1bfc4e05f8b83234828a27504c0c5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea42c43e99e9da3eea3440151d10e74f104e3b13161b1b46186517cdfb455151(
    *,
    account: builtins.str,
    cluster_identifier: builtins.str,
    force: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    vpc_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2321a5fed3334265b97838abad90fad948fa6670da0259ba7e0d24e88326fdd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    subscription_name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    severity: typing.Optional[builtins.str] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
    source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a03817fc18a5081cfca50722e5b1bcd4346b2500146a8d3c9fb58b226dab6fe4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5380330c3f2bfa84f009dcca8a5550163665b16f1e8cc20ab09ad3a87750572d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6536d2dfac6abba560620e836213d5803aa8693e746ce5cbe8466802804ab2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea0cdf4a4de28abdd520f9b940b88096f2cf47a52a4e567f3499f9de63decbc(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52d3ea63d12acdf3723584b75502be9430562d66c6d2064ab04e9cc95304748(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08ce190a2e94a8276e315d45400484671c991298d1b7d3b8f33ad62f868b3578(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__120fc22c19a6b33fb57b31a06d8c453b9211739cf86ffc8e6ec5d9a28b6f82ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4608ccfe8b64fe9afee3e34458b1bc213f6339b18a11a53005b3c43906eca137(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e1fdab050622407fbbf867b34ce949080facef4619e33c1535fd1e620441ae4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f8d017fb369cae60fd6db670e2d0711cfe832e31a2eb08dc7c90f07ddc39eaa(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882750ef34f06482c6644922124100661565513fabbad49eed142788cd66cfa8(
    *,
    subscription_name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    severity: typing.Optional[builtins.str] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
    source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b090f5bcac0321af743a2821b9b20cd050f984204fe9b5d4288918250e146d1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    scheduled_action_name: builtins.str,
    enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    end_time: typing.Optional[builtins.str] = None,
    iam_role: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[builtins.str] = None,
    scheduled_action_description: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
    target_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledAction.ScheduledActionTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f309d088dd02a60f73f2f52762d748233f12e881a051aee387a69f7a54940d38(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5bed46ce545be8a344aa860129865dc4fdbf8bf1a4e1729c699750cc1b8853c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__872bb8f14b5c5de39d86d09c67159a166a6945e80b42d8739ecc9b58ae6ddbd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d91d9501f12e1db3372aea6023ac844c09772ef705ec20f4e25cb2a1b9febd2(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c0fa066a9596f001c1203f3253634dbe6d284bc1f95dcb4ad5fd93b943f900(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e240c42ffd0653ef9c64e552ae856adb8e46ef1e7445e0c799b2d0fb51a73b3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366bc157c377add120d344d662266845f682e125b0b0becc420c2ad8f012b7f7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94211d9fae42e57e02c956e8f7d0b69f6fe20e2302f5eb33117e7999a3762703(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f13602601a3ed50e4b17c16a24c1a91206f10e208fad90a5e8f6ad4590662c8d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37dee953d9dbcdfb3a7265aa1538c058a9dde8ebabb0b409a0151155cacc75c4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScheduledAction.ScheduledActionTypeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9de594935dd2c45b02090ed3f1a15ec7c1dd2188d0620a5fd7867737ec5417(
    *,
    cluster_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eebc6afccb22ead40bc9246f8233bd603d435e1b55a37a3aec3f29c6ec7e14e0(
    *,
    cluster_identifier: builtins.str,
    classic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cluster_type: typing.Optional[builtins.str] = None,
    node_type: typing.Optional[builtins.str] = None,
    number_of_nodes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf516288cb4d8f79c051b1547fbb68f2eb5395600f53e173adbf24e5978510e6(
    *,
    cluster_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d636da52cf59446f020e242a88d41b50e55ef8273a113c78f968a7fe23c05cdb(
    *,
    pause_cluster: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledAction.PauseClusterMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resize_cluster: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledAction.ResizeClusterMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resume_cluster: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledAction.ResumeClusterMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b8f33670db3a11840dd3dde7157d6c714dfbdf357d1a2d7ffab1191d271b169(
    *,
    scheduled_action_name: builtins.str,
    enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    end_time: typing.Optional[builtins.str] = None,
    iam_role: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[builtins.str] = None,
    scheduled_action_description: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
    target_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledAction.ScheduledActionTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
