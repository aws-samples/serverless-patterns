'''
# Amazon Pinpoint Email Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_pinpointemail as pinpointemail
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for PinpointEmail construct libraries](https://constructs.dev/search?q=pinpointemail)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::PinpointEmail resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PinpointEmail.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::PinpointEmail](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PinpointEmail.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSet",
):
    '''Create a configuration set.

    *Configuration sets* are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpointemail as pinpointemail
        
        cfn_configuration_set = pinpointemail.CfnConfigurationSet(self, "MyCfnConfigurationSet",
            name="name",
        
            # the properties below are optional
            delivery_options=pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty(
                sending_pool_name="sendingPoolName"
            ),
            reputation_options=pinpointemail.CfnConfigurationSet.ReputationOptionsProperty(
                reputation_metrics_enabled=False
            ),
            sending_options=pinpointemail.CfnConfigurationSet.SendingOptionsProperty(
                sending_enabled=False
            ),
            tags=[pinpointemail.CfnConfigurationSet.TagsProperty(
                key="key",
                value="value"
            )],
            tracking_options=pinpointemail.CfnConfigurationSet.TrackingOptionsProperty(
                custom_redirect_domain="customRedirectDomain"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        reputation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.ReputationOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sending_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.SendingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnConfigurationSet.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tracking_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.TrackingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the configuration set.
        :param delivery_options: An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
        :param reputation_options: An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.
        :param sending_options: An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the configuration set.
        :param tracking_options: An object that defines the open and click tracking options for emails that you send using the configuration set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0c95495940bb828b5dc5b2e121395259e9f69d29759aa8ece46c8d24a50624d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetProps(
            name=name,
            delivery_options=delivery_options,
            reputation_options=reputation_options,
            sending_options=sending_options,
            tags=tags,
            tracking_options=tracking_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6dd1ef01c80034f28eb402d34ecce4ecdd4b4ee13faa3eadfb7b0805bfbbbe2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fb71c0b982741aeb6153f00ad8e6a58d1f789158697dc239fe4471c16c599e2)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the configuration set.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0f1c3ca4f76345cbebb7e55834ee085650913c3700910ccf2891098bf5dd795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryOptions")
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.DeliveryOptionsProperty"]]:
        '''An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.DeliveryOptionsProperty"]], jsii.get(self, "deliveryOptions"))

    @delivery_options.setter
    def delivery_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.DeliveryOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdcf7f0b3bf6a04a00a0208ead0f7591a2bd56d6ba291c6b4adff7cb91ec5478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryOptions", value)

    @builtins.property
    @jsii.member(jsii_name="reputationOptions")
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.ReputationOptionsProperty"]]:
        '''An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.ReputationOptionsProperty"]], jsii.get(self, "reputationOptions"))

    @reputation_options.setter
    def reputation_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.ReputationOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08a035b25a3044f443eb9cde1e8501ee0eede79cdfcd1d0177653d7d73eb455b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reputationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="sendingOptions")
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SendingOptionsProperty"]]:
        '''An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SendingOptionsProperty"]], jsii.get(self, "sendingOptions"))

    @sending_options.setter
    def sending_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SendingOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a002abbcbbddd9fe2b7eeab04bcbf56da40005220f6a6b628394edc7a7e25416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendingOptions", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]]:
        '''An object that defines the tags (keys and values) that you want to associate with the configuration set.'''
        return typing.cast(typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e1905ded5be062554dde4d6148690ed8450e064903c4976c9e0eae6a7dd3e7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="trackingOptions")
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.TrackingOptionsProperty"]]:
        '''An object that defines the open and click tracking options for emails that you send using the configuration set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.TrackingOptionsProperty"]], jsii.get(self, "trackingOptions"))

    @tracking_options.setter
    def tracking_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.TrackingOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8a9d08348c04d0e30f1fef6c518db68645e9f8ea6b383d9c916bafb9534f1aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackingOptions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_pool_name": "sendingPoolName"},
    )
    class DeliveryOptionsProperty:
        def __init__(
            self,
            *,
            sending_pool_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Used to associate a configuration set with a dedicated IP pool.

            :param sending_pool_name: The name of the dedicated IP pool that you want to associate with the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                delivery_options_property = pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b87d56e9a0432c3a95462e01fb3c39b9869ae10127a6bd6d73f529f40f2a3ac8)
                check_type(argname="argument sending_pool_name", value=sending_pool_name, expected_type=type_hints["sending_pool_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sending_pool_name is not None:
                self._values["sending_pool_name"] = sending_pool_name

        @builtins.property
        def sending_pool_name(self) -> typing.Optional[builtins.str]:
            '''The name of the dedicated IP pool that you want to associate with the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html#cfn-pinpointemail-configurationset-deliveryoptions-sendingpoolname
            '''
            result = self._values.get("sending_pool_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeliveryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSet.ReputationOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"reputation_metrics_enabled": "reputationMetricsEnabled"},
    )
    class ReputationOptionsProperty:
        def __init__(
            self,
            *,
            reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Enable or disable collection of reputation metrics for emails that you send using this configuration set in the current AWS Region.

            :param reputation_metrics_enabled: If ``true`` , tracking of reputation metrics is enabled for the configuration set. If ``false`` , tracking of reputation metrics is disabled for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                reputation_options_property = pinpointemail.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e33514614151b3f76bcc5d3ad68caca768f9336a4d68ad246d64b79f24465c55)
                check_type(argname="argument reputation_metrics_enabled", value=reputation_metrics_enabled, expected_type=type_hints["reputation_metrics_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if reputation_metrics_enabled is not None:
                self._values["reputation_metrics_enabled"] = reputation_metrics_enabled

        @builtins.property
        def reputation_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , tracking of reputation metrics is enabled for the configuration set.

            If ``false`` , tracking of reputation metrics is disabled for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html#cfn-pinpointemail-configurationset-reputationoptions-reputationmetricsenabled
            '''
            result = self._values.get("reputation_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReputationOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSet.SendingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_enabled": "sendingEnabled"},
    )
    class SendingOptionsProperty:
        def __init__(
            self,
            *,
            sending_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Used to enable or disable email sending for messages that use this configuration set in the current AWS Region.

            :param sending_enabled: If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                sending_options_property = pinpointemail.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80604583cdc26fa7af9cfe1304d24d01df42384b417a45510828012cca0d25ee)
                check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sending_enabled is not None:
                self._values["sending_enabled"] = sending_enabled

        @builtins.property
        def sending_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , email sending is enabled for the configuration set.

            If ``false`` , email sending is disabled for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html#cfn-pinpointemail-configurationset-sendingoptions-sendingenabled
            '''
            result = self._values.get("sending_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SendingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSet.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines the tags (keys and values) that you want to associate with the configuration set.

            :param key: One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character. If you specify tags for the configuration set, then this value is required.
            :param value: The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnConfigurationSet.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__562620ce645d1437ef0f1b78294f817e372f989c3c14f2fe487adf61fab8a53a)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that defines a tag.

            The maximum length of a tag key is 128 characters. The minimum length is 1 character.

            If you specify tags for the configuration set, then this value is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html#cfn-pinpointemail-configurationset-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that defines a tag.

            The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html#cfn-pinpointemail-configurationset-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSet.TrackingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_redirect_domain": "customRedirectDomain"},
    )
    class TrackingOptionsProperty:
        def __init__(
            self,
            *,
            custom_redirect_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines the tracking options for a configuration set.

            When you use Amazon Pinpoint to send an email, it contains an invisible image that's used to track when recipients open your email. If your email contains links, those links are changed slightly in order to track when recipients click them.

            These images and links include references to a domain operated by AWS . You can optionally configure Amazon Pinpoint to use a domain that you operate for these images and links.

            :param custom_redirect_domain: The domain that you want to use for tracking open and click events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                tracking_options_property = pinpointemail.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__770defe01720c229063087808abe9e7902d8fac443aca8bf69c21ea22113e15b)
                check_type(argname="argument custom_redirect_domain", value=custom_redirect_domain, expected_type=type_hints["custom_redirect_domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_redirect_domain is not None:
                self._values["custom_redirect_domain"] = custom_redirect_domain

        @builtins.property
        def custom_redirect_domain(self) -> typing.Optional[builtins.str]:
            '''The domain that you want to use for tracking open and click events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html#cfn-pinpointemail-configurationset-trackingoptions-customredirectdomain
            '''
            result = self._values.get("custom_redirect_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrackingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationSetEventDestination(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetEventDestination",
):
    '''Create an event destination.

    In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

    A single configuration set can include more than one event destination.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpointemail as pinpointemail
        
        cfn_configuration_set_event_destination = pinpointemail.CfnConfigurationSetEventDestination(self, "MyCfnConfigurationSetEventDestination",
            configuration_set_name="configurationSetName",
            event_destination_name="eventDestinationName",
        
            # the properties below are optional
            event_destination=pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty(
                matching_event_types=["matchingEventTypes"],
        
                # the properties below are optional
                cloud_watch_destination=pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                ),
                enabled=False,
                kinesis_firehose_destination=pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                ),
                pinpoint_destination=pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                    application_arn="applicationArn"
                ),
                sns_destination=pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration_set_name: builtins.str,
        event_destination_name: builtins.str,
        event_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration_set_name: The name of the configuration set that contains the event destination that you want to modify.
        :param event_destination_name: The name of the event destination that you want to modify.
        :param event_destination: An object that defines the event destination.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c3015fa55474d84ea557c71099210d5a0a477cd6ac12fea1054d78cb722283a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetEventDestinationProps(
            configuration_set_name=configuration_set_name,
            event_destination_name=event_destination_name,
            event_destination=event_destination,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bda08a945b3045dd0b58544b0d06601426131e7f452c2293b7251954f6a10a0e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__39c836d8d3ff3584a309a0060359145fc888941ac619de072d584340ef996bfd)
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
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set that contains the event destination that you want to modify.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

    @configuration_set_name.setter
    def configuration_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__531085dd5a5b31c859071d23a3a67b1c875544a11378b6547e6de3e4fa79c253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSetName", value)

    @builtins.property
    @jsii.member(jsii_name="eventDestinationName")
    def event_destination_name(self) -> builtins.str:
        '''The name of the event destination that you want to modify.'''
        return typing.cast(builtins.str, jsii.get(self, "eventDestinationName"))

    @event_destination_name.setter
    def event_destination_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__417f9cd4ba4ef0b12bc917319cc0864f3255ed6b4672667c9ad0354b4bd226cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestinationName", value)

    @builtins.property
    @jsii.member(jsii_name="eventDestination")
    def event_destination(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.EventDestinationProperty"]]:
        '''An object that defines the event destination.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.EventDestinationProperty"]], jsii.get(self, "eventDestination"))

    @event_destination.setter
    def event_destination(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.EventDestinationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1cbb4828ca2826fd6cc6f4229b9942f7954db47a766c559f870e0067b4ca12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestination", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_configurations": "dimensionConfigurations"},
    )
    class CloudWatchDestinationProperty:
        def __init__(
            self,
            *,
            dimension_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''An object that defines an Amazon CloudWatch destination for email events.

            You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

            :param dimension_configurations: An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                cloud_watch_destination_property = pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3890c1ab36bc2dce2545a00422d39a194c278990fbd2a7bdeea2af24ee642295)
                check_type(argname="argument dimension_configurations", value=dimension_configurations, expected_type=type_hints["dimension_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimension_configurations is not None:
                self._values["dimension_configurations"] = dimension_configurations

        @builtins.property
        def dimension_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]]:
            '''An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html#cfn-pinpointemail-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations
            '''
            result = self._values.get("dimension_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_dimension_value": "defaultDimensionValue",
            "dimension_name": "dimensionName",
            "dimension_value_source": "dimensionValueSource",
        },
    )
    class DimensionConfigurationProperty:
        def __init__(
            self,
            *,
            default_dimension_value: builtins.str,
            dimension_name: builtins.str,
            dimension_value_source: builtins.str,
        ) -> None:
            '''An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

            :param default_dimension_value: The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria: - It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-). - It can contain no more than 256 characters.
            :param dimension_name: The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria: - It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-). - It can contain no more than 256 characters.
            :param dimension_value_source: The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. Acceptable values: ``MESSAGE_TAG`` , ``EMAIL_HEADER`` , and ``LINK_TAG`` . If you want Amazon Pinpoint to use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` API, choose ``MESSAGE_TAG`` . If you want Amazon Pinpoint to use your own email headers, choose ``EMAIL_HEADER`` . If you want Amazon Pinpoint to use tags that are specified in your links, choose ``LINK_TAG`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                dimension_configuration_property = pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                    default_dimension_value="defaultDimensionValue",
                    dimension_name="dimensionName",
                    dimension_value_source="dimensionValueSource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ccd2366db9978b106bbb0a2988750605a355ac35d2ea11def8733bd8c10738a4)
                check_type(argname="argument default_dimension_value", value=default_dimension_value, expected_type=type_hints["default_dimension_value"])
                check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
                check_type(argname="argument dimension_value_source", value=dimension_value_source, expected_type=type_hints["dimension_value_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_dimension_value": default_dimension_value,
                "dimension_name": dimension_name,
                "dimension_value_source": dimension_value_source,
            }

        @builtins.property
        def default_dimension_value(self) -> builtins.str:
            '''The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email.

            This value has to meet the following criteria:

            - It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).
            - It can contain no more than 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue
            '''
            result = self._values.get("default_dimension_value")
            assert result is not None, "Required property 'default_dimension_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_name(self) -> builtins.str:
            '''The name of an Amazon CloudWatch dimension associated with an email sending metric.

            The name has to meet the following criteria:

            - It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).
            - It can contain no more than 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionname
            '''
            result = self._values.get("dimension_name")
            assert result is not None, "Required property 'dimension_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_value_source(self) -> builtins.str:
            '''The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch.

            Acceptable values: ``MESSAGE_TAG`` , ``EMAIL_HEADER`` , and ``LINK_TAG`` .

            If you want Amazon Pinpoint to use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` API, choose ``MESSAGE_TAG`` . If you want Amazon Pinpoint to use your own email headers, choose ``EMAIL_HEADER`` . If you want Amazon Pinpoint to use tags that are specified in your links, choose ``LINK_TAG`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource
            '''
            result = self._values.get("dimension_value_source")
            assert result is not None, "Required property 'dimension_value_source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "matching_event_types": "matchingEventTypes",
            "cloud_watch_destination": "cloudWatchDestination",
            "enabled": "enabled",
            "kinesis_firehose_destination": "kinesisFirehoseDestination",
            "pinpoint_destination": "pinpointDestination",
            "sns_destination": "snsDestination",
        },
    )
    class EventDestinationProperty:
        def __init__(
            self,
            *,
            matching_event_types: typing.Sequence[builtins.str],
            cloud_watch_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            kinesis_firehose_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            pinpoint_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.PinpointDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints.

            *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

            :param matching_event_types: The types of events that Amazon Pinpoint sends to the specified event destinations. Acceptable values: ``SEND`` , ``REJECT`` , ``BOUNCE`` , ``COMPLAINT`` , ``DELIVERY`` , ``OPEN`` , ``CLICK`` , and ``RENDERING_FAILURE`` .
            :param cloud_watch_destination: An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
            :param enabled: If ``true`` , the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this ``EventDestinationDefinition`` . If ``false`` , the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.
            :param kinesis_firehose_destination: An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.
            :param pinpoint_destination: An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
            :param sns_destination: An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                event_destination_property = pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty(
                    matching_event_types=["matchingEventTypes"],
                
                    # the properties below are optional
                    cloud_watch_destination=pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                        dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                            default_dimension_value="defaultDimensionValue",
                            dimension_name="dimensionName",
                            dimension_value_source="dimensionValueSource"
                        )]
                    ),
                    enabled=False,
                    kinesis_firehose_destination=pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    pinpoint_destination=pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                        application_arn="applicationArn"
                    ),
                    sns_destination=pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__104e59f6882a3ee4477993f5d5d8b2b9d54f3335f8081b27847a6161f06d420f)
                check_type(argname="argument matching_event_types", value=matching_event_types, expected_type=type_hints["matching_event_types"])
                check_type(argname="argument cloud_watch_destination", value=cloud_watch_destination, expected_type=type_hints["cloud_watch_destination"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument kinesis_firehose_destination", value=kinesis_firehose_destination, expected_type=type_hints["kinesis_firehose_destination"])
                check_type(argname="argument pinpoint_destination", value=pinpoint_destination, expected_type=type_hints["pinpoint_destination"])
                check_type(argname="argument sns_destination", value=sns_destination, expected_type=type_hints["sns_destination"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "matching_event_types": matching_event_types,
            }
            if cloud_watch_destination is not None:
                self._values["cloud_watch_destination"] = cloud_watch_destination
            if enabled is not None:
                self._values["enabled"] = enabled
            if kinesis_firehose_destination is not None:
                self._values["kinesis_firehose_destination"] = kinesis_firehose_destination
            if pinpoint_destination is not None:
                self._values["pinpoint_destination"] = pinpoint_destination
            if sns_destination is not None:
                self._values["sns_destination"] = sns_destination

        @builtins.property
        def matching_event_types(self) -> typing.List[builtins.str]:
            '''The types of events that Amazon Pinpoint sends to the specified event destinations.

            Acceptable values: ``SEND`` , ``REJECT`` , ``BOUNCE`` , ``COMPLAINT`` , ``DELIVERY`` , ``OPEN`` , ``CLICK`` , and ``RENDERING_FAILURE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-matchingeventtypes
            '''
            result = self._values.get("matching_event_types")
            assert result is not None, "Required property 'matching_event_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def cloud_watch_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]]:
            '''An object that defines an Amazon CloudWatch destination for email events.

            You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-cloudwatchdestination
            '''
            result = self._values.get("cloud_watch_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , the event destination is enabled.

            When the event destination is enabled, the specified event types are sent to the destinations in this ``EventDestinationDefinition`` .

            If ``false`` , the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def kinesis_firehose_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]]:
            '''An object that defines an Amazon Kinesis Data Firehose destination for email events.

            You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-kinesisfirehosedestination
            '''
            result = self._values.get("kinesis_firehose_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]], result)

        @builtins.property
        def pinpoint_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.PinpointDestinationProperty"]]:
            '''An object that defines a Amazon Pinpoint destination for email events.

            You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-pinpointdestination
            '''
            result = self._values.get("pinpoint_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.PinpointDestinationProperty"]], result)

        @builtins.property
        def sns_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]]:
            '''An object that defines an Amazon SNS destination for email events.

            You can use Amazon SNS to send notification when certain email events occur.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-snsdestination
            '''
            result = self._values.get("sns_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_arn": "deliveryStreamArn",
            "iam_role_arn": "iamRoleArn",
        },
    )
    class KinesisFirehoseDestinationProperty:
        def __init__(
            self,
            *,
            delivery_stream_arn: builtins.str,
            iam_role_arn: builtins.str,
        ) -> None:
            '''An object that defines an Amazon Kinesis Data Firehose destination for email events.

            You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

            :param delivery_stream_arn: The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.
            :param iam_role_arn: The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                kinesis_firehose_destination_property = pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43c2c3692ca31d8abbe447c4b0e81276c57714dbc8f0252a42bc4f7eed3e4993)
                check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream_arn": delivery_stream_arn,
                "iam_role_arn": iam_role_arn,
            }

        @builtins.property
        def delivery_stream_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html#cfn-pinpointemail-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn
            '''
            result = self._values.get("delivery_stream_arn")
            assert result is not None, "Required property 'delivery_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html#cfn-pinpointemail-configurationseteventdestination-kinesisfirehosedestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"application_arn": "applicationArn"},
    )
    class PinpointDestinationProperty:
        def __init__(
            self,
            *,
            application_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines a Amazon Pinpoint destination for email events.

            You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.

            :param application_arn: The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                pinpoint_destination_property = pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                    application_arn="applicationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bbddedb697a679ed675b3745ff92e290485fe90cb047702b3bb582a50b890e9)
                check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_arn is not None:
                self._values["application_arn"] = application_arn

        @builtins.property
        def application_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html#cfn-pinpointemail-configurationseteventdestination-pinpointdestination-applicationarn
            '''
            result = self._values.get("application_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PinpointDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsDestinationProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''An object that defines an Amazon SNS destination for email events.

            You can use Amazon SNS to send notification when certain email events occur.

            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                sns_destination_property = pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e69a19dbd93611e562aa28aa846b8a4bc63f64174335e8cc8f07c1738049a566)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html#cfn-pinpointemail-configurationseteventdestination-snsdestination-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetEventDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "event_destination_name": "eventDestinationName",
        "event_destination": "eventDestination",
    },
)
class CfnConfigurationSetEventDestinationProps:
    def __init__(
        self,
        *,
        configuration_set_name: builtins.str,
        event_destination_name: builtins.str,
        event_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSetEventDestination``.

        :param configuration_set_name: The name of the configuration set that contains the event destination that you want to modify.
        :param event_destination_name: The name of the event destination that you want to modify.
        :param event_destination: An object that defines the event destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpointemail as pinpointemail
            
            cfn_configuration_set_event_destination_props = pinpointemail.CfnConfigurationSetEventDestinationProps(
                configuration_set_name="configurationSetName",
                event_destination_name="eventDestinationName",
            
                # the properties below are optional
                event_destination=pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty(
                    matching_event_types=["matchingEventTypes"],
            
                    # the properties below are optional
                    cloud_watch_destination=pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                        dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                            default_dimension_value="defaultDimensionValue",
                            dimension_name="dimensionName",
                            dimension_value_source="dimensionValueSource"
                        )]
                    ),
                    enabled=False,
                    kinesis_firehose_destination=pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    pinpoint_destination=pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                        application_arn="applicationArn"
                    ),
                    sns_destination=pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57e9786b221f2fd79da4253828be14c3a7e3896c31e26ad734a340d32255e585)
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            check_type(argname="argument event_destination_name", value=event_destination_name, expected_type=type_hints["event_destination_name"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }
        if event_destination is not None:
            self._values["event_destination"] = event_destination

    @builtins.property
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set that contains the event destination that you want to modify.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-configurationsetname
        '''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination_name(self) -> builtins.str:
        '''The name of the event destination that you want to modify.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestinationname
        '''
        result = self._values.get("event_destination_name")
        assert result is not None, "Required property 'event_destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSetEventDestination.EventDestinationProperty]]:
        '''An object that defines the event destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination
        '''
        result = self._values.get("event_destination")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSetEventDestination.EventDestinationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetEventDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpointemail.CfnConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "delivery_options": "deliveryOptions",
        "reputation_options": "reputationOptions",
        "sending_options": "sendingOptions",
        "tags": "tags",
        "tracking_options": "trackingOptions",
    },
)
class CfnConfigurationSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        reputation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sending_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tracking_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSet``.

        :param name: The name of the configuration set.
        :param delivery_options: An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
        :param reputation_options: An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.
        :param sending_options: An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the configuration set.
        :param tracking_options: An object that defines the open and click tracking options for emails that you send using the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpointemail as pinpointemail
            
            cfn_configuration_set_props = pinpointemail.CfnConfigurationSetProps(
                name="name",
            
                # the properties below are optional
                delivery_options=pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName"
                ),
                reputation_options=pinpointemail.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                ),
                sending_options=pinpointemail.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                ),
                tags=[pinpointemail.CfnConfigurationSet.TagsProperty(
                    key="key",
                    value="value"
                )],
                tracking_options=pinpointemail.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7457bc18f69701233a827baf81b82c7229d8f23d32fefec43a93349bf23f182f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument delivery_options", value=delivery_options, expected_type=type_hints["delivery_options"])
            check_type(argname="argument reputation_options", value=reputation_options, expected_type=type_hints["reputation_options"])
            check_type(argname="argument sending_options", value=sending_options, expected_type=type_hints["sending_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tracking_options", value=tracking_options, expected_type=type_hints["tracking_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if delivery_options is not None:
            self._values["delivery_options"] = delivery_options
        if reputation_options is not None:
            self._values["reputation_options"] = reputation_options
        if sending_options is not None:
            self._values["sending_options"] = sending_options
        if tags is not None:
            self._values["tags"] = tags
        if tracking_options is not None:
            self._values["tracking_options"] = tracking_options

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.DeliveryOptionsProperty]]:
        '''An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-deliveryoptions
        '''
        result = self._values.get("delivery_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.DeliveryOptionsProperty]], result)

    @builtins.property
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.ReputationOptionsProperty]]:
        '''An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-reputationoptions
        '''
        result = self._values.get("reputation_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.ReputationOptionsProperty]], result)

    @builtins.property
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SendingOptionsProperty]]:
        '''An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-sendingoptions
        '''
        result = self._values.get("sending_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SendingOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]]:
        '''An object that defines the tags (keys and values) that you want to associate with the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]], result)

    @builtins.property
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.TrackingOptionsProperty]]:
        '''An object that defines the open and click tracking options for emails that you send using the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-trackingoptions
        '''
        result = self._values.get("tracking_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.TrackingOptionsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDedicatedIpPool(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpointemail.CfnDedicatedIpPool",
):
    '''A request to create a new dedicated IP pool.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpointemail as pinpointemail
        
        cfn_dedicated_ip_pool = pinpointemail.CfnDedicatedIpPool(self, "MyCfnDedicatedIpPool",
            pool_name="poolName",
            tags=[pinpointemail.CfnDedicatedIpPool.TagsProperty(
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
        pool_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnDedicatedIpPool.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param pool_name: The name of the dedicated IP pool.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__899a68183365f6ff6816e9b10a8ecb9638a47c22455c5e67ef8907a0bbc5bf31)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDedicatedIpPoolProps(pool_name=pool_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1cf085443e5626a1250bb7258f52d1348a70395f9010d1a929116713b6e1478)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1bc0ee25699131d2d5741f4e7932c5b94f203f53bed5fcb62a6c2f2d7c2ed216)
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
    @jsii.member(jsii_name="poolName")
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dedicated IP pool.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolName"))

    @pool_name.setter
    def pool_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39b83ac5220a2c46a88fe28bbde61c6d4c98d3ca6e0d78c5103c2d9a77837ebc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]]:
        '''An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.'''
        return typing.cast(typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__717209b640ba8aaa41556e1eebf21b07d3a79a0194abd55440b0b7e9eaab3e51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnDedicatedIpPool.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.

            :param key: One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character. If you specify tags for the dedicated IP pool, then this value is required.
            :param value: The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnDedicatedIpPool.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__73df4e743a7061a50cbc7e6826959340c55955221009295c773f9ea7bd24154b)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that defines a tag.

            The maximum length of a tag key is 128 characters. The minimum length is 1 character.

            If you specify tags for the dedicated IP pool, then this value is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html#cfn-pinpointemail-dedicatedippool-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that defines a tag.

            The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html#cfn-pinpointemail-dedicatedippool-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpointemail.CfnDedicatedIpPoolProps",
    jsii_struct_bases=[],
    name_mapping={"pool_name": "poolName", "tags": "tags"},
)
class CfnDedicatedIpPoolProps:
    def __init__(
        self,
        *,
        pool_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnDedicatedIpPool.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDedicatedIpPool``.

        :param pool_name: The name of the dedicated IP pool.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpointemail as pinpointemail
            
            cfn_dedicated_ip_pool_props = pinpointemail.CfnDedicatedIpPoolProps(
                pool_name="poolName",
                tags=[pinpointemail.CfnDedicatedIpPool.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7360a974f3245b975f2f201ea546325186350707a7355c987cb6e19dee857622)
            check_type(argname="argument pool_name", value=pool_name, expected_type=type_hints["pool_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if pool_name is not None:
            self._values["pool_name"] = pool_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dedicated IP pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-poolname
        '''
        result = self._values.get("pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]]:
        '''An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDedicatedIpPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIdentity(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pinpointemail.CfnIdentity",
):
    '''Specifies an identity to use for sending email through Amazon Pinpoint.

    In Amazon Pinpoint, an *identity* is an email address or domain that you use when you send email. Before you can use Amazon Pinpoint to send an email from an identity, you first have to verify it. By verifying an identity, you demonstrate that you're the owner of the address or domain, and that you've given Amazon Pinpoint permission to send email from that identity.

    When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email.

    When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.
    .. epigraph::

       When you use CloudFormation to specify an identity, CloudFormation might indicate that the identity was created successfully. However, you have to verify the identity before you can use it to send email.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pinpointemail as pinpointemail
        
        cfn_identity = pinpointemail.CfnIdentity(self, "MyCfnIdentity",
            name="name",
        
            # the properties below are optional
            dkim_signing_enabled=False,
            feedback_forwarding_enabled=False,
            mail_from_attributes=pinpointemail.CfnIdentity.MailFromAttributesProperty(
                behavior_on_mx_failure="behaviorOnMxFailure",
                mail_from_domain="mailFromDomain"
            ),
            tags=[pinpointemail.CfnIdentity.TagsProperty(
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
        name: builtins.str,
        dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        mail_from_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdentity.MailFromAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnIdentity.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The address or domain of the identity, such as *sender@example.com* or *example.co.uk* .
        :param dkim_signing_enabled: For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain. If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.
        :param feedback_forwarding_enabled: Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event. When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email. When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
        :param mail_from_attributes: Used to enable or disable the custom Mail-From domain configuration for an email identity.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the email identity.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f326a74ba0fea8fd81e31aaa8d715b3c05b23e23144183b83fb47b6043729720)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIdentityProps(
            name=name,
            dkim_signing_enabled=dkim_signing_enabled,
            feedback_forwarding_enabled=feedback_forwarding_enabled,
            mail_from_attributes=mail_from_attributes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e4e4543be7981341109206dcbcc042403c49ab5cc93a7468e1c2d0fc2d981d6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__16da2963f775d8cf55ea65eedcf98bff589e32eeb4121a26c1eaa47f470e4d6f)
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
    @jsii.member(jsii_name="attrIdentityDnsRecordName1")
    def attr_identity_dns_record_name1(self) -> builtins.str:
        '''The host name for the first token that you have to add to the DNS configuration for your domain.

        For more information, see `Verifying a Domain <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html#channels-email-manage-verify-domain>`_ in the Amazon Pinpoint User Guide.

        :cloudformationAttribute: IdentityDNSRecordName1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName1"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordName2")
    def attr_identity_dns_record_name2(self) -> builtins.str:
        '''The host name for the second token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordName2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName2"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordName3")
    def attr_identity_dns_record_name3(self) -> builtins.str:
        '''The host name for the third token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordName3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName3"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordValue1")
    def attr_identity_dns_record_value1(self) -> builtins.str:
        '''The record value for the first token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordValue1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue1"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordValue2")
    def attr_identity_dns_record_value2(self) -> builtins.str:
        '''The record value for the second token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordValue2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue2"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordValue3")
    def attr_identity_dns_record_value3(self) -> builtins.str:
        '''The record value for the third token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordValue3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue3"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The address or domain of the identity, such as *sender@example.com* or *example.co.uk* .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a344c6ab13691bd4bd97468f73a415d92b5843889d1efba47066f38e2fcb9cd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="dkimSigningEnabled")
    def dkim_signing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "dkimSigningEnabled"))

    @dkim_signing_enabled.setter
    def dkim_signing_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d0a095db592acb68d9c479b2be05bf7557914e245d0d076aed2c2cecf3b945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dkimSigningEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="feedbackForwardingEnabled")
    def feedback_forwarding_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Used to enable or disable feedback forwarding for an identity.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "feedbackForwardingEnabled"))

    @feedback_forwarding_enabled.setter
    def feedback_forwarding_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff82aaaef73393b328387bb3901051117fe4defd7e0c76ae82e9bcdbcccb25fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "feedbackForwardingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="mailFromAttributes")
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIdentity.MailFromAttributesProperty"]]:
        '''Used to enable or disable the custom Mail-From domain configuration for an email identity.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIdentity.MailFromAttributesProperty"]], jsii.get(self, "mailFromAttributes"))

    @mail_from_attributes.setter
    def mail_from_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIdentity.MailFromAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58adb03bd00520402e29450292dd98c03ea130644b0ff31629f5af40200b7411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mailFromAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnIdentity.TagsProperty"]]:
        '''An object that defines the tags (keys and values) that you want to associate with the email identity.'''
        return typing.cast(typing.Optional[typing.List["CfnIdentity.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnIdentity.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43129449e96a5f647cffa7f20d0cf0a1c571e88e40b467b90ed004495e72fe4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnIdentity.MailFromAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "behavior_on_mx_failure": "behaviorOnMxFailure",
            "mail_from_domain": "mailFromDomain",
        },
    )
    class MailFromAttributesProperty:
        def __init__(
            self,
            *,
            behavior_on_mx_failure: typing.Optional[builtins.str] = None,
            mail_from_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A list of attributes that are associated with a MAIL FROM domain.

            :param behavior_on_mx_failure: The action that Amazon Pinpoint to takes if it can't read the required MX record for a custom MAIL FROM domain. When you set this value to ``UseDefaultValue`` , Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage`` , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to deliver the email. These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.
            :param mail_from_domain: The name of a domain that an email identity uses as a custom MAIL FROM domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                mail_from_attributes_property = pinpointemail.CfnIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc9de2604bb5c3007061506d2abc0741740e03dc2f774a74f08a1b0510196bb8)
                check_type(argname="argument behavior_on_mx_failure", value=behavior_on_mx_failure, expected_type=type_hints["behavior_on_mx_failure"])
                check_type(argname="argument mail_from_domain", value=mail_from_domain, expected_type=type_hints["mail_from_domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if behavior_on_mx_failure is not None:
                self._values["behavior_on_mx_failure"] = behavior_on_mx_failure
            if mail_from_domain is not None:
                self._values["mail_from_domain"] = mail_from_domain

        @builtins.property
        def behavior_on_mx_failure(self) -> typing.Optional[builtins.str]:
            '''The action that Amazon Pinpoint to takes if it can't read the required MX record for a custom MAIL FROM domain.

            When you set this value to ``UseDefaultValue`` , Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage`` , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to deliver the email.

            These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html#cfn-pinpointemail-identity-mailfromattributes-behavioronmxfailure
            '''
            result = self._values.get("behavior_on_mx_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mail_from_domain(self) -> typing.Optional[builtins.str]:
            '''The name of a domain that an email identity uses as a custom MAIL FROM domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html#cfn-pinpointemail-identity-mailfromattributes-mailfromdomain
            '''
            result = self._values.get("mail_from_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MailFromAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pinpointemail.CfnIdentity.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines the tags (keys and values) that you want to associate with the identity.

            :param key: One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character. If you specify tags for the identity, then this value is required.
            :param value: The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnIdentity.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb7e3cf8545172df7fe9babf9116222ca731c0cf6b2d91caa35d2b263387135d)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that defines a tag.

            The maximum length of a tag key is 128 characters. The minimum length is 1 character.

            If you specify tags for the identity, then this value is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html#cfn-pinpointemail-identity-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that defines a tag.

            The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html#cfn-pinpointemail-identity-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pinpointemail.CfnIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dkim_signing_enabled": "dkimSigningEnabled",
        "feedback_forwarding_enabled": "feedbackForwardingEnabled",
        "mail_from_attributes": "mailFromAttributes",
        "tags": "tags",
    },
)
class CfnIdentityProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        mail_from_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnIdentity.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIdentity``.

        :param name: The address or domain of the identity, such as *sender@example.com* or *example.co.uk* .
        :param dkim_signing_enabled: For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain. If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.
        :param feedback_forwarding_enabled: Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event. When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email. When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
        :param mail_from_attributes: Used to enable or disable the custom Mail-From domain configuration for an email identity.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the email identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pinpointemail as pinpointemail
            
            cfn_identity_props = pinpointemail.CfnIdentityProps(
                name="name",
            
                # the properties below are optional
                dkim_signing_enabled=False,
                feedback_forwarding_enabled=False,
                mail_from_attributes=pinpointemail.CfnIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                ),
                tags=[pinpointemail.CfnIdentity.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__070bd24a79d16b8bdadba5241ca10cde0d0f04ed19c67a953f10a85f040f648f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dkim_signing_enabled", value=dkim_signing_enabled, expected_type=type_hints["dkim_signing_enabled"])
            check_type(argname="argument feedback_forwarding_enabled", value=feedback_forwarding_enabled, expected_type=type_hints["feedback_forwarding_enabled"])
            check_type(argname="argument mail_from_attributes", value=mail_from_attributes, expected_type=type_hints["mail_from_attributes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if dkim_signing_enabled is not None:
            self._values["dkim_signing_enabled"] = dkim_signing_enabled
        if feedback_forwarding_enabled is not None:
            self._values["feedback_forwarding_enabled"] = feedback_forwarding_enabled
        if mail_from_attributes is not None:
            self._values["mail_from_attributes"] = mail_from_attributes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The address or domain of the identity, such as *sender@example.com* or *example.co.uk* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dkim_signing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain.

        If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-dkimsigningenabled
        '''
        result = self._values.get("dkim_signing_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def feedback_forwarding_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Used to enable or disable feedback forwarding for an identity.

        This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.

        When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.

        When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-feedbackforwardingenabled
        '''
        result = self._values.get("feedback_forwarding_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIdentity.MailFromAttributesProperty]]:
        '''Used to enable or disable the custom Mail-From domain configuration for an email identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-mailfromattributes
        '''
        result = self._values.get("mail_from_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIdentity.MailFromAttributesProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnIdentity.TagsProperty]]:
        '''An object that defines the tags (keys and values) that you want to associate with the email identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnIdentity.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfigurationSet",
    "CfnConfigurationSetEventDestination",
    "CfnConfigurationSetEventDestinationProps",
    "CfnConfigurationSetProps",
    "CfnDedicatedIpPool",
    "CfnDedicatedIpPoolProps",
    "CfnIdentity",
    "CfnIdentityProps",
]

