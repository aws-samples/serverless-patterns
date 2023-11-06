'''
# Amazon Pinpoint Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_pinpoint as pinpoint
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Pinpoint construct libraries](https://constructs.dev/search?q=pinpoint)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Pinpoint resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Pinpoint.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Pinpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Pinpoint.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnADMChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnADMChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    You can use the ADM channel to send push notifications through the Amazon Device Messaging (ADM) service to apps that run on Amazon devices, such as Kindle Fire tablets. Before you can use Amazon Pinpoint to send messages to Amazon devices, you have to enable the ADM channel for an Amazon Pinpoint application.

    The ADMChannel resource represents the status and authentication settings for the ADM channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_aDMChannel = pinpoint.CfnADMChannel(self, "MyCfnADMChannel",
            application_id="applicationId",
            client_id="clientId",
            client_secret="clientSecret",
        
            # the properties below are optional
            enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that the ADM channel applies to.
        :param client_id: The Client ID that you received from Amazon to send messages by using ADM.
        :param client_secret: The Client Secret that you received from Amazon to send messages by using ADM.
        :param enabled: Specifies whether to enable the ADM channel for the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf704e00bb5859cb830fbb4d1e376040266671aa90e04a47641d8d055085dae)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnADMChannelProps(
            application_id=application_id,
            client_id=client_id,
            client_secret=client_secret,
            enabled=enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6370d32f16b93db7c704589cdcc432969bf4bb7eecdf1c1ecce61abeb6703b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d7f38c58309e10d9e9c3e9cdd18ecdf0206a62dafe257a225fce81498a09d52)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the ADM channel applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__516a9ba4b7757af253ff004793a1979569edace2e0341aecf95d98ab8878fb7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        '''The Client ID that you received from Amazon to send messages by using ADM.'''
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ca2b0ebc55a347f1c856351a7ea66aa33f15336b7c29ebd44c657ad1e32c50f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        '''The Client Secret that you received from Amazon to send messages by using ADM.'''
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43ceab49423ae46becea7c2f42867ef5034b7107d6f0e0def0f82103c810cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the ADM channel for the application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29f9495da313043ed76a0fcbe057cba0bc82dd16c11f653c0c4ce29add3f3d6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnADMChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "enabled": "enabled",
    },
)
class CfnADMChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnADMChannel``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that the ADM channel applies to.
        :param client_id: The Client ID that you received from Amazon to send messages by using ADM.
        :param client_secret: The Client Secret that you received from Amazon to send messages by using ADM.
        :param enabled: Specifies whether to enable the ADM channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_aDMChannel_props = pinpoint.CfnADMChannelProps(
                application_id="applicationId",
                client_id="clientId",
                client_secret="clientSecret",
            
                # the properties below are optional
                enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ae5a29f3b4adfec5b1c827ee1bea8d33d99e697476ac7b7f9b8fea86b0bfc8)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the ADM channel applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The Client ID that you received from Amazon to send messages by using ADM.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientid
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''The Client Secret that you received from Amazon to send messages by using ADM.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientsecret
        '''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the ADM channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnADMChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAPNSChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAPNSChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    You can use the APNs channel to send push notification messages to the Apple Push Notification service (APNs). Before you can use Amazon Pinpoint to send notifications to APNs, you have to enable the APNs channel for an Amazon Pinpoint application.

    The APNSChannel resource represents the status and authentication settings for the APNs channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_aPNSChannel = pinpoint.CfnAPNSChannel(self, "MyCfnAPNSChannel",
            application_id="applicationId",
        
            # the properties below are optional
            bundle_id="bundleId",
            certificate="certificate",
            default_authentication_method="defaultAuthenticationMethod",
            enabled=False,
            private_key="privateKey",
            team_id="teamId",
            token_key="tokenKey",
            token_key_id="tokenKeyId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that the APNs channel applies to.
        :param bundle_id: The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
        :param certificate: The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.
        :param default_authentication_method: The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are ``key`` or ``certificate`` .
        :param enabled: Specifies whether to enable the APNs channel for the application.
        :param private_key: The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.
        :param team_id: The identifier that's assigned to your Apple Developer Account team. This identifier is used for APNs tokens.
        :param token_key: The authentication key to use for APNs tokens.
        :param token_key_id: The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c6d01d6ac4514b60aaeb636fa32c4f2935eb954acb47fe1f335948796c5b38)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAPNSChannelProps(
            application_id=application_id,
            bundle_id=bundle_id,
            certificate=certificate,
            default_authentication_method=default_authentication_method,
            enabled=enabled,
            private_key=private_key,
            team_id=team_id,
            token_key=token_key,
            token_key_id=token_key_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ef2edffbfaec89f01e614ae0d36665094bca9d2873273de72ca37709500647)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1dd87eeeb0b6f658fbf73ac4ee0a5ce23911fd99d4342fd6e60ca8b210fdb972)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the APNs channel applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ec692a61d1b998fa192954294bd412c7117bc611c68ba50855c6b11be36d360)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''The bundle identifier that's assigned to your iOS app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fdc4ba23303245bc510c4bc0780d997ced5645298a9309ce4a0b668e50b681f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleId", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The APNs client certificate that you received from Apple.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b2b358bd8e58ccda4eaae0530a3da766174cc23bb14dcbe422279e23ffc7c5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAuthenticationMethod"))

    @default_authentication_method.setter
    def default_authentication_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3201f885e965d3cbc3fd27f17ec2f46000a5ba9bfe7044238c7ddcab8c78d33a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAuthenticationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the APNs channel for the application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ed3ad95420b6948df7339f9eb6816bcaed443dfcee74ef7485882c3fc6c9be2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e32129c9e89fe5fb120406d63eb937f83ada047a3a02266a6a4b77dd025f761d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that's assigned to your Apple Developer Account team.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__126052989c39a52610fc6e54340c3dfe4273d45aa56b9ee0096604832a8af83f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKey")
    def token_key(self) -> typing.Optional[builtins.str]:
        '''The authentication key to use for APNs tokens.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKey"))

    @token_key.setter
    def token_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c68905895fc14733013b7072172056341167e4e6fbde6cccac5d4da6a970a70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKey", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKeyId")
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''The key identifier that's assigned to your APNs signing key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyId"))

    @token_key_id.setter
    def token_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e111ff96fa2864617af9bc1196e6a5c0f42a455a826bc67955c67c9e02a60ff0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKeyId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAPNSChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "bundle_id": "bundleId",
        "certificate": "certificate",
        "default_authentication_method": "defaultAuthenticationMethod",
        "enabled": "enabled",
        "private_key": "privateKey",
        "team_id": "teamId",
        "token_key": "tokenKey",
        "token_key_id": "tokenKeyId",
    },
)
class CfnAPNSChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAPNSChannel``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that the APNs channel applies to.
        :param bundle_id: The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
        :param certificate: The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.
        :param default_authentication_method: The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are ``key`` or ``certificate`` .
        :param enabled: Specifies whether to enable the APNs channel for the application.
        :param private_key: The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.
        :param team_id: The identifier that's assigned to your Apple Developer Account team. This identifier is used for APNs tokens.
        :param token_key: The authentication key to use for APNs tokens.
        :param token_key_id: The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_aPNSChannel_props = pinpoint.CfnAPNSChannelProps(
                application_id="applicationId",
            
                # the properties below are optional
                bundle_id="bundleId",
                certificate="certificate",
                default_authentication_method="defaultAuthenticationMethod",
                enabled=False,
                private_key="privateKey",
                team_id="teamId",
                token_key="tokenKey",
                token_key_id="tokenKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68cad147d39b410bb9ad20221185a1521986df7fc3b2870715568b76969e443f)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument bundle_id", value=bundle_id, expected_type=type_hints["bundle_id"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument default_authentication_method", value=default_authentication_method, expected_type=type_hints["default_authentication_method"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument token_key", value=token_key, expected_type=type_hints["token_key"])
            check_type(argname="argument token_key_id", value=token_key_id, expected_type=type_hints["token_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }
        if bundle_id is not None:
            self._values["bundle_id"] = bundle_id
        if certificate is not None:
            self._values["certificate"] = certificate
        if default_authentication_method is not None:
            self._values["default_authentication_method"] = default_authentication_method
        if enabled is not None:
            self._values["enabled"] = enabled
        if private_key is not None:
            self._values["private_key"] = private_key
        if team_id is not None:
            self._values["team_id"] = team_id
        if token_key is not None:
            self._values["token_key"] = token_key
        if token_key_id is not None:
            self._values["token_key_id"] = token_key_id

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the APNs channel applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''The bundle identifier that's assigned to your iOS app.

        This identifier is used for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-bundleid
        '''
        result = self._values.get("bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The APNs client certificate that you received from Apple.

        Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs.

        Valid options are ``key`` or ``certificate`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-defaultauthenticationmethod
        '''
        result = self._values.get("default_authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the APNs channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that's assigned to your Apple Developer Account team.

        This identifier is used for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-teamid
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key(self) -> typing.Optional[builtins.str]:
        '''The authentication key to use for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkey
        '''
        result = self._values.get("token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''The key identifier that's assigned to your APNs signing key.

        Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkeyid
        '''
        result = self._values.get("token_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPNSChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAPNSSandboxChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAPNSSandboxChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    You can use the APNs sandbox channel to send push notification messages to the sandbox environment of the Apple Push Notification service (APNs). Before you can use Amazon Pinpoint to send notifications to the APNs sandbox environment, you have to enable the APNs sandbox channel for an Amazon Pinpoint application.

    The APNSSandboxChannel resource represents the status and authentication settings of the APNs sandbox channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_aPNSSandbox_channel = pinpoint.CfnAPNSSandboxChannel(self, "MyCfnAPNSSandboxChannel",
            application_id="applicationId",
        
            # the properties below are optional
            bundle_id="bundleId",
            certificate="certificate",
            default_authentication_method="defaultAuthenticationMethod",
            enabled=False,
            private_key="privateKey",
            team_id="teamId",
            token_key="tokenKey",
            token_key_id="tokenKeyId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that the APNs sandbox channel applies to.
        :param bundle_id: The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
        :param certificate: The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.
        :param default_authentication_method: The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are ``key`` or ``certificate`` .
        :param enabled: Specifies whether to enable the APNs Sandbox channel for the Amazon Pinpoint application.
        :param private_key: The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.
        :param team_id: The identifier that's assigned to your Apple Developer Account team. This identifier is used for APNs tokens.
        :param token_key: The authentication key to use for APNs tokens.
        :param token_key_id: The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2cdf1bd0828fb196281b0c6e09fb772d25d46b1f609996c702cd33ded3923dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAPNSSandboxChannelProps(
            application_id=application_id,
            bundle_id=bundle_id,
            certificate=certificate,
            default_authentication_method=default_authentication_method,
            enabled=enabled,
            private_key=private_key,
            team_id=team_id,
            token_key=token_key,
            token_key_id=token_key_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9afd220964f59a3aa7c276349cbfbe0194a39fc3cc38e67756b3372dc695d32)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63e4d9ee78998839059ebfdb4c7eec999776002f59a110424dcbdbbf354898ec)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the APNs sandbox channel applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e3a391d32b5c7c832ea76d26b3ce0f36d370d03206b1ef42defc87b6ecd1656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''The bundle identifier that's assigned to your iOS app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c13e391d9c40b56efef97e70420259e3f16f091119a589e3cb14cde7fbcffb5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleId", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The APNs client certificate that you received from Apple.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d929856dc7781e860f17aa023d8a01e0cb7f1ec7cb93f928f78a77e4c76991a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAuthenticationMethod"))

    @default_authentication_method.setter
    def default_authentication_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72936dce4a9d9b3355d20141e15f0e706016979a3653c66d8027d3c7b0ee03d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAuthenticationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the APNs Sandbox channel for the Amazon Pinpoint application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4666c0e59b9ee82106f0a8a6fe42b502df677f3d4e454cc2c1d8a8c3dc1e8d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__348e545ce1c804626ae2b2b83b8cccbc3635d89315ef72cfc11baf2cad881c10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that's assigned to your Apple Developer Account team.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b8fd4f8d072de699b28339406a81391b189fddec1b0bbd68f9faec4d296b070)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKey")
    def token_key(self) -> typing.Optional[builtins.str]:
        '''The authentication key to use for APNs tokens.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKey"))

    @token_key.setter
    def token_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__622ff057d2fa4cb1f10160e466a9f238a6f82b2da34b6a446ac4789934351392)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKey", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKeyId")
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''The key identifier that's assigned to your APNs signing key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyId"))

    @token_key_id.setter
    def token_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a1c83d822fd7f724c76e48f4fadc86e26cedf4936d86d6a2d5600e9949b8e2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKeyId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAPNSSandboxChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "bundle_id": "bundleId",
        "certificate": "certificate",
        "default_authentication_method": "defaultAuthenticationMethod",
        "enabled": "enabled",
        "private_key": "privateKey",
        "team_id": "teamId",
        "token_key": "tokenKey",
        "token_key_id": "tokenKeyId",
    },
)
class CfnAPNSSandboxChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAPNSSandboxChannel``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that the APNs sandbox channel applies to.
        :param bundle_id: The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
        :param certificate: The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.
        :param default_authentication_method: The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are ``key`` or ``certificate`` .
        :param enabled: Specifies whether to enable the APNs Sandbox channel for the Amazon Pinpoint application.
        :param private_key: The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.
        :param team_id: The identifier that's assigned to your Apple Developer Account team. This identifier is used for APNs tokens.
        :param token_key: The authentication key to use for APNs tokens.
        :param token_key_id: The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_aPNSSandbox_channel_props = pinpoint.CfnAPNSSandboxChannelProps(
                application_id="applicationId",
            
                # the properties below are optional
                bundle_id="bundleId",
                certificate="certificate",
                default_authentication_method="defaultAuthenticationMethod",
                enabled=False,
                private_key="privateKey",
                team_id="teamId",
                token_key="tokenKey",
                token_key_id="tokenKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3609ffaa3fba04e4ff88045f06f94408c36907fca82875dc1aab7ae3cba1f30a)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument bundle_id", value=bundle_id, expected_type=type_hints["bundle_id"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument default_authentication_method", value=default_authentication_method, expected_type=type_hints["default_authentication_method"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument token_key", value=token_key, expected_type=type_hints["token_key"])
            check_type(argname="argument token_key_id", value=token_key_id, expected_type=type_hints["token_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }
        if bundle_id is not None:
            self._values["bundle_id"] = bundle_id
        if certificate is not None:
            self._values["certificate"] = certificate
        if default_authentication_method is not None:
            self._values["default_authentication_method"] = default_authentication_method
        if enabled is not None:
            self._values["enabled"] = enabled
        if private_key is not None:
            self._values["private_key"] = private_key
        if team_id is not None:
            self._values["team_id"] = team_id
        if token_key is not None:
            self._values["token_key"] = token_key
        if token_key_id is not None:
            self._values["token_key_id"] = token_key_id

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the APNs sandbox channel applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''The bundle identifier that's assigned to your iOS app.

        This identifier is used for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-bundleid
        '''
        result = self._values.get("bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The APNs client certificate that you received from Apple.

        Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs.

        Valid options are ``key`` or ``certificate`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-defaultauthenticationmethod
        '''
        result = self._values.get("default_authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the APNs Sandbox channel for the Amazon Pinpoint application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that's assigned to your Apple Developer Account team.

        This identifier is used for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-teamid
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key(self) -> typing.Optional[builtins.str]:
        '''The authentication key to use for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkey
        '''
        result = self._values.get("token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''The key identifier that's assigned to your APNs signing key.

        Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkeyid
        '''
        result = self._values.get("token_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPNSSandboxChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAPNSVoipChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAPNSVoipChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    You can use the APNs VoIP channel to send VoIP notification messages to the Apple Push Notification service (APNs). Before you can use Amazon Pinpoint to send VoIP notifications to APNs, you have to enable the APNs VoIP channel for an Amazon Pinpoint application.

    The APNSVoipChannel resource represents the status and authentication settings of the APNs VoIP channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_aPNSVoip_channel = pinpoint.CfnAPNSVoipChannel(self, "MyCfnAPNSVoipChannel",
            application_id="applicationId",
        
            # the properties below are optional
            bundle_id="bundleId",
            certificate="certificate",
            default_authentication_method="defaultAuthenticationMethod",
            enabled=False,
            private_key="privateKey",
            team_id="teamId",
            token_key="tokenKey",
            token_key_id="tokenKeyId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that the APNs VoIP channel applies to.
        :param bundle_id: The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
        :param certificate: The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.
        :param default_authentication_method: The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are ``key`` or ``certificate`` .
        :param enabled: Specifies whether to enable the APNs VoIP channel for the Amazon Pinpoint application.
        :param private_key: The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.
        :param team_id: The identifier that's assigned to your Apple Developer Account team. This identifier is used for APNs tokens.
        :param token_key: The authentication key to use for APNs tokens.
        :param token_key_id: The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__354fbb51dc05a5c7b142870475ffebba049d56e406e383a83bcdf9e1205f7e3a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAPNSVoipChannelProps(
            application_id=application_id,
            bundle_id=bundle_id,
            certificate=certificate,
            default_authentication_method=default_authentication_method,
            enabled=enabled,
            private_key=private_key,
            team_id=team_id,
            token_key=token_key,
            token_key_id=token_key_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c295e4c7ef221f73636feb125bd7e1fe6267e5dbbe723147da0cdae19845d8e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__04703119f79d8184e97b28f75a030ff15aca233258d881aa000b618281a64d0d)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the APNs VoIP channel applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d8cf83888d2c3bcb29e553a924bf2bb2b5423243bfd76ff45039cec94c4203f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''The bundle identifier that's assigned to your iOS app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ef79ce48a4708565800ada7142b5f84f70dba36f6631fea19ceabe5dae7c09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleId", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The APNs client certificate that you received from Apple.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d72c80d8e62631c30f10c530f1e875432ad32c73b6aeba9bb7bb054e1c4fa878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAuthenticationMethod"))

    @default_authentication_method.setter
    def default_authentication_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c7e303ad6e775381a9141f9cfef12089fa928c85c8a8b45394b4a0670e83e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAuthenticationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the APNs VoIP channel for the Amazon Pinpoint application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29971c6564c0a97fcd5481816c5791d2527814f70f07c3dc75b5bdd5f178679)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52ffc29c2e58a29c36ceeb81a921d67080e931e597c389630a2a8b8bb4605bf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that's assigned to your Apple Developer Account team.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5795637c70bd87670d111ed19a94136ea8689882020ecd1f2b3a9ca1dc588adc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKey")
    def token_key(self) -> typing.Optional[builtins.str]:
        '''The authentication key to use for APNs tokens.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKey"))

    @token_key.setter
    def token_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a763a314ff762c118e43a2503d59c9db34d817fcbe98b899a2695c1da28a6cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKey", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKeyId")
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''The key identifier that's assigned to your APNs signing key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyId"))

    @token_key_id.setter
    def token_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46127dd7405f371138f3f8925f703cbdf74dc4d1920b57b2c4046a9f4c8678c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKeyId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAPNSVoipChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "bundle_id": "bundleId",
        "certificate": "certificate",
        "default_authentication_method": "defaultAuthenticationMethod",
        "enabled": "enabled",
        "private_key": "privateKey",
        "team_id": "teamId",
        "token_key": "tokenKey",
        "token_key_id": "tokenKeyId",
    },
)
class CfnAPNSVoipChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAPNSVoipChannel``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that the APNs VoIP channel applies to.
        :param bundle_id: The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
        :param certificate: The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.
        :param default_authentication_method: The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are ``key`` or ``certificate`` .
        :param enabled: Specifies whether to enable the APNs VoIP channel for the Amazon Pinpoint application.
        :param private_key: The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.
        :param team_id: The identifier that's assigned to your Apple Developer Account team. This identifier is used for APNs tokens.
        :param token_key: The authentication key to use for APNs tokens.
        :param token_key_id: The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_aPNSVoip_channel_props = pinpoint.CfnAPNSVoipChannelProps(
                application_id="applicationId",
            
                # the properties below are optional
                bundle_id="bundleId",
                certificate="certificate",
                default_authentication_method="defaultAuthenticationMethod",
                enabled=False,
                private_key="privateKey",
                team_id="teamId",
                token_key="tokenKey",
                token_key_id="tokenKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2515eaa7a5b0f17c9115c41e25d7466476c5fc2356786c269e03db415b0b6a0)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument bundle_id", value=bundle_id, expected_type=type_hints["bundle_id"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument default_authentication_method", value=default_authentication_method, expected_type=type_hints["default_authentication_method"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument token_key", value=token_key, expected_type=type_hints["token_key"])
            check_type(argname="argument token_key_id", value=token_key_id, expected_type=type_hints["token_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }
        if bundle_id is not None:
            self._values["bundle_id"] = bundle_id
        if certificate is not None:
            self._values["certificate"] = certificate
        if default_authentication_method is not None:
            self._values["default_authentication_method"] = default_authentication_method
        if enabled is not None:
            self._values["enabled"] = enabled
        if private_key is not None:
            self._values["private_key"] = private_key
        if team_id is not None:
            self._values["team_id"] = team_id
        if token_key is not None:
            self._values["token_key"] = token_key
        if token_key_id is not None:
            self._values["token_key_id"] = token_key_id

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the APNs VoIP channel applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''The bundle identifier that's assigned to your iOS app.

        This identifier is used for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-bundleid
        '''
        result = self._values.get("bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The APNs client certificate that you received from Apple.

        Specify this value if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs.

        Valid options are ``key`` or ``certificate`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-defaultauthenticationmethod
        '''
        result = self._values.get("default_authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the APNs VoIP channel for the Amazon Pinpoint application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that's assigned to your Apple Developer Account team.

        This identifier is used for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-teamid
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key(self) -> typing.Optional[builtins.str]:
        '''The authentication key to use for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkey
        '''
        result = self._values.get("token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''The key identifier that's assigned to your APNs signing key.

        Specify this value if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkeyid
        '''
        result = self._values.get("token_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPNSVoipChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAPNSVoipSandboxChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAPNSVoipSandboxChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    You can use the APNs VoIP sandbox channel to send VoIP notification messages to the sandbox environment of the Apple Push Notification service (APNs). Before you can use Amazon Pinpoint to send VoIP notifications to the APNs sandbox environment, you have to enable the APNs VoIP sandbox channel for an Amazon Pinpoint application.

    The APNSVoipSandboxChannel resource represents the status and authentication settings of the APNs VoIP sandbox channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_aPNSVoip_sandbox_channel = pinpoint.CfnAPNSVoipSandboxChannel(self, "MyCfnAPNSVoipSandboxChannel",
            application_id="applicationId",
        
            # the properties below are optional
            bundle_id="bundleId",
            certificate="certificate",
            default_authentication_method="defaultAuthenticationMethod",
            enabled=False,
            private_key="privateKey",
            team_id="teamId",
            token_key="tokenKey",
            token_key_id="tokenKeyId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the application that the APNs VoIP sandbox channel applies to.
        :param bundle_id: The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
        :param certificate: The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with the APNs sandbox environment by using an APNs certificate.
        :param default_authentication_method: The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are ``key`` or ``certificate`` .
        :param enabled: Specifies whether the APNs VoIP sandbox channel is enabled for the application.
        :param private_key: The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with the APNs sandbox environment.
        :param team_id: The identifier that's assigned to your Apple developer account team. This identifier is used for APNs tokens.
        :param token_key: The authentication key to use for APNs tokens.
        :param token_key_id: The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with the APNs sandbox environment by using APNs tokens.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda00a8216a1537d1791cebffe3e648359ad880fd824bfd90472a552cf2f17a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAPNSVoipSandboxChannelProps(
            application_id=application_id,
            bundle_id=bundle_id,
            certificate=certificate,
            default_authentication_method=default_authentication_method,
            enabled=enabled,
            private_key=private_key,
            team_id=team_id,
            token_key=token_key,
            token_key_id=token_key_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b73a7955f3c2112f01b23293d78c4a55e7bf14ae478719955fa7bbf05e013cba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22adf58a327644519c6703d2838a632c1d54b15bced0304f64e2c1f588f54bcf)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the application that the APNs VoIP sandbox channel applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350373fee7f7d95897dd93a64ed1fba8e5c7633cc24c346e6eae6f6f8022ca85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''The bundle identifier that's assigned to your iOS app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adacd8b3feedf89d701eb54dc830cd89599763f610af1ab0ddae724bd2b9ab9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleId", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The APNs client certificate that you received from Apple.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186164a38f8208bb7b7f4347d8ffc572fd4d74da65ed43f189482ccb05e0b9e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAuthenticationMethod"))

    @default_authentication_method.setter
    def default_authentication_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f546750c5bd78ff62a69bbe58c6bd21bab499a931542106097f2be0e61b0738)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAuthenticationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the APNs VoIP sandbox channel is enabled for the application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac5c1ce5cc72d2472a9881976d507f68a31b18a54d9853cc07d5e5f47c1f566)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with the APNs sandbox environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c7912f617707f8a3bf055962376421068d396c4548da62240dea44b4d840a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that's assigned to your Apple developer account team.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b56d6aec3a3108d8b2afad8a6b2db8101173ab0c6faa42c50e79e0ad96fb3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKey")
    def token_key(self) -> typing.Optional[builtins.str]:
        '''The authentication key to use for APNs tokens.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKey"))

    @token_key.setter
    def token_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f79c9d0b861c37cd183ab0b80d916731b90ace98ab3e741d2de7cddce91497c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKey", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKeyId")
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''The key identifier that's assigned to your APNs signing key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyId"))

    @token_key_id.setter
    def token_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd15602c1b7a8a7fe5ed82c46d42d3b30e6bc52c8618e996139c2d1c461696f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKeyId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAPNSVoipSandboxChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "bundle_id": "bundleId",
        "certificate": "certificate",
        "default_authentication_method": "defaultAuthenticationMethod",
        "enabled": "enabled",
        "private_key": "privateKey",
        "team_id": "teamId",
        "token_key": "tokenKey",
        "token_key_id": "tokenKeyId",
    },
)
class CfnAPNSVoipSandboxChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAPNSVoipSandboxChannel``.

        :param application_id: The unique identifier for the application that the APNs VoIP sandbox channel applies to.
        :param bundle_id: The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens.
        :param certificate: The APNs client certificate that you received from Apple. Specify this value if you want Amazon Pinpoint to communicate with the APNs sandbox environment by using an APNs certificate.
        :param default_authentication_method: The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs. Valid options are ``key`` or ``certificate`` .
        :param enabled: Specifies whether the APNs VoIP sandbox channel is enabled for the application.
        :param private_key: The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with the APNs sandbox environment.
        :param team_id: The identifier that's assigned to your Apple developer account team. This identifier is used for APNs tokens.
        :param token_key: The authentication key to use for APNs tokens.
        :param token_key_id: The key identifier that's assigned to your APNs signing key. Specify this value if you want Amazon Pinpoint to communicate with the APNs sandbox environment by using APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_aPNSVoip_sandbox_channel_props = pinpoint.CfnAPNSVoipSandboxChannelProps(
                application_id="applicationId",
            
                # the properties below are optional
                bundle_id="bundleId",
                certificate="certificate",
                default_authentication_method="defaultAuthenticationMethod",
                enabled=False,
                private_key="privateKey",
                team_id="teamId",
                token_key="tokenKey",
                token_key_id="tokenKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c73c61658383943c9f8d75c0d3353564c42bbc4ebb21db0dbb12fd8e993b5ea4)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument bundle_id", value=bundle_id, expected_type=type_hints["bundle_id"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument default_authentication_method", value=default_authentication_method, expected_type=type_hints["default_authentication_method"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument token_key", value=token_key, expected_type=type_hints["token_key"])
            check_type(argname="argument token_key_id", value=token_key_id, expected_type=type_hints["token_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }
        if bundle_id is not None:
            self._values["bundle_id"] = bundle_id
        if certificate is not None:
            self._values["certificate"] = certificate
        if default_authentication_method is not None:
            self._values["default_authentication_method"] = default_authentication_method
        if enabled is not None:
            self._values["enabled"] = enabled
        if private_key is not None:
            self._values["private_key"] = private_key
        if team_id is not None:
            self._values["team_id"] = team_id
        if token_key is not None:
            self._values["token_key"] = token_key
        if token_key_id is not None:
            self._values["token_key_id"] = token_key_id

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the application that the APNs VoIP sandbox channel applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''The bundle identifier that's assigned to your iOS app.

        This identifier is used for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-bundleid
        '''
        result = self._values.get("bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The APNs client certificate that you received from Apple.

        Specify this value if you want Amazon Pinpoint to communicate with the APNs sandbox environment by using an APNs certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs.

        Valid options are ``key`` or ``certificate`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-defaultauthenticationmethod
        '''
        result = self._values.get("default_authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the APNs VoIP sandbox channel is enabled for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with the APNs sandbox environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that's assigned to your Apple developer account team.

        This identifier is used for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-teamid
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key(self) -> typing.Optional[builtins.str]:
        '''The authentication key to use for APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkey
        '''
        result = self._values.get("token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''The key identifier that's assigned to your APNs signing key.

        Specify this value if you want Amazon Pinpoint to communicate with the APNs sandbox environment by using APNs tokens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkeyid
        '''
        result = self._values.get("token_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPNSVoipSandboxChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnApp(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnApp",
):
    '''An *app* is an Amazon Pinpoint application, also referred to as a *project* .

    An application is a collection of related settings, customer information, segments, campaigns, and other types of Amazon Pinpoint resources.

    The App resource represents an Amazon Pinpoint application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        # tags: Any
        
        cfn_app = pinpoint.CfnApp(self, "MyCfnApp",
            name="name",
        
            # the properties below are optional
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The display name of the application.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0f8bd367843c451288aaaaf44baa44f09abffc0daba385520088889fd81e23)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a1a0b3dc0d592b65e802e1e0b8f6d8ec8f0dc7df60bf7d1633880668ff742e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__40e034d00b2f813e571c292acc2ff9b22e3caa8f934e8935b27235f80a809b8c)
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
        '''The Amazon Resource Name (ARN) of the application.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The display name of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cda5c7fde34ff297b3dd15ab1185cf7a20ee1de5b1dbc01014c4cdbc7628bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e084f2f5a25d396c8ccb2664d39e210e8baca99dd9f5b729df463e35b2565c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnAppProps:
    def __init__(self, *, name: builtins.str, tags: typing.Any = None) -> None:
        '''Properties for defining a ``CfnApp``.

        :param name: The display name of the application.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            # tags: Any
            
            cfn_app_props = pinpoint.CfnAppProps(
                name="name",
            
                # the properties below are optional
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5ece6d9985e2c12212269fba01e0f60516e87697766368b6a5343813fba618c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnApplicationSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnApplicationSettings",
):
    '''Specifies the settings for an Amazon Pinpoint application.

    In Amazon Pinpoint, an *application* (also referred to as an *app* or *project* ) is a collection of related settings, customer information, segments, and campaigns, and other types of Amazon Pinpoint resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_application_settings = pinpoint.CfnApplicationSettings(self, "MyCfnApplicationSettings",
            application_id="applicationId",
        
            # the properties below are optional
            campaign_hook=pinpoint.CfnApplicationSettings.CampaignHookProperty(
                lambda_function_name="lambdaFunctionName",
                mode="mode",
                web_url="webUrl"
            ),
            cloud_watch_metrics_enabled=False,
            limits=pinpoint.CfnApplicationSettings.LimitsProperty(
                daily=123,
                maximum_duration=123,
                messages_per_second=123,
                total=123
            ),
            quiet_time=pinpoint.CfnApplicationSettings.QuietTimeProperty(
                end="end",
                start="start"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        campaign_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplicationSettings.CampaignHookProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplicationSettings.LimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        quiet_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplicationSettings.QuietTimeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application.
        :param campaign_hook: The settings for the Lambda function to use by default as a code hook for campaigns in the application. To override these settings for a specific campaign, use the Campaign resource to define custom Lambda function settings for the campaign.
        :param cloud_watch_metrics_enabled: Specifies whether to enable application-related alarms in Amazon CloudWatch.
        :param limits: The default sending limits for campaigns in the application. To override these limits for a specific campaign, use the Campaign resource to define custom limits for the campaign.
        :param quiet_time: The default quiet time for campaigns in the application. Quiet time is a specific time range when campaigns don't send messages to endpoints, if all the following conditions are met: - The ``EndpointDemographic.Timezone`` property of the endpoint is set to a valid value. - The current time in the endpoint's time zone is later than or equal to the time specified by the ``QuietTime.Start`` property for the application (or a campaign that has custom quiet time settings). - The current time in the endpoint's time zone is earlier than or equal to the time specified by the ``QuietTime.End`` property for the application (or a campaign that has custom quiet time settings). If any of the preceding conditions isn't met, the endpoint will receive messages from a campaign, even if quiet time is enabled. To override the default quiet time settings for a specific campaign, use the Campaign resource to define a custom quiet time for the campaign.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fccaf1bda545922f59167d307e79647dd7b5a9bdb6a0d209e2ca4103d5382dec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationSettingsProps(
            application_id=application_id,
            campaign_hook=campaign_hook,
            cloud_watch_metrics_enabled=cloud_watch_metrics_enabled,
            limits=limits,
            quiet_time=quiet_time,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf14b6ff8c636cd9737f33917ef781db4b0cad7f678d53682c3daae1564d0f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab86b68966b26e641e0dc1136bda485826e3978c2c9073ea008e6b1ec19b32d2)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77178b3d447e29013b551ae5835b06acbc057abc44ff6d0ef62fba4da67d443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="campaignHook")
    def campaign_hook(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.CampaignHookProperty"]]:
        '''The settings for the Lambda function to use by default as a code hook for campaigns in the application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.CampaignHookProperty"]], jsii.get(self, "campaignHook"))

    @campaign_hook.setter
    def campaign_hook(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.CampaignHookProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5230c9c3bb4cc93dbcaf0c5e212a80abd53a33c7588270b53fc93dae0c27d139)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "campaignHook", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchMetricsEnabled")
    def cloud_watch_metrics_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable application-related alarms in Amazon CloudWatch.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "cloudWatchMetricsEnabled"))

    @cloud_watch_metrics_enabled.setter
    def cloud_watch_metrics_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__755097f5bd91236a9086d9ae0fa2948236768a3b8aa298efa8cb0b079e4f3406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchMetricsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="limits")
    def limits(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.LimitsProperty"]]:
        '''The default sending limits for campaigns in the application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.LimitsProperty"]], jsii.get(self, "limits"))

    @limits.setter
    def limits(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.LimitsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__160a20b435f7b6094f46c527888adf81437d233b9f3372717ff3235293b3cb53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limits", value)

    @builtins.property
    @jsii.member(jsii_name="quietTime")
    def quiet_time(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.QuietTimeProperty"]]:
        '''The default quiet time for campaigns in the application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.QuietTimeProperty"]], jsii.get(self, "quietTime"))

    @quiet_time.setter
    def quiet_time(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationSettings.QuietTimeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c87df35c4674de93532f2b097e8a5e8acc739757c089b203b35e483e743d6a56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quietTime", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnApplicationSettings.CampaignHookProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_function_name": "lambdaFunctionName",
            "mode": "mode",
            "web_url": "webUrl",
        },
    )
    class CampaignHookProperty:
        def __init__(
            self,
            *,
            lambda_function_name: typing.Optional[builtins.str] = None,
            mode: typing.Optional[builtins.str] = None,
            web_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the Lambda function to use by default as a code hook for campaigns in the application.

            :param lambda_function_name: The name or Amazon Resource Name (ARN) of the Lambda function that Amazon Pinpoint invokes to send messages for campaigns in the application.
            :param mode: The mode that Amazon Pinpoint uses to invoke the Lambda function. Possible values are:. - ``FILTER`` - Invoke the function to customize the segment that's used by a campaign. - ``DELIVERY`` - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the ``CustomDeliveryConfiguration`` and ``CampaignCustomMessage`` objects of the campaign.
            :param web_url: The web URL that Amazon Pinpoint calls to invoke the Lambda function over HTTPS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                campaign_hook_property = pinpoint.CfnApplicationSettings.CampaignHookProperty(
                    lambda_function_name="lambdaFunctionName",
                    mode="mode",
                    web_url="webUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3735fe29377ea2a62d3732e899a51c8a9e72347e64f199653047cab6f9d9506e)
                check_type(argname="argument lambda_function_name", value=lambda_function_name, expected_type=type_hints["lambda_function_name"])
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument web_url", value=web_url, expected_type=type_hints["web_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_function_name is not None:
                self._values["lambda_function_name"] = lambda_function_name
            if mode is not None:
                self._values["mode"] = mode
            if web_url is not None:
                self._values["web_url"] = web_url

        @builtins.property
        def lambda_function_name(self) -> typing.Optional[builtins.str]:
            '''The name or Amazon Resource Name (ARN) of the Lambda function that Amazon Pinpoint invokes to send messages for campaigns in the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-lambdafunctionname
            '''
            result = self._values.get("lambda_function_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''The mode that Amazon Pinpoint uses to invoke the Lambda function. Possible values are:.

            - ``FILTER`` - Invoke the function to customize the segment that's used by a campaign.
            - ``DELIVERY`` - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the ``CustomDeliveryConfiguration`` and ``CampaignCustomMessage`` objects of the campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def web_url(self) -> typing.Optional[builtins.str]:
            '''The web URL that Amazon Pinpoint calls to invoke the Lambda function over HTTPS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-weburl
            '''
            result = self._values.get("web_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnApplicationSettings.LimitsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "daily": "daily",
            "maximum_duration": "maximumDuration",
            "messages_per_second": "messagesPerSecond",
            "total": "total",
        },
    )
    class LimitsProperty:
        def __init__(
            self,
            *,
            daily: typing.Optional[jsii.Number] = None,
            maximum_duration: typing.Optional[jsii.Number] = None,
            messages_per_second: typing.Optional[jsii.Number] = None,
            total: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the default sending limits for campaigns in the application.

            :param daily: The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. The maximum value is 100.
            :param maximum_duration: The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds.
            :param messages_per_second: The maximum number of messages that a campaign can send each second. The minimum value is 1. The maximum value is 20,000.
            :param total: The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. The maximum value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                limits_property = pinpoint.CfnApplicationSettings.LimitsProperty(
                    daily=123,
                    maximum_duration=123,
                    messages_per_second=123,
                    total=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b567fc1a36320c43d98124a1a42b18b1cf5865a4a20180bd858cfdbdddb76c0)
                check_type(argname="argument daily", value=daily, expected_type=type_hints["daily"])
                check_type(argname="argument maximum_duration", value=maximum_duration, expected_type=type_hints["maximum_duration"])
                check_type(argname="argument messages_per_second", value=messages_per_second, expected_type=type_hints["messages_per_second"])
                check_type(argname="argument total", value=total, expected_type=type_hints["total"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if daily is not None:
                self._values["daily"] = daily
            if maximum_duration is not None:
                self._values["maximum_duration"] = maximum_duration
            if messages_per_second is not None:
                self._values["messages_per_second"] = messages_per_second
            if total is not None:
                self._values["total"] = total

        @builtins.property
        def daily(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period.

            The maximum value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-daily
            '''
            result = self._values.get("daily")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_duration(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign.

            The minimum value is 60 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-maximumduration
            '''
            result = self._values.get("maximum_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def messages_per_second(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of messages that a campaign can send each second.

            The minimum value is 1. The maximum value is 20,000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-messagespersecond
            '''
            result = self._values.get("messages_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign.

            The maximum value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-total
            '''
            result = self._values.get("total")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnApplicationSettings.QuietTimeProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class QuietTimeProperty:
        def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
            '''Specifies the start and end times that define a time range when messages aren't sent to endpoints.

            :param end: The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use ``02:30`` to represent 2:30 AM, or ``14:30`` to represent 2:30 PM.
            :param start: The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use ``02:30`` to represent 2:30 AM, or ``14:30`` to represent 2:30 PM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                quiet_time_property = pinpoint.CfnApplicationSettings.QuietTimeProperty(
                    end="end",
                    start="start"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8f1c3eef4ae7697239fc1a13ba90492d492b7d5021e1b6b4bbdda3168071fee)
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
                check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end": end,
                "start": start,
            }

        @builtins.property
        def end(self) -> builtins.str:
            '''The specific time when quiet time ends.

            This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use ``02:30`` to represent 2:30 AM, or ``14:30`` to represent 2:30 PM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start(self) -> builtins.str:
            '''The specific time when quiet time begins.

            This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use ``02:30`` to represent 2:30 AM, or ``14:30`` to represent 2:30 PM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-start
            '''
            result = self._values.get("start")
            assert result is not None, "Required property 'start' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuietTimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnApplicationSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "campaign_hook": "campaignHook",
        "cloud_watch_metrics_enabled": "cloudWatchMetricsEnabled",
        "limits": "limits",
        "quiet_time": "quietTime",
    },
)
class CfnApplicationSettingsProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        campaign_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.CampaignHookProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.LimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        quiet_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.QuietTimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplicationSettings``.

        :param application_id: The unique identifier for the Amazon Pinpoint application.
        :param campaign_hook: The settings for the Lambda function to use by default as a code hook for campaigns in the application. To override these settings for a specific campaign, use the Campaign resource to define custom Lambda function settings for the campaign.
        :param cloud_watch_metrics_enabled: Specifies whether to enable application-related alarms in Amazon CloudWatch.
        :param limits: The default sending limits for campaigns in the application. To override these limits for a specific campaign, use the Campaign resource to define custom limits for the campaign.
        :param quiet_time: The default quiet time for campaigns in the application. Quiet time is a specific time range when campaigns don't send messages to endpoints, if all the following conditions are met: - The ``EndpointDemographic.Timezone`` property of the endpoint is set to a valid value. - The current time in the endpoint's time zone is later than or equal to the time specified by the ``QuietTime.Start`` property for the application (or a campaign that has custom quiet time settings). - The current time in the endpoint's time zone is earlier than or equal to the time specified by the ``QuietTime.End`` property for the application (or a campaign that has custom quiet time settings). If any of the preceding conditions isn't met, the endpoint will receive messages from a campaign, even if quiet time is enabled. To override the default quiet time settings for a specific campaign, use the Campaign resource to define a custom quiet time for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_application_settings_props = pinpoint.CfnApplicationSettingsProps(
                application_id="applicationId",
            
                # the properties below are optional
                campaign_hook=pinpoint.CfnApplicationSettings.CampaignHookProperty(
                    lambda_function_name="lambdaFunctionName",
                    mode="mode",
                    web_url="webUrl"
                ),
                cloud_watch_metrics_enabled=False,
                limits=pinpoint.CfnApplicationSettings.LimitsProperty(
                    daily=123,
                    maximum_duration=123,
                    messages_per_second=123,
                    total=123
                ),
                quiet_time=pinpoint.CfnApplicationSettings.QuietTimeProperty(
                    end="end",
                    start="start"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__848467a4d3edb707abe4565a3db11fcd50755d6c664897537827d7e2003fb02d)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument campaign_hook", value=campaign_hook, expected_type=type_hints["campaign_hook"])
            check_type(argname="argument cloud_watch_metrics_enabled", value=cloud_watch_metrics_enabled, expected_type=type_hints["cloud_watch_metrics_enabled"])
            check_type(argname="argument limits", value=limits, expected_type=type_hints["limits"])
            check_type(argname="argument quiet_time", value=quiet_time, expected_type=type_hints["quiet_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }
        if campaign_hook is not None:
            self._values["campaign_hook"] = campaign_hook
        if cloud_watch_metrics_enabled is not None:
            self._values["cloud_watch_metrics_enabled"] = cloud_watch_metrics_enabled
        if limits is not None:
            self._values["limits"] = limits
        if quiet_time is not None:
            self._values["quiet_time"] = quiet_time

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def campaign_hook(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.CampaignHookProperty]]:
        '''The settings for the Lambda function to use by default as a code hook for campaigns in the application.

        To override these settings for a specific campaign, use the Campaign resource to define custom Lambda function settings for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-campaignhook
        '''
        result = self._values.get("campaign_hook")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.CampaignHookProperty]], result)

    @builtins.property
    def cloud_watch_metrics_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable application-related alarms in Amazon CloudWatch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-cloudwatchmetricsenabled
        '''
        result = self._values.get("cloud_watch_metrics_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def limits(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.LimitsProperty]]:
        '''The default sending limits for campaigns in the application.

        To override these limits for a specific campaign, use the Campaign resource to define custom limits for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-limits
        '''
        result = self._values.get("limits")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.LimitsProperty]], result)

    @builtins.property
    def quiet_time(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.QuietTimeProperty]]:
        '''The default quiet time for campaigns in the application.

        Quiet time is a specific time range when campaigns don't send messages to endpoints, if all the following conditions are met:

        - The ``EndpointDemographic.Timezone`` property of the endpoint is set to a valid value.
        - The current time in the endpoint's time zone is later than or equal to the time specified by the ``QuietTime.Start`` property for the application (or a campaign that has custom quiet time settings).
        - The current time in the endpoint's time zone is earlier than or equal to the time specified by the ``QuietTime.End`` property for the application (or a campaign that has custom quiet time settings).

        If any of the preceding conditions isn't met, the endpoint will receive messages from a campaign, even if quiet time is enabled.

        To override the default quiet time settings for a specific campaign, use the Campaign resource to define a custom quiet time for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-quiettime
        '''
        result = self._values.get("quiet_time")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.QuietTimeProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnBaiduChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnBaiduChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    You can use the Baidu channel to send notifications to the Baidu Cloud Push notification service. Before you can use Amazon Pinpoint to send notifications to the Baidu Cloud Push service, you have to enable the Baidu channel for an Amazon Pinpoint application.

    The BaiduChannel resource represents the status and authentication settings of the Baidu channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_baidu_channel = pinpoint.CfnBaiduChannel(self, "MyCfnBaiduChannel",
            api_key="apiKey",
            application_id="applicationId",
            secret_key="secretKey",
        
            # the properties below are optional
            enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        application_id: builtins.str,
        secret_key: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_key: The API key that you received from the Baidu Cloud Push service to communicate with the service.
        :param application_id: The unique identifier for the Amazon Pinpoint application that you're configuring the Baidu channel for.
        :param secret_key: The secret key that you received from the Baidu Cloud Push service to communicate with the service.
        :param enabled: Specifies whether to enable the Baidu channel for the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87a51d70a760e3a97ac0ecff0ea42b251dacb1982201c515754052b0924b8e68)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBaiduChannelProps(
            api_key=api_key,
            application_id=application_id,
            secret_key=secret_key,
            enabled=enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d887fd5e4f274a7c9f9fb685c04f9829ef3a76fa07377a74cc728de290ff58b5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3559f4e7df7dcb2b8e21ae2606a6d30ab6d91b28c6e5d05bcd80f01ac1b85bc)
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
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        '''The API key that you received from the Baidu Cloud Push service to communicate with the service.'''
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d55ab74c3304a8f7ee5eb7755db2b7575dede417448da381789b65757a6e26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that you're configuring the Baidu channel for.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdcdb9cb03617bf41a449212c19519749eeb4eac75fa6316b5c70055f4067c20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        '''The secret key that you received from the Baidu Cloud Push service to communicate with the service.'''
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__985764c1478c22f92314f563a4e1501861497b260954b0683c149c92a0325375)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the Baidu channel for the application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__322e2fecb20c91419f0797aeaab2607597e674c854ce690ae78042ae1dd3e42f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnBaiduChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "application_id": "applicationId",
        "secret_key": "secretKey",
        "enabled": "enabled",
    },
)
class CfnBaiduChannelProps:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        application_id: builtins.str,
        secret_key: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBaiduChannel``.

        :param api_key: The API key that you received from the Baidu Cloud Push service to communicate with the service.
        :param application_id: The unique identifier for the Amazon Pinpoint application that you're configuring the Baidu channel for.
        :param secret_key: The secret key that you received from the Baidu Cloud Push service to communicate with the service.
        :param enabled: Specifies whether to enable the Baidu channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_baidu_channel_props = pinpoint.CfnBaiduChannelProps(
                api_key="apiKey",
                application_id="applicationId",
                secret_key="secretKey",
            
                # the properties below are optional
                enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea99679b99d64e9a67176579da7115a89002eb9da18df44b574208277637df1c)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
            "application_id": application_id,
            "secret_key": secret_key,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def api_key(self) -> builtins.str:
        '''The API key that you received from the Baidu Cloud Push service to communicate with the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-apikey
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that you're configuring the Baidu channel for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_key(self) -> builtins.str:
        '''The secret key that you received from the Baidu Cloud Push service to communicate with the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-secretkey
        '''
        result = self._values.get("secret_key")
        assert result is not None, "Required property 'secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the Baidu channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBaiduChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCampaign(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign",
):
    '''Specifies the settings for a campaign.

    A *campaign* is a messaging initiative that engages a specific segment of users for an Amazon Pinpoint application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        # attributes: Any
        # custom_config: Any
        # metrics: Any
        # tags: Any
        
        cfn_campaign = pinpoint.CfnCampaign(self, "MyCfnCampaign",
            application_id="applicationId",
            name="name",
            schedule=pinpoint.CfnCampaign.ScheduleProperty(
                end_time="endTime",
                event_filter=pinpoint.CfnCampaign.CampaignEventFilterProperty(
                    dimensions=pinpoint.CfnCampaign.EventDimensionsProperty(
                        attributes=attributes,
                        event_type=pinpoint.CfnCampaign.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        metrics=metrics
                    ),
                    filter_type="filterType"
                ),
                frequency="frequency",
                is_local_time=False,
                quiet_time=pinpoint.CfnCampaign.QuietTimeProperty(
                    end="end",
                    start="start"
                ),
                start_time="startTime",
                time_zone="timeZone"
            ),
            segment_id="segmentId",
        
            # the properties below are optional
            additional_treatments=[pinpoint.CfnCampaign.WriteTreatmentResourceProperty(
                custom_delivery_configuration=pinpoint.CfnCampaign.CustomDeliveryConfigurationProperty(
                    delivery_uri="deliveryUri",
                    endpoint_types=["endpointTypes"]
                ),
                message_configuration=pinpoint.CfnCampaign.MessageConfigurationProperty(
                    adm_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    apns_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    baidu_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    custom_message=pinpoint.CfnCampaign.CampaignCustomMessageProperty(
                        data="data"
                    ),
                    default_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    email_message=pinpoint.CfnCampaign.CampaignEmailMessageProperty(
                        body="body",
                        from_address="fromAddress",
                        html_body="htmlBody",
                        title="title"
                    ),
                    gcm_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    in_app_message=pinpoint.CfnCampaign.CampaignInAppMessageProperty(
                        content=[pinpoint.CfnCampaign.InAppMessageContentProperty(
                            background_color="backgroundColor",
                            body_config=pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                                alignment="alignment",
                                body="body",
                                text_color="textColor"
                            ),
                            header_config=pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                                alignment="alignment",
                                header="header",
                                text_color="textColor"
                            ),
                            image_url="imageUrl",
                            primary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                    background_color="backgroundColor",
                                    border_radius=123,
                                    button_action="buttonAction",
                                    link="link",
                                    text="text",
                                    text_color="textColor"
                                ),
                                ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                )
                            ),
                            secondary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                    background_color="backgroundColor",
                                    border_radius=123,
                                    button_action="buttonAction",
                                    link="link",
                                    text="text",
                                    text_color="textColor"
                                ),
                                ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                )
                            )
                        )],
                        custom_config=custom_config,
                        layout="layout"
                    ),
                    sms_message=pinpoint.CfnCampaign.CampaignSmsMessageProperty(
                        body="body",
                        entity_id="entityId",
                        message_type="messageType",
                        origination_number="originationNumber",
                        sender_id="senderId",
                        template_id="templateId"
                    )
                ),
                schedule=pinpoint.CfnCampaign.ScheduleProperty(
                    end_time="endTime",
                    event_filter=pinpoint.CfnCampaign.CampaignEventFilterProperty(
                        dimensions=pinpoint.CfnCampaign.EventDimensionsProperty(
                            attributes=attributes,
                            event_type=pinpoint.CfnCampaign.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            metrics=metrics
                        ),
                        filter_type="filterType"
                    ),
                    frequency="frequency",
                    is_local_time=False,
                    quiet_time=pinpoint.CfnCampaign.QuietTimeProperty(
                        end="end",
                        start="start"
                    ),
                    start_time="startTime",
                    time_zone="timeZone"
                ),
                size_percent=123,
                template_configuration=pinpoint.CfnCampaign.TemplateConfigurationProperty(
                    email_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    push_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    sms_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    voice_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    )
                ),
                treatment_description="treatmentDescription",
                treatment_name="treatmentName"
            )],
            campaign_hook=pinpoint.CfnCampaign.CampaignHookProperty(
                lambda_function_name="lambdaFunctionName",
                mode="mode",
                web_url="webUrl"
            ),
            custom_delivery_configuration=pinpoint.CfnCampaign.CustomDeliveryConfigurationProperty(
                delivery_uri="deliveryUri",
                endpoint_types=["endpointTypes"]
            ),
            description="description",
            holdout_percent=123,
            is_paused=False,
            limits=pinpoint.CfnCampaign.LimitsProperty(
                daily=123,
                maximum_duration=123,
                messages_per_second=123,
                session=123,
                total=123
            ),
            message_configuration=pinpoint.CfnCampaign.MessageConfigurationProperty(
                adm_message=pinpoint.CfnCampaign.MessageProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_small_icon_url="imageSmallIconUrl",
                    image_url="imageUrl",
                    json_body="jsonBody",
                    media_url="mediaUrl",
                    raw_content="rawContent",
                    silent_push=False,
                    time_to_live=123,
                    title="title",
                    url="url"
                ),
                apns_message=pinpoint.CfnCampaign.MessageProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_small_icon_url="imageSmallIconUrl",
                    image_url="imageUrl",
                    json_body="jsonBody",
                    media_url="mediaUrl",
                    raw_content="rawContent",
                    silent_push=False,
                    time_to_live=123,
                    title="title",
                    url="url"
                ),
                baidu_message=pinpoint.CfnCampaign.MessageProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_small_icon_url="imageSmallIconUrl",
                    image_url="imageUrl",
                    json_body="jsonBody",
                    media_url="mediaUrl",
                    raw_content="rawContent",
                    silent_push=False,
                    time_to_live=123,
                    title="title",
                    url="url"
                ),
                custom_message=pinpoint.CfnCampaign.CampaignCustomMessageProperty(
                    data="data"
                ),
                default_message=pinpoint.CfnCampaign.MessageProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_small_icon_url="imageSmallIconUrl",
                    image_url="imageUrl",
                    json_body="jsonBody",
                    media_url="mediaUrl",
                    raw_content="rawContent",
                    silent_push=False,
                    time_to_live=123,
                    title="title",
                    url="url"
                ),
                email_message=pinpoint.CfnCampaign.CampaignEmailMessageProperty(
                    body="body",
                    from_address="fromAddress",
                    html_body="htmlBody",
                    title="title"
                ),
                gcm_message=pinpoint.CfnCampaign.MessageProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_small_icon_url="imageSmallIconUrl",
                    image_url="imageUrl",
                    json_body="jsonBody",
                    media_url="mediaUrl",
                    raw_content="rawContent",
                    silent_push=False,
                    time_to_live=123,
                    title="title",
                    url="url"
                ),
                in_app_message=pinpoint.CfnCampaign.CampaignInAppMessageProperty(
                    content=[pinpoint.CfnCampaign.InAppMessageContentProperty(
                        background_color="backgroundColor",
                        body_config=pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                            alignment="alignment",
                            body="body",
                            text_color="textColor"
                        ),
                        header_config=pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                            alignment="alignment",
                            header="header",
                            text_color="textColor"
                        ),
                        image_url="imageUrl",
                        primary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                            android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            ),
                            default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                background_color="backgroundColor",
                                border_radius=123,
                                button_action="buttonAction",
                                link="link",
                                text="text",
                                text_color="textColor"
                            ),
                            ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            ),
                            web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            )
                        ),
                        secondary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                            android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            ),
                            default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                background_color="backgroundColor",
                                border_radius=123,
                                button_action="buttonAction",
                                link="link",
                                text="text",
                                text_color="textColor"
                            ),
                            ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            ),
                            web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            )
                        )
                    )],
                    custom_config=custom_config,
                    layout="layout"
                ),
                sms_message=pinpoint.CfnCampaign.CampaignSmsMessageProperty(
                    body="body",
                    entity_id="entityId",
                    message_type="messageType",
                    origination_number="originationNumber",
                    sender_id="senderId",
                    template_id="templateId"
                )
            ),
            priority=123,
            segment_version=123,
            tags=tags,
            template_configuration=pinpoint.CfnCampaign.TemplateConfigurationProperty(
                email_template=pinpoint.CfnCampaign.TemplateProperty(
                    name="name",
                    version="version"
                ),
                push_template=pinpoint.CfnCampaign.TemplateProperty(
                    name="name",
                    version="version"
                ),
                sms_template=pinpoint.CfnCampaign.TemplateProperty(
                    name="name",
                    version="version"
                ),
                voice_template=pinpoint.CfnCampaign.TemplateProperty(
                    name="name",
                    version="version"
                )
            ),
            treatment_description="treatmentDescription",
            treatment_name="treatmentName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        name: builtins.str,
        schedule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]],
        segment_id: builtins.str,
        additional_treatments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.WriteTreatmentResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        campaign_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CampaignHookProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_delivery_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CustomDeliveryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        holdout_percent: typing.Optional[jsii.Number] = None,
        is_paused: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.LimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        message_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.MessageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        segment_version: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        template_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TemplateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        treatment_description: typing.Optional[builtins.str] = None,
        treatment_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that the campaign is associated with.
        :param name: The name of the campaign.
        :param schedule: The schedule settings for the campaign.
        :param segment_id: The unique identifier for the segment to associate with the campaign.
        :param additional_treatments: An array of requests that defines additional treatments for the campaign, in addition to the default treatment for the campaign.
        :param campaign_hook: Specifies the Lambda function to use as a code hook for a campaign.
        :param custom_delivery_configuration: The delivery configuration settings for sending the treatment through a custom channel. This object is required if the ``MessageConfiguration`` object for the treatment specifies a ``CustomMessage`` object.
        :param description: A custom description of the campaign.
        :param holdout_percent: The allocated percentage of users (segment members) who shouldn't receive messages from the campaign.
        :param is_paused: Specifies whether to pause the campaign. A paused campaign doesn't run unless you resume it by changing this value to ``false`` . If you restart a campaign, the campaign restarts from the beginning and not at the point you paused it. If a campaign is running it will complete and then pause. Pause only pauses or skips the next run for a recurring future scheduled campaign. A campaign scheduled for immediate can't be paused.
        :param limits: The messaging limits for the campaign.
        :param message_configuration: The message configuration settings for the campaign.
        :param priority: An integer between 1 and 5, inclusive, that represents the priority of the in-app message campaign, where 1 is the highest priority and 5 is the lowest. If there are multiple messages scheduled to be displayed at the same time, the priority determines the order in which those messages are displayed.
        :param segment_version: The version of the segment to associate with the campaign.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_configuration: The message template to use for the treatment.
        :param treatment_description: A custom description of the default treatment for the campaign.
        :param treatment_name: A custom name of the default treatment for the campaign, if the campaign has multiple treatments. A *treatment* is a variation of a campaign that's used for A/B testing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37daefd9aecddac1551b6da8a771d74af1f7a13678f1d1fb2d351fab8d081055)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCampaignProps(
            application_id=application_id,
            name=name,
            schedule=schedule,
            segment_id=segment_id,
            additional_treatments=additional_treatments,
            campaign_hook=campaign_hook,
            custom_delivery_configuration=custom_delivery_configuration,
            description=description,
            holdout_percent=holdout_percent,
            is_paused=is_paused,
            limits=limits,
            message_configuration=message_configuration,
            priority=priority,
            segment_version=segment_version,
            tags=tags,
            template_configuration=template_configuration,
            treatment_description=treatment_description,
            treatment_name=treatment_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e15e4e500736a6e94e0b0439baae0e844c072ad04e21f846e6d90b4d664758f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__59807fa6d089ddbb2e1a05b1cd16f356100de47cbb6921352a89adfb25cf0cc2)
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
        '''The Amazon Resource Name (ARN) of the campaign.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCampaignId")
    def attr_campaign_id(self) -> builtins.str:
        '''The unique identifier for the campaign.

        :cloudformationAttribute: CampaignId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCampaignId"))

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the campaign is associated with.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__961093a0b2a649a27da7667fd113667242f9d38dc807ec0c0d27a031ef4583b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the campaign.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f60f9e8c94473fc78021759e41a1198fa36a2907ab9bbaabe3369a50277e2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.ScheduleProperty"]:
        '''The schedule settings for the campaign.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.ScheduleProperty"], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCampaign.ScheduleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2181cc1c01db963e61293d6df1af9886ac4eab655deaf6a0e57d1e205e3475d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="segmentId")
    def segment_id(self) -> builtins.str:
        '''The unique identifier for the segment to associate with the campaign.'''
        return typing.cast(builtins.str, jsii.get(self, "segmentId"))

    @segment_id.setter
    def segment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__785cdfc13b1f0cf0280965fcfdcb49bb03ad6603227a7fafd5b6f82cd1655f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segmentId", value)

    @builtins.property
    @jsii.member(jsii_name="additionalTreatments")
    def additional_treatments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.WriteTreatmentResourceProperty"]]]]:
        '''An array of requests that defines additional treatments for the campaign, in addition to the default treatment for the campaign.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.WriteTreatmentResourceProperty"]]]], jsii.get(self, "additionalTreatments"))

    @additional_treatments.setter
    def additional_treatments(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.WriteTreatmentResourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb8abceb723e5d996583338abd7b9da817cebc58734650cbcd416e12f060c3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalTreatments", value)

    @builtins.property
    @jsii.member(jsii_name="campaignHook")
    def campaign_hook(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignHookProperty"]]:
        '''Specifies the Lambda function to use as a code hook for a campaign.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignHookProperty"]], jsii.get(self, "campaignHook"))

    @campaign_hook.setter
    def campaign_hook(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignHookProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cff8453460fff6b3777f9639816cc3be2cbf9b40080e6c14e18992f375f59ae5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "campaignHook", value)

    @builtins.property
    @jsii.member(jsii_name="customDeliveryConfiguration")
    def custom_delivery_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CustomDeliveryConfigurationProperty"]]:
        '''The delivery configuration settings for sending the treatment through a custom channel.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CustomDeliveryConfigurationProperty"]], jsii.get(self, "customDeliveryConfiguration"))

    @custom_delivery_configuration.setter
    def custom_delivery_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CustomDeliveryConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21d75ff1ff920f03885a49b618f7c1b3b5e9da8ba735b125a3c88ec62fc0fe17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDeliveryConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the campaign.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3206e9b3e101dbdfbab4b167fbbe437b6df5a8667f1e3d52e265ef2504caff76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="holdoutPercent")
    def holdout_percent(self) -> typing.Optional[jsii.Number]:
        '''The allocated percentage of users (segment members) who shouldn't receive messages from the campaign.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "holdoutPercent"))

    @holdout_percent.setter
    def holdout_percent(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2a3f194f0e2f61ac095227219a69bb6002b2f11a3e883ee97a77d3aaf575c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "holdoutPercent", value)

    @builtins.property
    @jsii.member(jsii_name="isPaused")
    def is_paused(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to pause the campaign.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isPaused"))

    @is_paused.setter
    def is_paused(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__971ecc06c6c0a231935c31808c1d067094e14be95f83916e7193d19d062edff7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isPaused", value)

    @builtins.property
    @jsii.member(jsii_name="limits")
    def limits(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.LimitsProperty"]]:
        '''The messaging limits for the campaign.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.LimitsProperty"]], jsii.get(self, "limits"))

    @limits.setter
    def limits(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.LimitsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02466c3fea035dae6003b4d892edc226a948018c5026a83391d853e1adb5c661)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limits", value)

    @builtins.property
    @jsii.member(jsii_name="messageConfiguration")
    def message_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageConfigurationProperty"]]:
        '''The message configuration settings for the campaign.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageConfigurationProperty"]], jsii.get(self, "messageConfiguration"))

    @message_configuration.setter
    def message_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__782bb62da5f39fb9d597470af1efa4fcdb0ff80ce246b1a68705abda99d37c22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[jsii.Number]:
        '''An integer between 1 and 5, inclusive, that represents the priority of the in-app message campaign, where 1 is the highest priority and 5 is the lowest.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11af643454a88e879a3d44a841a7440d463052b9a9f8894837afdeb1d0f7c0a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="segmentVersion")
    def segment_version(self) -> typing.Optional[jsii.Number]:
        '''The version of the segment to associate with the campaign.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "segmentVersion"))

    @segment_version.setter
    def segment_version(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7789111cb61d2c87282d1ee29b8e1ecd9cdfe305539a62babdf135df40e102a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segmentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a55591fb10b3aa649e3cc4fff7081bd27134808f40b3426f0d1b1040c798fa32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateConfiguration")
    def template_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateConfigurationProperty"]]:
        '''The message template to use for the treatment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateConfigurationProperty"]], jsii.get(self, "templateConfiguration"))

    @template_configuration.setter
    def template_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b25bbca63e825ff6b501abde63e2de2d55b4f48c1b50cc14e8f9738d2688f0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="treatmentDescription")
    def treatment_description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the default treatment for the campaign.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "treatmentDescription"))

    @treatment_description.setter
    def treatment_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de82f559d77ceee4a216d0bcdff67a789e4cdd47818a7e2dda70c2dd6c55e63a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatmentDescription", value)

    @builtins.property
    @jsii.member(jsii_name="treatmentName")
    def treatment_name(self) -> typing.Optional[builtins.str]:
        '''A custom name of the default treatment for the campaign, if the campaign has multiple treatments.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "treatmentName"))

    @treatment_name.setter
    def treatment_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e70fc32fa7b96683078cd6d613bd62ff764758438673848d56e541e3d845a4e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatmentName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.AttributeDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_type": "attributeType", "values": "values"},
    )
    class AttributeDimensionProperty:
        def __init__(
            self,
            *,
            attribute_type: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies attribute-based criteria for including or excluding endpoints from a segment.

            :param attribute_type: The type of segment dimension to use. Valid values are:. - ``INCLUSIVE`` – endpoints that have attributes matching the values are included in the segment. - ``EXCLUSIVE`` – endpoints that have attributes matching the values are excluded from the segment. - ``CONTAINS`` – endpoints that have attributes' substrings match the values are included in the segment. - ``BEFORE`` – endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment. - ``AFTER`` – endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment. - ``BETWEEN`` – endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment. - ``ON`` – endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
            :param values: The criteria values to use for the segment dimension. Depending on the value of the ``AttributeType`` property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                attribute_dimension_property = pinpoint.CfnCampaign.AttributeDimensionProperty(
                    attribute_type="attributeType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8ed7dd96c16aafe275aca4c5eaab9d3f935bac9194d2f86699b1d5a484552dd)
                check_type(argname="argument attribute_type", value=attribute_type, expected_type=type_hints["attribute_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attribute_type is not None:
                self._values["attribute_type"] = attribute_type
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def attribute_type(self) -> typing.Optional[builtins.str]:
            '''The type of segment dimension to use. Valid values are:.

            - ``INCLUSIVE`` – endpoints that have attributes matching the values are included in the segment.
            - ``EXCLUSIVE`` – endpoints that have attributes matching the values are excluded from the segment.
            - ``CONTAINS`` – endpoints that have attributes' substrings match the values are included in the segment.
            - ``BEFORE`` – endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
            - ``AFTER`` – endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
            - ``BETWEEN`` – endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.
            - ``ON`` – endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-attributetype
            '''
            result = self._values.get("attribute_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The criteria values to use for the segment dimension.

            Depending on the value of the ``AttributeType`` property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.CampaignCustomMessageProperty",
        jsii_struct_bases=[],
        name_mapping={"data": "data"},
    )
    class CampaignCustomMessageProperty:
        def __init__(self, *, data: typing.Optional[builtins.str] = None) -> None:
            '''Specifies the contents of a message that's sent through a custom channel to recipients of a campaign.

            :param data: The raw, JSON-formatted string to use as the payload for the message. The maximum size is 5 KB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigncustommessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                campaign_custom_message_property = pinpoint.CfnCampaign.CampaignCustomMessageProperty(
                    data="data"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96d7068cf46b5dea22187b378d27f37888567bca535d3c161fdf5816f4109e7b)
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''The raw, JSON-formatted string to use as the payload for the message.

            The maximum size is 5 KB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigncustommessage.html#cfn-pinpoint-campaign-campaigncustommessage-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignCustomMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.CampaignEmailMessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "body": "body",
            "from_address": "fromAddress",
            "html_body": "htmlBody",
            "title": "title",
        },
    )
    class CampaignEmailMessageProperty:
        def __init__(
            self,
            *,
            body: typing.Optional[builtins.str] = None,
            from_address: typing.Optional[builtins.str] = None,
            html_body: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the content and "From" address for an email message that's sent to recipients of a campaign.

            :param body: The body of the email for recipients whose email clients don't render HTML content.
            :param from_address: The verified email address to send the email from. The default address is the ``FromAddress`` specified for the email channel for the application.
            :param html_body: The body of the email, in HTML format, for recipients whose email clients render HTML content.
            :param title: The subject line, or title, of the email.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                campaign_email_message_property = pinpoint.CfnCampaign.CampaignEmailMessageProperty(
                    body="body",
                    from_address="fromAddress",
                    html_body="htmlBody",
                    title="title"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fcad47e2a39463d474a4de463cff3ea866a329d0049874cb14dec65a5192428a)
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument from_address", value=from_address, expected_type=type_hints["from_address"])
                check_type(argname="argument html_body", value=html_body, expected_type=type_hints["html_body"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if body is not None:
                self._values["body"] = body
            if from_address is not None:
                self._values["from_address"] = from_address
            if html_body is not None:
                self._values["html_body"] = html_body
            if title is not None:
                self._values["title"] = title

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The body of the email for recipients whose email clients don't render HTML content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def from_address(self) -> typing.Optional[builtins.str]:
            '''The verified email address to send the email from.

            The default address is the ``FromAddress`` specified for the email channel for the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-fromaddress
            '''
            result = self._values.get("from_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def html_body(self) -> typing.Optional[builtins.str]:
            '''The body of the email, in HTML format, for recipients whose email clients render HTML content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-htmlbody
            '''
            result = self._values.get("html_body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''The subject line, or title, of the email.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignEmailMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.CampaignEventFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"dimensions": "dimensions", "filter_type": "filterType"},
    )
    class CampaignEventFilterProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.EventDimensionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            filter_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the settings for events that cause a campaign to be sent.

            :param dimensions: The dimension settings of the event filter for the campaign.
            :param filter_type: The type of event that causes the campaign to be sent. Valid values are: ``SYSTEM`` , sends the campaign when a system event occurs; and, ``ENDPOINT`` , sends the campaign when an endpoint event (Events resource) occurs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # attributes: Any
                # metrics: Any
                
                campaign_event_filter_property = pinpoint.CfnCampaign.CampaignEventFilterProperty(
                    dimensions=pinpoint.CfnCampaign.EventDimensionsProperty(
                        attributes=attributes,
                        event_type=pinpoint.CfnCampaign.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        metrics=metrics
                    ),
                    filter_type="filterType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5711bd48d2337448a48cdb597629c06c82e881cc34b812165389291f4792ec81)
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument filter_type", value=filter_type, expected_type=type_hints["filter_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if filter_type is not None:
                self._values["filter_type"] = filter_type

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.EventDimensionsProperty"]]:
            '''The dimension settings of the event filter for the campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.EventDimensionsProperty"]], result)

        @builtins.property
        def filter_type(self) -> typing.Optional[builtins.str]:
            '''The type of event that causes the campaign to be sent.

            Valid values are: ``SYSTEM`` , sends the campaign when a system event occurs; and, ``ENDPOINT`` , sends the campaign when an endpoint event (Events resource) occurs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-filtertype
            '''
            result = self._values.get("filter_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignEventFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.CampaignHookProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_function_name": "lambdaFunctionName",
            "mode": "mode",
            "web_url": "webUrl",
        },
    )
    class CampaignHookProperty:
        def __init__(
            self,
            *,
            lambda_function_name: typing.Optional[builtins.str] = None,
            mode: typing.Optional[builtins.str] = None,
            web_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies settings for invoking an Lambda function that customizes a segment for a campaign.

            :param lambda_function_name: The name or Amazon Resource Name (ARN) of the Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign.
            :param mode: The mode that Amazon Pinpoint uses to invoke the Lambda function. Possible values are:. - ``FILTER`` - Invoke the function to customize the segment that's used by a campaign. - ``DELIVERY`` - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the ``CustomDeliveryConfiguration`` and ``CampaignCustomMessage`` objects of the campaign.
            :param web_url: The web URL that Amazon Pinpoint calls to invoke the Lambda function over HTTPS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                campaign_hook_property = pinpoint.CfnCampaign.CampaignHookProperty(
                    lambda_function_name="lambdaFunctionName",
                    mode="mode",
                    web_url="webUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__97f75cb7e807dfe79a19b85bf104c570738dd0d9e5565d57425d54082fae4765)
                check_type(argname="argument lambda_function_name", value=lambda_function_name, expected_type=type_hints["lambda_function_name"])
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument web_url", value=web_url, expected_type=type_hints["web_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_function_name is not None:
                self._values["lambda_function_name"] = lambda_function_name
            if mode is not None:
                self._values["mode"] = mode
            if web_url is not None:
                self._values["web_url"] = web_url

        @builtins.property
        def lambda_function_name(self) -> typing.Optional[builtins.str]:
            '''The name or Amazon Resource Name (ARN) of the Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-lambdafunctionname
            '''
            result = self._values.get("lambda_function_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''The mode that Amazon Pinpoint uses to invoke the Lambda function. Possible values are:.

            - ``FILTER`` - Invoke the function to customize the segment that's used by a campaign.
            - ``DELIVERY`` - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the ``CustomDeliveryConfiguration`` and ``CampaignCustomMessage`` objects of the campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def web_url(self) -> typing.Optional[builtins.str]:
            '''The web URL that Amazon Pinpoint calls to invoke the Lambda function over HTTPS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-weburl
            '''
            result = self._values.get("web_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.CampaignInAppMessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content": "content",
            "custom_config": "customConfig",
            "layout": "layout",
        },
    )
    class CampaignInAppMessageProperty:
        def __init__(
            self,
            *,
            content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.InAppMessageContentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            custom_config: typing.Any = None,
            layout: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the appearance of an in-app message, including the message type, the title and body text, text and background colors, and the configurations of buttons that appear in the message.

            :param content: An array that contains configurtion information about the in-app message for the campaign, including title and body text, text colors, background colors, image URLs, and button configurations.
            :param custom_config: Custom data, in the form of key-value pairs, that is included in an in-app messaging payload.
            :param layout: A string that describes how the in-app message will appear. You can specify one of the following:. - ``BOTTOM_BANNER`` – a message that appears as a banner at the bottom of the page. - ``TOP_BANNER`` – a message that appears as a banner at the top of the page. - ``OVERLAYS`` – a message that covers entire screen. - ``MOBILE_FEED`` – a message that appears in a window in front of the page. - ``MIDDLE_BANNER`` – a message that appears as a banner in the middle of the page. - ``CAROUSEL`` – a scrollable layout of up to five unique messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # custom_config: Any
                
                campaign_in_app_message_property = pinpoint.CfnCampaign.CampaignInAppMessageProperty(
                    content=[pinpoint.CfnCampaign.InAppMessageContentProperty(
                        background_color="backgroundColor",
                        body_config=pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                            alignment="alignment",
                            body="body",
                            text_color="textColor"
                        ),
                        header_config=pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                            alignment="alignment",
                            header="header",
                            text_color="textColor"
                        ),
                        image_url="imageUrl",
                        primary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                            android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            ),
                            default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                background_color="backgroundColor",
                                border_radius=123,
                                button_action="buttonAction",
                                link="link",
                                text="text",
                                text_color="textColor"
                            ),
                            ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            ),
                            web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            )
                        ),
                        secondary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                            android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            ),
                            default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                background_color="backgroundColor",
                                border_radius=123,
                                button_action="buttonAction",
                                link="link",
                                text="text",
                                text_color="textColor"
                            ),
                            ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            ),
                            web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                button_action="buttonAction",
                                link="link"
                            )
                        )
                    )],
                    custom_config=custom_config,
                    layout="layout"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__369c68d5a011c28939ef45c9d0181abf68afee30d2c4a541e27cc384bdbaaac0)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument custom_config", value=custom_config, expected_type=type_hints["custom_config"])
                check_type(argname="argument layout", value=layout, expected_type=type_hints["layout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content
            if custom_config is not None:
                self._values["custom_config"] = custom_config
            if layout is not None:
                self._values["layout"] = layout

        @builtins.property
        def content(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageContentProperty"]]]]:
            '''An array that contains configurtion information about the in-app message for the campaign, including title and body text, text colors, background colors, image URLs, and button configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageContentProperty"]]]], result)

        @builtins.property
        def custom_config(self) -> typing.Any:
            '''Custom data, in the form of key-value pairs, that is included in an in-app messaging payload.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-customconfig
            '''
            result = self._values.get("custom_config")
            return typing.cast(typing.Any, result)

        @builtins.property
        def layout(self) -> typing.Optional[builtins.str]:
            '''A string that describes how the in-app message will appear. You can specify one of the following:.

            - ``BOTTOM_BANNER`` – a message that appears as a banner at the bottom of the page.
            - ``TOP_BANNER`` – a message that appears as a banner at the top of the page.
            - ``OVERLAYS`` – a message that covers entire screen.
            - ``MOBILE_FEED`` – a message that appears in a window in front of the page.
            - ``MIDDLE_BANNER`` – a message that appears as a banner in the middle of the page.
            - ``CAROUSEL`` – a scrollable layout of up to five unique messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-layout
            '''
            result = self._values.get("layout")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignInAppMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.CampaignSmsMessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "body": "body",
            "entity_id": "entityId",
            "message_type": "messageType",
            "origination_number": "originationNumber",
            "sender_id": "senderId",
            "template_id": "templateId",
        },
    )
    class CampaignSmsMessageProperty:
        def __init__(
            self,
            *,
            body: typing.Optional[builtins.str] = None,
            entity_id: typing.Optional[builtins.str] = None,
            message_type: typing.Optional[builtins.str] = None,
            origination_number: typing.Optional[builtins.str] = None,
            sender_id: typing.Optional[builtins.str] = None,
            template_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the content and settings for an SMS message that's sent to recipients of a campaign.

            :param body: The body of the SMS message.
            :param entity_id: The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.
            :param message_type: The SMS message type. Valid values are ``TRANSACTIONAL`` (for messages that are critical or time-sensitive, such as a one-time passwords) and ``PROMOTIONAL`` (for messsages that aren't critical or time-sensitive, such as marketing messages).
            :param origination_number: The long code to send the SMS message from. This value should be one of the dedicated long codes that's assigned to your AWS account. Although it isn't required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.
            :param sender_id: The alphabetic Sender ID to display as the sender of the message on a recipient's device. Support for sender IDs varies by country or region. To specify a phone number as the sender, omit this parameter and use ``OriginationNumber`` instead. For more information about support for Sender ID by country, see the `Amazon Pinpoint User Guide <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html>`_ .
            :param template_id: The template ID received from the regulatory body for sending SMS in your country.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                campaign_sms_message_property = pinpoint.CfnCampaign.CampaignSmsMessageProperty(
                    body="body",
                    entity_id="entityId",
                    message_type="messageType",
                    origination_number="originationNumber",
                    sender_id="senderId",
                    template_id="templateId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4dd8e843454abe931dda3035fe9577af97315cb66140b3b775493c16267a7b5c)
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument entity_id", value=entity_id, expected_type=type_hints["entity_id"])
                check_type(argname="argument message_type", value=message_type, expected_type=type_hints["message_type"])
                check_type(argname="argument origination_number", value=origination_number, expected_type=type_hints["origination_number"])
                check_type(argname="argument sender_id", value=sender_id, expected_type=type_hints["sender_id"])
                check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if body is not None:
                self._values["body"] = body
            if entity_id is not None:
                self._values["entity_id"] = entity_id
            if message_type is not None:
                self._values["message_type"] = message_type
            if origination_number is not None:
                self._values["origination_number"] = origination_number
            if sender_id is not None:
                self._values["sender_id"] = sender_id
            if template_id is not None:
                self._values["template_id"] = template_id

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The body of the SMS message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entity_id(self) -> typing.Optional[builtins.str]:
            '''The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-entityid
            '''
            result = self._values.get("entity_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message_type(self) -> typing.Optional[builtins.str]:
            '''The SMS message type.

            Valid values are ``TRANSACTIONAL`` (for messages that are critical or time-sensitive, such as a one-time passwords) and ``PROMOTIONAL`` (for messsages that aren't critical or time-sensitive, such as marketing messages).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-messagetype
            '''
            result = self._values.get("message_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def origination_number(self) -> typing.Optional[builtins.str]:
            '''The long code to send the SMS message from.

            This value should be one of the dedicated long codes that's assigned to your AWS account. Although it isn't required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-originationnumber
            '''
            result = self._values.get("origination_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sender_id(self) -> typing.Optional[builtins.str]:
            '''The alphabetic Sender ID to display as the sender of the message on a recipient's device.

            Support for sender IDs varies by country or region. To specify a phone number as the sender, omit this parameter and use ``OriginationNumber`` instead. For more information about support for Sender ID by country, see the `Amazon Pinpoint User Guide <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-senderid
            '''
            result = self._values.get("sender_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_id(self) -> typing.Optional[builtins.str]:
            '''The template ID received from the regulatory body for sending SMS in your country.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-templateid
            '''
            result = self._values.get("template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignSmsMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.CustomDeliveryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_uri": "deliveryUri",
            "endpoint_types": "endpointTypes",
        },
    )
    class CustomDeliveryConfigurationProperty:
        def __init__(
            self,
            *,
            delivery_uri: typing.Optional[builtins.str] = None,
            endpoint_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the delivery configuration settings for sending a campaign or campaign treatment through a custom channel.

            This object is required if you use the ``CampaignCustomMessage`` object to define the message to send for the campaign or campaign treatment.

            :param delivery_uri: The destination to send the campaign or treatment to. This value can be one of the following:. - The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment. - The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.
            :param endpoint_types: The types of endpoints to send the campaign or treatment to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ``ChannelType`` property of an endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-customdeliveryconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                custom_delivery_configuration_property = pinpoint.CfnCampaign.CustomDeliveryConfigurationProperty(
                    delivery_uri="deliveryUri",
                    endpoint_types=["endpointTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5f9eeac0ef1da7f791086412cb13c53a0147c6a9c383482edc81fc463b9850d)
                check_type(argname="argument delivery_uri", value=delivery_uri, expected_type=type_hints["delivery_uri"])
                check_type(argname="argument endpoint_types", value=endpoint_types, expected_type=type_hints["endpoint_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delivery_uri is not None:
                self._values["delivery_uri"] = delivery_uri
            if endpoint_types is not None:
                self._values["endpoint_types"] = endpoint_types

        @builtins.property
        def delivery_uri(self) -> typing.Optional[builtins.str]:
            '''The destination to send the campaign or treatment to. This value can be one of the following:.

            - The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.
            - The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-customdeliveryconfiguration.html#cfn-pinpoint-campaign-customdeliveryconfiguration-deliveryuri
            '''
            result = self._values.get("delivery_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def endpoint_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The types of endpoints to send the campaign or treatment to.

            Each valid value maps to a type of channel that you can associate with an endpoint by using the ``ChannelType`` property of an endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-customdeliveryconfiguration.html#cfn-pinpoint-campaign-customdeliveryconfiguration-endpointtypes
            '''
            result = self._values.get("endpoint_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomDeliveryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.DefaultButtonConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "background_color": "backgroundColor",
            "border_radius": "borderRadius",
            "button_action": "buttonAction",
            "link": "link",
            "text": "text",
            "text_color": "textColor",
        },
    )
    class DefaultButtonConfigurationProperty:
        def __init__(
            self,
            *,
            background_color: typing.Optional[builtins.str] = None,
            border_radius: typing.Optional[jsii.Number] = None,
            button_action: typing.Optional[builtins.str] = None,
            link: typing.Optional[builtins.str] = None,
            text: typing.Optional[builtins.str] = None,
            text_color: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the default behavior for a button that appears in an in-app message.

            You can optionally add button configurations that specifically apply to iOS, Android, or web browser users.

            :param background_color: The background color of a button, expressed as a hex color code (such as #000000 for black).
            :param border_radius: The border radius of a button.
            :param button_action: The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following: - ``LINK`` – A link to a web destination. - ``DEEP_LINK`` – A link to a specific page in an application. - ``CLOSE`` – Dismisses the message.
            :param link: The destination (such as a URL) for a button.
            :param text: The text that appears on a button in an in-app message.
            :param text_color: The color of the body text in a button, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                default_button_configuration_property = pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                    background_color="backgroundColor",
                    border_radius=123,
                    button_action="buttonAction",
                    link="link",
                    text="text",
                    text_color="textColor"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f33b27b37a2b40ecdc2e462af2efd8e422d0ae8e5d18e6600390ef57c62446c)
                check_type(argname="argument background_color", value=background_color, expected_type=type_hints["background_color"])
                check_type(argname="argument border_radius", value=border_radius, expected_type=type_hints["border_radius"])
                check_type(argname="argument button_action", value=button_action, expected_type=type_hints["button_action"])
                check_type(argname="argument link", value=link, expected_type=type_hints["link"])
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
                check_type(argname="argument text_color", value=text_color, expected_type=type_hints["text_color"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if background_color is not None:
                self._values["background_color"] = background_color
            if border_radius is not None:
                self._values["border_radius"] = border_radius
            if button_action is not None:
                self._values["button_action"] = button_action
            if link is not None:
                self._values["link"] = link
            if text is not None:
                self._values["text"] = text
            if text_color is not None:
                self._values["text_color"] = text_color

        @builtins.property
        def background_color(self) -> typing.Optional[builtins.str]:
            '''The background color of a button, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-backgroundcolor
            '''
            result = self._values.get("background_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def border_radius(self) -> typing.Optional[jsii.Number]:
            '''The border radius of a button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-borderradius
            '''
            result = self._values.get("border_radius")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def button_action(self) -> typing.Optional[builtins.str]:
            '''The action that occurs when a recipient chooses a button in an in-app message.

            You can specify one of the following:

            - ``LINK`` – A link to a web destination.
            - ``DEEP_LINK`` – A link to a specific page in an application.
            - ``CLOSE`` – Dismisses the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-buttonaction
            '''
            result = self._values.get("button_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def link(self) -> typing.Optional[builtins.str]:
            '''The destination (such as a URL) for a button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-link
            '''
            result = self._values.get("link")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text(self) -> typing.Optional[builtins.str]:
            '''The text that appears on a button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-text
            '''
            result = self._values.get("text")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_color(self) -> typing.Optional[builtins.str]:
            '''The color of the body text in a button, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-textcolor
            '''
            result = self._values.get("text_color")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultButtonConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.EventDimensionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attributes": "attributes",
            "event_type": "eventType",
            "metrics": "metrics",
        },
    )
    class EventDimensionsProperty:
        def __init__(
            self,
            *,
            attributes: typing.Any = None,
            event_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.SetDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            metrics: typing.Any = None,
        ) -> None:
            '''Specifies the dimensions for an event filter that determines when a campaign is sent or a journey activity is performed.

            :param attributes: One or more custom attributes that your application reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            :param event_type: The name of the event that causes the campaign to be sent or the journey activity to be performed. This can be a standard event that Amazon Pinpoint generates, such as ``_email.delivered`` or ``_custom.delivered`` . For campaigns, this can also be a custom event that's specific to your application. For information about standard events, see `Streaming Amazon Pinpoint Events <https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html>`_ in the *Amazon Pinpoint Developer Guide* .
            :param metrics: One or more custom metrics that your application reports to Amazon Pinpoint . You can use these metrics as selection criteria when you create an event filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # attributes: Any
                # metrics: Any
                
                event_dimensions_property = pinpoint.CfnCampaign.EventDimensionsProperty(
                    attributes=attributes,
                    event_type=pinpoint.CfnCampaign.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    metrics=metrics
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b9fa660e0e2abbffc8641498aef64f5a8b1fa0b16a3ee77e0d23eb78fb8ecec)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
                check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if event_type is not None:
                self._values["event_type"] = event_type
            if metrics is not None:
                self._values["metrics"] = metrics

        @builtins.property
        def attributes(self) -> typing.Any:
            '''One or more custom attributes that your application reports to Amazon Pinpoint.

            You can use these attributes as selection criteria when you create an event filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Any, result)

        @builtins.property
        def event_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SetDimensionProperty"]]:
            '''The name of the event that causes the campaign to be sent or the journey activity to be performed.

            This can be a standard event that Amazon Pinpoint generates, such as ``_email.delivered`` or ``_custom.delivered`` . For campaigns, this can also be a custom event that's specific to your application. For information about standard events, see `Streaming Amazon Pinpoint Events <https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html>`_ in the *Amazon Pinpoint Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-eventtype
            '''
            result = self._values.get("event_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SetDimensionProperty"]], result)

        @builtins.property
        def metrics(self) -> typing.Any:
            '''One or more custom metrics that your application reports to Amazon Pinpoint .

            You can use these metrics as selection criteria when you create an event filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-metrics
            '''
            result = self._values.get("metrics")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDimensionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.InAppMessageBodyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alignment": "alignment",
            "body": "body",
            "text_color": "textColor",
        },
    )
    class InAppMessageBodyConfigProperty:
        def __init__(
            self,
            *,
            alignment: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            text_color: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration of main body text of the in-app message.

            :param alignment: The text alignment of the main body text of the message. Acceptable values: ``LEFT`` , ``CENTER`` , ``RIGHT`` .
            :param body: The main body text of the message.
            :param text_color: The color of the body text, expressed as a string consisting of a hex color code (such as "#000000" for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                in_app_message_body_config_property = pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                    alignment="alignment",
                    body="body",
                    text_color="textColor"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__21ae3f4ad63a8f7249b2c0e72d6d5745cf2f08ebe23067ab107734aa59137ff6)
                check_type(argname="argument alignment", value=alignment, expected_type=type_hints["alignment"])
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument text_color", value=text_color, expected_type=type_hints["text_color"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alignment is not None:
                self._values["alignment"] = alignment
            if body is not None:
                self._values["body"] = body
            if text_color is not None:
                self._values["text_color"] = text_color

        @builtins.property
        def alignment(self) -> typing.Optional[builtins.str]:
            '''The text alignment of the main body text of the message.

            Acceptable values: ``LEFT`` , ``CENTER`` , ``RIGHT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-alignment
            '''
            result = self._values.get("alignment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The main body text of the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_color(self) -> typing.Optional[builtins.str]:
            '''The color of the body text, expressed as a string consisting of a hex color code (such as "#000000" for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-textcolor
            '''
            result = self._values.get("text_color")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InAppMessageBodyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.InAppMessageButtonProperty",
        jsii_struct_bases=[],
        name_mapping={
            "android": "android",
            "default_config": "defaultConfig",
            "ios": "ios",
            "web": "web",
        },
    )
    class InAppMessageButtonProperty:
        def __init__(
            self,
            *,
            android: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.OverrideButtonConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.DefaultButtonConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ios: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.OverrideButtonConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            web: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.OverrideButtonConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration of a button that appears in an in-app message.

            :param android: An object that defines the default behavior for a button in in-app messages sent to Android.
            :param default_config: An object that defines the default behavior for a button in an in-app message.
            :param ios: An object that defines the default behavior for a button in in-app messages sent to iOS devices.
            :param web: An object that defines the default behavior for a button in in-app messages for web applications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                in_app_message_button_property = pinpoint.CfnCampaign.InAppMessageButtonProperty(
                    android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    ),
                    default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                        background_color="backgroundColor",
                        border_radius=123,
                        button_action="buttonAction",
                        link="link",
                        text="text",
                        text_color="textColor"
                    ),
                    ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    ),
                    web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__78fc873c9d930c4eed8ba526034beaf3e18989761683e374e83ccb29d875b8c2)
                check_type(argname="argument android", value=android, expected_type=type_hints["android"])
                check_type(argname="argument default_config", value=default_config, expected_type=type_hints["default_config"])
                check_type(argname="argument ios", value=ios, expected_type=type_hints["ios"])
                check_type(argname="argument web", value=web, expected_type=type_hints["web"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if android is not None:
                self._values["android"] = android
            if default_config is not None:
                self._values["default_config"] = default_config
            if ios is not None:
                self._values["ios"] = ios
            if web is not None:
                self._values["web"] = web

        @builtins.property
        def android(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.OverrideButtonConfigurationProperty"]]:
            '''An object that defines the default behavior for a button in in-app messages sent to Android.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-android
            '''
            result = self._values.get("android")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.OverrideButtonConfigurationProperty"]], result)

        @builtins.property
        def default_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.DefaultButtonConfigurationProperty"]]:
            '''An object that defines the default behavior for a button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-defaultconfig
            '''
            result = self._values.get("default_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.DefaultButtonConfigurationProperty"]], result)

        @builtins.property
        def ios(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.OverrideButtonConfigurationProperty"]]:
            '''An object that defines the default behavior for a button in in-app messages sent to iOS devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-ios
            '''
            result = self._values.get("ios")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.OverrideButtonConfigurationProperty"]], result)

        @builtins.property
        def web(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.OverrideButtonConfigurationProperty"]]:
            '''An object that defines the default behavior for a button in in-app messages for web applications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-web
            '''
            result = self._values.get("web")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.OverrideButtonConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InAppMessageButtonProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.InAppMessageContentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "background_color": "backgroundColor",
            "body_config": "bodyConfig",
            "header_config": "headerConfig",
            "image_url": "imageUrl",
            "primary_btn": "primaryBtn",
            "secondary_btn": "secondaryBtn",
        },
    )
    class InAppMessageContentProperty:
        def __init__(
            self,
            *,
            background_color: typing.Optional[builtins.str] = None,
            body_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.InAppMessageBodyConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            header_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.InAppMessageHeaderConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_url: typing.Optional[builtins.str] = None,
            primary_btn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.InAppMessageButtonProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            secondary_btn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.InAppMessageButtonProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration and contents of an in-app message.

            :param background_color: The background color for an in-app message banner, expressed as a hex color code (such as #000000 for black).
            :param body_config: Specifies the configuration of main body text in an in-app message template.
            :param header_config: Specifies the configuration and content of the header or title text of the in-app message.
            :param image_url: The URL of the image that appears on an in-app message banner.
            :param primary_btn: An object that contains configuration information about the primary button in an in-app message.
            :param secondary_btn: An object that contains configuration information about the secondary button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                in_app_message_content_property = pinpoint.CfnCampaign.InAppMessageContentProperty(
                    background_color="backgroundColor",
                    body_config=pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                        alignment="alignment",
                        body="body",
                        text_color="textColor"
                    ),
                    header_config=pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                        alignment="alignment",
                        header="header",
                        text_color="textColor"
                    ),
                    image_url="imageUrl",
                    primary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                        android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                            background_color="backgroundColor",
                            border_radius=123,
                            button_action="buttonAction",
                            link="link",
                            text="text",
                            text_color="textColor"
                        ),
                        ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        )
                    ),
                    secondary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                        android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                            background_color="backgroundColor",
                            border_radius=123,
                            button_action="buttonAction",
                            link="link",
                            text="text",
                            text_color="textColor"
                        ),
                        ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__92cd497e859572c8cc118d0c5229a7d36478b7b8c2b34925e5f2f4e7072545de)
                check_type(argname="argument background_color", value=background_color, expected_type=type_hints["background_color"])
                check_type(argname="argument body_config", value=body_config, expected_type=type_hints["body_config"])
                check_type(argname="argument header_config", value=header_config, expected_type=type_hints["header_config"])
                check_type(argname="argument image_url", value=image_url, expected_type=type_hints["image_url"])
                check_type(argname="argument primary_btn", value=primary_btn, expected_type=type_hints["primary_btn"])
                check_type(argname="argument secondary_btn", value=secondary_btn, expected_type=type_hints["secondary_btn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if background_color is not None:
                self._values["background_color"] = background_color
            if body_config is not None:
                self._values["body_config"] = body_config
            if header_config is not None:
                self._values["header_config"] = header_config
            if image_url is not None:
                self._values["image_url"] = image_url
            if primary_btn is not None:
                self._values["primary_btn"] = primary_btn
            if secondary_btn is not None:
                self._values["secondary_btn"] = secondary_btn

        @builtins.property
        def background_color(self) -> typing.Optional[builtins.str]:
            '''The background color for an in-app message banner, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-backgroundcolor
            '''
            result = self._values.get("background_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageBodyConfigProperty"]]:
            '''Specifies the configuration of main body text in an in-app message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-bodyconfig
            '''
            result = self._values.get("body_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageBodyConfigProperty"]], result)

        @builtins.property
        def header_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageHeaderConfigProperty"]]:
            '''Specifies the configuration and content of the header or title text of the in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-headerconfig
            '''
            result = self._values.get("header_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageHeaderConfigProperty"]], result)

        @builtins.property
        def image_url(self) -> typing.Optional[builtins.str]:
            '''The URL of the image that appears on an in-app message banner.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-imageurl
            '''
            result = self._values.get("image_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary_btn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageButtonProperty"]]:
            '''An object that contains configuration information about the primary button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-primarybtn
            '''
            result = self._values.get("primary_btn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageButtonProperty"]], result)

        @builtins.property
        def secondary_btn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageButtonProperty"]]:
            '''An object that contains configuration information about the secondary button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-secondarybtn
            '''
            result = self._values.get("secondary_btn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.InAppMessageButtonProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InAppMessageContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alignment": "alignment",
            "header": "header",
            "text_color": "textColor",
        },
    )
    class InAppMessageHeaderConfigProperty:
        def __init__(
            self,
            *,
            alignment: typing.Optional[builtins.str] = None,
            header: typing.Optional[builtins.str] = None,
            text_color: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration and content of the header or title text of the in-app message.

            :param alignment: The text alignment of the title of the message. Acceptable values: ``LEFT`` , ``CENTER`` , ``RIGHT`` .
            :param header: The header or title text of the in-app message.
            :param text_color: The color of the body text, expressed as a string consisting of a hex color code (such as "#000000" for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                in_app_message_header_config_property = pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                    alignment="alignment",
                    header="header",
                    text_color="textColor"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e4df544f968e3811d35ae203f458bcfbed6d3f0f45e80591bb8247658d1ea0a)
                check_type(argname="argument alignment", value=alignment, expected_type=type_hints["alignment"])
                check_type(argname="argument header", value=header, expected_type=type_hints["header"])
                check_type(argname="argument text_color", value=text_color, expected_type=type_hints["text_color"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alignment is not None:
                self._values["alignment"] = alignment
            if header is not None:
                self._values["header"] = header
            if text_color is not None:
                self._values["text_color"] = text_color

        @builtins.property
        def alignment(self) -> typing.Optional[builtins.str]:
            '''The text alignment of the title of the message.

            Acceptable values: ``LEFT`` , ``CENTER`` , ``RIGHT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-alignment
            '''
            result = self._values.get("alignment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def header(self) -> typing.Optional[builtins.str]:
            '''The header or title text of the in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-header
            '''
            result = self._values.get("header")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_color(self) -> typing.Optional[builtins.str]:
            '''The color of the body text, expressed as a string consisting of a hex color code (such as "#000000" for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-textcolor
            '''
            result = self._values.get("text_color")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InAppMessageHeaderConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.LimitsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "daily": "daily",
            "maximum_duration": "maximumDuration",
            "messages_per_second": "messagesPerSecond",
            "session": "session",
            "total": "total",
        },
    )
    class LimitsProperty:
        def __init__(
            self,
            *,
            daily: typing.Optional[jsii.Number] = None,
            maximum_duration: typing.Optional[jsii.Number] = None,
            messages_per_second: typing.Optional[jsii.Number] = None,
            session: typing.Optional[jsii.Number] = None,
            total: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the limits on the messages that a campaign can send.

            :param daily: The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. The maximum value is 100.
            :param maximum_duration: The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds.
            :param messages_per_second: The maximum number of messages that a campaign can send each second. The minimum value is 1. The maximum value is 20,000.
            :param session: The maximum number of messages that the campaign can send per user session.
            :param total: The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. The maximum value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                limits_property = pinpoint.CfnCampaign.LimitsProperty(
                    daily=123,
                    maximum_duration=123,
                    messages_per_second=123,
                    session=123,
                    total=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65312f3cd527ec459025805d805815ae9b2c77518abcf438fb299c6957605e74)
                check_type(argname="argument daily", value=daily, expected_type=type_hints["daily"])
                check_type(argname="argument maximum_duration", value=maximum_duration, expected_type=type_hints["maximum_duration"])
                check_type(argname="argument messages_per_second", value=messages_per_second, expected_type=type_hints["messages_per_second"])
                check_type(argname="argument session", value=session, expected_type=type_hints["session"])
                check_type(argname="argument total", value=total, expected_type=type_hints["total"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if daily is not None:
                self._values["daily"] = daily
            if maximum_duration is not None:
                self._values["maximum_duration"] = maximum_duration
            if messages_per_second is not None:
                self._values["messages_per_second"] = messages_per_second
            if session is not None:
                self._values["session"] = session
            if total is not None:
                self._values["total"] = total

        @builtins.property
        def daily(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period.

            The maximum value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-daily
            '''
            result = self._values.get("daily")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_duration(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign.

            The minimum value is 60 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-maximumduration
            '''
            result = self._values.get("maximum_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def messages_per_second(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of messages that a campaign can send each second.

            The minimum value is 1. The maximum value is 20,000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-messagespersecond
            '''
            result = self._values.get("messages_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def session(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of messages that the campaign can send per user session.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-session
            '''
            result = self._values.get("session")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign.

            The maximum value is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-total
            '''
            result = self._values.get("total")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.MessageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adm_message": "admMessage",
            "apns_message": "apnsMessage",
            "baidu_message": "baiduMessage",
            "custom_message": "customMessage",
            "default_message": "defaultMessage",
            "email_message": "emailMessage",
            "gcm_message": "gcmMessage",
            "in_app_message": "inAppMessage",
            "sms_message": "smsMessage",
        },
    )
    class MessageConfigurationProperty:
        def __init__(
            self,
            *,
            adm_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.MessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            apns_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.MessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            baidu_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.MessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CampaignCustomMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            default_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.MessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            email_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CampaignEmailMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            gcm_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.MessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            in_app_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CampaignInAppMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sms_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CampaignSmsMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the message configuration settings for a campaign.

            :param adm_message: The message that the campaign sends through the ADM (Amazon Device Messaging) channel. If specified, this message overrides the default message.
            :param apns_message: The message that the campaign sends through the APNs (Apple Push Notification service) channel. If specified, this message overrides the default message.
            :param baidu_message: The message that the campaign sends through the Baidu (Baidu Cloud Push) channel. If specified, this message overrides the default message.
            :param custom_message: The message that the campaign sends through a custom channel, as specified by the delivery configuration ( ``CustomDeliveryConfiguration`` ) settings for the campaign. If specified, this message overrides the default message.
            :param default_message: The default message that the campaign sends through all the channels that are configured for the campaign.
            :param email_message: The message that the campaign sends through the email channel. If specified, this message overrides the default message.
            :param gcm_message: The message that the campaign sends through the GCM channel, which enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. If specified, this message overrides the default message.
            :param in_app_message: The default message for the in-app messaging channel. This message overrides the default message ( ``DefaultMessage`` ).
            :param sms_message: The message that the campaign sends through the SMS channel. If specified, this message overrides the default message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # custom_config: Any
                
                message_configuration_property = pinpoint.CfnCampaign.MessageConfigurationProperty(
                    adm_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    apns_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    baidu_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    custom_message=pinpoint.CfnCampaign.CampaignCustomMessageProperty(
                        data="data"
                    ),
                    default_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    email_message=pinpoint.CfnCampaign.CampaignEmailMessageProperty(
                        body="body",
                        from_address="fromAddress",
                        html_body="htmlBody",
                        title="title"
                    ),
                    gcm_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    in_app_message=pinpoint.CfnCampaign.CampaignInAppMessageProperty(
                        content=[pinpoint.CfnCampaign.InAppMessageContentProperty(
                            background_color="backgroundColor",
                            body_config=pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                                alignment="alignment",
                                body="body",
                                text_color="textColor"
                            ),
                            header_config=pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                                alignment="alignment",
                                header="header",
                                text_color="textColor"
                            ),
                            image_url="imageUrl",
                            primary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                    background_color="backgroundColor",
                                    border_radius=123,
                                    button_action="buttonAction",
                                    link="link",
                                    text="text",
                                    text_color="textColor"
                                ),
                                ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                )
                            ),
                            secondary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                    background_color="backgroundColor",
                                    border_radius=123,
                                    button_action="buttonAction",
                                    link="link",
                                    text="text",
                                    text_color="textColor"
                                ),
                                ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                )
                            )
                        )],
                        custom_config=custom_config,
                        layout="layout"
                    ),
                    sms_message=pinpoint.CfnCampaign.CampaignSmsMessageProperty(
                        body="body",
                        entity_id="entityId",
                        message_type="messageType",
                        origination_number="originationNumber",
                        sender_id="senderId",
                        template_id="templateId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__19ee131a34a71e54155365b2853c207245d2bee1c5e924da6d8afba431a24d2d)
                check_type(argname="argument adm_message", value=adm_message, expected_type=type_hints["adm_message"])
                check_type(argname="argument apns_message", value=apns_message, expected_type=type_hints["apns_message"])
                check_type(argname="argument baidu_message", value=baidu_message, expected_type=type_hints["baidu_message"])
                check_type(argname="argument custom_message", value=custom_message, expected_type=type_hints["custom_message"])
                check_type(argname="argument default_message", value=default_message, expected_type=type_hints["default_message"])
                check_type(argname="argument email_message", value=email_message, expected_type=type_hints["email_message"])
                check_type(argname="argument gcm_message", value=gcm_message, expected_type=type_hints["gcm_message"])
                check_type(argname="argument in_app_message", value=in_app_message, expected_type=type_hints["in_app_message"])
                check_type(argname="argument sms_message", value=sms_message, expected_type=type_hints["sms_message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if adm_message is not None:
                self._values["adm_message"] = adm_message
            if apns_message is not None:
                self._values["apns_message"] = apns_message
            if baidu_message is not None:
                self._values["baidu_message"] = baidu_message
            if custom_message is not None:
                self._values["custom_message"] = custom_message
            if default_message is not None:
                self._values["default_message"] = default_message
            if email_message is not None:
                self._values["email_message"] = email_message
            if gcm_message is not None:
                self._values["gcm_message"] = gcm_message
            if in_app_message is not None:
                self._values["in_app_message"] = in_app_message
            if sms_message is not None:
                self._values["sms_message"] = sms_message

        @builtins.property
        def adm_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]]:
            '''The message that the campaign sends through the ADM (Amazon Device Messaging) channel.

            If specified, this message overrides the default message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-admmessage
            '''
            result = self._values.get("adm_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def apns_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]]:
            '''The message that the campaign sends through the APNs (Apple Push Notification service) channel.

            If specified, this message overrides the default message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-apnsmessage
            '''
            result = self._values.get("apns_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def baidu_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]]:
            '''The message that the campaign sends through the Baidu (Baidu Cloud Push) channel.

            If specified, this message overrides the default message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-baidumessage
            '''
            result = self._values.get("baidu_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def custom_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignCustomMessageProperty"]]:
            '''The message that the campaign sends through a custom channel, as specified by the delivery configuration ( ``CustomDeliveryConfiguration`` ) settings for the campaign.

            If specified, this message overrides the default message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-custommessage
            '''
            result = self._values.get("custom_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignCustomMessageProperty"]], result)

        @builtins.property
        def default_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]]:
            '''The default message that the campaign sends through all the channels that are configured for the campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-defaultmessage
            '''
            result = self._values.get("default_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def email_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignEmailMessageProperty"]]:
            '''The message that the campaign sends through the email channel.

            If specified, this message overrides the default message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-emailmessage
            '''
            result = self._values.get("email_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignEmailMessageProperty"]], result)

        @builtins.property
        def gcm_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]]:
            '''The message that the campaign sends through the GCM channel, which enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service.

            If specified, this message overrides the default message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-gcmmessage
            '''
            result = self._values.get("gcm_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def in_app_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignInAppMessageProperty"]]:
            '''The default message for the in-app messaging channel.

            This message overrides the default message ( ``DefaultMessage`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-inappmessage
            '''
            result = self._values.get("in_app_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignInAppMessageProperty"]], result)

        @builtins.property
        def sms_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignSmsMessageProperty"]]:
            '''The message that the campaign sends through the SMS channel.

            If specified, this message overrides the default message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-smsmessage
            '''
            result = self._values.get("sms_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignSmsMessageProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.MessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "body": "body",
            "image_icon_url": "imageIconUrl",
            "image_small_icon_url": "imageSmallIconUrl",
            "image_url": "imageUrl",
            "json_body": "jsonBody",
            "media_url": "mediaUrl",
            "raw_content": "rawContent",
            "silent_push": "silentPush",
            "time_to_live": "timeToLive",
            "title": "title",
            "url": "url",
        },
    )
    class MessageProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            image_icon_url: typing.Optional[builtins.str] = None,
            image_small_icon_url: typing.Optional[builtins.str] = None,
            image_url: typing.Optional[builtins.str] = None,
            json_body: typing.Optional[builtins.str] = None,
            media_url: typing.Optional[builtins.str] = None,
            raw_content: typing.Optional[builtins.str] = None,
            silent_push: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            time_to_live: typing.Optional[jsii.Number] = None,
            title: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the content and settings for a push notification that's sent to recipients of a campaign.

            :param action: The action to occur if a recipient taps the push notification. Valid values are:. - ``OPEN_APP`` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. - ``DEEP_LINK`` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android. - ``URL`` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.
            :param body: The body of the notification message. The maximum number of characters is 200.
            :param image_icon_url: The URL of the image to display as the push notification icon, such as the icon for the app.
            :param image_small_icon_url: The URL of the image to display as the small, push notification icon, such as a small version of the icon for the app.
            :param image_url: The URL of an image to display in the push notification.
            :param json_body: The JSON payload to use for a silent push notification.
            :param media_url: The URL of the image or video to display in the push notification.
            :param raw_content: The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.
            :param silent_push: Specifies whether the notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration, displaying messages in an in-app message center, or supporting phone home functionality.
            :param time_to_live: The number of seconds that the push notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when it's sent to a push notification service. If this value is ``0`` , the service treats the notification as if it expires immediately and the service doesn't store or try to deliver the notification again. This value doesn't apply to messages that are sent through the Amazon Device Messaging (ADM) service.
            :param title: The title to display above the notification message on a recipient's device.
            :param url: The URL to open in a recipient's default mobile browser, if a recipient taps the push notification and the value of the ``Action`` property is ``URL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                message_property = pinpoint.CfnCampaign.MessageProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_small_icon_url="imageSmallIconUrl",
                    image_url="imageUrl",
                    json_body="jsonBody",
                    media_url="mediaUrl",
                    raw_content="rawContent",
                    silent_push=False,
                    time_to_live=123,
                    title="title",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e10775d47c3c54e5c5d9eb755116a023f41dcce118ba93b6367946e2ab5d357)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument image_icon_url", value=image_icon_url, expected_type=type_hints["image_icon_url"])
                check_type(argname="argument image_small_icon_url", value=image_small_icon_url, expected_type=type_hints["image_small_icon_url"])
                check_type(argname="argument image_url", value=image_url, expected_type=type_hints["image_url"])
                check_type(argname="argument json_body", value=json_body, expected_type=type_hints["json_body"])
                check_type(argname="argument media_url", value=media_url, expected_type=type_hints["media_url"])
                check_type(argname="argument raw_content", value=raw_content, expected_type=type_hints["raw_content"])
                check_type(argname="argument silent_push", value=silent_push, expected_type=type_hints["silent_push"])
                check_type(argname="argument time_to_live", value=time_to_live, expected_type=type_hints["time_to_live"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if body is not None:
                self._values["body"] = body
            if image_icon_url is not None:
                self._values["image_icon_url"] = image_icon_url
            if image_small_icon_url is not None:
                self._values["image_small_icon_url"] = image_small_icon_url
            if image_url is not None:
                self._values["image_url"] = image_url
            if json_body is not None:
                self._values["json_body"] = json_body
            if media_url is not None:
                self._values["media_url"] = media_url
            if raw_content is not None:
                self._values["raw_content"] = raw_content
            if silent_push is not None:
                self._values["silent_push"] = silent_push
            if time_to_live is not None:
                self._values["time_to_live"] = time_to_live
            if title is not None:
                self._values["title"] = title
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The action to occur if a recipient taps the push notification. Valid values are:.

            - ``OPEN_APP`` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
            - ``DEEP_LINK`` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
            - ``URL`` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The body of the notification message.

            The maximum number of characters is 200.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_icon_url(self) -> typing.Optional[builtins.str]:
            '''The URL of the image to display as the push notification icon, such as the icon for the app.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageiconurl
            '''
            result = self._values.get("image_icon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_small_icon_url(self) -> typing.Optional[builtins.str]:
            '''The URL of the image to display as the small, push notification icon, such as a small version of the icon for the app.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imagesmalliconurl
            '''
            result = self._values.get("image_small_icon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_url(self) -> typing.Optional[builtins.str]:
            '''The URL of an image to display in the push notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageurl
            '''
            result = self._values.get("image_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def json_body(self) -> typing.Optional[builtins.str]:
            '''The JSON payload to use for a silent push notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-jsonbody
            '''
            result = self._values.get("json_body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def media_url(self) -> typing.Optional[builtins.str]:
            '''The URL of the image or video to display in the push notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-mediaurl
            '''
            result = self._values.get("media_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def raw_content(self) -> typing.Optional[builtins.str]:
            '''The raw, JSON-formatted string to use as the payload for the notification message.

            If specified, this value overrides all other content for the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-rawcontent
            '''
            result = self._values.get("raw_content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def silent_push(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the notification is a silent push notification, which is a push notification that doesn't display on a recipient's device.

            Silent push notifications can be used for cases such as updating an app's configuration, displaying messages in an in-app message center, or supporting phone home functionality.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-silentpush
            '''
            result = self._values.get("silent_push")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def time_to_live(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds that the push notification service should keep the message, if the service is unable to deliver the notification the first time.

            This value is converted to an expiration value when it's sent to a push notification service. If this value is ``0`` , the service treats the notification as if it expires immediately and the service doesn't store or try to deliver the notification again.

            This value doesn't apply to messages that are sent through the Amazon Device Messaging (ADM) service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-timetolive
            '''
            result = self._values.get("time_to_live")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''The title to display above the notification message on a recipient's device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL to open in a recipient's default mobile browser, if a recipient taps the push notification and the value of the ``Action`` property is ``URL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison_operator": "comparisonOperator", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(
            self,
            *,
            comparison_operator: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies metric-based criteria for including or excluding endpoints from a segment.

            These criteria derive from custom metrics that you define for endpoints.

            :param comparison_operator: The operator to use when comparing metric values. Valid values are: ``GREATER_THAN`` , ``LESS_THAN`` , ``GREATER_THAN_OR_EQUAL`` , ``LESS_THAN_OR_EQUAL`` , and ``EQUAL`` .
            :param value: The value to compare.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                metric_dimension_property = pinpoint.CfnCampaign.MetricDimensionProperty(
                    comparison_operator="comparisonOperator",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__745d5a430d0962dfe8f060c450b75b4f10183f52b049bde8621fe86f62aca87f)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if comparison_operator is not None:
                self._values["comparison_operator"] = comparison_operator
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def comparison_operator(self) -> typing.Optional[builtins.str]:
            '''The operator to use when comparing metric values.

            Valid values are: ``GREATER_THAN`` , ``LESS_THAN`` , ``GREATER_THAN_OR_EQUAL`` , ``LESS_THAN_OR_EQUAL`` , and ``EQUAL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The value to compare.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.OverrideButtonConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"button_action": "buttonAction", "link": "link"},
    )
    class OverrideButtonConfigurationProperty:
        def __init__(
            self,
            *,
            button_action: typing.Optional[builtins.str] = None,
            link: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration of a button with settings that are specific to a certain device type.

            :param button_action: The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following: - ``LINK`` – A link to a web destination. - ``DEEP_LINK`` – A link to a specific page in an application. - ``CLOSE`` – Dismisses the message.
            :param link: The destination (such as a URL) for a button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                override_button_configuration_property = pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                    button_action="buttonAction",
                    link="link"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c3b91e735b0193b6a55e963c7e865354137511b772f20b5d5141bbdaa7ab3330)
                check_type(argname="argument button_action", value=button_action, expected_type=type_hints["button_action"])
                check_type(argname="argument link", value=link, expected_type=type_hints["link"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if button_action is not None:
                self._values["button_action"] = button_action
            if link is not None:
                self._values["link"] = link

        @builtins.property
        def button_action(self) -> typing.Optional[builtins.str]:
            '''The action that occurs when a recipient chooses a button in an in-app message.

            You can specify one of the following:

            - ``LINK`` – A link to a web destination.
            - ``DEEP_LINK`` – A link to a specific page in an application.
            - ``CLOSE`` – Dismisses the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html#cfn-pinpoint-campaign-overridebuttonconfiguration-buttonaction
            '''
            result = self._values.get("button_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def link(self) -> typing.Optional[builtins.str]:
            '''The destination (such as a URL) for a button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html#cfn-pinpoint-campaign-overridebuttonconfiguration-link
            '''
            result = self._values.get("link")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OverrideButtonConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.QuietTimeProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class QuietTimeProperty:
        def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
            '''Specifies the start and end times that define a time range when messages aren't sent to endpoints.

            :param end: The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use ``02:30`` to represent 2:30 AM, or ``14:30`` to represent 2:30 PM.
            :param start: The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use ``02:30`` to represent 2:30 AM, or ``14:30`` to represent 2:30 PM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-quiettime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                quiet_time_property = pinpoint.CfnCampaign.QuietTimeProperty(
                    end="end",
                    start="start"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ac197d4cddf9ac51bf378c659cf40f2873cba889a659e00e4af9364d7f3eb40)
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
                check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end": end,
                "start": start,
            }

        @builtins.property
        def end(self) -> builtins.str:
            '''The specific time when quiet time ends.

            This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use ``02:30`` to represent 2:30 AM, or ``14:30`` to represent 2:30 PM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-quiettime.html#cfn-pinpoint-campaign-quiettime-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start(self) -> builtins.str:
            '''The specific time when quiet time begins.

            This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use ``02:30`` to represent 2:30 AM, or ``14:30`` to represent 2:30 PM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-quiettime.html#cfn-pinpoint-campaign-quiettime-start
            '''
            result = self._values.get("start")
            assert result is not None, "Required property 'start' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuietTimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_time": "endTime",
            "event_filter": "eventFilter",
            "frequency": "frequency",
            "is_local_time": "isLocalTime",
            "quiet_time": "quietTime",
            "start_time": "startTime",
            "time_zone": "timeZone",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            end_time: typing.Optional[builtins.str] = None,
            event_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CampaignEventFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            frequency: typing.Optional[builtins.str] = None,
            is_local_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            quiet_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.QuietTimeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            start_time: typing.Optional[builtins.str] = None,
            time_zone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the schedule settings for a campaign.

            :param end_time: The scheduled time, in ISO 8601 format, when the campaign ended or will end.
            :param event_filter: The type of event that causes the campaign to be sent, if the value of the ``Frequency`` property is ``EVENT`` .
            :param frequency: Specifies how often the campaign is sent or whether the campaign is sent in response to a specific event.
            :param is_local_time: Specifies whether the start and end times for the campaign schedule use each recipient's local time. To base the schedule on each recipient's local time, set this value to ``true`` .
            :param quiet_time: The default quiet time for the campaign. Quiet time is a specific time range when a campaign doesn't send messages to endpoints, if all the following conditions are met: - The ``EndpointDemographic.Timezone`` property of the endpoint is set to a valid value. - The current time in the endpoint's time zone is later than or equal to the time specified by the ``QuietTime.Start`` property for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified by the ``QuietTime.End`` property for the campaign. If any of the preceding conditions isn't met, the endpoint will receive messages from the campaign, even if quiet time is enabled.
            :param start_time: The scheduled time when the campaign began or will begin. Valid values are: ``IMMEDIATE`` , to start the campaign immediately; or, a specific time in ISO 8601 format.
            :param time_zone: The starting UTC offset for the campaign schedule, if the value of the ``IsLocalTime`` property is ``true`` . Valid values are: ``UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+13, UTC-02, UTC-03, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-10,`` and ``UTC-11`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # attributes: Any
                # metrics: Any
                
                schedule_property = pinpoint.CfnCampaign.ScheduleProperty(
                    end_time="endTime",
                    event_filter=pinpoint.CfnCampaign.CampaignEventFilterProperty(
                        dimensions=pinpoint.CfnCampaign.EventDimensionsProperty(
                            attributes=attributes,
                            event_type=pinpoint.CfnCampaign.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            metrics=metrics
                        ),
                        filter_type="filterType"
                    ),
                    frequency="frequency",
                    is_local_time=False,
                    quiet_time=pinpoint.CfnCampaign.QuietTimeProperty(
                        end="end",
                        start="start"
                    ),
                    start_time="startTime",
                    time_zone="timeZone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b66ee1a8ddef7f92fbc394edfdc3e9420175412f7af13cdc63cea4db024d06a6)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument event_filter", value=event_filter, expected_type=type_hints["event_filter"])
                check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
                check_type(argname="argument is_local_time", value=is_local_time, expected_type=type_hints["is_local_time"])
                check_type(argname="argument quiet_time", value=quiet_time, expected_type=type_hints["quiet_time"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
                check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if end_time is not None:
                self._values["end_time"] = end_time
            if event_filter is not None:
                self._values["event_filter"] = event_filter
            if frequency is not None:
                self._values["frequency"] = frequency
            if is_local_time is not None:
                self._values["is_local_time"] = is_local_time
            if quiet_time is not None:
                self._values["quiet_time"] = quiet_time
            if start_time is not None:
                self._values["start_time"] = start_time
            if time_zone is not None:
                self._values["time_zone"] = time_zone

        @builtins.property
        def end_time(self) -> typing.Optional[builtins.str]:
            '''The scheduled time, in ISO 8601 format, when the campaign ended or will end.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-endtime
            '''
            result = self._values.get("end_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_filter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignEventFilterProperty"]]:
            '''The type of event that causes the campaign to be sent, if the value of the ``Frequency`` property is ``EVENT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-eventfilter
            '''
            result = self._values.get("event_filter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CampaignEventFilterProperty"]], result)

        @builtins.property
        def frequency(self) -> typing.Optional[builtins.str]:
            '''Specifies how often the campaign is sent or whether the campaign is sent in response to a specific event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-frequency
            '''
            result = self._values.get("frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_local_time(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the start and end times for the campaign schedule use each recipient's local time.

            To base the schedule on each recipient's local time, set this value to ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-islocaltime
            '''
            result = self._values.get("is_local_time")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def quiet_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.QuietTimeProperty"]]:
            '''The default quiet time for the campaign.

            Quiet time is a specific time range when a campaign doesn't send messages to endpoints, if all the following conditions are met:

            - The ``EndpointDemographic.Timezone`` property of the endpoint is set to a valid value.
            - The current time in the endpoint's time zone is later than or equal to the time specified by the ``QuietTime.Start`` property for the campaign.
            - The current time in the endpoint's time zone is earlier than or equal to the time specified by the ``QuietTime.End`` property for the campaign.

            If any of the preceding conditions isn't met, the endpoint will receive messages from the campaign, even if quiet time is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-quiettime
            '''
            result = self._values.get("quiet_time")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.QuietTimeProperty"]], result)

        @builtins.property
        def start_time(self) -> typing.Optional[builtins.str]:
            '''The scheduled time when the campaign began or will begin.

            Valid values are: ``IMMEDIATE`` , to start the campaign immediately; or, a specific time in ISO 8601 format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def time_zone(self) -> typing.Optional[builtins.str]:
            '''The starting UTC offset for the campaign schedule, if the value of the ``IsLocalTime`` property is ``true`` .

            Valid values are: ``UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+13, UTC-02, UTC-03, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-10,`` and ``UTC-11`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-timezone
            '''
            result = self._values.get("time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.SetDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class SetDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the dimension type and values for a segment dimension.

            :param dimension_type: The type of segment dimension to use. Valid values are: ``INCLUSIVE`` , endpoints that match the criteria are included in the segment; and, ``EXCLUSIVE`` , endpoints that match the criteria are excluded from the segment.
            :param values: The criteria values to use for the segment dimension. Depending on the value of the ``DimensionType`` property, endpoints are included or excluded from the segment if their values match the criteria values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                set_dimension_property = pinpoint.CfnCampaign.SetDimensionProperty(
                    dimension_type="dimensionType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__708a9738583487f1b206b6e3901c7d9e8ffb999c5ecf2d03d83130db9cbe8a86)
                check_type(argname="argument dimension_type", value=dimension_type, expected_type=type_hints["dimension_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimension_type is not None:
                self._values["dimension_type"] = dimension_type
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def dimension_type(self) -> typing.Optional[builtins.str]:
            '''The type of segment dimension to use.

            Valid values are: ``INCLUSIVE`` , endpoints that match the criteria are included in the segment; and, ``EXCLUSIVE`` , endpoints that match the criteria are excluded from the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The criteria values to use for the segment dimension.

            Depending on the value of the ``DimensionType`` property, endpoints are included or excluded from the segment if their values match the criteria values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SetDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.TemplateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "email_template": "emailTemplate",
            "push_template": "pushTemplate",
            "sms_template": "smsTemplate",
            "voice_template": "voiceTemplate",
        },
    )
    class TemplateConfigurationProperty:
        def __init__(
            self,
            *,
            email_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            push_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sms_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            voice_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the message template to use for the message, for each type of channel.

            :param email_template: The email template to use for the message.
            :param push_template: The push notification template to use for the message.
            :param sms_template: The SMS template to use for the message.
            :param voice_template: The voice template to use for the message. This object isn't supported for campaigns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                template_configuration_property = pinpoint.CfnCampaign.TemplateConfigurationProperty(
                    email_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    push_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    sms_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    voice_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c789b47b3af2152c0a9bba84f3affeffa89dda156afa661148fbea98621da92c)
                check_type(argname="argument email_template", value=email_template, expected_type=type_hints["email_template"])
                check_type(argname="argument push_template", value=push_template, expected_type=type_hints["push_template"])
                check_type(argname="argument sms_template", value=sms_template, expected_type=type_hints["sms_template"])
                check_type(argname="argument voice_template", value=voice_template, expected_type=type_hints["voice_template"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email_template is not None:
                self._values["email_template"] = email_template
            if push_template is not None:
                self._values["push_template"] = push_template
            if sms_template is not None:
                self._values["sms_template"] = sms_template
            if voice_template is not None:
                self._values["voice_template"] = voice_template

        @builtins.property
        def email_template(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateProperty"]]:
            '''The email template to use for the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html#cfn-pinpoint-campaign-templateconfiguration-emailtemplate
            '''
            result = self._values.get("email_template")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateProperty"]], result)

        @builtins.property
        def push_template(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateProperty"]]:
            '''The push notification template to use for the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html#cfn-pinpoint-campaign-templateconfiguration-pushtemplate
            '''
            result = self._values.get("push_template")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateProperty"]], result)

        @builtins.property
        def sms_template(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateProperty"]]:
            '''The SMS template to use for the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html#cfn-pinpoint-campaign-templateconfiguration-smstemplate
            '''
            result = self._values.get("sms_template")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateProperty"]], result)

        @builtins.property
        def voice_template(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateProperty"]]:
            '''The voice template to use for the message.

            This object isn't supported for campaigns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html#cfn-pinpoint-campaign-templateconfiguration-voicetemplate
            '''
            result = self._values.get("voice_template")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.TemplateProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class TemplateProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the name and version of the message template to use for the message.

            :param name: The name of the message template to use for the message. If specified, this value must match the name of an existing message template.
            :param version: The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the `Template Versions <https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html>`_ resource. If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-template.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                template_property = pinpoint.CfnCampaign.TemplateProperty(
                    name="name",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91bebb7687409a9932eec1ddc30e9e5bce21c49bebfb75e054c06cc0e3bc8854)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the message template to use for the message.

            If specified, this value must match the name of an existing message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-template.html#cfn-pinpoint-campaign-template-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for the version of the message template to use for the message.

            If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the `Template Versions <https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html>`_ resource.

            If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-template.html#cfn-pinpoint-campaign-template-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaign.WriteTreatmentResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_delivery_configuration": "customDeliveryConfiguration",
            "message_configuration": "messageConfiguration",
            "schedule": "schedule",
            "size_percent": "sizePercent",
            "template_configuration": "templateConfiguration",
            "treatment_description": "treatmentDescription",
            "treatment_name": "treatmentName",
        },
    )
    class WriteTreatmentResourceProperty:
        def __init__(
            self,
            *,
            custom_delivery_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CustomDeliveryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            message_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.MessageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            size_percent: typing.Optional[jsii.Number] = None,
            template_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TemplateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            treatment_description: typing.Optional[builtins.str] = None,
            treatment_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the settings for a campaign treatment.

            A *treatment* is a variation of a campaign that's used for A/B testing of a campaign.

            :param custom_delivery_configuration: The delivery configuration settings for sending the treatment through a custom channel. This object is required if the ``MessageConfiguration`` object for the treatment specifies a ``CustomMessage`` object.
            :param message_configuration: The message configuration settings for the treatment.
            :param schedule: The schedule settings for the treatment.
            :param size_percent: The allocated percentage of users (segment members) to send the treatment to.
            :param template_configuration: The message template to use for the treatment.
            :param treatment_description: A custom description of the treatment.
            :param treatment_name: A custom name for the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # attributes: Any
                # custom_config: Any
                # metrics: Any
                
                write_treatment_resource_property = pinpoint.CfnCampaign.WriteTreatmentResourceProperty(
                    custom_delivery_configuration=pinpoint.CfnCampaign.CustomDeliveryConfigurationProperty(
                        delivery_uri="deliveryUri",
                        endpoint_types=["endpointTypes"]
                    ),
                    message_configuration=pinpoint.CfnCampaign.MessageConfigurationProperty(
                        adm_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        apns_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        baidu_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        custom_message=pinpoint.CfnCampaign.CampaignCustomMessageProperty(
                            data="data"
                        ),
                        default_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        email_message=pinpoint.CfnCampaign.CampaignEmailMessageProperty(
                            body="body",
                            from_address="fromAddress",
                            html_body="htmlBody",
                            title="title"
                        ),
                        gcm_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        in_app_message=pinpoint.CfnCampaign.CampaignInAppMessageProperty(
                            content=[pinpoint.CfnCampaign.InAppMessageContentProperty(
                                background_color="backgroundColor",
                                body_config=pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                                    alignment="alignment",
                                    body="body",
                                    text_color="textColor"
                                ),
                                header_config=pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                                    alignment="alignment",
                                    header="header",
                                    text_color="textColor"
                                ),
                                image_url="imageUrl",
                                primary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                    android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    ),
                                    default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                        background_color="backgroundColor",
                                        border_radius=123,
                                        button_action="buttonAction",
                                        link="link",
                                        text="text",
                                        text_color="textColor"
                                    ),
                                    ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    ),
                                    web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    )
                                ),
                                secondary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                    android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    ),
                                    default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                        background_color="backgroundColor",
                                        border_radius=123,
                                        button_action="buttonAction",
                                        link="link",
                                        text="text",
                                        text_color="textColor"
                                    ),
                                    ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    ),
                                    web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    )
                                )
                            )],
                            custom_config=custom_config,
                            layout="layout"
                        ),
                        sms_message=pinpoint.CfnCampaign.CampaignSmsMessageProperty(
                            body="body",
                            entity_id="entityId",
                            message_type="messageType",
                            origination_number="originationNumber",
                            sender_id="senderId",
                            template_id="templateId"
                        )
                    ),
                    schedule=pinpoint.CfnCampaign.ScheduleProperty(
                        end_time="endTime",
                        event_filter=pinpoint.CfnCampaign.CampaignEventFilterProperty(
                            dimensions=pinpoint.CfnCampaign.EventDimensionsProperty(
                                attributes=attributes,
                                event_type=pinpoint.CfnCampaign.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                metrics=metrics
                            ),
                            filter_type="filterType"
                        ),
                        frequency="frequency",
                        is_local_time=False,
                        quiet_time=pinpoint.CfnCampaign.QuietTimeProperty(
                            end="end",
                            start="start"
                        ),
                        start_time="startTime",
                        time_zone="timeZone"
                    ),
                    size_percent=123,
                    template_configuration=pinpoint.CfnCampaign.TemplateConfigurationProperty(
                        email_template=pinpoint.CfnCampaign.TemplateProperty(
                            name="name",
                            version="version"
                        ),
                        push_template=pinpoint.CfnCampaign.TemplateProperty(
                            name="name",
                            version="version"
                        ),
                        sms_template=pinpoint.CfnCampaign.TemplateProperty(
                            name="name",
                            version="version"
                        ),
                        voice_template=pinpoint.CfnCampaign.TemplateProperty(
                            name="name",
                            version="version"
                        )
                    ),
                    treatment_description="treatmentDescription",
                    treatment_name="treatmentName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b64050a2eeb087f58f88d6a71e465dce41ef9c2d308dac9e92c90fd2f8d3384d)
                check_type(argname="argument custom_delivery_configuration", value=custom_delivery_configuration, expected_type=type_hints["custom_delivery_configuration"])
                check_type(argname="argument message_configuration", value=message_configuration, expected_type=type_hints["message_configuration"])
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
                check_type(argname="argument size_percent", value=size_percent, expected_type=type_hints["size_percent"])
                check_type(argname="argument template_configuration", value=template_configuration, expected_type=type_hints["template_configuration"])
                check_type(argname="argument treatment_description", value=treatment_description, expected_type=type_hints["treatment_description"])
                check_type(argname="argument treatment_name", value=treatment_name, expected_type=type_hints["treatment_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_delivery_configuration is not None:
                self._values["custom_delivery_configuration"] = custom_delivery_configuration
            if message_configuration is not None:
                self._values["message_configuration"] = message_configuration
            if schedule is not None:
                self._values["schedule"] = schedule
            if size_percent is not None:
                self._values["size_percent"] = size_percent
            if template_configuration is not None:
                self._values["template_configuration"] = template_configuration
            if treatment_description is not None:
                self._values["treatment_description"] = treatment_description
            if treatment_name is not None:
                self._values["treatment_name"] = treatment_name

        @builtins.property
        def custom_delivery_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CustomDeliveryConfigurationProperty"]]:
            '''The delivery configuration settings for sending the treatment through a custom channel.

            This object is required if the ``MessageConfiguration`` object for the treatment specifies a ``CustomMessage`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-customdeliveryconfiguration
            '''
            result = self._values.get("custom_delivery_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CustomDeliveryConfigurationProperty"]], result)

        @builtins.property
        def message_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageConfigurationProperty"]]:
            '''The message configuration settings for the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-messageconfiguration
            '''
            result = self._values.get("message_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.MessageConfigurationProperty"]], result)

        @builtins.property
        def schedule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ScheduleProperty"]]:
            '''The schedule settings for the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-schedule
            '''
            result = self._values.get("schedule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ScheduleProperty"]], result)

        @builtins.property
        def size_percent(self) -> typing.Optional[jsii.Number]:
            '''The allocated percentage of users (segment members) to send the treatment to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-sizepercent
            '''
            result = self._values.get("size_percent")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def template_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateConfigurationProperty"]]:
            '''The message template to use for the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-templateconfiguration
            '''
            result = self._values.get("template_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TemplateConfigurationProperty"]], result)

        @builtins.property
        def treatment_description(self) -> typing.Optional[builtins.str]:
            '''A custom description of the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentdescription
            '''
            result = self._values.get("treatment_description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def treatment_name(self) -> typing.Optional[builtins.str]:
            '''A custom name for the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentname
            '''
            result = self._values.get("treatment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WriteTreatmentResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnCampaignProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "name": "name",
        "schedule": "schedule",
        "segment_id": "segmentId",
        "additional_treatments": "additionalTreatments",
        "campaign_hook": "campaignHook",
        "custom_delivery_configuration": "customDeliveryConfiguration",
        "description": "description",
        "holdout_percent": "holdoutPercent",
        "is_paused": "isPaused",
        "limits": "limits",
        "message_configuration": "messageConfiguration",
        "priority": "priority",
        "segment_version": "segmentVersion",
        "tags": "tags",
        "template_configuration": "templateConfiguration",
        "treatment_description": "treatmentDescription",
        "treatment_name": "treatmentName",
    },
)
class CfnCampaignProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        name: builtins.str,
        schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
        segment_id: builtins.str,
        additional_treatments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.WriteTreatmentResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        campaign_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CampaignHookProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_delivery_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CustomDeliveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        holdout_percent: typing.Optional[jsii.Number] = None,
        is_paused: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.LimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        message_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        segment_version: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        template_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        treatment_description: typing.Optional[builtins.str] = None,
        treatment_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCampaign``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that the campaign is associated with.
        :param name: The name of the campaign.
        :param schedule: The schedule settings for the campaign.
        :param segment_id: The unique identifier for the segment to associate with the campaign.
        :param additional_treatments: An array of requests that defines additional treatments for the campaign, in addition to the default treatment for the campaign.
        :param campaign_hook: Specifies the Lambda function to use as a code hook for a campaign.
        :param custom_delivery_configuration: The delivery configuration settings for sending the treatment through a custom channel. This object is required if the ``MessageConfiguration`` object for the treatment specifies a ``CustomMessage`` object.
        :param description: A custom description of the campaign.
        :param holdout_percent: The allocated percentage of users (segment members) who shouldn't receive messages from the campaign.
        :param is_paused: Specifies whether to pause the campaign. A paused campaign doesn't run unless you resume it by changing this value to ``false`` . If you restart a campaign, the campaign restarts from the beginning and not at the point you paused it. If a campaign is running it will complete and then pause. Pause only pauses or skips the next run for a recurring future scheduled campaign. A campaign scheduled for immediate can't be paused.
        :param limits: The messaging limits for the campaign.
        :param message_configuration: The message configuration settings for the campaign.
        :param priority: An integer between 1 and 5, inclusive, that represents the priority of the in-app message campaign, where 1 is the highest priority and 5 is the lowest. If there are multiple messages scheduled to be displayed at the same time, the priority determines the order in which those messages are displayed.
        :param segment_version: The version of the segment to associate with the campaign.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_configuration: The message template to use for the treatment.
        :param treatment_description: A custom description of the default treatment for the campaign.
        :param treatment_name: A custom name of the default treatment for the campaign, if the campaign has multiple treatments. A *treatment* is a variation of a campaign that's used for A/B testing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            # attributes: Any
            # custom_config: Any
            # metrics: Any
            # tags: Any
            
            cfn_campaign_props = pinpoint.CfnCampaignProps(
                application_id="applicationId",
                name="name",
                schedule=pinpoint.CfnCampaign.ScheduleProperty(
                    end_time="endTime",
                    event_filter=pinpoint.CfnCampaign.CampaignEventFilterProperty(
                        dimensions=pinpoint.CfnCampaign.EventDimensionsProperty(
                            attributes=attributes,
                            event_type=pinpoint.CfnCampaign.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            metrics=metrics
                        ),
                        filter_type="filterType"
                    ),
                    frequency="frequency",
                    is_local_time=False,
                    quiet_time=pinpoint.CfnCampaign.QuietTimeProperty(
                        end="end",
                        start="start"
                    ),
                    start_time="startTime",
                    time_zone="timeZone"
                ),
                segment_id="segmentId",
            
                # the properties below are optional
                additional_treatments=[pinpoint.CfnCampaign.WriteTreatmentResourceProperty(
                    custom_delivery_configuration=pinpoint.CfnCampaign.CustomDeliveryConfigurationProperty(
                        delivery_uri="deliveryUri",
                        endpoint_types=["endpointTypes"]
                    ),
                    message_configuration=pinpoint.CfnCampaign.MessageConfigurationProperty(
                        adm_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        apns_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        baidu_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        custom_message=pinpoint.CfnCampaign.CampaignCustomMessageProperty(
                            data="data"
                        ),
                        default_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        email_message=pinpoint.CfnCampaign.CampaignEmailMessageProperty(
                            body="body",
                            from_address="fromAddress",
                            html_body="htmlBody",
                            title="title"
                        ),
                        gcm_message=pinpoint.CfnCampaign.MessageProperty(
                            action="action",
                            body="body",
                            image_icon_url="imageIconUrl",
                            image_small_icon_url="imageSmallIconUrl",
                            image_url="imageUrl",
                            json_body="jsonBody",
                            media_url="mediaUrl",
                            raw_content="rawContent",
                            silent_push=False,
                            time_to_live=123,
                            title="title",
                            url="url"
                        ),
                        in_app_message=pinpoint.CfnCampaign.CampaignInAppMessageProperty(
                            content=[pinpoint.CfnCampaign.InAppMessageContentProperty(
                                background_color="backgroundColor",
                                body_config=pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                                    alignment="alignment",
                                    body="body",
                                    text_color="textColor"
                                ),
                                header_config=pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                                    alignment="alignment",
                                    header="header",
                                    text_color="textColor"
                                ),
                                image_url="imageUrl",
                                primary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                    android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    ),
                                    default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                        background_color="backgroundColor",
                                        border_radius=123,
                                        button_action="buttonAction",
                                        link="link",
                                        text="text",
                                        text_color="textColor"
                                    ),
                                    ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    ),
                                    web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    )
                                ),
                                secondary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                    android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    ),
                                    default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                        background_color="backgroundColor",
                                        border_radius=123,
                                        button_action="buttonAction",
                                        link="link",
                                        text="text",
                                        text_color="textColor"
                                    ),
                                    ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    ),
                                    web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                        button_action="buttonAction",
                                        link="link"
                                    )
                                )
                            )],
                            custom_config=custom_config,
                            layout="layout"
                        ),
                        sms_message=pinpoint.CfnCampaign.CampaignSmsMessageProperty(
                            body="body",
                            entity_id="entityId",
                            message_type="messageType",
                            origination_number="originationNumber",
                            sender_id="senderId",
                            template_id="templateId"
                        )
                    ),
                    schedule=pinpoint.CfnCampaign.ScheduleProperty(
                        end_time="endTime",
                        event_filter=pinpoint.CfnCampaign.CampaignEventFilterProperty(
                            dimensions=pinpoint.CfnCampaign.EventDimensionsProperty(
                                attributes=attributes,
                                event_type=pinpoint.CfnCampaign.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                metrics=metrics
                            ),
                            filter_type="filterType"
                        ),
                        frequency="frequency",
                        is_local_time=False,
                        quiet_time=pinpoint.CfnCampaign.QuietTimeProperty(
                            end="end",
                            start="start"
                        ),
                        start_time="startTime",
                        time_zone="timeZone"
                    ),
                    size_percent=123,
                    template_configuration=pinpoint.CfnCampaign.TemplateConfigurationProperty(
                        email_template=pinpoint.CfnCampaign.TemplateProperty(
                            name="name",
                            version="version"
                        ),
                        push_template=pinpoint.CfnCampaign.TemplateProperty(
                            name="name",
                            version="version"
                        ),
                        sms_template=pinpoint.CfnCampaign.TemplateProperty(
                            name="name",
                            version="version"
                        ),
                        voice_template=pinpoint.CfnCampaign.TemplateProperty(
                            name="name",
                            version="version"
                        )
                    ),
                    treatment_description="treatmentDescription",
                    treatment_name="treatmentName"
                )],
                campaign_hook=pinpoint.CfnCampaign.CampaignHookProperty(
                    lambda_function_name="lambdaFunctionName",
                    mode="mode",
                    web_url="webUrl"
                ),
                custom_delivery_configuration=pinpoint.CfnCampaign.CustomDeliveryConfigurationProperty(
                    delivery_uri="deliveryUri",
                    endpoint_types=["endpointTypes"]
                ),
                description="description",
                holdout_percent=123,
                is_paused=False,
                limits=pinpoint.CfnCampaign.LimitsProperty(
                    daily=123,
                    maximum_duration=123,
                    messages_per_second=123,
                    session=123,
                    total=123
                ),
                message_configuration=pinpoint.CfnCampaign.MessageConfigurationProperty(
                    adm_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    apns_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    baidu_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    custom_message=pinpoint.CfnCampaign.CampaignCustomMessageProperty(
                        data="data"
                    ),
                    default_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    email_message=pinpoint.CfnCampaign.CampaignEmailMessageProperty(
                        body="body",
                        from_address="fromAddress",
                        html_body="htmlBody",
                        title="title"
                    ),
                    gcm_message=pinpoint.CfnCampaign.MessageProperty(
                        action="action",
                        body="body",
                        image_icon_url="imageIconUrl",
                        image_small_icon_url="imageSmallIconUrl",
                        image_url="imageUrl",
                        json_body="jsonBody",
                        media_url="mediaUrl",
                        raw_content="rawContent",
                        silent_push=False,
                        time_to_live=123,
                        title="title",
                        url="url"
                    ),
                    in_app_message=pinpoint.CfnCampaign.CampaignInAppMessageProperty(
                        content=[pinpoint.CfnCampaign.InAppMessageContentProperty(
                            background_color="backgroundColor",
                            body_config=pinpoint.CfnCampaign.InAppMessageBodyConfigProperty(
                                alignment="alignment",
                                body="body",
                                text_color="textColor"
                            ),
                            header_config=pinpoint.CfnCampaign.InAppMessageHeaderConfigProperty(
                                alignment="alignment",
                                header="header",
                                text_color="textColor"
                            ),
                            image_url="imageUrl",
                            primary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                    background_color="backgroundColor",
                                    border_radius=123,
                                    button_action="buttonAction",
                                    link="link",
                                    text="text",
                                    text_color="textColor"
                                ),
                                ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                )
                            ),
                            secondary_btn=pinpoint.CfnCampaign.InAppMessageButtonProperty(
                                android=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                default_config=pinpoint.CfnCampaign.DefaultButtonConfigurationProperty(
                                    background_color="backgroundColor",
                                    border_radius=123,
                                    button_action="buttonAction",
                                    link="link",
                                    text="text",
                                    text_color="textColor"
                                ),
                                ios=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                ),
                                web=pinpoint.CfnCampaign.OverrideButtonConfigurationProperty(
                                    button_action="buttonAction",
                                    link="link"
                                )
                            )
                        )],
                        custom_config=custom_config,
                        layout="layout"
                    ),
                    sms_message=pinpoint.CfnCampaign.CampaignSmsMessageProperty(
                        body="body",
                        entity_id="entityId",
                        message_type="messageType",
                        origination_number="originationNumber",
                        sender_id="senderId",
                        template_id="templateId"
                    )
                ),
                priority=123,
                segment_version=123,
                tags=tags,
                template_configuration=pinpoint.CfnCampaign.TemplateConfigurationProperty(
                    email_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    push_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    sms_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    ),
                    voice_template=pinpoint.CfnCampaign.TemplateProperty(
                        name="name",
                        version="version"
                    )
                ),
                treatment_description="treatmentDescription",
                treatment_name="treatmentName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8089eb09489d44c4a64192dbd9c8fe4f0ae8d17684ba1c3d9763b2d2393e97f)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument segment_id", value=segment_id, expected_type=type_hints["segment_id"])
            check_type(argname="argument additional_treatments", value=additional_treatments, expected_type=type_hints["additional_treatments"])
            check_type(argname="argument campaign_hook", value=campaign_hook, expected_type=type_hints["campaign_hook"])
            check_type(argname="argument custom_delivery_configuration", value=custom_delivery_configuration, expected_type=type_hints["custom_delivery_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument holdout_percent", value=holdout_percent, expected_type=type_hints["holdout_percent"])
            check_type(argname="argument is_paused", value=is_paused, expected_type=type_hints["is_paused"])
            check_type(argname="argument limits", value=limits, expected_type=type_hints["limits"])
            check_type(argname="argument message_configuration", value=message_configuration, expected_type=type_hints["message_configuration"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument segment_version", value=segment_version, expected_type=type_hints["segment_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_configuration", value=template_configuration, expected_type=type_hints["template_configuration"])
            check_type(argname="argument treatment_description", value=treatment_description, expected_type=type_hints["treatment_description"])
            check_type(argname="argument treatment_name", value=treatment_name, expected_type=type_hints["treatment_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "name": name,
            "schedule": schedule,
            "segment_id": segment_id,
        }
        if additional_treatments is not None:
            self._values["additional_treatments"] = additional_treatments
        if campaign_hook is not None:
            self._values["campaign_hook"] = campaign_hook
        if custom_delivery_configuration is not None:
            self._values["custom_delivery_configuration"] = custom_delivery_configuration
        if description is not None:
            self._values["description"] = description
        if holdout_percent is not None:
            self._values["holdout_percent"] = holdout_percent
        if is_paused is not None:
            self._values["is_paused"] = is_paused
        if limits is not None:
            self._values["limits"] = limits
        if message_configuration is not None:
            self._values["message_configuration"] = message_configuration
        if priority is not None:
            self._values["priority"] = priority
        if segment_version is not None:
            self._values["segment_version"] = segment_version
        if tags is not None:
            self._values["tags"] = tags
        if template_configuration is not None:
            self._values["template_configuration"] = template_configuration
        if treatment_description is not None:
            self._values["treatment_description"] = treatment_description
        if treatment_name is not None:
            self._values["treatment_name"] = treatment_name

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the campaign is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCampaign.ScheduleProperty]:
        '''The schedule settings for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCampaign.ScheduleProperty], result)

    @builtins.property
    def segment_id(self) -> builtins.str:
        '''The unique identifier for the segment to associate with the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentid
        '''
        result = self._values.get("segment_id")
        assert result is not None, "Required property 'segment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_treatments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.WriteTreatmentResourceProperty]]]]:
        '''An array of requests that defines additional treatments for the campaign, in addition to the default treatment for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-additionaltreatments
        '''
        result = self._values.get("additional_treatments")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.WriteTreatmentResourceProperty]]]], result)

    @builtins.property
    def campaign_hook(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CampaignHookProperty]]:
        '''Specifies the Lambda function to use as a code hook for a campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-campaignhook
        '''
        result = self._values.get("campaign_hook")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CampaignHookProperty]], result)

    @builtins.property
    def custom_delivery_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CustomDeliveryConfigurationProperty]]:
        '''The delivery configuration settings for sending the treatment through a custom channel.

        This object is required if the ``MessageConfiguration`` object for the treatment specifies a ``CustomMessage`` object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-customdeliveryconfiguration
        '''
        result = self._values.get("custom_delivery_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CustomDeliveryConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def holdout_percent(self) -> typing.Optional[jsii.Number]:
        '''The allocated percentage of users (segment members) who shouldn't receive messages from the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-holdoutpercent
        '''
        result = self._values.get("holdout_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def is_paused(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to pause the campaign.

        A paused campaign doesn't run unless you resume it by changing this value to ``false`` . If you restart a campaign, the campaign restarts from the beginning and not at the point you paused it. If a campaign is running it will complete and then pause. Pause only pauses or skips the next run for a recurring future scheduled campaign. A campaign scheduled for immediate can't be paused.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-ispaused
        '''
        result = self._values.get("is_paused")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def limits(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.LimitsProperty]]:
        '''The messaging limits for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-limits
        '''
        result = self._values.get("limits")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.LimitsProperty]], result)

    @builtins.property
    def message_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.MessageConfigurationProperty]]:
        '''The message configuration settings for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-messageconfiguration
        '''
        result = self._values.get("message_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.MessageConfigurationProperty]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''An integer between 1 and 5, inclusive, that represents the priority of the in-app message campaign, where 1 is the highest priority and 5 is the lowest.

        If there are multiple messages scheduled to be displayed at the same time, the priority determines the order in which those messages are displayed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def segment_version(self) -> typing.Optional[jsii.Number]:
        '''The version of the segment to associate with the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentversion
        '''
        result = self._values.get("segment_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.TemplateConfigurationProperty]]:
        '''The message template to use for the treatment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-templateconfiguration
        '''
        result = self._values.get("template_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.TemplateConfigurationProperty]], result)

    @builtins.property
    def treatment_description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the default treatment for the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentdescription
        '''
        result = self._values.get("treatment_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def treatment_name(self) -> typing.Optional[builtins.str]:
        '''A custom name of the default treatment for the campaign, if the campaign has multiple treatments.

        A *treatment* is a variation of a campaign that's used for A/B testing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentname
        '''
        result = self._values.get("treatment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCampaignProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEmailChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnEmailChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    You can use the email channel to send email to users. Before you can use Amazon Pinpoint to send email, you must enable the email channel for an Amazon Pinpoint application.

    The EmailChannel resource represents the status, identity, and other settings of the email channel for an application

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_email_channel = pinpoint.CfnEmailChannel(self, "MyCfnEmailChannel",
            application_id="applicationId",
            from_address="fromAddress",
            identity="identity",
        
            # the properties below are optional
            configuration_set="configurationSet",
            enabled=False,
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        from_address: builtins.str,
        identity: builtins.str,
        configuration_set: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that you're specifying the email channel for.
        :param from_address: The verified email address that you want to send email from when you send email through the channel.
        :param identity: The Amazon Resource Name (ARN) of the identity, verified with Amazon Simple Email Service (Amazon SES), that you want to use when you send email through the channel.
        :param configuration_set: The `Amazon SES configuration set <https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html>`_ that you want to apply to messages that you send through the channel.
        :param enabled: Specifies whether to enable the email channel for the application.
        :param role_arn: The ARN of the AWS Identity and Access Management (IAM) role that you want Amazon Pinpoint to use when it submits email-related event data for the channel.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7abae51eb3b1f161941e50db5fbebe5cf3c749c2e815f973039ad61896339f89)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEmailChannelProps(
            application_id=application_id,
            from_address=from_address,
            identity=identity,
            configuration_set=configuration_set,
            enabled=enabled,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ba4a138e19718fd866fa836cf4c6257f18fa42d0f772d51831891027e5e310)
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
            type_hints = typing.get_type_hints(_typecheckingstub__804ea79845a98fef52b447794c21d02312b3947df72f3a2cdbebf5c0ef8cadc0)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that you're specifying the email channel for.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2b7ac710eb003a05553de77978a0bf432e0b082141849898c5dfbf164b61b4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="fromAddress")
    def from_address(self) -> builtins.str:
        '''The verified email address that you want to send email from when you send email through the channel.'''
        return typing.cast(builtins.str, jsii.get(self, "fromAddress"))

    @from_address.setter
    def from_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3571c9e54456a7ff75562506238acc99b19962f8b9247aba2fe3df1a62aac7c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromAddress", value)

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the identity, verified with Amazon Simple Email Service (Amazon SES), that you want to use when you send email through the channel.'''
        return typing.cast(builtins.str, jsii.get(self, "identity"))

    @identity.setter
    def identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5982a64c199a3dbd05157469619fb87103bb18d60ac17c887674ca1c98af71a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identity", value)

    @builtins.property
    @jsii.member(jsii_name="configurationSet")
    def configuration_set(self) -> typing.Optional[builtins.str]:
        '''The `Amazon SES configuration set <https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html>`_ that you want to apply to messages that you send through the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationSet"))

    @configuration_set.setter
    def configuration_set(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0552904454280c91b20abb544ebf8f0d5d10b3561c644ab81e7433e68739c947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSet", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the email channel for the application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6552928532890b0bb4451f89e36f2fd0599fa25332569a30589de6dabd1c2ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AWS Identity and Access Management (IAM) role that you want Amazon Pinpoint to use when it submits email-related event data for the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91d75ea3a5bc3900bbc4b0958bbc0263a57362f325b830004dddc72b23dfe1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnEmailChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "from_address": "fromAddress",
        "identity": "identity",
        "configuration_set": "configurationSet",
        "enabled": "enabled",
        "role_arn": "roleArn",
    },
)
class CfnEmailChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        from_address: builtins.str,
        identity: builtins.str,
        configuration_set: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEmailChannel``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that you're specifying the email channel for.
        :param from_address: The verified email address that you want to send email from when you send email through the channel.
        :param identity: The Amazon Resource Name (ARN) of the identity, verified with Amazon Simple Email Service (Amazon SES), that you want to use when you send email through the channel.
        :param configuration_set: The `Amazon SES configuration set <https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html>`_ that you want to apply to messages that you send through the channel.
        :param enabled: Specifies whether to enable the email channel for the application.
        :param role_arn: The ARN of the AWS Identity and Access Management (IAM) role that you want Amazon Pinpoint to use when it submits email-related event data for the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_email_channel_props = pinpoint.CfnEmailChannelProps(
                application_id="applicationId",
                from_address="fromAddress",
                identity="identity",
            
                # the properties below are optional
                configuration_set="configurationSet",
                enabled=False,
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31b287f2c5e7cfc3790c0eca9541325a73a2157dce8dbc1d3b7d9fa702d77ff)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument from_address", value=from_address, expected_type=type_hints["from_address"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument configuration_set", value=configuration_set, expected_type=type_hints["configuration_set"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "from_address": from_address,
            "identity": identity,
        }
        if configuration_set is not None:
            self._values["configuration_set"] = configuration_set
        if enabled is not None:
            self._values["enabled"] = enabled
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that you're specifying the email channel for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def from_address(self) -> builtins.str:
        '''The verified email address that you want to send email from when you send email through the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-fromaddress
        '''
        result = self._values.get("from_address")
        assert result is not None, "Required property 'from_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the identity, verified with Amazon Simple Email Service (Amazon SES), that you want to use when you send email through the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-identity
        '''
        result = self._values.get("identity")
        assert result is not None, "Required property 'identity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_set(self) -> typing.Optional[builtins.str]:
        '''The `Amazon SES configuration set <https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html>`_ that you want to apply to messages that you send through the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-configurationset
        '''
        result = self._values.get("configuration_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the email channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AWS Identity and Access Management (IAM) role that you want Amazon Pinpoint to use when it submits email-related event data for the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEmailChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEmailTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnEmailTemplate",
):
    '''Creates a message template that you can use in messages that are sent through the email channel.

    A *message template* is a set of content and settings that you can define, save, and reuse in messages for any of your Amazon Pinpoint applications.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        # tags: Any
        
        cfn_email_template = pinpoint.CfnEmailTemplate(self, "MyCfnEmailTemplate",
            subject="subject",
            template_name="templateName",
        
            # the properties below are optional
            default_substitutions="defaultSubstitutions",
            html_part="htmlPart",
            tags=tags,
            template_description="templateDescription",
            text_part="textPart"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        subject: builtins.str,
        template_name: builtins.str,
        default_substitutions: typing.Optional[builtins.str] = None,
        html_part: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
        text_part: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param subject: The subject line, or title, to use in email messages that are based on the message template.
        :param template_name: The name of the message template.
        :param default_substitutions: A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.
        :param html_part: The message body, in HTML format, to use in email messages that are based on the message template. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_description: A custom description of the message template.
        :param text_part: The message body, in plain text format, to use in email messages that are based on the message template. We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de92e890e6311a7e5df00104dcb543dcbde46783a8f7ec2de256f236f59ae292)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEmailTemplateProps(
            subject=subject,
            template_name=template_name,
            default_substitutions=default_substitutions,
            html_part=html_part,
            tags=tags,
            template_description=template_description,
            text_part=text_part,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f42a278c52013133399f446e5f556044c118bbcf83e230b9f2be36ee65826b57)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c3e092405beeb55725972c93849cea40cde8553e295e89147bbdf1dabae9b7c)
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
        '''The Amazon Resource Name (ARN) of the message template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        '''The subject line, or title, to use in email messages that are based on the message template.'''
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__842354b6737d3f066011001448187e6cd47eb9292c3c3d91c53ed677fabd97e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> builtins.str:
        '''The name of the message template.'''
        return typing.cast(builtins.str, jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d7fb2858f2a5e78df5c14250eeed341724afc16b64bc850806da4d4163ec985)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSubstitutions")
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''A JSON object that specifies the default values to use for message variables in the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubstitutions"))

    @default_substitutions.setter
    def default_substitutions(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__425a551c7dd2994ef2bc28faf10c1acccbf845469fdf77c6105ccd9dfe28de77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSubstitutions", value)

    @builtins.property
    @jsii.member(jsii_name="htmlPart")
    def html_part(self) -> typing.Optional[builtins.str]:
        '''The message body, in HTML format, to use in email messages that are based on the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlPart"))

    @html_part.setter
    def html_part(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3064679445a684550ed2de9bfc8b89465ffd8b09aabf1e7a299ac6a62dbee6bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "htmlPart", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b95a2d7d0d9191200b484886260a273682ff8d2a18c40ed91b782e67a644f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateDescription")
    def template_description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDescription"))

    @template_description.setter
    def template_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bf14ba8036655640c904b31bf6ece4c3ad5c62108cf693250e9d46e9cdc90af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateDescription", value)

    @builtins.property
    @jsii.member(jsii_name="textPart")
    def text_part(self) -> typing.Optional[builtins.str]:
        '''The message body, in plain text format, to use in email messages that are based on the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textPart"))

    @text_part.setter
    def text_part(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ff0c2083d81dbecc8b9bdfa839def0127c389629ac4dce169887c0ca4f55952)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textPart", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnEmailTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "subject": "subject",
        "template_name": "templateName",
        "default_substitutions": "defaultSubstitutions",
        "html_part": "htmlPart",
        "tags": "tags",
        "template_description": "templateDescription",
        "text_part": "textPart",
    },
)
class CfnEmailTemplateProps:
    def __init__(
        self,
        *,
        subject: builtins.str,
        template_name: builtins.str,
        default_substitutions: typing.Optional[builtins.str] = None,
        html_part: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
        text_part: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEmailTemplate``.

        :param subject: The subject line, or title, to use in email messages that are based on the message template.
        :param template_name: The name of the message template.
        :param default_substitutions: A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.
        :param html_part: The message body, in HTML format, to use in email messages that are based on the message template. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_description: A custom description of the message template.
        :param text_part: The message body, in plain text format, to use in email messages that are based on the message template. We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            # tags: Any
            
            cfn_email_template_props = pinpoint.CfnEmailTemplateProps(
                subject="subject",
                template_name="templateName",
            
                # the properties below are optional
                default_substitutions="defaultSubstitutions",
                html_part="htmlPart",
                tags=tags,
                template_description="templateDescription",
                text_part="textPart"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82e765dee130dbbde67e866633bee4ee835d943cf8392dcd6605e0dde4e3821c)
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            check_type(argname="argument default_substitutions", value=default_substitutions, expected_type=type_hints["default_substitutions"])
            check_type(argname="argument html_part", value=html_part, expected_type=type_hints["html_part"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_description", value=template_description, expected_type=type_hints["template_description"])
            check_type(argname="argument text_part", value=text_part, expected_type=type_hints["text_part"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subject": subject,
            "template_name": template_name,
        }
        if default_substitutions is not None:
            self._values["default_substitutions"] = default_substitutions
        if html_part is not None:
            self._values["html_part"] = html_part
        if tags is not None:
            self._values["tags"] = tags
        if template_description is not None:
            self._values["template_description"] = template_description
        if text_part is not None:
            self._values["text_part"] = text_part

    @builtins.property
    def subject(self) -> builtins.str:
        '''The subject line, or title, to use in email messages that are based on the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-subject
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_name(self) -> builtins.str:
        '''The name of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatename
        '''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''A JSON object that specifies the default values to use for message variables in the message template.

        This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-defaultsubstitutions
        '''
        result = self._values.get("default_substitutions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def html_part(self) -> typing.Optional[builtins.str]:
        '''The message body, in HTML format, to use in email messages that are based on the message template.

        We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-htmlpart
        '''
        result = self._values.get("html_part")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatedescription
        '''
        result = self._values.get("template_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text_part(self) -> typing.Optional[builtins.str]:
        '''The message body, in plain text format, to use in email messages that are based on the message template.

        We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-textpart
        '''
        result = self._values.get("text_part")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEmailTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEventStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnEventStream",
):
    '''Creates a new event stream for an application or updates the settings of an existing event stream for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_event_stream = pinpoint.CfnEventStream(self, "MyCfnEventStream",
            application_id="applicationId",
            destination_stream_arn="destinationStreamArn",
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        destination_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that you want to export data from.
        :param destination_stream_arn: The Amazon Resource Name (ARN) of the Amazon Kinesis data stream or Amazon Kinesis Data Firehose delivery stream that you want to publish event data to. For a Kinesis data stream, the ARN format is: ``arn:aws:kinesis: region : account-id :stream/ stream_name`` For a Kinesis Data Firehose delivery stream, the ARN format is: ``arn:aws:firehose: region : account-id :deliverystream/ stream_name``
        :param role_arn: The AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to publish event data to the stream in your AWS account.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7494978a71be7ff003e54391145803489ba95ef1f0579d626731310f2491ba6d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventStreamProps(
            application_id=application_id,
            destination_stream_arn=destination_stream_arn,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__435c126caf6964a902f691992ec1aed7a9475c2ef6e6810980f351ded58de5d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57c83ccd79833fec29db310b9fa416d840e817fcaf74b16d9b3022cc002f0d0a)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that you want to export data from.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a0d74f7910ba4b74041b4a3f8ceb6f9b383589c9435748173e5da796ac0a468)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="destinationStreamArn")
    def destination_stream_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Kinesis data stream or Amazon Kinesis Data Firehose delivery stream that you want to publish event data to.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationStreamArn"))

    @destination_stream_arn.setter
    def destination_stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__523733f36a90ab4e5bdf0e39f89059f03b9879e928c1155d176f7a0df99913b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationStreamArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to publish event data to the stream in your AWS account.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a3815f734b46370b2c5a51cd95e50e77cbb9061f0c2d09fbe8c169d14033420)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnEventStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "destination_stream_arn": "destinationStreamArn",
        "role_arn": "roleArn",
    },
)
class CfnEventStreamProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        destination_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnEventStream``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that you want to export data from.
        :param destination_stream_arn: The Amazon Resource Name (ARN) of the Amazon Kinesis data stream or Amazon Kinesis Data Firehose delivery stream that you want to publish event data to. For a Kinesis data stream, the ARN format is: ``arn:aws:kinesis: region : account-id :stream/ stream_name`` For a Kinesis Data Firehose delivery stream, the ARN format is: ``arn:aws:firehose: region : account-id :deliverystream/ stream_name``
        :param role_arn: The AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to publish event data to the stream in your AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_event_stream_props = pinpoint.CfnEventStreamProps(
                application_id="applicationId",
                destination_stream_arn="destinationStreamArn",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef26e6e94ef7fa3322d0acc6e2ff1ff55f9317bf3c2fad1529941a4ab3b906e)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument destination_stream_arn", value=destination_stream_arn, expected_type=type_hints["destination_stream_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "destination_stream_arn": destination_stream_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that you want to export data from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_stream_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Kinesis data stream or Amazon Kinesis Data Firehose delivery stream that you want to publish event data to.

        For a Kinesis data stream, the ARN format is: ``arn:aws:kinesis: region : account-id :stream/ stream_name``

        For a Kinesis Data Firehose delivery stream, the ARN format is: ``arn:aws:firehose: region : account-id :deliverystream/ stream_name``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-destinationstreamarn
        '''
        result = self._values.get("destination_stream_arn")
        assert result is not None, "Required property 'destination_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to publish event data to the stream in your AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGCMChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnGCMChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    You can use the GCM channel to send push notification messages to the Firebase Cloud Messaging (FCM) service, which replaced the Google Cloud Messaging (GCM) service. Before you use Amazon Pinpoint to send notifications to FCM, you have to enable the GCM channel for an Amazon Pinpoint application.

    The GCMChannel resource represents the status and authentication settings of the GCM channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_gCMChannel = pinpoint.CfnGCMChannel(self, "MyCfnGCMChannel",
            api_key="apiKey",
            application_id="applicationId",
        
            # the properties below are optional
            enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_key: The Web API key, also called the *server key* , that you received from Google to communicate with Google services.
        :param application_id: The unique identifier for the Amazon Pinpoint application that the GCM channel applies to.
        :param enabled: Specifies whether to enable the GCM channel for the Amazon Pinpoint application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb3f8f63a6157e10547523707b6985118a3e678783d2603097b290368727ae6a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGCMChannelProps(
            api_key=api_key, application_id=application_id, enabled=enabled
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__732d5f076acad8123890183928c3e25c1f90349cfdf24a56d105df721fe5dcb2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__83e3844a6b42a96c5783c4b32eee3c53d44a5c8c29b7a53d4285dfe56debd9a4)
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
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        '''The Web API key, also called the *server key* , that you received from Google to communicate with Google services.'''
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99b00ece767606c36fcd8737c20c953bd966f1fb88386fcfccdecab9be060dfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the GCM channel applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5cf7652f52bd0665760eefdef4ebe4661341c7d2f743790a82538cc9b1a59da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the GCM channel for the Amazon Pinpoint application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__934c050e152924d121e2ce630b51de8fe2580d8d1dda58e4e88cd58ff0b0bbfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnGCMChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "application_id": "applicationId",
        "enabled": "enabled",
    },
)
class CfnGCMChannelProps:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGCMChannel``.

        :param api_key: The Web API key, also called the *server key* , that you received from Google to communicate with Google services.
        :param application_id: The unique identifier for the Amazon Pinpoint application that the GCM channel applies to.
        :param enabled: Specifies whether to enable the GCM channel for the Amazon Pinpoint application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_gCMChannel_props = pinpoint.CfnGCMChannelProps(
                api_key="apiKey",
                application_id="applicationId",
            
                # the properties below are optional
                enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e274fb934af0ad701780242707b5b8268879db22917a3c6b496e2649c2c225eb)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
            "application_id": application_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def api_key(self) -> builtins.str:
        '''The Web API key, also called the *server key* , that you received from Google to communicate with Google services.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-apikey
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the GCM channel applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the GCM channel for the Amazon Pinpoint application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGCMChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnInAppTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnInAppTemplate",
):
    '''Creates a message template that you can use to send in-app messages.

    A message template is a set of content and settings that you can define, save, and reuse in messages for any of your Amazon Pinpoint applications. The In-App channel is unavailable in AWS GovCloud (US).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        # custom_config: Any
        # tags: Any
        
        cfn_in_app_template = pinpoint.CfnInAppTemplate(self, "MyCfnInAppTemplate",
            template_name="templateName",
        
            # the properties below are optional
            content=[pinpoint.CfnInAppTemplate.InAppMessageContentProperty(
                background_color="backgroundColor",
                body_config=pinpoint.CfnInAppTemplate.BodyConfigProperty(
                    alignment="alignment",
                    body="body",
                    text_color="textColor"
                ),
                header_config=pinpoint.CfnInAppTemplate.HeaderConfigProperty(
                    alignment="alignment",
                    header="header",
                    text_color="textColor"
                ),
                image_url="imageUrl",
                primary_btn=pinpoint.CfnInAppTemplate.ButtonConfigProperty(
                    android=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    ),
                    default_config=pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty(
                        background_color="backgroundColor",
                        border_radius=123,
                        button_action="buttonAction",
                        link="link",
                        text="text",
                        text_color="textColor"
                    ),
                    ios=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    ),
                    web=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    )
                ),
                secondary_btn=pinpoint.CfnInAppTemplate.ButtonConfigProperty(
                    android=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    ),
                    default_config=pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty(
                        background_color="backgroundColor",
                        border_radius=123,
                        button_action="buttonAction",
                        link="link",
                        text="text",
                        text_color="textColor"
                    ),
                    ios=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    ),
                    web=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    )
                )
            )],
            custom_config=custom_config,
            layout="layout",
            tags=tags,
            template_description="templateDescription"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        template_name: builtins.str,
        content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.InAppMessageContentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        custom_config: typing.Any = None,
        layout: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param template_name: The name of the in-app message template.
        :param content: An object that contains information about the content of an in-app message, including its title and body text, text colors, background colors, images, buttons, and behaviors.
        :param custom_config: Custom data, in the form of key-value pairs, that is included in an in-app messaging payload.
        :param layout: A string that determines the appearance of the in-app message. You can specify one of the following:. - ``BOTTOM_BANNER`` – a message that appears as a banner at the bottom of the page. - ``TOP_BANNER`` – a message that appears as a banner at the top of the page. - ``OVERLAYS`` – a message that covers entire screen. - ``MOBILE_FEED`` – a message that appears in a window in front of the page. - ``MIDDLE_BANNER`` – a message that appears as a banner in the middle of the page. - ``CAROUSEL`` – a scrollable layout of up to five unique messages.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_description: An optional description of the in-app template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e512a1e228b31487f3066dd3e4275e9158997062fd71387d46ccec37606a2d52)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInAppTemplateProps(
            template_name=template_name,
            content=content,
            custom_config=custom_config,
            layout=layout,
            tags=tags,
            template_description=template_description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5b14ad185ba48d75f55570e3ad1a13d78e14254d3beb52e4d282f7011b5af3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__102b7ba4ca5d76c2bcb7d579a1ce2b270541375ae87c3324aec995eb1fb8f88d)
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
        '''The Amazon Resource Name (ARN) of the message template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> builtins.str:
        '''The name of the in-app message template.'''
        return typing.cast(builtins.str, jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__783c9d3a13dcf9b910dcd7009b3f921a2196ebca80cad6d5f6d8d9a2131b6317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateName", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.InAppMessageContentProperty"]]]]:
        '''An object that contains information about the content of an in-app message, including its title and body text, text colors, background colors, images, buttons, and behaviors.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.InAppMessageContentProperty"]]]], jsii.get(self, "content"))

    @content.setter
    def content(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.InAppMessageContentProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29c306b59b5a82d785edcc24ad4f92afce261ef2ea4bd786f4c5db21c19d779c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="customConfig")
    def custom_config(self) -> typing.Any:
        '''Custom data, in the form of key-value pairs, that is included in an in-app messaging payload.'''
        return typing.cast(typing.Any, jsii.get(self, "customConfig"))

    @custom_config.setter
    def custom_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2ca164aa9281ef31e4a2e0a2f52e7cb0f98adf80d4e8d05370ff01dc3a8c724)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customConfig", value)

    @builtins.property
    @jsii.member(jsii_name="layout")
    def layout(self) -> typing.Optional[builtins.str]:
        '''A string that determines the appearance of the in-app message.

        You can specify one of the following:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "layout"))

    @layout.setter
    def layout(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b43b04a5a55917e5e8acbe2af8759330169d92abcb7e8f70276761c87fde2b09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layout", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26614d8a74e54c08b442c84a7e9695ce8c396ca893b287d6ae5b7ff009122c16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateDescription")
    def template_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the in-app template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDescription"))

    @template_description.setter
    def template_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2c97689320ae40b05704c91857a6423cddaf3dbeffb7698e0a39308b57220d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateDescription", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnInAppTemplate.BodyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alignment": "alignment",
            "body": "body",
            "text_color": "textColor",
        },
    )
    class BodyConfigProperty:
        def __init__(
            self,
            *,
            alignment: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            text_color: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration of the main body text of the in-app message.

            :param alignment: The text alignment of the main body text of the message. Acceptable values: ``LEFT`` , ``CENTER`` , ``RIGHT`` .
            :param body: The main body text of the message.
            :param text_color: The color of the body text, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                body_config_property = pinpoint.CfnInAppTemplate.BodyConfigProperty(
                    alignment="alignment",
                    body="body",
                    text_color="textColor"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03774d65640cad8e484f201e69f919d0ed339dbe776b950876db72c627fd35c7)
                check_type(argname="argument alignment", value=alignment, expected_type=type_hints["alignment"])
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument text_color", value=text_color, expected_type=type_hints["text_color"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alignment is not None:
                self._values["alignment"] = alignment
            if body is not None:
                self._values["body"] = body
            if text_color is not None:
                self._values["text_color"] = text_color

        @builtins.property
        def alignment(self) -> typing.Optional[builtins.str]:
            '''The text alignment of the main body text of the message.

            Acceptable values: ``LEFT`` , ``CENTER`` , ``RIGHT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-alignment
            '''
            result = self._values.get("alignment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The main body text of the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_color(self) -> typing.Optional[builtins.str]:
            '''The color of the body text, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-textcolor
            '''
            result = self._values.get("text_color")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BodyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnInAppTemplate.ButtonConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "android": "android",
            "default_config": "defaultConfig",
            "ios": "ios",
            "web": "web",
        },
    )
    class ButtonConfigProperty:
        def __init__(
            self,
            *,
            android: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.OverrideButtonConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.DefaultButtonConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ios: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.OverrideButtonConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            web: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.OverrideButtonConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the behavior of buttons that appear in an in-app message template.

            :param android: Optional button configuration to use for in-app messages sent to Android devices. This button configuration overrides the default button configuration.
            :param default_config: Specifies the default behavior of a button that appears in an in-app message. You can optionally add button configurations that specifically apply to iOS, Android, or web browser users.
            :param ios: Optional button configuration to use for in-app messages sent to iOS devices. This button configuration overrides the default button configuration.
            :param web: Optional button configuration to use for in-app messages sent to web applications. This button configuration overrides the default button configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                button_config_property = pinpoint.CfnInAppTemplate.ButtonConfigProperty(
                    android=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    ),
                    default_config=pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty(
                        background_color="backgroundColor",
                        border_radius=123,
                        button_action="buttonAction",
                        link="link",
                        text="text",
                        text_color="textColor"
                    ),
                    ios=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    ),
                    web=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                        button_action="buttonAction",
                        link="link"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b54d14fb9a053c1e37fd12c48b941690f58aa3a225fc8bb133010937f4249b84)
                check_type(argname="argument android", value=android, expected_type=type_hints["android"])
                check_type(argname="argument default_config", value=default_config, expected_type=type_hints["default_config"])
                check_type(argname="argument ios", value=ios, expected_type=type_hints["ios"])
                check_type(argname="argument web", value=web, expected_type=type_hints["web"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if android is not None:
                self._values["android"] = android
            if default_config is not None:
                self._values["default_config"] = default_config
            if ios is not None:
                self._values["ios"] = ios
            if web is not None:
                self._values["web"] = web

        @builtins.property
        def android(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.OverrideButtonConfigurationProperty"]]:
            '''Optional button configuration to use for in-app messages sent to Android devices.

            This button configuration overrides the default button configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-android
            '''
            result = self._values.get("android")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.OverrideButtonConfigurationProperty"]], result)

        @builtins.property
        def default_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.DefaultButtonConfigurationProperty"]]:
            '''Specifies the default behavior of a button that appears in an in-app message.

            You can optionally add button configurations that specifically apply to iOS, Android, or web browser users.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-defaultconfig
            '''
            result = self._values.get("default_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.DefaultButtonConfigurationProperty"]], result)

        @builtins.property
        def ios(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.OverrideButtonConfigurationProperty"]]:
            '''Optional button configuration to use for in-app messages sent to iOS devices.

            This button configuration overrides the default button configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-ios
            '''
            result = self._values.get("ios")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.OverrideButtonConfigurationProperty"]], result)

        @builtins.property
        def web(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.OverrideButtonConfigurationProperty"]]:
            '''Optional button configuration to use for in-app messages sent to web applications.

            This button configuration overrides the default button configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-web
            '''
            result = self._values.get("web")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.OverrideButtonConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ButtonConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "background_color": "backgroundColor",
            "border_radius": "borderRadius",
            "button_action": "buttonAction",
            "link": "link",
            "text": "text",
            "text_color": "textColor",
        },
    )
    class DefaultButtonConfigurationProperty:
        def __init__(
            self,
            *,
            background_color: typing.Optional[builtins.str] = None,
            border_radius: typing.Optional[jsii.Number] = None,
            button_action: typing.Optional[builtins.str] = None,
            link: typing.Optional[builtins.str] = None,
            text: typing.Optional[builtins.str] = None,
            text_color: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the default behavior of a button that appears in an in-app message.

            You can optionally add button configurations that specifically apply to iOS, Android, or web browser users.

            :param background_color: The background color of a button, expressed as a hex color code (such as #000000 for black).
            :param border_radius: The border radius of a button.
            :param button_action: The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following: - ``LINK`` – A link to a web destination. - ``DEEP_LINK`` – A link to a specific page in an application. - ``CLOSE`` – Dismisses the message.
            :param link: The destination (such as a URL) for a button.
            :param text: The text that appears on a button in an in-app message.
            :param text_color: The color of the body text in a button, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                default_button_configuration_property = pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty(
                    background_color="backgroundColor",
                    border_radius=123,
                    button_action="buttonAction",
                    link="link",
                    text="text",
                    text_color="textColor"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__062d1a7daee932b386386a6e49e873bba429615975bdf28124c7a6fc931c6aee)
                check_type(argname="argument background_color", value=background_color, expected_type=type_hints["background_color"])
                check_type(argname="argument border_radius", value=border_radius, expected_type=type_hints["border_radius"])
                check_type(argname="argument button_action", value=button_action, expected_type=type_hints["button_action"])
                check_type(argname="argument link", value=link, expected_type=type_hints["link"])
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
                check_type(argname="argument text_color", value=text_color, expected_type=type_hints["text_color"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if background_color is not None:
                self._values["background_color"] = background_color
            if border_radius is not None:
                self._values["border_radius"] = border_radius
            if button_action is not None:
                self._values["button_action"] = button_action
            if link is not None:
                self._values["link"] = link
            if text is not None:
                self._values["text"] = text
            if text_color is not None:
                self._values["text_color"] = text_color

        @builtins.property
        def background_color(self) -> typing.Optional[builtins.str]:
            '''The background color of a button, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-backgroundcolor
            '''
            result = self._values.get("background_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def border_radius(self) -> typing.Optional[jsii.Number]:
            '''The border radius of a button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-borderradius
            '''
            result = self._values.get("border_radius")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def button_action(self) -> typing.Optional[builtins.str]:
            '''The action that occurs when a recipient chooses a button in an in-app message.

            You can specify one of the following:

            - ``LINK`` – A link to a web destination.
            - ``DEEP_LINK`` – A link to a specific page in an application.
            - ``CLOSE`` – Dismisses the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-buttonaction
            '''
            result = self._values.get("button_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def link(self) -> typing.Optional[builtins.str]:
            '''The destination (such as a URL) for a button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-link
            '''
            result = self._values.get("link")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text(self) -> typing.Optional[builtins.str]:
            '''The text that appears on a button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-text
            '''
            result = self._values.get("text")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_color(self) -> typing.Optional[builtins.str]:
            '''The color of the body text in a button, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-textcolor
            '''
            result = self._values.get("text_color")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultButtonConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnInAppTemplate.HeaderConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alignment": "alignment",
            "header": "header",
            "text_color": "textColor",
        },
    )
    class HeaderConfigProperty:
        def __init__(
            self,
            *,
            alignment: typing.Optional[builtins.str] = None,
            header: typing.Optional[builtins.str] = None,
            text_color: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration and content of the header or title text of the in-app message.

            :param alignment: The text alignment of the title of the message. Acceptable values: ``LEFT`` , ``CENTER`` , ``RIGHT`` .
            :param header: The title text of the in-app message.
            :param text_color: The color of the title text, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                header_config_property = pinpoint.CfnInAppTemplate.HeaderConfigProperty(
                    alignment="alignment",
                    header="header",
                    text_color="textColor"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f33f1d8b7937ccb2928adfdd2a81f68a6c9e96bb0d037e0c9c6b6aa0311b8d5)
                check_type(argname="argument alignment", value=alignment, expected_type=type_hints["alignment"])
                check_type(argname="argument header", value=header, expected_type=type_hints["header"])
                check_type(argname="argument text_color", value=text_color, expected_type=type_hints["text_color"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alignment is not None:
                self._values["alignment"] = alignment
            if header is not None:
                self._values["header"] = header
            if text_color is not None:
                self._values["text_color"] = text_color

        @builtins.property
        def alignment(self) -> typing.Optional[builtins.str]:
            '''The text alignment of the title of the message.

            Acceptable values: ``LEFT`` , ``CENTER`` , ``RIGHT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-alignment
            '''
            result = self._values.get("alignment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def header(self) -> typing.Optional[builtins.str]:
            '''The title text of the in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-header
            '''
            result = self._values.get("header")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_color(self) -> typing.Optional[builtins.str]:
            '''The color of the title text, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-textcolor
            '''
            result = self._values.get("text_color")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HeaderConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnInAppTemplate.InAppMessageContentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "background_color": "backgroundColor",
            "body_config": "bodyConfig",
            "header_config": "headerConfig",
            "image_url": "imageUrl",
            "primary_btn": "primaryBtn",
            "secondary_btn": "secondaryBtn",
        },
    )
    class InAppMessageContentProperty:
        def __init__(
            self,
            *,
            background_color: typing.Optional[builtins.str] = None,
            body_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.BodyConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            header_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.HeaderConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_url: typing.Optional[builtins.str] = None,
            primary_btn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.ButtonConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            secondary_btn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInAppTemplate.ButtonConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration of an in-app message, including its header, body, buttons, colors, and images.

            :param background_color: The background color for an in-app message banner, expressed as a hex color code (such as #000000 for black).
            :param body_config: An object that contains configuration information about the header or title text of the in-app message.
            :param header_config: An object that contains configuration information about the header or title text of the in-app message.
            :param image_url: The URL of the image that appears on an in-app message banner.
            :param primary_btn: An object that contains configuration information about the primary button in an in-app message.
            :param secondary_btn: An object that contains configuration information about the secondary button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                in_app_message_content_property = pinpoint.CfnInAppTemplate.InAppMessageContentProperty(
                    background_color="backgroundColor",
                    body_config=pinpoint.CfnInAppTemplate.BodyConfigProperty(
                        alignment="alignment",
                        body="body",
                        text_color="textColor"
                    ),
                    header_config=pinpoint.CfnInAppTemplate.HeaderConfigProperty(
                        alignment="alignment",
                        header="header",
                        text_color="textColor"
                    ),
                    image_url="imageUrl",
                    primary_btn=pinpoint.CfnInAppTemplate.ButtonConfigProperty(
                        android=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        default_config=pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty(
                            background_color="backgroundColor",
                            border_radius=123,
                            button_action="buttonAction",
                            link="link",
                            text="text",
                            text_color="textColor"
                        ),
                        ios=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        web=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        )
                    ),
                    secondary_btn=pinpoint.CfnInAppTemplate.ButtonConfigProperty(
                        android=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        default_config=pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty(
                            background_color="backgroundColor",
                            border_radius=123,
                            button_action="buttonAction",
                            link="link",
                            text="text",
                            text_color="textColor"
                        ),
                        ios=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        web=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__195213fb034889c4b5d757d6fb9b79046ced092a52301af0483c67520253e406)
                check_type(argname="argument background_color", value=background_color, expected_type=type_hints["background_color"])
                check_type(argname="argument body_config", value=body_config, expected_type=type_hints["body_config"])
                check_type(argname="argument header_config", value=header_config, expected_type=type_hints["header_config"])
                check_type(argname="argument image_url", value=image_url, expected_type=type_hints["image_url"])
                check_type(argname="argument primary_btn", value=primary_btn, expected_type=type_hints["primary_btn"])
                check_type(argname="argument secondary_btn", value=secondary_btn, expected_type=type_hints["secondary_btn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if background_color is not None:
                self._values["background_color"] = background_color
            if body_config is not None:
                self._values["body_config"] = body_config
            if header_config is not None:
                self._values["header_config"] = header_config
            if image_url is not None:
                self._values["image_url"] = image_url
            if primary_btn is not None:
                self._values["primary_btn"] = primary_btn
            if secondary_btn is not None:
                self._values["secondary_btn"] = secondary_btn

        @builtins.property
        def background_color(self) -> typing.Optional[builtins.str]:
            '''The background color for an in-app message banner, expressed as a hex color code (such as #000000 for black).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-backgroundcolor
            '''
            result = self._values.get("background_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.BodyConfigProperty"]]:
            '''An object that contains configuration information about the header or title text of the in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-bodyconfig
            '''
            result = self._values.get("body_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.BodyConfigProperty"]], result)

        @builtins.property
        def header_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.HeaderConfigProperty"]]:
            '''An object that contains configuration information about the header or title text of the in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-headerconfig
            '''
            result = self._values.get("header_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.HeaderConfigProperty"]], result)

        @builtins.property
        def image_url(self) -> typing.Optional[builtins.str]:
            '''The URL of the image that appears on an in-app message banner.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-imageurl
            '''
            result = self._values.get("image_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary_btn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.ButtonConfigProperty"]]:
            '''An object that contains configuration information about the primary button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-primarybtn
            '''
            result = self._values.get("primary_btn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.ButtonConfigProperty"]], result)

        @builtins.property
        def secondary_btn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.ButtonConfigProperty"]]:
            '''An object that contains configuration information about the secondary button in an in-app message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-secondarybtn
            '''
            result = self._values.get("secondary_btn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInAppTemplate.ButtonConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InAppMessageContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"button_action": "buttonAction", "link": "link"},
    )
    class OverrideButtonConfigurationProperty:
        def __init__(
            self,
            *,
            button_action: typing.Optional[builtins.str] = None,
            link: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration of a button with settings that are specific to a certain device type.

            :param button_action: The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following: - ``LINK`` – A link to a web destination. - ``DEEP_LINK`` – A link to a specific page in an application. - ``CLOSE`` – Dismisses the message.
            :param link: The destination (such as a URL) for a button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                override_button_configuration_property = pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                    button_action="buttonAction",
                    link="link"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a29b7f724524fecb2d0850fe702875c3a15f609e99011276708d4c705b2e8fc)
                check_type(argname="argument button_action", value=button_action, expected_type=type_hints["button_action"])
                check_type(argname="argument link", value=link, expected_type=type_hints["link"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if button_action is not None:
                self._values["button_action"] = button_action
            if link is not None:
                self._values["link"] = link

        @builtins.property
        def button_action(self) -> typing.Optional[builtins.str]:
            '''The action that occurs when a recipient chooses a button in an in-app message.

            You can specify one of the following:

            - ``LINK`` – A link to a web destination.
            - ``DEEP_LINK`` – A link to a specific page in an application.
            - ``CLOSE`` – Dismisses the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html#cfn-pinpoint-inapptemplate-overridebuttonconfiguration-buttonaction
            '''
            result = self._values.get("button_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def link(self) -> typing.Optional[builtins.str]:
            '''The destination (such as a URL) for a button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html#cfn-pinpoint-inapptemplate-overridebuttonconfiguration-link
            '''
            result = self._values.get("link")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OverrideButtonConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnInAppTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "template_name": "templateName",
        "content": "content",
        "custom_config": "customConfig",
        "layout": "layout",
        "tags": "tags",
        "template_description": "templateDescription",
    },
)
class CfnInAppTemplateProps:
    def __init__(
        self,
        *,
        template_name: builtins.str,
        content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.InAppMessageContentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        custom_config: typing.Any = None,
        layout: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnInAppTemplate``.

        :param template_name: The name of the in-app message template.
        :param content: An object that contains information about the content of an in-app message, including its title and body text, text colors, background colors, images, buttons, and behaviors.
        :param custom_config: Custom data, in the form of key-value pairs, that is included in an in-app messaging payload.
        :param layout: A string that determines the appearance of the in-app message. You can specify one of the following:. - ``BOTTOM_BANNER`` – a message that appears as a banner at the bottom of the page. - ``TOP_BANNER`` – a message that appears as a banner at the top of the page. - ``OVERLAYS`` – a message that covers entire screen. - ``MOBILE_FEED`` – a message that appears in a window in front of the page. - ``MIDDLE_BANNER`` – a message that appears as a banner in the middle of the page. - ``CAROUSEL`` – a scrollable layout of up to five unique messages.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_description: An optional description of the in-app template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            # custom_config: Any
            # tags: Any
            
            cfn_in_app_template_props = pinpoint.CfnInAppTemplateProps(
                template_name="templateName",
            
                # the properties below are optional
                content=[pinpoint.CfnInAppTemplate.InAppMessageContentProperty(
                    background_color="backgroundColor",
                    body_config=pinpoint.CfnInAppTemplate.BodyConfigProperty(
                        alignment="alignment",
                        body="body",
                        text_color="textColor"
                    ),
                    header_config=pinpoint.CfnInAppTemplate.HeaderConfigProperty(
                        alignment="alignment",
                        header="header",
                        text_color="textColor"
                    ),
                    image_url="imageUrl",
                    primary_btn=pinpoint.CfnInAppTemplate.ButtonConfigProperty(
                        android=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        default_config=pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty(
                            background_color="backgroundColor",
                            border_radius=123,
                            button_action="buttonAction",
                            link="link",
                            text="text",
                            text_color="textColor"
                        ),
                        ios=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        web=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        )
                    ),
                    secondary_btn=pinpoint.CfnInAppTemplate.ButtonConfigProperty(
                        android=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        default_config=pinpoint.CfnInAppTemplate.DefaultButtonConfigurationProperty(
                            background_color="backgroundColor",
                            border_radius=123,
                            button_action="buttonAction",
                            link="link",
                            text="text",
                            text_color="textColor"
                        ),
                        ios=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        ),
                        web=pinpoint.CfnInAppTemplate.OverrideButtonConfigurationProperty(
                            button_action="buttonAction",
                            link="link"
                        )
                    )
                )],
                custom_config=custom_config,
                layout="layout",
                tags=tags,
                template_description="templateDescription"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e454773fb34afe57455c1ba518ee98492a81389b5fa127cd17273718dc8bcd1d)
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument custom_config", value=custom_config, expected_type=type_hints["custom_config"])
            check_type(argname="argument layout", value=layout, expected_type=type_hints["layout"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_description", value=template_description, expected_type=type_hints["template_description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_name": template_name,
        }
        if content is not None:
            self._values["content"] = content
        if custom_config is not None:
            self._values["custom_config"] = custom_config
        if layout is not None:
            self._values["layout"] = layout
        if tags is not None:
            self._values["tags"] = tags
        if template_description is not None:
            self._values["template_description"] = template_description

    @builtins.property
    def template_name(self) -> builtins.str:
        '''The name of the in-app message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-templatename
        '''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInAppTemplate.InAppMessageContentProperty]]]]:
        '''An object that contains information about the content of an in-app message, including its title and body text, text colors, background colors, images, buttons, and behaviors.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-content
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInAppTemplate.InAppMessageContentProperty]]]], result)

    @builtins.property
    def custom_config(self) -> typing.Any:
        '''Custom data, in the form of key-value pairs, that is included in an in-app messaging payload.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-customconfig
        '''
        result = self._values.get("custom_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def layout(self) -> typing.Optional[builtins.str]:
        '''A string that determines the appearance of the in-app message. You can specify one of the following:.

        - ``BOTTOM_BANNER`` – a message that appears as a banner at the bottom of the page.
        - ``TOP_BANNER`` – a message that appears as a banner at the top of the page.
        - ``OVERLAYS`` – a message that covers entire screen.
        - ``MOBILE_FEED`` – a message that appears in a window in front of the page.
        - ``MIDDLE_BANNER`` – a message that appears as a banner in the middle of the page.
        - ``CAROUSEL`` – a scrollable layout of up to five unique messages.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-layout
        '''
        result = self._values.get("layout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the in-app template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-templatedescription
        '''
        result = self._values.get("template_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInAppTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPushTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnPushTemplate",
):
    '''Creates a message template that you can use in messages that are sent through a push notification channel.

    A *message template* is a set of content and settings that you can define, save, and reuse in messages for any of your Amazon Pinpoint applications.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        # tags: Any
        
        cfn_push_template = pinpoint.CfnPushTemplate(self, "MyCfnPushTemplate",
            template_name="templateName",
        
            # the properties below are optional
            adm=pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty(
                action="action",
                body="body",
                image_icon_url="imageIconUrl",
                image_url="imageUrl",
                small_image_icon_url="smallImageIconUrl",
                sound="sound",
                title="title",
                url="url"
            ),
            apns=pinpoint.CfnPushTemplate.APNSPushNotificationTemplateProperty(
                action="action",
                body="body",
                media_url="mediaUrl",
                sound="sound",
                title="title",
                url="url"
            ),
            baidu=pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty(
                action="action",
                body="body",
                image_icon_url="imageIconUrl",
                image_url="imageUrl",
                small_image_icon_url="smallImageIconUrl",
                sound="sound",
                title="title",
                url="url"
            ),
            default=pinpoint.CfnPushTemplate.DefaultPushNotificationTemplateProperty(
                action="action",
                body="body",
                sound="sound",
                title="title",
                url="url"
            ),
            default_substitutions="defaultSubstitutions",
            gcm=pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty(
                action="action",
                body="body",
                image_icon_url="imageIconUrl",
                image_url="imageUrl",
                small_image_icon_url="smallImageIconUrl",
                sound="sound",
                title="title",
                url="url"
            ),
            tags=tags,
            template_description="templateDescription"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        template_name: builtins.str,
        adm: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPushTemplate.AndroidPushNotificationTemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        apns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPushTemplate.APNSPushNotificationTemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        baidu: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPushTemplate.AndroidPushNotificationTemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        default: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPushTemplate.DefaultPushNotificationTemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_substitutions: typing.Optional[builtins.str] = None,
        gcm: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPushTemplate.AndroidPushNotificationTemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param template_name: The name of the message template.
        :param adm: The message template to use for the ADM (Amazon Device Messaging) channel. This message template overrides the default template for push notification channels ( ``Default`` ).
        :param apns: The message template to use for the APNs (Apple Push Notification service) channel. This message template overrides the default template for push notification channels ( ``Default`` ).
        :param baidu: The message template to use for the Baidu (Baidu Cloud Push) channel. This message template overrides the default template for push notification channels ( ``Default`` ).
        :param default: The default message template to use for push notification channels.
        :param default_substitutions: A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.
        :param gcm: The message template to use for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message template overrides the default template for push notification channels ( ``Default`` ).
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_description: A custom description of the message template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c19924c3c4d187e6a4e597c337133470b5e94ec01287814b990418d143d50c8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPushTemplateProps(
            template_name=template_name,
            adm=adm,
            apns=apns,
            baidu=baidu,
            default=default,
            default_substitutions=default_substitutions,
            gcm=gcm,
            tags=tags,
            template_description=template_description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bd85bcc1afb08087adaf829b60ae72f7f789c00438280b47cfad3e4e8e188e7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0ea973d201048a1d85c8527dd218e3ea4ba36e582e42e4b36d47bb6c0addca0)
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
        '''The Amazon Resource Name (ARN) of the message template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> builtins.str:
        '''The name of the message template.'''
        return typing.cast(builtins.str, jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6689f4b17f3d51c97d046ff920f42167020ecdb954bcbb703df795aa48fd62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateName", value)

    @builtins.property
    @jsii.member(jsii_name="adm")
    def adm(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]]:
        '''The message template to use for the ADM (Amazon Device Messaging) channel.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]], jsii.get(self, "adm"))

    @adm.setter
    def adm(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32be5ab1563dc059696ad2e290c93a984c7450eb1d680d90dca0e7d42ea02fbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adm", value)

    @builtins.property
    @jsii.member(jsii_name="apns")
    def apns(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.APNSPushNotificationTemplateProperty"]]:
        '''The message template to use for the APNs (Apple Push Notification service) channel.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.APNSPushNotificationTemplateProperty"]], jsii.get(self, "apns"))

    @apns.setter
    def apns(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.APNSPushNotificationTemplateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77bf2e4b13ec2cfe475f08ed23562640cbcde98d9cb8138c3f3573cc417e532f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apns", value)

    @builtins.property
    @jsii.member(jsii_name="baidu")
    def baidu(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]]:
        '''The message template to use for the Baidu (Baidu Cloud Push) channel.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]], jsii.get(self, "baidu"))

    @baidu.setter
    def baidu(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dcb8053ca59ff9c0be19a4383b3295f95ada8ab1360a0c61f563aac118fc624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baidu", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.DefaultPushNotificationTemplateProperty"]]:
        '''The default message template to use for push notification channels.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.DefaultPushNotificationTemplateProperty"]], jsii.get(self, "default"))

    @default.setter
    def default(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.DefaultPushNotificationTemplateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c2576f9168b75160bea5859251791623f4dc1decc495cb1d53a55ff7a531800)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSubstitutions")
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''A JSON object that specifies the default values to use for message variables in the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubstitutions"))

    @default_substitutions.setter
    def default_substitutions(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a64a0af135c2c3f325587b4f9494bb2df541b2eb06fed9948a862f1c957678)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSubstitutions", value)

    @builtins.property
    @jsii.member(jsii_name="gcm")
    def gcm(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]]:
        '''The message template to use for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]], jsii.get(self, "gcm"))

    @gcm.setter
    def gcm(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__156c2a5b1c581871d4bbfb9adc0ebccc63555f7c7e7091b1772889dc981ccba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcm", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4cbceedb7f94ba5ae9fa8704dff30ab1f8d628748f0401c3a77272aace3cb98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateDescription")
    def template_description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDescription"))

    @template_description.setter
    def template_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbbbc4798da119c7d2ec902e6a1f2d7eb20ea88bc394a4e63a0a146c6f9b2327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateDescription", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnPushTemplate.APNSPushNotificationTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "body": "body",
            "media_url": "mediaUrl",
            "sound": "sound",
            "title": "title",
            "url": "url",
        },
    )
    class APNSPushNotificationTemplateProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            media_url: typing.Optional[builtins.str] = None,
            sound: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies channel-specific content and settings for a message template that can be used in push notifications that are sent through the APNs (Apple Push Notification service) channel.

            :param action: The action to occur if a recipient taps a push notification that's based on the message template. Valid values are: - ``OPEN_APP`` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. - ``DEEP_LINK`` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS platform. - ``URL`` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.
            :param body: The message body to use in push notifications that are based on the message template.
            :param media_url: The URL of an image or video to display in push notifications that are based on the message template.
            :param sound: The key for the sound to play when the recipient receives a push notification that's based on the message template. The value for this key is the name of a sound file in your app's main bundle or the ``Library/Sounds`` folder in your app's data container. If the sound file can't be found or you specify ``default`` for the value, the system plays the default alert sound.
            :param title: The title to use in push notifications that are based on the message template. This title appears above the notification message on a recipient's device.
            :param url: The URL to open in the recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the ``Action`` property is ``URL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                a_pNSPush_notification_template_property = pinpoint.CfnPushTemplate.APNSPushNotificationTemplateProperty(
                    action="action",
                    body="body",
                    media_url="mediaUrl",
                    sound="sound",
                    title="title",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1861c8949f9a6171d40596e1bf6cec657c1d8c3a46a998e615674ad5a63e714b)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument media_url", value=media_url, expected_type=type_hints["media_url"])
                check_type(argname="argument sound", value=sound, expected_type=type_hints["sound"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if body is not None:
                self._values["body"] = body
            if media_url is not None:
                self._values["media_url"] = media_url
            if sound is not None:
                self._values["sound"] = sound
            if title is not None:
                self._values["title"] = title
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The action to occur if a recipient taps a push notification that's based on the message template.

            Valid values are:

            - ``OPEN_APP`` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
            - ``DEEP_LINK`` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS platform.
            - ``URL`` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The message body to use in push notifications that are based on the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def media_url(self) -> typing.Optional[builtins.str]:
            '''The URL of an image or video to display in push notifications that are based on the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-mediaurl
            '''
            result = self._values.get("media_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sound(self) -> typing.Optional[builtins.str]:
            '''The key for the sound to play when the recipient receives a push notification that's based on the message template.

            The value for this key is the name of a sound file in your app's main bundle or the ``Library/Sounds`` folder in your app's data container. If the sound file can't be found or you specify ``default`` for the value, the system plays the default alert sound.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-sound
            '''
            result = self._values.get("sound")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''The title to use in push notifications that are based on the message template.

            This title appears above the notification message on a recipient's device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL to open in the recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the ``Action`` property is ``URL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "APNSPushNotificationTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "body": "body",
            "image_icon_url": "imageIconUrl",
            "image_url": "imageUrl",
            "small_image_icon_url": "smallImageIconUrl",
            "sound": "sound",
            "title": "title",
            "url": "url",
        },
    )
    class AndroidPushNotificationTemplateProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            image_icon_url: typing.Optional[builtins.str] = None,
            image_url: typing.Optional[builtins.str] = None,
            small_image_icon_url: typing.Optional[builtins.str] = None,
            sound: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies channel-specific content and settings for a message template that can be used in push notifications that are sent through the ADM (Amazon Device Messaging), Baidu (Baidu Cloud Push), or GCM (Firebase Cloud Messaging, formerly Google Cloud Messaging) channel.

            :param action: The action to occur if a recipient taps a push notification that's based on the message template. Valid values are: - ``OPEN_APP`` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. - ``DEEP_LINK`` – Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform. - ``URL`` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.
            :param body: The message body to use in a push notification that's based on the message template.
            :param image_icon_url: The URL of the large icon image to display in the content view of a push notification that's based on the message template.
            :param image_url: The URL of an image to display in a push notification that's based on the message template.
            :param small_image_icon_url: The URL of the small icon image to display in the status bar and the content view of a push notification that's based on the message template.
            :param sound: The sound to play when a recipient receives a push notification that's based on the message template. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in ``/res/raw/`` .
            :param title: The title to use in a push notification that's based on the message template. This title appears above the notification message on a recipient's device.
            :param url: The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the ``Action`` property is ``URL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                android_push_notification_template_property = pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_url="imageUrl",
                    small_image_icon_url="smallImageIconUrl",
                    sound="sound",
                    title="title",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f593b8352c58b9474c9c8b60e12209df9340663b07a166aaafa9f4361f9fc9c7)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument image_icon_url", value=image_icon_url, expected_type=type_hints["image_icon_url"])
                check_type(argname="argument image_url", value=image_url, expected_type=type_hints["image_url"])
                check_type(argname="argument small_image_icon_url", value=small_image_icon_url, expected_type=type_hints["small_image_icon_url"])
                check_type(argname="argument sound", value=sound, expected_type=type_hints["sound"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if body is not None:
                self._values["body"] = body
            if image_icon_url is not None:
                self._values["image_icon_url"] = image_icon_url
            if image_url is not None:
                self._values["image_url"] = image_url
            if small_image_icon_url is not None:
                self._values["small_image_icon_url"] = small_image_icon_url
            if sound is not None:
                self._values["sound"] = sound
            if title is not None:
                self._values["title"] = title
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The action to occur if a recipient taps a push notification that's based on the message template.

            Valid values are:

            - ``OPEN_APP`` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
            - ``DEEP_LINK`` – Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.
            - ``URL`` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The message body to use in a push notification that's based on the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_icon_url(self) -> typing.Optional[builtins.str]:
            '''The URL of the large icon image to display in the content view of a push notification that's based on the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageiconurl
            '''
            result = self._values.get("image_icon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_url(self) -> typing.Optional[builtins.str]:
            '''The URL of an image to display in a push notification that's based on the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageurl
            '''
            result = self._values.get("image_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def small_image_icon_url(self) -> typing.Optional[builtins.str]:
            '''The URL of the small icon image to display in the status bar and the content view of a push notification that's based on the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-smallimageiconurl
            '''
            result = self._values.get("small_image_icon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sound(self) -> typing.Optional[builtins.str]:
            '''The sound to play when a recipient receives a push notification that's based on the message template.

            You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in ``/res/raw/`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-sound
            '''
            result = self._values.get("sound")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''The title to use in a push notification that's based on the message template.

            This title appears above the notification message on a recipient's device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the ``Action`` property is ``URL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AndroidPushNotificationTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnPushTemplate.DefaultPushNotificationTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "body": "body",
            "sound": "sound",
            "title": "title",
            "url": "url",
        },
    )
    class DefaultPushNotificationTemplateProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            sound: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the default settings and content for a message template that can be used in messages that are sent through a push notification channel.

            :param action: The action to occur if a recipient taps a push notification that's based on the message template. Valid values are: - ``OPEN_APP`` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. - ``DEEP_LINK`` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS and Android platforms. - ``URL`` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.
            :param body: The message body to use in push notifications that are based on the message template.
            :param sound: The sound to play when a recipient receives a push notification that's based on the message template. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in ``/res/raw/`` . For an iOS platform, this value is the key for the name of a sound file in your app's main bundle or the ``Library/Sounds`` folder in your app's data container. If the sound file can't be found or you specify ``default`` for the value, the system plays the default alert sound.
            :param title: The title to use in push notifications that are based on the message template. This title appears above the notification message on a recipient's device.
            :param url: The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the ``Action`` property is ``URL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                default_push_notification_template_property = pinpoint.CfnPushTemplate.DefaultPushNotificationTemplateProperty(
                    action="action",
                    body="body",
                    sound="sound",
                    title="title",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f1a9fa0c7c3f0969aca855183fe31bb20a3232f7f68fca405d8416de89628dfb)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument sound", value=sound, expected_type=type_hints["sound"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if body is not None:
                self._values["body"] = body
            if sound is not None:
                self._values["sound"] = sound
            if title is not None:
                self._values["title"] = title
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The action to occur if a recipient taps a push notification that's based on the message template.

            Valid values are:

            - ``OPEN_APP`` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
            - ``DEEP_LINK`` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS and Android platforms.
            - ``URL`` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The message body to use in push notifications that are based on the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sound(self) -> typing.Optional[builtins.str]:
            '''The sound to play when a recipient receives a push notification that's based on the message template.

            You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in ``/res/raw/`` .

            For an iOS platform, this value is the key for the name of a sound file in your app's main bundle or the ``Library/Sounds`` folder in your app's data container. If the sound file can't be found or you specify ``default`` for the value, the system plays the default alert sound.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-sound
            '''
            result = self._values.get("sound")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''The title to use in push notifications that are based on the message template.

            This title appears above the notification message on a recipient's device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the ``Action`` property is ``URL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultPushNotificationTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnPushTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "template_name": "templateName",
        "adm": "adm",
        "apns": "apns",
        "baidu": "baidu",
        "default": "default",
        "default_substitutions": "defaultSubstitutions",
        "gcm": "gcm",
        "tags": "tags",
        "template_description": "templateDescription",
    },
)
class CfnPushTemplateProps:
    def __init__(
        self,
        *,
        template_name: builtins.str,
        adm: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        apns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.APNSPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        baidu: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        default: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.DefaultPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        default_substitutions: typing.Optional[builtins.str] = None,
        gcm: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPushTemplate``.

        :param template_name: The name of the message template.
        :param adm: The message template to use for the ADM (Amazon Device Messaging) channel. This message template overrides the default template for push notification channels ( ``Default`` ).
        :param apns: The message template to use for the APNs (Apple Push Notification service) channel. This message template overrides the default template for push notification channels ( ``Default`` ).
        :param baidu: The message template to use for the Baidu (Baidu Cloud Push) channel. This message template overrides the default template for push notification channels ( ``Default`` ).
        :param default: The default message template to use for push notification channels.
        :param default_substitutions: A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.
        :param gcm: The message template to use for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message template overrides the default template for push notification channels ( ``Default`` ).
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_description: A custom description of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            # tags: Any
            
            cfn_push_template_props = pinpoint.CfnPushTemplateProps(
                template_name="templateName",
            
                # the properties below are optional
                adm=pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_url="imageUrl",
                    small_image_icon_url="smallImageIconUrl",
                    sound="sound",
                    title="title",
                    url="url"
                ),
                apns=pinpoint.CfnPushTemplate.APNSPushNotificationTemplateProperty(
                    action="action",
                    body="body",
                    media_url="mediaUrl",
                    sound="sound",
                    title="title",
                    url="url"
                ),
                baidu=pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_url="imageUrl",
                    small_image_icon_url="smallImageIconUrl",
                    sound="sound",
                    title="title",
                    url="url"
                ),
                default=pinpoint.CfnPushTemplate.DefaultPushNotificationTemplateProperty(
                    action="action",
                    body="body",
                    sound="sound",
                    title="title",
                    url="url"
                ),
                default_substitutions="defaultSubstitutions",
                gcm=pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty(
                    action="action",
                    body="body",
                    image_icon_url="imageIconUrl",
                    image_url="imageUrl",
                    small_image_icon_url="smallImageIconUrl",
                    sound="sound",
                    title="title",
                    url="url"
                ),
                tags=tags,
                template_description="templateDescription"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd3a4d65d82add35f6d1294904a394ae2b9d9f09c6f0f78d8e25def5b4fa1b13)
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            check_type(argname="argument adm", value=adm, expected_type=type_hints["adm"])
            check_type(argname="argument apns", value=apns, expected_type=type_hints["apns"])
            check_type(argname="argument baidu", value=baidu, expected_type=type_hints["baidu"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument default_substitutions", value=default_substitutions, expected_type=type_hints["default_substitutions"])
            check_type(argname="argument gcm", value=gcm, expected_type=type_hints["gcm"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_description", value=template_description, expected_type=type_hints["template_description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_name": template_name,
        }
        if adm is not None:
            self._values["adm"] = adm
        if apns is not None:
            self._values["apns"] = apns
        if baidu is not None:
            self._values["baidu"] = baidu
        if default is not None:
            self._values["default"] = default
        if default_substitutions is not None:
            self._values["default_substitutions"] = default_substitutions
        if gcm is not None:
            self._values["gcm"] = gcm
        if tags is not None:
            self._values["tags"] = tags
        if template_description is not None:
            self._values["template_description"] = template_description

    @builtins.property
    def template_name(self) -> builtins.str:
        '''The name of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatename
        '''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def adm(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]]:
        '''The message template to use for the ADM (Amazon Device Messaging) channel.

        This message template overrides the default template for push notification channels ( ``Default`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-adm
        '''
        result = self._values.get("adm")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]], result)

    @builtins.property
    def apns(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.APNSPushNotificationTemplateProperty]]:
        '''The message template to use for the APNs (Apple Push Notification service) channel.

        This message template overrides the default template for push notification channels ( ``Default`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-apns
        '''
        result = self._values.get("apns")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.APNSPushNotificationTemplateProperty]], result)

    @builtins.property
    def baidu(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]]:
        '''The message template to use for the Baidu (Baidu Cloud Push) channel.

        This message template overrides the default template for push notification channels ( ``Default`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-baidu
        '''
        result = self._values.get("baidu")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]], result)

    @builtins.property
    def default(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.DefaultPushNotificationTemplateProperty]]:
        '''The default message template to use for push notification channels.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-default
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.DefaultPushNotificationTemplateProperty]], result)

    @builtins.property
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''A JSON object that specifies the default values to use for message variables in the message template.

        This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-defaultsubstitutions
        '''
        result = self._values.get("default_substitutions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcm(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]]:
        '''The message template to use for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service.

        This message template overrides the default template for push notification channels ( ``Default`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-gcm
        '''
        result = self._values.get("gcm")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatedescription
        '''
        result = self._values.get("template_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPushTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSMSChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnSMSChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    To send an SMS text message, you send the message through the SMS channel. Before you can use Amazon Pinpoint to send text messages, you have to enable the SMS channel for an Amazon Pinpoint application.

    The SMSChannel resource represents the status, sender ID, and other settings for the SMS channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_sMSChannel = pinpoint.CfnSMSChannel(self, "MyCfnSMSChannel",
            application_id="applicationId",
        
            # the properties below are optional
            enabled=False,
            sender_id="senderId",
            short_code="shortCode"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        sender_id: typing.Optional[builtins.str] = None,
        short_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that the SMS channel applies to.
        :param enabled: Specifies whether to enable the SMS channel for the application.
        :param sender_id: The identity that you want to display on recipients' devices when they receive messages from the SMS channel. .. epigraph:: SenderIDs are only supported in certain countries and regions. For more information, see `Supported Countries and Regions <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html>`_ in the *Amazon Pinpoint User Guide* .
        :param short_code: The registered short code that you want to use when you send messages through the SMS channel. .. epigraph:: For information about obtaining a dedicated short code for sending SMS messages, see `Requesting Dedicated Short Codes for SMS Messaging with Amazon Pinpoint <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-awssupport-short-code.html>`_ in the *Amazon Pinpoint User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b9e0e4cae717e114a852dc3bc4437c0b746385acea12e532445a77a378c9144)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSMSChannelProps(
            application_id=application_id,
            enabled=enabled,
            sender_id=sender_id,
            short_code=short_code,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__641cf7f9195aae9dae6d69036a20e83e49d7bc731fda0b737b4de53f5f30cea7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8af6ca2c0ec1dafc5e3f466617ea8759dcb8af2b029c793db0cddd445d4b3830)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the SMS channel applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e0414ce1e027ab6b5c67ee68d8a3766a8bfae21baef29b830c4881812533f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the SMS channel for the application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2854f045b9f30c7825e8267836e4fbe8206a1f421b757b06ed0b04dbb40c5a12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="senderId")
    def sender_id(self) -> typing.Optional[builtins.str]:
        '''The identity that you want to display on recipients' devices when they receive messages from the SMS channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "senderId"))

    @sender_id.setter
    def sender_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e23b829beec325729e74969ea029e8d36727faa2fed854351448b8dc2e86eec5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "senderId", value)

    @builtins.property
    @jsii.member(jsii_name="shortCode")
    def short_code(self) -> typing.Optional[builtins.str]:
        '''The registered short code that you want to use when you send messages through the SMS channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortCode"))

    @short_code.setter
    def short_code(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__581a443ec8905d7aa8644d9335605a1cb33151dcb443f96ded6410d3769aa4be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortCode", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnSMSChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "enabled": "enabled",
        "sender_id": "senderId",
        "short_code": "shortCode",
    },
)
class CfnSMSChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        sender_id: typing.Optional[builtins.str] = None,
        short_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSMSChannel``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that the SMS channel applies to.
        :param enabled: Specifies whether to enable the SMS channel for the application.
        :param sender_id: The identity that you want to display on recipients' devices when they receive messages from the SMS channel. .. epigraph:: SenderIDs are only supported in certain countries and regions. For more information, see `Supported Countries and Regions <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html>`_ in the *Amazon Pinpoint User Guide* .
        :param short_code: The registered short code that you want to use when you send messages through the SMS channel. .. epigraph:: For information about obtaining a dedicated short code for sending SMS messages, see `Requesting Dedicated Short Codes for SMS Messaging with Amazon Pinpoint <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-awssupport-short-code.html>`_ in the *Amazon Pinpoint User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_sMSChannel_props = pinpoint.CfnSMSChannelProps(
                application_id="applicationId",
            
                # the properties below are optional
                enabled=False,
                sender_id="senderId",
                short_code="shortCode"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d552897f1d5758cdf867f5379dff6344a4a7cebdd47142cd2fc361f08aca12a)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument sender_id", value=sender_id, expected_type=type_hints["sender_id"])
            check_type(argname="argument short_code", value=short_code, expected_type=type_hints["short_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if sender_id is not None:
            self._values["sender_id"] = sender_id
        if short_code is not None:
            self._values["short_code"] = short_code

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the SMS channel applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the SMS channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def sender_id(self) -> typing.Optional[builtins.str]:
        '''The identity that you want to display on recipients' devices when they receive messages from the SMS channel.

        .. epigraph::

           SenderIDs are only supported in certain countries and regions. For more information, see `Supported Countries and Regions <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html>`_ in the *Amazon Pinpoint User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-senderid
        '''
        result = self._values.get("sender_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def short_code(self) -> typing.Optional[builtins.str]:
        '''The registered short code that you want to use when you send messages through the SMS channel.

        .. epigraph::

           For information about obtaining a dedicated short code for sending SMS messages, see `Requesting Dedicated Short Codes for SMS Messaging with Amazon Pinpoint <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-awssupport-short-code.html>`_ in the *Amazon Pinpoint User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-shortcode
        '''
        result = self._values.get("short_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSMSChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSegment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment",
):
    '''Updates the configuration, dimension, and other settings for an existing segment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        # attributes: Any
        # metrics: Any
        # tags: Any
        # user_attributes: Any
        
        cfn_segment = pinpoint.CfnSegment(self, "MyCfnSegment",
            application_id="applicationId",
            name="name",
        
            # the properties below are optional
            dimensions=pinpoint.CfnSegment.SegmentDimensionsProperty(
                attributes=attributes,
                behavior=pinpoint.CfnSegment.BehaviorProperty(
                    recency=pinpoint.CfnSegment.RecencyProperty(
                        duration="duration",
                        recency_type="recencyType"
                    )
                ),
                demographic=pinpoint.CfnSegment.DemographicProperty(
                    app_version=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    channel=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    device_type=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    make=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    model=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    platform=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    )
                ),
                location=pinpoint.CfnSegment.LocationProperty(
                    country=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    gps_point=pinpoint.CfnSegment.GPSPointProperty(
                        coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                            latitude=123,
                            longitude=123
                        ),
                        range_in_kilometers=123
                    )
                ),
                metrics=metrics,
                user_attributes=user_attributes
            ),
            segment_groups=pinpoint.CfnSegment.SegmentGroupsProperty(
                groups=[pinpoint.CfnSegment.GroupsProperty(
                    dimensions=[pinpoint.CfnSegment.SegmentDimensionsProperty(
                        attributes=attributes,
                        behavior=pinpoint.CfnSegment.BehaviorProperty(
                            recency=pinpoint.CfnSegment.RecencyProperty(
                                duration="duration",
                                recency_type="recencyType"
                            )
                        ),
                        demographic=pinpoint.CfnSegment.DemographicProperty(
                            app_version=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            channel=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            device_type=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            make=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            model=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            platform=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            )
                        ),
                        location=pinpoint.CfnSegment.LocationProperty(
                            country=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            gps_point=pinpoint.CfnSegment.GPSPointProperty(
                                coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                                    latitude=123,
                                    longitude=123
                                ),
                                range_in_kilometers=123
                            )
                        ),
                        metrics=metrics,
                        user_attributes=user_attributes
                    )],
                    source_segments=[pinpoint.CfnSegment.SourceSegmentsProperty(
                        id="id",
        
                        # the properties below are optional
                        version=123
                    )],
                    source_type="sourceType",
                    type="type"
                )],
                include="include"
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        name: builtins.str,
        dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SegmentDimensionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        segment_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SegmentGroupsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that the segment is associated with.
        :param name: The name of the segment. .. epigraph:: A segment must have a name otherwise it will not appear in the Amazon Pinpoint console.
        :param dimensions: The criteria that define the dimensions for the segment.
        :param segment_groups: The segment group to use and the dimensions to apply to the group's base segments in order to build the segment. A segment group can consist of zero or more base segments. Your request can include only one segment group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f709a034a24c1bdbcf2c3ad69a8ec499d4a31c52228cfccf041a018ef8db5db6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSegmentProps(
            application_id=application_id,
            name=name,
            dimensions=dimensions,
            segment_groups=segment_groups,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab85436978fff9eb6b667bf369ce182d580e19493d318100b008eac7b205fad6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95ab46f3fcb3681e3b4d5ef5d055867767a26fd2eecb436628e106f3a21495b6)
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
        '''The Amazon Resource Name (ARN) of the segment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSegmentId")
    def attr_segment_id(self) -> builtins.str:
        '''The unique identifier for the segment.

        :cloudformationAttribute: SegmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentId"))

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the segment is associated with.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee563039c51ce7c946ee64d0544b6912c0e141d424096bcf6910faba0e279086)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the segment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e74415b4339bad69f40ae0cf82368a3aa0c5a21ee8d8ab9924fa39314e9dd645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SegmentDimensionsProperty"]]:
        '''The criteria that define the dimensions for the segment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SegmentDimensionsProperty"]], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SegmentDimensionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7596346842df00f96b4cdfdbd4c88e3d1ebd1006ff6eef96d986ad843c4fe2e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="segmentGroups")
    def segment_groups(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SegmentGroupsProperty"]]:
        '''The segment group to use and the dimensions to apply to the group's base segments in order to build the segment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SegmentGroupsProperty"]], jsii.get(self, "segmentGroups"))

    @segment_groups.setter
    def segment_groups(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SegmentGroupsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e5f8482204fc248f33a5d809b6fe0b1a60a440ed824a88a497c788578f74864)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segmentGroups", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19cf08f783ce7a107cff33dc3328d3098db5e5346e4d3f31d8f9929137028aa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.AttributeDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_type": "attributeType", "values": "values"},
    )
    class AttributeDimensionProperty:
        def __init__(
            self,
            *,
            attribute_type: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies attribute-based criteria for including or excluding endpoints from a segment.

            :param attribute_type: The type of segment dimension to use. Valid values are:. - ``INCLUSIVE`` – endpoints that have attributes matching the values are included in the segment. - ``EXCLUSIVE`` – endpoints that have attributes matching the values are excluded from the segment. - ``CONTAINS`` – endpoints that have attributes' substrings match the values are included in the segment. - ``BEFORE`` – endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment. - ``AFTER`` – endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment. - ``BETWEEN`` – endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment. - ``ON`` – endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
            :param values: The criteria values to use for the segment dimension. Depending on the value of the ``AttributeType`` property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                attribute_dimension_property = pinpoint.CfnSegment.AttributeDimensionProperty(
                    attribute_type="attributeType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d49995e4abe481142cc1c1660891bc0850ad1b99f1957bfacf77c4a80bdd90e2)
                check_type(argname="argument attribute_type", value=attribute_type, expected_type=type_hints["attribute_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attribute_type is not None:
                self._values["attribute_type"] = attribute_type
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def attribute_type(self) -> typing.Optional[builtins.str]:
            '''The type of segment dimension to use. Valid values are:.

            - ``INCLUSIVE`` – endpoints that have attributes matching the values are included in the segment.
            - ``EXCLUSIVE`` – endpoints that have attributes matching the values are excluded from the segment.
            - ``CONTAINS`` – endpoints that have attributes' substrings match the values are included in the segment.
            - ``BEFORE`` – endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
            - ``AFTER`` – endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
            - ``BETWEEN`` – endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.
            - ``ON`` – endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-attributetype
            '''
            result = self._values.get("attribute_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The criteria values to use for the segment dimension.

            Depending on the value of the ``AttributeType`` property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.BehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={"recency": "recency"},
    )
    class BehaviorProperty:
        def __init__(
            self,
            *,
            recency: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.RecencyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies behavior-based criteria for the segment, such as how recently users have used your app.

            :param recency: Specifies how recently segment members were active.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-behavior.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                behavior_property = pinpoint.CfnSegment.BehaviorProperty(
                    recency=pinpoint.CfnSegment.RecencyProperty(
                        duration="duration",
                        recency_type="recencyType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d797ad7bc3f43fe6b8489c7a02d2973f45c5c7e2f11b2576d335fe1b930e7a7)
                check_type(argname="argument recency", value=recency, expected_type=type_hints["recency"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if recency is not None:
                self._values["recency"] = recency

        @builtins.property
        def recency(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.RecencyProperty"]]:
            '''Specifies how recently segment members were active.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-behavior.html#cfn-pinpoint-segment-behavior-recency
            '''
            result = self._values.get("recency")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.RecencyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.CoordinatesProperty",
        jsii_struct_bases=[],
        name_mapping={"latitude": "latitude", "longitude": "longitude"},
    )
    class CoordinatesProperty:
        def __init__(self, *, latitude: jsii.Number, longitude: jsii.Number) -> None:
            '''Specifies the GPS coordinates of a location.

            :param latitude: The latitude coordinate of the location.
            :param longitude: The longitude coordinate of the location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-coordinates.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                coordinates_property = pinpoint.CfnSegment.CoordinatesProperty(
                    latitude=123,
                    longitude=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3879f4d4c4bc9d3ad9fd3c00fa3f25f1619888f2ef36dfb925dc53cea8ce12a)
                check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
                check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "latitude": latitude,
                "longitude": longitude,
            }

        @builtins.property
        def latitude(self) -> jsii.Number:
            '''The latitude coordinate of the location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-coordinates.html#cfn-pinpoint-segment-coordinates-latitude
            '''
            result = self._values.get("latitude")
            assert result is not None, "Required property 'latitude' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def longitude(self) -> jsii.Number:
            '''The longitude coordinate of the location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-coordinates.html#cfn-pinpoint-segment-coordinates-longitude
            '''
            result = self._values.get("longitude")
            assert result is not None, "Required property 'longitude' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoordinatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.DemographicProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_version": "appVersion",
            "channel": "channel",
            "device_type": "deviceType",
            "make": "make",
            "model": "model",
            "platform": "platform",
        },
    )
    class DemographicProperty:
        def __init__(
            self,
            *,
            app_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SetDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SetDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            device_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SetDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            make: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SetDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SetDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            platform: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SetDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies demographic-based criteria, such as device platform, for the segment.

            :param app_version: The app version criteria for the segment.
            :param channel: The channel criteria for the segment.
            :param device_type: The device type criteria for the segment.
            :param make: The device make criteria for the segment.
            :param model: The device model criteria for the segment.
            :param platform: The device platform criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-demographic.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                demographic_property = pinpoint.CfnSegment.DemographicProperty(
                    app_version=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    channel=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    device_type=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    make=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    model=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    platform=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df576e40323de6048cf308e0f8dda245dbb9d73c2f5a00bc7b66a74ab5ebe3bb)
                check_type(argname="argument app_version", value=app_version, expected_type=type_hints["app_version"])
                check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
                check_type(argname="argument device_type", value=device_type, expected_type=type_hints["device_type"])
                check_type(argname="argument make", value=make, expected_type=type_hints["make"])
                check_type(argname="argument model", value=model, expected_type=type_hints["model"])
                check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_version is not None:
                self._values["app_version"] = app_version
            if channel is not None:
                self._values["channel"] = channel
            if device_type is not None:
                self._values["device_type"] = device_type
            if make is not None:
                self._values["make"] = make
            if model is not None:
                self._values["model"] = model
            if platform is not None:
                self._values["platform"] = platform

        @builtins.property
        def app_version(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]]:
            '''The app version criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-demographic.html#cfn-pinpoint-segment-demographic-appversion
            '''
            result = self._values.get("app_version")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def channel(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]]:
            '''The channel criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-demographic.html#cfn-pinpoint-segment-demographic-channel
            '''
            result = self._values.get("channel")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def device_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]]:
            '''The device type criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-demographic.html#cfn-pinpoint-segment-demographic-devicetype
            '''
            result = self._values.get("device_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def make(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]]:
            '''The device make criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-demographic.html#cfn-pinpoint-segment-demographic-make
            '''
            result = self._values.get("make")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def model(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]]:
            '''The device model criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-demographic.html#cfn-pinpoint-segment-demographic-model
            '''
            result = self._values.get("model")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def platform(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]]:
            '''The device platform criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-demographic.html#cfn-pinpoint-segment-demographic-platform
            '''
            result = self._values.get("platform")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DemographicProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.GPSPointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "coordinates": "coordinates",
            "range_in_kilometers": "rangeInKilometers",
        },
    )
    class GPSPointProperty:
        def __init__(
            self,
            *,
            coordinates: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.CoordinatesProperty", typing.Dict[builtins.str, typing.Any]]],
            range_in_kilometers: jsii.Number,
        ) -> None:
            '''Specifies the GPS coordinates of the endpoint location.

            :param coordinates: The GPS coordinates to measure distance from.
            :param range_in_kilometers: The range, in kilometers, from the GPS coordinates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-gpspoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                g_pSPoint_property = pinpoint.CfnSegment.GPSPointProperty(
                    coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                        latitude=123,
                        longitude=123
                    ),
                    range_in_kilometers=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b3846c00f867e46d49f949447ce9f2d30f2fcdb206fa831c6d6ae0ce795c8bf)
                check_type(argname="argument coordinates", value=coordinates, expected_type=type_hints["coordinates"])
                check_type(argname="argument range_in_kilometers", value=range_in_kilometers, expected_type=type_hints["range_in_kilometers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "coordinates": coordinates,
                "range_in_kilometers": range_in_kilometers,
            }

        @builtins.property
        def coordinates(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnSegment.CoordinatesProperty"]:
            '''The GPS coordinates to measure distance from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-gpspoint.html#cfn-pinpoint-segment-gpspoint-coordinates
            '''
            result = self._values.get("coordinates")
            assert result is not None, "Required property 'coordinates' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSegment.CoordinatesProperty"], result)

        @builtins.property
        def range_in_kilometers(self) -> jsii.Number:
            '''The range, in kilometers, from the GPS coordinates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-gpspoint.html#cfn-pinpoint-segment-gpspoint-rangeinkilometers
            '''
            result = self._values.get("range_in_kilometers")
            assert result is not None, "Required property 'range_in_kilometers' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GPSPointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.GroupsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "source_segments": "sourceSegments",
            "source_type": "sourceType",
            "type": "type",
        },
    )
    class GroupsProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SegmentDimensionsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_segments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SourceSegmentsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_type: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An array that defines the set of segment criteria to evaluate when handling segment groups for the segment.

            :param dimensions: An array that defines the dimensions to include or exclude from the segment.
            :param source_segments: The base segment to build the segment on. A base segment, also called a *source segment* , defines the initial population of endpoints for a segment. When you add dimensions to the segment, Amazon Pinpoint filters the base segment by using the dimensions that you specify. You can specify more than one dimensional segment or only one imported segment. If you specify an imported segment, the segment size estimate that displays on the Amazon Pinpoint console indicates the size of the imported segment without any filters applied to it.
            :param source_type: Specifies how to handle multiple base segments for the segment. For example, if you specify three base segments for the segment, whether the resulting segment is based on all, any, or none of the base segments.
            :param type: Specifies how to handle multiple dimensions for the segment. For example, if you specify three dimensions for the segment, whether the resulting segment includes endpoints that match all, any, or none of the dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-groups.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # attributes: Any
                # metrics: Any
                # user_attributes: Any
                
                groups_property = pinpoint.CfnSegment.GroupsProperty(
                    dimensions=[pinpoint.CfnSegment.SegmentDimensionsProperty(
                        attributes=attributes,
                        behavior=pinpoint.CfnSegment.BehaviorProperty(
                            recency=pinpoint.CfnSegment.RecencyProperty(
                                duration="duration",
                                recency_type="recencyType"
                            )
                        ),
                        demographic=pinpoint.CfnSegment.DemographicProperty(
                            app_version=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            channel=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            device_type=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            make=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            model=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            platform=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            )
                        ),
                        location=pinpoint.CfnSegment.LocationProperty(
                            country=pinpoint.CfnSegment.SetDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            gps_point=pinpoint.CfnSegment.GPSPointProperty(
                                coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                                    latitude=123,
                                    longitude=123
                                ),
                                range_in_kilometers=123
                            )
                        ),
                        metrics=metrics,
                        user_attributes=user_attributes
                    )],
                    source_segments=[pinpoint.CfnSegment.SourceSegmentsProperty(
                        id="id",
                
                        # the properties below are optional
                        version=123
                    )],
                    source_type="sourceType",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__405e07d40b8c0ddf44ea93acd9dc1d8ffffac9f12f4e6664e60c86b7c263462b)
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument source_segments", value=source_segments, expected_type=type_hints["source_segments"])
                check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if source_segments is not None:
                self._values["source_segments"] = source_segments
            if source_type is not None:
                self._values["source_type"] = source_type
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegment.SegmentDimensionsProperty"]]]]:
            '''An array that defines the dimensions to include or exclude from the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-groups.html#cfn-pinpoint-segment-groups-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegment.SegmentDimensionsProperty"]]]], result)

        @builtins.property
        def source_segments(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegment.SourceSegmentsProperty"]]]]:
            '''The base segment to build the segment on.

            A base segment, also called a *source segment* , defines the initial population of endpoints for a segment. When you add dimensions to the segment, Amazon Pinpoint filters the base segment by using the dimensions that you specify.

            You can specify more than one dimensional segment or only one imported segment. If you specify an imported segment, the segment size estimate that displays on the Amazon Pinpoint console indicates the size of the imported segment without any filters applied to it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-groups.html#cfn-pinpoint-segment-groups-sourcesegments
            '''
            result = self._values.get("source_segments")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegment.SourceSegmentsProperty"]]]], result)

        @builtins.property
        def source_type(self) -> typing.Optional[builtins.str]:
            '''Specifies how to handle multiple base segments for the segment.

            For example, if you specify three base segments for the segment, whether the resulting segment is based on all, any, or none of the base segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-groups.html#cfn-pinpoint-segment-groups-sourcetype
            '''
            result = self._values.get("source_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''Specifies how to handle multiple dimensions for the segment.

            For example, if you specify three dimensions for the segment, whether the resulting segment includes endpoints that match all, any, or none of the dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-groups.html#cfn-pinpoint-segment-groups-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"country": "country", "gps_point": "gpsPoint"},
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            country: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.SetDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            gps_point: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.GPSPointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies location-based criteria, such as region or GPS coordinates, for the segment.

            :param country: The country or region code, in ISO 3166-1 alpha-2 format, for the segment.
            :param gps_point: The GPS point dimension for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                location_property = pinpoint.CfnSegment.LocationProperty(
                    country=pinpoint.CfnSegment.SetDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    gps_point=pinpoint.CfnSegment.GPSPointProperty(
                        coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                            latitude=123,
                            longitude=123
                        ),
                        range_in_kilometers=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__176f693f956da86315323388adcf262aadf7a6cdb3d859cf5c0bf58ec01ee91c)
                check_type(argname="argument country", value=country, expected_type=type_hints["country"])
                check_type(argname="argument gps_point", value=gps_point, expected_type=type_hints["gps_point"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if country is not None:
                self._values["country"] = country
            if gps_point is not None:
                self._values["gps_point"] = gps_point

        @builtins.property
        def country(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]]:
            '''The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-location.html#cfn-pinpoint-segment-location-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def gps_point(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.GPSPointProperty"]]:
            '''The GPS point dimension for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-location.html#cfn-pinpoint-segment-location-gpspoint
            '''
            result = self._values.get("gps_point")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.GPSPointProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.RecencyProperty",
        jsii_struct_bases=[],
        name_mapping={"duration": "duration", "recency_type": "recencyType"},
    )
    class RecencyProperty:
        def __init__(
            self,
            *,
            duration: builtins.str,
            recency_type: builtins.str,
        ) -> None:
            '''Specifies how recently segment members were active.

            :param duration: The duration to use when determining which users have been active or inactive with your app. Possible values: ``HR_24`` | ``DAY_7`` | ``DAY_14`` | ``DAY_30`` .
            :param recency_type: The type of recency dimension to use for the segment. Valid values are: ``ACTIVE`` and ``INACTIVE`` . If the value is ``ACTIVE`` , the segment includes users who have used your app within the specified duration are included in the segment. If the value is ``INACTIVE`` , the segment includes users who haven't used your app within the specified duration are included in the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-recency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                recency_property = pinpoint.CfnSegment.RecencyProperty(
                    duration="duration",
                    recency_type="recencyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__89a5e84535a2aa99d9b66489bc9e075515372707f29ea67a982953e313b5fe25)
                check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
                check_type(argname="argument recency_type", value=recency_type, expected_type=type_hints["recency_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "duration": duration,
                "recency_type": recency_type,
            }

        @builtins.property
        def duration(self) -> builtins.str:
            '''The duration to use when determining which users have been active or inactive with your app.

            Possible values: ``HR_24`` | ``DAY_7`` | ``DAY_14`` | ``DAY_30`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-recency.html#cfn-pinpoint-segment-recency-duration
            '''
            result = self._values.get("duration")
            assert result is not None, "Required property 'duration' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def recency_type(self) -> builtins.str:
            '''The type of recency dimension to use for the segment.

            Valid values are: ``ACTIVE`` and ``INACTIVE`` . If the value is ``ACTIVE`` , the segment includes users who have used your app within the specified duration are included in the segment. If the value is ``INACTIVE`` , the segment includes users who haven't used your app within the specified duration are included in the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-recency.html#cfn-pinpoint-segment-recency-recencytype
            '''
            result = self._values.get("recency_type")
            assert result is not None, "Required property 'recency_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.SegmentDimensionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attributes": "attributes",
            "behavior": "behavior",
            "demographic": "demographic",
            "location": "location",
            "metrics": "metrics",
            "user_attributes": "userAttributes",
        },
    )
    class SegmentDimensionsProperty:
        def __init__(
            self,
            *,
            attributes: typing.Any = None,
            behavior: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.BehaviorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            demographic: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.DemographicProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            metrics: typing.Any = None,
            user_attributes: typing.Any = None,
        ) -> None:
            '''Specifies the dimension settings for a segment.

            :param attributes: One or more custom attributes to use as criteria for the segment. For more information see `AttributeDimension <https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments.html#apps-application-id-segments-model-attributedimension>`_
            :param behavior: The behavior-based criteria, such as how recently users have used your app, for the segment.
            :param demographic: The demographic-based criteria, such as device platform, for the segment.
            :param location: The location-based criteria, such as region or GPS coordinates, for the segment.
            :param metrics: One or more custom metrics to use as criteria for the segment.
            :param user_attributes: One or more custom user attributes to use as criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # attributes: Any
                # metrics: Any
                # user_attributes: Any
                
                segment_dimensions_property = pinpoint.CfnSegment.SegmentDimensionsProperty(
                    attributes=attributes,
                    behavior=pinpoint.CfnSegment.BehaviorProperty(
                        recency=pinpoint.CfnSegment.RecencyProperty(
                            duration="duration",
                            recency_type="recencyType"
                        )
                    ),
                    demographic=pinpoint.CfnSegment.DemographicProperty(
                        app_version=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        channel=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        device_type=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        make=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        model=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        platform=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        )
                    ),
                    location=pinpoint.CfnSegment.LocationProperty(
                        country=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        gps_point=pinpoint.CfnSegment.GPSPointProperty(
                            coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                                latitude=123,
                                longitude=123
                            ),
                            range_in_kilometers=123
                        )
                    ),
                    metrics=metrics,
                    user_attributes=user_attributes
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__adeb504bbef1b7a7cd91e8fa51e7e9213f7c20d5c30f440671bd80b76c44bfc7)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
                check_type(argname="argument demographic", value=demographic, expected_type=type_hints["demographic"])
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
                check_type(argname="argument user_attributes", value=user_attributes, expected_type=type_hints["user_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if behavior is not None:
                self._values["behavior"] = behavior
            if demographic is not None:
                self._values["demographic"] = demographic
            if location is not None:
                self._values["location"] = location
            if metrics is not None:
                self._values["metrics"] = metrics
            if user_attributes is not None:
                self._values["user_attributes"] = user_attributes

        @builtins.property
        def attributes(self) -> typing.Any:
            '''One or more custom attributes to use as criteria for the segment.

            For more information see `AttributeDimension <https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments.html#apps-application-id-segments-model-attributedimension>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Any, result)

        @builtins.property
        def behavior(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.BehaviorProperty"]]:
            '''The behavior-based criteria, such as how recently users have used your app, for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-behavior
            '''
            result = self._values.get("behavior")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.BehaviorProperty"]], result)

        @builtins.property
        def demographic(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.DemographicProperty"]]:
            '''The demographic-based criteria, such as device platform, for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-demographic
            '''
            result = self._values.get("demographic")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.DemographicProperty"]], result)

        @builtins.property
        def location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.LocationProperty"]]:
            '''The location-based criteria, such as region or GPS coordinates, for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegment.LocationProperty"]], result)

        @builtins.property
        def metrics(self) -> typing.Any:
            '''One or more custom metrics to use as criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-metrics
            '''
            result = self._values.get("metrics")
            return typing.cast(typing.Any, result)

        @builtins.property
        def user_attributes(self) -> typing.Any:
            '''One or more custom user attributes to use as criteria for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-userattributes
            '''
            result = self._values.get("user_attributes")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentDimensionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.SegmentGroupsProperty",
        jsii_struct_bases=[],
        name_mapping={"groups": "groups", "include": "include"},
    )
    class SegmentGroupsProperty:
        def __init__(
            self,
            *,
            groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegment.GroupsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            include: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the set of segment criteria to evaluate when handling segment groups for the segment.

            :param groups: Specifies the set of segment criteria to evaluate when handling segment groups for the segment.
            :param include: Specifies how to handle multiple segment groups for the segment. For example, if the segment includes three segment groups, whether the resulting segment includes endpoints that match all, any, or none of the segment groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                # attributes: Any
                # metrics: Any
                # user_attributes: Any
                
                segment_groups_property = pinpoint.CfnSegment.SegmentGroupsProperty(
                    groups=[pinpoint.CfnSegment.GroupsProperty(
                        dimensions=[pinpoint.CfnSegment.SegmentDimensionsProperty(
                            attributes=attributes,
                            behavior=pinpoint.CfnSegment.BehaviorProperty(
                                recency=pinpoint.CfnSegment.RecencyProperty(
                                    duration="duration",
                                    recency_type="recencyType"
                                )
                            ),
                            demographic=pinpoint.CfnSegment.DemographicProperty(
                                app_version=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                channel=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                device_type=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                make=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                model=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                platform=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            ),
                            location=pinpoint.CfnSegment.LocationProperty(
                                country=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                gps_point=pinpoint.CfnSegment.GPSPointProperty(
                                    coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                                        latitude=123,
                                        longitude=123
                                    ),
                                    range_in_kilometers=123
                                )
                            ),
                            metrics=metrics,
                            user_attributes=user_attributes
                        )],
                        source_segments=[pinpoint.CfnSegment.SourceSegmentsProperty(
                            id="id",
                
                            # the properties below are optional
                            version=123
                        )],
                        source_type="sourceType",
                        type="type"
                    )],
                    include="include"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55b3b5cb3109787d3404864eb7762673d08dde2e0d43b66abe674298c9571b73)
                check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
                check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if groups is not None:
                self._values["groups"] = groups
            if include is not None:
                self._values["include"] = include

        @builtins.property
        def groups(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegment.GroupsProperty"]]]]:
            '''Specifies the set of segment criteria to evaluate when handling segment groups for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-groups
            '''
            result = self._values.get("groups")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegment.GroupsProperty"]]]], result)

        @builtins.property
        def include(self) -> typing.Optional[builtins.str]:
            '''Specifies how to handle multiple segment groups for the segment.

            For example, if the segment includes three segment groups, whether the resulting segment includes endpoints that match all, any, or none of the segment groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-include
            '''
            result = self._values.get("include")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentGroupsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.SetDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class SetDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the dimension type and values for a segment dimension.

            :param dimension_type: The type of segment dimension to use. Valid values are: ``INCLUSIVE`` , endpoints that match the criteria are included in the segment; and, ``EXCLUSIVE`` , endpoints that match the criteria are excluded from the segment.
            :param values: The criteria values to use for the segment dimension. Depending on the value of the ``DimensionType`` property, endpoints are included or excluded from the segment if their values match the criteria values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                set_dimension_property = pinpoint.CfnSegment.SetDimensionProperty(
                    dimension_type="dimensionType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__39b0c4354cc8075763f75e56a57757addd2fe34b15dd9c9b4a9b7998d437d5bb)
                check_type(argname="argument dimension_type", value=dimension_type, expected_type=type_hints["dimension_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimension_type is not None:
                self._values["dimension_type"] = dimension_type
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def dimension_type(self) -> typing.Optional[builtins.str]:
            '''The type of segment dimension to use.

            Valid values are: ``INCLUSIVE`` , endpoints that match the criteria are included in the segment; and, ``EXCLUSIVE`` , endpoints that match the criteria are excluded from the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The criteria values to use for the segment dimension.

            Depending on the value of the ``DimensionType`` property, endpoints are included or excluded from the segment if their values match the criteria values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SetDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegment.SourceSegmentsProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "version": "version"},
    )
    class SourceSegmentsProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            version: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the base segment to build the segment on.

            A base segment, also called a *source segment* , defines the initial population of endpoints for a segment. When you add dimensions to the segment, Amazon Pinpoint filters the base segment by using the dimensions that you specify.

            You can specify more than one dimensional segment or only one imported segment. If you specify an imported segment, the segment size estimate that displays on the Amazon Pinpoint console indicates the size of the imported segment without any filters applied to it.

            :param id: The unique identifier for the source segment.
            :param version: The version number of the source segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-sourcesegments.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpoint as pinpoint
                
                source_segments_property = pinpoint.CfnSegment.SourceSegmentsProperty(
                    id="id",
                
                    # the properties below are optional
                    version=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__388da4420307c3fdf7dde8a1d10d0e8cc8d6c962e3fadadd9fae09d96077589e)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def id(self) -> builtins.str:
            '''The unique identifier for the source segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-sourcesegments.html#cfn-pinpoint-segment-sourcesegments-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[jsii.Number]:
            '''The version number of the source segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-sourcesegments.html#cfn-pinpoint-segment-sourcesegments-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceSegmentsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnSegmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "name": "name",
        "dimensions": "dimensions",
        "segment_groups": "segmentGroups",
        "tags": "tags",
    },
)
class CfnSegmentProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        name: builtins.str,
        dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SegmentDimensionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        segment_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SegmentGroupsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnSegment``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that the segment is associated with.
        :param name: The name of the segment. .. epigraph:: A segment must have a name otherwise it will not appear in the Amazon Pinpoint console.
        :param dimensions: The criteria that define the dimensions for the segment.
        :param segment_groups: The segment group to use and the dimensions to apply to the group's base segments in order to build the segment. A segment group can consist of zero or more base segments. Your request can include only one segment group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            # attributes: Any
            # metrics: Any
            # tags: Any
            # user_attributes: Any
            
            cfn_segment_props = pinpoint.CfnSegmentProps(
                application_id="applicationId",
                name="name",
            
                # the properties below are optional
                dimensions=pinpoint.CfnSegment.SegmentDimensionsProperty(
                    attributes=attributes,
                    behavior=pinpoint.CfnSegment.BehaviorProperty(
                        recency=pinpoint.CfnSegment.RecencyProperty(
                            duration="duration",
                            recency_type="recencyType"
                        )
                    ),
                    demographic=pinpoint.CfnSegment.DemographicProperty(
                        app_version=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        channel=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        device_type=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        make=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        model=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        platform=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        )
                    ),
                    location=pinpoint.CfnSegment.LocationProperty(
                        country=pinpoint.CfnSegment.SetDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        gps_point=pinpoint.CfnSegment.GPSPointProperty(
                            coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                                latitude=123,
                                longitude=123
                            ),
                            range_in_kilometers=123
                        )
                    ),
                    metrics=metrics,
                    user_attributes=user_attributes
                ),
                segment_groups=pinpoint.CfnSegment.SegmentGroupsProperty(
                    groups=[pinpoint.CfnSegment.GroupsProperty(
                        dimensions=[pinpoint.CfnSegment.SegmentDimensionsProperty(
                            attributes=attributes,
                            behavior=pinpoint.CfnSegment.BehaviorProperty(
                                recency=pinpoint.CfnSegment.RecencyProperty(
                                    duration="duration",
                                    recency_type="recencyType"
                                )
                            ),
                            demographic=pinpoint.CfnSegment.DemographicProperty(
                                app_version=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                channel=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                device_type=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                make=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                model=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                platform=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            ),
                            location=pinpoint.CfnSegment.LocationProperty(
                                country=pinpoint.CfnSegment.SetDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                gps_point=pinpoint.CfnSegment.GPSPointProperty(
                                    coordinates=pinpoint.CfnSegment.CoordinatesProperty(
                                        latitude=123,
                                        longitude=123
                                    ),
                                    range_in_kilometers=123
                                )
                            ),
                            metrics=metrics,
                            user_attributes=user_attributes
                        )],
                        source_segments=[pinpoint.CfnSegment.SourceSegmentsProperty(
                            id="id",
            
                            # the properties below are optional
                            version=123
                        )],
                        source_type="sourceType",
                        type="type"
                    )],
                    include="include"
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25f43b43d50881dc0b12d0713cceab9df4a33654c37f0f4032f99c402541ca95)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument segment_groups", value=segment_groups, expected_type=type_hints["segment_groups"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "name": name,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if segment_groups is not None:
            self._values["segment_groups"] = segment_groups
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the segment is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the segment.

        .. epigraph::

           A segment must have a name otherwise it will not appear in the Amazon Pinpoint console.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSegment.SegmentDimensionsProperty]]:
        '''The criteria that define the dimensions for the segment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSegment.SegmentDimensionsProperty]], result)

    @builtins.property
    def segment_groups(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSegment.SegmentGroupsProperty]]:
        '''The segment group to use and the dimensions to apply to the group's base segments in order to build the segment.

        A segment group can consist of zero or more base segments. Your request can include only one segment group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-segmentgroups
        '''
        result = self._values.get("segment_groups")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSegment.SegmentGroupsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSegmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSmsTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnSmsTemplate",
):
    '''Creates a message template that you can use in messages that are sent through the SMS channel.

    A *message template* is a set of content and settings that you can define, save, and reuse in messages for any of your Amazon Pinpoint applications.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        # tags: Any
        
        cfn_sms_template = pinpoint.CfnSmsTemplate(self, "MyCfnSmsTemplate",
            body="body",
            template_name="templateName",
        
            # the properties below are optional
            default_substitutions="defaultSubstitutions",
            tags=tags,
            template_description="templateDescription"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        body: builtins.str,
        template_name: builtins.str,
        default_substitutions: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param body: The message body to use in text messages that are based on the message template.
        :param template_name: The name of the message template.
        :param default_substitutions: A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_description: A custom description of the message template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1536fb6b841b2ae28085a22bbac5257230add94dcddd63c390ad3d6941c1bdbc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSmsTemplateProps(
            body=body,
            template_name=template_name,
            default_substitutions=default_substitutions,
            tags=tags,
            template_description=template_description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__284689e5f66f12908f35f21c7be81438110fcbe4de00b5e612fe3c4938da9b7d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a6f692351821c040a7e25e23778d74d6c709b84a9830d9e3895692d6e33126e)
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
        '''The Amazon Resource Name (ARN) of the message template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        '''The message body to use in text messages that are based on the message template.'''
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84ff9f4a2706bc6d280232f48449544baf035de043a7edd477c36b49a770d660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> builtins.str:
        '''The name of the message template.'''
        return typing.cast(builtins.str, jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68a2e9c56e1723b59d90c1859572868534e794fb2dfb13f93bee7d09edcc1a16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSubstitutions")
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''A JSON object that specifies the default values to use for message variables in the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubstitutions"))

    @default_substitutions.setter
    def default_substitutions(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a6ff98aa698d81509091ca1cf004f062a6bbff5ac1491a78ba87aa2bc032f69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSubstitutions", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10b1b81307b1076556a881c595d43cb014a04a4bd2d3218f10021904adb69043)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateDescription")
    def template_description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDescription"))

    @template_description.setter
    def template_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd3fa157e9a3304bccf83ba2950a06e1182c1194aca31c385f8914954dcfd3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateDescription", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnSmsTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "body": "body",
        "template_name": "templateName",
        "default_substitutions": "defaultSubstitutions",
        "tags": "tags",
        "template_description": "templateDescription",
    },
)
class CfnSmsTemplateProps:
    def __init__(
        self,
        *,
        body: builtins.str,
        template_name: builtins.str,
        default_substitutions: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSmsTemplate``.

        :param body: The message body to use in text messages that are based on the message template.
        :param template_name: The name of the message template.
        :param default_substitutions: A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param template_description: A custom description of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            # tags: Any
            
            cfn_sms_template_props = pinpoint.CfnSmsTemplateProps(
                body="body",
                template_name="templateName",
            
                # the properties below are optional
                default_substitutions="defaultSubstitutions",
                tags=tags,
                template_description="templateDescription"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__423db93371632488090f99bb5f94b3d74c4b49c176f644adb2f9a9b89eb1ec23)
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            check_type(argname="argument default_substitutions", value=default_substitutions, expected_type=type_hints["default_substitutions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_description", value=template_description, expected_type=type_hints["template_description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "body": body,
            "template_name": template_name,
        }
        if default_substitutions is not None:
            self._values["default_substitutions"] = default_substitutions
        if tags is not None:
            self._values["tags"] = tags
        if template_description is not None:
            self._values["template_description"] = template_description

    @builtins.property
    def body(self) -> builtins.str:
        '''The message body to use in text messages that are based on the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-body
        '''
        result = self._values.get("body")
        assert result is not None, "Required property 'body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_name(self) -> builtins.str:
        '''The name of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatename
        '''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''A JSON object that specifies the default values to use for message variables in the message template.

        This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-defaultsubstitutions
        '''
        result = self._values.get("default_substitutions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatedescription
        '''
        result = self._values.get("template_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSmsTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnVoiceChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnVoiceChannel",
):
    '''A *channel* is a type of platform that you can deliver messages to.

    To send a voice message, you send the message through the voice channel. Before you can use Amazon Pinpoint to send voice messages, you have to enable the voice channel for an Amazon Pinpoint application.

    The VoiceChannel resource represents the status and other information about the voice channel for an application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpoint as pinpoint
        
        cfn_voice_channel = pinpoint.CfnVoiceChannel(self, "MyCfnVoiceChannel",
            application_id="applicationId",
        
            # the properties below are optional
            enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The unique identifier for the Amazon Pinpoint application that the voice channel applies to.
        :param enabled: Specifies whether to enable the voice channel for the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eefa81940d32d619367bdcf45d70859abb04ed0a3acb03e963889c077b6a175)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVoiceChannelProps(application_id=application_id, enabled=enabled)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcfd177d8879192e1452736feddc938b4633ce829ab6b202a0f20e96fa0d1c4c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__36815d159fd7f8a16a1c1f294ec64660877a873116a1ebc133b345c3c735adf5)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the voice channel applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d66b91fe903bebc80d5aa290f53e57858be37231f0b2b67a3792364acd72e44a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the voice channel for the application.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55f9072e4ea10db6545a901f75a87f0db23d51ed4c12907c8203b488bc5d23b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpoint.CfnVoiceChannelProps",
    jsii_struct_bases=[],
    name_mapping={"application_id": "applicationId", "enabled": "enabled"},
)
class CfnVoiceChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVoiceChannel``.

        :param application_id: The unique identifier for the Amazon Pinpoint application that the voice channel applies to.
        :param enabled: Specifies whether to enable the voice channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpoint as pinpoint
            
            cfn_voice_channel_props = pinpoint.CfnVoiceChannelProps(
                application_id="applicationId",
            
                # the properties below are optional
                enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf39a3de9821d1b054616d0b2e269d51093b75f3abc30724908da5749e0280bf)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier for the Amazon Pinpoint application that the voice channel applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to enable the voice channel for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVoiceChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnADMChannel",
    "CfnADMChannelProps",
    "CfnAPNSChannel",
    "CfnAPNSChannelProps",
    "CfnAPNSSandboxChannel",
    "CfnAPNSSandboxChannelProps",
    "CfnAPNSVoipChannel",
    "CfnAPNSVoipChannelProps",
    "CfnAPNSVoipSandboxChannel",
    "CfnAPNSVoipSandboxChannelProps",
    "CfnApp",
    "CfnAppProps",
    "CfnApplicationSettings",
    "CfnApplicationSettingsProps",
    "CfnBaiduChannel",
    "CfnBaiduChannelProps",
    "CfnCampaign",
    "CfnCampaignProps",
    "CfnEmailChannel",
    "CfnEmailChannelProps",
    "CfnEmailTemplate",
    "CfnEmailTemplateProps",
    "CfnEventStream",
    "CfnEventStreamProps",
    "CfnGCMChannel",
    "CfnGCMChannelProps",
    "CfnInAppTemplate",
    "CfnInAppTemplateProps",
    "CfnPushTemplate",
    "CfnPushTemplateProps",
    "CfnSMSChannel",
    "CfnSMSChannelProps",
    "CfnSegment",
    "CfnSegmentProps",
    "CfnSmsTemplate",
    "CfnSmsTemplateProps",
    "CfnVoiceChannel",
    "CfnVoiceChannelProps",
]

publication.publish()

def _typecheckingstub__aaf704e00bb5859cb830fbb4d1e376040266671aa90e04a47641d8d055085dae(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    client_id: builtins.str,
    client_secret: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6370d32f16b93db7c704589cdcc432969bf4bb7eecdf1c1ecce61abeb6703b1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7f38c58309e10d9e9c3e9cdd18ecdf0206a62dafe257a225fce81498a09d52(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__516a9ba4b7757af253ff004793a1979569edace2e0341aecf95d98ab8878fb7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ca2b0ebc55a347f1c856351a7ea66aa33f15336b7c29ebd44c657ad1e32c50f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43ceab49423ae46becea7c2f42867ef5034b7107d6f0e0def0f82103c810cba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f9495da313043ed76a0fcbe057cba0bc82dd16c11f653c0c4ce29add3f3d6a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ae5a29f3b4adfec5b1c827ee1bea8d33d99e697476ac7b7f9b8fea86b0bfc8(
    *,
    application_id: builtins.str,
    client_id: builtins.str,
    client_secret: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c6d01d6ac4514b60aaeb636fa32c4f2935eb954acb47fe1f335948796c5b38(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    bundle_id: typing.Optional[builtins.str] = None,
    certificate: typing.Optional[builtins.str] = None,
    default_authentication_method: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    private_key: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    token_key: typing.Optional[builtins.str] = None,
    token_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ef2edffbfaec89f01e614ae0d36665094bca9d2873273de72ca37709500647(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd87eeeb0b6f658fbf73ac4ee0a5ce23911fd99d4342fd6e60ca8b210fdb972(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec692a61d1b998fa192954294bd412c7117bc611c68ba50855c6b11be36d360(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fdc4ba23303245bc510c4bc0780d997ced5645298a9309ce4a0b668e50b681f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b2b358bd8e58ccda4eaae0530a3da766174cc23bb14dcbe422279e23ffc7c5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3201f885e965d3cbc3fd27f17ec2f46000a5ba9bfe7044238c7ddcab8c78d33a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed3ad95420b6948df7339f9eb6816bcaed443dfcee74ef7485882c3fc6c9be2(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32129c9e89fe5fb120406d63eb937f83ada047a3a02266a6a4b77dd025f761d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126052989c39a52610fc6e54340c3dfe4273d45aa56b9ee0096604832a8af83f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c68905895fc14733013b7072172056341167e4e6fbde6cccac5d4da6a970a70(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e111ff96fa2864617af9bc1196e6a5c0f42a455a826bc67955c67c9e02a60ff0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68cad147d39b410bb9ad20221185a1521986df7fc3b2870715568b76969e443f(
    *,
    application_id: builtins.str,
    bundle_id: typing.Optional[builtins.str] = None,
    certificate: typing.Optional[builtins.str] = None,
    default_authentication_method: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    private_key: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    token_key: typing.Optional[builtins.str] = None,
    token_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2cdf1bd0828fb196281b0c6e09fb772d25d46b1f609996c702cd33ded3923dc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    bundle_id: typing.Optional[builtins.str] = None,
    certificate: typing.Optional[builtins.str] = None,
    default_authentication_method: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    private_key: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    token_key: typing.Optional[builtins.str] = None,
    token_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9afd220964f59a3aa7c276349cbfbe0194a39fc3cc38e67756b3372dc695d32(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63e4d9ee78998839059ebfdb4c7eec999776002f59a110424dcbdbbf354898ec(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e3a391d32b5c7c832ea76d26b3ce0f36d370d03206b1ef42defc87b6ecd1656(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c13e391d9c40b56efef97e70420259e3f16f091119a589e3cb14cde7fbcffb5b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d929856dc7781e860f17aa023d8a01e0cb7f1ec7cb93f928f78a77e4c76991a3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72936dce4a9d9b3355d20141e15f0e706016979a3653c66d8027d3c7b0ee03d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4666c0e59b9ee82106f0a8a6fe42b502df677f3d4e454cc2c1d8a8c3dc1e8d9(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348e545ce1c804626ae2b2b83b8cccbc3635d89315ef72cfc11baf2cad881c10(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b8fd4f8d072de699b28339406a81391b189fddec1b0bbd68f9faec4d296b070(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622ff057d2fa4cb1f10160e466a9f238a6f82b2da34b6a446ac4789934351392(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a1c83d822fd7f724c76e48f4fadc86e26cedf4936d86d6a2d5600e9949b8e2c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3609ffaa3fba04e4ff88045f06f94408c36907fca82875dc1aab7ae3cba1f30a(
    *,
    application_id: builtins.str,
    bundle_id: typing.Optional[builtins.str] = None,
    certificate: typing.Optional[builtins.str] = None,
    default_authentication_method: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    private_key: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    token_key: typing.Optional[builtins.str] = None,
    token_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__354fbb51dc05a5c7b142870475ffebba049d56e406e383a83bcdf9e1205f7e3a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    bundle_id: typing.Optional[builtins.str] = None,
    certificate: typing.Optional[builtins.str] = None,
    default_authentication_method: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    private_key: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    token_key: typing.Optional[builtins.str] = None,
    token_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c295e4c7ef221f73636feb125bd7e1fe6267e5dbbe723147da0cdae19845d8e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04703119f79d8184e97b28f75a030ff15aca233258d881aa000b618281a64d0d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d8cf83888d2c3bcb29e553a924bf2bb2b5423243bfd76ff45039cec94c4203f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ef79ce48a4708565800ada7142b5f84f70dba36f6631fea19ceabe5dae7c09(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d72c80d8e62631c30f10c530f1e875432ad32c73b6aeba9bb7bb054e1c4fa878(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c7e303ad6e775381a9141f9cfef12089fa928c85c8a8b45394b4a0670e83e4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29971c6564c0a97fcd5481816c5791d2527814f70f07c3dc75b5bdd5f178679(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52ffc29c2e58a29c36ceeb81a921d67080e931e597c389630a2a8b8bb4605bf7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5795637c70bd87670d111ed19a94136ea8689882020ecd1f2b3a9ca1dc588adc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a763a314ff762c118e43a2503d59c9db34d817fcbe98b899a2695c1da28a6cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46127dd7405f371138f3f8925f703cbdf74dc4d1920b57b2c4046a9f4c8678c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2515eaa7a5b0f17c9115c41e25d7466476c5fc2356786c269e03db415b0b6a0(
    *,
    application_id: builtins.str,
    bundle_id: typing.Optional[builtins.str] = None,
    certificate: typing.Optional[builtins.str] = None,
    default_authentication_method: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    private_key: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    token_key: typing.Optional[builtins.str] = None,
    token_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda00a8216a1537d1791cebffe3e648359ad880fd824bfd90472a552cf2f17a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    bundle_id: typing.Optional[builtins.str] = None,
    certificate: typing.Optional[builtins.str] = None,
    default_authentication_method: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    private_key: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    token_key: typing.Optional[builtins.str] = None,
    token_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b73a7955f3c2112f01b23293d78c4a55e7bf14ae478719955fa7bbf05e013cba(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22adf58a327644519c6703d2838a632c1d54b15bced0304f64e2c1f588f54bcf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350373fee7f7d95897dd93a64ed1fba8e5c7633cc24c346e6eae6f6f8022ca85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adacd8b3feedf89d701eb54dc830cd89599763f610af1ab0ddae724bd2b9ab9e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186164a38f8208bb7b7f4347d8ffc572fd4d74da65ed43f189482ccb05e0b9e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f546750c5bd78ff62a69bbe58c6bd21bab499a931542106097f2be0e61b0738(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac5c1ce5cc72d2472a9881976d507f68a31b18a54d9853cc07d5e5f47c1f566(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c7912f617707f8a3bf055962376421068d396c4548da62240dea44b4d840a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b56d6aec3a3108d8b2afad8a6b2db8101173ab0c6faa42c50e79e0ad96fb3a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f79c9d0b861c37cd183ab0b80d916731b90ace98ab3e741d2de7cddce91497c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd15602c1b7a8a7fe5ed82c46d42d3b30e6bc52c8618e996139c2d1c461696f4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c73c61658383943c9f8d75c0d3353564c42bbc4ebb21db0dbb12fd8e993b5ea4(
    *,
    application_id: builtins.str,
    bundle_id: typing.Optional[builtins.str] = None,
    certificate: typing.Optional[builtins.str] = None,
    default_authentication_method: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    private_key: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    token_key: typing.Optional[builtins.str] = None,
    token_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0f8bd367843c451288aaaaf44baa44f09abffc0daba385520088889fd81e23(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a1a0b3dc0d592b65e802e1e0b8f6d8ec8f0dc7df60bf7d1633880668ff742e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e034d00b2f813e571c292acc2ff9b22e3caa8f934e8935b27235f80a809b8c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cda5c7fde34ff297b3dd15ab1185cf7a20ee1de5b1dbc01014c4cdbc7628bfb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e084f2f5a25d396c8ccb2664d39e210e8baca99dd9f5b729df463e35b2565c3(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5ece6d9985e2c12212269fba01e0f60516e87697766368b6a5343813fba618c(
    *,
    name: builtins.str,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fccaf1bda545922f59167d307e79647dd7b5a9bdb6a0d209e2ca4103d5382dec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    campaign_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.CampaignHookProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.LimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    quiet_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.QuietTimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf14b6ff8c636cd9737f33917ef781db4b0cad7f678d53682c3daae1564d0f1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab86b68966b26e641e0dc1136bda485826e3978c2c9073ea008e6b1ec19b32d2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77178b3d447e29013b551ae5835b06acbc057abc44ff6d0ef62fba4da67d443(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5230c9c3bb4cc93dbcaf0c5e212a80abd53a33c7588270b53fc93dae0c27d139(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.CampaignHookProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__755097f5bd91236a9086d9ae0fa2948236768a3b8aa298efa8cb0b079e4f3406(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__160a20b435f7b6094f46c527888adf81437d233b9f3372717ff3235293b3cb53(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.LimitsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c87df35c4674de93532f2b097e8a5e8acc739757c089b203b35e483e743d6a56(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationSettings.QuietTimeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3735fe29377ea2a62d3732e899a51c8a9e72347e64f199653047cab6f9d9506e(
    *,
    lambda_function_name: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    web_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b567fc1a36320c43d98124a1a42b18b1cf5865a4a20180bd858cfdbdddb76c0(
    *,
    daily: typing.Optional[jsii.Number] = None,
    maximum_duration: typing.Optional[jsii.Number] = None,
    messages_per_second: typing.Optional[jsii.Number] = None,
    total: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f1c3eef4ae7697239fc1a13ba90492d492b7d5021e1b6b4bbdda3168071fee(
    *,
    end: builtins.str,
    start: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__848467a4d3edb707abe4565a3db11fcd50755d6c664897537827d7e2003fb02d(
    *,
    application_id: builtins.str,
    campaign_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.CampaignHookProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.LimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    quiet_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationSettings.QuietTimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a51d70a760e3a97ac0ecff0ea42b251dacb1982201c515754052b0924b8e68(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_key: builtins.str,
    application_id: builtins.str,
    secret_key: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d887fd5e4f274a7c9f9fb685c04f9829ef3a76fa07377a74cc728de290ff58b5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3559f4e7df7dcb2b8e21ae2606a6d30ab6d91b28c6e5d05bcd80f01ac1b85bc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d55ab74c3304a8f7ee5eb7755db2b7575dede417448da381789b65757a6e26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdcdb9cb03617bf41a449212c19519749eeb4eac75fa6316b5c70055f4067c20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__985764c1478c22f92314f563a4e1501861497b260954b0683c149c92a0325375(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322e2fecb20c91419f0797aeaab2607597e674c854ce690ae78042ae1dd3e42f(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea99679b99d64e9a67176579da7115a89002eb9da18df44b574208277637df1c(
    *,
    api_key: builtins.str,
    application_id: builtins.str,
    secret_key: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37daefd9aecddac1551b6da8a771d74af1f7a13678f1d1fb2d351fab8d081055(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    name: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    segment_id: builtins.str,
    additional_treatments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.WriteTreatmentResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    campaign_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CampaignHookProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_delivery_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CustomDeliveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    holdout_percent: typing.Optional[jsii.Number] = None,
    is_paused: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.LimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    message_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    priority: typing.Optional[jsii.Number] = None,
    segment_version: typing.Optional[jsii.Number] = None,
    tags: typing.Any = None,
    template_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    treatment_description: typing.Optional[builtins.str] = None,
    treatment_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e15e4e500736a6e94e0b0439baae0e844c072ad04e21f846e6d90b4d664758f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59807fa6d089ddbb2e1a05b1cd16f356100de47cbb6921352a89adfb25cf0cc2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__961093a0b2a649a27da7667fd113667242f9d38dc807ec0c0d27a031ef4583b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f60f9e8c94473fc78021759e41a1198fa36a2907ab9bbaabe3369a50277e2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2181cc1c01db963e61293d6df1af9886ac4eab655deaf6a0e57d1e205e3475d(
    value: typing.Union[_IResolvable_da3f097b, CfnCampaign.ScheduleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785cdfc13b1f0cf0280965fcfdcb49bb03ad6603227a7fafd5b6f82cd1655f22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb8abceb723e5d996583338abd7b9da817cebc58734650cbcd416e12f060c3e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.WriteTreatmentResourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cff8453460fff6b3777f9639816cc3be2cbf9b40080e6c14e18992f375f59ae5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CampaignHookProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21d75ff1ff920f03885a49b618f7c1b3b5e9da8ba735b125a3c88ec62fc0fe17(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CustomDeliveryConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3206e9b3e101dbdfbab4b167fbbe437b6df5a8667f1e3d52e265ef2504caff76(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2a3f194f0e2f61ac095227219a69bb6002b2f11a3e883ee97a77d3aaf575c1(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__971ecc06c6c0a231935c31808c1d067094e14be95f83916e7193d19d062edff7(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02466c3fea035dae6003b4d892edc226a948018c5026a83391d853e1adb5c661(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.LimitsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__782bb62da5f39fb9d597470af1efa4fcdb0ff80ce246b1a68705abda99d37c22(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.MessageConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11af643454a88e879a3d44a841a7440d463052b9a9f8894837afdeb1d0f7c0a4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7789111cb61d2c87282d1ee29b8e1ecd9cdfe305539a62babdf135df40e102a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a55591fb10b3aa649e3cc4fff7081bd27134808f40b3426f0d1b1040c798fa32(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b25bbca63e825ff6b501abde63e2de2d55b4f48c1b50cc14e8f9738d2688f0e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.TemplateConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de82f559d77ceee4a216d0bcdff67a789e4cdd47818a7e2dda70c2dd6c55e63a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70fc32fa7b96683078cd6d613bd62ff764758438673848d56e541e3d845a4e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8ed7dd96c16aafe275aca4c5eaab9d3f935bac9194d2f86699b1d5a484552dd(
    *,
    attribute_type: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d7068cf46b5dea22187b378d27f37888567bca535d3c161fdf5816f4109e7b(
    *,
    data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcad47e2a39463d474a4de463cff3ea866a329d0049874cb14dec65a5192428a(
    *,
    body: typing.Optional[builtins.str] = None,
    from_address: typing.Optional[builtins.str] = None,
    html_body: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5711bd48d2337448a48cdb597629c06c82e881cc34b812165389291f4792ec81(
    *,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.EventDimensionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    filter_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f75cb7e807dfe79a19b85bf104c570738dd0d9e5565d57425d54082fae4765(
    *,
    lambda_function_name: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    web_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__369c68d5a011c28939ef45c9d0181abf68afee30d2c4a541e27cc384bdbaaac0(
    *,
    content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.InAppMessageContentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_config: typing.Any = None,
    layout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd8e843454abe931dda3035fe9577af97315cb66140b3b775493c16267a7b5c(
    *,
    body: typing.Optional[builtins.str] = None,
    entity_id: typing.Optional[builtins.str] = None,
    message_type: typing.Optional[builtins.str] = None,
    origination_number: typing.Optional[builtins.str] = None,
    sender_id: typing.Optional[builtins.str] = None,
    template_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5f9eeac0ef1da7f791086412cb13c53a0147c6a9c383482edc81fc463b9850d(
    *,
    delivery_uri: typing.Optional[builtins.str] = None,
    endpoint_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f33b27b37a2b40ecdc2e462af2efd8e422d0ae8e5d18e6600390ef57c62446c(
    *,
    background_color: typing.Optional[builtins.str] = None,
    border_radius: typing.Optional[jsii.Number] = None,
    button_action: typing.Optional[builtins.str] = None,
    link: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
    text_color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9fa660e0e2abbffc8641498aef64f5a8b1fa0b16a3ee77e0d23eb78fb8ecec(
    *,
    attributes: typing.Any = None,
    event_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SetDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metrics: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ae3f4ad63a8f7249b2c0e72d6d5745cf2f08ebe23067ab107734aa59137ff6(
    *,
    alignment: typing.Optional[builtins.str] = None,
    body: typing.Optional[builtins.str] = None,
    text_color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78fc873c9d930c4eed8ba526034beaf3e18989761683e374e83ccb29d875b8c2(
    *,
    android: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.OverrideButtonConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.DefaultButtonConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ios: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.OverrideButtonConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    web: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.OverrideButtonConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92cd497e859572c8cc118d0c5229a7d36478b7b8c2b34925e5f2f4e7072545de(
    *,
    background_color: typing.Optional[builtins.str] = None,
    body_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.InAppMessageBodyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    header_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.InAppMessageHeaderConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_url: typing.Optional[builtins.str] = None,
    primary_btn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.InAppMessageButtonProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    secondary_btn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.InAppMessageButtonProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4df544f968e3811d35ae203f458bcfbed6d3f0f45e80591bb8247658d1ea0a(
    *,
    alignment: typing.Optional[builtins.str] = None,
    header: typing.Optional[builtins.str] = None,
    text_color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65312f3cd527ec459025805d805815ae9b2c77518abcf438fb299c6957605e74(
    *,
    daily: typing.Optional[jsii.Number] = None,
    maximum_duration: typing.Optional[jsii.Number] = None,
    messages_per_second: typing.Optional[jsii.Number] = None,
    session: typing.Optional[jsii.Number] = None,
    total: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19ee131a34a71e54155365b2853c207245d2bee1c5e924da6d8afba431a24d2d(
    *,
    adm_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    apns_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    baidu_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CampaignCustomMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    email_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CampaignEmailMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gcm_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    in_app_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CampaignInAppMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sms_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CampaignSmsMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e10775d47c3c54e5c5d9eb755116a023f41dcce118ba93b6367946e2ab5d357(
    *,
    action: typing.Optional[builtins.str] = None,
    body: typing.Optional[builtins.str] = None,
    image_icon_url: typing.Optional[builtins.str] = None,
    image_small_icon_url: typing.Optional[builtins.str] = None,
    image_url: typing.Optional[builtins.str] = None,
    json_body: typing.Optional[builtins.str] = None,
    media_url: typing.Optional[builtins.str] = None,
    raw_content: typing.Optional[builtins.str] = None,
    silent_push: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    time_to_live: typing.Optional[jsii.Number] = None,
    title: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__745d5a430d0962dfe8f060c450b75b4f10183f52b049bde8621fe86f62aca87f(
    *,
    comparison_operator: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3b91e735b0193b6a55e963c7e865354137511b772f20b5d5141bbdaa7ab3330(
    *,
    button_action: typing.Optional[builtins.str] = None,
    link: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac197d4cddf9ac51bf378c659cf40f2873cba889a659e00e4af9364d7f3eb40(
    *,
    end: builtins.str,
    start: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66ee1a8ddef7f92fbc394edfdc3e9420175412f7af13cdc63cea4db024d06a6(
    *,
    end_time: typing.Optional[builtins.str] = None,
    event_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CampaignEventFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    frequency: typing.Optional[builtins.str] = None,
    is_local_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    quiet_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.QuietTimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    start_time: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__708a9738583487f1b206b6e3901c7d9e8ffb999c5ecf2d03d83130db9cbe8a86(
    *,
    dimension_type: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c789b47b3af2152c0a9bba84f3affeffa89dda156afa661148fbea98621da92c(
    *,
    email_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    push_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sms_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    voice_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91bebb7687409a9932eec1ddc30e9e5bce21c49bebfb75e054c06cc0e3bc8854(
    *,
    name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b64050a2eeb087f58f88d6a71e465dce41ef9c2d308dac9e92c90fd2f8d3384d(
    *,
    custom_delivery_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CustomDeliveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    message_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    size_percent: typing.Optional[jsii.Number] = None,
    template_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    treatment_description: typing.Optional[builtins.str] = None,
    treatment_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8089eb09489d44c4a64192dbd9c8fe4f0ae8d17684ba1c3d9763b2d2393e97f(
    *,
    application_id: builtins.str,
    name: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    segment_id: builtins.str,
    additional_treatments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.WriteTreatmentResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    campaign_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CampaignHookProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_delivery_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CustomDeliveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    holdout_percent: typing.Optional[jsii.Number] = None,
    is_paused: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.LimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    message_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.MessageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    priority: typing.Optional[jsii.Number] = None,
    segment_version: typing.Optional[jsii.Number] = None,
    tags: typing.Any = None,
    template_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    treatment_description: typing.Optional[builtins.str] = None,
    treatment_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7abae51eb3b1f161941e50db5fbebe5cf3c749c2e815f973039ad61896339f89(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    from_address: builtins.str,
    identity: builtins.str,
    configuration_set: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ba4a138e19718fd866fa836cf4c6257f18fa42d0f772d51831891027e5e310(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__804ea79845a98fef52b447794c21d02312b3947df72f3a2cdbebf5c0ef8cadc0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2b7ac710eb003a05553de77978a0bf432e0b082141849898c5dfbf164b61b4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3571c9e54456a7ff75562506238acc99b19962f8b9247aba2fe3df1a62aac7c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5982a64c199a3dbd05157469619fb87103bb18d60ac17c887674ca1c98af71a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0552904454280c91b20abb544ebf8f0d5d10b3561c644ab81e7433e68739c947(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6552928532890b0bb4451f89e36f2fd0599fa25332569a30589de6dabd1c2ff(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91d75ea3a5bc3900bbc4b0958bbc0263a57362f325b830004dddc72b23dfe1b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31b287f2c5e7cfc3790c0eca9541325a73a2157dce8dbc1d3b7d9fa702d77ff(
    *,
    application_id: builtins.str,
    from_address: builtins.str,
    identity: builtins.str,
    configuration_set: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de92e890e6311a7e5df00104dcb543dcbde46783a8f7ec2de256f236f59ae292(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    subject: builtins.str,
    template_name: builtins.str,
    default_substitutions: typing.Optional[builtins.str] = None,
    html_part: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    template_description: typing.Optional[builtins.str] = None,
    text_part: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42a278c52013133399f446e5f556044c118bbcf83e230b9f2be36ee65826b57(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c3e092405beeb55725972c93849cea40cde8553e295e89147bbdf1dabae9b7c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__842354b6737d3f066011001448187e6cd47eb9292c3c3d91c53ed677fabd97e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d7fb2858f2a5e78df5c14250eeed341724afc16b64bc850806da4d4163ec985(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__425a551c7dd2994ef2bc28faf10c1acccbf845469fdf77c6105ccd9dfe28de77(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3064679445a684550ed2de9bfc8b89465ffd8b09aabf1e7a299ac6a62dbee6bb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b95a2d7d0d9191200b484886260a273682ff8d2a18c40ed91b782e67a644f0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bf14ba8036655640c904b31bf6ece4c3ad5c62108cf693250e9d46e9cdc90af(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ff0c2083d81dbecc8b9bdfa839def0127c389629ac4dce169887c0ca4f55952(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e765dee130dbbde67e866633bee4ee835d943cf8392dcd6605e0dde4e3821c(
    *,
    subject: builtins.str,
    template_name: builtins.str,
    default_substitutions: typing.Optional[builtins.str] = None,
    html_part: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    template_description: typing.Optional[builtins.str] = None,
    text_part: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7494978a71be7ff003e54391145803489ba95ef1f0579d626731310f2491ba6d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    destination_stream_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435c126caf6964a902f691992ec1aed7a9475c2ef6e6810980f351ded58de5d9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c83ccd79833fec29db310b9fa416d840e817fcaf74b16d9b3022cc002f0d0a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0d74f7910ba4b74041b4a3f8ceb6f9b383589c9435748173e5da796ac0a468(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__523733f36a90ab4e5bdf0e39f89059f03b9879e928c1155d176f7a0df99913b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a3815f734b46370b2c5a51cd95e50e77cbb9061f0c2d09fbe8c169d14033420(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef26e6e94ef7fa3322d0acc6e2ff1ff55f9317bf3c2fad1529941a4ab3b906e(
    *,
    application_id: builtins.str,
    destination_stream_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb3f8f63a6157e10547523707b6985118a3e678783d2603097b290368727ae6a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_key: builtins.str,
    application_id: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__732d5f076acad8123890183928c3e25c1f90349cfdf24a56d105df721fe5dcb2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83e3844a6b42a96c5783c4b32eee3c53d44a5c8c29b7a53d4285dfe56debd9a4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99b00ece767606c36fcd8737c20c953bd966f1fb88386fcfccdecab9be060dfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5cf7652f52bd0665760eefdef4ebe4661341c7d2f743790a82538cc9b1a59da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__934c050e152924d121e2ce630b51de8fe2580d8d1dda58e4e88cd58ff0b0bbfa(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e274fb934af0ad701780242707b5b8268879db22917a3c6b496e2649c2c225eb(
    *,
    api_key: builtins.str,
    application_id: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e512a1e228b31487f3066dd3e4275e9158997062fd71387d46ccec37606a2d52(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    template_name: builtins.str,
    content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.InAppMessageContentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_config: typing.Any = None,
    layout: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    template_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5b14ad185ba48d75f55570e3ad1a13d78e14254d3beb52e4d282f7011b5af3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__102b7ba4ca5d76c2bcb7d579a1ce2b270541375ae87c3324aec995eb1fb8f88d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__783c9d3a13dcf9b910dcd7009b3f921a2196ebca80cad6d5f6d8d9a2131b6317(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c306b59b5a82d785edcc24ad4f92afce261ef2ea4bd786f4c5db21c19d779c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInAppTemplate.InAppMessageContentProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2ca164aa9281ef31e4a2e0a2f52e7cb0f98adf80d4e8d05370ff01dc3a8c724(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b43b04a5a55917e5e8acbe2af8759330169d92abcb7e8f70276761c87fde2b09(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26614d8a74e54c08b442c84a7e9695ce8c396ca893b287d6ae5b7ff009122c16(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c97689320ae40b05704c91857a6423cddaf3dbeffb7698e0a39308b57220d2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03774d65640cad8e484f201e69f919d0ed339dbe776b950876db72c627fd35c7(
    *,
    alignment: typing.Optional[builtins.str] = None,
    body: typing.Optional[builtins.str] = None,
    text_color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54d14fb9a053c1e37fd12c48b941690f58aa3a225fc8bb133010937f4249b84(
    *,
    android: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.OverrideButtonConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.DefaultButtonConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ios: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.OverrideButtonConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    web: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.OverrideButtonConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062d1a7daee932b386386a6e49e873bba429615975bdf28124c7a6fc931c6aee(
    *,
    background_color: typing.Optional[builtins.str] = None,
    border_radius: typing.Optional[jsii.Number] = None,
    button_action: typing.Optional[builtins.str] = None,
    link: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
    text_color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f33f1d8b7937ccb2928adfdd2a81f68a6c9e96bb0d037e0c9c6b6aa0311b8d5(
    *,
    alignment: typing.Optional[builtins.str] = None,
    header: typing.Optional[builtins.str] = None,
    text_color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__195213fb034889c4b5d757d6fb9b79046ced092a52301af0483c67520253e406(
    *,
    background_color: typing.Optional[builtins.str] = None,
    body_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.BodyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    header_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.HeaderConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_url: typing.Optional[builtins.str] = None,
    primary_btn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.ButtonConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    secondary_btn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.ButtonConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a29b7f724524fecb2d0850fe702875c3a15f609e99011276708d4c705b2e8fc(
    *,
    button_action: typing.Optional[builtins.str] = None,
    link: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e454773fb34afe57455c1ba518ee98492a81389b5fa127cd17273718dc8bcd1d(
    *,
    template_name: builtins.str,
    content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInAppTemplate.InAppMessageContentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_config: typing.Any = None,
    layout: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    template_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c19924c3c4d187e6a4e597c337133470b5e94ec01287814b990418d143d50c8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    template_name: builtins.str,
    adm: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    apns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.APNSPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    baidu: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.DefaultPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_substitutions: typing.Optional[builtins.str] = None,
    gcm: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
    template_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bd85bcc1afb08087adaf829b60ae72f7f789c00438280b47cfad3e4e8e188e7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ea973d201048a1d85c8527dd218e3ea4ba36e582e42e4b36d47bb6c0addca0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6689f4b17f3d51c97d046ff920f42167020ecdb954bcbb703df795aa48fd62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32be5ab1563dc059696ad2e290c93a984c7450eb1d680d90dca0e7d42ea02fbd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77bf2e4b13ec2cfe475f08ed23562640cbcde98d9cb8138c3f3573cc417e532f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.APNSPushNotificationTemplateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dcb8053ca59ff9c0be19a4383b3295f95ada8ab1360a0c61f563aac118fc624(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c2576f9168b75160bea5859251791623f4dc1decc495cb1d53a55ff7a531800(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.DefaultPushNotificationTemplateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a64a0af135c2c3f325587b4f9494bb2df541b2eb06fed9948a862f1c957678(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__156c2a5b1c581871d4bbfb9adc0ebccc63555f7c7e7091b1772889dc981ccba4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPushTemplate.AndroidPushNotificationTemplateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4cbceedb7f94ba5ae9fa8704dff30ab1f8d628748f0401c3a77272aace3cb98(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbbbc4798da119c7d2ec902e6a1f2d7eb20ea88bc394a4e63a0a146c6f9b2327(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1861c8949f9a6171d40596e1bf6cec657c1d8c3a46a998e615674ad5a63e714b(
    *,
    action: typing.Optional[builtins.str] = None,
    body: typing.Optional[builtins.str] = None,
    media_url: typing.Optional[builtins.str] = None,
    sound: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f593b8352c58b9474c9c8b60e12209df9340663b07a166aaafa9f4361f9fc9c7(
    *,
    action: typing.Optional[builtins.str] = None,
    body: typing.Optional[builtins.str] = None,
    image_icon_url: typing.Optional[builtins.str] = None,
    image_url: typing.Optional[builtins.str] = None,
    small_image_icon_url: typing.Optional[builtins.str] = None,
    sound: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a9fa0c7c3f0969aca855183fe31bb20a3232f7f68fca405d8416de89628dfb(
    *,
    action: typing.Optional[builtins.str] = None,
    body: typing.Optional[builtins.str] = None,
    sound: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd3a4d65d82add35f6d1294904a394ae2b9d9f09c6f0f78d8e25def5b4fa1b13(
    *,
    template_name: builtins.str,
    adm: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    apns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.APNSPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    baidu: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.DefaultPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_substitutions: typing.Optional[builtins.str] = None,
    gcm: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPushTemplate.AndroidPushNotificationTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
    template_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b9e0e4cae717e114a852dc3bc4437c0b746385acea12e532445a77a378c9144(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    sender_id: typing.Optional[builtins.str] = None,
    short_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__641cf7f9195aae9dae6d69036a20e83e49d7bc731fda0b737b4de53f5f30cea7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af6ca2c0ec1dafc5e3f466617ea8759dcb8af2b029c793db0cddd445d4b3830(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e0414ce1e027ab6b5c67ee68d8a3766a8bfae21baef29b830c4881812533f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2854f045b9f30c7825e8267836e4fbe8206a1f421b757b06ed0b04dbb40c5a12(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e23b829beec325729e74969ea029e8d36727faa2fed854351448b8dc2e86eec5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__581a443ec8905d7aa8644d9335605a1cb33151dcb443f96ded6410d3769aa4be(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d552897f1d5758cdf867f5379dff6344a4a7cebdd47142cd2fc361f08aca12a(
    *,
    application_id: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    sender_id: typing.Optional[builtins.str] = None,
    short_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f709a034a24c1bdbcf2c3ad69a8ec499d4a31c52228cfccf041a018ef8db5db6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    name: builtins.str,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SegmentDimensionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SegmentGroupsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab85436978fff9eb6b667bf369ce182d580e19493d318100b008eac7b205fad6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95ab46f3fcb3681e3b4d5ef5d055867767a26fd2eecb436628e106f3a21495b6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee563039c51ce7c946ee64d0544b6912c0e141d424096bcf6910faba0e279086(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74415b4339bad69f40ae0cf82368a3aa0c5a21ee8d8ab9924fa39314e9dd645(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7596346842df00f96b4cdfdbd4c88e3d1ebd1006ff6eef96d986ad843c4fe2e1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSegment.SegmentDimensionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e5f8482204fc248f33a5d809b6fe0b1a60a440ed824a88a497c788578f74864(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSegment.SegmentGroupsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19cf08f783ce7a107cff33dc3328d3098db5e5346e4d3f31d8f9929137028aa2(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d49995e4abe481142cc1c1660891bc0850ad1b99f1957bfacf77c4a80bdd90e2(
    *,
    attribute_type: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d797ad7bc3f43fe6b8489c7a02d2973f45c5c7e2f11b2576d335fe1b930e7a7(
    *,
    recency: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.RecencyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3879f4d4c4bc9d3ad9fd3c00fa3f25f1619888f2ef36dfb925dc53cea8ce12a(
    *,
    latitude: jsii.Number,
    longitude: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df576e40323de6048cf308e0f8dda245dbb9d73c2f5a00bc7b66a74ab5ebe3bb(
    *,
    app_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SetDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SetDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    device_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SetDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    make: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SetDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SetDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    platform: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SetDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3846c00f867e46d49f949447ce9f2d30f2fcdb206fa831c6d6ae0ce795c8bf(
    *,
    coordinates: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.CoordinatesProperty, typing.Dict[builtins.str, typing.Any]]],
    range_in_kilometers: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405e07d40b8c0ddf44ea93acd9dc1d8ffffac9f12f4e6664e60c86b7c263462b(
    *,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SegmentDimensionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_segments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SourceSegmentsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_type: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__176f693f956da86315323388adcf262aadf7a6cdb3d859cf5c0bf58ec01ee91c(
    *,
    country: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SetDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gps_point: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.GPSPointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89a5e84535a2aa99d9b66489bc9e075515372707f29ea67a982953e313b5fe25(
    *,
    duration: builtins.str,
    recency_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adeb504bbef1b7a7cd91e8fa51e7e9213f7c20d5c30f440671bd80b76c44bfc7(
    *,
    attributes: typing.Any = None,
    behavior: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.BehaviorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    demographic: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.DemographicProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metrics: typing.Any = None,
    user_attributes: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55b3b5cb3109787d3404864eb7762673d08dde2e0d43b66abe674298c9571b73(
    *,
    groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.GroupsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39b0c4354cc8075763f75e56a57757addd2fe34b15dd9c9b4a9b7998d437d5bb(
    *,
    dimension_type: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__388da4420307c3fdf7dde8a1d10d0e8cc8d6c962e3fadadd9fae09d96077589e(
    *,
    id: builtins.str,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25f43b43d50881dc0b12d0713cceab9df4a33654c37f0f4032f99c402541ca95(
    *,
    application_id: builtins.str,
    name: builtins.str,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SegmentDimensionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegment.SegmentGroupsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1536fb6b841b2ae28085a22bbac5257230add94dcddd63c390ad3d6941c1bdbc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    body: builtins.str,
    template_name: builtins.str,
    default_substitutions: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    template_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284689e5f66f12908f35f21c7be81438110fcbe4de00b5e612fe3c4938da9b7d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a6f692351821c040a7e25e23778d74d6c709b84a9830d9e3895692d6e33126e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84ff9f4a2706bc6d280232f48449544baf035de043a7edd477c36b49a770d660(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68a2e9c56e1723b59d90c1859572868534e794fb2dfb13f93bee7d09edcc1a16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a6ff98aa698d81509091ca1cf004f062a6bbff5ac1491a78ba87aa2bc032f69(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10b1b81307b1076556a881c595d43cb014a04a4bd2d3218f10021904adb69043(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd3fa157e9a3304bccf83ba2950a06e1182c1194aca31c385f8914954dcfd3d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__423db93371632488090f99bb5f94b3d74c4b49c176f644adb2f9a9b89eb1ec23(
    *,
    body: builtins.str,
    template_name: builtins.str,
    default_substitutions: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    template_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eefa81940d32d619367bdcf45d70859abb04ed0a3acb03e963889c077b6a175(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcfd177d8879192e1452736feddc938b4633ce829ab6b202a0f20e96fa0d1c4c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36815d159fd7f8a16a1c1f294ec64660877a873116a1ebc133b345c3c735adf5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d66b91fe903bebc80d5aa290f53e57858be37231f0b2b67a3792364acd72e44a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55f9072e4ea10db6545a901f75a87f0db23d51ed4c12907c8203b488bc5d23b8(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf39a3de9821d1b054616d0b2e269d51093b75f3abc30724908da5749e0280bf(
    *,
    application_id: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass
