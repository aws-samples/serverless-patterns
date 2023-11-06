'''
# Amazon DynamoDB Accelerator Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_dax as dax
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DAX construct libraries](https://constructs.dev/search?q=dax)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DAX resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DAX.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DAX](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DAX.html).

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
    jsii_type="aws-cdk-lib.aws_dax.CfnCluster",
):
    '''Creates a DAX cluster.

    All nodes in the cluster run the same DAX caching software.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dax as dax
        
        # tags: Any
        
        cfn_cluster = dax.CfnCluster(self, "MyCfnCluster",
            iam_role_arn="iamRoleArn",
            node_type="nodeType",
            replication_factor=123,
        
            # the properties below are optional
            availability_zones=["availabilityZones"],
            cluster_endpoint_encryption_type="clusterEndpointEncryptionType",
            cluster_name="clusterName",
            description="description",
            notification_topic_arn="notificationTopicArn",
            parameter_group_name="parameterGroupName",
            preferred_maintenance_window="preferredMaintenanceWindow",
            security_group_ids=["securityGroupIds"],
            sse_specification=dax.CfnCluster.SSESpecificationProperty(
                sse_enabled=False
            ),
            subnet_group_name="subnetGroupName",
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        iam_role_arn: builtins.str,
        node_type: builtins.str,
        replication_factor: jsii.Number,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        cluster_endpoint_encryption_type: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sse_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.SSESpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param iam_role_arn: A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.
        :param node_type: The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        :param replication_factor: The number of nodes in the DAX cluster. A replication factor of 1 will create a single-node cluster, without any read replicas. For additional fault tolerance, you can create a multiple node cluster with one or more read replicas. To do this, set ``ReplicationFactor`` to a number between 3 (one primary and two read replicas) and 10 (one primary and nine read replicas). ``If the AvailabilityZones`` parameter is provided, its length must equal the ``ReplicationFactor`` . .. epigraph:: AWS recommends that you have at least two read replicas per cluster.
        :param availability_zones: The Availability Zones (AZs) in which the cluster nodes will reside after the cluster has been created or updated. If provided, the length of this list must equal the ``ReplicationFactor`` parameter. If you omit this parameter, DAX will spread the nodes across Availability Zones for the highest availability.
        :param cluster_endpoint_encryption_type: The encryption type of the cluster's endpoint. Available values are:. - ``NONE`` - The cluster's endpoint will be unencrypted. - ``TLS`` - The cluster's endpoint will be encrypted with Transport Layer Security, and will provide an x509 certificate for authentication. The default value is ``NONE`` .
        :param cluster_name: The name of the DAX cluster.
        :param description: The description of the cluster.
        :param notification_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent. .. epigraph:: The Amazon SNS topic owner must be same as the DAX cluster owner.
        :param parameter_group_name: The parameter group to be associated with the DAX cluster.
        :param preferred_maintenance_window: A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        :param security_group_ids: A list of security group IDs to be assigned to each node in the DAX cluster. (Each of the security group ID is system-generated.) If this parameter is not specified, DAX assigns the default VPC security group to each node.
        :param sse_specification: Represents the settings used to enable server-side encryption on the cluster.
        :param subnet_group_name: The name of the subnet group to be used for the replication group. .. epigraph:: DAX clusters can only run in an Amazon VPC environment. All of the subnets that you specify in a subnet group must exist in the same VPC.
        :param tags: A set of tags to associate with the DAX cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324ad6077b574145119496cf9145399149504cf843373d16080bbfc26bdf337c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            iam_role_arn=iam_role_arn,
            node_type=node_type,
            replication_factor=replication_factor,
            availability_zones=availability_zones,
            cluster_endpoint_encryption_type=cluster_endpoint_encryption_type,
            cluster_name=cluster_name,
            description=description,
            notification_topic_arn=notification_topic_arn,
            parameter_group_name=parameter_group_name,
            preferred_maintenance_window=preferred_maintenance_window,
            security_group_ids=security_group_ids,
            sse_specification=sse_specification,
            subnet_group_name=subnet_group_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d414733c7b35171bc3653d115c315aa4807828bc7abf2009139681ae47eb70e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ee21d3d8dd72965a18313e6a1cb72a1cfef30cf20a4c6548e7c6c058f074ada)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the ARN of the DAX cluster. For example:.

        ``{ "Fn::GetAtt": [" MyDAXCluster ", "Arn"] }``

        Returns a value similar to the following:

        ``arn:aws:dax:us-east-1:111122223333:cache/MyDAXCluster``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterDiscoveryEndpoint")
    def attr_cluster_discovery_endpoint(self) -> builtins.str:
        '''Returns the endpoint of the DAX cluster. For example:.

        ``{ "Fn::GetAtt": [" MyDAXCluster ", "ClusterDiscoveryEndpoint"] }``

        Returns a value similar to the following:

        ``mydaxcluster.0h3d6x.clustercfg.dax.use1.cache.amazonaws.com:8111``

        :cloudformationAttribute: ClusterDiscoveryEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterDiscoveryEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterDiscoveryEndpointUrl")
    def attr_cluster_discovery_endpoint_url(self) -> builtins.str:
        '''Returns the endpoint URL of the DAX cluster.

        :cloudformationAttribute: ClusterDiscoveryEndpointURL
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterDiscoveryEndpointUrl"))

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
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> builtins.str:
        '''A valid Amazon Resource Name (ARN) that identifies an IAM role.'''
        return typing.cast(builtins.str, jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb205cc2bdee610b978432d1997360928a422ee08c38d7eaa95f25765747d7da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> builtins.str:
        '''The node type for the nodes in the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35f185d77a7a9b7e4e188c805eafa1588c84d01033e5b3e460bb7a048d200d61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

    @builtins.property
    @jsii.member(jsii_name="replicationFactor")
    def replication_factor(self) -> jsii.Number:
        '''The number of nodes in the DAX cluster.'''
        return typing.cast(jsii.Number, jsii.get(self, "replicationFactor"))

    @replication_factor.setter
    def replication_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__677b2e5437e61284517ed7aee0a4937cf305bade89a1d41e76f9e477ceac0dd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationFactor", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Availability Zones (AZs) in which the cluster nodes will reside after the cluster has been created or updated.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cdb08dd2cbc052aef8ec0c40131efcc7c715f5b0055abf6929c66a3a34ed715)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="clusterEndpointEncryptionType")
    def cluster_endpoint_encryption_type(self) -> typing.Optional[builtins.str]:
        '''The encryption type of the cluster's endpoint.

        Available values are:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterEndpointEncryptionType"))

    @cluster_endpoint_encryption_type.setter
    def cluster_endpoint_encryption_type(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc0e98a5ffcb93a9b3d088991c357c86c87ed47bf2ed50e45df9f1fa7653baf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterEndpointEncryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''The name of the DAX cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665031432f0d154265a0bc96541521c3cf1315802ded05775f9d360dbd71614d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e936f055c9c5c8fb047e8707a99756966620342b83efe4e4d270336903753881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArn")
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTopicArn"))

    @notification_topic_arn.setter
    def notification_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__852eb5b1ac0dc6981cbea6d3a51527ef97091db66755959ae1dc62f475cd0c3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The parameter group to be associated with the DAX cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterGroupName"))

    @parameter_group_name.setter
    def parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e16d62f0febe6be319f5d22ac44912821c71bd96043e40c59ce7d4580ee4a991)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''A range of time when maintenance of DAX cluster software will be performed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f41df49a5a9be16a4fbafcf6ee5011bca6e3bcbe8270c612a05a2f9a67b052d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to be assigned to each node in the DAX cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__680b6e626892e5ffe6db2acedd4a24345ca1a33a929fff18b1ebb320d971d6d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="sseSpecification")
    def sse_specification(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SSESpecificationProperty"]]:
        '''Represents the settings used to enable server-side encryption on the cluster.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SSESpecificationProperty"]], jsii.get(self, "sseSpecification"))

    @sse_specification.setter
    def sse_specification(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SSESpecificationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd943a79f12c83e70343df7b142a7c0aba1cf9f88daa8f114a18686cd12b7c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subnet group to be used for the replication group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetGroupName"))

    @subnet_group_name.setter
    def subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bdc3f0c22e0d922c88db96440ab16a9fa4473af97333a2f58f6894daecdf8db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''A set of tags to associate with the DAX cluster.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b1f9bc9715305b6189911164a6ad38b80782a264bb5366231290a4017855a00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dax.CfnCluster.SSESpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"sse_enabled": "sseEnabled"},
    )
    class SSESpecificationProperty:
        def __init__(
            self,
            *,
            sse_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents the settings used to enable server-side encryption.

            :param sse_enabled: Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dax-cluster-ssespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dax as dax
                
                s_sESpecification_property = dax.CfnCluster.SSESpecificationProperty(
                    sse_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e519d3094d95ddc323860984c5b5c2702e16db8b3e7a7fd08b117de038a1b01e)
                check_type(argname="argument sse_enabled", value=sse_enabled, expected_type=type_hints["sse_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sse_enabled is not None:
                self._values["sse_enabled"] = sse_enabled

        @builtins.property
        def sse_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dax-cluster-ssespecification.html#cfn-dax-cluster-ssespecification-sseenabled
            '''
            result = self._values.get("sse_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SSESpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dax.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "iam_role_arn": "iamRoleArn",
        "node_type": "nodeType",
        "replication_factor": "replicationFactor",
        "availability_zones": "availabilityZones",
        "cluster_endpoint_encryption_type": "clusterEndpointEncryptionType",
        "cluster_name": "clusterName",
        "description": "description",
        "notification_topic_arn": "notificationTopicArn",
        "parameter_group_name": "parameterGroupName",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "security_group_ids": "securityGroupIds",
        "sse_specification": "sseSpecification",
        "subnet_group_name": "subnetGroupName",
        "tags": "tags",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        iam_role_arn: builtins.str,
        node_type: builtins.str,
        replication_factor: jsii.Number,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        cluster_endpoint_encryption_type: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sse_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SSESpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param iam_role_arn: A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.
        :param node_type: The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        :param replication_factor: The number of nodes in the DAX cluster. A replication factor of 1 will create a single-node cluster, without any read replicas. For additional fault tolerance, you can create a multiple node cluster with one or more read replicas. To do this, set ``ReplicationFactor`` to a number between 3 (one primary and two read replicas) and 10 (one primary and nine read replicas). ``If the AvailabilityZones`` parameter is provided, its length must equal the ``ReplicationFactor`` . .. epigraph:: AWS recommends that you have at least two read replicas per cluster.
        :param availability_zones: The Availability Zones (AZs) in which the cluster nodes will reside after the cluster has been created or updated. If provided, the length of this list must equal the ``ReplicationFactor`` parameter. If you omit this parameter, DAX will spread the nodes across Availability Zones for the highest availability.
        :param cluster_endpoint_encryption_type: The encryption type of the cluster's endpoint. Available values are:. - ``NONE`` - The cluster's endpoint will be unencrypted. - ``TLS`` - The cluster's endpoint will be encrypted with Transport Layer Security, and will provide an x509 certificate for authentication. The default value is ``NONE`` .
        :param cluster_name: The name of the DAX cluster.
        :param description: The description of the cluster.
        :param notification_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent. .. epigraph:: The Amazon SNS topic owner must be same as the DAX cluster owner.
        :param parameter_group_name: The parameter group to be associated with the DAX cluster.
        :param preferred_maintenance_window: A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        :param security_group_ids: A list of security group IDs to be assigned to each node in the DAX cluster. (Each of the security group ID is system-generated.) If this parameter is not specified, DAX assigns the default VPC security group to each node.
        :param sse_specification: Represents the settings used to enable server-side encryption on the cluster.
        :param subnet_group_name: The name of the subnet group to be used for the replication group. .. epigraph:: DAX clusters can only run in an Amazon VPC environment. All of the subnets that you specify in a subnet group must exist in the same VPC.
        :param tags: A set of tags to associate with the DAX cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dax as dax
            
            # tags: Any
            
            cfn_cluster_props = dax.CfnClusterProps(
                iam_role_arn="iamRoleArn",
                node_type="nodeType",
                replication_factor=123,
            
                # the properties below are optional
                availability_zones=["availabilityZones"],
                cluster_endpoint_encryption_type="clusterEndpointEncryptionType",
                cluster_name="clusterName",
                description="description",
                notification_topic_arn="notificationTopicArn",
                parameter_group_name="parameterGroupName",
                preferred_maintenance_window="preferredMaintenanceWindow",
                security_group_ids=["securityGroupIds"],
                sse_specification=dax.CfnCluster.SSESpecificationProperty(
                    sse_enabled=False
                ),
                subnet_group_name="subnetGroupName",
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece2ee11399f77b699021f70d8286031a08ea0aa17f1c2afcda136bb9f1269b8)
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument replication_factor", value=replication_factor, expected_type=type_hints["replication_factor"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument cluster_endpoint_encryption_type", value=cluster_endpoint_encryption_type, expected_type=type_hints["cluster_endpoint_encryption_type"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument notification_topic_arn", value=notification_topic_arn, expected_type=type_hints["notification_topic_arn"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument sse_specification", value=sse_specification, expected_type=type_hints["sse_specification"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iam_role_arn": iam_role_arn,
            "node_type": node_type,
            "replication_factor": replication_factor,
        }
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if cluster_endpoint_encryption_type is not None:
            self._values["cluster_endpoint_encryption_type"] = cluster_endpoint_encryption_type
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if description is not None:
            self._values["description"] = description
        if notification_topic_arn is not None:
            self._values["notification_topic_arn"] = notification_topic_arn
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if sse_specification is not None:
            self._values["sse_specification"] = sse_specification
        if subnet_group_name is not None:
            self._values["subnet_group_name"] = subnet_group_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def iam_role_arn(self) -> builtins.str:
        '''A valid Amazon Resource Name (ARN) that identifies an IAM role.

        At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-iamrolearn
        '''
        result = self._values.get("iam_role_arn")
        assert result is not None, "Required property 'iam_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_type(self) -> builtins.str:
        '''The node type for the nodes in the cluster.

        (All nodes in a DAX cluster are of the same type.)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-nodetype
        '''
        result = self._values.get("node_type")
        assert result is not None, "Required property 'node_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_factor(self) -> jsii.Number:
        '''The number of nodes in the DAX cluster.

        A replication factor of 1 will create a single-node cluster, without any read replicas. For additional fault tolerance, you can create a multiple node cluster with one or more read replicas. To do this, set ``ReplicationFactor`` to a number between 3 (one primary and two read replicas) and 10 (one primary and nine read replicas). ``If the AvailabilityZones`` parameter is provided, its length must equal the ``ReplicationFactor`` .
        .. epigraph::

           AWS recommends that you have at least two read replicas per cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-replicationfactor
        '''
        result = self._values.get("replication_factor")
        assert result is not None, "Required property 'replication_factor' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Availability Zones (AZs) in which the cluster nodes will reside after the cluster has been created or updated.

        If provided, the length of this list must equal the ``ReplicationFactor`` parameter. If you omit this parameter, DAX will spread the nodes across Availability Zones for the highest availability.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-availabilityzones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cluster_endpoint_encryption_type(self) -> typing.Optional[builtins.str]:
        '''The encryption type of the cluster's endpoint. Available values are:.

        - ``NONE`` - The cluster's endpoint will be unencrypted.
        - ``TLS`` - The cluster's endpoint will be encrypted with Transport Layer Security, and will provide an x509 certificate for authentication.

        The default value is ``NONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-clusterendpointencryptiontype
        '''
        result = self._values.get("cluster_endpoint_encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''The name of the DAX cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-clustername
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.

        .. epigraph::

           The Amazon SNS topic owner must be same as the DAX cluster owner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-notificationtopicarn
        '''
        result = self._values.get("notification_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The parameter group to be associated with the DAX cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-parametergroupname
        '''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''A range of time when maintenance of DAX cluster software will be performed.

        For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to be assigned to each node in the DAX cluster.

        (Each of the security group ID is system-generated.)

        If this parameter is not specified, DAX assigns the default VPC security group to each node.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sse_specification(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.SSESpecificationProperty]]:
        '''Represents the settings used to enable server-side encryption on the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-ssespecification
        '''
        result = self._values.get("sse_specification")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.SSESpecificationProperty]], result)

    @builtins.property
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subnet group to be used for the replication group.

        .. epigraph::

           DAX clusters can only run in an Amazon VPC environment. All of the subnets that you specify in a subnet group must exist in the same VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-subnetgroupname
        '''
        result = self._values.get("subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''A set of tags to associate with the DAX cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnParameterGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dax.CfnParameterGroup",
):
    '''A named set of parameters that are applied to all of the nodes in a DAX cluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dax as dax
        
        # parameter_name_values: Any
        
        cfn_parameter_group = dax.CfnParameterGroup(self, "MyCfnParameterGroup",
            description="description",
            parameter_group_name="parameterGroupName",
            parameter_name_values=parameter_name_values
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        parameter_name_values: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description of the parameter group.
        :param parameter_group_name: The name of the parameter group.
        :param parameter_name_values: An array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter. .. epigraph:: ``record-ttl-millis`` and ``query-ttl-millis`` are the only supported parameter names. For more details, see `Configuring TTL Settings <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings.ttl>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57163a266c7ddaa448bd986af45e05e85c86557e3ddab63ad97ececcea717676)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnParameterGroupProps(
            description=description,
            parameter_group_name=parameter_group_name,
            parameter_name_values=parameter_name_values,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f230255f83e3cded6147eae9447b88505dc5f3d28a6f75d4b196ae7245a76670)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5cce943d70ba76fabad51fccc17e3282e4fe54469397dd4319c96c25517ad24)
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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the parameter group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c69816d4620c5775a1c8536ee3cdebce5fc002925ee3bbe750f855c8b55f53f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterGroupName"))

    @parameter_group_name.setter
    def parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56c6d935312fa98d33575df3870fd47d07214c86df208dc2fd5f7b89a19593a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterNameValues")
    def parameter_name_values(self) -> typing.Any:
        '''An array of name-value pairs for the parameters in the group.'''
        return typing.cast(typing.Any, jsii.get(self, "parameterNameValues"))

    @parameter_name_values.setter
    def parameter_name_values(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__debcae534ba3b42bfd314c77f9ee5a02478b2fdc28d91af155cd6ef12d42e1d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterNameValues", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dax.CfnParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "parameter_group_name": "parameterGroupName",
        "parameter_name_values": "parameterNameValues",
    },
)
class CfnParameterGroupProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        parameter_name_values: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnParameterGroup``.

        :param description: A description of the parameter group.
        :param parameter_group_name: The name of the parameter group.
        :param parameter_name_values: An array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter. .. epigraph:: ``record-ttl-millis`` and ``query-ttl-millis`` are the only supported parameter names. For more details, see `Configuring TTL Settings <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings.ttl>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dax as dax
            
            # parameter_name_values: Any
            
            cfn_parameter_group_props = dax.CfnParameterGroupProps(
                description="description",
                parameter_group_name="parameterGroupName",
                parameter_name_values=parameter_name_values
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4491dae1cabd7717750afcb42defd554be706d191983437cf2d1cccca64615d2)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
            check_type(argname="argument parameter_name_values", value=parameter_name_values, expected_type=type_hints["parameter_name_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name
        if parameter_name_values is not None:
            self._values["parameter_name_values"] = parameter_name_values

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html#cfn-dax-parametergroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html#cfn-dax-parametergroup-parametergroupname
        '''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name_values(self) -> typing.Any:
        '''An array of name-value pairs for the parameters in the group.

        Each element in the array represents a single parameter.
        .. epigraph::

           ``record-ttl-millis`` and ``query-ttl-millis`` are the only supported parameter names. For more details, see `Configuring TTL Settings <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings.ttl>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html#cfn-dax-parametergroup-parameternamevalues
        '''
        result = self._values.get("parameter_name_values")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSubnetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dax.CfnSubnetGroup",
):
    '''Creates a new subnet group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dax as dax
        
        cfn_subnet_group = dax.CfnSubnetGroup(self, "MyCfnSubnetGroup",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            description="description",
            subnet_group_name="subnetGroupName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        subnet_ids: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param subnet_ids: A list of VPC subnet IDs for the subnet group.
        :param description: The description of the subnet group.
        :param subnet_group_name: The name of the subnet group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83031360ae2c1b57012ac874ff39a0718c041d983e9345fa429f3eff1d27a78d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubnetGroupProps(
            subnet_ids=subnet_ids,
            description=description,
            subnet_group_name=subnet_group_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a6cfa9c63186ca6b95f7908df8b9814c18ae438aca12498244549ff62f31d4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5010e475b88c49fe4ee87b051c7cb5b0d38299083102dcae537d01057ef8ac6e)
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
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''A list of VPC subnet IDs for the subnet group.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b575229942d4a326fd75d3e99e02ca2d0d8088221c14a233d99d0d9be6118e98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the subnet group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__631477a917e513577c5d75fd3744b03476a5a0d4c798c9fe66d1c319aaa81251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subnet group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetGroupName"))

    @subnet_group_name.setter
    def subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f155103d3d1c304714ba9aeac35a7b6fa637436e6c85878763b22c643099102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetGroupName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dax.CfnSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "subnet_ids": "subnetIds",
        "description": "description",
        "subnet_group_name": "subnetGroupName",
    },
)
class CfnSubnetGroupProps:
    def __init__(
        self,
        *,
        subnet_ids: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubnetGroup``.

        :param subnet_ids: A list of VPC subnet IDs for the subnet group.
        :param description: The description of the subnet group.
        :param subnet_group_name: The name of the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dax as dax
            
            cfn_subnet_group_props = dax.CfnSubnetGroupProps(
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                description="description",
                subnet_group_name="subnetGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2a634e35853b0d535a4301ce03172062663607e6b5c0a2d367871acce1292a4)
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_ids": subnet_ids,
        }
        if description is not None:
            self._values["description"] = description
        if subnet_group_name is not None:
            self._values["subnet_group_name"] = subnet_group_name

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''A list of VPC subnet IDs for the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html#cfn-dax-subnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html#cfn-dax-subnetgroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html#cfn-dax-subnetgroup-subnetgroupname
        '''
        result = self._values.get("subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
    "CfnParameterGroup",
    "CfnParameterGroupProps",
    "CfnSubnetGroup",
    "CfnSubnetGroupProps",
]

publication.publish()

def _typecheckingstub__324ad6077b574145119496cf9145399149504cf843373d16080bbfc26bdf337c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    iam_role_arn: builtins.str,
    node_type: builtins.str,
    replication_factor: jsii.Number,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    cluster_endpoint_encryption_type: typing.Optional[builtins.str] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    notification_topic_arn: typing.Optional[builtins.str] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    sse_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SSESpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d414733c7b35171bc3653d115c315aa4807828bc7abf2009139681ae47eb70e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ee21d3d8dd72965a18313e6a1cb72a1cfef30cf20a4c6548e7c6c058f074ada(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb205cc2bdee610b978432d1997360928a422ee08c38d7eaa95f25765747d7da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f185d77a7a9b7e4e188c805eafa1588c84d01033e5b3e460bb7a048d200d61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__677b2e5437e61284517ed7aee0a4937cf305bade89a1d41e76f9e477ceac0dd0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cdb08dd2cbc052aef8ec0c40131efcc7c715f5b0055abf6929c66a3a34ed715(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc0e98a5ffcb93a9b3d088991c357c86c87ed47bf2ed50e45df9f1fa7653baf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665031432f0d154265a0bc96541521c3cf1315802ded05775f9d360dbd71614d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e936f055c9c5c8fb047e8707a99756966620342b83efe4e4d270336903753881(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__852eb5b1ac0dc6981cbea6d3a51527ef97091db66755959ae1dc62f475cd0c3b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e16d62f0febe6be319f5d22ac44912821c71bd96043e40c59ce7d4580ee4a991(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f41df49a5a9be16a4fbafcf6ee5011bca6e3bcbe8270c612a05a2f9a67b052d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__680b6e626892e5ffe6db2acedd4a24345ca1a33a929fff18b1ebb320d971d6d1(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd943a79f12c83e70343df7b142a7c0aba1cf9f88daa8f114a18686cd12b7c2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.SSESpecificationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bdc3f0c22e0d922c88db96440ab16a9fa4473af97333a2f58f6894daecdf8db(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b1f9bc9715305b6189911164a6ad38b80782a264bb5366231290a4017855a00(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e519d3094d95ddc323860984c5b5c2702e16db8b3e7a7fd08b117de038a1b01e(
    *,
    sse_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece2ee11399f77b699021f70d8286031a08ea0aa17f1c2afcda136bb9f1269b8(
    *,
    iam_role_arn: builtins.str,
    node_type: builtins.str,
    replication_factor: jsii.Number,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    cluster_endpoint_encryption_type: typing.Optional[builtins.str] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    notification_topic_arn: typing.Optional[builtins.str] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    sse_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SSESpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57163a266c7ddaa448bd986af45e05e85c86557e3ddab63ad97ececcea717676(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    parameter_name_values: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f230255f83e3cded6147eae9447b88505dc5f3d28a6f75d4b196ae7245a76670(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5cce943d70ba76fabad51fccc17e3282e4fe54469397dd4319c96c25517ad24(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c69816d4620c5775a1c8536ee3cdebce5fc002925ee3bbe750f855c8b55f53f4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56c6d935312fa98d33575df3870fd47d07214c86df208dc2fd5f7b89a19593a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__debcae534ba3b42bfd314c77f9ee5a02478b2fdc28d91af155cd6ef12d42e1d0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4491dae1cabd7717750afcb42defd554be706d191983437cf2d1cccca64615d2(
    *,
    description: typing.Optional[builtins.str] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    parameter_name_values: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83031360ae2c1b57012ac874ff39a0718c041d983e9345fa429f3eff1d27a78d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    subnet_ids: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a6cfa9c63186ca6b95f7908df8b9814c18ae438aca12498244549ff62f31d4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5010e475b88c49fe4ee87b051c7cb5b0d38299083102dcae537d01057ef8ac6e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b575229942d4a326fd75d3e99e02ca2d0d8088221c14a233d99d0d9be6118e98(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__631477a917e513577c5d75fd3744b03476a5a0d4c798c9fe66d1c319aaa81251(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f155103d3d1c304714ba9aeac35a7b6fa637436e6c85878763b22c643099102(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a634e35853b0d535a4301ce03172062663607e6b5c0a2d367871acce1292a4(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
