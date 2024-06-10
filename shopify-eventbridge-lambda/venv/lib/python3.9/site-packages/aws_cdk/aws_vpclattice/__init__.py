'''
# AWS::VpcLattice Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_vpclattice as vpclattice
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for VpcLattice construct libraries](https://constructs.dev/search?q=vpclattice)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::VpcLattice resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_VpcLattice.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::VpcLattice](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_VpcLattice.html).

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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAccessLogSubscription(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnAccessLogSubscription",
):
    '''Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose.

    The service network owner can use the access logs to audit the services in the network. The service network owner can only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see `Access logs <https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html>`_ in the *Amazon VPC Lattice User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html
    :cloudformationResource: AWS::VpcLattice::AccessLogSubscription
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        cfn_access_log_subscription = vpclattice.CfnAccessLogSubscription(self, "MyCfnAccessLogSubscription",
            destination_arn="destinationArn",
        
            # the properties below are optional
            resource_identifier="resourceIdentifier",
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
        destination_arn: builtins.str,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_arn: The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.
        :param resource_identifier: The ID or Amazon Resource Name (ARN) of the service network or service.
        :param tags: The tags for the access log subscription.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1e4f257245d8e5be92083145da5c0b7311cde5a905b65c5cb20fb0c7230032)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessLogSubscriptionProps(
            destination_arn=destination_arn,
            resource_identifier=resource_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b373a2103376ee17034d5f8a2bd66281964526c897621d59f595a7ee710dece)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f207b1387515fc7caa56e4c3c30125161e739b43f33921086c670ed7af78619e)
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
        '''The Amazon Resource Name (ARN) of the access log subscription.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the access log subscription.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the access log subscription.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceId")
    def attr_resource_id(self) -> builtins.str:
        '''The ID of the service network or service.

        :cloudformationAttribute: ResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceId"))

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
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the destination.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationArn"))

    @destination_arn.setter
    def destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__880b45928aa837a0dba3740b58b3250033476ee4e3d14b774b01c4cd2d224862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service network or service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b93aeac48124e92f9f09dd3e99f9ef8ac5e9d002fe64dea86b3d7700ae862f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the access log subscription.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f88ce1faaa39f21f51b79668a87b932a07532be6cdddad83e4090e05f9de003e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnAccessLogSubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_arn": "destinationArn",
        "resource_identifier": "resourceIdentifier",
        "tags": "tags",
    },
)
class CfnAccessLogSubscriptionProps:
    def __init__(
        self,
        *,
        destination_arn: builtins.str,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessLogSubscription``.

        :param destination_arn: The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.
        :param resource_identifier: The ID or Amazon Resource Name (ARN) of the service network or service.
        :param tags: The tags for the access log subscription.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            cfn_access_log_subscription_props = vpclattice.CfnAccessLogSubscriptionProps(
                destination_arn="destinationArn",
            
                # the properties below are optional
                resource_identifier="resourceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7551e4dc1730a5c7bf48ba5c2eccbe95ed6914a39663f70c2dc1846465e8eb40)
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_arn": destination_arn,
        }
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the destination.

        The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html#cfn-vpclattice-accesslogsubscription-destinationarn
        '''
        result = self._values.get("destination_arn")
        assert result is not None, "Required property 'destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service network or service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html#cfn-vpclattice-accesslogsubscription-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the access log subscription.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html#cfn-vpclattice-accesslogsubscription-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessLogSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAuthPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnAuthPolicy",
):
    '''Creates or updates the auth policy. The policy string in JSON must not contain newlines or blank lines.

    For more information, see `Auth policies <https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html>`_ in the *Amazon VPC Lattice User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-authpolicy.html
    :cloudformationResource: AWS::VpcLattice::AuthPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        # policy: Any
        
        cfn_auth_policy = vpclattice.CfnAuthPolicy(self, "MyCfnAuthPolicy",
            policy=policy,
            resource_identifier="resourceIdentifier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy: typing.Any,
        resource_identifier: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy: The auth policy.
        :param resource_identifier: The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc7f80c1c8d027e6648f29dec237037cc235db1d8d50ebf4422488fb91b8baf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAuthPolicyProps(
            policy=policy, resource_identifier=resource_identifier
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5f70c44b3f60fa4c4dc9571d48bccab272ae2d8e0388211e0c37b15b6bb398b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77adb13a1a8a12ce61a7ed6ec7e7cb8bb87b99d67e87c3dc791a7287c4814c5c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the auth policy.

        The auth policy is only active when the auth type is set to ``AWS _IAM`` . If you provide a policy, then authentication and authorization decisions are made based on this policy and the client's IAM policy. If the auth type is ``NONE`` , then any auth policy you provide will remain inactive.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''The auth policy.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17ec53a4ae132f699e3368133cd6066a7924febd9eaadf1625f077db673021d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> builtins.str:
        '''The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2514bd99a036fd72228bf57ad953594909d7d395566fdbeb7ff5aff3293879f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnAuthPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy": "policy", "resource_identifier": "resourceIdentifier"},
)
class CfnAuthPolicyProps:
    def __init__(
        self,
        *,
        policy: typing.Any,
        resource_identifier: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnAuthPolicy``.

        :param policy: The auth policy.
        :param resource_identifier: The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-authpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            # policy: Any
            
            cfn_auth_policy_props = vpclattice.CfnAuthPolicyProps(
                policy=policy,
                resource_identifier="resourceIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d3fae469a4114f5041ab337d4b2b87c6bebd93bfab70112ebf9e83154ff99a2)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
            "resource_identifier": resource_identifier,
        }

    @builtins.property
    def policy(self) -> typing.Any:
        '''The auth policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-authpolicy.html#cfn-vpclattice-authpolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_identifier(self) -> builtins.str:
        '''The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-authpolicy.html#cfn-vpclattice-authpolicy-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        assert result is not None, "Required property 'resource_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAuthPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnListener(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnListener",
):
    '''Creates a listener for a service.

    Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see `Listeners <https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html>`_ in the *Amazon VPC Lattice User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html
    :cloudformationResource: AWS::VpcLattice::Listener
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        cfn_listener = vpclattice.CfnListener(self, "MyCfnListener",
            default_action=vpclattice.CfnListener.DefaultActionProperty(
                fixed_response=vpclattice.CfnListener.FixedResponseProperty(
                    status_code=123
                ),
                forward=vpclattice.CfnListener.ForwardProperty(
                    target_groups=[vpclattice.CfnListener.WeightedTargetGroupProperty(
                        target_group_identifier="targetGroupIdentifier",
        
                        # the properties below are optional
                        weight=123
                    )]
                )
            ),
            protocol="protocol",
        
            # the properties below are optional
            name="name",
            port=123,
            service_identifier="serviceIdentifier",
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
        default_action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnListener.DefaultActionProperty", typing.Dict[builtins.str, typing.Any]]],
        protocol: builtins.str,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        service_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param default_action: The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.
        :param protocol: The listener protocol.
        :param name: The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param port: The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.
        :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
        :param tags: The tags for the listener.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf0492fe381e6c540d4fceb6599cf5162be861921ce004b402eda7520043896)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnListenerProps(
            default_action=default_action,
            protocol=protocol,
            name=name,
            port=port,
            service_identifier=service_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25b05e2b4b011a9e577c8e7138d4c3dd6e9ec07662ecaaf676372223833cb5b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5715a8b3b39f5a4c8c946b85c67be15dcfc7edfb2b226908322e417d9d0bd31)
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
        '''The Amazon Resource Name (ARN) of the listener.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the listener.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceArn")
    def attr_service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the service.

        :cloudformationAttribute: ServiceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceId")
    def attr_service_id(self) -> builtins.str:
        '''The ID of the service.

        :cloudformationAttribute: ServiceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceId"))

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
    @jsii.member(jsii_name="defaultAction")
    def default_action(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnListener.DefaultActionProperty"]:
        '''The action for the default rule.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnListener.DefaultActionProperty"], jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnListener.DefaultActionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1229fc3c4aaabfa1f9070833cc86ddb5be622124d223b483013096dc0aa21c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        '''The listener protocol.'''
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be640f5e33aaca4e3b3006d7b10a59a023e68cde6cfbeb0bfd196b5c45d669d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the listener.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104c1d020e852a1a0976b78cd610d4d052759087e8b62439928254eafc6bb997)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The listener port.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a0149fd9aab80b3782107ecd9c41ff0650b7a79a7f9ac61e250a4364883c4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="serviceIdentifier")
    def service_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceIdentifier"))

    @service_identifier.setter
    def service_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d439d803b5f48fef5e4cb28a8126bd2873fb6db421fc78917613a39ba02471fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the listener.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bdb1d86bfde2da64bd233fa7351069e7394020e32eca07770f43cd1b50cca3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnListener.DefaultActionProperty",
        jsii_struct_bases=[],
        name_mapping={"fixed_response": "fixedResponse", "forward": "forward"},
    )
    class DefaultActionProperty:
        def __init__(
            self,
            *,
            fixed_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnListener.FixedResponseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            forward: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnListener.ForwardProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The action for the default rule.

            Each listener has a default rule. The default rule is used if no other rules match.

            :param fixed_response: Describes an action that returns a custom HTTP response.
            :param forward: Describes a forward action. You can use forward actions to route requests to one or more target groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-defaultaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                default_action_property = vpclattice.CfnListener.DefaultActionProperty(
                    fixed_response=vpclattice.CfnListener.FixedResponseProperty(
                        status_code=123
                    ),
                    forward=vpclattice.CfnListener.ForwardProperty(
                        target_groups=[vpclattice.CfnListener.WeightedTargetGroupProperty(
                            target_group_identifier="targetGroupIdentifier",
                
                            # the properties below are optional
                            weight=123
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6602b39b19cadd1593258c7a69267d1af5d7fc891a209bfc3d9044363f099466)
                check_type(argname="argument fixed_response", value=fixed_response, expected_type=type_hints["fixed_response"])
                check_type(argname="argument forward", value=forward, expected_type=type_hints["forward"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if fixed_response is not None:
                self._values["fixed_response"] = fixed_response
            if forward is not None:
                self._values["forward"] = forward

        @builtins.property
        def fixed_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnListener.FixedResponseProperty"]]:
            '''Describes an action that returns a custom HTTP response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-defaultaction.html#cfn-vpclattice-listener-defaultaction-fixedresponse
            '''
            result = self._values.get("fixed_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnListener.FixedResponseProperty"]], result)

        @builtins.property
        def forward(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnListener.ForwardProperty"]]:
            '''Describes a forward action.

            You can use forward actions to route requests to one or more target groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-defaultaction.html#cfn-vpclattice-listener-defaultaction-forward
            '''
            result = self._values.get("forward")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnListener.ForwardProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnListener.FixedResponseProperty",
        jsii_struct_bases=[],
        name_mapping={"status_code": "statusCode"},
    )
    class FixedResponseProperty:
        def __init__(self, *, status_code: jsii.Number) -> None:
            '''Describes an action that returns a custom HTTP response.

            :param status_code: The HTTP response code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-fixedresponse.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                fixed_response_property = vpclattice.CfnListener.FixedResponseProperty(
                    status_code=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76b0a5cea9cf961398e2abd115a12a0d1717ccabd032d36586e85319edd6e147)
                check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status_code": status_code,
            }

        @builtins.property
        def status_code(self) -> jsii.Number:
            '''The HTTP response code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-fixedresponse.html#cfn-vpclattice-listener-fixedresponse-statuscode
            '''
            result = self._values.get("status_code")
            assert result is not None, "Required property 'status_code' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FixedResponseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnListener.ForwardProperty",
        jsii_struct_bases=[],
        name_mapping={"target_groups": "targetGroups"},
    )
    class ForwardProperty:
        def __init__(
            self,
            *,
            target_groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnListener.WeightedTargetGroupProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The forward action.

            Traffic that matches the rule is forwarded to the specified target groups.

            :param target_groups: The target groups. Traffic matching the rule is forwarded to the specified target groups. With forward actions, you can assign a weight that controls the prioritization and selection of each target group. This means that requests are distributed to individual target groups based on their weights. For example, if two target groups have the same weight, each target group receives half of the traffic. The default value is 1. This means that if only one target group is provided, there is no need to set the weight; 100% of the traffic goes to that target group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-forward.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                forward_property = vpclattice.CfnListener.ForwardProperty(
                    target_groups=[vpclattice.CfnListener.WeightedTargetGroupProperty(
                        target_group_identifier="targetGroupIdentifier",
                
                        # the properties below are optional
                        weight=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9093fece335bbe1a3446db4db253cf7d0a348828e72e6455586ea506df70caa)
                check_type(argname="argument target_groups", value=target_groups, expected_type=type_hints["target_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_groups": target_groups,
            }

        @builtins.property
        def target_groups(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnListener.WeightedTargetGroupProperty"]]]:
            '''The target groups.

            Traffic matching the rule is forwarded to the specified target groups. With forward actions, you can assign a weight that controls the prioritization and selection of each target group. This means that requests are distributed to individual target groups based on their weights. For example, if two target groups have the same weight, each target group receives half of the traffic.

            The default value is 1. This means that if only one target group is provided, there is no need to set the weight; 100% of the traffic goes to that target group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-forward.html#cfn-vpclattice-listener-forward-targetgroups
            '''
            result = self._values.get("target_groups")
            assert result is not None, "Required property 'target_groups' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnListener.WeightedTargetGroupProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ForwardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnListener.WeightedTargetGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_group_identifier": "targetGroupIdentifier",
            "weight": "weight",
        },
    )
    class WeightedTargetGroupProperty:
        def __init__(
            self,
            *,
            target_group_identifier: builtins.str,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the weight of a target group.

            :param target_group_identifier: The ID of the target group.
            :param weight: Only required if you specify multiple target groups for a forward action. The weight determines how requests are distributed to the target group. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group. If there's only one target group specified, then the default value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-weightedtargetgroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                weighted_target_group_property = vpclattice.CfnListener.WeightedTargetGroupProperty(
                    target_group_identifier="targetGroupIdentifier",
                
                    # the properties below are optional
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9c09b0cb0878b1a32d785c3518fc1c21913c2ec5370c786f57403db8cff4d43e)
                check_type(argname="argument target_group_identifier", value=target_group_identifier, expected_type=type_hints["target_group_identifier"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_group_identifier": target_group_identifier,
            }
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def target_group_identifier(self) -> builtins.str:
            '''The ID of the target group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-weightedtargetgroup.html#cfn-vpclattice-listener-weightedtargetgroup-targetgroupidentifier
            '''
            result = self._values.get("target_group_identifier")
            assert result is not None, "Required property 'target_group_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''Only required if you specify multiple target groups for a forward action.

            The weight determines how requests are distributed to the target group. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group. If there's only one target group specified, then the default value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-weightedtargetgroup.html#cfn-vpclattice-listener-weightedtargetgroup-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WeightedTargetGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnListenerProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_action": "defaultAction",
        "protocol": "protocol",
        "name": "name",
        "port": "port",
        "service_identifier": "serviceIdentifier",
        "tags": "tags",
    },
)
class CfnListenerProps:
    def __init__(
        self,
        *,
        default_action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnListener.DefaultActionProperty, typing.Dict[builtins.str, typing.Any]]],
        protocol: builtins.str,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        service_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnListener``.

        :param default_action: The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.
        :param protocol: The listener protocol.
        :param name: The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param port: The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.
        :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
        :param tags: The tags for the listener.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            cfn_listener_props = vpclattice.CfnListenerProps(
                default_action=vpclattice.CfnListener.DefaultActionProperty(
                    fixed_response=vpclattice.CfnListener.FixedResponseProperty(
                        status_code=123
                    ),
                    forward=vpclattice.CfnListener.ForwardProperty(
                        target_groups=[vpclattice.CfnListener.WeightedTargetGroupProperty(
                            target_group_identifier="targetGroupIdentifier",
            
                            # the properties below are optional
                            weight=123
                        )]
                    )
                ),
                protocol="protocol",
            
                # the properties below are optional
                name="name",
                port=123,
                service_identifier="serviceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2abd654d29759383ba4227953efda14c5f7db6190ad40176eb92bfbb7ccc5693)
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument service_identifier", value=service_identifier, expected_type=type_hints["service_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_action": default_action,
            "protocol": protocol,
        }
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if service_identifier is not None:
            self._values["service_identifier"] = service_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def default_action(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnListener.DefaultActionProperty]:
        '''The action for the default rule.

        Each listener has a default rule. The default rule is used if no other rules match.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-defaultaction
        '''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnListener.DefaultActionProperty], result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''The listener protocol.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the listener.

        A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.

        If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The listener port.

        You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-serviceidentifier
        '''
        result = self._values.get("service_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the listener.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnListenerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnResourcePolicy",
):
    '''Retrieves information about the resource policy.

    The resource policy is an IAM policy created on behalf of the resource owner when they share a resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcepolicy.html
    :cloudformationResource: AWS::VpcLattice::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        # policy: Any
        
        cfn_resource_policy = vpclattice.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            policy=policy,
            resource_arn="resourceArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy: typing.Any,
        resource_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy: The Amazon Resource Name (ARN) of the service network or service.
        :param resource_arn: An IAM policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cc9008c3f7ccae7d54d444c5b5dcc1b03b4db009ad23c4a5ed74863b84b8360)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(policy=policy, resource_arn=resource_arn)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f59c385ec0fb1e5259ddbe4dcf2dc2f9536688a56ee6370da1f2fc23f2c1c63b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__06094face44c3f8ef3bb0ce5b6a09f5384d137bb913e2b9c1f4b816492211e25)
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
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''The Amazon Resource Name (ARN) of the service network or service.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2222735d3aa86622d6c42b8990fc3cacd9a757664d0c3b751cabcab6a2a8766e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''An IAM policy.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ed10d5f1b65a1ffbcbbe61eb60ea82b7e503a39f49b95b7c028aaabc889b94c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy": "policy", "resource_arn": "resourceArn"},
)
class CfnResourcePolicyProps:
    def __init__(self, *, policy: typing.Any, resource_arn: builtins.str) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param policy: The Amazon Resource Name (ARN) of the service network or service.
        :param resource_arn: An IAM policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            # policy: Any
            
            cfn_resource_policy_props = vpclattice.CfnResourcePolicyProps(
                policy=policy,
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1737436eeafbe996ee74ec168a6fb4cb8dd64c1c2bcb91c9ba68d5dc234bb69e)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
            "resource_arn": resource_arn,
        }

    @builtins.property
    def policy(self) -> typing.Any:
        '''The Amazon Resource Name (ARN) of the service network or service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcepolicy.html#cfn-vpclattice-resourcepolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''An IAM policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcepolicy.html#cfn-vpclattice-resourcepolicy-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule",
):
    '''Creates a listener rule.

    Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see `Listener rules <https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules>`_ in the *Amazon VPC Lattice User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html
    :cloudformationResource: AWS::VpcLattice::Rule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        cfn_rule = vpclattice.CfnRule(self, "MyCfnRule",
            action=vpclattice.CfnRule.ActionProperty(
                fixed_response=vpclattice.CfnRule.FixedResponseProperty(
                    status_code=123
                ),
                forward=vpclattice.CfnRule.ForwardProperty(
                    target_groups=[vpclattice.CfnRule.WeightedTargetGroupProperty(
                        target_group_identifier="targetGroupIdentifier",
        
                        # the properties below are optional
                        weight=123
                    )]
                )
            ),
            match=vpclattice.CfnRule.MatchProperty(
                http_match=vpclattice.CfnRule.HttpMatchProperty(
                    header_matches=[vpclattice.CfnRule.HeaderMatchProperty(
                        match=vpclattice.CfnRule.HeaderMatchTypeProperty(
                            contains="contains",
                            exact="exact",
                            prefix="prefix"
                        ),
                        name="name",
        
                        # the properties below are optional
                        case_sensitive=False
                    )],
                    method="method",
                    path_match=vpclattice.CfnRule.PathMatchProperty(
                        match=vpclattice.CfnRule.PathMatchTypeProperty(
                            exact="exact",
                            prefix="prefix"
                        ),
        
                        # the properties below are optional
                        case_sensitive=False
                    )
                )
            ),
            priority=123,
        
            # the properties below are optional
            listener_identifier="listenerIdentifier",
            name="name",
            service_identifier="serviceIdentifier",
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
        action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
        match: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.MatchProperty", typing.Dict[builtins.str, typing.Any]]],
        priority: jsii.Number,
        listener_identifier: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action: Describes the action for a rule.
        :param match: The rule match.
        :param priority: The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.
        :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
        :param name: The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
        :param tags: The tags for the rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f45608cbfcaa493b76adef96feba7bb9cfff722793ed8a8e3ad2ccbbf68c533)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuleProps(
            action=action,
            match=match,
            priority=priority,
            listener_identifier=listener_identifier,
            name=name,
            service_identifier=service_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d651bd36d1c80d99f9160012e56f69989add7b630fa3d9da3c16cb3c8734ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__20bc926eed79e916a2f7cec725d072c0eb273b91fef311c7e031ce8af37d54aa)
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
        '''The Amazon Resource Name (ARN) of the rule.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the listener.

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
    @jsii.member(jsii_name="action")
    def action(self) -> typing.Union[_IResolvable_da3f097b, "CfnRule.ActionProperty"]:
        '''Describes the action for a rule.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.ActionProperty"], jsii.get(self, "action"))

    @action.setter
    def action(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRule.ActionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4831a0ebaf652d9b7e5a895ef4da1dc54804353e6303bbcb314ad42908d8c965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> typing.Union[_IResolvable_da3f097b, "CfnRule.MatchProperty"]:
        '''The rule match.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.MatchProperty"], jsii.get(self, "match"))

    @match.setter
    def match(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRule.MatchProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd4d52163d104bfa08417185bdade5bedb8947694d6ba4b6a9e8bc741f0321b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "match", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''The priority assigned to the rule.'''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d0b11d8826488634c2e67d07c081b88a95c54c743a4ac0444fa56263eeb00a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="listenerIdentifier")
    def listener_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the listener.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listenerIdentifier"))

    @listener_identifier.setter
    def listener_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86497ac412bb2fc35b930995de6deddbf98007ebabd53ed6e274ef359f0cebc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51cc80bda3c829a5316a48eac071f13c4d5d5f3c5979ba275dd2082a3151db00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceIdentifier")
    def service_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceIdentifier"))

    @service_identifier.setter
    def service_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d064beb02b3c7cccb41e9933a5d63000b7e0e37c2991adcbba0ad9a473a97843)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the rule.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39474ed0177df79f9fd5f7c9f646a32fa2d33929af64c4284c7219a8b2b00b99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"fixed_response": "fixedResponse", "forward": "forward"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            fixed_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.FixedResponseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            forward: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.ForwardProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the action for a rule.

            :param fixed_response: The fixed response action. The rule returns a custom HTTP response.
            :param forward: The forward action. Traffic that matches the rule is forwarded to the specified target groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                action_property = vpclattice.CfnRule.ActionProperty(
                    fixed_response=vpclattice.CfnRule.FixedResponseProperty(
                        status_code=123
                    ),
                    forward=vpclattice.CfnRule.ForwardProperty(
                        target_groups=[vpclattice.CfnRule.WeightedTargetGroupProperty(
                            target_group_identifier="targetGroupIdentifier",
                
                            # the properties below are optional
                            weight=123
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__04c6f3c9bd69bd2f93b3c88c3b361f99b9477bec244066c37ffd18df7b2a0a56)
                check_type(argname="argument fixed_response", value=fixed_response, expected_type=type_hints["fixed_response"])
                check_type(argname="argument forward", value=forward, expected_type=type_hints["forward"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if fixed_response is not None:
                self._values["fixed_response"] = fixed_response
            if forward is not None:
                self._values["forward"] = forward

        @builtins.property
        def fixed_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.FixedResponseProperty"]]:
            '''The fixed response action.

            The rule returns a custom HTTP response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-action.html#cfn-vpclattice-rule-action-fixedresponse
            '''
            result = self._values.get("fixed_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.FixedResponseProperty"]], result)

        @builtins.property
        def forward(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.ForwardProperty"]]:
            '''The forward action.

            Traffic that matches the rule is forwarded to the specified target groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-action.html#cfn-vpclattice-rule-action-forward
            '''
            result = self._values.get("forward")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.ForwardProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.FixedResponseProperty",
        jsii_struct_bases=[],
        name_mapping={"status_code": "statusCode"},
    )
    class FixedResponseProperty:
        def __init__(self, *, status_code: jsii.Number) -> None:
            '''Describes an action that returns a custom HTTP response.

            :param status_code: The HTTP response code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-fixedresponse.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                fixed_response_property = vpclattice.CfnRule.FixedResponseProperty(
                    status_code=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff85d81b73e36cb50a7ae6ffd52486c85c15acb655542991949e89274d4ea728)
                check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status_code": status_code,
            }

        @builtins.property
        def status_code(self) -> jsii.Number:
            '''The HTTP response code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-fixedresponse.html#cfn-vpclattice-rule-fixedresponse-statuscode
            '''
            result = self._values.get("status_code")
            assert result is not None, "Required property 'status_code' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FixedResponseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.ForwardProperty",
        jsii_struct_bases=[],
        name_mapping={"target_groups": "targetGroups"},
    )
    class ForwardProperty:
        def __init__(
            self,
            *,
            target_groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.WeightedTargetGroupProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The forward action.

            Traffic that matches the rule is forwarded to the specified target groups.

            :param target_groups: The target groups. Traffic matching the rule is forwarded to the specified target groups. With forward actions, you can assign a weight that controls the prioritization and selection of each target group. This means that requests are distributed to individual target groups based on their weights. For example, if two target groups have the same weight, each target group receives half of the traffic. The default value is 1. This means that if only one target group is provided, there is no need to set the weight; 100% of the traffic goes to that target group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-forward.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                forward_property = vpclattice.CfnRule.ForwardProperty(
                    target_groups=[vpclattice.CfnRule.WeightedTargetGroupProperty(
                        target_group_identifier="targetGroupIdentifier",
                
                        # the properties below are optional
                        weight=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ea337f287d1d79e1d0c20433003396ff773f2e81d32743e3cf5e7ab9cee0fd3d)
                check_type(argname="argument target_groups", value=target_groups, expected_type=type_hints["target_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_groups": target_groups,
            }

        @builtins.property
        def target_groups(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.WeightedTargetGroupProperty"]]]:
            '''The target groups.

            Traffic matching the rule is forwarded to the specified target groups. With forward actions, you can assign a weight that controls the prioritization and selection of each target group. This means that requests are distributed to individual target groups based on their weights. For example, if two target groups have the same weight, each target group receives half of the traffic.

            The default value is 1. This means that if only one target group is provided, there is no need to set the weight; 100% of the traffic goes to that target group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-forward.html#cfn-vpclattice-rule-forward-targetgroups
            '''
            result = self._values.get("target_groups")
            assert result is not None, "Required property 'target_groups' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.WeightedTargetGroupProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ForwardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.HeaderMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "match": "match",
            "name": "name",
            "case_sensitive": "caseSensitive",
        },
    )
    class HeaderMatchProperty:
        def __init__(
            self,
            *,
            match: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.HeaderMatchTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            case_sensitive: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the constraints for a header match.

            Matches incoming requests with rule based on request header value before applying rule action.

            :param match: The header match type.
            :param name: The name of the header.
            :param case_sensitive: Indicates whether the match is case sensitive. Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                header_match_property = vpclattice.CfnRule.HeaderMatchProperty(
                    match=vpclattice.CfnRule.HeaderMatchTypeProperty(
                        contains="contains",
                        exact="exact",
                        prefix="prefix"
                    ),
                    name="name",
                
                    # the properties below are optional
                    case_sensitive=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b50d3564237e0e7e7f750b13a3a214ba49fdad1f491f0aff09930ce9d039865)
                check_type(argname="argument match", value=match, expected_type=type_hints["match"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument case_sensitive", value=case_sensitive, expected_type=type_hints["case_sensitive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "match": match,
                "name": name,
            }
            if case_sensitive is not None:
                self._values["case_sensitive"] = case_sensitive

        @builtins.property
        def match(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRule.HeaderMatchTypeProperty"]:
            '''The header match type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html#cfn-vpclattice-rule-headermatch-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.HeaderMatchTypeProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the header.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html#cfn-vpclattice-rule-headermatch-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def case_sensitive(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the match is case sensitive.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html#cfn-vpclattice-rule-headermatch-casesensitive
            '''
            result = self._values.get("case_sensitive")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HeaderMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.HeaderMatchTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"contains": "contains", "exact": "exact", "prefix": "prefix"},
    )
    class HeaderMatchTypeProperty:
        def __init__(
            self,
            *,
            contains: typing.Optional[builtins.str] = None,
            exact: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a header match type.

            :param contains: A contains type match.
            :param exact: An exact type match.
            :param prefix: A prefix type match. Matches the value with the prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                header_match_type_property = vpclattice.CfnRule.HeaderMatchTypeProperty(
                    contains="contains",
                    exact="exact",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa37d94a8648ace54a5d9ae24ca82b09c1be743e08c3e294c267db9399616d38)
                check_type(argname="argument contains", value=contains, expected_type=type_hints["contains"])
                check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if contains is not None:
                self._values["contains"] = contains
            if exact is not None:
                self._values["exact"] = exact
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def contains(self) -> typing.Optional[builtins.str]:
            '''A contains type match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html#cfn-vpclattice-rule-headermatchtype-contains
            '''
            result = self._values.get("contains")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''An exact type match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html#cfn-vpclattice-rule-headermatchtype-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix type match.

            Matches the value with the prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html#cfn-vpclattice-rule-headermatchtype-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HeaderMatchTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.HttpMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "header_matches": "headerMatches",
            "method": "method",
            "path_match": "pathMatch",
        },
    )
    class HttpMatchProperty:
        def __init__(
            self,
            *,
            header_matches: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.HeaderMatchProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            method: typing.Optional[builtins.str] = None,
            path_match: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.PathMatchProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes criteria that can be applied to incoming requests.

            :param header_matches: The header matches. Matches incoming requests with rule based on request header value before applying rule action.
            :param method: The HTTP method type.
            :param path_match: The path match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                http_match_property = vpclattice.CfnRule.HttpMatchProperty(
                    header_matches=[vpclattice.CfnRule.HeaderMatchProperty(
                        match=vpclattice.CfnRule.HeaderMatchTypeProperty(
                            contains="contains",
                            exact="exact",
                            prefix="prefix"
                        ),
                        name="name",
                
                        # the properties below are optional
                        case_sensitive=False
                    )],
                    method="method",
                    path_match=vpclattice.CfnRule.PathMatchProperty(
                        match=vpclattice.CfnRule.PathMatchTypeProperty(
                            exact="exact",
                            prefix="prefix"
                        ),
                
                        # the properties below are optional
                        case_sensitive=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf0fb28e64b05586218d1ede069d6bce1f66bc9a71e5b502e421438aa4861ccd)
                check_type(argname="argument header_matches", value=header_matches, expected_type=type_hints["header_matches"])
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
                check_type(argname="argument path_match", value=path_match, expected_type=type_hints["path_match"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if header_matches is not None:
                self._values["header_matches"] = header_matches
            if method is not None:
                self._values["method"] = method
            if path_match is not None:
                self._values["path_match"] = path_match

        @builtins.property
        def header_matches(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.HeaderMatchProperty"]]]]:
            '''The header matches.

            Matches incoming requests with rule based on request header value before applying rule action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html#cfn-vpclattice-rule-httpmatch-headermatches
            '''
            result = self._values.get("header_matches")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.HeaderMatchProperty"]]]], result)

        @builtins.property
        def method(self) -> typing.Optional[builtins.str]:
            '''The HTTP method type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html#cfn-vpclattice-rule-httpmatch-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path_match(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.PathMatchProperty"]]:
            '''The path match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html#cfn-vpclattice-rule-httpmatch-pathmatch
            '''
            result = self._values.get("path_match")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.PathMatchProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.MatchProperty",
        jsii_struct_bases=[],
        name_mapping={"http_match": "httpMatch"},
    )
    class MatchProperty:
        def __init__(
            self,
            *,
            http_match: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.HttpMatchProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Describes a rule match.

            :param http_match: The HTTP criteria that a rule must match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-match.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                match_property = vpclattice.CfnRule.MatchProperty(
                    http_match=vpclattice.CfnRule.HttpMatchProperty(
                        header_matches=[vpclattice.CfnRule.HeaderMatchProperty(
                            match=vpclattice.CfnRule.HeaderMatchTypeProperty(
                                contains="contains",
                                exact="exact",
                                prefix="prefix"
                            ),
                            name="name",
                
                            # the properties below are optional
                            case_sensitive=False
                        )],
                        method="method",
                        path_match=vpclattice.CfnRule.PathMatchProperty(
                            match=vpclattice.CfnRule.PathMatchTypeProperty(
                                exact="exact",
                                prefix="prefix"
                            ),
                
                            # the properties below are optional
                            case_sensitive=False
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b3f38f593ee1c3bd797c45487a3c9434156011ce201d62cb45b4050c52d28b38)
                check_type(argname="argument http_match", value=http_match, expected_type=type_hints["http_match"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "http_match": http_match,
            }

        @builtins.property
        def http_match(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRule.HttpMatchProperty"]:
            '''The HTTP criteria that a rule must match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-match.html#cfn-vpclattice-rule-match-httpmatch
            '''
            result = self._values.get("http_match")
            assert result is not None, "Required property 'http_match' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.HttpMatchProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.PathMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"match": "match", "case_sensitive": "caseSensitive"},
    )
    class PathMatchProperty:
        def __init__(
            self,
            *,
            match: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.PathMatchTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            case_sensitive: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the conditions that can be applied when matching a path for incoming requests.

            :param match: The type of path match.
            :param case_sensitive: Indicates whether the match is case sensitive. Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                path_match_property = vpclattice.CfnRule.PathMatchProperty(
                    match=vpclattice.CfnRule.PathMatchTypeProperty(
                        exact="exact",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    case_sensitive=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b3db801a33274be473b1f5c6d4b035a08ceec0a5a1f394c7636a8bcd11333b55)
                check_type(argname="argument match", value=match, expected_type=type_hints["match"])
                check_type(argname="argument case_sensitive", value=case_sensitive, expected_type=type_hints["case_sensitive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "match": match,
            }
            if case_sensitive is not None:
                self._values["case_sensitive"] = case_sensitive

        @builtins.property
        def match(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRule.PathMatchTypeProperty"]:
            '''The type of path match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatch.html#cfn-vpclattice-rule-pathmatch-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.PathMatchTypeProperty"], result)

        @builtins.property
        def case_sensitive(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the match is case sensitive.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatch.html#cfn-vpclattice-rule-pathmatch-casesensitive
            '''
            result = self._values.get("case_sensitive")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PathMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.PathMatchTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"exact": "exact", "prefix": "prefix"},
    )
    class PathMatchTypeProperty:
        def __init__(
            self,
            *,
            exact: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a path match type.

            Each rule can include only one of the following types of paths.

            :param exact: An exact match of the path.
            :param prefix: A prefix match of the path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatchtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                path_match_type_property = vpclattice.CfnRule.PathMatchTypeProperty(
                    exact="exact",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b85e2c7fa7e122ba1d9745180db6f272b1f2133239021cd2e06bb8128ca5aec)
                check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exact is not None:
                self._values["exact"] = exact
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def exact(self) -> typing.Optional[builtins.str]:
            '''An exact match of the path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatchtype.html#cfn-vpclattice-rule-pathmatchtype-exact
            '''
            result = self._values.get("exact")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix match of the path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatchtype.html#cfn-vpclattice-rule-pathmatchtype-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PathMatchTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnRule.WeightedTargetGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_group_identifier": "targetGroupIdentifier",
            "weight": "weight",
        },
    )
    class WeightedTargetGroupProperty:
        def __init__(
            self,
            *,
            target_group_identifier: builtins.str,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the weight of a target group.

            :param target_group_identifier: The ID of the target group.
            :param weight: Only required if you specify multiple target groups for a forward action. The weight determines how requests are distributed to the target group. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group. If there's only one target group specified, then the default value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-weightedtargetgroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                weighted_target_group_property = vpclattice.CfnRule.WeightedTargetGroupProperty(
                    target_group_identifier="targetGroupIdentifier",
                
                    # the properties below are optional
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b7392120a2424ba71a102eca12ce26fd517effbedb27cafee4856b6b721fcdf)
                check_type(argname="argument target_group_identifier", value=target_group_identifier, expected_type=type_hints["target_group_identifier"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_group_identifier": target_group_identifier,
            }
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def target_group_identifier(self) -> builtins.str:
            '''The ID of the target group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-weightedtargetgroup.html#cfn-vpclattice-rule-weightedtargetgroup-targetgroupidentifier
            '''
            result = self._values.get("target_group_identifier")
            assert result is not None, "Required property 'target_group_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''Only required if you specify multiple target groups for a forward action.

            The weight determines how requests are distributed to the target group. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group. If there's only one target group specified, then the default value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-weightedtargetgroup.html#cfn-vpclattice-rule-weightedtargetgroup-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WeightedTargetGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "match": "match",
        "priority": "priority",
        "listener_identifier": "listenerIdentifier",
        "name": "name",
        "service_identifier": "serviceIdentifier",
        "tags": "tags",
    },
)
class CfnRuleProps:
    def __init__(
        self,
        *,
        action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
        match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.MatchProperty, typing.Dict[builtins.str, typing.Any]]],
        priority: jsii.Number,
        listener_identifier: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRule``.

        :param action: Describes the action for a rule.
        :param match: The rule match.
        :param priority: The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.
        :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
        :param name: The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
        :param tags: The tags for the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            cfn_rule_props = vpclattice.CfnRuleProps(
                action=vpclattice.CfnRule.ActionProperty(
                    fixed_response=vpclattice.CfnRule.FixedResponseProperty(
                        status_code=123
                    ),
                    forward=vpclattice.CfnRule.ForwardProperty(
                        target_groups=[vpclattice.CfnRule.WeightedTargetGroupProperty(
                            target_group_identifier="targetGroupIdentifier",
            
                            # the properties below are optional
                            weight=123
                        )]
                    )
                ),
                match=vpclattice.CfnRule.MatchProperty(
                    http_match=vpclattice.CfnRule.HttpMatchProperty(
                        header_matches=[vpclattice.CfnRule.HeaderMatchProperty(
                            match=vpclattice.CfnRule.HeaderMatchTypeProperty(
                                contains="contains",
                                exact="exact",
                                prefix="prefix"
                            ),
                            name="name",
            
                            # the properties below are optional
                            case_sensitive=False
                        )],
                        method="method",
                        path_match=vpclattice.CfnRule.PathMatchProperty(
                            match=vpclattice.CfnRule.PathMatchTypeProperty(
                                exact="exact",
                                prefix="prefix"
                            ),
            
                            # the properties below are optional
                            case_sensitive=False
                        )
                    )
                ),
                priority=123,
            
                # the properties below are optional
                listener_identifier="listenerIdentifier",
                name="name",
                service_identifier="serviceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81f380fdbb7ddd606a65742cdc6a3fac2454948798f8a3adcb8fb7c0451af6e1)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument listener_identifier", value=listener_identifier, expected_type=type_hints["listener_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_identifier", value=service_identifier, expected_type=type_hints["service_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "match": match,
            "priority": priority,
        }
        if listener_identifier is not None:
            self._values["listener_identifier"] = listener_identifier
        if name is not None:
            self._values["name"] = name
        if service_identifier is not None:
            self._values["service_identifier"] = service_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action(self) -> typing.Union[_IResolvable_da3f097b, CfnRule.ActionProperty]:
        '''Describes the action for a rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRule.ActionProperty], result)

    @builtins.property
    def match(self) -> typing.Union[_IResolvable_da3f097b, CfnRule.MatchProperty]:
        '''The rule match.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-match
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRule.MatchProperty], result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The priority assigned to the rule.

        Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def listener_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the listener.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-listeneridentifier
        '''
        result = self._values.get("listener_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.

        If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-serviceidentifier
        '''
        result = self._values.get("service_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnService(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnService",
):
    '''Creates a service.

    A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).

    For more information, see `Services <https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html>`_ in the *Amazon VPC Lattice User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html
    :cloudformationResource: AWS::VpcLattice::Service
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        cfn_service = vpclattice.CfnService(self, "MyCfnService",
            auth_type="authType",
            certificate_arn="certificateArn",
            custom_domain_name="customDomainName",
            dns_entry=vpclattice.CfnService.DnsEntryProperty(
                domain_name="domainName",
                hosted_zone_id="hostedZoneId"
            ),
            name="name",
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
        auth_type: typing.Optional[builtins.str] = None,
        certificate_arn: typing.Optional[builtins.str] = None,
        custom_domain_name: typing.Optional[builtins.str] = None,
        dns_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.DnsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auth_type: The type of IAM policy. - ``NONE`` : The resource does not use an IAM policy. This is the default. - ``AWS_IAM`` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required. Default: - "NONE"
        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate.
        :param custom_domain_name: The custom domain name of the service.
        :param dns_entry: The DNS information of the service.
        :param name: The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param tags: The tags for the service.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a5a5cd8abc7f43b01f33e191d5a271b64487609134b2e87132fdd4f957285a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProps(
            auth_type=auth_type,
            certificate_arn=certificate_arn,
            custom_domain_name=custom_domain_name,
            dns_entry=dns_entry,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede9bc29bf899f3899c1f881b2709bb1f0d23807a2e274be3a163f1b4b86acfd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fbb5695c8ef98469b47253bc993bea5743f87030ca8d9b68ecd329248f054b27)
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
        '''The Amazon Resource Name (ARN) of the service.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the service was created, specified in ISO-8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsEntryDomainName")
    def attr_dns_entry_domain_name(self) -> builtins.str:
        '''The domain name of the service.

        :cloudformationAttribute: DnsEntry.DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsEntryDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsEntryHostedZoneId")
    def attr_dns_entry_hosted_zone_id(self) -> builtins.str:
        '''The ID of the hosted zone.

        :cloudformationAttribute: DnsEntry.HostedZoneId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsEntryHostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the service.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The date and time that the service was last updated, specified in ISO-8601 format.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the service.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''The type of IAM policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a70974b59c552436983235cafb9a1d52635ecc79eda4efc46a88f6f69fbb8e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec43dcb4a99200212eaa3b3d98fdc8b685986279ce14a132f43f10398ee250a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="customDomainName")
    def custom_domain_name(self) -> typing.Optional[builtins.str]:
        '''The custom domain name of the service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDomainName"))

    @custom_domain_name.setter
    def custom_domain_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60edf6d15d2c6498b1a3aed4ac4a5ceb778ad1626e8271377eecdd4be4493948)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDomainName", value)

    @builtins.property
    @jsii.member(jsii_name="dnsEntry")
    def dns_entry(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.DnsEntryProperty"]]:
        '''The DNS information of the service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.DnsEntryProperty"]], jsii.get(self, "dnsEntry"))

    @dns_entry.setter
    def dns_entry(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.DnsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69a25412bdecd3b0a07c10496705afe686d7dda967f747cf78a50c21f26ba5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsEntry", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b25aa4618a9e265feb7ffb40f1a51d09cd074949bd7ad1d47db2b9c5fd8cfc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the service.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25281814f89f12d37427d1d0bc5ca08326738dbfdba7392691e4723e9c4dcadd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnService.DnsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"domain_name": "domainName", "hosted_zone_id": "hostedZoneId"},
    )
    class DnsEntryProperty:
        def __init__(
            self,
            *,
            domain_name: typing.Optional[builtins.str] = None,
            hosted_zone_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the DNS information of a service.

            :param domain_name: The domain name of the service.
            :param hosted_zone_id: The ID of the hosted zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-service-dnsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                dns_entry_property = vpclattice.CfnService.DnsEntryProperty(
                    domain_name="domainName",
                    hosted_zone_id="hostedZoneId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__350bdb412cdac4bfc1263bd628a727b517c2865cb31003e192ffdcece2f4d69f)
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if domain_name is not None:
                self._values["domain_name"] = domain_name
            if hosted_zone_id is not None:
                self._values["hosted_zone_id"] = hosted_zone_id

        @builtins.property
        def domain_name(self) -> typing.Optional[builtins.str]:
            '''The domain name of the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-service-dnsentry.html#cfn-vpclattice-service-dnsentry-domainname
            '''
            result = self._values.get("domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hosted_zone_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the hosted zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-service-dnsentry.html#cfn-vpclattice-service-dnsentry-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DnsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnServiceNetwork(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnServiceNetwork",
):
    '''Creates a service network.

    A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.

    For more information, see `Service networks <https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html>`_ in the *Amazon VPC Lattice User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html
    :cloudformationResource: AWS::VpcLattice::ServiceNetwork
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        cfn_service_network = vpclattice.CfnServiceNetwork(self, "MyCfnServiceNetwork",
            auth_type="authType",
            name="name",
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
        auth_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auth_type: The type of IAM policy. - ``NONE`` : The resource does not use an IAM policy. This is the default. - ``AWS_IAM`` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required. Default: - "NONE"
        :param name: The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param tags: The tags for the service network.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__656136ed78cebb4875c7f9ba5dbfd3a8474257e368bb831d8f332cd48e509940)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceNetworkProps(auth_type=auth_type, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d0d95730aa970c2f6def693b1a11d7668dcf1e0f233cf3d15c3c6b791e7af6d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__612efa918fb76d4c5a50630f1e4be8fb203a03be817615eeae63568c3eb61424)
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
        '''The Amazon Resource Name (ARN) of the service network.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the service network was created, specified in ISO-8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the service network.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The date and time of the last update, specified in ISO-8601 format.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

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
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''The type of IAM policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e1ed93b1487fcdbf42eab2852c8ca8d412d4b9bc37a1f1155f59fc20a7f87eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1bb59c73b32d0a58bca47ccddf295ff25d18ab46e10146997a37cf96f542ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the service network.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f79b2202986ede0dc063bd10252c9e40fc261092241edb5b4d3a67b64f7b30e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnServiceNetworkProps",
    jsii_struct_bases=[],
    name_mapping={"auth_type": "authType", "name": "name", "tags": "tags"},
)
class CfnServiceNetworkProps:
    def __init__(
        self,
        *,
        auth_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceNetwork``.

        :param auth_type: The type of IAM policy. - ``NONE`` : The resource does not use an IAM policy. This is the default. - ``AWS_IAM`` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required. Default: - "NONE"
        :param name: The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param tags: The tags for the service network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            cfn_service_network_props = vpclattice.CfnServiceNetworkProps(
                auth_type="authType",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d53f770e586510e575c9248934a04f476ddc52636df2e0e8ad22f5800f529a9b)
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''The type of IAM policy.

        - ``NONE`` : The resource does not use an IAM policy. This is the default.
        - ``AWS_IAM`` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.

        :default: - "NONE"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html#cfn-vpclattice-servicenetwork-authtype
        '''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service network.

        The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.

        If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html#cfn-vpclattice-servicenetwork-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the service network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html#cfn-vpclattice-servicenetwork-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnServiceNetworkServiceAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnServiceNetworkServiceAssociation",
):
    '''Associates a service with a service network.

    For more information, see `Manage service associations <https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations>`_ in the *Amazon VPC Lattice User Guide* .

    You can't use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.

    You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.

    As a result of this operation, the association is created in the service network account and the association owner account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html
    :cloudformationResource: AWS::VpcLattice::ServiceNetworkServiceAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        cfn_service_network_service_association = vpclattice.CfnServiceNetworkServiceAssociation(self, "MyCfnServiceNetworkServiceAssociation",
            dns_entry=vpclattice.CfnServiceNetworkServiceAssociation.DnsEntryProperty(
                domain_name="domainName",
                hosted_zone_id="hostedZoneId"
            ),
            service_identifier="serviceIdentifier",
            service_network_identifier="serviceNetworkIdentifier",
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
        dns_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceNetworkServiceAssociation.DnsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        service_identifier: typing.Optional[builtins.str] = None,
        service_network_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dns_entry: The DNS information of the service.
        :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
        :param service_network_identifier: The ID or Amazon Resource Name (ARN) of the service network. You must use the ARN if the resources specified in the operation are in different accounts.
        :param tags: The tags for the association.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fca8cd49cce41155937ce0a58cb5d8795cc6cabeb7236c6e50e7dc2ec43a4fa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceNetworkServiceAssociationProps(
            dns_entry=dns_entry,
            service_identifier=service_identifier,
            service_network_identifier=service_network_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a4300461bf566f5491212d517e1d6b8df088a4ea2f68b04d929fb12365621d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e71e42fb335b2b21f3537e21922a452cdb6c566736b25b3b05b94f588da50548)
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
        '''The Amazon Resource Name (ARN) of the association between the service network and the service.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the association was created, specified in ISO-8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsEntryDomainName")
    def attr_dns_entry_domain_name(self) -> builtins.str:
        '''The domain name of the service.

        :cloudformationAttribute: DnsEntry.DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsEntryDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsEntryHostedZoneId")
    def attr_dns_entry_hosted_zone_id(self) -> builtins.str:
        '''The ID of the hosted zone.

        :cloudformationAttribute: DnsEntry.HostedZoneId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsEntryHostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the of the association between the service network and the service.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceArn")
    def attr_service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the service.

        :cloudformationAttribute: ServiceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceId")
    def attr_service_id(self) -> builtins.str:
        '''The ID of the service.

        :cloudformationAttribute: ServiceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceName")
    def attr_service_name(self) -> builtins.str:
        '''The name of the service.

        :cloudformationAttribute: ServiceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceName"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceNetworkArn")
    def attr_service_network_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the service network.

        :cloudformationAttribute: ServiceNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceNetworkId")
    def attr_service_network_id(self) -> builtins.str:
        '''The ID of the service network.

        :cloudformationAttribute: ServiceNetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceNetworkId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceNetworkName")
    def attr_service_network_name(self) -> builtins.str:
        '''The name of the service network.

        :cloudformationAttribute: ServiceNetworkName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceNetworkName"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the association between the service network and the service.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="dnsEntry")
    def dns_entry(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceNetworkServiceAssociation.DnsEntryProperty"]]:
        '''The DNS information of the service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceNetworkServiceAssociation.DnsEntryProperty"]], jsii.get(self, "dnsEntry"))

    @dns_entry.setter
    def dns_entry(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceNetworkServiceAssociation.DnsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f68128cc2cb951cff136fe7dc696b177c6548c0bcd99175bcb34be9901b080af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsEntry", value)

    @builtins.property
    @jsii.member(jsii_name="serviceIdentifier")
    def service_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceIdentifier"))

    @service_identifier.setter
    def service_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d58c219fada7817ea6759a37ff3ff1d9902faa0c846b05316564255d0e13a5aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNetworkIdentifier"))

    @service_network_identifier.setter
    def service_network_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb007fb3169ca199487503275ba31886585aec7dca0edb77074a3fe972df4d57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNetworkIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the association.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2c0792733dff1f8284dd7ee58181b21c87eab3a32ab103634656eb91059a42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnServiceNetworkServiceAssociation.DnsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"domain_name": "domainName", "hosted_zone_id": "hostedZoneId"},
    )
    class DnsEntryProperty:
        def __init__(
            self,
            *,
            domain_name: typing.Optional[builtins.str] = None,
            hosted_zone_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The DNS information.

            :param domain_name: The domain name of the service.
            :param hosted_zone_id: The ID of the hosted zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                dns_entry_property = vpclattice.CfnServiceNetworkServiceAssociation.DnsEntryProperty(
                    domain_name="domainName",
                    hosted_zone_id="hostedZoneId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__90a651984f70593b4ef5f3ba0f9c2d977e66d24a280608544e6813cf2491219b)
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if domain_name is not None:
                self._values["domain_name"] = domain_name
            if hosted_zone_id is not None:
                self._values["hosted_zone_id"] = hosted_zone_id

        @builtins.property
        def domain_name(self) -> typing.Optional[builtins.str]:
            '''The domain name of the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry.html#cfn-vpclattice-servicenetworkserviceassociation-dnsentry-domainname
            '''
            result = self._values.get("domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hosted_zone_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the hosted zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry.html#cfn-vpclattice-servicenetworkserviceassociation-dnsentry-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DnsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnServiceNetworkServiceAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "dns_entry": "dnsEntry",
        "service_identifier": "serviceIdentifier",
        "service_network_identifier": "serviceNetworkIdentifier",
        "tags": "tags",
    },
)
class CfnServiceNetworkServiceAssociationProps:
    def __init__(
        self,
        *,
        dns_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceNetworkServiceAssociation.DnsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        service_identifier: typing.Optional[builtins.str] = None,
        service_network_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceNetworkServiceAssociation``.

        :param dns_entry: The DNS information of the service.
        :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
        :param service_network_identifier: The ID or Amazon Resource Name (ARN) of the service network. You must use the ARN if the resources specified in the operation are in different accounts.
        :param tags: The tags for the association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            cfn_service_network_service_association_props = vpclattice.CfnServiceNetworkServiceAssociationProps(
                dns_entry=vpclattice.CfnServiceNetworkServiceAssociation.DnsEntryProperty(
                    domain_name="domainName",
                    hosted_zone_id="hostedZoneId"
                ),
                service_identifier="serviceIdentifier",
                service_network_identifier="serviceNetworkIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afab0499c2760b1eb61696969b251958021ccc26369b2379c43988b23b75c3bb)
            check_type(argname="argument dns_entry", value=dns_entry, expected_type=type_hints["dns_entry"])
            check_type(argname="argument service_identifier", value=service_identifier, expected_type=type_hints["service_identifier"])
            check_type(argname="argument service_network_identifier", value=service_network_identifier, expected_type=type_hints["service_network_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dns_entry is not None:
            self._values["dns_entry"] = dns_entry
        if service_identifier is not None:
            self._values["service_identifier"] = service_identifier
        if service_network_identifier is not None:
            self._values["service_network_identifier"] = service_network_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dns_entry(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceNetworkServiceAssociation.DnsEntryProperty]]:
        '''The DNS information of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html#cfn-vpclattice-servicenetworkserviceassociation-dnsentry
        '''
        result = self._values.get("dns_entry")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceNetworkServiceAssociation.DnsEntryProperty]], result)

    @builtins.property
    def service_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html#cfn-vpclattice-servicenetworkserviceassociation-serviceidentifier
        '''
        result = self._values.get("service_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_network_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service network.

        You must use the ARN if the resources specified in the operation are in different accounts.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html#cfn-vpclattice-servicenetworkserviceassociation-servicenetworkidentifier
        '''
        result = self._values.get("service_network_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html#cfn-vpclattice-servicenetworkserviceassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceNetworkServiceAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnServiceNetworkVpcAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnServiceNetworkVpcAssociation",
):
    '''Associates a VPC with a service network.

    When you associate a VPC with the service network, it enables all the resources within that VPC to be clients and communicate with other services in the service network. For more information, see `Manage VPC associations <https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations>`_ in the *Amazon VPC Lattice User Guide* .

    You can't use this operation if there is a disassociation in progress. If the association fails, retry by deleting the association and recreating it.

    As a result of this operation, the association gets created in the service network account and the VPC owner account.

    If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html
    :cloudformationResource: AWS::VpcLattice::ServiceNetworkVpcAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        cfn_service_network_vpc_association = vpclattice.CfnServiceNetworkVpcAssociation(self, "MyCfnServiceNetworkVpcAssociation",
            security_group_ids=["securityGroupIds"],
            service_network_identifier="serviceNetworkIdentifier",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_identifier="vpcIdentifier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_network_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_group_ids: The IDs of the security groups. Security groups aren't added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see `Control traffic to resources using security groups <https://docs.aws.amazon.com//vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon VPC User Guide* .
        :param service_network_identifier: The ID or Amazon Resource Name (ARN) of the service network. You must use the ARN when the resources specified in the operation are in different accounts.
        :param tags: The tags for the association.
        :param vpc_identifier: The ID of the VPC.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a5a54250d817f615a37a7e170370627b854e32b301763e487856be43f74b85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceNetworkVpcAssociationProps(
            security_group_ids=security_group_ids,
            service_network_identifier=service_network_identifier,
            tags=tags,
            vpc_identifier=vpc_identifier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a777bb860f38a86636abc4d189acce8a0a7ac6053361f00055e5cb62ab8e467d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2251a301b298c27c60a8b9cf498a2fffccb3a393af00110a619bdae2aabcca8)
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
        '''The Amazon Resource Name (ARN) of the association between the service network and the VPC.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the association was created, specified in ISO-8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the specified association between the service network and the VPC.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceNetworkArn")
    def attr_service_network_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the service network.

        :cloudformationAttribute: ServiceNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceNetworkId")
    def attr_service_network_id(self) -> builtins.str:
        '''The ID of the service network.

        :cloudformationAttribute: ServiceNetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceNetworkId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceNetworkName")
    def attr_service_network_name(self) -> builtins.str:
        '''The name of the service network.

        :cloudformationAttribute: ServiceNetworkName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceNetworkName"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the association.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcId")
    def attr_vpc_id(self) -> builtins.str:
        '''The ID of the VPC.

        :cloudformationAttribute: VpcId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcId"))

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
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IDs of the security groups.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7648287c9bb4584c27c2b5afd67f788d009960d3e5e7da18f36497b7f076ccb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNetworkIdentifier"))

    @service_network_identifier.setter
    def service_network_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cb6bcb56c90e2399b65bebe5be5e4be4991d64b684b6b2b35b1eeae49577c11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNetworkIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the association.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50bc759b63592b5a79a57951c96725b2b895bdf89f2c8cf8ac09f44f09c10ce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcIdentifier")
    def vpc_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID of the VPC.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdentifier"))

    @vpc_identifier.setter
    def vpc_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9b391eb61efda0eb74e9ad1d922235fdde79a86c6fda50bb367d2a7e6535645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcIdentifier", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnServiceNetworkVpcAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_ids": "securityGroupIds",
        "service_network_identifier": "serviceNetworkIdentifier",
        "tags": "tags",
        "vpc_identifier": "vpcIdentifier",
    },
)
class CfnServiceNetworkVpcAssociationProps:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_network_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceNetworkVpcAssociation``.

        :param security_group_ids: The IDs of the security groups. Security groups aren't added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see `Control traffic to resources using security groups <https://docs.aws.amazon.com//vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon VPC User Guide* .
        :param service_network_identifier: The ID or Amazon Resource Name (ARN) of the service network. You must use the ARN when the resources specified in the operation are in different accounts.
        :param tags: The tags for the association.
        :param vpc_identifier: The ID of the VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            cfn_service_network_vpc_association_props = vpclattice.CfnServiceNetworkVpcAssociationProps(
                security_group_ids=["securityGroupIds"],
                service_network_identifier="serviceNetworkIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_identifier="vpcIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f41a8834cfa086c1096ce2ce95d12df58a5d84c6b647b3712e7e34e8d51ad2d)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument service_network_identifier", value=service_network_identifier, expected_type=type_hints["service_network_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_identifier", value=vpc_identifier, expected_type=type_hints["vpc_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if service_network_identifier is not None:
            self._values["service_network_identifier"] = service_network_identifier
        if tags is not None:
            self._values["tags"] = tags
        if vpc_identifier is not None:
            self._values["vpc_identifier"] = vpc_identifier

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IDs of the security groups.

        Security groups aren't added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see `Control traffic to resources using security groups <https://docs.aws.amazon.com//vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon VPC User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html#cfn-vpclattice-servicenetworkvpcassociation-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_network_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID or Amazon Resource Name (ARN) of the service network.

        You must use the ARN when the resources specified in the operation are in different accounts.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html#cfn-vpclattice-servicenetworkvpcassociation-servicenetworkidentifier
        '''
        result = self._values.get("service_network_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html#cfn-vpclattice-servicenetworkvpcassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_identifier(self) -> typing.Optional[builtins.str]:
        '''The ID of the VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html#cfn-vpclattice-servicenetworkvpcassociation-vpcidentifier
        '''
        result = self._values.get("vpc_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceNetworkVpcAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "auth_type": "authType",
        "certificate_arn": "certificateArn",
        "custom_domain_name": "customDomainName",
        "dns_entry": "dnsEntry",
        "name": "name",
        "tags": "tags",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        auth_type: typing.Optional[builtins.str] = None,
        certificate_arn: typing.Optional[builtins.str] = None,
        custom_domain_name: typing.Optional[builtins.str] = None,
        dns_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.DnsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnService``.

        :param auth_type: The type of IAM policy. - ``NONE`` : The resource does not use an IAM policy. This is the default. - ``AWS_IAM`` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required. Default: - "NONE"
        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate.
        :param custom_domain_name: The custom domain name of the service.
        :param dns_entry: The DNS information of the service.
        :param name: The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param tags: The tags for the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            cfn_service_props = vpclattice.CfnServiceProps(
                auth_type="authType",
                certificate_arn="certificateArn",
                custom_domain_name="customDomainName",
                dns_entry=vpclattice.CfnService.DnsEntryProperty(
                    domain_name="domainName",
                    hosted_zone_id="hostedZoneId"
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ecf90b6f56cf421fa3bfc899e4a66109adebb4da4149086c731ec18d7c75ab)
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument custom_domain_name", value=custom_domain_name, expected_type=type_hints["custom_domain_name"])
            check_type(argname="argument dns_entry", value=dns_entry, expected_type=type_hints["dns_entry"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if custom_domain_name is not None:
            self._values["custom_domain_name"] = custom_domain_name
        if dns_entry is not None:
            self._values["dns_entry"] = dns_entry
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''The type of IAM policy.

        - ``NONE`` : The resource does not use an IAM policy. This is the default.
        - ``AWS_IAM`` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.

        :default: - "NONE"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-authtype
        '''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-certificatearn
        '''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_domain_name(self) -> typing.Optional[builtins.str]:
        '''The custom domain name of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-customdomainname
        '''
        result = self._values.get("custom_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_entry(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.DnsEntryProperty]]:
        '''The DNS information of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-dnsentry
        '''
        result = self._values.get("dns_entry")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.DnsEntryProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service.

        The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.

        If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTargetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnTargetGroup",
):
    '''Creates a target group.

    A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.

    For more information, see `Target groups <https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html>`_ in the *Amazon VPC Lattice User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html
    :cloudformationResource: AWS::VpcLattice::TargetGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_vpclattice as vpclattice
        
        cfn_target_group = vpclattice.CfnTargetGroup(self, "MyCfnTargetGroup",
            type="type",
        
            # the properties below are optional
            config=vpclattice.CfnTargetGroup.TargetGroupConfigProperty(
                health_check=vpclattice.CfnTargetGroup.HealthCheckConfigProperty(
                    enabled=False,
                    health_check_interval_seconds=123,
                    health_check_timeout_seconds=123,
                    healthy_threshold_count=123,
                    matcher=vpclattice.CfnTargetGroup.MatcherProperty(
                        http_code="httpCode"
                    ),
                    path="path",
                    port=123,
                    protocol="protocol",
                    protocol_version="protocolVersion",
                    unhealthy_threshold_count=123
                ),
                ip_address_type="ipAddressType",
                lambda_event_structure_version="lambdaEventStructureVersion",
                port=123,
                protocol="protocol",
                protocol_version="protocolVersion",
                vpc_identifier="vpcIdentifier"
            ),
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            targets=[vpclattice.CfnTargetGroup.TargetProperty(
                id="id",
        
                # the properties below are optional
                port=123
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTargetGroup.TargetGroupConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTargetGroup.TargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param type: The type of target group.
        :param config: The target group configuration.
        :param name: The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param tags: The tags for the target group.
        :param targets: Describes a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f8ff68e6e993cdd9866d74d0830ca79ebc03271ed9540ff83660d8fdf63dc4c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTargetGroupProps(
            type=type, config=config, name=name, tags=tags, targets=targets
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c70d0b50b842bdfae9675e5b4269b63a85b8628e64b89a33fda5aadcc9888b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__18aa70ee6ccd3fe0b980b18772790e5a930273d23e3db11021bcaf45618e5fe2)
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
        '''The Amazon Resource Name (ARN) of the target group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the target group was created, specified in ISO-8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the target group.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The date and time that the target group was last updated, specified in ISO-8601 format.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The operation's status.

        You can retry the operation if the status is ``CREATE_FAILED`` . However, if you retry it while the status is ``CREATE_IN_PROGRESS`` , there is no change in the status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of target group.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a4cf8759e96c450234f0436aec63d79736c8f32e5dce7700462faa9baabbb06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.TargetGroupConfigProperty"]]:
        '''The target group configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.TargetGroupConfigProperty"]], jsii.get(self, "config"))

    @config.setter
    def config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.TargetGroupConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa8640187487f07eca4afad1c9572ddd8bc8c999dcf3d4db28459391b85f9cab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "config", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the target group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8f01c11a279bf1da79b9907f630447212c4f57ae5173a2e7ef98271a44fa7ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the target group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__136df6fcae40b885020641351e843f89511c6e92fa2173475366a4820c5ddd41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.TargetProperty"]]]]:
        '''Describes a target.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.TargetProperty"]]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.TargetProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc9e71a8b226ae62bf17321c794331f8bbbd90e67522bffd60ad5a876cf88391)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnTargetGroup.HealthCheckConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "health_check_interval_seconds": "healthCheckIntervalSeconds",
            "health_check_timeout_seconds": "healthCheckTimeoutSeconds",
            "healthy_threshold_count": "healthyThresholdCount",
            "matcher": "matcher",
            "path": "path",
            "port": "port",
            "protocol": "protocol",
            "protocol_version": "protocolVersion",
            "unhealthy_threshold_count": "unhealthyThresholdCount",
        },
    )
    class HealthCheckConfigProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            health_check_interval_seconds: typing.Optional[jsii.Number] = None,
            health_check_timeout_seconds: typing.Optional[jsii.Number] = None,
            healthy_threshold_count: typing.Optional[jsii.Number] = None,
            matcher: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTargetGroup.MatcherProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            path: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            protocol: typing.Optional[builtins.str] = None,
            protocol_version: typing.Optional[builtins.str] = None,
            unhealthy_threshold_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the health check configuration of a target group.

            Health check configurations aren't used for target groups of type ``LAMBDA`` or ``ALB`` .

            :param enabled: Indicates whether health checking is enabled.
            :param health_check_interval_seconds: The approximate amount of time, in seconds, between health checks of an individual target. The range is 5–300 seconds. The default is 30 seconds.
            :param health_check_timeout_seconds: The amount of time, in seconds, to wait before reporting a target as unhealthy. The range is 1–120 seconds. The default is 5 seconds.
            :param healthy_threshold_count: The number of consecutive successful health checks required before considering an unhealthy target healthy. The range is 2–10. The default is 5.
            :param matcher: The codes to use when checking for a successful response from a target.
            :param path: The destination for health checks on the targets. If the protocol version is ``HTTP/1.1`` or ``HTTP/2`` , specify a valid URI (for example, ``/path?query`` ). The default path is ``/`` . Health checks are not supported if the protocol version is ``gRPC`` , however, you can choose ``HTTP/1.1`` or ``HTTP/2`` and specify a valid URI.
            :param port: The port used when performing health checks on targets. The default setting is the port that a target receives traffic on.
            :param protocol: The protocol used when performing health checks on targets. The possible protocols are ``HTTP`` and ``HTTPS`` . The default is ``HTTP`` .
            :param protocol_version: The protocol version used when performing health checks on targets. The possible protocol versions are ``HTTP1`` and ``HTTP2`` .
            :param unhealthy_threshold_count: The number of consecutive failed health checks required before considering a target unhealthy. The range is 2–10. The default is 2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                health_check_config_property = vpclattice.CfnTargetGroup.HealthCheckConfigProperty(
                    enabled=False,
                    health_check_interval_seconds=123,
                    health_check_timeout_seconds=123,
                    healthy_threshold_count=123,
                    matcher=vpclattice.CfnTargetGroup.MatcherProperty(
                        http_code="httpCode"
                    ),
                    path="path",
                    port=123,
                    protocol="protocol",
                    protocol_version="protocolVersion",
                    unhealthy_threshold_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a09939992f1eb5c8167fae61e1096131911a8e389625b3dc5b5dde0beafbe8c1)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument health_check_interval_seconds", value=health_check_interval_seconds, expected_type=type_hints["health_check_interval_seconds"])
                check_type(argname="argument health_check_timeout_seconds", value=health_check_timeout_seconds, expected_type=type_hints["health_check_timeout_seconds"])
                check_type(argname="argument healthy_threshold_count", value=healthy_threshold_count, expected_type=type_hints["healthy_threshold_count"])
                check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument protocol_version", value=protocol_version, expected_type=type_hints["protocol_version"])
                check_type(argname="argument unhealthy_threshold_count", value=unhealthy_threshold_count, expected_type=type_hints["unhealthy_threshold_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if health_check_interval_seconds is not None:
                self._values["health_check_interval_seconds"] = health_check_interval_seconds
            if health_check_timeout_seconds is not None:
                self._values["health_check_timeout_seconds"] = health_check_timeout_seconds
            if healthy_threshold_count is not None:
                self._values["healthy_threshold_count"] = healthy_threshold_count
            if matcher is not None:
                self._values["matcher"] = matcher
            if path is not None:
                self._values["path"] = path
            if port is not None:
                self._values["port"] = port
            if protocol is not None:
                self._values["protocol"] = protocol
            if protocol_version is not None:
                self._values["protocol_version"] = protocol_version
            if unhealthy_threshold_count is not None:
                self._values["unhealthy_threshold_count"] = unhealthy_threshold_count

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether health checking is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def health_check_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''The approximate amount of time, in seconds, between health checks of an individual target.

            The range is 5–300 seconds. The default is 30 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-healthcheckintervalseconds
            '''
            result = self._values.get("health_check_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def health_check_timeout_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, to wait before reporting a target as unhealthy.

            The range is 1–120 seconds. The default is 5 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-healthchecktimeoutseconds
            '''
            result = self._values.get("health_check_timeout_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def healthy_threshold_count(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive successful health checks required before considering an unhealthy target healthy.

            The range is 2–10. The default is 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-healthythresholdcount
            '''
            result = self._values.get("healthy_threshold_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def matcher(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.MatcherProperty"]]:
            '''The codes to use when checking for a successful response from a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-matcher
            '''
            result = self._values.get("matcher")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.MatcherProperty"]], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The destination for health checks on the targets.

            If the protocol version is ``HTTP/1.1`` or ``HTTP/2`` , specify a valid URI (for example, ``/path?query`` ). The default path is ``/`` . Health checks are not supported if the protocol version is ``gRPC`` , however, you can choose ``HTTP/1.1`` or ``HTTP/2`` and specify a valid URI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port used when performing health checks on targets.

            The default setting is the port that a target receives traffic on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The protocol used when performing health checks on targets.

            The possible protocols are ``HTTP`` and ``HTTPS`` . The default is ``HTTP`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol_version(self) -> typing.Optional[builtins.str]:
            '''The protocol version used when performing health checks on targets.

            The possible protocol versions are ``HTTP1`` and ``HTTP2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-protocolversion
            '''
            result = self._values.get("protocol_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unhealthy_threshold_count(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive failed health checks required before considering a target unhealthy.

            The range is 2–10. The default is 2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-unhealthythresholdcount
            '''
            result = self._values.get("unhealthy_threshold_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnTargetGroup.MatcherProperty",
        jsii_struct_bases=[],
        name_mapping={"http_code": "httpCode"},
    )
    class MatcherProperty:
        def __init__(self, *, http_code: builtins.str) -> None:
            '''Describes the codes to use when checking for a successful response from a target for health checks.

            :param http_code: The HTTP code to use when checking for a successful response from a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-matcher.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                matcher_property = vpclattice.CfnTargetGroup.MatcherProperty(
                    http_code="httpCode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30dd80af951d79d177912b8867baf5806675529c6f61c59734e939b828d3cb22)
                check_type(argname="argument http_code", value=http_code, expected_type=type_hints["http_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "http_code": http_code,
            }

        @builtins.property
        def http_code(self) -> builtins.str:
            '''The HTTP code to use when checking for a successful response from a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-matcher.html#cfn-vpclattice-targetgroup-matcher-httpcode
            '''
            result = self._values.get("http_code")
            assert result is not None, "Required property 'http_code' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MatcherProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnTargetGroup.TargetGroupConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "health_check": "healthCheck",
            "ip_address_type": "ipAddressType",
            "lambda_event_structure_version": "lambdaEventStructureVersion",
            "port": "port",
            "protocol": "protocol",
            "protocol_version": "protocolVersion",
            "vpc_identifier": "vpcIdentifier",
        },
    )
    class TargetGroupConfigProperty:
        def __init__(
            self,
            *,
            health_check: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTargetGroup.HealthCheckConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ip_address_type: typing.Optional[builtins.str] = None,
            lambda_event_structure_version: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            protocol: typing.Optional[builtins.str] = None,
            protocol_version: typing.Optional[builtins.str] = None,
            vpc_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration of a target group.

            For more information, see `Target groups <https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html>`_ in the *Amazon VPC Lattice User Guide* .

            :param health_check: The health check configuration. Not supported if the target group type is ``LAMBDA`` or ``ALB`` .
            :param ip_address_type: The type of IP address used for the target group. Supported only if the target group type is ``IP`` . The default is ``IPV4`` . Default: - "IPV4"
            :param lambda_event_structure_version: The version of the event structure that your Lambda function receives. Supported only if the target group type is ``LAMBDA`` . The default is ``V1`` .
            :param port: The port on which the targets are listening. For HTTP, the default is 80. For HTTPS, the default is 443. Not supported if the target group type is ``LAMBDA`` .
            :param protocol: The protocol to use for routing traffic to the targets. The default is the protocol of the target group. Not supported if the target group type is ``LAMBDA`` .
            :param protocol_version: The protocol version. The default is ``HTTP1`` . Not supported if the target group type is ``LAMBDA`` . Default: - "HTTP1"
            :param vpc_identifier: The ID of the VPC. Not supported if the target group type is ``LAMBDA`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                target_group_config_property = vpclattice.CfnTargetGroup.TargetGroupConfigProperty(
                    health_check=vpclattice.CfnTargetGroup.HealthCheckConfigProperty(
                        enabled=False,
                        health_check_interval_seconds=123,
                        health_check_timeout_seconds=123,
                        healthy_threshold_count=123,
                        matcher=vpclattice.CfnTargetGroup.MatcherProperty(
                            http_code="httpCode"
                        ),
                        path="path",
                        port=123,
                        protocol="protocol",
                        protocol_version="protocolVersion",
                        unhealthy_threshold_count=123
                    ),
                    ip_address_type="ipAddressType",
                    lambda_event_structure_version="lambdaEventStructureVersion",
                    port=123,
                    protocol="protocol",
                    protocol_version="protocolVersion",
                    vpc_identifier="vpcIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a041432c3078e0853d7935a61589530e15207ff82506b97572b2bcbf7738a359)
                check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
                check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
                check_type(argname="argument lambda_event_structure_version", value=lambda_event_structure_version, expected_type=type_hints["lambda_event_structure_version"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument protocol_version", value=protocol_version, expected_type=type_hints["protocol_version"])
                check_type(argname="argument vpc_identifier", value=vpc_identifier, expected_type=type_hints["vpc_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if health_check is not None:
                self._values["health_check"] = health_check
            if ip_address_type is not None:
                self._values["ip_address_type"] = ip_address_type
            if lambda_event_structure_version is not None:
                self._values["lambda_event_structure_version"] = lambda_event_structure_version
            if port is not None:
                self._values["port"] = port
            if protocol is not None:
                self._values["protocol"] = protocol
            if protocol_version is not None:
                self._values["protocol_version"] = protocol_version
            if vpc_identifier is not None:
                self._values["vpc_identifier"] = vpc_identifier

        @builtins.property
        def health_check(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.HealthCheckConfigProperty"]]:
            '''The health check configuration.

            Not supported if the target group type is ``LAMBDA`` or ``ALB`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-healthcheck
            '''
            result = self._values.get("health_check")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTargetGroup.HealthCheckConfigProperty"]], result)

        @builtins.property
        def ip_address_type(self) -> typing.Optional[builtins.str]:
            '''The type of IP address used for the target group.

            Supported only if the target group type is ``IP`` . The default is ``IPV4`` .

            :default: - "IPV4"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-ipaddresstype
            '''
            result = self._values.get("ip_address_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lambda_event_structure_version(self) -> typing.Optional[builtins.str]:
            '''The version of the event structure that your Lambda function receives.

            Supported only if the target group type is ``LAMBDA`` . The default is ``V1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-lambdaeventstructureversion
            '''
            result = self._values.get("lambda_event_structure_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port on which the targets are listening.

            For HTTP, the default is 80. For HTTPS, the default is 443. Not supported if the target group type is ``LAMBDA`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The protocol to use for routing traffic to the targets.

            The default is the protocol of the target group. Not supported if the target group type is ``LAMBDA`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol_version(self) -> typing.Optional[builtins.str]:
            '''The protocol version.

            The default is ``HTTP1`` . Not supported if the target group type is ``LAMBDA`` .

            :default: - "HTTP1"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-protocolversion
            '''
            result = self._values.get("protocol_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_identifier(self) -> typing.Optional[builtins.str]:
            '''The ID of the VPC.

            Not supported if the target group type is ``LAMBDA`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-vpcidentifier
            '''
            result = self._values.get("vpc_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetGroupConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_vpclattice.CfnTargetGroup.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "port": "port"},
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes a target.

            :param id: The ID of the target. If the target group type is ``INSTANCE`` , this is an instance ID. If the target group type is ``IP`` , this is an IP address. If the target group type is ``LAMBDA`` , this is the ARN of a Lambda function. If the target group type is ``ALB`` , this is the ARN of an Application Load Balancer.
            :param port: The port on which the target is listening. For HTTP, the default is 80. For HTTPS, the default is 443.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_vpclattice as vpclattice
                
                target_property = vpclattice.CfnTargetGroup.TargetProperty(
                    id="id",
                
                    # the properties below are optional
                    port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d56100b501da89da21de19c41e69ce3c600f9f6f41dbc6fa3266fed88928b79)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def id(self) -> builtins.str:
            '''The ID of the target.

            If the target group type is ``INSTANCE`` , this is an instance ID. If the target group type is ``IP`` , this is an IP address. If the target group type is ``LAMBDA`` , this is the ARN of a Lambda function. If the target group type is ``ALB`` , this is the ARN of an Application Load Balancer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-target.html#cfn-vpclattice-targetgroup-target-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port on which the target is listening.

            For HTTP, the default is 80. For HTTPS, the default is 443.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-target.html#cfn-vpclattice-targetgroup-target-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_vpclattice.CfnTargetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "config": "config",
        "name": "name",
        "tags": "tags",
        "targets": "targets",
    },
)
class CfnTargetGroupProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetGroup.TargetGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetGroup.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTargetGroup``.

        :param type: The type of target group.
        :param config: The target group configuration.
        :param name: The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen. If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param tags: The tags for the target group.
        :param targets: Describes a target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_vpclattice as vpclattice
            
            cfn_target_group_props = vpclattice.CfnTargetGroupProps(
                type="type",
            
                # the properties below are optional
                config=vpclattice.CfnTargetGroup.TargetGroupConfigProperty(
                    health_check=vpclattice.CfnTargetGroup.HealthCheckConfigProperty(
                        enabled=False,
                        health_check_interval_seconds=123,
                        health_check_timeout_seconds=123,
                        healthy_threshold_count=123,
                        matcher=vpclattice.CfnTargetGroup.MatcherProperty(
                            http_code="httpCode"
                        ),
                        path="path",
                        port=123,
                        protocol="protocol",
                        protocol_version="protocolVersion",
                        unhealthy_threshold_count=123
                    ),
                    ip_address_type="ipAddressType",
                    lambda_event_structure_version="lambdaEventStructureVersion",
                    port=123,
                    protocol="protocol",
                    protocol_version="protocolVersion",
                    vpc_identifier="vpcIdentifier"
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                targets=[vpclattice.CfnTargetGroup.TargetProperty(
                    id="id",
            
                    # the properties below are optional
                    port=123
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7726205b43353108496846bc1f02062590e018e95fc96e11e69453af71727ed0)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if config is not None:
            self._values["config"] = config
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if targets is not None:
            self._values["targets"] = targets

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of target group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTargetGroup.TargetGroupConfigProperty]]:
        '''The target group configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-config
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTargetGroup.TargetGroupConfigProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the target group.

        The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.

        If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the target group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTargetGroup.TargetProperty]]]]:
        '''Describes a target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-targets
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTargetGroup.TargetProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTargetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessLogSubscription",
    "CfnAccessLogSubscriptionProps",
    "CfnAuthPolicy",
    "CfnAuthPolicyProps",
    "CfnListener",
    "CfnListenerProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CfnRule",
    "CfnRuleProps",
    "CfnService",
    "CfnServiceNetwork",
    "CfnServiceNetworkProps",
    "CfnServiceNetworkServiceAssociation",
    "CfnServiceNetworkServiceAssociationProps",
    "CfnServiceNetworkVpcAssociation",
    "CfnServiceNetworkVpcAssociationProps",
    "CfnServiceProps",
    "CfnTargetGroup",
    "CfnTargetGroupProps",
]

publication.publish()

def _typecheckingstub__5d1e4f257245d8e5be92083145da5c0b7311cde5a905b65c5cb20fb0c7230032(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_arn: builtins.str,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b373a2103376ee17034d5f8a2bd66281964526c897621d59f595a7ee710dece(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f207b1387515fc7caa56e4c3c30125161e739b43f33921086c670ed7af78619e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__880b45928aa837a0dba3740b58b3250033476ee4e3d14b774b01c4cd2d224862(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b93aeac48124e92f9f09dd3e99f9ef8ac5e9d002fe64dea86b3d7700ae862f0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f88ce1faaa39f21f51b79668a87b932a07532be6cdddad83e4090e05f9de003e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7551e4dc1730a5c7bf48ba5c2eccbe95ed6914a39663f70c2dc1846465e8eb40(
    *,
    destination_arn: builtins.str,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abc7f80c1c8d027e6648f29dec237037cc235db1d8d50ebf4422488fb91b8baf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy: typing.Any,
    resource_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f70c44b3f60fa4c4dc9571d48bccab272ae2d8e0388211e0c37b15b6bb398b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77adb13a1a8a12ce61a7ed6ec7e7cb8bb87b99d67e87c3dc791a7287c4814c5c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17ec53a4ae132f699e3368133cd6066a7924febd9eaadf1625f077db673021d6(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2514bd99a036fd72228bf57ad953594909d7d395566fdbeb7ff5aff3293879f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d3fae469a4114f5041ab337d4b2b87c6bebd93bfab70112ebf9e83154ff99a2(
    *,
    policy: typing.Any,
    resource_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf0492fe381e6c540d4fceb6599cf5162be861921ce004b402eda7520043896(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnListener.DefaultActionProperty, typing.Dict[builtins.str, typing.Any]]],
    protocol: builtins.str,
    name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    service_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25b05e2b4b011a9e577c8e7138d4c3dd6e9ec07662ecaaf676372223833cb5b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5715a8b3b39f5a4c8c946b85c67be15dcfc7edfb2b226908322e417d9d0bd31(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1229fc3c4aaabfa1f9070833cc86ddb5be622124d223b483013096dc0aa21c3(
    value: typing.Union[_IResolvable_da3f097b, CfnListener.DefaultActionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be640f5e33aaca4e3b3006d7b10a59a023e68cde6cfbeb0bfd196b5c45d669d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104c1d020e852a1a0976b78cd610d4d052759087e8b62439928254eafc6bb997(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a0149fd9aab80b3782107ecd9c41ff0650b7a79a7f9ac61e250a4364883c4c(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d439d803b5f48fef5e4cb28a8126bd2873fb6db421fc78917613a39ba02471fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bdb1d86bfde2da64bd233fa7351069e7394020e32eca07770f43cd1b50cca3a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6602b39b19cadd1593258c7a69267d1af5d7fc891a209bfc3d9044363f099466(
    *,
    fixed_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnListener.FixedResponseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    forward: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnListener.ForwardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76b0a5cea9cf961398e2abd115a12a0d1717ccabd032d36586e85319edd6e147(
    *,
    status_code: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9093fece335bbe1a3446db4db253cf7d0a348828e72e6455586ea506df70caa(
    *,
    target_groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnListener.WeightedTargetGroupProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c09b0cb0878b1a32d785c3518fc1c21913c2ec5370c786f57403db8cff4d43e(
    *,
    target_group_identifier: builtins.str,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2abd654d29759383ba4227953efda14c5f7db6190ad40176eb92bfbb7ccc5693(
    *,
    default_action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnListener.DefaultActionProperty, typing.Dict[builtins.str, typing.Any]]],
    protocol: builtins.str,
    name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    service_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cc9008c3f7ccae7d54d444c5b5dcc1b03b4db009ad23c4a5ed74863b84b8360(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy: typing.Any,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f59c385ec0fb1e5259ddbe4dcf2dc2f9536688a56ee6370da1f2fc23f2c1c63b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06094face44c3f8ef3bb0ce5b6a09f5384d137bb913e2b9c1f4b816492211e25(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2222735d3aa86622d6c42b8990fc3cacd9a757664d0c3b751cabcab6a2a8766e(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed10d5f1b65a1ffbcbbe61eb60ea82b7e503a39f49b95b7c028aaabc889b94c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1737436eeafbe996ee74ec168a6fb4cb8dd64c1c2bcb91c9ba68d5dc234bb69e(
    *,
    policy: typing.Any,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f45608cbfcaa493b76adef96feba7bb9cfff722793ed8a8e3ad2ccbbf68c533(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.MatchProperty, typing.Dict[builtins.str, typing.Any]]],
    priority: jsii.Number,
    listener_identifier: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d651bd36d1c80d99f9160012e56f69989add7b630fa3d9da3c16cb3c8734ea(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20bc926eed79e916a2f7cec725d072c0eb273b91fef311c7e031ce8af37d54aa(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4831a0ebaf652d9b7e5a895ef4da1dc54804353e6303bbcb314ad42908d8c965(
    value: typing.Union[_IResolvable_da3f097b, CfnRule.ActionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd4d52163d104bfa08417185bdade5bedb8947694d6ba4b6a9e8bc741f0321b(
    value: typing.Union[_IResolvable_da3f097b, CfnRule.MatchProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d0b11d8826488634c2e67d07c081b88a95c54c743a4ac0444fa56263eeb00a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86497ac412bb2fc35b930995de6deddbf98007ebabd53ed6e274ef359f0cebc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51cc80bda3c829a5316a48eac071f13c4d5d5f3c5979ba275dd2082a3151db00(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d064beb02b3c7cccb41e9933a5d63000b7e0e37c2991adcbba0ad9a473a97843(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39474ed0177df79f9fd5f7c9f646a32fa2d33929af64c4284c7219a8b2b00b99(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04c6f3c9bd69bd2f93b3c88c3b361f99b9477bec244066c37ffd18df7b2a0a56(
    *,
    fixed_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.FixedResponseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    forward: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ForwardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff85d81b73e36cb50a7ae6ffd52486c85c15acb655542991949e89274d4ea728(
    *,
    status_code: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea337f287d1d79e1d0c20433003396ff773f2e81d32743e3cf5e7ab9cee0fd3d(
    *,
    target_groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.WeightedTargetGroupProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b50d3564237e0e7e7f750b13a3a214ba49fdad1f491f0aff09930ce9d039865(
    *,
    match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.HeaderMatchTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    case_sensitive: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa37d94a8648ace54a5d9ae24ca82b09c1be743e08c3e294c267db9399616d38(
    *,
    contains: typing.Optional[builtins.str] = None,
    exact: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf0fb28e64b05586218d1ede069d6bce1f66bc9a71e5b502e421438aa4861ccd(
    *,
    header_matches: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.HeaderMatchProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    method: typing.Optional[builtins.str] = None,
    path_match: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.PathMatchProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f38f593ee1c3bd797c45487a3c9434156011ce201d62cb45b4050c52d28b38(
    *,
    http_match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.HttpMatchProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3db801a33274be473b1f5c6d4b035a08ceec0a5a1f394c7636a8bcd11333b55(
    *,
    match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.PathMatchTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    case_sensitive: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b85e2c7fa7e122ba1d9745180db6f272b1f2133239021cd2e06bb8128ca5aec(
    *,
    exact: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b7392120a2424ba71a102eca12ce26fd517effbedb27cafee4856b6b721fcdf(
    *,
    target_group_identifier: builtins.str,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f380fdbb7ddd606a65742cdc6a3fac2454948798f8a3adcb8fb7c0451af6e1(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.MatchProperty, typing.Dict[builtins.str, typing.Any]]],
    priority: jsii.Number,
    listener_identifier: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a5a5cd8abc7f43b01f33e191d5a271b64487609134b2e87132fdd4f957285a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auth_type: typing.Optional[builtins.str] = None,
    certificate_arn: typing.Optional[builtins.str] = None,
    custom_domain_name: typing.Optional[builtins.str] = None,
    dns_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.DnsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ede9bc29bf899f3899c1f881b2709bb1f0d23807a2e274be3a163f1b4b86acfd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbb5695c8ef98469b47253bc993bea5743f87030ca8d9b68ecd329248f054b27(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a70974b59c552436983235cafb9a1d52635ecc79eda4efc46a88f6f69fbb8e6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec43dcb4a99200212eaa3b3d98fdc8b685986279ce14a132f43f10398ee250a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60edf6d15d2c6498b1a3aed4ac4a5ceb778ad1626e8271377eecdd4be4493948(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69a25412bdecd3b0a07c10496705afe686d7dda967f747cf78a50c21f26ba5e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.DnsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b25aa4618a9e265feb7ffb40f1a51d09cd074949bd7ad1d47db2b9c5fd8cfc1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25281814f89f12d37427d1d0bc5ca08326738dbfdba7392691e4723e9c4dcadd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350bdb412cdac4bfc1263bd628a727b517c2865cb31003e192ffdcece2f4d69f(
    *,
    domain_name: typing.Optional[builtins.str] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__656136ed78cebb4875c7f9ba5dbfd3a8474257e368bb831d8f332cd48e509940(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auth_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0d95730aa970c2f6def693b1a11d7668dcf1e0f233cf3d15c3c6b791e7af6d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__612efa918fb76d4c5a50630f1e4be8fb203a03be817615eeae63568c3eb61424(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e1ed93b1487fcdbf42eab2852c8ca8d412d4b9bc37a1f1155f59fc20a7f87eb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1bb59c73b32d0a58bca47ccddf295ff25d18ab46e10146997a37cf96f542ea(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f79b2202986ede0dc063bd10252c9e40fc261092241edb5b4d3a67b64f7b30e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d53f770e586510e575c9248934a04f476ddc52636df2e0e8ad22f5800f529a9b(
    *,
    auth_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fca8cd49cce41155937ce0a58cb5d8795cc6cabeb7236c6e50e7dc2ec43a4fa(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dns_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceNetworkServiceAssociation.DnsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_identifier: typing.Optional[builtins.str] = None,
    service_network_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a4300461bf566f5491212d517e1d6b8df088a4ea2f68b04d929fb12365621d2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e71e42fb335b2b21f3537e21922a452cdb6c566736b25b3b05b94f588da50548(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f68128cc2cb951cff136fe7dc696b177c6548c0bcd99175bcb34be9901b080af(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceNetworkServiceAssociation.DnsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d58c219fada7817ea6759a37ff3ff1d9902faa0c846b05316564255d0e13a5aa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb007fb3169ca199487503275ba31886585aec7dca0edb77074a3fe972df4d57(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2c0792733dff1f8284dd7ee58181b21c87eab3a32ab103634656eb91059a42(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a651984f70593b4ef5f3ba0f9c2d977e66d24a280608544e6813cf2491219b(
    *,
    domain_name: typing.Optional[builtins.str] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afab0499c2760b1eb61696969b251958021ccc26369b2379c43988b23b75c3bb(
    *,
    dns_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceNetworkServiceAssociation.DnsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_identifier: typing.Optional[builtins.str] = None,
    service_network_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a5a54250d817f615a37a7e170370627b854e32b301763e487856be43f74b85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    service_network_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a777bb860f38a86636abc4d189acce8a0a7ac6053361f00055e5cb62ab8e467d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2251a301b298c27c60a8b9cf498a2fffccb3a393af00110a619bdae2aabcca8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7648287c9bb4584c27c2b5afd67f788d009960d3e5e7da18f36497b7f076ccb8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cb6bcb56c90e2399b65bebe5be5e4be4991d64b684b6b2b35b1eeae49577c11(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50bc759b63592b5a79a57951c96725b2b895bdf89f2c8cf8ac09f44f09c10ce3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b391eb61efda0eb74e9ad1d922235fdde79a86c6fda50bb367d2a7e6535645(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f41a8834cfa086c1096ce2ce95d12df58a5d84c6b647b3712e7e34e8d51ad2d(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    service_network_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ecf90b6f56cf421fa3bfc899e4a66109adebb4da4149086c731ec18d7c75ab(
    *,
    auth_type: typing.Optional[builtins.str] = None,
    certificate_arn: typing.Optional[builtins.str] = None,
    custom_domain_name: typing.Optional[builtins.str] = None,
    dns_entry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.DnsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8ff68e6e993cdd9866d74d0830ca79ebc03271ed9540ff83660d8fdf63dc4c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    type: builtins.str,
    config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetGroup.TargetGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetGroup.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c70d0b50b842bdfae9675e5b4269b63a85b8628e64b89a33fda5aadcc9888b2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18aa70ee6ccd3fe0b980b18772790e5a930273d23e3db11021bcaf45618e5fe2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a4cf8759e96c450234f0436aec63d79736c8f32e5dce7700462faa9baabbb06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa8640187487f07eca4afad1c9572ddd8bc8c999dcf3d4db28459391b85f9cab(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTargetGroup.TargetGroupConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f01c11a279bf1da79b9907f630447212c4f57ae5173a2e7ef98271a44fa7ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136df6fcae40b885020641351e843f89511c6e92fa2173475366a4820c5ddd41(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9e71a8b226ae62bf17321c794331f8bbbd90e67522bffd60ad5a876cf88391(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTargetGroup.TargetProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a09939992f1eb5c8167fae61e1096131911a8e389625b3dc5b5dde0beafbe8c1(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    health_check_interval_seconds: typing.Optional[jsii.Number] = None,
    health_check_timeout_seconds: typing.Optional[jsii.Number] = None,
    healthy_threshold_count: typing.Optional[jsii.Number] = None,
    matcher: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetGroup.MatcherProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    path: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    protocol_version: typing.Optional[builtins.str] = None,
    unhealthy_threshold_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30dd80af951d79d177912b8867baf5806675529c6f61c59734e939b828d3cb22(
    *,
    http_code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a041432c3078e0853d7935a61589530e15207ff82506b97572b2bcbf7738a359(
    *,
    health_check: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetGroup.HealthCheckConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    lambda_event_structure_version: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    protocol_version: typing.Optional[builtins.str] = None,
    vpc_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d56100b501da89da21de19c41e69ce3c600f9f6f41dbc6fa3266fed88928b79(
    *,
    id: builtins.str,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7726205b43353108496846bc1f02062590e018e95fc96e11e69453af71727ed0(
    *,
    type: builtins.str,
    config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetGroup.TargetGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetGroup.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
