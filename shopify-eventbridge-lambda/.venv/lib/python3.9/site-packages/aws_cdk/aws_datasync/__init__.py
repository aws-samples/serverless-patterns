'''
# AWS::DataSync Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_datasync as datasync
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DataSync construct libraries](https://constructs.dev/search?q=datasync)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DataSync resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataSync.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DataSync](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataSync.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAgent(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnAgent",
):
    '''The ``AWS::DataSync::Agent`` resource activates an AWS DataSync agent that you've deployed for storage discovery or data transfers.

    The activation process associates the agent with your AWS account .

    For more information, see the following topics in the *AWS DataSync User Guide* :

    - `DataSync agent requirements <https://docs.aws.amazon.com/datasync/latest/userguide/agent-requirements.html>`_
    - `DataSync network requirements <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html>`_
    - `Create a DataSync agent <https://docs.aws.amazon.com/datasync/latest/userguide/configure-agent.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html
    :cloudformationResource: AWS::DataSync::Agent
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_agent = datasync.CfnAgent(self, "MyCfnAgent",
            activation_key="activationKey",
            agent_name="agentName",
            security_group_arns=["securityGroupArns"],
            subnet_arns=["subnetArns"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_endpoint_id="vpcEndpointId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        activation_key: typing.Optional[builtins.str] = None,
        agent_name: typing.Optional[builtins.str] = None,
        security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_endpoint_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param activation_key: Specifies your DataSync agent's activation key. If you don't have an activation key, see `Activate your agent <https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html>`_ .
        :param agent_name: Specifies a name for your agent. You can see this name in the DataSync console.
        :param security_group_arns: The Amazon Resource Names (ARNs) of the security groups used to protect your data transfer task subnets. See `SecurityGroupArns <https://docs.aws.amazon.com/datasync/latest/userguide/API_Ec2Config.html#DataSync-Type-Ec2Config-SecurityGroupArns>`_ . *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$``
        :param subnet_arns: Specifies the ARN of the subnet where you want to run your DataSync task when using a VPC endpoint. This is the subnet where DataSync creates and manages the `network interfaces <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces>`_ for your transfer. You can only specify one ARN.
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least one tag for your agent.
        :param vpc_endpoint_id: The ID of the virtual private cloud (VPC) endpoint that the agent has access to. This is the client-side VPC endpoint, powered by AWS PrivateLink . If you don't have an AWS PrivateLink VPC endpoint, see `AWS PrivateLink and VPC endpoints <https://docs.aws.amazon.com//vpc/latest/userguide/endpoint-services-overview.html>`_ in the *Amazon VPC User Guide* . For more information about activating your agent in a private network based on a VPC, see `Using AWS DataSync in a Virtual Private Cloud <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-in-vpc.html>`_ in the *AWS DataSync User Guide.* A VPC endpoint ID looks like this: ``vpce-01234d5aff67890e1`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d936a9373128610a07487a343ef5f669c26d2f82d825e32d371bce59b97aa93c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAgentProps(
            activation_key=activation_key,
            agent_name=agent_name,
            security_group_arns=security_group_arns,
            subnet_arns=subnet_arns,
            tags=tags,
            vpc_endpoint_id=vpc_endpoint_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81fbad3909c49b87e552d1214005285ecb6b192ba23456279698e48b81961aac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__45ceb39e9063ce041ae5fa861dd0bf69001bf3c69cc12e412d36e67d3f7da074)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentArn")
    def attr_agent_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the agent.

        Use the ``ListAgents`` operation to return a list of agents for your account and AWS Region .

        :cloudformationAttribute: AgentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointType")
    def attr_endpoint_type(self) -> builtins.str:
        '''The type of endpoint that your agent is connected to.

        If the endpoint is a VPC endpoint, the agent is not accessible over the public internet.

        :cloudformationAttribute: EndpointType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointType"))

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
    @jsii.member(jsii_name="activationKey")
    def activation_key(self) -> typing.Optional[builtins.str]:
        '''Specifies your DataSync agent's activation key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activationKey"))

    @activation_key.setter
    def activation_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__487cd8023e4b2808d444a1f5c85f66a51d757299d1239cf71233c99176c0522d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activationKey", value)

    @builtins.property
    @jsii.member(jsii_name="agentName")
    def agent_name(self) -> typing.Optional[builtins.str]:
        '''Specifies a name for your agent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentName"))

    @agent_name.setter
    def agent_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4450f3881b2dffdb43cc0604c9cfd8a0efa10d69ac51ad3d1bf11d605de50a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentName", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupArns")
    def security_group_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Names (ARNs) of the security groups used to protect your data transfer task subnets.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupArns"))

    @security_group_arns.setter
    def security_group_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3397ee88e1e2dd7128616ed90dbaaeea7d67a2ae384d286cdcfaa48849d48f9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupArns", value)

    @builtins.property
    @jsii.member(jsii_name="subnetArns")
    def subnet_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the ARN of the subnet where you want to run your DataSync task when using a VPC endpoint.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetArns"))

    @subnet_arns.setter
    def subnet_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c121bd2b79eb0fd51d5790002f0a61a6ac6a1606ce08b2d3d61b1bb196968ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetArns", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae8ff35f7c199f1e5218a6432dc5893a46003bc8921b159534e548343397b69c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC) endpoint that the agent has access to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcEndpointId"))

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__382a2bd8de9abd26a4050c65ad2d6baa552585795b8cb589d8cc033b01c16bcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcEndpointId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnAgentProps",
    jsii_struct_bases=[],
    name_mapping={
        "activation_key": "activationKey",
        "agent_name": "agentName",
        "security_group_arns": "securityGroupArns",
        "subnet_arns": "subnetArns",
        "tags": "tags",
        "vpc_endpoint_id": "vpcEndpointId",
    },
)
class CfnAgentProps:
    def __init__(
        self,
        *,
        activation_key: typing.Optional[builtins.str] = None,
        agent_name: typing.Optional[builtins.str] = None,
        security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_endpoint_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAgent``.

        :param activation_key: Specifies your DataSync agent's activation key. If you don't have an activation key, see `Activate your agent <https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html>`_ .
        :param agent_name: Specifies a name for your agent. You can see this name in the DataSync console.
        :param security_group_arns: The Amazon Resource Names (ARNs) of the security groups used to protect your data transfer task subnets. See `SecurityGroupArns <https://docs.aws.amazon.com/datasync/latest/userguide/API_Ec2Config.html#DataSync-Type-Ec2Config-SecurityGroupArns>`_ . *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$``
        :param subnet_arns: Specifies the ARN of the subnet where you want to run your DataSync task when using a VPC endpoint. This is the subnet where DataSync creates and manages the `network interfaces <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces>`_ for your transfer. You can only specify one ARN.
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least one tag for your agent.
        :param vpc_endpoint_id: The ID of the virtual private cloud (VPC) endpoint that the agent has access to. This is the client-side VPC endpoint, powered by AWS PrivateLink . If you don't have an AWS PrivateLink VPC endpoint, see `AWS PrivateLink and VPC endpoints <https://docs.aws.amazon.com//vpc/latest/userguide/endpoint-services-overview.html>`_ in the *Amazon VPC User Guide* . For more information about activating your agent in a private network based on a VPC, see `Using AWS DataSync in a Virtual Private Cloud <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-in-vpc.html>`_ in the *AWS DataSync User Guide.* A VPC endpoint ID looks like this: ``vpce-01234d5aff67890e1`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_agent_props = datasync.CfnAgentProps(
                activation_key="activationKey",
                agent_name="agentName",
                security_group_arns=["securityGroupArns"],
                subnet_arns=["subnetArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_endpoint_id="vpcEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6733a53a5c0a8ea652fdedb421d3ea702ad3e42c07f57a164d132594aefc8eb)
            check_type(argname="argument activation_key", value=activation_key, expected_type=type_hints["activation_key"])
            check_type(argname="argument agent_name", value=agent_name, expected_type=type_hints["agent_name"])
            check_type(argname="argument security_group_arns", value=security_group_arns, expected_type=type_hints["security_group_arns"])
            check_type(argname="argument subnet_arns", value=subnet_arns, expected_type=type_hints["subnet_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if activation_key is not None:
            self._values["activation_key"] = activation_key
        if agent_name is not None:
            self._values["agent_name"] = agent_name
        if security_group_arns is not None:
            self._values["security_group_arns"] = security_group_arns
        if subnet_arns is not None:
            self._values["subnet_arns"] = subnet_arns
        if tags is not None:
            self._values["tags"] = tags
        if vpc_endpoint_id is not None:
            self._values["vpc_endpoint_id"] = vpc_endpoint_id

    @builtins.property
    def activation_key(self) -> typing.Optional[builtins.str]:
        '''Specifies your DataSync agent's activation key.

        If you don't have an activation key, see `Activate your agent <https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-activationkey
        '''
        result = self._values.get("activation_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def agent_name(self) -> typing.Optional[builtins.str]:
        '''Specifies a name for your agent.

        You can see this name in the DataSync console.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-agentname
        '''
        result = self._values.get("agent_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Names (ARNs) of the security groups used to protect your data transfer task subnets.

        See `SecurityGroupArns <https://docs.aws.amazon.com/datasync/latest/userguide/API_Ec2Config.html#DataSync-Type-Ec2Config-SecurityGroupArns>`_ .

        *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-securitygrouparns
        '''
        result = self._values.get("security_group_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the ARN of the subnet where you want to run your DataSync task when using a VPC endpoint.

        This is the subnet where DataSync creates and manages the `network interfaces <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces>`_ for your transfer. You can only specify one ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-subnetarns
        '''
        result = self._values.get("subnet_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.

        We recommend creating at least one tag for your agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC) endpoint that the agent has access to.

        This is the client-side VPC endpoint, powered by AWS PrivateLink . If you don't have an AWS PrivateLink VPC endpoint, see `AWS PrivateLink and VPC endpoints <https://docs.aws.amazon.com//vpc/latest/userguide/endpoint-services-overview.html>`_ in the *Amazon VPC User Guide* .

        For more information about activating your agent in a private network based on a VPC, see `Using AWS DataSync in a Virtual Private Cloud <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-in-vpc.html>`_ in the *AWS DataSync User Guide.*

        A VPC endpoint ID looks like this: ``vpce-01234d5aff67890e1`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-vpcendpointid
        '''
        result = self._values.get("vpc_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAgentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnLocationAzureBlob(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationAzureBlob",
):
    '''Creates a transfer *location* for a Microsoft Azure Blob Storage container.

    AWS DataSync can use this location as a transfer source or destination.

    Before you begin, make sure you know `how DataSync accesses Azure Blob Storage <https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access>`_ and works with `access tiers <https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers>`_ and `blob types <https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#blob-types>`_ . You also need a `DataSync agent <https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-creating-agent>`_ that can connect to your container.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html
    :cloudformationResource: AWS::DataSync::LocationAzureBlob
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_azure_blob = datasync.CfnLocationAzureBlob(self, "MyCfnLocationAzureBlob",
            agent_arns=["agentArns"],
            azure_blob_authentication_type="azureBlobAuthenticationType",
        
            # the properties below are optional
            azure_access_tier="azureAccessTier",
            azure_blob_container_url="azureBlobContainerUrl",
            azure_blob_sas_configuration=datasync.CfnLocationAzureBlob.AzureBlobSasConfigurationProperty(
                azure_blob_sas_token="azureBlobSasToken"
            ),
            azure_blob_type="azureBlobType",
            subdirectory="subdirectory",
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
        agent_arns: typing.Sequence[builtins.str],
        azure_blob_authentication_type: builtins.str,
        azure_access_tier: typing.Optional[builtins.str] = None,
        azure_blob_container_url: typing.Optional[builtins.str] = None,
        azure_blob_sas_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationAzureBlob.AzureBlobSasConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        azure_blob_type: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_arns: Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container. You can specify more than one agent. For more information, see `Using multiple agents for your transfer <https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html>`_ .
        :param azure_blob_authentication_type: Specifies the authentication method DataSync uses to access your Azure Blob Storage. DataSync can access blob storage using a shared access signature (SAS). Default: - "SAS"
        :param azure_access_tier: Specifies the access tier that you want your objects or files transferred into. This only applies when using the location as a transfer destination. For more information, see `Access tiers <https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers>`_ . Default: - "HOT"
        :param azure_blob_container_url: Specifies the URL of the Azure Blob Storage container involved in your transfer.
        :param azure_blob_sas_configuration: Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.
        :param azure_blob_type: Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the `Azure Blob Storage documentation <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs>`_ . Default: - "BLOCK"
        :param subdirectory: Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, ``/my/images`` ).
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your transfer location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a49f57a1ab4813b1537b04053be19b99e3fa8f143f30fac9d1bc72caa4ec5f2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationAzureBlobProps(
            agent_arns=agent_arns,
            azure_blob_authentication_type=azure_blob_authentication_type,
            azure_access_tier=azure_access_tier,
            azure_blob_container_url=azure_blob_container_url,
            azure_blob_sas_configuration=azure_blob_sas_configuration,
            azure_blob_type=azure_blob_type,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc59f45abf5059f82345f619c384b01d137f4d49a1506da910056ac15ef819a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ebde5c22aa68229dea3796deaf496ab61b9ffcfdf6d4f56a59875e6047047203)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The ARN of the Azure Blob Storage transfer location that you created.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the Azure Blob Storage transfer location that you created.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04d94ab53395a58893ca5e5668d51e78b5d567de304ebc1b3c8937ab5824c459)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentArns", value)

    @builtins.property
    @jsii.member(jsii_name="azureBlobAuthenticationType")
    def azure_blob_authentication_type(self) -> builtins.str:
        '''Specifies the authentication method DataSync uses to access your Azure Blob Storage.'''
        return typing.cast(builtins.str, jsii.get(self, "azureBlobAuthenticationType"))

    @azure_blob_authentication_type.setter
    def azure_blob_authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d66037c88c30360a6dbdeedf60b7cdd8b0d971ae11fb4944eb61af92fe413080)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureBlobAuthenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="azureAccessTier")
    def azure_access_tier(self) -> typing.Optional[builtins.str]:
        '''Specifies the access tier that you want your objects or files transferred into.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureAccessTier"))

    @azure_access_tier.setter
    def azure_access_tier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38eadceb910bce5de77c7dd9c218a003ad2d8b865f6b732f47b6b7fea8c1f40d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureAccessTier", value)

    @builtins.property
    @jsii.member(jsii_name="azureBlobContainerUrl")
    def azure_blob_container_url(self) -> typing.Optional[builtins.str]:
        '''Specifies the URL of the Azure Blob Storage container involved in your transfer.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureBlobContainerUrl"))

    @azure_blob_container_url.setter
    def azure_blob_container_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__795c3fa003f02e9d97d1fae401c02ed1af3b616ece635550bbc9fd6c2e0dde05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureBlobContainerUrl", value)

    @builtins.property
    @jsii.member(jsii_name="azureBlobSasConfiguration")
    def azure_blob_sas_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationAzureBlob.AzureBlobSasConfigurationProperty"]]:
        '''Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationAzureBlob.AzureBlobSasConfigurationProperty"]], jsii.get(self, "azureBlobSasConfiguration"))

    @azure_blob_sas_configuration.setter
    def azure_blob_sas_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationAzureBlob.AzureBlobSasConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60754be8cb63c6569b923d0c78a823449ddaa3c5aba51833aae257e02f1bd392)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureBlobSasConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="azureBlobType")
    def azure_blob_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureBlobType"))

    @azure_blob_type.setter
    def azure_blob_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e74328b40eb55d86e422d5f30530d28f29d1393792015d7646eb06c8819408d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureBlobType", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, ``/my/images`` ).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__861788b0a9a32f402ab93793acdec22ae6bb15d217371b8ba36d7cb8ba33fc6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49f572b838ff9ece4d89d77403924adeec2030197b239758db39cea71436acfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationAzureBlob.AzureBlobSasConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"azure_blob_sas_token": "azureBlobSasToken"},
    )
    class AzureBlobSasConfigurationProperty:
        def __init__(self, *, azure_blob_sas_token: builtins.str) -> None:
            '''The shared access signature (SAS) configuration that allows AWS DataSync to access your Microsoft Azure Blob Storage.

            For more information, see `SAS tokens <https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-sas-tokens>`_ for accessing your Azure Blob Storage.

            :param azure_blob_sas_token: Specifies a SAS token that provides permissions to access your Azure Blob Storage. The token is part of the SAS URI string that comes after the storage resource URI and a question mark. A token looks something like this: ``sp=r&st=2023-12-20T14:54:52Z&se=2023-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=aBBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationazureblob-azureblobsasconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                azure_blob_sas_configuration_property = datasync.CfnLocationAzureBlob.AzureBlobSasConfigurationProperty(
                    azure_blob_sas_token="azureBlobSasToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3b97bd3f13ec4166f121eb8229b7a3322702a4782d767aca2fc1323e923cced8)
                check_type(argname="argument azure_blob_sas_token", value=azure_blob_sas_token, expected_type=type_hints["azure_blob_sas_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "azure_blob_sas_token": azure_blob_sas_token,
            }

        @builtins.property
        def azure_blob_sas_token(self) -> builtins.str:
            '''Specifies a SAS token that provides permissions to access your Azure Blob Storage.

            The token is part of the SAS URI string that comes after the storage resource URI and a question mark. A token looks something like this:

            ``sp=r&st=2023-12-20T14:54:52Z&se=2023-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=aBBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationazureblob-azureblobsasconfiguration.html#cfn-datasync-locationazureblob-azureblobsasconfiguration-azureblobsastoken
            '''
            result = self._values.get("azure_blob_sas_token")
            assert result is not None, "Required property 'azure_blob_sas_token' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AzureBlobSasConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationAzureBlobProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_arns": "agentArns",
        "azure_blob_authentication_type": "azureBlobAuthenticationType",
        "azure_access_tier": "azureAccessTier",
        "azure_blob_container_url": "azureBlobContainerUrl",
        "azure_blob_sas_configuration": "azureBlobSasConfiguration",
        "azure_blob_type": "azureBlobType",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationAzureBlobProps:
    def __init__(
        self,
        *,
        agent_arns: typing.Sequence[builtins.str],
        azure_blob_authentication_type: builtins.str,
        azure_access_tier: typing.Optional[builtins.str] = None,
        azure_blob_container_url: typing.Optional[builtins.str] = None,
        azure_blob_sas_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationAzureBlob.AzureBlobSasConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        azure_blob_type: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationAzureBlob``.

        :param agent_arns: Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container. You can specify more than one agent. For more information, see `Using multiple agents for your transfer <https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html>`_ .
        :param azure_blob_authentication_type: Specifies the authentication method DataSync uses to access your Azure Blob Storage. DataSync can access blob storage using a shared access signature (SAS). Default: - "SAS"
        :param azure_access_tier: Specifies the access tier that you want your objects or files transferred into. This only applies when using the location as a transfer destination. For more information, see `Access tiers <https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers>`_ . Default: - "HOT"
        :param azure_blob_container_url: Specifies the URL of the Azure Blob Storage container involved in your transfer.
        :param azure_blob_sas_configuration: Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.
        :param azure_blob_type: Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the `Azure Blob Storage documentation <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs>`_ . Default: - "BLOCK"
        :param subdirectory: Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, ``/my/images`` ).
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your transfer location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_azure_blob_props = datasync.CfnLocationAzureBlobProps(
                agent_arns=["agentArns"],
                azure_blob_authentication_type="azureBlobAuthenticationType",
            
                # the properties below are optional
                azure_access_tier="azureAccessTier",
                azure_blob_container_url="azureBlobContainerUrl",
                azure_blob_sas_configuration=datasync.CfnLocationAzureBlob.AzureBlobSasConfigurationProperty(
                    azure_blob_sas_token="azureBlobSasToken"
                ),
                azure_blob_type="azureBlobType",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d386b9f5845962fa66385393ccc6424f66b9aee312fecdc96fe3ec242f754bf1)
            check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            check_type(argname="argument azure_blob_authentication_type", value=azure_blob_authentication_type, expected_type=type_hints["azure_blob_authentication_type"])
            check_type(argname="argument azure_access_tier", value=azure_access_tier, expected_type=type_hints["azure_access_tier"])
            check_type(argname="argument azure_blob_container_url", value=azure_blob_container_url, expected_type=type_hints["azure_blob_container_url"])
            check_type(argname="argument azure_blob_sas_configuration", value=azure_blob_sas_configuration, expected_type=type_hints["azure_blob_sas_configuration"])
            check_type(argname="argument azure_blob_type", value=azure_blob_type, expected_type=type_hints["azure_blob_type"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arns": agent_arns,
            "azure_blob_authentication_type": azure_blob_authentication_type,
        }
        if azure_access_tier is not None:
            self._values["azure_access_tier"] = azure_access_tier
        if azure_blob_container_url is not None:
            self._values["azure_blob_container_url"] = azure_blob_container_url
        if azure_blob_sas_configuration is not None:
            self._values["azure_blob_sas_configuration"] = azure_blob_sas_configuration
        if azure_blob_type is not None:
            self._values["azure_blob_type"] = azure_blob_type
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_arns(self) -> typing.List[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container.

        You can specify more than one agent. For more information, see `Using multiple agents for your transfer <https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-agentarns
        '''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def azure_blob_authentication_type(self) -> builtins.str:
        '''Specifies the authentication method DataSync uses to access your Azure Blob Storage.

        DataSync can access blob storage using a shared access signature (SAS).

        :default: - "SAS"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureblobauthenticationtype
        '''
        result = self._values.get("azure_blob_authentication_type")
        assert result is not None, "Required property 'azure_blob_authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def azure_access_tier(self) -> typing.Optional[builtins.str]:
        '''Specifies the access tier that you want your objects or files transferred into.

        This only applies when using the location as a transfer destination. For more information, see `Access tiers <https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers>`_ .

        :default: - "HOT"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureaccesstier
        '''
        result = self._values.get("azure_access_tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_blob_container_url(self) -> typing.Optional[builtins.str]:
        '''Specifies the URL of the Azure Blob Storage container involved in your transfer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureblobcontainerurl
        '''
        result = self._values.get("azure_blob_container_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_blob_sas_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationAzureBlob.AzureBlobSasConfigurationProperty]]:
        '''Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureblobsasconfiguration
        '''
        result = self._values.get("azure_blob_sas_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationAzureBlob.AzureBlobSasConfigurationProperty]], result)

    @builtins.property
    def azure_blob_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage.

        Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the `Azure Blob Storage documentation <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs>`_ .

        :default: - "BLOCK"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureblobtype
        '''
        result = self._values.get("azure_blob_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, ``/my/images`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.

        We recommend creating at least a name tag for your transfer location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationAzureBlobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationEFS(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationEFS",
):
    '''The ``AWS::DataSync::LocationEFS`` resource creates an endpoint for an Amazon EFS file system.

    AWS DataSync can access this endpoint as a source or destination location.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html
    :cloudformationResource: AWS::DataSync::LocationEFS
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_eFS = datasync.CfnLocationEFS(self, "MyCfnLocationEFS",
            ec2_config=datasync.CfnLocationEFS.Ec2ConfigProperty(
                security_group_arns=["securityGroupArns"],
                subnet_arn="subnetArn"
            ),
        
            # the properties below are optional
            access_point_arn="accessPointArn",
            efs_filesystem_arn="efsFilesystemArn",
            file_system_access_role_arn="fileSystemAccessRoleArn",
            in_transit_encryption="inTransitEncryption",
            subdirectory="subdirectory",
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
        ec2_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationEFS.Ec2ConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        access_point_arn: typing.Optional[builtins.str] = None,
        efs_filesystem_arn: typing.Optional[builtins.str] = None,
        file_system_access_role_arn: typing.Optional[builtins.str] = None,
        in_transit_encryption: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ec2_config: Specifies the subnet and security groups DataSync uses to access your Amazon EFS file system.
        :param access_point_arn: Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to access the Amazon EFS file system.
        :param efs_filesystem_arn: Specifies the ARN for the Amazon EFS file system.
        :param file_system_access_role_arn: Specifies an AWS Identity and Access Management (IAM) role that DataSync assumes when mounting the Amazon EFS file system.
        :param in_transit_encryption: Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it copies data to or from the Amazon EFS file system. If you specify an access point using ``AccessPointArn`` or an IAM role using ``FileSystemAccessRoleArn`` , you must set this parameter to ``TLS1_2`` .
        :param subdirectory: Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data (depending on if this is a source or destination location). By default, DataSync uses the root directory, but you can also include subdirectories. .. epigraph:: You must specify a value with forward slashes (for example, ``/path/to/folder`` ).
        :param tags: Specifies the key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f2ede238fa34ab9a0ff568aeab0bbaa47ee9542611afbf58163acd201706303)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationEFSProps(
            ec2_config=ec2_config,
            access_point_arn=access_point_arn,
            efs_filesystem_arn=efs_filesystem_arn,
            file_system_access_role_arn=file_system_access_role_arn,
            in_transit_encryption=in_transit_encryption,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__525f362005e39a7a0c870fbf4abfc0e5c277ffc6df5e1c59dc837aa27682d7b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3212431159a669650412490f33351420b4d25f3e521ae34f0776a8c33c44638f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon EFS file system.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the Amazon EFS file system.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="ec2Config")
    def ec2_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLocationEFS.Ec2ConfigProperty"]:
        '''Specifies the subnet and security groups DataSync uses to access your Amazon EFS file system.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLocationEFS.Ec2ConfigProperty"], jsii.get(self, "ec2Config"))

    @ec2_config.setter
    def ec2_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLocationEFS.Ec2ConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d49a9691cc648acec6401c31a8bd66d218ef81be6a8c7372287fd0137a541e69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2Config", value)

    @builtins.property
    @jsii.member(jsii_name="accessPointArn")
    def access_point_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to access the Amazon EFS file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessPointArn"))

    @access_point_arn.setter
    def access_point_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a5354be840dc5932b18b5eb78c21c9212f8dfeaf26584c5369c42c79b0feda0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPointArn", value)

    @builtins.property
    @jsii.member(jsii_name="efsFilesystemArn")
    def efs_filesystem_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the ARN for the Amazon EFS file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "efsFilesystemArn"))

    @efs_filesystem_arn.setter
    def efs_filesystem_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1daff75583eb771bbf36150a90de86f19ae11bcb1891de8abe3057537f0e6439)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "efsFilesystemArn", value)

    @builtins.property
    @jsii.member(jsii_name="fileSystemAccessRoleArn")
    def file_system_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies an AWS Identity and Access Management (IAM) role that DataSync assumes when mounting the Amazon EFS file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemAccessRoleArn"))

    @file_system_access_role_arn.setter
    def file_system_access_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b6f2d80c69bdbcb291a9018a79abaac597880c119d6d606fc8af02dd73a8289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="inTransitEncryption")
    def in_transit_encryption(self) -> typing.Optional[builtins.str]:
        '''Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it copies data to or from the Amazon EFS file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inTransitEncryption"))

    @in_transit_encryption.setter
    def in_transit_encryption(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0148fd532364a7b64fc661f81d6f489722b42c925d8bb2ca2c363cec6d7aa6fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inTransitEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies a mount path for your Amazon EFS file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c79c757570d3b36786238e89b35ce024a869534edc2665cbf1292460b498cc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the key-value pair that represents a tag that you want to add to the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e70a483245df685cb33e660b85ed2768354b191a41a3909b76b309f43c43c73e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationEFS.Ec2ConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_arns": "securityGroupArns",
            "subnet_arn": "subnetArn",
        },
    )
    class Ec2ConfigProperty:
        def __init__(
            self,
            *,
            security_group_arns: typing.Sequence[builtins.str],
            subnet_arn: builtins.str,
        ) -> None:
            '''The subnet and security groups that AWS DataSync uses to access your Amazon EFS file system.

            :param security_group_arns: Specifies the Amazon Resource Names (ARNs) of the security groups associated with an Amazon EFS file system's mount target.
            :param subnet_arn: Specifies the ARN of a subnet where DataSync creates the `network interfaces <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces>`_ for managing traffic during your transfer. The subnet must be located: - In the same virtual private cloud (VPC) as the Amazon EFS file system. - In the same Availability Zone as at least one mount target for the Amazon EFS file system. .. epigraph:: You don't need to specify a subnet that includes a file system mount target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                ec2_config_property = datasync.CfnLocationEFS.Ec2ConfigProperty(
                    security_group_arns=["securityGroupArns"],
                    subnet_arn="subnetArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__17d7739807e0941f242944e9f35ecd7849678f3d74f7a74f34b42fd7260f4cdb)
                check_type(argname="argument security_group_arns", value=security_group_arns, expected_type=type_hints["security_group_arns"])
                check_type(argname="argument subnet_arn", value=subnet_arn, expected_type=type_hints["subnet_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_arns": security_group_arns,
                "subnet_arn": subnet_arn,
            }

        @builtins.property
        def security_group_arns(self) -> typing.List[builtins.str]:
            '''Specifies the Amazon Resource Names (ARNs) of the security groups associated with an Amazon EFS file system's mount target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-securitygrouparns
            '''
            result = self._values.get("security_group_arns")
            assert result is not None, "Required property 'security_group_arns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_arn(self) -> builtins.str:
            '''Specifies the ARN of a subnet where DataSync creates the `network interfaces <https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces>`_ for managing traffic during your transfer.

            The subnet must be located:

            - In the same virtual private cloud (VPC) as the Amazon EFS file system.
            - In the same Availability Zone as at least one mount target for the Amazon EFS file system.

            .. epigraph::

               You don't need to specify a subnet that includes a file system mount target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-subnetarn
            '''
            result = self._values.get("subnet_arn")
            assert result is not None, "Required property 'subnet_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ec2ConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationEFSProps",
    jsii_struct_bases=[],
    name_mapping={
        "ec2_config": "ec2Config",
        "access_point_arn": "accessPointArn",
        "efs_filesystem_arn": "efsFilesystemArn",
        "file_system_access_role_arn": "fileSystemAccessRoleArn",
        "in_transit_encryption": "inTransitEncryption",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationEFSProps:
    def __init__(
        self,
        *,
        ec2_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationEFS.Ec2ConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        access_point_arn: typing.Optional[builtins.str] = None,
        efs_filesystem_arn: typing.Optional[builtins.str] = None,
        file_system_access_role_arn: typing.Optional[builtins.str] = None,
        in_transit_encryption: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationEFS``.

        :param ec2_config: Specifies the subnet and security groups DataSync uses to access your Amazon EFS file system.
        :param access_point_arn: Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to access the Amazon EFS file system.
        :param efs_filesystem_arn: Specifies the ARN for the Amazon EFS file system.
        :param file_system_access_role_arn: Specifies an AWS Identity and Access Management (IAM) role that DataSync assumes when mounting the Amazon EFS file system.
        :param in_transit_encryption: Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it copies data to or from the Amazon EFS file system. If you specify an access point using ``AccessPointArn`` or an IAM role using ``FileSystemAccessRoleArn`` , you must set this parameter to ``TLS1_2`` .
        :param subdirectory: Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data (depending on if this is a source or destination location). By default, DataSync uses the root directory, but you can also include subdirectories. .. epigraph:: You must specify a value with forward slashes (for example, ``/path/to/folder`` ).
        :param tags: Specifies the key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_eFSProps = datasync.CfnLocationEFSProps(
                ec2_config=datasync.CfnLocationEFS.Ec2ConfigProperty(
                    security_group_arns=["securityGroupArns"],
                    subnet_arn="subnetArn"
                ),
            
                # the properties below are optional
                access_point_arn="accessPointArn",
                efs_filesystem_arn="efsFilesystemArn",
                file_system_access_role_arn="fileSystemAccessRoleArn",
                in_transit_encryption="inTransitEncryption",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd308e189fe63ce2cc80398d76a37684d9c1c36b8dfa1dfed227e06d9f65ca69)
            check_type(argname="argument ec2_config", value=ec2_config, expected_type=type_hints["ec2_config"])
            check_type(argname="argument access_point_arn", value=access_point_arn, expected_type=type_hints["access_point_arn"])
            check_type(argname="argument efs_filesystem_arn", value=efs_filesystem_arn, expected_type=type_hints["efs_filesystem_arn"])
            check_type(argname="argument file_system_access_role_arn", value=file_system_access_role_arn, expected_type=type_hints["file_system_access_role_arn"])
            check_type(argname="argument in_transit_encryption", value=in_transit_encryption, expected_type=type_hints["in_transit_encryption"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ec2_config": ec2_config,
        }
        if access_point_arn is not None:
            self._values["access_point_arn"] = access_point_arn
        if efs_filesystem_arn is not None:
            self._values["efs_filesystem_arn"] = efs_filesystem_arn
        if file_system_access_role_arn is not None:
            self._values["file_system_access_role_arn"] = file_system_access_role_arn
        if in_transit_encryption is not None:
            self._values["in_transit_encryption"] = in_transit_encryption
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def ec2_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLocationEFS.Ec2ConfigProperty]:
        '''Specifies the subnet and security groups DataSync uses to access your Amazon EFS file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-ec2config
        '''
        result = self._values.get("ec2_config")
        assert result is not None, "Required property 'ec2_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLocationEFS.Ec2ConfigProperty], result)

    @builtins.property
    def access_point_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to access the Amazon EFS file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-accesspointarn
        '''
        result = self._values.get("access_point_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def efs_filesystem_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the ARN for the Amazon EFS file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-efsfilesystemarn
        '''
        result = self._values.get("efs_filesystem_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies an AWS Identity and Access Management (IAM) role that DataSync assumes when mounting the Amazon EFS file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-filesystemaccessrolearn
        '''
        result = self._values.get("file_system_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def in_transit_encryption(self) -> typing.Optional[builtins.str]:
        '''Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it copies data to or from the Amazon EFS file system.

        If you specify an access point using ``AccessPointArn`` or an IAM role using ``FileSystemAccessRoleArn`` , you must set this parameter to ``TLS1_2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-intransitencryption
        '''
        result = self._values.get("in_transit_encryption")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies a mount path for your Amazon EFS file system.

        This is where DataSync reads or writes data (depending on if this is a source or destination location). By default, DataSync uses the root directory, but you can also include subdirectories.
        .. epigraph::

           You must specify a value with forward slashes (for example, ``/path/to/folder`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the key-value pair that represents a tag that you want to add to the resource.

        The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationEFSProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationFSxLustre(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxLustre",
):
    '''The ``AWS::DataSync::LocationFSxLustre`` resource specifies an endpoint for an Amazon FSx for Lustre file system.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html
    :cloudformationResource: AWS::DataSync::LocationFSxLustre
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_fSx_lustre = datasync.CfnLocationFSxLustre(self, "MyCfnLocationFSxLustre",
            security_group_arns=["securityGroupArns"],
        
            # the properties below are optional
            fsx_filesystem_arn="fsxFilesystemArn",
            subdirectory="subdirectory",
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
        security_group_arns: typing.Sequence[builtins.str],
        fsx_filesystem_arn: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_group_arns: The ARNs of the security groups that are used to configure the FSx for Lustre file system. *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$`` *Length constraints* : Maximum length of 128.
        :param fsx_filesystem_arn: The Amazon Resource Name (ARN) for the FSx for Lustre file system.
        :param subdirectory: A subdirectory in the location's path. This subdirectory in the FSx for Lustre file system is used to read data from the FSx for Lustre source location or write data to the FSx for Lustre destination.
        :param tags: The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6a366fbae202f0039019565ac7d26837d23db858eddf6c8193ddf4bd207f597)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationFSxLustreProps(
            security_group_arns=security_group_arns,
            fsx_filesystem_arn=fsx_filesystem_arn,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332f63f71b2f53346897bbd853b4475cc78f7de950e12cd596388ff61046d9c9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f97bf53ea28971717bcec4e0b4b238ec382a67beac05ae5d4cec2c272e4d0dbd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The ARN of the specified FSx for Lustre file system location.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the specified FSx for Lustre file system location.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="securityGroupArns")
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of the security groups that are used to configure the FSx for Lustre file system.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupArns"))

    @security_group_arns.setter
    def security_group_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99604bc3d8ba3f9cebd4d615800e9e9a5eaa9a24ac1406cc329212e19bb3f563)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupArns", value)

    @builtins.property
    @jsii.member(jsii_name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the FSx for Lustre file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsxFilesystemArn"))

    @fsx_filesystem_arn.setter
    def fsx_filesystem_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f40986c7e15e37098358bbc0b06f54552260ebd0c2cbbb23d0aa7575a77572d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsxFilesystemArn", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''A subdirectory in the location's path.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2de39d8f3d5835ff4125e18bd0c7dc9e8523a72a468c28a594ec8bcbcfc0280)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The key-value pair that represents a tag that you want to add to the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a21025c45a3ae349b404b0660292a1df2a3f9dfb1668c68c70eaac990ad31495)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxLustreProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_arns": "securityGroupArns",
        "fsx_filesystem_arn": "fsxFilesystemArn",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationFSxLustreProps:
    def __init__(
        self,
        *,
        security_group_arns: typing.Sequence[builtins.str],
        fsx_filesystem_arn: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationFSxLustre``.

        :param security_group_arns: The ARNs of the security groups that are used to configure the FSx for Lustre file system. *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$`` *Length constraints* : Maximum length of 128.
        :param fsx_filesystem_arn: The Amazon Resource Name (ARN) for the FSx for Lustre file system.
        :param subdirectory: A subdirectory in the location's path. This subdirectory in the FSx for Lustre file system is used to read data from the FSx for Lustre source location or write data to the FSx for Lustre destination.
        :param tags: The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_fSx_lustre_props = datasync.CfnLocationFSxLustreProps(
                security_group_arns=["securityGroupArns"],
            
                # the properties below are optional
                fsx_filesystem_arn="fsxFilesystemArn",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb4c1967b655fb7ba3b02e398f8b2dc61e2cb372e8e862f4aea92b2ccf89bd90)
            check_type(argname="argument security_group_arns", value=security_group_arns, expected_type=type_hints["security_group_arns"])
            check_type(argname="argument fsx_filesystem_arn", value=fsx_filesystem_arn, expected_type=type_hints["fsx_filesystem_arn"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_arns": security_group_arns,
        }
        if fsx_filesystem_arn is not None:
            self._values["fsx_filesystem_arn"] = fsx_filesystem_arn
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of the security groups that are used to configure the FSx for Lustre file system.

        *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$``

        *Length constraints* : Maximum length of 128.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html#cfn-datasync-locationfsxlustre-securitygrouparns
        '''
        result = self._values.get("security_group_arns")
        assert result is not None, "Required property 'security_group_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def fsx_filesystem_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the FSx for Lustre file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html#cfn-datasync-locationfsxlustre-fsxfilesystemarn
        '''
        result = self._values.get("fsx_filesystem_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''A subdirectory in the location's path.

        This subdirectory in the FSx for Lustre file system is used to read data from the FSx for Lustre source location or write data to the FSx for Lustre destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html#cfn-datasync-locationfsxlustre-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The key-value pair that represents a tag that you want to add to the resource.

        The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html#cfn-datasync-locationfsxlustre-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationFSxLustreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationFSxONTAP(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxONTAP",
):
    '''The ``AWS::DataSync::LocationFSxONTAP`` resource creates an endpoint for an Amazon FSx for NetApp ONTAP file system.

    AWS DataSync can access this endpoint as a source or destination location.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html
    :cloudformationResource: AWS::DataSync::LocationFSxONTAP
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_fSx_oNTAP = datasync.CfnLocationFSxONTAP(self, "MyCfnLocationFSxONTAP",
            security_group_arns=["securityGroupArns"],
            storage_virtual_machine_arn="storageVirtualMachineArn",
        
            # the properties below are optional
            protocol=datasync.CfnLocationFSxONTAP.ProtocolProperty(
                nfs=datasync.CfnLocationFSxONTAP.NFSProperty(
                    mount_options=datasync.CfnLocationFSxONTAP.NfsMountOptionsProperty(
                        version="version"
                    )
                ),
                smb=datasync.CfnLocationFSxONTAP.SMBProperty(
                    mount_options=datasync.CfnLocationFSxONTAP.SmbMountOptionsProperty(
                        version="version"
                    ),
                    password="password",
                    user="user",
        
                    # the properties below are optional
                    domain="domain"
                )
            ),
            subdirectory="subdirectory",
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
        security_group_arns: typing.Sequence[builtins.str],
        storage_virtual_machine_arn: builtins.str,
        protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationFSxONTAP.ProtocolProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_group_arns: Specifies the Amazon Resource Names (ARNs) of the security groups that DataSync can use to access your FSx for ONTAP file system. You must configure the security groups to allow outbound traffic on the following ports (depending on the protocol that you're using): - *Network File System (NFS)* : TCP ports 111, 635, and 2049 - *Server Message Block (SMB)* : TCP port 445 Your file system's security groups must also allow inbound traffic on the same port.
        :param storage_virtual_machine_arn: Specifies the ARN of the storage virtual machine (SVM) in your file system where you want to copy data to or from.
        :param protocol: Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.
        :param subdirectory: Specifies a path to the file share in the SVM where you'll copy your data. You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be ``/vol1`` , ``/vol1/tree1`` , or ``/share1`` . .. epigraph:: Don't specify a junction path in the SVM's root volume. For more information, see `Managing FSx for ONTAP storage virtual machines <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html>`_ in the *Amazon FSx for NetApp ONTAP User Guide* .
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e90aee609011bf6205e58d539383e731c53e81e52f2c60ef5d94494c4efecc80)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationFSxONTAPProps(
            security_group_arns=security_group_arns,
            storage_virtual_machine_arn=storage_virtual_machine_arn,
            protocol=protocol,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f2c1a750537c459c40274b80eb75ffeda15c9ed3de3b01eed5b59c97b35e4bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c959eff12bc94e8be3c884c6e634a1457d1afa3b8f64323154a19f3e7e5fe14)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrFsxFilesystemArn")
    def attr_fsx_filesystem_arn(self) -> builtins.str:
        '''The ARN of the FSx for ONTAP file system in the specified location.

        :cloudformationAttribute: FsxFilesystemArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFsxFilesystemArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The ARN of the specified location.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the specified location.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="securityGroupArns")
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''Specifies the Amazon Resource Names (ARNs) of the security groups that DataSync can use to access your FSx for ONTAP file system.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupArns"))

    @security_group_arns.setter
    def security_group_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43462066b9ef98956b46d8c5c9b702871e858cd735a7625c74fc7ccbcf3881a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupArns", value)

    @builtins.property
    @jsii.member(jsii_name="storageVirtualMachineArn")
    def storage_virtual_machine_arn(self) -> builtins.str:
        '''Specifies the ARN of the storage virtual machine (SVM) in your file system where you want to copy data to or from.'''
        return typing.cast(builtins.str, jsii.get(self, "storageVirtualMachineArn"))

    @storage_virtual_machine_arn.setter
    def storage_virtual_machine_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f60908dedc90f4e4aaa149c48a33bbbbc89033f34371228431f30831e0fb33b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageVirtualMachineArn", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.ProtocolProperty"]]:
        '''Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.ProtocolProperty"]], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.ProtocolProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5733cffea1e4acc30fa46f3869492191e577ff7fb19e3b0a0964257388c93711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies a path to the file share in the SVM where you'll copy your data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1a8a96a468989ae9c3368522664b5a8e7caf45b58424f818667a6642c442f18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf18f603ac473d61e4ddeeabdd924bdda3ada2926fd940579ba552851ac8e4a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxONTAP.NFSProperty",
        jsii_struct_bases=[],
        name_mapping={"mount_options": "mountOptions"},
    )
    class NFSProperty:
        def __init__(
            self,
            *,
            mount_options: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationFSxONTAP.NfsMountOptionsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies the Network File System (NFS) protocol configuration that AWS DataSync uses to access a storage virtual machine (SVM) on your Amazon FSx for NetApp ONTAP file system.

            For more information, see `Accessing FSx for ONTAP file systems <https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access>`_ .

            :param mount_options: Specifies how DataSync can access a location using the NFS protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                n_fSProperty = datasync.CfnLocationFSxONTAP.NFSProperty(
                    mount_options=datasync.CfnLocationFSxONTAP.NfsMountOptionsProperty(
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d906f77d136eff99651e2ce7c223df26baf12fd4ff6587250dd429255fe44e40)
                check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mount_options": mount_options,
            }

        @builtins.property
        def mount_options(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.NfsMountOptionsProperty"]:
            '''Specifies how DataSync can access a location using the NFS protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfs.html#cfn-datasync-locationfsxontap-nfs-mountoptions
            '''
            result = self._values.get("mount_options")
            assert result is not None, "Required property 'mount_options' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.NfsMountOptionsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NFSProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxONTAP.NfsMountOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"version": "version"},
    )
    class NfsMountOptionsProperty:
        def __init__(self, *, version: typing.Optional[builtins.str] = None) -> None:
            '''Specifies how DataSync can access a location using the NFS protocol.

            :param version: Specifies the NFS version that you want DataSync to use when mounting your NFS share. If the server refuses to use the version specified, the task fails. You can specify the following options: - ``AUTOMATIC`` (default): DataSync chooses NFS version 4.1. - ``NFS3`` : Stateless protocol version that allows for asynchronous writes on the server. - ``NFSv4_0`` : Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems. - ``NFSv4_1`` : Stateful protocol version that supports sessions, directory delegations, and parallel data processing. NFS version 4.1 also includes all features available in version 4.0. .. epigraph:: DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfsmountoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                nfs_mount_options_property = datasync.CfnLocationFSxONTAP.NfsMountOptionsProperty(
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4dc53c3b8f4ac95cd4581df290c1b03f1580286e8f150e8c15513946465d8f08)
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''Specifies the NFS version that you want DataSync to use when mounting your NFS share.

            If the server refuses to use the version specified, the task fails.

            You can specify the following options:

            - ``AUTOMATIC`` (default): DataSync chooses NFS version 4.1.
            - ``NFS3`` : Stateless protocol version that allows for asynchronous writes on the server.
            - ``NFSv4_0`` : Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems.
            - ``NFSv4_1`` : Stateful protocol version that supports sessions, directory delegations, and parallel data processing. NFS version 4.1 also includes all features available in version 4.0.

            .. epigraph::

               DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfsmountoptions.html#cfn-datasync-locationfsxontap-nfsmountoptions-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NfsMountOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxONTAP.ProtocolProperty",
        jsii_struct_bases=[],
        name_mapping={"nfs": "nfs", "smb": "smb"},
    )
    class ProtocolProperty:
        def __init__(
            self,
            *,
            nfs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationFSxONTAP.NFSProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            smb: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationFSxONTAP.SMBProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the data transfer protocol that AWS DataSync uses to access your Amazon FSx file system.

            :param nfs: Specifies the Network File System (NFS) protocol configuration that DataSync uses to access your FSx for ONTAP file system's storage virtual machine (SVM).
            :param smb: Specifies the Server Message Block (SMB) protocol configuration that DataSync uses to access your FSx for ONTAP file system's SVM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                protocol_property = datasync.CfnLocationFSxONTAP.ProtocolProperty(
                    nfs=datasync.CfnLocationFSxONTAP.NFSProperty(
                        mount_options=datasync.CfnLocationFSxONTAP.NfsMountOptionsProperty(
                            version="version"
                        )
                    ),
                    smb=datasync.CfnLocationFSxONTAP.SMBProperty(
                        mount_options=datasync.CfnLocationFSxONTAP.SmbMountOptionsProperty(
                            version="version"
                        ),
                        password="password",
                        user="user",
                
                        # the properties below are optional
                        domain="domain"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__232010cfdb13b273652e859ad8547bc7677b6700a32713cd27647e3b35759f4e)
                check_type(argname="argument nfs", value=nfs, expected_type=type_hints["nfs"])
                check_type(argname="argument smb", value=smb, expected_type=type_hints["smb"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if nfs is not None:
                self._values["nfs"] = nfs
            if smb is not None:
                self._values["smb"] = smb

        @builtins.property
        def nfs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.NFSProperty"]]:
            '''Specifies the Network File System (NFS) protocol configuration that DataSync uses to access your FSx for ONTAP file system's storage virtual machine (SVM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html#cfn-datasync-locationfsxontap-protocol-nfs
            '''
            result = self._values.get("nfs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.NFSProperty"]], result)

        @builtins.property
        def smb(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.SMBProperty"]]:
            '''Specifies the Server Message Block (SMB) protocol configuration that DataSync uses to access your FSx for ONTAP file system's SVM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html#cfn-datasync-locationfsxontap-protocol-smb
            '''
            result = self._values.get("smb")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.SMBProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProtocolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxONTAP.SMBProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mount_options": "mountOptions",
            "password": "password",
            "user": "user",
            "domain": "domain",
        },
    )
    class SMBProperty:
        def __init__(
            self,
            *,
            mount_options: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationFSxONTAP.SmbMountOptionsProperty", typing.Dict[builtins.str, typing.Any]]],
            password: builtins.str,
            user: builtins.str,
            domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the Server Message Block (SMB) protocol configuration that AWS DataSync uses to access a storage virtual machine (SVM) on your Amazon FSx for NetApp ONTAP file system.

            For more information, see `Accessing FSx for ONTAP file systems <https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access>`_ .

            :param mount_options: Specifies how DataSync can access a location using the SMB protocol.
            :param password: Specifies the password of a user who has permission to access your SVM.
            :param user: Specifies a user name that can mount the location and access the files, folders, and metadata that you need in the SVM. If you provide a user in your Active Directory, note the following: - If you're using AWS Directory Service for Microsoft Active Directory , the user must be a member of the AWS Delegated FSx Administrators group. - If you're using a self-managed Active Directory, the user must be a member of either the Domain Admins group or a custom group that you specified for file system administration when you created your file system. Make sure that the user has the permissions it needs to copy the data you want: - ``SE_TCB_NAME`` : Required to set object ownership and file metadata. With this privilege, you also can copy NTFS discretionary access lists (DACLs). - ``SE_SECURITY_NAME`` : May be needed to copy NTFS system access control lists (SACLs). This operation specifically requires the Windows privilege, which is granted to members of the Domain Admins group. If you configure your task to copy SACLs, make sure that the user has the required privileges. For information about copying SACLs, see `Ownership and permissions-related options <https://docs.aws.amazon.com/datasync/latest/userguide/create-task.html#configure-ownership-and-permissions>`_ .
            :param domain: Specifies the fully qualified domain name (FQDN) of the Microsoft Active Directory that your storage virtual machine (SVM) belongs to. If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right SVM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                s_mBProperty = datasync.CfnLocationFSxONTAP.SMBProperty(
                    mount_options=datasync.CfnLocationFSxONTAP.SmbMountOptionsProperty(
                        version="version"
                    ),
                    password="password",
                    user="user",
                
                    # the properties below are optional
                    domain="domain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa05e4e2966437016f666744220c772c1b0c0e2c81f8e8e7f44a5b139fc021d0)
                check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
                check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mount_options": mount_options,
                "password": password,
                "user": user,
            }
            if domain is not None:
                self._values["domain"] = domain

        @builtins.property
        def mount_options(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.SmbMountOptionsProperty"]:
            '''Specifies how DataSync can access a location using the SMB protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html#cfn-datasync-locationfsxontap-smb-mountoptions
            '''
            result = self._values.get("mount_options")
            assert result is not None, "Required property 'mount_options' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLocationFSxONTAP.SmbMountOptionsProperty"], result)

        @builtins.property
        def password(self) -> builtins.str:
            '''Specifies the password of a user who has permission to access your SVM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html#cfn-datasync-locationfsxontap-smb-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user(self) -> builtins.str:
            '''Specifies a user name that can mount the location and access the files, folders, and metadata that you need in the SVM.

            If you provide a user in your Active Directory, note the following:

            - If you're using AWS Directory Service for Microsoft Active Directory , the user must be a member of the AWS Delegated FSx Administrators group.
            - If you're using a self-managed Active Directory, the user must be a member of either the Domain Admins group or a custom group that you specified for file system administration when you created your file system.

            Make sure that the user has the permissions it needs to copy the data you want:

            - ``SE_TCB_NAME`` : Required to set object ownership and file metadata. With this privilege, you also can copy NTFS discretionary access lists (DACLs).
            - ``SE_SECURITY_NAME`` : May be needed to copy NTFS system access control lists (SACLs). This operation specifically requires the Windows privilege, which is granted to members of the Domain Admins group. If you configure your task to copy SACLs, make sure that the user has the required privileges. For information about copying SACLs, see `Ownership and permissions-related options <https://docs.aws.amazon.com/datasync/latest/userguide/create-task.html#configure-ownership-and-permissions>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html#cfn-datasync-locationfsxontap-smb-user
            '''
            result = self._values.get("user")
            assert result is not None, "Required property 'user' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def domain(self) -> typing.Optional[builtins.str]:
            '''Specifies the fully qualified domain name (FQDN) of the Microsoft Active Directory that your storage virtual machine (SVM) belongs to.

            If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right SVM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html#cfn-datasync-locationfsxontap-smb-domain
            '''
            result = self._values.get("domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SMBProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxONTAP.SmbMountOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"version": "version"},
    )
    class SmbMountOptionsProperty:
        def __init__(self, *, version: typing.Optional[builtins.str] = None) -> None:
            '''Specifies the version of the Server Message Block (SMB) protocol that AWS DataSync uses to access an SMB file server.

            :param version: By default, DataSync automatically chooses an SMB protocol version based on negotiation with your SMB file server. You also can configure DataSync to use a specific SMB version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically. These are the following options for configuring the SMB version: - ``AUTOMATIC`` (default): DataSync and the SMB file server negotiate the highest version of SMB that they mutually support between 2.1 and 3.1.1. This is the recommended option. If you instead choose a specific version that your file server doesn't support, you may get an ``Operation Not Supported`` error. - ``SMB3`` : Restricts the protocol negotiation to only SMB version 3.0.2. - ``SMB2`` : Restricts the protocol negotiation to only SMB version 2.1. - ``SMB2_0`` : Restricts the protocol negotiation to only SMB version 2.0. - ``SMB1`` : Restricts the protocol negotiation to only SMB version 1.0. .. epigraph:: The ``SMB1`` option isn't available when `creating an Amazon FSx for NetApp ONTAP location <https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smbmountoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                smb_mount_options_property = datasync.CfnLocationFSxONTAP.SmbMountOptionsProperty(
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91fd30cfcc64f01817f69da9fc6b6a4e13642f15c75979166fdab51ee88f8a8e)
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''By default, DataSync automatically chooses an SMB protocol version based on negotiation with your SMB file server.

            You also can configure DataSync to use a specific SMB version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically.

            These are the following options for configuring the SMB version:

            - ``AUTOMATIC`` (default): DataSync and the SMB file server negotiate the highest version of SMB that they mutually support between 2.1 and 3.1.1.

            This is the recommended option. If you instead choose a specific version that your file server doesn't support, you may get an ``Operation Not Supported`` error.

            - ``SMB3`` : Restricts the protocol negotiation to only SMB version 3.0.2.
            - ``SMB2`` : Restricts the protocol negotiation to only SMB version 2.1.
            - ``SMB2_0`` : Restricts the protocol negotiation to only SMB version 2.0.
            - ``SMB1`` : Restricts the protocol negotiation to only SMB version 1.0.

            .. epigraph::

               The ``SMB1`` option isn't available when `creating an Amazon FSx for NetApp ONTAP location <https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smbmountoptions.html#cfn-datasync-locationfsxontap-smbmountoptions-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SmbMountOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxONTAPProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_arns": "securityGroupArns",
        "storage_virtual_machine_arn": "storageVirtualMachineArn",
        "protocol": "protocol",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationFSxONTAPProps:
    def __init__(
        self,
        *,
        security_group_arns: typing.Sequence[builtins.str],
        storage_virtual_machine_arn: builtins.str,
        protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxONTAP.ProtocolProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationFSxONTAP``.

        :param security_group_arns: Specifies the Amazon Resource Names (ARNs) of the security groups that DataSync can use to access your FSx for ONTAP file system. You must configure the security groups to allow outbound traffic on the following ports (depending on the protocol that you're using): - *Network File System (NFS)* : TCP ports 111, 635, and 2049 - *Server Message Block (SMB)* : TCP port 445 Your file system's security groups must also allow inbound traffic on the same port.
        :param storage_virtual_machine_arn: Specifies the ARN of the storage virtual machine (SVM) in your file system where you want to copy data to or from.
        :param protocol: Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.
        :param subdirectory: Specifies a path to the file share in the SVM where you'll copy your data. You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be ``/vol1`` , ``/vol1/tree1`` , or ``/share1`` . .. epigraph:: Don't specify a junction path in the SVM's root volume. For more information, see `Managing FSx for ONTAP storage virtual machines <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html>`_ in the *Amazon FSx for NetApp ONTAP User Guide* .
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_fSx_oNTAPProps = datasync.CfnLocationFSxONTAPProps(
                security_group_arns=["securityGroupArns"],
                storage_virtual_machine_arn="storageVirtualMachineArn",
            
                # the properties below are optional
                protocol=datasync.CfnLocationFSxONTAP.ProtocolProperty(
                    nfs=datasync.CfnLocationFSxONTAP.NFSProperty(
                        mount_options=datasync.CfnLocationFSxONTAP.NfsMountOptionsProperty(
                            version="version"
                        )
                    ),
                    smb=datasync.CfnLocationFSxONTAP.SMBProperty(
                        mount_options=datasync.CfnLocationFSxONTAP.SmbMountOptionsProperty(
                            version="version"
                        ),
                        password="password",
                        user="user",
            
                        # the properties below are optional
                        domain="domain"
                    )
                ),
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80ce3cf4001e297ef6c59ffcd2e700197ec14104852b7d6b75aac1725cb45d8b)
            check_type(argname="argument security_group_arns", value=security_group_arns, expected_type=type_hints["security_group_arns"])
            check_type(argname="argument storage_virtual_machine_arn", value=storage_virtual_machine_arn, expected_type=type_hints["storage_virtual_machine_arn"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_arns": security_group_arns,
            "storage_virtual_machine_arn": storage_virtual_machine_arn,
        }
        if protocol is not None:
            self._values["protocol"] = protocol
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''Specifies the Amazon Resource Names (ARNs) of the security groups that DataSync can use to access your FSx for ONTAP file system.

        You must configure the security groups to allow outbound traffic on the following ports (depending on the protocol that you're using):

        - *Network File System (NFS)* : TCP ports 111, 635, and 2049
        - *Server Message Block (SMB)* : TCP port 445

        Your file system's security groups must also allow inbound traffic on the same port.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-securitygrouparns
        '''
        result = self._values.get("security_group_arns")
        assert result is not None, "Required property 'security_group_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def storage_virtual_machine_arn(self) -> builtins.str:
        '''Specifies the ARN of the storage virtual machine (SVM) in your file system where you want to copy data to or from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-storagevirtualmachinearn
        '''
        result = self._values.get("storage_virtual_machine_arn")
        assert result is not None, "Required property 'storage_virtual_machine_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationFSxONTAP.ProtocolProperty]]:
        '''Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationFSxONTAP.ProtocolProperty]], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies a path to the file share in the SVM where you'll copy your data.

        You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be ``/vol1`` , ``/vol1/tree1`` , or ``/share1`` .
        .. epigraph::

           Don't specify a junction path in the SVM's root volume. For more information, see `Managing FSx for ONTAP storage virtual machines <https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html>`_ in the *Amazon FSx for NetApp ONTAP User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.

        We recommend creating at least a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationFSxONTAPProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationFSxOpenZFS(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxOpenZFS",
):
    '''The ``AWS::DataSync::LocationFSxOpenZFS`` resource specifies an endpoint for an Amazon FSx for OpenZFS file system.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html
    :cloudformationResource: AWS::DataSync::LocationFSxOpenZFS
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_fSx_open_zFS = datasync.CfnLocationFSxOpenZFS(self, "MyCfnLocationFSxOpenZFS",
            protocol=datasync.CfnLocationFSxOpenZFS.ProtocolProperty(
                nfs=datasync.CfnLocationFSxOpenZFS.NFSProperty(
                    mount_options=datasync.CfnLocationFSxOpenZFS.MountOptionsProperty(
                        version="version"
                    )
                )
            ),
            security_group_arns=["securityGroupArns"],
        
            # the properties below are optional
            fsx_filesystem_arn="fsxFilesystemArn",
            subdirectory="subdirectory",
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
        protocol: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationFSxOpenZFS.ProtocolProperty", typing.Dict[builtins.str, typing.Any]]],
        security_group_arns: typing.Sequence[builtins.str],
        fsx_filesystem_arn: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param protocol: The type of protocol that AWS DataSync uses to access your file system.
        :param security_group_arns: The ARNs of the security groups that are used to configure the FSx for OpenZFS file system. *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$`` *Length constraints* : Maximum length of 128.
        :param fsx_filesystem_arn: The Amazon Resource Name (ARN) of the FSx for OpenZFS file system.
        :param subdirectory: A subdirectory in the location's path that must begin with ``/fsx`` . DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).
        :param tags: The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ad8c513f918bb8d8381bbd62e5e1a111d39af1c2ed6ba47a729880d177982e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationFSxOpenZFSProps(
            protocol=protocol,
            security_group_arns=security_group_arns,
            fsx_filesystem_arn=fsx_filesystem_arn,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1607aef74d95939cb07d1755f55358e0d063c7dc0bb1c91110bc825233382e02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__618ba438d447571bd06af749cb3c483e174a8bf053f1381c5214c86336394ca7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The ARN of the specified FSx for OpenZFS file system location.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the specified FSx for OpenZFS file system location.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="protocol")
    def protocol(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLocationFSxOpenZFS.ProtocolProperty"]:
        '''The type of protocol that AWS DataSync uses to access your file system.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLocationFSxOpenZFS.ProtocolProperty"], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLocationFSxOpenZFS.ProtocolProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddafc49b43359e47266c55b1856065646a5a0a4d1fee7e74184b46d0a9ea1323)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupArns")
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of the security groups that are used to configure the FSx for OpenZFS file system.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupArns"))

    @security_group_arns.setter
    def security_group_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1541ed866ade55559c6d5705d3e2c71e861be18522927a112e488f0495a437ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupArns", value)

    @builtins.property
    @jsii.member(jsii_name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the FSx for OpenZFS file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsxFilesystemArn"))

    @fsx_filesystem_arn.setter
    def fsx_filesystem_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed3bb479112a50476f67687992c13945d7c7956773f0372592cc754ca002e2be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsxFilesystemArn", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''A subdirectory in the location's path that must begin with ``/fsx`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dad170792efea1b233597f89fd5ab9cb0ae92aa33fc727fac7ab53c7c07c2dc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The key-value pair that represents a tag that you want to add to the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c49d460645d98663ac93a723deb6ca797169b9d9ede4cada79adec615c02492)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxOpenZFS.MountOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"version": "version"},
    )
    class MountOptionsProperty:
        def __init__(self, *, version: typing.Optional[builtins.str] = None) -> None:
            '''Represents the mount options that are available for DataSync to access a Network File System (NFS) location.

            :param version: The specific NFS version that you want DataSync to use to mount your NFS share. If the server refuses to use the version specified, the sync will fail. If you don't specify a version, DataSync defaults to ``AUTOMATIC`` . That is, DataSync automatically selects a version based on negotiation with the NFS server. You can specify the following NFS versions: - *`NFSv3 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc1813>`_* : Stateless protocol version that allows for asynchronous writes on the server. - *`NFSv4.0 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3530>`_* : Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems. - *`NFSv4.1 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5661>`_* : Stateful protocol version that supports sessions, directory delegations, and parallel data processing. Version 4.1 also includes all features available in version 4.0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-mountoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                mount_options_property = datasync.CfnLocationFSxOpenZFS.MountOptionsProperty(
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cfda36e06bba17b0bffc6c6a8c3817aa3805236389cc12c4dbffb61442f143c8)
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The specific NFS version that you want DataSync to use to mount your NFS share.

            If the server refuses to use the version specified, the sync will fail. If you don't specify a version, DataSync defaults to ``AUTOMATIC`` . That is, DataSync automatically selects a version based on negotiation with the NFS server.

            You can specify the following NFS versions:

            - *`NFSv3 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc1813>`_* : Stateless protocol version that allows for asynchronous writes on the server.
            - *`NFSv4.0 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3530>`_* : Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems.
            - *`NFSv4.1 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5661>`_* : Stateful protocol version that supports sessions, directory delegations, and parallel data processing. Version 4.1 also includes all features available in version 4.0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-mountoptions.html#cfn-datasync-locationfsxopenzfs-mountoptions-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MountOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxOpenZFS.NFSProperty",
        jsii_struct_bases=[],
        name_mapping={"mount_options": "mountOptions"},
    )
    class NFSProperty:
        def __init__(
            self,
            *,
            mount_options: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationFSxOpenZFS.MountOptionsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Represents the Network File System (NFS) protocol that AWS DataSync uses to access your Amazon FSx for OpenZFS file system.

            :param mount_options: Represents the mount options that are available for DataSync to access an NFS location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-nfs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                n_fSProperty = datasync.CfnLocationFSxOpenZFS.NFSProperty(
                    mount_options=datasync.CfnLocationFSxOpenZFS.MountOptionsProperty(
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b2291a1530562b2a7a2c025ec9cd5ab602cc0bc08d1a9d2d8804639aec6a8489)
                check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mount_options": mount_options,
            }

        @builtins.property
        def mount_options(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnLocationFSxOpenZFS.MountOptionsProperty"]:
            '''Represents the mount options that are available for DataSync to access an NFS location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-nfs.html#cfn-datasync-locationfsxopenzfs-nfs-mountoptions
            '''
            result = self._values.get("mount_options")
            assert result is not None, "Required property 'mount_options' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLocationFSxOpenZFS.MountOptionsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NFSProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxOpenZFS.ProtocolProperty",
        jsii_struct_bases=[],
        name_mapping={"nfs": "nfs"},
    )
    class ProtocolProperty:
        def __init__(
            self,
            *,
            nfs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationFSxOpenZFS.NFSProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Represents the protocol that AWS DataSync uses to access your Amazon FSx for OpenZFS file system.

            :param nfs: Represents the Network File System (NFS) protocol that DataSync uses to access your FSx for OpenZFS file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-protocol.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                protocol_property = datasync.CfnLocationFSxOpenZFS.ProtocolProperty(
                    nfs=datasync.CfnLocationFSxOpenZFS.NFSProperty(
                        mount_options=datasync.CfnLocationFSxOpenZFS.MountOptionsProperty(
                            version="version"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f41739d7c107eef7d64b8f86d076d7f20e79f98ab22fca2329e2030a8081468)
                check_type(argname="argument nfs", value=nfs, expected_type=type_hints["nfs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if nfs is not None:
                self._values["nfs"] = nfs

        @builtins.property
        def nfs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxOpenZFS.NFSProperty"]]:
            '''Represents the Network File System (NFS) protocol that DataSync uses to access your FSx for OpenZFS file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-protocol.html#cfn-datasync-locationfsxopenzfs-protocol-nfs
            '''
            result = self._values.get("nfs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationFSxOpenZFS.NFSProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProtocolProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxOpenZFSProps",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "security_group_arns": "securityGroupArns",
        "fsx_filesystem_arn": "fsxFilesystemArn",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationFSxOpenZFSProps:
    def __init__(
        self,
        *,
        protocol: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxOpenZFS.ProtocolProperty, typing.Dict[builtins.str, typing.Any]]],
        security_group_arns: typing.Sequence[builtins.str],
        fsx_filesystem_arn: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationFSxOpenZFS``.

        :param protocol: The type of protocol that AWS DataSync uses to access your file system.
        :param security_group_arns: The ARNs of the security groups that are used to configure the FSx for OpenZFS file system. *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$`` *Length constraints* : Maximum length of 128.
        :param fsx_filesystem_arn: The Amazon Resource Name (ARN) of the FSx for OpenZFS file system.
        :param subdirectory: A subdirectory in the location's path that must begin with ``/fsx`` . DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).
        :param tags: The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_fSx_open_zFSProps = datasync.CfnLocationFSxOpenZFSProps(
                protocol=datasync.CfnLocationFSxOpenZFS.ProtocolProperty(
                    nfs=datasync.CfnLocationFSxOpenZFS.NFSProperty(
                        mount_options=datasync.CfnLocationFSxOpenZFS.MountOptionsProperty(
                            version="version"
                        )
                    )
                ),
                security_group_arns=["securityGroupArns"],
            
                # the properties below are optional
                fsx_filesystem_arn="fsxFilesystemArn",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16adeb69f25af324c507b1a5b1905509ca406e488b6f1f503c1037668ea1c423)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument security_group_arns", value=security_group_arns, expected_type=type_hints["security_group_arns"])
            check_type(argname="argument fsx_filesystem_arn", value=fsx_filesystem_arn, expected_type=type_hints["fsx_filesystem_arn"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
            "security_group_arns": security_group_arns,
        }
        if fsx_filesystem_arn is not None:
            self._values["fsx_filesystem_arn"] = fsx_filesystem_arn
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def protocol(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLocationFSxOpenZFS.ProtocolProperty]:
        '''The type of protocol that AWS DataSync uses to access your file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLocationFSxOpenZFS.ProtocolProperty], result)

    @builtins.property
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of the security groups that are used to configure the FSx for OpenZFS file system.

        *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$``

        *Length constraints* : Maximum length of 128.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-securitygrouparns
        '''
        result = self._values.get("security_group_arns")
        assert result is not None, "Required property 'security_group_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def fsx_filesystem_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the FSx for OpenZFS file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-fsxfilesystemarn
        '''
        result = self._values.get("fsx_filesystem_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''A subdirectory in the location's path that must begin with ``/fsx`` .

        DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The key-value pair that represents a tag that you want to add to the resource.

        The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationFSxOpenZFSProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationFSxWindows(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxWindows",
):
    '''The ``AWS::DataSync::LocationFSxWindows`` resource specifies an endpoint for an Amazon FSx for Windows Server file system.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html
    :cloudformationResource: AWS::DataSync::LocationFSxWindows
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_fSx_windows = datasync.CfnLocationFSxWindows(self, "MyCfnLocationFSxWindows",
            security_group_arns=["securityGroupArns"],
            user="user",
        
            # the properties below are optional
            domain="domain",
            fsx_filesystem_arn="fsxFilesystemArn",
            password="password",
            subdirectory="subdirectory",
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
        security_group_arns: typing.Sequence[builtins.str],
        user: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        fsx_filesystem_arn: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_group_arns: The Amazon Resource Names (ARNs) of the security groups that are used to configure the FSx for Windows File Server file system. *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$`` *Length constraints* : Maximum length of 128.
        :param user: The user who has the permissions to access files and folders in the FSx for Windows File Server file system. For information about choosing a user name that ensures sufficient permissions to files, folders, and metadata, see `user <https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#FSxWuser>`_ .
        :param domain: Specifies the name of the Microsoft Active Directory domain that the FSx for Windows File Server file system belongs to. If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.
        :param fsx_filesystem_arn: Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file system.
        :param password: Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.
        :param subdirectory: Specifies a mount path for your file system using forward slashes. This is where DataSync reads or writes data (depending on if this is a source or destination location).
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c93d65e558fb10f2d82a30ed92129805bd6595247629ad020c0793d238ab28)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationFSxWindowsProps(
            security_group_arns=security_group_arns,
            user=user,
            domain=domain,
            fsx_filesystem_arn=fsx_filesystem_arn,
            password=password,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543b917e94b9026d545236925ac70a71da95a62071411ad3a7a83379d3ce0dcd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a8e8a3ae5b78a07a65a6d98cd11d85b2bc6ea1356e1b5cb4ffa7d4da482b187)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The ARN of the specified FSx for Windows Server file system location.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the specified FSx for Windows Server file system location.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="securityGroupArns")
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARNs) of the security groups that are used to configure the FSx for Windows File Server file system.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupArns"))

    @security_group_arns.setter
    def security_group_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__627d2025f40a7ab53f282cdc8322a1d894fdfaa9a3bd70d74612c70ade3e0325)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupArns", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        '''The user who has the permissions to access files and folders in the FSx for Windows File Server file system.'''
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d45f9d99683ac8fb9741da3800803485aee87f8917d4e8dc41b244517870b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the Microsoft Active Directory domain that the FSx for Windows File Server file system belongs to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__356f65660a522cc7efd2dbff7f12ba4d654cc19ff311a66ebb391fc6f659ef92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsxFilesystemArn"))

    @fsx_filesystem_arn.setter
    def fsx_filesystem_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cfc208b531344d673280b57ea62e26f43f7ae28704e223829300459ed7a5ae5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsxFilesystemArn", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebf29df57a68b0e86263f1ac5ee2f8f2c771094dfd4377bb7e540e3af1f598c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies a mount path for your file system using forward slashes.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a35bda492feb7951b7758508a280efaf76334f6397db60c3c1225de0566b628)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__602782cd2d11ed3007adaab1a6e7826b15d7a1236d0d2fa763c3a9b1471eda1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationFSxWindowsProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_arns": "securityGroupArns",
        "user": "user",
        "domain": "domain",
        "fsx_filesystem_arn": "fsxFilesystemArn",
        "password": "password",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationFSxWindowsProps:
    def __init__(
        self,
        *,
        security_group_arns: typing.Sequence[builtins.str],
        user: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        fsx_filesystem_arn: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationFSxWindows``.

        :param security_group_arns: The Amazon Resource Names (ARNs) of the security groups that are used to configure the FSx for Windows File Server file system. *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$`` *Length constraints* : Maximum length of 128.
        :param user: The user who has the permissions to access files and folders in the FSx for Windows File Server file system. For information about choosing a user name that ensures sufficient permissions to files, folders, and metadata, see `user <https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#FSxWuser>`_ .
        :param domain: Specifies the name of the Microsoft Active Directory domain that the FSx for Windows File Server file system belongs to. If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.
        :param fsx_filesystem_arn: Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file system.
        :param password: Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.
        :param subdirectory: Specifies a mount path for your file system using forward slashes. This is where DataSync reads or writes data (depending on if this is a source or destination location).
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_fSx_windows_props = datasync.CfnLocationFSxWindowsProps(
                security_group_arns=["securityGroupArns"],
                user="user",
            
                # the properties below are optional
                domain="domain",
                fsx_filesystem_arn="fsxFilesystemArn",
                password="password",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f5ba282a9548e2767c09028be2186cfa923b38c45c6c77db774a616f6106dfd)
            check_type(argname="argument security_group_arns", value=security_group_arns, expected_type=type_hints["security_group_arns"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument fsx_filesystem_arn", value=fsx_filesystem_arn, expected_type=type_hints["fsx_filesystem_arn"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_arns": security_group_arns,
            "user": user,
        }
        if domain is not None:
            self._values["domain"] = domain
        if fsx_filesystem_arn is not None:
            self._values["fsx_filesystem_arn"] = fsx_filesystem_arn
        if password is not None:
            self._values["password"] = password
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARNs) of the security groups that are used to configure the FSx for Windows File Server file system.

        *Pattern* : ``^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$``

        *Length constraints* : Maximum length of 128.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-securitygrouparns
        '''
        result = self._values.get("security_group_arns")
        assert result is not None, "Required property 'security_group_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def user(self) -> builtins.str:
        '''The user who has the permissions to access files and folders in the FSx for Windows File Server file system.

        For information about choosing a user name that ensures sufficient permissions to files, folders, and metadata, see `user <https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#FSxWuser>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-user
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the Microsoft Active Directory domain that the FSx for Windows File Server file system belongs to.

        If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fsx_filesystem_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-fsxfilesystemarn
        '''
        result = self._values.get("fsx_filesystem_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies a mount path for your file system using forward slashes.

        This is where DataSync reads or writes data (depending on if this is a source or destination location).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.

        We recommend creating at least a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationFSxWindowsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationHDFS(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationHDFS",
):
    '''The ``AWS::DataSync::LocationHDFS`` resource specifies an endpoint for a Hadoop Distributed File System (HDFS).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html
    :cloudformationResource: AWS::DataSync::LocationHDFS
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_hDFS = datasync.CfnLocationHDFS(self, "MyCfnLocationHDFS",
            agent_arns=["agentArns"],
            authentication_type="authenticationType",
            name_nodes=[datasync.CfnLocationHDFS.NameNodeProperty(
                hostname="hostname",
                port=123
            )],
        
            # the properties below are optional
            block_size=123,
            kerberos_keytab="kerberosKeytab",
            kerberos_krb5_conf="kerberosKrb5Conf",
            kerberos_principal="kerberosPrincipal",
            kms_key_provider_uri="kmsKeyProviderUri",
            qop_configuration=datasync.CfnLocationHDFS.QopConfigurationProperty(
                data_transfer_protection="dataTransferProtection",
                rpc_protection="rpcProtection"
            ),
            replication_factor=123,
            simple_user="simpleUser",
            subdirectory="subdirectory",
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
        agent_arns: typing.Sequence[builtins.str],
        authentication_type: builtins.str,
        name_nodes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationHDFS.NameNodeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        block_size: typing.Optional[jsii.Number] = None,
        kerberos_keytab: typing.Optional[builtins.str] = None,
        kerberos_krb5_conf: typing.Optional[builtins.str] = None,
        kerberos_principal: typing.Optional[builtins.str] = None,
        kms_key_provider_uri: typing.Optional[builtins.str] = None,
        qop_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationHDFS.QopConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        replication_factor: typing.Optional[jsii.Number] = None,
        simple_user: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_arns: The Amazon Resource Names (ARNs) of the agents that are used to connect to the HDFS cluster.
        :param authentication_type: The authentication mode used to determine identity of user.
        :param name_nodes: The NameNode that manages the HDFS namespace. The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes. You can use only one NameNode.
        :param block_size: The size of data blocks to write into the HDFS cluster. The block size must be a multiple of 512 bytes. The default block size is 128 mebibytes (MiB).
        :param kerberos_keytab: The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys. Provide the base64-encoded file text. If ``KERBEROS`` is specified for ``AuthType`` , this value is required.
        :param kerberos_krb5_conf: The ``krb5.conf`` file that contains the Kerberos configuration information. You can load the ``krb5.conf`` by providing a string of the file's contents or an Amazon S3 presigned URL of the file. If ``KERBEROS`` is specified for ``AuthType`` , this value is required.
        :param kerberos_principal: The Kerberos principal with access to the files and folders on the HDFS cluster. .. epigraph:: If ``KERBEROS`` is specified for ``AuthenticationType`` , this parameter is required.
        :param kms_key_provider_uri: The URI of the HDFS cluster's Key Management Server (KMS).
        :param qop_configuration: The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster. If ``QopConfiguration`` isn't specified, ``RpcProtection`` and ``DataTransferProtection`` default to ``PRIVACY`` . If you set ``RpcProtection`` or ``DataTransferProtection`` , the other parameter assumes the same value.
        :param replication_factor: The number of DataNodes to replicate the data to when writing to the HDFS cluster. By default, data is replicated to three DataNodes. Default: - 3
        :param simple_user: The user name used to identify the client on the host operating system. .. epigraph:: If ``SIMPLE`` is specified for ``AuthenticationType`` , this parameter is required.
        :param subdirectory: A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write data to the HDFS cluster. If the subdirectory isn't specified, it will default to ``/`` .
        :param tags: The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4e6e207e87512241da6969739eafac75aaa4606f7d5a869a5c3730ac474aba5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationHDFSProps(
            agent_arns=agent_arns,
            authentication_type=authentication_type,
            name_nodes=name_nodes,
            block_size=block_size,
            kerberos_keytab=kerberos_keytab,
            kerberos_krb5_conf=kerberos_krb5_conf,
            kerberos_principal=kerberos_principal,
            kms_key_provider_uri=kms_key_provider_uri,
            qop_configuration=qop_configuration,
            replication_factor=replication_factor,
            simple_user=simple_user,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16ad8322840db3a52346c879eb9f99bb34e8c97d2b5db9416f434c897bb3f3c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a475327a7ef18072ddcee0391d79181ad96efb93aad6484cf5ecd4adb8a5acea)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the HDFS cluster location to describe.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the HDFS cluster location.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARNs) of the agents that are used to connect to the HDFS cluster.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__589134abb411230e5151d5dbdc2d3f57049d54aa4991a0e31b28febbed363542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentArns", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        '''The authentication mode used to determine identity of user.'''
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1212707812d568c33e201782b49fb54b24478da5aafb6b468e2de0fce2aa31bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="nameNodes")
    def name_nodes(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLocationHDFS.NameNodeProperty"]]]:
        '''The NameNode that manages the HDFS namespace.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLocationHDFS.NameNodeProperty"]]], jsii.get(self, "nameNodes"))

    @name_nodes.setter
    def name_nodes(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLocationHDFS.NameNodeProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a76145fef05ad13cf6d623dec2e81ad7c19c154ecd30d8aae3a73e81c6576491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameNodes", value)

    @builtins.property
    @jsii.member(jsii_name="blockSize")
    def block_size(self) -> typing.Optional[jsii.Number]:
        '''The size of data blocks to write into the HDFS cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockSize"))

    @block_size.setter
    def block_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf27e0cd386bf2173a19ecd724060c7f84d674c6012a12d7d80434a642f7669)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockSize", value)

    @builtins.property
    @jsii.member(jsii_name="kerberosKeytab")
    def kerberos_keytab(self) -> typing.Optional[builtins.str]:
        '''The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kerberosKeytab"))

    @kerberos_keytab.setter
    def kerberos_keytab(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6057391a851d073ac6f1367fe8fd1c48123fb8ce205d25a7b62dab5b2526403)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kerberosKeytab", value)

    @builtins.property
    @jsii.member(jsii_name="kerberosKrb5Conf")
    def kerberos_krb5_conf(self) -> typing.Optional[builtins.str]:
        '''The ``krb5.conf`` file that contains the Kerberos configuration information. You can load the ``krb5.conf`` by providing a string of the file's contents or an Amazon S3 presigned URL of the file. If ``KERBEROS`` is specified for ``AuthType`` , this value is required.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kerberosKrb5Conf"))

    @kerberos_krb5_conf.setter
    def kerberos_krb5_conf(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27c3b0c34aebfd29ee44b9714b36c3784836c4bafab215880054ced544ffceb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kerberosKrb5Conf", value)

    @builtins.property
    @jsii.member(jsii_name="kerberosPrincipal")
    def kerberos_principal(self) -> typing.Optional[builtins.str]:
        '''The Kerberos principal with access to the files and folders on the HDFS cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kerberosPrincipal"))

    @kerberos_principal.setter
    def kerberos_principal(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb3b88f77d23303189ba83b98eb4ba536946b54369bfcbde6934d23750d702d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kerberosPrincipal", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyProviderUri")
    def kms_key_provider_uri(self) -> typing.Optional[builtins.str]:
        '''The URI of the HDFS cluster's Key Management Server (KMS).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyProviderUri"))

    @kms_key_provider_uri.setter
    def kms_key_provider_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b391dcf3cbfdc1b073c64fdd7b6cf479a7438a0decfd4019ee6bed21145ed395)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyProviderUri", value)

    @builtins.property
    @jsii.member(jsii_name="qopConfiguration")
    def qop_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationHDFS.QopConfigurationProperty"]]:
        '''The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationHDFS.QopConfigurationProperty"]], jsii.get(self, "qopConfiguration"))

    @qop_configuration.setter
    def qop_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationHDFS.QopConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eada24423cf34a46defb2fb08ff49d30f58ea6d6486c0e6ccf15fc65da913ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qopConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="replicationFactor")
    def replication_factor(self) -> typing.Optional[jsii.Number]:
        '''The number of DataNodes to replicate the data to when writing to the HDFS cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicationFactor"))

    @replication_factor.setter
    def replication_factor(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3ee4cc2c6ca661c5acfc5a8bd53136b2b61234dbf0df2632f2355ceb274c2df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationFactor", value)

    @builtins.property
    @jsii.member(jsii_name="simpleUser")
    def simple_user(self) -> typing.Optional[builtins.str]:
        '''The user name used to identify the client on the host operating system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "simpleUser"))

    @simple_user.setter
    def simple_user(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cacb880eb4be9b59946ed860edadb54c1921088c8a1676c2966339de1ad488d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "simpleUser", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''A subdirectory in the HDFS cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00f88a655a03c9f1a9a7cf557e70ba70d9c5e3ea34a07249c483f3de0111a360)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The key-value pair that represents the tag that you want to add to the location.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aae452f9b71c01ce6062b4ea9224245a9cc1780c588d392319b30c53a0bc99d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationHDFS.NameNodeProperty",
        jsii_struct_bases=[],
        name_mapping={"hostname": "hostname", "port": "port"},
    )
    class NameNodeProperty:
        def __init__(self, *, hostname: builtins.str, port: jsii.Number) -> None:
            '''The NameNode of the Hadoop Distributed File System (HDFS).

            The NameNode manages the file system's namespace and performs operations such as opening, closing, and renaming files and directories. The NameNode also contains the information to map blocks of data to the DataNodes.

            :param hostname: The hostname of the NameNode in the HDFS cluster. This value is the IP address or Domain Name Service (DNS) name of the NameNode. An agent that's installed on-premises uses this hostname to communicate with the NameNode in the network.
            :param port: The port that the NameNode uses to listen to client requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                name_node_property = datasync.CfnLocationHDFS.NameNodeProperty(
                    hostname="hostname",
                    port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff067b203598a07a938143f104acc0c36107b9a8f09480a3d654c038b1737385)
                check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hostname": hostname,
                "port": port,
            }

        @builtins.property
        def hostname(self) -> builtins.str:
            '''The hostname of the NameNode in the HDFS cluster.

            This value is the IP address or Domain Name Service (DNS) name of the NameNode. An agent that's installed on-premises uses this hostname to communicate with the NameNode in the network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html#cfn-datasync-locationhdfs-namenode-hostname
            '''
            result = self._values.get("hostname")
            assert result is not None, "Required property 'hostname' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The port that the NameNode uses to listen to client requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html#cfn-datasync-locationhdfs-namenode-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NameNodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationHDFS.QopConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_transfer_protection": "dataTransferProtection",
            "rpc_protection": "rpcProtection",
        },
    )
    class QopConfigurationProperty:
        def __init__(
            self,
            *,
            data_transfer_protection: typing.Optional[builtins.str] = None,
            rpc_protection: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer privacy settings configured on the Hadoop Distributed File System (HDFS) cluster.

            :param data_transfer_protection: The data transfer protection setting configured on the HDFS cluster. This setting corresponds to your ``dfs.data.transfer.protection`` setting in the ``hdfs-site.xml`` file on your Hadoop cluster. Default: - "PRIVACY"
            :param rpc_protection: The Remote Procedure Call (RPC) protection setting configured on the HDFS cluster. This setting corresponds to your ``hadoop.rpc.protection`` setting in your ``core-site.xml`` file on your Hadoop cluster. Default: - "PRIVACY"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                qop_configuration_property = datasync.CfnLocationHDFS.QopConfigurationProperty(
                    data_transfer_protection="dataTransferProtection",
                    rpc_protection="rpcProtection"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf9687c3478faca4ca6f46765e18256315fbf00b11876af5dad6a28a53a6ef4b)
                check_type(argname="argument data_transfer_protection", value=data_transfer_protection, expected_type=type_hints["data_transfer_protection"])
                check_type(argname="argument rpc_protection", value=rpc_protection, expected_type=type_hints["rpc_protection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_transfer_protection is not None:
                self._values["data_transfer_protection"] = data_transfer_protection
            if rpc_protection is not None:
                self._values["rpc_protection"] = rpc_protection

        @builtins.property
        def data_transfer_protection(self) -> typing.Optional[builtins.str]:
            '''The data transfer protection setting configured on the HDFS cluster.

            This setting corresponds to your ``dfs.data.transfer.protection`` setting in the ``hdfs-site.xml`` file on your Hadoop cluster.

            :default: - "PRIVACY"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html#cfn-datasync-locationhdfs-qopconfiguration-datatransferprotection
            '''
            result = self._values.get("data_transfer_protection")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rpc_protection(self) -> typing.Optional[builtins.str]:
            '''The Remote Procedure Call (RPC) protection setting configured on the HDFS cluster.

            This setting corresponds to your ``hadoop.rpc.protection`` setting in your ``core-site.xml`` file on your Hadoop cluster.

            :default: - "PRIVACY"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html#cfn-datasync-locationhdfs-qopconfiguration-rpcprotection
            '''
            result = self._values.get("rpc_protection")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QopConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationHDFSProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_arns": "agentArns",
        "authentication_type": "authenticationType",
        "name_nodes": "nameNodes",
        "block_size": "blockSize",
        "kerberos_keytab": "kerberosKeytab",
        "kerberos_krb5_conf": "kerberosKrb5Conf",
        "kerberos_principal": "kerberosPrincipal",
        "kms_key_provider_uri": "kmsKeyProviderUri",
        "qop_configuration": "qopConfiguration",
        "replication_factor": "replicationFactor",
        "simple_user": "simpleUser",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationHDFSProps:
    def __init__(
        self,
        *,
        agent_arns: typing.Sequence[builtins.str],
        authentication_type: builtins.str,
        name_nodes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationHDFS.NameNodeProperty, typing.Dict[builtins.str, typing.Any]]]]],
        block_size: typing.Optional[jsii.Number] = None,
        kerberos_keytab: typing.Optional[builtins.str] = None,
        kerberos_krb5_conf: typing.Optional[builtins.str] = None,
        kerberos_principal: typing.Optional[builtins.str] = None,
        kms_key_provider_uri: typing.Optional[builtins.str] = None,
        qop_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationHDFS.QopConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        replication_factor: typing.Optional[jsii.Number] = None,
        simple_user: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationHDFS``.

        :param agent_arns: The Amazon Resource Names (ARNs) of the agents that are used to connect to the HDFS cluster.
        :param authentication_type: The authentication mode used to determine identity of user.
        :param name_nodes: The NameNode that manages the HDFS namespace. The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes. You can use only one NameNode.
        :param block_size: The size of data blocks to write into the HDFS cluster. The block size must be a multiple of 512 bytes. The default block size is 128 mebibytes (MiB).
        :param kerberos_keytab: The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys. Provide the base64-encoded file text. If ``KERBEROS`` is specified for ``AuthType`` , this value is required.
        :param kerberos_krb5_conf: The ``krb5.conf`` file that contains the Kerberos configuration information. You can load the ``krb5.conf`` by providing a string of the file's contents or an Amazon S3 presigned URL of the file. If ``KERBEROS`` is specified for ``AuthType`` , this value is required.
        :param kerberos_principal: The Kerberos principal with access to the files and folders on the HDFS cluster. .. epigraph:: If ``KERBEROS`` is specified for ``AuthenticationType`` , this parameter is required.
        :param kms_key_provider_uri: The URI of the HDFS cluster's Key Management Server (KMS).
        :param qop_configuration: The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster. If ``QopConfiguration`` isn't specified, ``RpcProtection`` and ``DataTransferProtection`` default to ``PRIVACY`` . If you set ``RpcProtection`` or ``DataTransferProtection`` , the other parameter assumes the same value.
        :param replication_factor: The number of DataNodes to replicate the data to when writing to the HDFS cluster. By default, data is replicated to three DataNodes. Default: - 3
        :param simple_user: The user name used to identify the client on the host operating system. .. epigraph:: If ``SIMPLE`` is specified for ``AuthenticationType`` , this parameter is required.
        :param subdirectory: A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write data to the HDFS cluster. If the subdirectory isn't specified, it will default to ``/`` .
        :param tags: The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_hDFSProps = datasync.CfnLocationHDFSProps(
                agent_arns=["agentArns"],
                authentication_type="authenticationType",
                name_nodes=[datasync.CfnLocationHDFS.NameNodeProperty(
                    hostname="hostname",
                    port=123
                )],
            
                # the properties below are optional
                block_size=123,
                kerberos_keytab="kerberosKeytab",
                kerberos_krb5_conf="kerberosKrb5Conf",
                kerberos_principal="kerberosPrincipal",
                kms_key_provider_uri="kmsKeyProviderUri",
                qop_configuration=datasync.CfnLocationHDFS.QopConfigurationProperty(
                    data_transfer_protection="dataTransferProtection",
                    rpc_protection="rpcProtection"
                ),
                replication_factor=123,
                simple_user="simpleUser",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acd7db2bc2dffe624daa5332f50443b11a0c0e3a43b2ecd71e380ba6c4e4385c)
            check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument name_nodes", value=name_nodes, expected_type=type_hints["name_nodes"])
            check_type(argname="argument block_size", value=block_size, expected_type=type_hints["block_size"])
            check_type(argname="argument kerberos_keytab", value=kerberos_keytab, expected_type=type_hints["kerberos_keytab"])
            check_type(argname="argument kerberos_krb5_conf", value=kerberos_krb5_conf, expected_type=type_hints["kerberos_krb5_conf"])
            check_type(argname="argument kerberos_principal", value=kerberos_principal, expected_type=type_hints["kerberos_principal"])
            check_type(argname="argument kms_key_provider_uri", value=kms_key_provider_uri, expected_type=type_hints["kms_key_provider_uri"])
            check_type(argname="argument qop_configuration", value=qop_configuration, expected_type=type_hints["qop_configuration"])
            check_type(argname="argument replication_factor", value=replication_factor, expected_type=type_hints["replication_factor"])
            check_type(argname="argument simple_user", value=simple_user, expected_type=type_hints["simple_user"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arns": agent_arns,
            "authentication_type": authentication_type,
            "name_nodes": name_nodes,
        }
        if block_size is not None:
            self._values["block_size"] = block_size
        if kerberos_keytab is not None:
            self._values["kerberos_keytab"] = kerberos_keytab
        if kerberos_krb5_conf is not None:
            self._values["kerberos_krb5_conf"] = kerberos_krb5_conf
        if kerberos_principal is not None:
            self._values["kerberos_principal"] = kerberos_principal
        if kms_key_provider_uri is not None:
            self._values["kms_key_provider_uri"] = kms_key_provider_uri
        if qop_configuration is not None:
            self._values["qop_configuration"] = qop_configuration
        if replication_factor is not None:
            self._values["replication_factor"] = replication_factor
        if simple_user is not None:
            self._values["simple_user"] = simple_user
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARNs) of the agents that are used to connect to the HDFS cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-agentarns
        '''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''The authentication mode used to determine identity of user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-authenticationtype
        '''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name_nodes(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLocationHDFS.NameNodeProperty]]]:
        '''The NameNode that manages the HDFS namespace.

        The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes. You can use only one NameNode.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-namenodes
        '''
        result = self._values.get("name_nodes")
        assert result is not None, "Required property 'name_nodes' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLocationHDFS.NameNodeProperty]]], result)

    @builtins.property
    def block_size(self) -> typing.Optional[jsii.Number]:
        '''The size of data blocks to write into the HDFS cluster.

        The block size must be a multiple of 512 bytes. The default block size is 128 mebibytes (MiB).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-blocksize
        '''
        result = self._values.get("block_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kerberos_keytab(self) -> typing.Optional[builtins.str]:
        '''The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys.

        Provide the base64-encoded file text. If ``KERBEROS`` is specified for ``AuthType`` , this value is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-kerberoskeytab
        '''
        result = self._values.get("kerberos_keytab")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kerberos_krb5_conf(self) -> typing.Optional[builtins.str]:
        '''The ``krb5.conf`` file that contains the Kerberos configuration information. You can load the ``krb5.conf`` by providing a string of the file's contents or an Amazon S3 presigned URL of the file. If ``KERBEROS`` is specified for ``AuthType`` , this value is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-kerberoskrb5conf
        '''
        result = self._values.get("kerberos_krb5_conf")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kerberos_principal(self) -> typing.Optional[builtins.str]:
        '''The Kerberos principal with access to the files and folders on the HDFS cluster.

        .. epigraph::

           If ``KERBEROS`` is specified for ``AuthenticationType`` , this parameter is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-kerberosprincipal
        '''
        result = self._values.get("kerberos_principal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_provider_uri(self) -> typing.Optional[builtins.str]:
        '''The URI of the HDFS cluster's Key Management Server (KMS).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-kmskeyprovideruri
        '''
        result = self._values.get("kms_key_provider_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def qop_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationHDFS.QopConfigurationProperty]]:
        '''The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster.

        If ``QopConfiguration`` isn't specified, ``RpcProtection`` and ``DataTransferProtection`` default to ``PRIVACY`` . If you set ``RpcProtection`` or ``DataTransferProtection`` , the other parameter assumes the same value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-qopconfiguration
        '''
        result = self._values.get("qop_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationHDFS.QopConfigurationProperty]], result)

    @builtins.property
    def replication_factor(self) -> typing.Optional[jsii.Number]:
        '''The number of DataNodes to replicate the data to when writing to the HDFS cluster.

        By default, data is replicated to three DataNodes.

        :default: - 3

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-replicationfactor
        '''
        result = self._values.get("replication_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def simple_user(self) -> typing.Optional[builtins.str]:
        '''The user name used to identify the client on the host operating system.

        .. epigraph::

           If ``SIMPLE`` is specified for ``AuthenticationType`` , this parameter is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-simpleuser
        '''
        result = self._values.get("simple_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''A subdirectory in the HDFS cluster.

        This subdirectory is used to read data from or write data to the HDFS cluster. If the subdirectory isn't specified, it will default to ``/`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The key-value pair that represents the tag that you want to add to the location.

        The value can be an empty string. We recommend using tags to name your resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationHDFSProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationNFS(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationNFS",
):
    '''The ``AWS::DataSync::LocationNFS`` resource specifies a Network File System (NFS) file server that AWS DataSync can use as a transfer source or destination.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html
    :cloudformationResource: AWS::DataSync::LocationNFS
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_nFS = datasync.CfnLocationNFS(self, "MyCfnLocationNFS",
            on_prem_config=datasync.CfnLocationNFS.OnPremConfigProperty(
                agent_arns=["agentArns"]
            ),
        
            # the properties below are optional
            mount_options=datasync.CfnLocationNFS.MountOptionsProperty(
                version="version"
            ),
            server_hostname="serverHostname",
            subdirectory="subdirectory",
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
        on_prem_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationNFS.OnPremConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        mount_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationNFS.MountOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        server_hostname: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param on_prem_config: Specifies the Amazon Resource Name (ARN) of the DataSync agent that want to connect to your NFS file server. You can specify more than one agent. For more information, see `Using multiple agents for transfers <https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html>`_ .
        :param mount_options: Specifies the options that DataSync can use to mount your NFS file server.
        :param server_hostname: Specifies the Domain Name System (DNS) name or IP version 4 address of the NFS file server that your DataSync agent connects to.
        :param subdirectory: Specifies the export path in your NFS file server that you want DataSync to mount. This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see `Accessing NFS file servers <https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs>`_ .
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d069ca05c42fb87f307cca12e7ca62685374e8479c3259d679c41b7c9e2b1aef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationNFSProps(
            on_prem_config=on_prem_config,
            mount_options=mount_options,
            server_hostname=server_hostname,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40df789cb6a010f01823fe85f7288bf1ac70fb78042afb433c6d7133870bda33)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c316588e44bcf94ddca8831976b72238cd17eb18a3c521d497fc44d71155f2aa)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the NFS location that you created.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the NFS location that you created.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="onPremConfig")
    def on_prem_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLocationNFS.OnPremConfigProperty"]:
        '''Specifies the Amazon Resource Name (ARN) of the DataSync agent that want to connect to your NFS file server.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLocationNFS.OnPremConfigProperty"], jsii.get(self, "onPremConfig"))

    @on_prem_config.setter
    def on_prem_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLocationNFS.OnPremConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef5244b8ff59527535d3ba0996f08c461f6affc766845b00ae3805171907b04c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onPremConfig", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationNFS.MountOptionsProperty"]]:
        '''Specifies the options that DataSync can use to mount your NFS file server.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationNFS.MountOptionsProperty"]], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationNFS.MountOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f53e27778ea596fd0d4e8ad60113269d0f0aac45137d89e2a99be7a5c30e4fb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="serverHostname")
    def server_hostname(self) -> typing.Optional[builtins.str]:
        '''Specifies the Domain Name System (DNS) name or IP version 4 address of the NFS file server that your DataSync agent connects to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverHostname"))

    @server_hostname.setter
    def server_hostname(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db78699845c639e22a20c2990d72ef74b39b3dfd71d7723e31c7fb2f10aafea0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverHostname", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies the export path in your NFS file server that you want DataSync to mount.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f230ca1995ad30becaf0c71d285ca8bab104210d7223f477c8537757ea6e972b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6775dcca43d86f1ff2a8795efb1205f09fdcee773716c549b06acac462432bcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationNFS.MountOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"version": "version"},
    )
    class MountOptionsProperty:
        def __init__(self, *, version: typing.Optional[builtins.str] = None) -> None:
            '''Specifies the options that DataSync can use to mount your NFS file server.

            :param version: Specifies the NFS version that you want DataSync to use when mounting your NFS share. If the server refuses to use the version specified, the task fails. You can specify the following options: - ``AUTOMATIC`` (default): DataSync chooses NFS version 4.1. - ``NFS3`` : Stateless protocol version that allows for asynchronous writes on the server. - ``NFSv4_0`` : Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems. - ``NFSv4_1`` : Stateful protocol version that supports sessions, directory delegations, and parallel data processing. NFS version 4.1 also includes all features available in version 4.0. .. epigraph:: DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                mount_options_property = datasync.CfnLocationNFS.MountOptionsProperty(
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e2486d89e028a5b89b8598f356d7e2a5a050dc22284ebbeb5c3c0a76d928758)
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''Specifies the NFS version that you want DataSync to use when mounting your NFS share.

            If the server refuses to use the version specified, the task fails.

            You can specify the following options:

            - ``AUTOMATIC`` (default): DataSync chooses NFS version 4.1.
            - ``NFS3`` : Stateless protocol version that allows for asynchronous writes on the server.
            - ``NFSv4_0`` : Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems.
            - ``NFSv4_1`` : Stateful protocol version that supports sessions, directory delegations, and parallel data processing. NFS version 4.1 also includes all features available in version 4.0.

            .. epigraph::

               DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html#cfn-datasync-locationnfs-mountoptions-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MountOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationNFS.OnPremConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"agent_arns": "agentArns"},
    )
    class OnPremConfigProperty:
        def __init__(self, *, agent_arns: typing.Sequence[builtins.str]) -> None:
            '''The AWS DataSync agents that are connecting to a Network File System (NFS) location.

            :param agent_arns: The Amazon Resource Names (ARNs) of the agents connecting to a transfer location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                on_prem_config_property = datasync.CfnLocationNFS.OnPremConfigProperty(
                    agent_arns=["agentArns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf52296f64754ae5def817f69206eb64641343e40369d74f7a3de14644073deb)
                check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "agent_arns": agent_arns,
            }

        @builtins.property
        def agent_arns(self) -> typing.List[builtins.str]:
            '''The Amazon Resource Names (ARNs) of the agents connecting to a transfer location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html#cfn-datasync-locationnfs-onpremconfig-agentarns
            '''
            result = self._values.get("agent_arns")
            assert result is not None, "Required property 'agent_arns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnPremConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationNFSProps",
    jsii_struct_bases=[],
    name_mapping={
        "on_prem_config": "onPremConfig",
        "mount_options": "mountOptions",
        "server_hostname": "serverHostname",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationNFSProps:
    def __init__(
        self,
        *,
        on_prem_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationNFS.OnPremConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        mount_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationNFS.MountOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        server_hostname: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationNFS``.

        :param on_prem_config: Specifies the Amazon Resource Name (ARN) of the DataSync agent that want to connect to your NFS file server. You can specify more than one agent. For more information, see `Using multiple agents for transfers <https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html>`_ .
        :param mount_options: Specifies the options that DataSync can use to mount your NFS file server.
        :param server_hostname: Specifies the Domain Name System (DNS) name or IP version 4 address of the NFS file server that your DataSync agent connects to.
        :param subdirectory: Specifies the export path in your NFS file server that you want DataSync to mount. This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see `Accessing NFS file servers <https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs>`_ .
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_nFSProps = datasync.CfnLocationNFSProps(
                on_prem_config=datasync.CfnLocationNFS.OnPremConfigProperty(
                    agent_arns=["agentArns"]
                ),
            
                # the properties below are optional
                mount_options=datasync.CfnLocationNFS.MountOptionsProperty(
                    version="version"
                ),
                server_hostname="serverHostname",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f51fa3c0c693bb5826cc200004a0b1f04c19f70726432f02d5a4443185b49b1)
            check_type(argname="argument on_prem_config", value=on_prem_config, expected_type=type_hints["on_prem_config"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument server_hostname", value=server_hostname, expected_type=type_hints["server_hostname"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "on_prem_config": on_prem_config,
        }
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if server_hostname is not None:
            self._values["server_hostname"] = server_hostname
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def on_prem_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLocationNFS.OnPremConfigProperty]:
        '''Specifies the Amazon Resource Name (ARN) of the DataSync agent that want to connect to your NFS file server.

        You can specify more than one agent. For more information, see `Using multiple agents for transfers <https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-onpremconfig
        '''
        result = self._values.get("on_prem_config")
        assert result is not None, "Required property 'on_prem_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLocationNFS.OnPremConfigProperty], result)

    @builtins.property
    def mount_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationNFS.MountOptionsProperty]]:
        '''Specifies the options that DataSync can use to mount your NFS file server.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-mountoptions
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationNFS.MountOptionsProperty]], result)

    @builtins.property
    def server_hostname(self) -> typing.Optional[builtins.str]:
        '''Specifies the Domain Name System (DNS) name or IP version 4 address of the NFS file server that your DataSync agent connects to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-serverhostname
        '''
        result = self._values.get("server_hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies the export path in your NFS file server that you want DataSync to mount.

        This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see `Accessing NFS file servers <https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.

        We recommend creating at least a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationNFSProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationObjectStorage(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationObjectStorage",
):
    '''The ``AWS::DataSync::LocationObjectStorage`` resource specifies an endpoint for a self-managed object storage bucket.

    For more information about self-managed object storage locations, see `Creating a Location for Object Storage <https://docs.aws.amazon.com/datasync/latest/userguide/create-object-location.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html
    :cloudformationResource: AWS::DataSync::LocationObjectStorage
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_object_storage = datasync.CfnLocationObjectStorage(self, "MyCfnLocationObjectStorage",
            agent_arns=["agentArns"],
        
            # the properties below are optional
            access_key="accessKey",
            bucket_name="bucketName",
            secret_key="secretKey",
            server_certificate="serverCertificate",
            server_hostname="serverHostname",
            server_port=123,
            server_protocol="serverProtocol",
            subdirectory="subdirectory",
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
        agent_arns: typing.Sequence[builtins.str],
        access_key: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        server_certificate: typing.Optional[builtins.str] = None,
        server_hostname: typing.Optional[builtins.str] = None,
        server_port: typing.Optional[jsii.Number] = None,
        server_protocol: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_arns: Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can securely connect with your location.
        :param access_key: Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.
        :param bucket_name: Specifies the name of the object storage bucket involved in the transfer.
        :param secret_key: Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.
        :param server_certificate: Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA). You must specify a single ``.pem`` file with a full certificate chain (for example, ``file:///home/user/.ssh/object_storage_certificates.pem`` ). The certificate chain might include: - The object storage system's certificate - All intermediate certificates (if there are any) - The root certificate of the signing CA You can concatenate your certificates into a ``.pem`` file (which can be up to 32768 bytes before base64 encoding). The following example ``cat`` command creates an ``object_storage_certificates.pem`` file that includes three certificates: ``cat object_server_certificate.pem intermediate_certificate.pem ca_root_certificate.pem > object_storage_certificates.pem`` To use this parameter, configure ``ServerProtocol`` to ``HTTPS`` .
        :param server_hostname: Specifies the domain name or IP address of the object storage server. A DataSync agent uses this hostname to mount the object storage server in a network.
        :param server_port: Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).
        :param server_protocol: Specifies the protocol that your object storage server uses to communicate.
        :param subdirectory: Specifies the object prefix for your object storage server. If this is a source location, DataSync only copies objects with this prefix. If this is a destination location, DataSync writes all objects with this prefix.
        :param tags: Specifies the key-value pair that represents a tag that you want to add to the resource. Tags can help you manage, filter, and search for your resources. We recommend creating a name tag for your location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6afc4365b2246b057f5b97e5d62cc10a54cff3be74dae8a9bb184f54bec37125)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationObjectStorageProps(
            agent_arns=agent_arns,
            access_key=access_key,
            bucket_name=bucket_name,
            secret_key=secret_key,
            server_certificate=server_certificate,
            server_hostname=server_hostname,
            server_port=server_port,
            server_protocol=server_protocol,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61e61baf3961601d7838c5023c80bbf458fad24f9dd8cf4006490f1eccb76e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1891041f95311e30edfb4c440a05c41fa9ad1fb130ed42400500c57858f12085)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified object storage location.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the specified object storage location.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        '''Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can securely connect with your location.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af42e226779e989fe6f4a4e7403f44c0a7f4048f3185f2bd0fdbbe0f191363ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentArns", value)

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> typing.Optional[builtins.str]:
        '''Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bab62678e3c33f0a6edfb878fe17304321977ba3655bb45d3504aa54de9dadc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the object storage bucket involved in the transfer.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf6330b6613abe7771487991e7b16db5686e2242ecdbb63f4ef7e946766b4ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cdc4af71140887c9702de30a25cd730dad08983bb31931dbba45c838b77c638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="serverCertificate")
    def server_certificate(self) -> typing.Optional[builtins.str]:
        '''Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverCertificate"))

    @server_certificate.setter
    def server_certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe1a19b9b619faa0e6cc523990a61cf54a53b8ce9dee6069266a8bba0751c3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="serverHostname")
    def server_hostname(self) -> typing.Optional[builtins.str]:
        '''Specifies the domain name or IP address of the object storage server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverHostname"))

    @server_hostname.setter
    def server_hostname(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa6bb2a89a6471b8beee100b564375c694c575449e9d04bc9ede967e993738b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverHostname", value)

    @builtins.property
    @jsii.member(jsii_name="serverPort")
    def server_port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serverPort"))

    @server_port.setter
    def server_port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26f25c8e19d015decf49fc7f700522b335ae1d335eb9ab2a8043361791c53294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverPort", value)

    @builtins.property
    @jsii.member(jsii_name="serverProtocol")
    def server_protocol(self) -> typing.Optional[builtins.str]:
        '''Specifies the protocol that your object storage server uses to communicate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverProtocol"))

    @server_protocol.setter
    def server_protocol(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d86ff038021519c6b78d57b7c787246ca9822b5a3abe776e0b1a8086f5b1c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies the object prefix for your object storage server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3632c6248d8275b49a1adcc3708b5bb2fe80efcf6c9244f62d25487bffc9a210)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the key-value pair that represents a tag that you want to add to the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c7a3d48757bffde04fd1015e50d6672207d2522eec04091eebdb3ac177fb39a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationObjectStorageProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_arns": "agentArns",
        "access_key": "accessKey",
        "bucket_name": "bucketName",
        "secret_key": "secretKey",
        "server_certificate": "serverCertificate",
        "server_hostname": "serverHostname",
        "server_port": "serverPort",
        "server_protocol": "serverProtocol",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationObjectStorageProps:
    def __init__(
        self,
        *,
        agent_arns: typing.Sequence[builtins.str],
        access_key: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        server_certificate: typing.Optional[builtins.str] = None,
        server_hostname: typing.Optional[builtins.str] = None,
        server_port: typing.Optional[jsii.Number] = None,
        server_protocol: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationObjectStorage``.

        :param agent_arns: Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can securely connect with your location.
        :param access_key: Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.
        :param bucket_name: Specifies the name of the object storage bucket involved in the transfer.
        :param secret_key: Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.
        :param server_certificate: Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA). You must specify a single ``.pem`` file with a full certificate chain (for example, ``file:///home/user/.ssh/object_storage_certificates.pem`` ). The certificate chain might include: - The object storage system's certificate - All intermediate certificates (if there are any) - The root certificate of the signing CA You can concatenate your certificates into a ``.pem`` file (which can be up to 32768 bytes before base64 encoding). The following example ``cat`` command creates an ``object_storage_certificates.pem`` file that includes three certificates: ``cat object_server_certificate.pem intermediate_certificate.pem ca_root_certificate.pem > object_storage_certificates.pem`` To use this parameter, configure ``ServerProtocol`` to ``HTTPS`` .
        :param server_hostname: Specifies the domain name or IP address of the object storage server. A DataSync agent uses this hostname to mount the object storage server in a network.
        :param server_port: Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).
        :param server_protocol: Specifies the protocol that your object storage server uses to communicate.
        :param subdirectory: Specifies the object prefix for your object storage server. If this is a source location, DataSync only copies objects with this prefix. If this is a destination location, DataSync writes all objects with this prefix.
        :param tags: Specifies the key-value pair that represents a tag that you want to add to the resource. Tags can help you manage, filter, and search for your resources. We recommend creating a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_object_storage_props = datasync.CfnLocationObjectStorageProps(
                agent_arns=["agentArns"],
            
                # the properties below are optional
                access_key="accessKey",
                bucket_name="bucketName",
                secret_key="secretKey",
                server_certificate="serverCertificate",
                server_hostname="serverHostname",
                server_port=123,
                server_protocol="serverProtocol",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d542a26da4e93d9d103e234c98ed367d8b6bea7d295017a32de5525e1ec22b45)
            check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument server_certificate", value=server_certificate, expected_type=type_hints["server_certificate"])
            check_type(argname="argument server_hostname", value=server_hostname, expected_type=type_hints["server_hostname"])
            check_type(argname="argument server_port", value=server_port, expected_type=type_hints["server_port"])
            check_type(argname="argument server_protocol", value=server_protocol, expected_type=type_hints["server_protocol"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arns": agent_arns,
        }
        if access_key is not None:
            self._values["access_key"] = access_key
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if server_certificate is not None:
            self._values["server_certificate"] = server_certificate
        if server_hostname is not None:
            self._values["server_hostname"] = server_hostname
        if server_port is not None:
            self._values["server_port"] = server_port
        if server_protocol is not None:
            self._values["server_protocol"] = server_protocol
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_arns(self) -> typing.List[builtins.str]:
        '''Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can securely connect with your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-agentarns
        '''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-accesskey
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the object storage bucket involved in the transfer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-bucketname
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-secretkey
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_certificate(self) -> typing.Optional[builtins.str]:
        '''Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA).

        You must specify a single ``.pem`` file with a full certificate chain (for example, ``file:///home/user/.ssh/object_storage_certificates.pem`` ).

        The certificate chain might include:

        - The object storage system's certificate
        - All intermediate certificates (if there are any)
        - The root certificate of the signing CA

        You can concatenate your certificates into a ``.pem`` file (which can be up to 32768 bytes before base64 encoding). The following example ``cat`` command creates an ``object_storage_certificates.pem`` file that includes three certificates:

        ``cat object_server_certificate.pem intermediate_certificate.pem ca_root_certificate.pem > object_storage_certificates.pem``

        To use this parameter, configure ``ServerProtocol`` to ``HTTPS`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-servercertificate
        '''
        result = self._values.get("server_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_hostname(self) -> typing.Optional[builtins.str]:
        '''Specifies the domain name or IP address of the object storage server.

        A DataSync agent uses this hostname to mount the object storage server in a network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverhostname
        '''
        result = self._values.get("server_hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverport
        '''
        result = self._values.get("server_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_protocol(self) -> typing.Optional[builtins.str]:
        '''Specifies the protocol that your object storage server uses to communicate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverprotocol
        '''
        result = self._values.get("server_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies the object prefix for your object storage server.

        If this is a source location, DataSync only copies objects with this prefix. If this is a destination location, DataSync writes all objects with this prefix.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the key-value pair that represents a tag that you want to add to the resource.

        Tags can help you manage, filter, and search for your resources. We recommend creating a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationObjectStorageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationS3(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationS3",
):
    '''The ``AWS::DataSync::LocationS3`` resource specifies an endpoint for an Amazon S3 bucket.

    For more information, see `Create an Amazon S3 location <https://docs.aws.amazon.com/datasync/latest/userguide/create-locations-cli.html#create-location-s3-cli>`_ in the *AWS DataSync User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html
    :cloudformationResource: AWS::DataSync::LocationS3
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_s3 = datasync.CfnLocationS3(self, "MyCfnLocationS3",
            s3_config=datasync.CfnLocationS3.S3ConfigProperty(
                bucket_access_role_arn="bucketAccessRoleArn"
            ),
        
            # the properties below are optional
            s3_bucket_arn="s3BucketArn",
            s3_storage_class="s3StorageClass",
            subdirectory="subdirectory",
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
        s3_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationS3.S3ConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        s3_bucket_arn: typing.Optional[builtins.str] = None,
        s3_storage_class: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param s3_config: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket. For detailed information about using such a role, see `Creating a Location for Amazon S3 <https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html#create-s3-location>`_ in the *AWS DataSync User Guide* .
        :param s3_bucket_arn: The ARN of the Amazon S3 bucket.
        :param s3_storage_class: The Amazon S3 storage class that you want to store your files in when this location is used as a task destination. For buckets in AWS Regions , the storage class defaults to S3 Standard. For more information about S3 storage classes, see `Amazon S3 Storage Classes <https://docs.aws.amazon.com/s3/storage-classes/>`_ . Some storage classes have behaviors that can affect your S3 storage costs. For detailed information, see `Considerations When Working with Amazon S3 Storage Classes in DataSync <https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes>`_ . Default: - "STANDARD"
        :param subdirectory: Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location). .. epigraph:: DataSync can't transfer objects with a prefix that begins with a slash ( ``/`` ) or includes ``//`` , ``/./`` , or ``/../`` patterns. For example: - ``/photos`` - ``photos//2006/January`` - ``photos/./2006/February`` - ``photos/../2006/March``
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your transfer location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffb78212d43943a47f3d3a5e10125952e22d4754b8512843cf88c7c55f6514ee)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationS3Props(
            s3_config=s3_config,
            s3_bucket_arn=s3_bucket_arn,
            s3_storage_class=s3_storage_class,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a187d5155efd29d831744d9f56a48eb5fb642e6480113807dc45702657631e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__54c7d3981be7393042939c70bae0b4fb0e4420f2649a9d523d80810c5b47361e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified Amazon S3 location.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the specified Amazon S3 location.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="s3Config")
    def s3_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLocationS3.S3ConfigProperty"]:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLocationS3.S3ConfigProperty"], jsii.get(self, "s3Config"))

    @s3_config.setter
    def s3_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLocationS3.S3ConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97a8e39b836dbbdb49d0bd113962d59b27158d2ab86e97500f5dda21fc6f2d70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Config", value)

    @builtins.property
    @jsii.member(jsii_name="s3BucketArn")
    def s3_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketArn"))

    @s3_bucket_arn.setter
    def s3_bucket_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49ff9004432edb3637a4fd05fa9fd3158f9d7b6094ac54156943f7d6dd1d5047)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3StorageClass")
    def s3_storage_class(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 storage class that you want to store your files in when this location is used as a task destination.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3StorageClass"))

    @s3_storage_class.setter
    def s3_storage_class(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82a7d8ab492fdfb044b0e230d97fa1965715c74f4b35ab0403115732834d1e49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3StorageClass", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2ceccded2a2b37bcf132c0f563dba3e5c80cc42a7c55df19724af65ac2d8a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d6b2dd8b444ebab79ed4aae8987dfed0864cb4e3663bdfd36a643d72264608e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationS3.S3ConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_access_role_arn": "bucketAccessRoleArn"},
    )
    class S3ConfigProperty:
        def __init__(self, *, bucket_access_role_arn: builtins.str) -> None:
            '''Specifies the Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that DataSync uses to access your S3 bucket.

            For more information, see `Accessing S3 buckets <https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-access>`_ .

            :param bucket_access_role_arn: Specifies the ARN of the IAM role that DataSync uses to access your S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                s3_config_property = datasync.CfnLocationS3.S3ConfigProperty(
                    bucket_access_role_arn="bucketAccessRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce8f8003886002426ef5ce44b74ed398416c8d59b6cf5b10816d2ddc11294b14)
                check_type(argname="argument bucket_access_role_arn", value=bucket_access_role_arn, expected_type=type_hints["bucket_access_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_access_role_arn": bucket_access_role_arn,
            }

        @builtins.property
        def bucket_access_role_arn(self) -> builtins.str:
            '''Specifies the ARN of the IAM role that DataSync uses to access your S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html#cfn-datasync-locations3-s3config-bucketaccessrolearn
            '''
            result = self._values.get("bucket_access_role_arn")
            assert result is not None, "Required property 'bucket_access_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationS3Props",
    jsii_struct_bases=[],
    name_mapping={
        "s3_config": "s3Config",
        "s3_bucket_arn": "s3BucketArn",
        "s3_storage_class": "s3StorageClass",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationS3Props:
    def __init__(
        self,
        *,
        s3_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationS3.S3ConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        s3_bucket_arn: typing.Optional[builtins.str] = None,
        s3_storage_class: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationS3``.

        :param s3_config: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket. For detailed information about using such a role, see `Creating a Location for Amazon S3 <https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html#create-s3-location>`_ in the *AWS DataSync User Guide* .
        :param s3_bucket_arn: The ARN of the Amazon S3 bucket.
        :param s3_storage_class: The Amazon S3 storage class that you want to store your files in when this location is used as a task destination. For buckets in AWS Regions , the storage class defaults to S3 Standard. For more information about S3 storage classes, see `Amazon S3 Storage Classes <https://docs.aws.amazon.com/s3/storage-classes/>`_ . Some storage classes have behaviors that can affect your S3 storage costs. For detailed information, see `Considerations When Working with Amazon S3 Storage Classes in DataSync <https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes>`_ . Default: - "STANDARD"
        :param subdirectory: Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location). .. epigraph:: DataSync can't transfer objects with a prefix that begins with a slash ( ``/`` ) or includes ``//`` , ``/./`` , or ``/../`` patterns. For example: - ``/photos`` - ``photos//2006/January`` - ``photos/./2006/February`` - ``photos/../2006/March``
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your transfer location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_s3_props = datasync.CfnLocationS3Props(
                s3_config=datasync.CfnLocationS3.S3ConfigProperty(
                    bucket_access_role_arn="bucketAccessRoleArn"
                ),
            
                # the properties below are optional
                s3_bucket_arn="s3BucketArn",
                s3_storage_class="s3StorageClass",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1b9799e0fad9e71975d14e754aeb8ef0b5f52fcedcbabc328afae8c4a4afaa5)
            check_type(argname="argument s3_config", value=s3_config, expected_type=type_hints["s3_config"])
            check_type(argname="argument s3_bucket_arn", value=s3_bucket_arn, expected_type=type_hints["s3_bucket_arn"])
            check_type(argname="argument s3_storage_class", value=s3_storage_class, expected_type=type_hints["s3_storage_class"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_config": s3_config,
        }
        if s3_bucket_arn is not None:
            self._values["s3_bucket_arn"] = s3_bucket_arn
        if s3_storage_class is not None:
            self._values["s3_storage_class"] = s3_storage_class
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def s3_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLocationS3.S3ConfigProperty]:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket.

        For detailed information about using such a role, see `Creating a Location for Amazon S3 <https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html#create-s3-location>`_ in the *AWS DataSync User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config
        '''
        result = self._values.get("s3_config")
        assert result is not None, "Required property 's3_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLocationS3.S3ConfigProperty], result)

    @builtins.property
    def s3_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the Amazon S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn
        '''
        result = self._values.get("s3_bucket_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_storage_class(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 storage class that you want to store your files in when this location is used as a task destination.

        For buckets in AWS Regions , the storage class defaults to S3 Standard.

        For more information about S3 storage classes, see `Amazon S3 Storage Classes <https://docs.aws.amazon.com/s3/storage-classes/>`_ . Some storage classes have behaviors that can affect your S3 storage costs. For detailed information, see `Considerations When Working with Amazon S3 Storage Classes in DataSync <https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes>`_ .

        :default: - "STANDARD"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass
        '''
        result = self._values.get("s3_storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location).

        .. epigraph::

           DataSync can't transfer objects with a prefix that begins with a slash ( ``/`` ) or includes ``//`` , ``/./`` , or ``/../`` patterns. For example:

           - ``/photos``
           - ``photos//2006/January``
           - ``photos/./2006/February``
           - ``photos/../2006/March``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.

        We recommend creating at least a name tag for your transfer location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationS3Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocationSMB(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationSMB",
):
    '''The ``AWS::DataSync::LocationSMB`` resource specifies a Server Message Block (SMB) location.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html
    :cloudformationResource: AWS::DataSync::LocationSMB
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_location_sMB = datasync.CfnLocationSMB(self, "MyCfnLocationSMB",
            agent_arns=["agentArns"],
            user="user",
        
            # the properties below are optional
            domain="domain",
            mount_options=datasync.CfnLocationSMB.MountOptionsProperty(
                version="version"
            ),
            password="password",
            server_hostname="serverHostname",
            subdirectory="subdirectory",
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
        agent_arns: typing.Sequence[builtins.str],
        user: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLocationSMB.MountOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        password: typing.Optional[builtins.str] = None,
        server_hostname: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_arns: The Amazon Resource Names (ARNs) of agents to use for a Server Message Block (SMB) location.
        :param user: The user who can mount the share and has the permissions to access files and folders in the SMB share. For information about choosing a user name that ensures sufficient permissions to files, folders, and metadata, see `user <https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#SMBuser>`_ .
        :param domain: Specifies the name of the Active Directory domain that your SMB file server belongs to. If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.
        :param mount_options: Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.
        :param password: The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.
        :param server_hostname: Specifies the Domain Name Service (DNS) name or IP address of the SMB file server that your DataSync agent will mount. .. epigraph:: You can't specify an IP version 6 (IPv6) address.
        :param subdirectory: The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination. The SMB path should be a path that's exported by the SMB server, or a subdirectory of that path. The path should be such that it can be mounted by other SMB clients in your network. .. epigraph:: ``Subdirectory`` must be specified with forward slashes. For example, ``/path/to/folder`` . To transfer all the data in the folder you specified, DataSync must have permissions to mount the SMB share, as well as to access all the data in that share. To ensure this, either make sure that the user name and password specified belongs to the user who can mount the share, and who has the appropriate permissions for all of the files and directories that you want DataSync to access, or use credentials of a member of the Backup Operators group to mount the share. Doing either one enables the agent to access the data. For the agent to access directories, you must additionally enable all execute access.
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bafa6101408857d4661895c88a8c9839da8768aa52e07d3f2889a4f27c1cab7d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationSMBProps(
            agent_arns=agent_arns,
            user=user,
            domain=domain,
            mount_options=mount_options,
            password=password,
            server_hostname=server_hostname,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88508f3486fa9166f7847b61eef5d9a046ed0dae7d7da9e27f6f83d1f0019490)
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
            type_hints = typing.get_type_hints(_typecheckingstub__976a351d3a1231a7633ae322e4c36b99634cc2da556bf4d8eea9837c359833bb)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified SMB file system.

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''The URI of the specified SMB location.

        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

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
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARNs) of agents to use for a Server Message Block (SMB) location.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21ee66e7697fa761c39fe555b5fae211e45dedf33951d3701b7b6389dd8452b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentArns", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        '''The user who can mount the share and has the permissions to access files and folders in the SMB share.'''
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9112e8b177e52fbd055f221015988972f906f8c7291b4a1992bb1656cd033faa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the Active Directory domain that your SMB file server belongs to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__645408d26d2b2afb233a71045cf02aab2ca6bb9a00176ca0b16d93e1e633bf92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationSMB.MountOptionsProperty"]]:
        '''Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationSMB.MountOptionsProperty"]], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLocationSMB.MountOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9983585f73509aeb431e7337689500eb00129c754b73a4ef4022bebcd1bbc1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__188ea071908278e310db901e923a61e61176a5283d6d637c7cf24940f4af9a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="serverHostname")
    def server_hostname(self) -> typing.Optional[builtins.str]:
        '''Specifies the Domain Name Service (DNS) name or IP address of the SMB file server that your DataSync agent will mount.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverHostname"))

    @server_hostname.setter
    def server_hostname(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91814040ef607edb46eb6b7f17c10d591505c88dcd81419dd0065a7c2520ec99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverHostname", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b24807ca878b348d6926b1d8578692f8c738074f4ba29ed17cb920e40bb4a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b48314ac3635761aa21132da0f199200c2b741ddeca4e34176ee47fde9d19e47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnLocationSMB.MountOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"version": "version"},
    )
    class MountOptionsProperty:
        def __init__(self, *, version: typing.Optional[builtins.str] = None) -> None:
            '''Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.

            :param version: By default, DataSync automatically chooses an SMB protocol version based on negotiation with your SMB file server. You also can configure DataSync to use a specific SMB version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically. These are the following options for configuring the SMB version: - ``AUTOMATIC`` (default): DataSync and the SMB file server negotiate the highest version of SMB that they mutually support between 2.1 and 3.1.1. This is the recommended option. If you instead choose a specific version that your file server doesn't support, you may get an ``Operation Not Supported`` error. - ``SMB3`` : Restricts the protocol negotiation to only SMB version 3.0.2. - ``SMB2`` : Restricts the protocol negotiation to only SMB version 2.1. - ``SMB2_0`` : Restricts the protocol negotiation to only SMB version 2.0. - ``SMB1`` : Restricts the protocol negotiation to only SMB version 1.0. .. epigraph:: The ``SMB1`` option isn't available when `creating an Amazon FSx for NetApp ONTAP location <https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                mount_options_property = datasync.CfnLocationSMB.MountOptionsProperty(
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__465428a8e33c33a3926562e4b4d3d671db7fc7f2d1ff95443e6224cb280e8c00)
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''By default, DataSync automatically chooses an SMB protocol version based on negotiation with your SMB file server.

            You also can configure DataSync to use a specific SMB version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically.

            These are the following options for configuring the SMB version:

            - ``AUTOMATIC`` (default): DataSync and the SMB file server negotiate the highest version of SMB that they mutually support between 2.1 and 3.1.1.

            This is the recommended option. If you instead choose a specific version that your file server doesn't support, you may get an ``Operation Not Supported`` error.

            - ``SMB3`` : Restricts the protocol negotiation to only SMB version 3.0.2.
            - ``SMB2`` : Restricts the protocol negotiation to only SMB version 2.1.
            - ``SMB2_0`` : Restricts the protocol negotiation to only SMB version 2.0.
            - ``SMB1`` : Restricts the protocol negotiation to only SMB version 1.0.

            .. epigraph::

               The ``SMB1`` option isn't available when `creating an Amazon FSx for NetApp ONTAP location <https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html#cfn-datasync-locationsmb-mountoptions-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MountOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnLocationSMBProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_arns": "agentArns",
        "user": "user",
        "domain": "domain",
        "mount_options": "mountOptions",
        "password": "password",
        "server_hostname": "serverHostname",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationSMBProps:
    def __init__(
        self,
        *,
        agent_arns: typing.Sequence[builtins.str],
        user: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationSMB.MountOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        password: typing.Optional[builtins.str] = None,
        server_hostname: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocationSMB``.

        :param agent_arns: The Amazon Resource Names (ARNs) of agents to use for a Server Message Block (SMB) location.
        :param user: The user who can mount the share and has the permissions to access files and folders in the SMB share. For information about choosing a user name that ensures sufficient permissions to files, folders, and metadata, see `user <https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#SMBuser>`_ .
        :param domain: Specifies the name of the Active Directory domain that your SMB file server belongs to. If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.
        :param mount_options: Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.
        :param password: The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.
        :param server_hostname: Specifies the Domain Name Service (DNS) name or IP address of the SMB file server that your DataSync agent will mount. .. epigraph:: You can't specify an IP version 6 (IPv6) address.
        :param subdirectory: The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination. The SMB path should be a path that's exported by the SMB server, or a subdirectory of that path. The path should be such that it can be mounted by other SMB clients in your network. .. epigraph:: ``Subdirectory`` must be specified with forward slashes. For example, ``/path/to/folder`` . To transfer all the data in the folder you specified, DataSync must have permissions to mount the SMB share, as well as to access all the data in that share. To ensure this, either make sure that the user name and password specified belongs to the user who can mount the share, and who has the appropriate permissions for all of the files and directories that you want DataSync to access, or use credentials of a member of the Backup Operators group to mount the share. Doing either one enables the agent to access the data. For the agent to access directories, you must additionally enable all execute access.
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_location_sMBProps = datasync.CfnLocationSMBProps(
                agent_arns=["agentArns"],
                user="user",
            
                # the properties below are optional
                domain="domain",
                mount_options=datasync.CfnLocationSMB.MountOptionsProperty(
                    version="version"
                ),
                password="password",
                server_hostname="serverHostname",
                subdirectory="subdirectory",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20670d7cb18baa1155ccc397df310282442d51b95170ab568e5c0a9cbea5bc8)
            check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument server_hostname", value=server_hostname, expected_type=type_hints["server_hostname"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arns": agent_arns,
            "user": user,
        }
        if domain is not None:
            self._values["domain"] = domain
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if password is not None:
            self._values["password"] = password
        if server_hostname is not None:
            self._values["server_hostname"] = server_hostname
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARNs) of agents to use for a Server Message Block (SMB) location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-agentarns
        '''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def user(self) -> builtins.str:
        '''The user who can mount the share and has the permissions to access files and folders in the SMB share.

        For information about choosing a user name that ensures sufficient permissions to files, folders, and metadata, see `user <https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#SMBuser>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-user
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the Active Directory domain that your SMB file server belongs to.

        If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationSMB.MountOptionsProperty]]:
        '''Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-mountoptions
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationSMB.MountOptionsProperty]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_hostname(self) -> typing.Optional[builtins.str]:
        '''Specifies the Domain Name Service (DNS) name or IP address of the SMB file server that your DataSync agent will mount.

        .. epigraph::

           You can't specify an IP version 6 (IPv6) address.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-serverhostname
        '''
        result = self._values.get("server_hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination.

        The SMB path should be a path that's exported by the SMB server, or a subdirectory of that path. The path should be such that it can be mounted by other SMB clients in your network.
        .. epigraph::

           ``Subdirectory`` must be specified with forward slashes. For example, ``/path/to/folder`` .

        To transfer all the data in the folder you specified, DataSync must have permissions to mount the SMB share, as well as to access all the data in that share. To ensure this, either make sure that the user name and password specified belongs to the user who can mount the share, and who has the appropriate permissions for all of the files and directories that you want DataSync to access, or use credentials of a member of the Backup Operators group to mount the share. Doing either one enables the agent to access the data. For the agent to access directories, you must additionally enable all execute access.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.

        We recommend creating at least a name tag for your location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationSMBProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStorageSystem(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnStorageSystem",
):
    '''The ``AWS::DataSync::StorageSystem`` resource creates an AWS resource for an on-premises storage system that you want DataSync Discovery to collect information about.

    For more information, see `discovering your storage with DataSync Discovery. <https://docs.aws.amazon.com/datasync/latest/userguide/understanding-your-storage.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html
    :cloudformationResource: AWS::DataSync::StorageSystem
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_storage_system = datasync.CfnStorageSystem(self, "MyCfnStorageSystem",
            agent_arns=["agentArns"],
            server_configuration=datasync.CfnStorageSystem.ServerConfigurationProperty(
                server_hostname="serverHostname",
        
                # the properties below are optional
                server_port=123
            ),
            system_type="systemType",
        
            # the properties below are optional
            cloud_watch_log_group_arn="cloudWatchLogGroupArn",
            name="name",
            server_credentials=datasync.CfnStorageSystem.ServerCredentialsProperty(
                password="password",
                username="username"
            ),
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
        agent_arns: typing.Sequence[builtins.str],
        server_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnStorageSystem.ServerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        system_type: builtins.str,
        cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        server_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStorageSystem.ServerCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_arns: Specifies the Amazon Resource Name (ARN) of the DataSync agent that connects to and reads from your on-premises storage system's management interface. You can only specify one ARN.
        :param server_configuration: Specifies the server name and network port required to connect with the management interface of your on-premises storage system.
        :param system_type: Specifies the type of on-premises storage system that you want DataSync Discovery to collect information about. .. epigraph:: DataSync Discovery currently supports NetApp Fabric-Attached Storage (FAS) and All Flash FAS (AFF) systems running ONTAP 9.7 or later.
        :param cloud_watch_log_group_arn: Specifies the ARN of the Amazon CloudWatch log group for monitoring and logging discovery job events.
        :param name: Specifies a familiar name for your on-premises storage system.
        :param server_credentials: Specifies the user name and password for accessing your on-premises storage system's management interface.
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your on-premises storage system.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd03aea3d03c00385e272f326dc093d0575219e3eac09a9f89062f9453a9360f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStorageSystemProps(
            agent_arns=agent_arns,
            server_configuration=server_configuration,
            system_type=system_type,
            cloud_watch_log_group_arn=cloud_watch_log_group_arn,
            name=name,
            server_credentials=server_credentials,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d30237b704bab23311aad893ff50107b6fc1840c11f7ab06f9fd41ffce46d0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81b9c192e8b33247af58d9ec7498864f379be5476b6c0a2aeb98684bc257c348)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectivityStatus")
    def attr_connectivity_status(self) -> builtins.str:
        '''Indicates whether your DataSync agent can connect to your on-premises storage system.

        :cloudformationAttribute: ConnectivityStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectivityStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrSecretsManagerArn")
    def attr_secrets_manager_arn(self) -> builtins.str:
        '''The ARN of the secret that stores your on-premises storage system's credentials.

        DataSync Discovery stores these credentials in `AWS Secrets Manager <https://docs.aws.amazon.com/datasync/latest/userguide/discovery-configure-storage.html#discovery-add-storage>`_ .

        :cloudformationAttribute: SecretsManagerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSecretsManagerArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageSystemArn")
    def attr_storage_system_arn(self) -> builtins.str:
        '''The ARN of the on-premises storage system that you're using with DataSync Discovery.

        :cloudformationAttribute: StorageSystemArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageSystemArn"))

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
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) of the DataSync agent that connects to and reads from your on-premises storage system's management interface.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91c1b3e5cd2d7dd98537d8ad2c7deae28f00b5d6d23089b99cb0768ef5ca4d7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentArns", value)

    @builtins.property
    @jsii.member(jsii_name="serverConfiguration")
    def server_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnStorageSystem.ServerConfigurationProperty"]:
        '''Specifies the server name and network port required to connect with the management interface of your on-premises storage system.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnStorageSystem.ServerConfigurationProperty"], jsii.get(self, "serverConfiguration"))

    @server_configuration.setter
    def server_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnStorageSystem.ServerConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81366a44879ecfffc2cf1020a13667d2ef18466bde35cc8a36864bab3668086b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="systemType")
    def system_type(self) -> builtins.str:
        '''Specifies the type of on-premises storage system that you want DataSync Discovery to collect information about.'''
        return typing.cast(builtins.str, jsii.get(self, "systemType"))

    @system_type.setter
    def system_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ac346e347fbe1b4d60467d3562a6b070e1ed3e50a18844309f094f5f94cb7f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemType", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the ARN of the Amazon CloudWatch log group for monitoring and logging discovery job events.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogGroupArn"))

    @cloud_watch_log_group_arn.setter
    def cloud_watch_log_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8cf99420b818e4ec735e8ef96836c7c265a5bb74331a73d84e9fc56a6321299)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLogGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies a familiar name for your on-premises storage system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__764666a950d4d83875874f1d9312ef4c5d98748fc51fe8f1dc9c8cf696e4e0bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serverCredentials")
    def server_credentials(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStorageSystem.ServerCredentialsProperty"]]:
        '''Specifies the user name and password for accessing your on-premises storage system's management interface.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStorageSystem.ServerCredentialsProperty"]], jsii.get(self, "serverCredentials"))

    @server_credentials.setter
    def server_credentials(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStorageSystem.ServerCredentialsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f52a2f2a6197dee934b3eaad41d0b7cc429e508ed4c3d4437b45f339ffd8712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f06b57402f5a745b22a5a454fa8563a935276c499111bb78103406214b07c52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnStorageSystem.ServerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "server_hostname": "serverHostname",
            "server_port": "serverPort",
        },
    )
    class ServerConfigurationProperty:
        def __init__(
            self,
            *,
            server_hostname: builtins.str,
            server_port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The network settings that DataSync Discovery uses to connect with your on-premises storage system's management interface.

            :param server_hostname: The domain name or IP address of your storage system's management interface.
            :param server_port: The network port for accessing the storage system's management interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-serverconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                server_configuration_property = datasync.CfnStorageSystem.ServerConfigurationProperty(
                    server_hostname="serverHostname",
                
                    # the properties below are optional
                    server_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b2d9d38924c8714fdacccf65a04ce2f4670647a35b1330abeacb71b09b32c66)
                check_type(argname="argument server_hostname", value=server_hostname, expected_type=type_hints["server_hostname"])
                check_type(argname="argument server_port", value=server_port, expected_type=type_hints["server_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "server_hostname": server_hostname,
            }
            if server_port is not None:
                self._values["server_port"] = server_port

        @builtins.property
        def server_hostname(self) -> builtins.str:
            '''The domain name or IP address of your storage system's management interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-serverconfiguration.html#cfn-datasync-storagesystem-serverconfiguration-serverhostname
            '''
            result = self._values.get("server_hostname")
            assert result is not None, "Required property 'server_hostname' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def server_port(self) -> typing.Optional[jsii.Number]:
            '''The network port for accessing the storage system's management interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-serverconfiguration.html#cfn-datasync-storagesystem-serverconfiguration-serverport
            '''
            result = self._values.get("server_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnStorageSystem.ServerCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"password": "password", "username": "username"},
    )
    class ServerCredentialsProperty:
        def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
            '''The credentials that provide DataSync Discovery read access to your on-premises storage system's management interface.

            DataSync Discovery stores these credentials in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_ . For more information, see `Accessing your on-premises storage system <https://docs.aws.amazon.com/datasync/latest/userguide/discovery-configure-storage.html>`_ .

            :param password: Specifies the password for your storage system's management interface.
            :param username: Specifies the user name for your storage system's management interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-servercredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                server_credentials_property = datasync.CfnStorageSystem.ServerCredentialsProperty(
                    password="password",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4aca605fb52bb6e32c26164545155c20da0e4d47eff8787d0c19d543d3f0f293)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password": password,
                "username": username,
            }

        @builtins.property
        def password(self) -> builtins.str:
            '''Specifies the password for your storage system's management interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-servercredentials.html#cfn-datasync-storagesystem-servercredentials-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''Specifies the user name for your storage system's management interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-servercredentials.html#cfn-datasync-storagesystem-servercredentials-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnStorageSystemProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_arns": "agentArns",
        "server_configuration": "serverConfiguration",
        "system_type": "systemType",
        "cloud_watch_log_group_arn": "cloudWatchLogGroupArn",
        "name": "name",
        "server_credentials": "serverCredentials",
        "tags": "tags",
    },
)
class CfnStorageSystemProps:
    def __init__(
        self,
        *,
        agent_arns: typing.Sequence[builtins.str],
        server_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageSystem.ServerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        system_type: builtins.str,
        cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        server_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageSystem.ServerCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStorageSystem``.

        :param agent_arns: Specifies the Amazon Resource Name (ARN) of the DataSync agent that connects to and reads from your on-premises storage system's management interface. You can only specify one ARN.
        :param server_configuration: Specifies the server name and network port required to connect with the management interface of your on-premises storage system.
        :param system_type: Specifies the type of on-premises storage system that you want DataSync Discovery to collect information about. .. epigraph:: DataSync Discovery currently supports NetApp Fabric-Attached Storage (FAS) and All Flash FAS (AFF) systems running ONTAP 9.7 or later.
        :param cloud_watch_log_group_arn: Specifies the ARN of the Amazon CloudWatch log group for monitoring and logging discovery job events.
        :param name: Specifies a familiar name for your on-premises storage system.
        :param server_credentials: Specifies the user name and password for accessing your on-premises storage system's management interface.
        :param tags: Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your on-premises storage system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_storage_system_props = datasync.CfnStorageSystemProps(
                agent_arns=["agentArns"],
                server_configuration=datasync.CfnStorageSystem.ServerConfigurationProperty(
                    server_hostname="serverHostname",
            
                    # the properties below are optional
                    server_port=123
                ),
                system_type="systemType",
            
                # the properties below are optional
                cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                name="name",
                server_credentials=datasync.CfnStorageSystem.ServerCredentialsProperty(
                    password="password",
                    username="username"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07c9f88707493efc0c6204abeacfb93dcb4bfdc339feb06b9cedb3c14e549a6)
            check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            check_type(argname="argument server_configuration", value=server_configuration, expected_type=type_hints["server_configuration"])
            check_type(argname="argument system_type", value=system_type, expected_type=type_hints["system_type"])
            check_type(argname="argument cloud_watch_log_group_arn", value=cloud_watch_log_group_arn, expected_type=type_hints["cloud_watch_log_group_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument server_credentials", value=server_credentials, expected_type=type_hints["server_credentials"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arns": agent_arns,
            "server_configuration": server_configuration,
            "system_type": system_type,
        }
        if cloud_watch_log_group_arn is not None:
            self._values["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
        if name is not None:
            self._values["name"] = name
        if server_credentials is not None:
            self._values["server_credentials"] = server_credentials
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_arns(self) -> typing.List[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) of the DataSync agent that connects to and reads from your on-premises storage system's management interface.

        You can only specify one ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-agentarns
        '''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def server_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnStorageSystem.ServerConfigurationProperty]:
        '''Specifies the server name and network port required to connect with the management interface of your on-premises storage system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-serverconfiguration
        '''
        result = self._values.get("server_configuration")
        assert result is not None, "Required property 'server_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnStorageSystem.ServerConfigurationProperty], result)

    @builtins.property
    def system_type(self) -> builtins.str:
        '''Specifies the type of on-premises storage system that you want DataSync Discovery to collect information about.

        .. epigraph::

           DataSync Discovery currently supports NetApp Fabric-Attached Storage (FAS) and All Flash FAS (AFF) systems running ONTAP 9.7 or later.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-systemtype
        '''
        result = self._values.get("system_type")
        assert result is not None, "Required property 'system_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the ARN of the Amazon CloudWatch log group for monitoring and logging discovery job events.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-cloudwatchloggrouparn
        '''
        result = self._values.get("cloud_watch_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies a familiar name for your on-premises storage system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_credentials(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStorageSystem.ServerCredentialsProperty]]:
        '''Specifies the user name and password for accessing your on-premises storage system's management interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-servercredentials
        '''
        result = self._values.get("server_credentials")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStorageSystem.ServerCredentialsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies labels that help you categorize, filter, and search for your AWS resources.

        We recommend creating at least a name tag for your on-premises storage system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStorageSystemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTask(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datasync.CfnTask",
):
    '''The ``AWS::DataSync::Task`` resource specifies a task.

    A task is a set of two locations (source and destination) and a set of ``Options`` that you use to control the behavior of a task. If you don't specify ``Options`` when you create a task, AWS DataSync populates them with service defaults.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html
    :cloudformationResource: AWS::DataSync::Task
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datasync as datasync
        
        cfn_task = datasync.CfnTask(self, "MyCfnTask",
            destination_location_arn="destinationLocationArn",
            source_location_arn="sourceLocationArn",
        
            # the properties below are optional
            cloud_watch_log_group_arn="cloudWatchLogGroupArn",
            excludes=[datasync.CfnTask.FilterRuleProperty(
                filter_type="filterType",
                value="value"
            )],
            includes=[datasync.CfnTask.FilterRuleProperty(
                filter_type="filterType",
                value="value"
            )],
            manifest_config=datasync.CfnTask.ManifestConfigProperty(
                source=datasync.CfnTask.SourceProperty(
                    s3=datasync.CfnTask.ManifestConfigSourceS3Property(
                        bucket_access_role_arn="bucketAccessRoleArn",
                        manifest_object_path="manifestObjectPath",
                        manifest_object_version_id="manifestObjectVersionId",
                        s3_bucket_arn="s3BucketArn"
                    )
                ),
        
                # the properties below are optional
                action="action",
                format="format"
            ),
            name="name",
            options=datasync.CfnTask.OptionsProperty(
                atime="atime",
                bytes_per_second=123,
                gid="gid",
                log_level="logLevel",
                mtime="mtime",
                object_tags="objectTags",
                overwrite_mode="overwriteMode",
                posix_permissions="posixPermissions",
                preserve_deleted_files="preserveDeletedFiles",
                preserve_devices="preserveDevices",
                security_descriptor_copy_flags="securityDescriptorCopyFlags",
                task_queueing="taskQueueing",
                transfer_mode="transferMode",
                uid="uid",
                verify_mode="verifyMode"
            ),
            schedule=datasync.CfnTask.TaskScheduleProperty(
                schedule_expression="scheduleExpression",
                status="status"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            task_report_config=datasync.CfnTask.TaskReportConfigProperty(
                destination=datasync.CfnTask.DestinationProperty(
                    s3=datasync.CfnTask.S3Property(
                        bucket_access_role_arn="bucketAccessRoleArn",
                        s3_bucket_arn="s3BucketArn",
                        subdirectory="subdirectory"
                    )
                ),
                output_type="outputType",
        
                # the properties below are optional
                object_version_ids="objectVersionIds",
                overrides=datasync.CfnTask.OverridesProperty(
                    deleted=datasync.CfnTask.DeletedProperty(
                        report_level="reportLevel"
                    ),
                    skipped=datasync.CfnTask.SkippedProperty(
                        report_level="reportLevel"
                    ),
                    transferred=datasync.CfnTask.TransferredProperty(
                        report_level="reportLevel"
                    ),
                    verified=datasync.CfnTask.VerifiedProperty(
                        report_level="reportLevel"
                    )
                ),
                report_level="reportLevel"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_location_arn: builtins.str,
        source_location_arn: builtins.str,
        cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
        excludes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.FilterRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        includes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.FilterRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        manifest_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.ManifestConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.OptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.TaskScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_report_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.TaskReportConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_location_arn: The Amazon Resource Name (ARN) of an AWS storage resource's location.
        :param source_location_arn: Specifies the ARN of your transfer's source location.
        :param cloud_watch_log_group_arn: Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task. For more information, see `Monitoring DataSync with Amazon CloudWatch <https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html>`_ .
        :param excludes: Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see `Specifying what DataSync transfers by using filters <https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html>`_ .
        :param includes: Specifies include filters define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see `Specifying what DataSync transfers by using filters <https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html>`_ .
        :param manifest_config: The configuration of the manifest that lists the files or objects that you want DataSync to transfer. For more information, see `Specifying what DataSync transfers by using a manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html>`_ .
        :param name: Specifies the name of your task.
        :param options: Specifies your task's settings, such as preserving file metadata, verifying data integrity, among other options.
        :param schedule: Specifies a schedule for when you want your task to run. For more information, see `Scheduling your task <https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html>`_ .
        :param tags: Specifies the tags that you want to apply to your task. *Tags* are key-value pairs that help you manage, filter, and search for your DataSync resources.
        :param task_report_config: Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see `Monitoring your DataSync transfers with task reports <https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html>`_ . When using this parameter, your caller identity (the role that you're using DataSync with) must have the ``iam:PassRole`` permission. The `AWSDataSyncFullAccess <https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess>`_ policy includes this permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9add9673a1f0ceb078949e967bce91066ff7e0441dae95d55c11c4a503a397a6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTaskProps(
            destination_location_arn=destination_location_arn,
            source_location_arn=source_location_arn,
            cloud_watch_log_group_arn=cloud_watch_log_group_arn,
            excludes=excludes,
            includes=includes,
            manifest_config=manifest_config,
            name=name,
            options=options,
            schedule=schedule,
            tags=tags,
            task_report_config=task_report_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3be7cc30ea459e593fff3fb2223f039edaac10f8cf48a8f35f3ea41ae0a0ac99)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fbe8c198a5a1427e6615104f061ae888f969b7fa0c0a6ed3761dab32c01d9ad)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDestinationNetworkInterfaceArns")
    def attr_destination_network_interface_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of the destination elastic network interfaces (ENIs) that were created for your subnet.

        :cloudformationAttribute: DestinationNetworkInterfaceArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDestinationNetworkInterfaceArns"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceNetworkInterfaceArns")
    def attr_source_network_interface_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of the source ENIs that were created for your subnet.

        :cloudformationAttribute: SourceNetworkInterfaceArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSourceNetworkInterfaceArns"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the task that was described.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTaskArn")
    def attr_task_arn(self) -> builtins.str:
        '''The ARN of the task.

        :cloudformationAttribute: TaskArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTaskArn"))

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
    @jsii.member(jsii_name="destinationLocationArn")
    def destination_location_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of an AWS storage resource's location.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationLocationArn"))

    @destination_location_arn.setter
    def destination_location_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c829157af3cc4eaa91bd0ad747876d59f15cb71ac8ca56cbf9c19eae4bf9f086)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationLocationArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceLocationArn")
    def source_location_arn(self) -> builtins.str:
        '''Specifies the ARN of your transfer's source location.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceLocationArn"))

    @source_location_arn.setter
    def source_location_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ade222686ff2f8ad1e7e9582615e0d6dec7ef562c42e32823bf1637619af7b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceLocationArn", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogGroupArn"))

    @cloud_watch_log_group_arn.setter
    def cloud_watch_log_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5688467482337659d3d0d35a3798391a47635ed6dc628a2cfa41b22b61d0abe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLogGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTask.FilterRuleProperty"]]]]:
        '''Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTask.FilterRuleProperty"]]]], jsii.get(self, "excludes"))

    @excludes.setter
    def excludes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTask.FilterRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acacc184cead1f95fccb09d6e2d3e2f3763099227a59edf6a76e8128856fc021)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludes", value)

    @builtins.property
    @jsii.member(jsii_name="includes")
    def includes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTask.FilterRuleProperty"]]]]:
        '''Specifies include filters define the files, objects, and folders in your source location that you want DataSync to transfer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTask.FilterRuleProperty"]]]], jsii.get(self, "includes"))

    @includes.setter
    def includes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTask.FilterRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b70b42cfb53e13801c9b46a0aeb316cf7696061c5b7fc11b20c7970679838adb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includes", value)

    @builtins.property
    @jsii.member(jsii_name="manifestConfig")
    def manifest_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.ManifestConfigProperty"]]:
        '''The configuration of the manifest that lists the files or objects that you want DataSync to transfer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.ManifestConfigProperty"]], jsii.get(self, "manifestConfig"))

    @manifest_config.setter
    def manifest_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.ManifestConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adfc26e9a88359e12066dd2ec9b2a9e0a61fb79f73189fa8a39e637687c9fa9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifestConfig", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of your task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de210bcc8ac65745973f2b8e5143c561a12afe1f24163e2b50a4fe61574c7317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.OptionsProperty"]]:
        '''Specifies your task's settings, such as preserving file metadata, verifying data integrity, among other options.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.OptionsProperty"]], jsii.get(self, "options"))

    @options.setter
    def options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.OptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__155643afb5f1ecdb689d1809d2d2388ec39615a2be33d1719f3b98ba2e76677d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.TaskScheduleProperty"]]:
        '''Specifies a schedule for when you want your task to run.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.TaskScheduleProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.TaskScheduleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc267a8182541bd31db0c914ab3030d3b13f68b424b8e312a7b9267e3b0e4b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the tags that you want to apply to your task.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6a7067dff337df84908e53f4652767faada60769f6c9d1eed4c84d05c1d5126)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="taskReportConfig")
    def task_report_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.TaskReportConfigProperty"]]:
        '''Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.TaskReportConfigProperty"]], jsii.get(self, "taskReportConfig"))

    @task_report_config.setter
    def task_report_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.TaskReportConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06ecaf368f7ae42942552393e7a68a01ddc8712caa5620400a489d0b07baae6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskReportConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.DeletedProperty",
        jsii_struct_bases=[],
        name_mapping={"report_level": "reportLevel"},
    )
    class DeletedProperty:
        def __init__(
            self,
            *,
            report_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The reporting level for the deleted section of your DataSync task report.

            :param report_level: Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't. - ``ERRORS_ONLY`` : A report shows what DataSync was unable to delete. - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to delete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-deleted.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                deleted_property = datasync.CfnTask.DeletedProperty(
                    report_level="reportLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f037d4931daef78ea8657014c8257621eda14339f1dc65a4f3763703e838d7dd)
                check_type(argname="argument report_level", value=report_level, expected_type=type_hints["report_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if report_level is not None:
                self._values["report_level"] = report_level

        @builtins.property
        def report_level(self) -> typing.Optional[builtins.str]:
            '''Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't.

            - ``ERRORS_ONLY`` : A report shows what DataSync was unable to delete.
            - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to delete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-deleted.html#cfn-datasync-task-deleted-reportlevel
            '''
            result = self._values.get("report_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeletedProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3"},
    )
    class DestinationProperty:
        def __init__(
            self,
            *,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.S3Property", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies where DataSync uploads your `task report <https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html>`_ .

            :param s3: Specifies the Amazon S3 bucket where DataSync uploads your task report.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                destination_property = datasync.CfnTask.DestinationProperty(
                    s3=datasync.CfnTask.S3Property(
                        bucket_access_role_arn="bucketAccessRoleArn",
                        s3_bucket_arn="s3BucketArn",
                        subdirectory="subdirectory"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be6e4582c5e377e943fda0f71516c06eaa109c591ef7c38d5feb106fed3d93d8)
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.S3Property"]]:
            '''Specifies the Amazon S3 bucket where DataSync uploads your task report.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-destination.html#cfn-datasync-task-destination-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.S3Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.FilterRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"filter_type": "filterType", "value": "value"},
    )
    class FilterRuleProperty:
        def __init__(
            self,
            *,
            filter_type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies which files, folders, and objects to include or exclude when transferring files from source to destination.

            :param filter_type: The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.
            :param value: A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                filter_rule_property = datasync.CfnTask.FilterRuleProperty(
                    filter_type="filterType",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2957bcb9b505b6af4afc512d05d4225e97bb106c72da06526a6a27ec87040de)
                check_type(argname="argument filter_type", value=filter_type, expected_type=type_hints["filter_type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if filter_type is not None:
                self._values["filter_type"] = filter_type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def filter_type(self) -> typing.Optional[builtins.str]:
            '''The type of filter rule to apply.

            AWS DataSync only supports the SIMPLE_PATTERN rule type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-filtertype
            '''
            result = self._values.get("filter_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''A single filter string that consists of the patterns to include or exclude.

            The patterns are delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.ManifestConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source", "action": "action", "format": "format"},
    )
    class ManifestConfigProperty:
        def __init__(
            self,
            *,
            source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
            action: typing.Optional[builtins.str] = None,
            format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configures a manifest, which is a list of files or objects that you want AWS DataSync to transfer.

            For more information and configuration examples, see `Specifying what DataSync transfers by using a manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html>`_ .

            :param source: Specifies the manifest that you want DataSync to use and where it's hosted. .. epigraph:: You must specify this parameter if you're configuring a new manifest on or after February 7, 2024. If you don't, you'll get a 400 status code and ``ValidationException`` error stating that you're missing the IAM role for DataSync to access the S3 bucket where you're hosting your manifest. For more information, see `Providing DataSync access to your manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access>`_ .
            :param action: Specifies what DataSync uses the manifest for.
            :param format: Specifies the file format of your manifest. For more information, see `Creating a manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-create>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                manifest_config_property = datasync.CfnTask.ManifestConfigProperty(
                    source=datasync.CfnTask.SourceProperty(
                        s3=datasync.CfnTask.ManifestConfigSourceS3Property(
                            bucket_access_role_arn="bucketAccessRoleArn",
                            manifest_object_path="manifestObjectPath",
                            manifest_object_version_id="manifestObjectVersionId",
                            s3_bucket_arn="s3BucketArn"
                        )
                    ),
                
                    # the properties below are optional
                    action="action",
                    format="format"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24f392dd164095fff95d497fcd80fd8e99a252d97a070e9cb64573100cdcc65c)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source": source,
            }
            if action is not None:
                self._values["action"] = action
            if format is not None:
                self._values["format"] = format

        @builtins.property
        def source(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTask.SourceProperty"]:
            '''Specifies the manifest that you want DataSync to use and where it's hosted.

            .. epigraph::

               You must specify this parameter if you're configuring a new manifest on or after February 7, 2024.

               If you don't, you'll get a 400 status code and ``ValidationException`` error stating that you're missing the IAM role for DataSync to access the S3 bucket where you're hosting your manifest. For more information, see `Providing DataSync access to your manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfig.html#cfn-datasync-task-manifestconfig-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTask.SourceProperty"], result)

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''Specifies what DataSync uses the manifest for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfig.html#cfn-datasync-task-manifestconfig-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''Specifies the file format of your manifest.

            For more information, see `Creating a manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-create>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfig.html#cfn-datasync-task-manifestconfig-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManifestConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.ManifestConfigSourceS3Property",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_access_role_arn": "bucketAccessRoleArn",
            "manifest_object_path": "manifestObjectPath",
            "manifest_object_version_id": "manifestObjectVersionId",
            "s3_bucket_arn": "s3BucketArn",
        },
    )
    class ManifestConfigSourceS3Property:
        def __init__(
            self,
            *,
            bucket_access_role_arn: typing.Optional[builtins.str] = None,
            manifest_object_path: typing.Optional[builtins.str] = None,
            manifest_object_version_id: typing.Optional[builtins.str] = None,
            s3_bucket_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the S3 bucket where you're hosting the manifest that you want AWS DataSync to use.

            For more information and configuration examples, see `Specifying what DataSync transfers by using a manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html>`_ .

            :param bucket_access_role_arn: Specifies the AWS Identity and Access Management (IAM) role that allows DataSync to access your manifest. For more information, see `Providing DataSync access to your manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access>`_ .
            :param manifest_object_path: Specifies the Amazon S3 object key of your manifest. This can include a prefix (for example, ``prefix/my-manifest.csv`` ).
            :param manifest_object_version_id: Specifies the object version ID of the manifest that you want DataSync to use. If you don't set this, DataSync uses the latest version of the object.
            :param s3_bucket_arn: Specifies the Amazon Resource Name (ARN) of the S3 bucket where you're hosting your manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfigsources3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                manifest_config_source_s3_property = datasync.CfnTask.ManifestConfigSourceS3Property(
                    bucket_access_role_arn="bucketAccessRoleArn",
                    manifest_object_path="manifestObjectPath",
                    manifest_object_version_id="manifestObjectVersionId",
                    s3_bucket_arn="s3BucketArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1d8718794bcb3bdc90c54997b7600d13961852c4adddc60005e8bf3016ef3f8)
                check_type(argname="argument bucket_access_role_arn", value=bucket_access_role_arn, expected_type=type_hints["bucket_access_role_arn"])
                check_type(argname="argument manifest_object_path", value=manifest_object_path, expected_type=type_hints["manifest_object_path"])
                check_type(argname="argument manifest_object_version_id", value=manifest_object_version_id, expected_type=type_hints["manifest_object_version_id"])
                check_type(argname="argument s3_bucket_arn", value=s3_bucket_arn, expected_type=type_hints["s3_bucket_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_access_role_arn is not None:
                self._values["bucket_access_role_arn"] = bucket_access_role_arn
            if manifest_object_path is not None:
                self._values["manifest_object_path"] = manifest_object_path
            if manifest_object_version_id is not None:
                self._values["manifest_object_version_id"] = manifest_object_version_id
            if s3_bucket_arn is not None:
                self._values["s3_bucket_arn"] = s3_bucket_arn

        @builtins.property
        def bucket_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''Specifies the AWS Identity and Access Management (IAM) role that allows DataSync to access your manifest.

            For more information, see `Providing DataSync access to your manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfigsources3.html#cfn-datasync-task-manifestconfigsources3-bucketaccessrolearn
            '''
            result = self._values.get("bucket_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_object_path(self) -> typing.Optional[builtins.str]:
            '''Specifies the Amazon S3 object key of your manifest.

            This can include a prefix (for example, ``prefix/my-manifest.csv`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfigsources3.html#cfn-datasync-task-manifestconfigsources3-manifestobjectpath
            '''
            result = self._values.get("manifest_object_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_object_version_id(self) -> typing.Optional[builtins.str]:
            '''Specifies the object version ID of the manifest that you want DataSync to use.

            If you don't set this, DataSync uses the latest version of the object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfigsources3.html#cfn-datasync-task-manifestconfigsources3-manifestobjectversionid
            '''
            result = self._values.get("manifest_object_version_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_bucket_arn(self) -> typing.Optional[builtins.str]:
            '''Specifies the Amazon Resource Name (ARN) of the S3 bucket where you're hosting your manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-manifestconfigsources3.html#cfn-datasync-task-manifestconfigsources3-s3bucketarn
            '''
            result = self._values.get("s3_bucket_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManifestConfigSourceS3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.OptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "atime": "atime",
            "bytes_per_second": "bytesPerSecond",
            "gid": "gid",
            "log_level": "logLevel",
            "mtime": "mtime",
            "object_tags": "objectTags",
            "overwrite_mode": "overwriteMode",
            "posix_permissions": "posixPermissions",
            "preserve_deleted_files": "preserveDeletedFiles",
            "preserve_devices": "preserveDevices",
            "security_descriptor_copy_flags": "securityDescriptorCopyFlags",
            "task_queueing": "taskQueueing",
            "transfer_mode": "transferMode",
            "uid": "uid",
            "verify_mode": "verifyMode",
        },
    )
    class OptionsProperty:
        def __init__(
            self,
            *,
            atime: typing.Optional[builtins.str] = None,
            bytes_per_second: typing.Optional[jsii.Number] = None,
            gid: typing.Optional[builtins.str] = None,
            log_level: typing.Optional[builtins.str] = None,
            mtime: typing.Optional[builtins.str] = None,
            object_tags: typing.Optional[builtins.str] = None,
            overwrite_mode: typing.Optional[builtins.str] = None,
            posix_permissions: typing.Optional[builtins.str] = None,
            preserve_deleted_files: typing.Optional[builtins.str] = None,
            preserve_devices: typing.Optional[builtins.str] = None,
            security_descriptor_copy_flags: typing.Optional[builtins.str] = None,
            task_queueing: typing.Optional[builtins.str] = None,
            transfer_mode: typing.Optional[builtins.str] = None,
            uid: typing.Optional[builtins.str] = None,
            verify_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents the options that are available to control the behavior of a `StartTaskExecution <https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html>`_ operation. This behavior includes preserving metadata, such as user ID (UID), group ID (GID), and file permissions; overwriting files in the destination; data integrity verification; and so on.

            A task has a set of default options associated with it. If you don't specify an option in `StartTaskExecution <https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html>`_ , the default value is used. You can override the default options on each task execution by specifying an overriding ``Options`` value to `StartTaskExecution <https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html>`_ .

            :param atime: A file metadata value that shows the last time that a file was accessed (that is, when the file was read or written to). If you set ``Atime`` to ``BEST_EFFORT`` , AWS DataSync attempts to preserve the original ``Atime`` attribute on all source files (that is, the version before the PREPARING phase). However, ``Atime`` 's behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis. Default value: ``BEST_EFFORT`` ``BEST_EFFORT`` : Attempt to preserve the per-file ``Atime`` value (recommended). ``NONE`` : Ignore ``Atime`` . .. epigraph:: If ``Atime`` is set to ``BEST_EFFORT`` , ``Mtime`` must be set to ``PRESERVE`` . If ``Atime`` is set to ``NONE`` , ``Mtime`` must also be ``NONE`` .
            :param bytes_per_second: A value that limits the bandwidth used by AWS DataSync . For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to ``1048576`` (=1024*1024).
            :param gid: The group ID (GID) of the file's owners. Default value: ``INT_VALUE`` ``INT_VALUE`` : Preserve the integer value of the user ID (UID) and group ID (GID) (recommended). ``NAME`` : Currently not supported. ``NONE`` : Ignore the UID and GID.
            :param log_level: Specifies the type of logs that DataSync publishes to a Amazon CloudWatch Logs log group. To specify the log group, see `CloudWatchLogGroupArn <https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html#DataSync-CreateTask-request-CloudWatchLogGroupArn>`_ . - ``BASIC`` - Publishes logs with only basic information (such as transfer errors). - ``TRANSFER`` - Publishes logs for all files or objects that your DataSync task transfers and performs data-integrity checks on. - ``OFF`` - No logs are published.
            :param mtime: A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase. This option is required for cases when you need to run the same task more than one time. Default value: ``PRESERVE`` ``PRESERVE`` : Preserve original ``Mtime`` (recommended) ``NONE`` : Ignore ``Mtime`` . .. epigraph:: If ``Mtime`` is set to ``PRESERVE`` , ``Atime`` must be set to ``BEST_EFFORT`` . If ``Mtime`` is set to ``NONE`` , ``Atime`` must also be set to ``NONE`` .
            :param object_tags: Specifies whether you want DataSync to ``PRESERVE`` object tags (default behavior) when transferring between object storage systems. If you want your DataSync task to ignore object tags, specify the ``NONE`` value.
            :param overwrite_mode: Specifies whether DataSync should modify or preserve data at the destination location. - ``ALWAYS`` (default) - DataSync modifies data in the destination location when source data (including metadata) has changed. If DataSync overwrites objects, you might incur additional charges for certain Amazon S3 storage classes (for example, for retrieval or early deletion). For more information, see `Storage class considerations with Amazon S3 transfers <https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes>`_ . - ``NEVER`` - DataSync doesn't overwrite data in the destination location even if the source data has changed. You can use this option to protect against overwriting changes made to files or objects in the destination.
            :param posix_permissions: A value that determines which users or groups can access a file for a specific purpose, such as reading, writing, or execution of the file. This option should be set only for Network File System (NFS), Amazon EFS, and Amazon S3 locations. For more information about what metadata is copied by DataSync, see `Metadata Copied by DataSync <https://docs.aws.amazon.com/datasync/latest/userguide/special-files.html#metadata-copied>`_ . Default value: ``PRESERVE`` ``PRESERVE`` : Preserve POSIX-style permissions (recommended). ``NONE`` : Ignore permissions. .. epigraph:: AWS DataSync can preserve extant permissions of a source location.
            :param preserve_deleted_files: A value that specifies whether files in the destination that don't exist in the source file system are preserved. This option can affect your storage costs. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see `Considerations when working with Amazon S3 storage classes in DataSync <https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes>`_ in the *AWS DataSync User Guide* . Default value: ``PRESERVE`` ``PRESERVE`` : Ignore destination files that aren't present in the source (recommended). ``REMOVE`` : Delete destination files that aren't present in the source.
            :param preserve_devices: A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and re-create the files with that device name and metadata on the destination. DataSync does not copy the contents of such devices, only the name and metadata. .. epigraph:: AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and don't return an end-of-file (EOF) marker. Default value: ``NONE`` ``NONE`` : Ignore special devices (recommended). ``PRESERVE`` : Preserve character and block device metadata. This option isn't currently supported for Amazon EFS.
            :param security_descriptor_copy_flags: A value that determines which components of the SMB security descriptor are copied from source to destination objects. This value is only used for transfers between SMB and Amazon FSx for Windows File Server locations, or between two Amazon FSx for Windows File Server locations. For more information about how DataSync handles metadata, see `How DataSync Handles Metadata and Special Files <https://docs.aws.amazon.com/datasync/latest/userguide/special-files.html>`_ . Default value: ``OWNER_DACL`` ``OWNER_DACL`` : For each copied object, DataSync copies the following metadata: - Object owner. - NTFS discretionary access control lists (DACLs), which determine whether to grant access to an object. When you use option, DataSync does NOT copy the NTFS system access control lists (SACLs), which are used by administrators to log attempts to access a secured object. ``OWNER_DACL_SACL`` : For each copied object, DataSync copies the following metadata: - Object owner. - NTFS discretionary access control lists (DACLs), which determine whether to grant access to an object. - NTFS system access control lists (SACLs), which are used by administrators to log attempts to access a secured object. Copying SACLs requires granting additional permissions to the Windows user that DataSync uses to access your SMB location. For information about choosing a user that ensures sufficient permissions to files, folders, and metadata, see `user <https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#SMBuser>`_ . ``NONE`` : None of the SMB security descriptor components are copied. Destination objects are owned by the user that was provided for accessing the destination location. DACLs and SACLs are set based on the destination server’s configuration.
            :param task_queueing: Specifies whether your transfer tasks should be put into a queue during certain scenarios when `running multiple tasks <https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#running-multiple-tasks>`_ . This is ``ENABLED`` by default.
            :param transfer_mode: A value that determines whether DataSync transfers only the data and metadata that differ between the source and the destination location, or whether DataSync transfers all the content from the source, without comparing it to the destination location. ``CHANGED`` : DataSync copies only data or metadata that is new or different from the source location to the destination location. ``ALL`` : DataSync copies all source location content to the destination, without comparing it to existing content on the destination.
            :param uid: The user ID (UID) of the file's owner. Default value: ``INT_VALUE`` ``INT_VALUE`` : Preserve the integer value of the UID and group ID (GID) (recommended). ``NAME`` : Currently not supported ``NONE`` : Ignore the UID and GID.
            :param verify_mode: A value that determines whether a data integrity verification is performed at the end of a task execution after all data and metadata have been transferred. For more information, see `Configure task settings <https://docs.aws.amazon.com/datasync/latest/userguide/create-task.html>`_ . Default value: ``POINT_IN_TIME_CONSISTENT`` ``ONLY_FILES_TRANSFERRED`` (recommended): Perform verification only on files that were transferred. ``POINT_IN_TIME_CONSISTENT`` : Scan the entire source and entire destination at the end of the transfer to verify that the source and destination are fully synchronized. This option isn't supported when transferring to S3 Glacier or S3 Glacier Deep Archive storage classes. ``NONE`` : No additional verification is done at the end of the transfer, but all data transmissions are integrity-checked with checksum verification during the transfer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                options_property = datasync.CfnTask.OptionsProperty(
                    atime="atime",
                    bytes_per_second=123,
                    gid="gid",
                    log_level="logLevel",
                    mtime="mtime",
                    object_tags="objectTags",
                    overwrite_mode="overwriteMode",
                    posix_permissions="posixPermissions",
                    preserve_deleted_files="preserveDeletedFiles",
                    preserve_devices="preserveDevices",
                    security_descriptor_copy_flags="securityDescriptorCopyFlags",
                    task_queueing="taskQueueing",
                    transfer_mode="transferMode",
                    uid="uid",
                    verify_mode="verifyMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7557db697c0c06b71a63bdcbecc24fb94bbe4de1de1980fd9b1a7e36f454ea9)
                check_type(argname="argument atime", value=atime, expected_type=type_hints["atime"])
                check_type(argname="argument bytes_per_second", value=bytes_per_second, expected_type=type_hints["bytes_per_second"])
                check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
                check_type(argname="argument mtime", value=mtime, expected_type=type_hints["mtime"])
                check_type(argname="argument object_tags", value=object_tags, expected_type=type_hints["object_tags"])
                check_type(argname="argument overwrite_mode", value=overwrite_mode, expected_type=type_hints["overwrite_mode"])
                check_type(argname="argument posix_permissions", value=posix_permissions, expected_type=type_hints["posix_permissions"])
                check_type(argname="argument preserve_deleted_files", value=preserve_deleted_files, expected_type=type_hints["preserve_deleted_files"])
                check_type(argname="argument preserve_devices", value=preserve_devices, expected_type=type_hints["preserve_devices"])
                check_type(argname="argument security_descriptor_copy_flags", value=security_descriptor_copy_flags, expected_type=type_hints["security_descriptor_copy_flags"])
                check_type(argname="argument task_queueing", value=task_queueing, expected_type=type_hints["task_queueing"])
                check_type(argname="argument transfer_mode", value=transfer_mode, expected_type=type_hints["transfer_mode"])
                check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
                check_type(argname="argument verify_mode", value=verify_mode, expected_type=type_hints["verify_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if atime is not None:
                self._values["atime"] = atime
            if bytes_per_second is not None:
                self._values["bytes_per_second"] = bytes_per_second
            if gid is not None:
                self._values["gid"] = gid
            if log_level is not None:
                self._values["log_level"] = log_level
            if mtime is not None:
                self._values["mtime"] = mtime
            if object_tags is not None:
                self._values["object_tags"] = object_tags
            if overwrite_mode is not None:
                self._values["overwrite_mode"] = overwrite_mode
            if posix_permissions is not None:
                self._values["posix_permissions"] = posix_permissions
            if preserve_deleted_files is not None:
                self._values["preserve_deleted_files"] = preserve_deleted_files
            if preserve_devices is not None:
                self._values["preserve_devices"] = preserve_devices
            if security_descriptor_copy_flags is not None:
                self._values["security_descriptor_copy_flags"] = security_descriptor_copy_flags
            if task_queueing is not None:
                self._values["task_queueing"] = task_queueing
            if transfer_mode is not None:
                self._values["transfer_mode"] = transfer_mode
            if uid is not None:
                self._values["uid"] = uid
            if verify_mode is not None:
                self._values["verify_mode"] = verify_mode

        @builtins.property
        def atime(self) -> typing.Optional[builtins.str]:
            '''A file metadata value that shows the last time that a file was accessed (that is, when the file was read or written to).

            If you set ``Atime`` to ``BEST_EFFORT`` , AWS DataSync attempts to preserve the original ``Atime`` attribute on all source files (that is, the version before the PREPARING phase). However, ``Atime`` 's behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.

            Default value: ``BEST_EFFORT``

            ``BEST_EFFORT`` : Attempt to preserve the per-file ``Atime`` value (recommended).

            ``NONE`` : Ignore ``Atime`` .
            .. epigraph::

               If ``Atime`` is set to ``BEST_EFFORT`` , ``Mtime`` must be set to ``PRESERVE`` .

               If ``Atime`` is set to ``NONE`` , ``Mtime`` must also be ``NONE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-atime
            '''
            result = self._values.get("atime")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bytes_per_second(self) -> typing.Optional[jsii.Number]:
            '''A value that limits the bandwidth used by AWS DataSync .

            For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to ``1048576`` (=1024*1024).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-bytespersecond
            '''
            result = self._values.get("bytes_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gid(self) -> typing.Optional[builtins.str]:
            '''The group ID (GID) of the file's owners.

            Default value: ``INT_VALUE``

            ``INT_VALUE`` : Preserve the integer value of the user ID (UID) and group ID (GID) (recommended).

            ``NAME`` : Currently not supported.

            ``NONE`` : Ignore the UID and GID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-gid
            '''
            result = self._values.get("gid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''Specifies the type of logs that DataSync publishes to a Amazon CloudWatch Logs log group.

            To specify the log group, see `CloudWatchLogGroupArn <https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html#DataSync-CreateTask-request-CloudWatchLogGroupArn>`_ .

            - ``BASIC`` - Publishes logs with only basic information (such as transfer errors).
            - ``TRANSFER`` - Publishes logs for all files or objects that your DataSync task transfers and performs data-integrity checks on.
            - ``OFF`` - No logs are published.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mtime(self) -> typing.Optional[builtins.str]:
            '''A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.

            This option is required for cases when you need to run the same task more than one time.

            Default value: ``PRESERVE``

            ``PRESERVE`` : Preserve original ``Mtime`` (recommended)

            ``NONE`` : Ignore ``Mtime`` .
            .. epigraph::

               If ``Mtime`` is set to ``PRESERVE`` , ``Atime`` must be set to ``BEST_EFFORT`` .

               If ``Mtime`` is set to ``NONE`` , ``Atime`` must also be set to ``NONE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-mtime
            '''
            result = self._values.get("mtime")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_tags(self) -> typing.Optional[builtins.str]:
            '''Specifies whether you want DataSync to ``PRESERVE`` object tags (default behavior) when transferring between object storage systems.

            If you want your DataSync task to ignore object tags, specify the ``NONE`` value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-objecttags
            '''
            result = self._values.get("object_tags")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def overwrite_mode(self) -> typing.Optional[builtins.str]:
            '''Specifies whether DataSync should modify or preserve data at the destination location.

            - ``ALWAYS`` (default) - DataSync modifies data in the destination location when source data (including metadata) has changed.

            If DataSync overwrites objects, you might incur additional charges for certain Amazon S3 storage classes (for example, for retrieval or early deletion). For more information, see `Storage class considerations with Amazon S3 transfers <https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes>`_ .

            - ``NEVER`` - DataSync doesn't overwrite data in the destination location even if the source data has changed. You can use this option to protect against overwriting changes made to files or objects in the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-overwritemode
            '''
            result = self._values.get("overwrite_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def posix_permissions(self) -> typing.Optional[builtins.str]:
            '''A value that determines which users or groups can access a file for a specific purpose, such as reading, writing, or execution of the file.

            This option should be set only for Network File System (NFS), Amazon EFS, and Amazon S3 locations. For more information about what metadata is copied by DataSync, see `Metadata Copied by DataSync <https://docs.aws.amazon.com/datasync/latest/userguide/special-files.html#metadata-copied>`_ .

            Default value: ``PRESERVE``

            ``PRESERVE`` : Preserve POSIX-style permissions (recommended).

            ``NONE`` : Ignore permissions.
            .. epigraph::

               AWS DataSync can preserve extant permissions of a source location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-posixpermissions
            '''
            result = self._values.get("posix_permissions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preserve_deleted_files(self) -> typing.Optional[builtins.str]:
            '''A value that specifies whether files in the destination that don't exist in the source file system are preserved.

            This option can affect your storage costs. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see `Considerations when working with Amazon S3 storage classes in DataSync <https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes>`_ in the *AWS DataSync User Guide* .

            Default value: ``PRESERVE``

            ``PRESERVE`` : Ignore destination files that aren't present in the source (recommended).

            ``REMOVE`` : Delete destination files that aren't present in the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedeletedfiles
            '''
            result = self._values.get("preserve_deleted_files")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preserve_devices(self) -> typing.Optional[builtins.str]:
            '''A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and re-create the files with that device name and metadata on the destination.

            DataSync does not copy the contents of such devices, only the name and metadata.
            .. epigraph::

               AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and don't return an end-of-file (EOF) marker.

            Default value: ``NONE``

            ``NONE`` : Ignore special devices (recommended).

            ``PRESERVE`` : Preserve character and block device metadata. This option isn't currently supported for Amazon EFS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedevices
            '''
            result = self._values.get("preserve_devices")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_descriptor_copy_flags(self) -> typing.Optional[builtins.str]:
            '''A value that determines which components of the SMB security descriptor are copied from source to destination objects.

            This value is only used for transfers between SMB and Amazon FSx for Windows File Server locations, or between two Amazon FSx for Windows File Server locations. For more information about how DataSync handles metadata, see `How DataSync Handles Metadata and Special Files <https://docs.aws.amazon.com/datasync/latest/userguide/special-files.html>`_ .

            Default value: ``OWNER_DACL``

            ``OWNER_DACL`` : For each copied object, DataSync copies the following metadata:

            - Object owner.
            - NTFS discretionary access control lists (DACLs), which determine whether to grant access to an object.

            When you use option, DataSync does NOT copy the NTFS system access control lists (SACLs), which are used by administrators to log attempts to access a secured object.

            ``OWNER_DACL_SACL`` : For each copied object, DataSync copies the following metadata:

            - Object owner.
            - NTFS discretionary access control lists (DACLs), which determine whether to grant access to an object.
            - NTFS system access control lists (SACLs), which are used by administrators to log attempts to access a secured object.

            Copying SACLs requires granting additional permissions to the Windows user that DataSync uses to access your SMB location. For information about choosing a user that ensures sufficient permissions to files, folders, and metadata, see `user <https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#SMBuser>`_ .

            ``NONE`` : None of the SMB security descriptor components are copied. Destination objects are owned by the user that was provided for accessing the destination location. DACLs and SACLs are set based on the destination server’s configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-securitydescriptorcopyflags
            '''
            result = self._values.get("security_descriptor_copy_flags")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def task_queueing(self) -> typing.Optional[builtins.str]:
            '''Specifies whether your transfer tasks should be put into a queue during certain scenarios when `running multiple tasks <https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#running-multiple-tasks>`_ . This is ``ENABLED`` by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-taskqueueing
            '''
            result = self._values.get("task_queueing")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transfer_mode(self) -> typing.Optional[builtins.str]:
            '''A value that determines whether DataSync transfers only the data and metadata that differ between the source and the destination location, or whether DataSync transfers all the content from the source, without comparing it to the destination location.

            ``CHANGED`` : DataSync copies only data or metadata that is new or different from the source location to the destination location.

            ``ALL`` : DataSync copies all source location content to the destination, without comparing it to existing content on the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-transfermode
            '''
            result = self._values.get("transfer_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uid(self) -> typing.Optional[builtins.str]:
            '''The user ID (UID) of the file's owner.

            Default value: ``INT_VALUE``

            ``INT_VALUE`` : Preserve the integer value of the UID and group ID (GID) (recommended).

            ``NAME`` : Currently not supported

            ``NONE`` : Ignore the UID and GID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-uid
            '''
            result = self._values.get("uid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def verify_mode(self) -> typing.Optional[builtins.str]:
            '''A value that determines whether a data integrity verification is performed at the end of a task execution after all data and metadata have been transferred.

            For more information, see `Configure task settings <https://docs.aws.amazon.com/datasync/latest/userguide/create-task.html>`_ .

            Default value: ``POINT_IN_TIME_CONSISTENT``

            ``ONLY_FILES_TRANSFERRED`` (recommended): Perform verification only on files that were transferred.

            ``POINT_IN_TIME_CONSISTENT`` : Scan the entire source and entire destination at the end of the transfer to verify that the source and destination are fully synchronized. This option isn't supported when transferring to S3 Glacier or S3 Glacier Deep Archive storage classes.

            ``NONE`` : No additional verification is done at the end of the transfer, but all data transmissions are integrity-checked with checksum verification during the transfer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-verifymode
            '''
            result = self._values.get("verify_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.OverridesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deleted": "deleted",
            "skipped": "skipped",
            "transferred": "transferred",
            "verified": "verified",
        },
    )
    class OverridesProperty:
        def __init__(
            self,
            *,
            deleted: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.DeletedProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            skipped: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.SkippedProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            transferred: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.TransferredProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            verified: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.VerifiedProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Customizes the reporting level for aspects of your task report.

            For example, your report might generally only include errors, but you could specify that you want a list of successes and errors just for the files that DataSync attempted to delete in your destination location.

            :param deleted: Specifies the level of reporting for the files, objects, and directories that DataSync attempted to delete in your destination location. This only applies if you `configure your task <https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html>`_ to delete data in the destination that isn't in the source.
            :param skipped: Specifies the level of reporting for the files, objects, and directories that DataSync attempted to skip during your transfer.
            :param transferred: Specifies the level of reporting for the files, objects, and directories that DataSync attempted to transfer.
            :param verified: Specifies the level of reporting for the files, objects, and directories that DataSync attempted to verify during your transfer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                overrides_property = datasync.CfnTask.OverridesProperty(
                    deleted=datasync.CfnTask.DeletedProperty(
                        report_level="reportLevel"
                    ),
                    skipped=datasync.CfnTask.SkippedProperty(
                        report_level="reportLevel"
                    ),
                    transferred=datasync.CfnTask.TransferredProperty(
                        report_level="reportLevel"
                    ),
                    verified=datasync.CfnTask.VerifiedProperty(
                        report_level="reportLevel"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__56e46e186c62c84fedcf5320f54dff34c1ed74183d1e3e19905ddb4f42bdf47e)
                check_type(argname="argument deleted", value=deleted, expected_type=type_hints["deleted"])
                check_type(argname="argument skipped", value=skipped, expected_type=type_hints["skipped"])
                check_type(argname="argument transferred", value=transferred, expected_type=type_hints["transferred"])
                check_type(argname="argument verified", value=verified, expected_type=type_hints["verified"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if deleted is not None:
                self._values["deleted"] = deleted
            if skipped is not None:
                self._values["skipped"] = skipped
            if transferred is not None:
                self._values["transferred"] = transferred
            if verified is not None:
                self._values["verified"] = verified

        @builtins.property
        def deleted(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.DeletedProperty"]]:
            '''Specifies the level of reporting for the files, objects, and directories that DataSync attempted to delete in your destination location.

            This only applies if you `configure your task <https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html>`_ to delete data in the destination that isn't in the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html#cfn-datasync-task-overrides-deleted
            '''
            result = self._values.get("deleted")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.DeletedProperty"]], result)

        @builtins.property
        def skipped(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.SkippedProperty"]]:
            '''Specifies the level of reporting for the files, objects, and directories that DataSync attempted to skip during your transfer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html#cfn-datasync-task-overrides-skipped
            '''
            result = self._values.get("skipped")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.SkippedProperty"]], result)

        @builtins.property
        def transferred(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.TransferredProperty"]]:
            '''Specifies the level of reporting for the files, objects, and directories that DataSync attempted to transfer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html#cfn-datasync-task-overrides-transferred
            '''
            result = self._values.get("transferred")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.TransferredProperty"]], result)

        @builtins.property
        def verified(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.VerifiedProperty"]]:
            '''Specifies the level of reporting for the files, objects, and directories that DataSync attempted to verify during your transfer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html#cfn-datasync-task-overrides-verified
            '''
            result = self._values.get("verified")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.VerifiedProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.S3Property",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_access_role_arn": "bucketAccessRoleArn",
            "s3_bucket_arn": "s3BucketArn",
            "subdirectory": "subdirectory",
        },
    )
    class S3Property:
        def __init__(
            self,
            *,
            bucket_access_role_arn: typing.Optional[builtins.str] = None,
            s3_bucket_arn: typing.Optional[builtins.str] = None,
            subdirectory: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket_access_role_arn: 
            :param s3_bucket_arn: 
            :param subdirectory: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-s3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                s3_property = datasync.CfnTask.S3Property(
                    bucket_access_role_arn="bucketAccessRoleArn",
                    s3_bucket_arn="s3BucketArn",
                    subdirectory="subdirectory"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__20e126e77ec6892ccad16cb5774367950b600108005d5958e118340b3e757dd6)
                check_type(argname="argument bucket_access_role_arn", value=bucket_access_role_arn, expected_type=type_hints["bucket_access_role_arn"])
                check_type(argname="argument s3_bucket_arn", value=s3_bucket_arn, expected_type=type_hints["s3_bucket_arn"])
                check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_access_role_arn is not None:
                self._values["bucket_access_role_arn"] = bucket_access_role_arn
            if s3_bucket_arn is not None:
                self._values["s3_bucket_arn"] = s3_bucket_arn
            if subdirectory is not None:
                self._values["subdirectory"] = subdirectory

        @builtins.property
        def bucket_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-s3.html#cfn-datasync-task-s3-bucketaccessrolearn
            '''
            result = self._values.get("bucket_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_bucket_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-s3.html#cfn-datasync-task-s3-s3bucketarn
            '''
            result = self._values.get("s3_bucket_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subdirectory(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-s3.html#cfn-datasync-task-s3-subdirectory
            '''
            result = self._values.get("subdirectory")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.SkippedProperty",
        jsii_struct_bases=[],
        name_mapping={"report_level": "reportLevel"},
    )
    class SkippedProperty:
        def __init__(
            self,
            *,
            report_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The reporting level for the skipped section of your DataSync task report.

            :param report_level: Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't. - ``ERRORS_ONLY`` : A report shows what DataSync was unable to skip. - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to skip.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-skipped.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                skipped_property = datasync.CfnTask.SkippedProperty(
                    report_level="reportLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c18544378625bf9f1fbb6beae21b7f0068188b1f7befe07dd931ccd6703d499)
                check_type(argname="argument report_level", value=report_level, expected_type=type_hints["report_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if report_level is not None:
                self._values["report_level"] = report_level

        @builtins.property
        def report_level(self) -> typing.Optional[builtins.str]:
            '''Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't.

            - ``ERRORS_ONLY`` : A report shows what DataSync was unable to skip.
            - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to skip.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-skipped.html#cfn-datasync-task-skipped-reportlevel
            '''
            result = self._values.get("report_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SkippedProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3"},
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.ManifestConfigSourceS3Property", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the manifest that you want AWS DataSync to use and where it's hosted.

            For more information and configuration examples, see `Specifying what DataSync transfers by using a manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html>`_ .

            :param s3: Specifies the S3 bucket where you're hosting your manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                source_property = datasync.CfnTask.SourceProperty(
                    s3=datasync.CfnTask.ManifestConfigSourceS3Property(
                        bucket_access_role_arn="bucketAccessRoleArn",
                        manifest_object_path="manifestObjectPath",
                        manifest_object_version_id="manifestObjectVersionId",
                        s3_bucket_arn="s3BucketArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__648d2c1cae7d2043ba70966584d1164b3b2f9700f7b684da9f7e31f727c3d14d)
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.ManifestConfigSourceS3Property"]]:
            '''Specifies the S3 bucket where you're hosting your manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-source.html#cfn-datasync-task-source-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.ManifestConfigSourceS3Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.TaskReportConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "output_type": "outputType",
            "object_version_ids": "objectVersionIds",
            "overrides": "overrides",
            "report_level": "reportLevel",
        },
    )
    class TaskReportConfigProperty:
        def __init__(
            self,
            *,
            destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            output_type: builtins.str,
            object_version_ids: typing.Optional[builtins.str] = None,
            overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTask.OverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            report_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies how you want to configure a task report, which provides detailed information about for your AWS DataSync transfer.

            For more information, see `Task reports <https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html>`_ .

            :param destination: Specifies the Amazon S3 bucket where DataSync uploads your task report. For more information, see `Task reports <https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html#task-report-access>`_ .
            :param output_type: Specifies the type of task report that you want:. - ``SUMMARY_ONLY`` : Provides necessary details about your task, including the number of files, objects, and directories transferred and transfer duration. - ``STANDARD`` : Provides complete details about your task, including a full list of files, objects, and directories that were transferred, skipped, verified, and more.
            :param object_version_ids: Specifies whether your task report includes the new version of each object transferred into an S3 bucket. This only applies if you `enable versioning on your bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html>`_ . Keep in mind that setting this to ``INCLUDE`` can increase the duration of your task execution.
            :param overrides: Customizes the reporting level for aspects of your task report. For example, your report might generally only include errors, but you could specify that you want a list of successes and errors just for the files that DataSync attempted to delete in your destination location.
            :param report_level: Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't. - ``ERRORS_ONLY`` : A report shows what DataSync was unable to transfer, skip, verify, and delete. - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to transfer, skip, verify, and delete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                task_report_config_property = datasync.CfnTask.TaskReportConfigProperty(
                    destination=datasync.CfnTask.DestinationProperty(
                        s3=datasync.CfnTask.S3Property(
                            bucket_access_role_arn="bucketAccessRoleArn",
                            s3_bucket_arn="s3BucketArn",
                            subdirectory="subdirectory"
                        )
                    ),
                    output_type="outputType",
                
                    # the properties below are optional
                    object_version_ids="objectVersionIds",
                    overrides=datasync.CfnTask.OverridesProperty(
                        deleted=datasync.CfnTask.DeletedProperty(
                            report_level="reportLevel"
                        ),
                        skipped=datasync.CfnTask.SkippedProperty(
                            report_level="reportLevel"
                        ),
                        transferred=datasync.CfnTask.TransferredProperty(
                            report_level="reportLevel"
                        ),
                        verified=datasync.CfnTask.VerifiedProperty(
                            report_level="reportLevel"
                        )
                    ),
                    report_level="reportLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b009bd11595c3338d0fb505588fdbb9ccbeb567f140029bfcac0b346936a0fe1)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument output_type", value=output_type, expected_type=type_hints["output_type"])
                check_type(argname="argument object_version_ids", value=object_version_ids, expected_type=type_hints["object_version_ids"])
                check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
                check_type(argname="argument report_level", value=report_level, expected_type=type_hints["report_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "output_type": output_type,
            }
            if object_version_ids is not None:
                self._values["object_version_ids"] = object_version_ids
            if overrides is not None:
                self._values["overrides"] = overrides
            if report_level is not None:
                self._values["report_level"] = report_level

        @builtins.property
        def destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTask.DestinationProperty"]:
            '''Specifies the Amazon S3 bucket where DataSync uploads your task report.

            For more information, see `Task reports <https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html#task-report-access>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTask.DestinationProperty"], result)

        @builtins.property
        def output_type(self) -> builtins.str:
            '''Specifies the type of task report that you want:.

            - ``SUMMARY_ONLY`` : Provides necessary details about your task, including the number of files, objects, and directories transferred and transfer duration.
            - ``STANDARD`` : Provides complete details about your task, including a full list of files, objects, and directories that were transferred, skipped, verified, and more.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-outputtype
            '''
            result = self._values.get("output_type")
            assert result is not None, "Required property 'output_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version_ids(self) -> typing.Optional[builtins.str]:
            '''Specifies whether your task report includes the new version of each object transferred into an S3 bucket.

            This only applies if you `enable versioning on your bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html>`_ . Keep in mind that setting this to ``INCLUDE`` can increase the duration of your task execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-objectversionids
            '''
            result = self._values.get("object_version_ids")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.OverridesProperty"]]:
            '''Customizes the reporting level for aspects of your task report.

            For example, your report might generally only include errors, but you could specify that you want a list of successes and errors just for the files that DataSync attempted to delete in your destination location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-overrides
            '''
            result = self._values.get("overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTask.OverridesProperty"]], result)

        @builtins.property
        def report_level(self) -> typing.Optional[builtins.str]:
            '''Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't.

            - ``ERRORS_ONLY`` : A report shows what DataSync was unable to transfer, skip, verify, and delete.
            - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to transfer, skip, verify, and delete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-reportlevel
            '''
            result = self._values.get("report_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskReportConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.TaskScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression", "status": "status"},
    )
    class TaskScheduleProperty:
        def __init__(
            self,
            *,
            schedule_expression: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configures your AWS DataSync task to run on a `schedule <https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html>`_ (at a minimum interval of 1 hour).

            :param schedule_expression: Specifies your task schedule by using a cron expression in UTC time. For information about cron expression syntax, see the `*Amazon EventBridge User Guide* <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html>`_ .
            :param status: Specifies whether to enable or disable your task schedule. Your schedule is enabled by default, but there can be situations where you need to disable it. For example, you might need to perform maintenance on a storage system before you can begin a recurring DataSync transfer. DataSync might disable your schedule automatically if your task fails repeatedly with the same error. For more information, see the `*DataSync User Guide* <https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html#pause-task-schedule>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                task_schedule_property = datasync.CfnTask.TaskScheduleProperty(
                    schedule_expression="scheduleExpression",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bdd1c8daa067909640e521c94ab235dbc0cbd0298c594a9205908838932a520f)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schedule_expression is not None:
                self._values["schedule_expression"] = schedule_expression
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def schedule_expression(self) -> typing.Optional[builtins.str]:
            '''Specifies your task schedule by using a cron expression in UTC time.

            For information about cron expression syntax, see the `*Amazon EventBridge User Guide* <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html#cfn-datasync-task-taskschedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Specifies whether to enable or disable your task schedule.

            Your schedule is enabled by default, but there can be situations where you need to disable it. For example, you might need to perform maintenance on a storage system before you can begin a recurring DataSync transfer.

            DataSync might disable your schedule automatically if your task fails repeatedly with the same error. For more information, see the `*DataSync User Guide* <https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html#pause-task-schedule>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html#cfn-datasync-task-taskschedule-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.TransferredProperty",
        jsii_struct_bases=[],
        name_mapping={"report_level": "reportLevel"},
    )
    class TransferredProperty:
        def __init__(
            self,
            *,
            report_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The reporting level for the transferred section of your DataSync task report.

            :param report_level: Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't. - ``ERRORS_ONLY`` : A report shows what DataSync was unable to transfer. - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to transfer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-transferred.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                transferred_property = datasync.CfnTask.TransferredProperty(
                    report_level="reportLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__567e5569759125d2a549b0bdc4af58e1bd393094777e59c4cb349ddd217e5c09)
                check_type(argname="argument report_level", value=report_level, expected_type=type_hints["report_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if report_level is not None:
                self._values["report_level"] = report_level

        @builtins.property
        def report_level(self) -> typing.Optional[builtins.str]:
            '''Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't.

            - ``ERRORS_ONLY`` : A report shows what DataSync was unable to transfer.
            - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to transfer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-transferred.html#cfn-datasync-task-transferred-reportlevel
            '''
            result = self._values.get("report_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransferredProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datasync.CfnTask.VerifiedProperty",
        jsii_struct_bases=[],
        name_mapping={"report_level": "reportLevel"},
    )
    class VerifiedProperty:
        def __init__(
            self,
            *,
            report_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The reporting level for the verified section of your DataSync task report.

            :param report_level: Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't. - ``ERRORS_ONLY`` : A report shows what DataSync was unable to verify. - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to verify.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-verified.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datasync as datasync
                
                verified_property = datasync.CfnTask.VerifiedProperty(
                    report_level="reportLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__85b602e4eeecb093e03804ba0a072531ddddf4c7a2a1bbcf685fd0ff22c5bb57)
                check_type(argname="argument report_level", value=report_level, expected_type=type_hints["report_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if report_level is not None:
                self._values["report_level"] = report_level

        @builtins.property
        def report_level(self) -> typing.Optional[builtins.str]:
            '''Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't.

            - ``ERRORS_ONLY`` : A report shows what DataSync was unable to verify.
            - ``SUCCESSES_AND_ERRORS`` : A report shows what DataSync was able and unable to verify.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-verified.html#cfn-datasync-task-verified-reportlevel
            '''
            result = self._values.get("report_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VerifiedProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datasync.CfnTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_location_arn": "destinationLocationArn",
        "source_location_arn": "sourceLocationArn",
        "cloud_watch_log_group_arn": "cloudWatchLogGroupArn",
        "excludes": "excludes",
        "includes": "includes",
        "manifest_config": "manifestConfig",
        "name": "name",
        "options": "options",
        "schedule": "schedule",
        "tags": "tags",
        "task_report_config": "taskReportConfig",
    },
)
class CfnTaskProps:
    def __init__(
        self,
        *,
        destination_location_arn: builtins.str,
        source_location_arn: builtins.str,
        cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
        excludes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.FilterRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        includes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.FilterRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        manifest_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.ManifestConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.OptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.TaskScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_report_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.TaskReportConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTask``.

        :param destination_location_arn: The Amazon Resource Name (ARN) of an AWS storage resource's location.
        :param source_location_arn: Specifies the ARN of your transfer's source location.
        :param cloud_watch_log_group_arn: Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task. For more information, see `Monitoring DataSync with Amazon CloudWatch <https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html>`_ .
        :param excludes: Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see `Specifying what DataSync transfers by using filters <https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html>`_ .
        :param includes: Specifies include filters define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see `Specifying what DataSync transfers by using filters <https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html>`_ .
        :param manifest_config: The configuration of the manifest that lists the files or objects that you want DataSync to transfer. For more information, see `Specifying what DataSync transfers by using a manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html>`_ .
        :param name: Specifies the name of your task.
        :param options: Specifies your task's settings, such as preserving file metadata, verifying data integrity, among other options.
        :param schedule: Specifies a schedule for when you want your task to run. For more information, see `Scheduling your task <https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html>`_ .
        :param tags: Specifies the tags that you want to apply to your task. *Tags* are key-value pairs that help you manage, filter, and search for your DataSync resources.
        :param task_report_config: Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see `Monitoring your DataSync transfers with task reports <https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html>`_ . When using this parameter, your caller identity (the role that you're using DataSync with) must have the ``iam:PassRole`` permission. The `AWSDataSyncFullAccess <https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess>`_ policy includes this permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datasync as datasync
            
            cfn_task_props = datasync.CfnTaskProps(
                destination_location_arn="destinationLocationArn",
                source_location_arn="sourceLocationArn",
            
                # the properties below are optional
                cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                excludes=[datasync.CfnTask.FilterRuleProperty(
                    filter_type="filterType",
                    value="value"
                )],
                includes=[datasync.CfnTask.FilterRuleProperty(
                    filter_type="filterType",
                    value="value"
                )],
                manifest_config=datasync.CfnTask.ManifestConfigProperty(
                    source=datasync.CfnTask.SourceProperty(
                        s3=datasync.CfnTask.ManifestConfigSourceS3Property(
                            bucket_access_role_arn="bucketAccessRoleArn",
                            manifest_object_path="manifestObjectPath",
                            manifest_object_version_id="manifestObjectVersionId",
                            s3_bucket_arn="s3BucketArn"
                        )
                    ),
            
                    # the properties below are optional
                    action="action",
                    format="format"
                ),
                name="name",
                options=datasync.CfnTask.OptionsProperty(
                    atime="atime",
                    bytes_per_second=123,
                    gid="gid",
                    log_level="logLevel",
                    mtime="mtime",
                    object_tags="objectTags",
                    overwrite_mode="overwriteMode",
                    posix_permissions="posixPermissions",
                    preserve_deleted_files="preserveDeletedFiles",
                    preserve_devices="preserveDevices",
                    security_descriptor_copy_flags="securityDescriptorCopyFlags",
                    task_queueing="taskQueueing",
                    transfer_mode="transferMode",
                    uid="uid",
                    verify_mode="verifyMode"
                ),
                schedule=datasync.CfnTask.TaskScheduleProperty(
                    schedule_expression="scheduleExpression",
                    status="status"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                task_report_config=datasync.CfnTask.TaskReportConfigProperty(
                    destination=datasync.CfnTask.DestinationProperty(
                        s3=datasync.CfnTask.S3Property(
                            bucket_access_role_arn="bucketAccessRoleArn",
                            s3_bucket_arn="s3BucketArn",
                            subdirectory="subdirectory"
                        )
                    ),
                    output_type="outputType",
            
                    # the properties below are optional
                    object_version_ids="objectVersionIds",
                    overrides=datasync.CfnTask.OverridesProperty(
                        deleted=datasync.CfnTask.DeletedProperty(
                            report_level="reportLevel"
                        ),
                        skipped=datasync.CfnTask.SkippedProperty(
                            report_level="reportLevel"
                        ),
                        transferred=datasync.CfnTask.TransferredProperty(
                            report_level="reportLevel"
                        ),
                        verified=datasync.CfnTask.VerifiedProperty(
                            report_level="reportLevel"
                        )
                    ),
                    report_level="reportLevel"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5632ab868186e470f4d8f0c14e3f12b71107be017f54f3194a076b9da30b50d8)
            check_type(argname="argument destination_location_arn", value=destination_location_arn, expected_type=type_hints["destination_location_arn"])
            check_type(argname="argument source_location_arn", value=source_location_arn, expected_type=type_hints["source_location_arn"])
            check_type(argname="argument cloud_watch_log_group_arn", value=cloud_watch_log_group_arn, expected_type=type_hints["cloud_watch_log_group_arn"])
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument includes", value=includes, expected_type=type_hints["includes"])
            check_type(argname="argument manifest_config", value=manifest_config, expected_type=type_hints["manifest_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_report_config", value=task_report_config, expected_type=type_hints["task_report_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_location_arn": destination_location_arn,
            "source_location_arn": source_location_arn,
        }
        if cloud_watch_log_group_arn is not None:
            self._values["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
        if excludes is not None:
            self._values["excludes"] = excludes
        if includes is not None:
            self._values["includes"] = includes
        if manifest_config is not None:
            self._values["manifest_config"] = manifest_config
        if name is not None:
            self._values["name"] = name
        if options is not None:
            self._values["options"] = options
        if schedule is not None:
            self._values["schedule"] = schedule
        if tags is not None:
            self._values["tags"] = tags
        if task_report_config is not None:
            self._values["task_report_config"] = task_report_config

    @builtins.property
    def destination_location_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of an AWS storage resource's location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-destinationlocationarn
        '''
        result = self._values.get("destination_location_arn")
        assert result is not None, "Required property 'destination_location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_location_arn(self) -> builtins.str:
        '''Specifies the ARN of your transfer's source location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-sourcelocationarn
        '''
        result = self._values.get("source_location_arn")
        assert result is not None, "Required property 'source_location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.

        For more information, see `Monitoring DataSync with Amazon CloudWatch <https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-cloudwatchloggrouparn
        '''
        result = self._values.get("cloud_watch_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def excludes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTask.FilterRuleProperty]]]]:
        '''Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer.

        For more information and examples, see `Specifying what DataSync transfers by using filters <https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-excludes
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTask.FilterRuleProperty]]]], result)

    @builtins.property
    def includes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTask.FilterRuleProperty]]]]:
        '''Specifies include filters define the files, objects, and folders in your source location that you want DataSync to transfer.

        For more information and examples, see `Specifying what DataSync transfers by using filters <https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-includes
        '''
        result = self._values.get("includes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTask.FilterRuleProperty]]]], result)

    @builtins.property
    def manifest_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.ManifestConfigProperty]]:
        '''The configuration of the manifest that lists the files or objects that you want DataSync to transfer.

        For more information, see `Specifying what DataSync transfers by using a manifest <https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-manifestconfig
        '''
        result = self._values.get("manifest_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.ManifestConfigProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of your task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.OptionsProperty]]:
        '''Specifies your task's settings, such as preserving file metadata, verifying data integrity, among other options.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-options
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.OptionsProperty]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.TaskScheduleProperty]]:
        '''Specifies a schedule for when you want your task to run.

        For more information, see `Scheduling your task <https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.TaskScheduleProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the tags that you want to apply to your task.

        *Tags* are key-value pairs that help you manage, filter, and search for your DataSync resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def task_report_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.TaskReportConfigProperty]]:
        '''Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer.

        For more information, see `Monitoring your DataSync transfers with task reports <https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html>`_ .

        When using this parameter, your caller identity (the role that you're using DataSync with) must have the ``iam:PassRole`` permission. The `AWSDataSyncFullAccess <https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess>`_ policy includes this permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-taskreportconfig
        '''
        result = self._values.get("task_report_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.TaskReportConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAgent",
    "CfnAgentProps",
    "CfnLocationAzureBlob",
    "CfnLocationAzureBlobProps",
    "CfnLocationEFS",
    "CfnLocationEFSProps",
    "CfnLocationFSxLustre",
    "CfnLocationFSxLustreProps",
    "CfnLocationFSxONTAP",
    "CfnLocationFSxONTAPProps",
    "CfnLocationFSxOpenZFS",
    "CfnLocationFSxOpenZFSProps",
    "CfnLocationFSxWindows",
    "CfnLocationFSxWindowsProps",
    "CfnLocationHDFS",
    "CfnLocationHDFSProps",
    "CfnLocationNFS",
    "CfnLocationNFSProps",
    "CfnLocationObjectStorage",
    "CfnLocationObjectStorageProps",
    "CfnLocationS3",
    "CfnLocationS3Props",
    "CfnLocationSMB",
    "CfnLocationSMBProps",
    "CfnStorageSystem",
    "CfnStorageSystemProps",
    "CfnTask",
    "CfnTaskProps",
]

publication.publish()

def _typecheckingstub__d936a9373128610a07487a343ef5f669c26d2f82d825e32d371bce59b97aa93c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    activation_key: typing.Optional[builtins.str] = None,
    agent_name: typing.Optional[builtins.str] = None,
    security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81fbad3909c49b87e552d1214005285ecb6b192ba23456279698e48b81961aac(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ceb39e9063ce041ae5fa861dd0bf69001bf3c69cc12e412d36e67d3f7da074(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__487cd8023e4b2808d444a1f5c85f66a51d757299d1239cf71233c99176c0522d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4450f3881b2dffdb43cc0604c9cfd8a0efa10d69ac51ad3d1bf11d605de50a3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3397ee88e1e2dd7128616ed90dbaaeea7d67a2ae384d286cdcfaa48849d48f9c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c121bd2b79eb0fd51d5790002f0a61a6ac6a1606ce08b2d3d61b1bb196968ae(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae8ff35f7c199f1e5218a6432dc5893a46003bc8921b159534e548343397b69c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__382a2bd8de9abd26a4050c65ad2d6baa552585795b8cb589d8cc033b01c16bcd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6733a53a5c0a8ea652fdedb421d3ea702ad3e42c07f57a164d132594aefc8eb(
    *,
    activation_key: typing.Optional[builtins.str] = None,
    agent_name: typing.Optional[builtins.str] = None,
    security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a49f57a1ab4813b1537b04053be19b99e3fa8f143f30fac9d1bc72caa4ec5f2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_arns: typing.Sequence[builtins.str],
    azure_blob_authentication_type: builtins.str,
    azure_access_tier: typing.Optional[builtins.str] = None,
    azure_blob_container_url: typing.Optional[builtins.str] = None,
    azure_blob_sas_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationAzureBlob.AzureBlobSasConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    azure_blob_type: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc59f45abf5059f82345f619c384b01d137f4d49a1506da910056ac15ef819a9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebde5c22aa68229dea3796deaf496ab61b9ffcfdf6d4f56a59875e6047047203(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04d94ab53395a58893ca5e5668d51e78b5d567de304ebc1b3c8937ab5824c459(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d66037c88c30360a6dbdeedf60b7cdd8b0d971ae11fb4944eb61af92fe413080(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38eadceb910bce5de77c7dd9c218a003ad2d8b865f6b732f47b6b7fea8c1f40d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795c3fa003f02e9d97d1fae401c02ed1af3b616ece635550bbc9fd6c2e0dde05(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60754be8cb63c6569b923d0c78a823449ddaa3c5aba51833aae257e02f1bd392(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationAzureBlob.AzureBlobSasConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74328b40eb55d86e422d5f30530d28f29d1393792015d7646eb06c8819408d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__861788b0a9a32f402ab93793acdec22ae6bb15d217371b8ba36d7cb8ba33fc6b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49f572b838ff9ece4d89d77403924adeec2030197b239758db39cea71436acfb(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b97bd3f13ec4166f121eb8229b7a3322702a4782d767aca2fc1323e923cced8(
    *,
    azure_blob_sas_token: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d386b9f5845962fa66385393ccc6424f66b9aee312fecdc96fe3ec242f754bf1(
    *,
    agent_arns: typing.Sequence[builtins.str],
    azure_blob_authentication_type: builtins.str,
    azure_access_tier: typing.Optional[builtins.str] = None,
    azure_blob_container_url: typing.Optional[builtins.str] = None,
    azure_blob_sas_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationAzureBlob.AzureBlobSasConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    azure_blob_type: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2ede238fa34ab9a0ff568aeab0bbaa47ee9542611afbf58163acd201706303(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ec2_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationEFS.Ec2ConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    access_point_arn: typing.Optional[builtins.str] = None,
    efs_filesystem_arn: typing.Optional[builtins.str] = None,
    file_system_access_role_arn: typing.Optional[builtins.str] = None,
    in_transit_encryption: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__525f362005e39a7a0c870fbf4abfc0e5c277ffc6df5e1c59dc837aa27682d7b9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3212431159a669650412490f33351420b4d25f3e521ae34f0776a8c33c44638f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d49a9691cc648acec6401c31a8bd66d218ef81be6a8c7372287fd0137a541e69(
    value: typing.Union[_IResolvable_da3f097b, CfnLocationEFS.Ec2ConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a5354be840dc5932b18b5eb78c21c9212f8dfeaf26584c5369c42c79b0feda0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1daff75583eb771bbf36150a90de86f19ae11bcb1891de8abe3057537f0e6439(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b6f2d80c69bdbcb291a9018a79abaac597880c119d6d606fc8af02dd73a8289(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0148fd532364a7b64fc661f81d6f489722b42c925d8bb2ca2c363cec6d7aa6fb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c79c757570d3b36786238e89b35ce024a869534edc2665cbf1292460b498cc3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70a483245df685cb33e660b85ed2768354b191a41a3909b76b309f43c43c73e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d7739807e0941f242944e9f35ecd7849678f3d74f7a74f34b42fd7260f4cdb(
    *,
    security_group_arns: typing.Sequence[builtins.str],
    subnet_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd308e189fe63ce2cc80398d76a37684d9c1c36b8dfa1dfed227e06d9f65ca69(
    *,
    ec2_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationEFS.Ec2ConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    access_point_arn: typing.Optional[builtins.str] = None,
    efs_filesystem_arn: typing.Optional[builtins.str] = None,
    file_system_access_role_arn: typing.Optional[builtins.str] = None,
    in_transit_encryption: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a366fbae202f0039019565ac7d26837d23db858eddf6c8193ddf4bd207f597(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_group_arns: typing.Sequence[builtins.str],
    fsx_filesystem_arn: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332f63f71b2f53346897bbd853b4475cc78f7de950e12cd596388ff61046d9c9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f97bf53ea28971717bcec4e0b4b238ec382a67beac05ae5d4cec2c272e4d0dbd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99604bc3d8ba3f9cebd4d615800e9e9a5eaa9a24ac1406cc329212e19bb3f563(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f40986c7e15e37098358bbc0b06f54552260ebd0c2cbbb23d0aa7575a77572d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2de39d8f3d5835ff4125e18bd0c7dc9e8523a72a468c28a594ec8bcbcfc0280(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a21025c45a3ae349b404b0660292a1df2a3f9dfb1668c68c70eaac990ad31495(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4c1967b655fb7ba3b02e398f8b2dc61e2cb372e8e862f4aea92b2ccf89bd90(
    *,
    security_group_arns: typing.Sequence[builtins.str],
    fsx_filesystem_arn: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e90aee609011bf6205e58d539383e731c53e81e52f2c60ef5d94494c4efecc80(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_group_arns: typing.Sequence[builtins.str],
    storage_virtual_machine_arn: builtins.str,
    protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxONTAP.ProtocolProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f2c1a750537c459c40274b80eb75ffeda15c9ed3de3b01eed5b59c97b35e4bd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c959eff12bc94e8be3c884c6e634a1457d1afa3b8f64323154a19f3e7e5fe14(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43462066b9ef98956b46d8c5c9b702871e858cd735a7625c74fc7ccbcf3881a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f60908dedc90f4e4aaa149c48a33bbbbc89033f34371228431f30831e0fb33b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5733cffea1e4acc30fa46f3869492191e577ff7fb19e3b0a0964257388c93711(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationFSxONTAP.ProtocolProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a8a96a468989ae9c3368522664b5a8e7caf45b58424f818667a6642c442f18(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf18f603ac473d61e4ddeeabdd924bdda3ada2926fd940579ba552851ac8e4a6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d906f77d136eff99651e2ce7c223df26baf12fd4ff6587250dd429255fe44e40(
    *,
    mount_options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxONTAP.NfsMountOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dc53c3b8f4ac95cd4581df290c1b03f1580286e8f150e8c15513946465d8f08(
    *,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__232010cfdb13b273652e859ad8547bc7677b6700a32713cd27647e3b35759f4e(
    *,
    nfs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxONTAP.NFSProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    smb: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxONTAP.SMBProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa05e4e2966437016f666744220c772c1b0c0e2c81f8e8e7f44a5b139fc021d0(
    *,
    mount_options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxONTAP.SmbMountOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
    password: builtins.str,
    user: builtins.str,
    domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91fd30cfcc64f01817f69da9fc6b6a4e13642f15c75979166fdab51ee88f8a8e(
    *,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ce3cf4001e297ef6c59ffcd2e700197ec14104852b7d6b75aac1725cb45d8b(
    *,
    security_group_arns: typing.Sequence[builtins.str],
    storage_virtual_machine_arn: builtins.str,
    protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxONTAP.ProtocolProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ad8c513f918bb8d8381bbd62e5e1a111d39af1c2ed6ba47a729880d177982e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    protocol: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxOpenZFS.ProtocolProperty, typing.Dict[builtins.str, typing.Any]]],
    security_group_arns: typing.Sequence[builtins.str],
    fsx_filesystem_arn: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1607aef74d95939cb07d1755f55358e0d063c7dc0bb1c91110bc825233382e02(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618ba438d447571bd06af749cb3c483e174a8bf053f1381c5214c86336394ca7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddafc49b43359e47266c55b1856065646a5a0a4d1fee7e74184b46d0a9ea1323(
    value: typing.Union[_IResolvable_da3f097b, CfnLocationFSxOpenZFS.ProtocolProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1541ed866ade55559c6d5705d3e2c71e861be18522927a112e488f0495a437ce(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed3bb479112a50476f67687992c13945d7c7956773f0372592cc754ca002e2be(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dad170792efea1b233597f89fd5ab9cb0ae92aa33fc727fac7ab53c7c07c2dc7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c49d460645d98663ac93a723deb6ca797169b9d9ede4cada79adec615c02492(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfda36e06bba17b0bffc6c6a8c3817aa3805236389cc12c4dbffb61442f143c8(
    *,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2291a1530562b2a7a2c025ec9cd5ab602cc0bc08d1a9d2d8804639aec6a8489(
    *,
    mount_options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxOpenZFS.MountOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f41739d7c107eef7d64b8f86d076d7f20e79f98ab22fca2329e2030a8081468(
    *,
    nfs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxOpenZFS.NFSProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16adeb69f25af324c507b1a5b1905509ca406e488b6f1f503c1037668ea1c423(
    *,
    protocol: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationFSxOpenZFS.ProtocolProperty, typing.Dict[builtins.str, typing.Any]]],
    security_group_arns: typing.Sequence[builtins.str],
    fsx_filesystem_arn: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c93d65e558fb10f2d82a30ed92129805bd6595247629ad020c0793d238ab28(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_group_arns: typing.Sequence[builtins.str],
    user: builtins.str,
    domain: typing.Optional[builtins.str] = None,
    fsx_filesystem_arn: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543b917e94b9026d545236925ac70a71da95a62071411ad3a7a83379d3ce0dcd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a8e8a3ae5b78a07a65a6d98cd11d85b2bc6ea1356e1b5cb4ffa7d4da482b187(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627d2025f40a7ab53f282cdc8322a1d894fdfaa9a3bd70d74612c70ade3e0325(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d45f9d99683ac8fb9741da3800803485aee87f8917d4e8dc41b244517870b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__356f65660a522cc7efd2dbff7f12ba4d654cc19ff311a66ebb391fc6f659ef92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cfc208b531344d673280b57ea62e26f43f7ae28704e223829300459ed7a5ae5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebf29df57a68b0e86263f1ac5ee2f8f2c771094dfd4377bb7e540e3af1f598c7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a35bda492feb7951b7758508a280efaf76334f6397db60c3c1225de0566b628(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__602782cd2d11ed3007adaab1a6e7826b15d7a1236d0d2fa763c3a9b1471eda1a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f5ba282a9548e2767c09028be2186cfa923b38c45c6c77db774a616f6106dfd(
    *,
    security_group_arns: typing.Sequence[builtins.str],
    user: builtins.str,
    domain: typing.Optional[builtins.str] = None,
    fsx_filesystem_arn: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4e6e207e87512241da6969739eafac75aaa4606f7d5a869a5c3730ac474aba5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_arns: typing.Sequence[builtins.str],
    authentication_type: builtins.str,
    name_nodes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationHDFS.NameNodeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    block_size: typing.Optional[jsii.Number] = None,
    kerberos_keytab: typing.Optional[builtins.str] = None,
    kerberos_krb5_conf: typing.Optional[builtins.str] = None,
    kerberos_principal: typing.Optional[builtins.str] = None,
    kms_key_provider_uri: typing.Optional[builtins.str] = None,
    qop_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationHDFS.QopConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    replication_factor: typing.Optional[jsii.Number] = None,
    simple_user: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d16ad8322840db3a52346c879eb9f99bb34e8c97d2b5db9416f434c897bb3f3c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a475327a7ef18072ddcee0391d79181ad96efb93aad6484cf5ecd4adb8a5acea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589134abb411230e5151d5dbdc2d3f57049d54aa4991a0e31b28febbed363542(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1212707812d568c33e201782b49fb54b24478da5aafb6b468e2de0fce2aa31bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a76145fef05ad13cf6d623dec2e81ad7c19c154ecd30d8aae3a73e81c6576491(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLocationHDFS.NameNodeProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf27e0cd386bf2173a19ecd724060c7f84d674c6012a12d7d80434a642f7669(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6057391a851d073ac6f1367fe8fd1c48123fb8ce205d25a7b62dab5b2526403(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27c3b0c34aebfd29ee44b9714b36c3784836c4bafab215880054ced544ffceb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb3b88f77d23303189ba83b98eb4ba536946b54369bfcbde6934d23750d702d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b391dcf3cbfdc1b073c64fdd7b6cf479a7438a0decfd4019ee6bed21145ed395(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eada24423cf34a46defb2fb08ff49d30f58ea6d6486c0e6ccf15fc65da913ff(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationHDFS.QopConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3ee4cc2c6ca661c5acfc5a8bd53136b2b61234dbf0df2632f2355ceb274c2df(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cacb880eb4be9b59946ed860edadb54c1921088c8a1676c2966339de1ad488d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f88a655a03c9f1a9a7cf557e70ba70d9c5e3ea34a07249c483f3de0111a360(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aae452f9b71c01ce6062b4ea9224245a9cc1780c588d392319b30c53a0bc99d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff067b203598a07a938143f104acc0c36107b9a8f09480a3d654c038b1737385(
    *,
    hostname: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf9687c3478faca4ca6f46765e18256315fbf00b11876af5dad6a28a53a6ef4b(
    *,
    data_transfer_protection: typing.Optional[builtins.str] = None,
    rpc_protection: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acd7db2bc2dffe624daa5332f50443b11a0c0e3a43b2ecd71e380ba6c4e4385c(
    *,
    agent_arns: typing.Sequence[builtins.str],
    authentication_type: builtins.str,
    name_nodes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationHDFS.NameNodeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    block_size: typing.Optional[jsii.Number] = None,
    kerberos_keytab: typing.Optional[builtins.str] = None,
    kerberos_krb5_conf: typing.Optional[builtins.str] = None,
    kerberos_principal: typing.Optional[builtins.str] = None,
    kms_key_provider_uri: typing.Optional[builtins.str] = None,
    qop_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationHDFS.QopConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    replication_factor: typing.Optional[jsii.Number] = None,
    simple_user: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d069ca05c42fb87f307cca12e7ca62685374e8479c3259d679c41b7c9e2b1aef(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    on_prem_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationNFS.OnPremConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    mount_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationNFS.MountOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_hostname: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40df789cb6a010f01823fe85f7288bf1ac70fb78042afb433c6d7133870bda33(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c316588e44bcf94ddca8831976b72238cd17eb18a3c521d497fc44d71155f2aa(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef5244b8ff59527535d3ba0996f08c461f6affc766845b00ae3805171907b04c(
    value: typing.Union[_IResolvable_da3f097b, CfnLocationNFS.OnPremConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53e27778ea596fd0d4e8ad60113269d0f0aac45137d89e2a99be7a5c30e4fb6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationNFS.MountOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db78699845c639e22a20c2990d72ef74b39b3dfd71d7723e31c7fb2f10aafea0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f230ca1995ad30becaf0c71d285ca8bab104210d7223f477c8537757ea6e972b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6775dcca43d86f1ff2a8795efb1205f09fdcee773716c549b06acac462432bcd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e2486d89e028a5b89b8598f356d7e2a5a050dc22284ebbeb5c3c0a76d928758(
    *,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf52296f64754ae5def817f69206eb64641343e40369d74f7a3de14644073deb(
    *,
    agent_arns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f51fa3c0c693bb5826cc200004a0b1f04c19f70726432f02d5a4443185b49b1(
    *,
    on_prem_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationNFS.OnPremConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    mount_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationNFS.MountOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_hostname: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6afc4365b2246b057f5b97e5d62cc10a54cff3be74dae8a9bb184f54bec37125(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_arns: typing.Sequence[builtins.str],
    access_key: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    secret_key: typing.Optional[builtins.str] = None,
    server_certificate: typing.Optional[builtins.str] = None,
    server_hostname: typing.Optional[builtins.str] = None,
    server_port: typing.Optional[jsii.Number] = None,
    server_protocol: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61e61baf3961601d7838c5023c80bbf458fad24f9dd8cf4006490f1eccb76e8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1891041f95311e30edfb4c440a05c41fa9ad1fb130ed42400500c57858f12085(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af42e226779e989fe6f4a4e7403f44c0a7f4048f3185f2bd0fdbbe0f191363ec(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bab62678e3c33f0a6edfb878fe17304321977ba3655bb45d3504aa54de9dadc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf6330b6613abe7771487991e7b16db5686e2242ecdbb63f4ef7e946766b4ad(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cdc4af71140887c9702de30a25cd730dad08983bb31931dbba45c838b77c638(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe1a19b9b619faa0e6cc523990a61cf54a53b8ce9dee6069266a8bba0751c3c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa6bb2a89a6471b8beee100b564375c694c575449e9d04bc9ede967e993738b2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26f25c8e19d015decf49fc7f700522b335ae1d335eb9ab2a8043361791c53294(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d86ff038021519c6b78d57b7c787246ca9822b5a3abe776e0b1a8086f5b1c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3632c6248d8275b49a1adcc3708b5bb2fe80efcf6c9244f62d25487bffc9a210(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c7a3d48757bffde04fd1015e50d6672207d2522eec04091eebdb3ac177fb39a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d542a26da4e93d9d103e234c98ed367d8b6bea7d295017a32de5525e1ec22b45(
    *,
    agent_arns: typing.Sequence[builtins.str],
    access_key: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    secret_key: typing.Optional[builtins.str] = None,
    server_certificate: typing.Optional[builtins.str] = None,
    server_hostname: typing.Optional[builtins.str] = None,
    server_port: typing.Optional[jsii.Number] = None,
    server_protocol: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffb78212d43943a47f3d3a5e10125952e22d4754b8512843cf88c7c55f6514ee(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    s3_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationS3.S3ConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    s3_bucket_arn: typing.Optional[builtins.str] = None,
    s3_storage_class: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a187d5155efd29d831744d9f56a48eb5fb642e6480113807dc45702657631e2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c7d3981be7393042939c70bae0b4fb0e4420f2649a9d523d80810c5b47361e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a8e39b836dbbdb49d0bd113962d59b27158d2ab86e97500f5dda21fc6f2d70(
    value: typing.Union[_IResolvable_da3f097b, CfnLocationS3.S3ConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49ff9004432edb3637a4fd05fa9fd3158f9d7b6094ac54156943f7d6dd1d5047(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a7d8ab492fdfb044b0e230d97fa1965715c74f4b35ab0403115732834d1e49(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2ceccded2a2b37bcf132c0f563dba3e5c80cc42a7c55df19724af65ac2d8a4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d6b2dd8b444ebab79ed4aae8987dfed0864cb4e3663bdfd36a643d72264608e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce8f8003886002426ef5ce44b74ed398416c8d59b6cf5b10816d2ddc11294b14(
    *,
    bucket_access_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1b9799e0fad9e71975d14e754aeb8ef0b5f52fcedcbabc328afae8c4a4afaa5(
    *,
    s3_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationS3.S3ConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    s3_bucket_arn: typing.Optional[builtins.str] = None,
    s3_storage_class: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bafa6101408857d4661895c88a8c9839da8768aa52e07d3f2889a4f27c1cab7d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_arns: typing.Sequence[builtins.str],
    user: builtins.str,
    domain: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationSMB.MountOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    password: typing.Optional[builtins.str] = None,
    server_hostname: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88508f3486fa9166f7847b61eef5d9a046ed0dae7d7da9e27f6f83d1f0019490(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__976a351d3a1231a7633ae322e4c36b99634cc2da556bf4d8eea9837c359833bb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ee66e7697fa761c39fe555b5fae211e45dedf33951d3701b7b6389dd8452b6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9112e8b177e52fbd055f221015988972f906f8c7291b4a1992bb1656cd033faa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__645408d26d2b2afb233a71045cf02aab2ca6bb9a00176ca0b16d93e1e633bf92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9983585f73509aeb431e7337689500eb00129c754b73a4ef4022bebcd1bbc1c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLocationSMB.MountOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__188ea071908278e310db901e923a61e61176a5283d6d637c7cf24940f4af9a3c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91814040ef607edb46eb6b7f17c10d591505c88dcd81419dd0065a7c2520ec99(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b24807ca878b348d6926b1d8578692f8c738074f4ba29ed17cb920e40bb4a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b48314ac3635761aa21132da0f199200c2b741ddeca4e34176ee47fde9d19e47(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__465428a8e33c33a3926562e4b4d3d671db7fc7f2d1ff95443e6224cb280e8c00(
    *,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20670d7cb18baa1155ccc397df310282442d51b95170ab568e5c0a9cbea5bc8(
    *,
    agent_arns: typing.Sequence[builtins.str],
    user: builtins.str,
    domain: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLocationSMB.MountOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    password: typing.Optional[builtins.str] = None,
    server_hostname: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd03aea3d03c00385e272f326dc093d0575219e3eac09a9f89062f9453a9360f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_arns: typing.Sequence[builtins.str],
    server_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageSystem.ServerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    system_type: builtins.str,
    cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    server_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageSystem.ServerCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d30237b704bab23311aad893ff50107b6fc1840c11f7ab06f9fd41ffce46d0d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b9c192e8b33247af58d9ec7498864f379be5476b6c0a2aeb98684bc257c348(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c1b3e5cd2d7dd98537d8ad2c7deae28f00b5d6d23089b99cb0768ef5ca4d7f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81366a44879ecfffc2cf1020a13667d2ef18466bde35cc8a36864bab3668086b(
    value: typing.Union[_IResolvable_da3f097b, CfnStorageSystem.ServerConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac346e347fbe1b4d60467d3562a6b070e1ed3e50a18844309f094f5f94cb7f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8cf99420b818e4ec735e8ef96836c7c265a5bb74331a73d84e9fc56a6321299(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__764666a950d4d83875874f1d9312ef4c5d98748fc51fe8f1dc9c8cf696e4e0bd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f52a2f2a6197dee934b3eaad41d0b7cc429e508ed4c3d4437b45f339ffd8712(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStorageSystem.ServerCredentialsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f06b57402f5a745b22a5a454fa8563a935276c499111bb78103406214b07c52(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2d9d38924c8714fdacccf65a04ce2f4670647a35b1330abeacb71b09b32c66(
    *,
    server_hostname: builtins.str,
    server_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aca605fb52bb6e32c26164545155c20da0e4d47eff8787d0c19d543d3f0f293(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07c9f88707493efc0c6204abeacfb93dcb4bfdc339feb06b9cedb3c14e549a6(
    *,
    agent_arns: typing.Sequence[builtins.str],
    server_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageSystem.ServerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    system_type: builtins.str,
    cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    server_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageSystem.ServerCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9add9673a1f0ceb078949e967bce91066ff7e0441dae95d55c11c4a503a397a6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_location_arn: builtins.str,
    source_location_arn: builtins.str,
    cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
    excludes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.FilterRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    includes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.FilterRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    manifest_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.ManifestConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.OptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.TaskScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_report_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.TaskReportConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3be7cc30ea459e593fff3fb2223f039edaac10f8cf48a8f35f3ea41ae0a0ac99(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fbe8c198a5a1427e6615104f061ae888f969b7fa0c0a6ed3761dab32c01d9ad(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c829157af3cc4eaa91bd0ad747876d59f15cb71ac8ca56cbf9c19eae4bf9f086(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ade222686ff2f8ad1e7e9582615e0d6dec7ef562c42e32823bf1637619af7b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5688467482337659d3d0d35a3798391a47635ed6dc628a2cfa41b22b61d0abe7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acacc184cead1f95fccb09d6e2d3e2f3763099227a59edf6a76e8128856fc021(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTask.FilterRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b70b42cfb53e13801c9b46a0aeb316cf7696061c5b7fc11b20c7970679838adb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTask.FilterRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adfc26e9a88359e12066dd2ec9b2a9e0a61fb79f73189fa8a39e637687c9fa9c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.ManifestConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de210bcc8ac65745973f2b8e5143c561a12afe1f24163e2b50a4fe61574c7317(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155643afb5f1ecdb689d1809d2d2388ec39615a2be33d1719f3b98ba2e76677d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.OptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc267a8182541bd31db0c914ab3030d3b13f68b424b8e312a7b9267e3b0e4b4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.TaskScheduleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6a7067dff337df84908e53f4652767faada60769f6c9d1eed4c84d05c1d5126(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ecaf368f7ae42942552393e7a68a01ddc8712caa5620400a489d0b07baae6e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTask.TaskReportConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f037d4931daef78ea8657014c8257621eda14339f1dc65a4f3763703e838d7dd(
    *,
    report_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be6e4582c5e377e943fda0f71516c06eaa109c591ef7c38d5feb106fed3d93d8(
    *,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.S3Property, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2957bcb9b505b6af4afc512d05d4225e97bb106c72da06526a6a27ec87040de(
    *,
    filter_type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24f392dd164095fff95d497fcd80fd8e99a252d97a070e9cb64573100cdcc65c(
    *,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    action: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d8718794bcb3bdc90c54997b7600d13961852c4adddc60005e8bf3016ef3f8(
    *,
    bucket_access_role_arn: typing.Optional[builtins.str] = None,
    manifest_object_path: typing.Optional[builtins.str] = None,
    manifest_object_version_id: typing.Optional[builtins.str] = None,
    s3_bucket_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7557db697c0c06b71a63bdcbecc24fb94bbe4de1de1980fd9b1a7e36f454ea9(
    *,
    atime: typing.Optional[builtins.str] = None,
    bytes_per_second: typing.Optional[jsii.Number] = None,
    gid: typing.Optional[builtins.str] = None,
    log_level: typing.Optional[builtins.str] = None,
    mtime: typing.Optional[builtins.str] = None,
    object_tags: typing.Optional[builtins.str] = None,
    overwrite_mode: typing.Optional[builtins.str] = None,
    posix_permissions: typing.Optional[builtins.str] = None,
    preserve_deleted_files: typing.Optional[builtins.str] = None,
    preserve_devices: typing.Optional[builtins.str] = None,
    security_descriptor_copy_flags: typing.Optional[builtins.str] = None,
    task_queueing: typing.Optional[builtins.str] = None,
    transfer_mode: typing.Optional[builtins.str] = None,
    uid: typing.Optional[builtins.str] = None,
    verify_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e46e186c62c84fedcf5320f54dff34c1ed74183d1e3e19905ddb4f42bdf47e(
    *,
    deleted: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.DeletedProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    skipped: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.SkippedProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    transferred: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.TransferredProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    verified: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.VerifiedProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e126e77ec6892ccad16cb5774367950b600108005d5958e118340b3e757dd6(
    *,
    bucket_access_role_arn: typing.Optional[builtins.str] = None,
    s3_bucket_arn: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c18544378625bf9f1fbb6beae21b7f0068188b1f7befe07dd931ccd6703d499(
    *,
    report_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648d2c1cae7d2043ba70966584d1164b3b2f9700f7b684da9f7e31f727c3d14d(
    *,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.ManifestConfigSourceS3Property, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b009bd11595c3338d0fb505588fdbb9ccbeb567f140029bfcac0b346936a0fe1(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    output_type: builtins.str,
    object_version_ids: typing.Optional[builtins.str] = None,
    overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.OverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    report_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdd1c8daa067909640e521c94ab235dbc0cbd0298c594a9205908838932a520f(
    *,
    schedule_expression: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__567e5569759125d2a549b0bdc4af58e1bd393094777e59c4cb349ddd217e5c09(
    *,
    report_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b602e4eeecb093e03804ba0a072531ddddf4c7a2a1bbcf685fd0ff22c5bb57(
    *,
    report_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5632ab868186e470f4d8f0c14e3f12b71107be017f54f3194a076b9da30b50d8(
    *,
    destination_location_arn: builtins.str,
    source_location_arn: builtins.str,
    cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
    excludes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.FilterRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    includes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.FilterRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    manifest_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.ManifestConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.OptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.TaskScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_report_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTask.TaskReportConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