publication.publish()

def _typecheckingstub__b0c95495940bb828b5dc5b2e121395259e9f69d29759aa8ece46c8d24a50624d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    delivery_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    reputation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sending_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6dd1ef01c80034f28eb402d34ecce4ecdd4b4ee13faa3eadfb7b0805bfbbbe2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb71c0b982741aeb6153f00ad8e6a58d1f789158697dc239fe4471c16c599e2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f1c3ca4f76345cbebb7e55834ee085650913c3700910ccf2891098bf5dd795(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdcf7f0b3bf6a04a00a0208ead0f7591a2bd56d6ba291c6b4adff7cb91ec5478(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.DeliveryOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a035b25a3044f443eb9cde1e8501ee0eede79cdfcd1d0177653d7d73eb455b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.ReputationOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a002abbcbbddd9fe2b7eeab04bcbf56da40005220f6a6b628394edc7a7e25416(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SendingOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e1905ded5be062554dde4d6148690ed8450e064903c4976c9e0eae6a7dd3e7e(
    value: typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8a9d08348c04d0e30f1fef6c518db68645e9f8ea6b383d9c916bafb9534f1aa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.TrackingOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b87d56e9a0432c3a95462e01fb3c39b9869ae10127a6bd6d73f529f40f2a3ac8(
    *,
    sending_pool_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e33514614151b3f76bcc5d3ad68caca768f9336a4d68ad246d64b79f24465c55(
    *,
    reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80604583cdc26fa7af9cfe1304d24d01df42384b417a45510828012cca0d25ee(
    *,
    sending_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__562620ce645d1437ef0f1b78294f817e372f989c3c14f2fe487adf61fab8a53a(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__770defe01720c229063087808abe9e7902d8fac443aca8bf69c21ea22113e15b(
    *,
    custom_redirect_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3015fa55474d84ea557c71099210d5a0a477cd6ac12fea1054d78cb722283a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration_set_name: builtins.str,
    event_destination_name: builtins.str,
    event_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bda08a945b3045dd0b58544b0d06601426131e7f452c2293b7251954f6a10a0e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c836d8d3ff3584a309a0060359145fc888941ac619de072d584340ef996bfd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__531085dd5a5b31c859071d23a3a67b1c875544a11378b6547e6de3e4fa79c253(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417f9cd4ba4ef0b12bc917319cc0864f3255ed6b4672667c9ad0354b4bd226cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1cbb4828ca2826fd6cc6f4229b9942f7954db47a766c559f870e0067b4ca12(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSetEventDestination.EventDestinationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3890c1ab36bc2dce2545a00422d39a194c278990fbd2a7bdeea2af24ee642295(
    *,
    dimension_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.DimensionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd2366db9978b106bbb0a2988750605a355ac35d2ea11def8733bd8c10738a4(
    *,
    default_dimension_value: builtins.str,
    dimension_name: builtins.str,
    dimension_value_source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104e59f6882a3ee4477993f5d5d8b2b9d54f3335f8081b27847a6161f06d420f(
    *,
    matching_event_types: typing.Sequence[builtins.str],
    cloud_watch_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.CloudWatchDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kinesis_firehose_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    pinpoint_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.PinpointDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.SnsDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43c2c3692ca31d8abbe447c4b0e81276c57714dbc8f0252a42bc4f7eed3e4993(
    *,
    delivery_stream_arn: builtins.str,
    iam_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bbddedb697a679ed675b3745ff92e290485fe90cb047702b3bb582a50b890e9(
    *,
    application_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69a19dbd93611e562aa28aa846b8a4bc63f64174335e8cc8f07c1738049a566(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57e9786b221f2fd79da4253828be14c3a7e3896c31e26ad734a340d32255e585(
    *,
    configuration_set_name: builtins.str,
    event_destination_name: builtins.str,
    event_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7457bc18f69701233a827baf81b82c7229d8f23d32fefec43a93349bf23f182f(
    *,
    name: builtins.str,
    delivery_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    reputation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sending_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__899a68183365f6ff6816e9b10a8ecb9638a47c22455c5e67ef8907a0bbc5bf31(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    pool_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDedicatedIpPool.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1cf085443e5626a1250bb7258f52d1348a70395f9010d1a929116713b6e1478(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bc0ee25699131d2d5741f4e7932c5b94f203f53bed5fcb62a6c2f2d7c2ed216(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39b83ac5220a2c46a88fe28bbde61c6d4c98d3ca6e0d78c5103c2d9a77837ebc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__717209b640ba8aaa41556e1eebf21b07d3a79a0194abd55440b0b7e9eaab3e51(
    value: typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73df4e743a7061a50cbc7e6826959340c55955221009295c773f9ea7bd24154b(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7360a974f3245b975f2f201ea546325186350707a7355c987cb6e19dee857622(
    *,
    pool_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDedicatedIpPool.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f326a74ba0fea8fd81e31aaa8d715b3c05b23e23144183b83fb47b6043729720(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    mail_from_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnIdentity.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e4e4543be7981341109206dcbcc042403c49ab5cc93a7468e1c2d0fc2d981d6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16da2963f775d8cf55ea65eedcf98bff589e32eeb4121a26c1eaa47f470e4d6f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a344c6ab13691bd4bd97468f73a415d92b5843889d1efba47066f38e2fcb9cd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d0a095db592acb68d9c479b2be05bf7557914e245d0d076aed2c2cecf3b945(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff82aaaef73393b328387bb3901051117fe4defd7e0c76ae82e9bcdbcccb25fe(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58adb03bd00520402e29450292dd98c03ea130644b0ff31629f5af40200b7411(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIdentity.MailFromAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43129449e96a5f647cffa7f20d0cf0a1c571e88e40b467b90ed004495e72fe4e(
    value: typing.Optional[typing.List[CfnIdentity.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc9de2604bb5c3007061506d2abc0741740e03dc2f774a74f08a1b0510196bb8(
    *,
    behavior_on_mx_failure: typing.Optional[builtins.str] = None,
    mail_from_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7e3cf8545172df7fe9babf9116222ca731c0cf6b2d91caa35d2b263387135d(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__070bd24a79d16b8bdadba5241ca10cde0d0f04ed19c67a953f10a85f040f648f(
    *,
    name: builtins.str,
    dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    mail_from_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnIdentity.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
