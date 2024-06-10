'''
# AWS::Location Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_location as location
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Location construct libraries](https://constructs.dev/search?q=location)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Location resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Location.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-location-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Location](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Location.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAPIKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_location.CfnAPIKey",
):
    '''The API key resource in your AWS account, which lets you grant actions for Amazon Location resources to the API key bearer.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html
    :cloudformationResource: AWS::Location::APIKey
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_location as location
        
        cfn_aPIKey = location.CfnAPIKey(self, "MyCfnAPIKey",
            key_name="keyName",
            restrictions=location.CfnAPIKey.ApiKeyRestrictionsProperty(
                allow_actions=["allowActions"],
                allow_resources=["allowResources"],
        
                # the properties below are optional
                allow_referers=["allowReferers"]
            ),
        
            # the properties below are optional
            description="description",
            expire_time="expireTime",
            force_delete=False,
            force_update=False,
            no_expiry=False,
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
        key_name: builtins.str,
        restrictions: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAPIKey.ApiKeyRestrictionsProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        expire_time: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        force_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        no_expiry: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param key_name: A custom name for the API key resource. Requirements: - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). - Must be a unique API key name. - No spaces allowed. For example, ``ExampleAPIKey`` .
        :param restrictions: The API key restrictions for the API key resource.
        :param description: Updates the description for the API key resource.
        :param expire_time: The optional timestamp for when the API key resource will expire in `ISO 8601 format <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ .
        :param force_delete: ForceDelete bypasses an API key's expiry conditions and deletes the key. Set the parameter ``true`` to delete the key or to ``false`` to not preemptively delete the API key. Valid values: ``true`` , or ``false`` . .. epigraph:: This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.
        :param force_update: The boolean flag to be included for updating ``ExpireTime`` or Restrictions details. Must be set to ``true`` to update an API key resource that has been used in the past 7 days. ``False`` if force update is not preferred.
        :param no_expiry: Whether the API key should expire. Set to ``true`` to set the API key to have no expiration time.
        :param tags: Applies one or more tags to the map resource. A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2ae0e8c734c36fc4dfc2e50264fbc5e41cc44ca78d64c47f19cac56e4318d32)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAPIKeyProps(
            key_name=key_name,
            restrictions=restrictions,
            description=description,
            expire_time=expire_time,
            force_delete=force_delete,
            force_update=force_update,
            no_expiry=no_expiry,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90e4d83d582a33efc0dfeef244e5a4b84a90230cc485853b42d16a3e6f6609a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__099c2b5d173d474236a30915cc6fc0919b6fe1cf215f99e6636485c92a9af0ca)
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
        '''The Amazon Resource Name (ARN) for the resource.

        Used when you need to specify a resource across all AWS .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''The timestamp for when the API key resource was created in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ.

        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrKeyArn")
    def attr_key_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the API key resource.

        Used when you need to specify a resource across all AWS .

        :cloudformationAttribute: KeyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKeyArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''The timestamp for when the API key resource was last updated in ISO 8601 format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

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
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        '''A custom name for the API key resource.'''
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c00e03a38669285c7b235bbd87ec7317379694b0537c3a85e4741d27c54c9d3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="restrictions")
    def restrictions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAPIKey.ApiKeyRestrictionsProperty"]:
        '''The API key restrictions for the API key resource.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAPIKey.ApiKeyRestrictionsProperty"], jsii.get(self, "restrictions"))

    @restrictions.setter
    def restrictions(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAPIKey.ApiKeyRestrictionsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65682d4a834f16510a57f21e8af7c41ba661e7d0f78293abcd483f9d45afba31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictions", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Updates the description for the API key resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1957f4ade558178bedd1746c97b21ac5195a216695895f32ba33d6fe99216c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expireTime")
    def expire_time(self) -> typing.Optional[builtins.str]:
        '''The optional timestamp for when the API key resource will expire in `ISO 8601 format <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expireTime"))

    @expire_time.setter
    def expire_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8263b20b7b28c2712bf62bdacab9989763120af28d1e026f26e14f6e572ae7c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expireTime", value)

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''ForceDelete bypasses an API key's expiry conditions and deletes the key.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8379f2b16717a153383f6b36ff735d0d746008205280dddfc3ffe2f253f29a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="forceUpdate")
    def force_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The boolean flag to be included for updating ``ExpireTime`` or Restrictions details.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "forceUpdate"))

    @force_update.setter
    def force_update(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6402962818d046984829754f6a1e3957be1c7b7981fc92251adcdb9aaeefd493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="noExpiry")
    def no_expiry(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the API key should expire.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "noExpiry"))

    @no_expiry.setter
    def no_expiry(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f2e8a3ec18117161377722f1dd02cee2566e5eb477a2de4cfbc6a270028941e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noExpiry", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Applies one or more tags to the map resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__297a793f153416e3131543d9b1a435c125bf1b45672e8ee10841ec34b14e6d66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_location.CfnAPIKey.ApiKeyRestrictionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_actions": "allowActions",
            "allow_resources": "allowResources",
            "allow_referers": "allowReferers",
        },
    )
    class ApiKeyRestrictionsProperty:
        def __init__(
            self,
            *,
            allow_actions: typing.Sequence[builtins.str],
            allow_resources: typing.Sequence[builtins.str],
            allow_referers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''API Restrictions on the allowed actions, resources, and referers for an API key resource.

            :param allow_actions: A list of allowed actions that an API key resource grants permissions to perform. You must have at least one action for each type of resource. For example, if you have a place resource, you must include at least one place action. The following are valid values for the actions. - *Map actions* - ``geo:GetMap*`` - Allows all actions needed for map rendering. - *Place actions* - ``geo:SearchPlaceIndexForText`` - Allows geocoding. - ``geo:SearchPlaceIndexForPosition`` - Allows reverse geocoding. - ``geo:SearchPlaceIndexForSuggestions`` - Allows generating suggestions from text. - ``geo:GetPlace`` - Allows finding a place by place ID. - *Route actions* - ``geo:CalculateRoute`` - Allows point to point routing. - ``geo:CalculateRouteMatrix`` - Allows calculating a matrix of routes. .. epigraph:: You must use these strings exactly. For example, to provide access to map rendering, the only valid action is ``geo:GetMap*`` as an input to the list. ``["geo:GetMap*"]`` is valid but ``["geo:GetMapTile"]`` is not. Similarly, you cannot use ``["geo:SearchPlaceIndexFor*"]`` - you must list each of the Place actions separately.
            :param allow_resources: A list of allowed resource ARNs that a API key bearer can perform actions on. - The ARN must be the correct ARN for a map, place, or route ARN. You may include wildcards in the resource-id to match multiple resources of the same type. - The resources must be in the same ``partition`` , ``region`` , and ``account-id`` as the key that is being created. - Other than wildcards, you must include the full ARN, including the ``arn`` , ``partition`` , ``service`` , ``region`` , ``account-id`` and ``resource-id`` delimited by colons (:). - No spaces allowed, even with wildcards. For example, ``arn:aws:geo:region: *account-id* :map/ExampleMap*`` . For more information about ARN format, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ .
            :param allow_referers: An optional list of allowed HTTP referers for which requests must originate from. Requests using this API key from other domains will not be allowed. Requirements: - Contain only alphanumeric characters (A–Z, a–z, 0–9) or any symbols in this list ``$\\-._+!*``(),;/?:@=&` - May contain a percent (%) if followed by 2 hexadecimal digits (A-F, a-f, 0-9); this is used for URL encoding purposes. - May contain wildcard characters question mark (?) and asterisk (*). Question mark (?) will replace any single character (including hexadecimal digits). Asterisk (*) will replace any multiple characters (including multiple hexadecimal digits). - No spaces allowed. For example, ``https://example.com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-apikey-apikeyrestrictions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_location as location
                
                api_key_restrictions_property = location.CfnAPIKey.ApiKeyRestrictionsProperty(
                    allow_actions=["allowActions"],
                    allow_resources=["allowResources"],
                
                    # the properties below are optional
                    allow_referers=["allowReferers"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c74737f1e32f7583c8c63e1c8de07d36792e8e3aee5f799d6c8a265f1a3bebb)
                check_type(argname="argument allow_actions", value=allow_actions, expected_type=type_hints["allow_actions"])
                check_type(argname="argument allow_resources", value=allow_resources, expected_type=type_hints["allow_resources"])
                check_type(argname="argument allow_referers", value=allow_referers, expected_type=type_hints["allow_referers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_actions": allow_actions,
                "allow_resources": allow_resources,
            }
            if allow_referers is not None:
                self._values["allow_referers"] = allow_referers

        @builtins.property
        def allow_actions(self) -> typing.List[builtins.str]:
            '''A list of allowed actions that an API key resource grants permissions to perform.

            You must have at least one action for each type of resource. For example, if you have a place resource, you must include at least one place action.

            The following are valid values for the actions.

            - *Map actions*
            - ``geo:GetMap*`` - Allows all actions needed for map rendering.
            - *Place actions*
            - ``geo:SearchPlaceIndexForText`` - Allows geocoding.
            - ``geo:SearchPlaceIndexForPosition`` - Allows reverse geocoding.
            - ``geo:SearchPlaceIndexForSuggestions`` - Allows generating suggestions from text.
            - ``geo:GetPlace`` - Allows finding a place by place ID.
            - *Route actions*
            - ``geo:CalculateRoute`` - Allows point to point routing.
            - ``geo:CalculateRouteMatrix`` - Allows calculating a matrix of routes.

            .. epigraph::

               You must use these strings exactly. For example, to provide access to map rendering, the only valid action is ``geo:GetMap*`` as an input to the list. ``["geo:GetMap*"]`` is valid but ``["geo:GetMapTile"]`` is not. Similarly, you cannot use ``["geo:SearchPlaceIndexFor*"]`` - you must list each of the Place actions separately.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-apikey-apikeyrestrictions.html#cfn-location-apikey-apikeyrestrictions-allowactions
            '''
            result = self._values.get("allow_actions")
            assert result is not None, "Required property 'allow_actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def allow_resources(self) -> typing.List[builtins.str]:
            '''A list of allowed resource ARNs that a API key bearer can perform actions on.

            - The ARN must be the correct ARN for a map, place, or route ARN. You may include wildcards in the resource-id to match multiple resources of the same type.
            - The resources must be in the same ``partition`` , ``region`` , and ``account-id`` as the key that is being created.
            - Other than wildcards, you must include the full ARN, including the ``arn`` , ``partition`` , ``service`` , ``region`` , ``account-id`` and ``resource-id`` delimited by colons (:).
            - No spaces allowed, even with wildcards. For example, ``arn:aws:geo:region: *account-id* :map/ExampleMap*`` .

            For more information about ARN format, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-apikey-apikeyrestrictions.html#cfn-location-apikey-apikeyrestrictions-allowresources
            '''
            result = self._values.get("allow_resources")
            assert result is not None, "Required property 'allow_resources' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def allow_referers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An optional list of allowed HTTP referers for which requests must originate from.

            Requests using this API key from other domains will not be allowed.

            Requirements:

            - Contain only alphanumeric characters (A–Z, a–z, 0–9) or any symbols in this list ``$\\-._+!*``(),;/?:@=&`
            - May contain a percent (%) if followed by 2 hexadecimal digits (A-F, a-f, 0-9); this is used for URL encoding purposes.
            - May contain wildcard characters question mark (?) and asterisk (*).

            Question mark (?) will replace any single character (including hexadecimal digits).

            Asterisk (*) will replace any multiple characters (including multiple hexadecimal digits).

            - No spaces allowed. For example, ``https://example.com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-apikey-apikeyrestrictions.html#cfn-location-apikey-apikeyrestrictions-allowreferers
            '''
            result = self._values.get("allow_referers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiKeyRestrictionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_location.CfnAPIKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "key_name": "keyName",
        "restrictions": "restrictions",
        "description": "description",
        "expire_time": "expireTime",
        "force_delete": "forceDelete",
        "force_update": "forceUpdate",
        "no_expiry": "noExpiry",
        "tags": "tags",
    },
)
class CfnAPIKeyProps:
    def __init__(
        self,
        *,
        key_name: builtins.str,
        restrictions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAPIKey.ApiKeyRestrictionsProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        expire_time: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        force_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        no_expiry: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAPIKey``.

        :param key_name: A custom name for the API key resource. Requirements: - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). - Must be a unique API key name. - No spaces allowed. For example, ``ExampleAPIKey`` .
        :param restrictions: The API key restrictions for the API key resource.
        :param description: Updates the description for the API key resource.
        :param expire_time: The optional timestamp for when the API key resource will expire in `ISO 8601 format <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ .
        :param force_delete: ForceDelete bypasses an API key's expiry conditions and deletes the key. Set the parameter ``true`` to delete the key or to ``false`` to not preemptively delete the API key. Valid values: ``true`` , or ``false`` . .. epigraph:: This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.
        :param force_update: The boolean flag to be included for updating ``ExpireTime`` or Restrictions details. Must be set to ``true`` to update an API key resource that has been used in the past 7 days. ``False`` if force update is not preferred.
        :param no_expiry: Whether the API key should expire. Set to ``true`` to set the API key to have no expiration time.
        :param tags: Applies one or more tags to the map resource. A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_location as location
            
            cfn_aPIKey_props = location.CfnAPIKeyProps(
                key_name="keyName",
                restrictions=location.CfnAPIKey.ApiKeyRestrictionsProperty(
                    allow_actions=["allowActions"],
                    allow_resources=["allowResources"],
            
                    # the properties below are optional
                    allow_referers=["allowReferers"]
                ),
            
                # the properties below are optional
                description="description",
                expire_time="expireTime",
                force_delete=False,
                force_update=False,
                no_expiry=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe99c80388f80e304ec3579f14c21edc069b0865131b2673a8f49e8274c07f4)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expire_time", value=expire_time, expected_type=type_hints["expire_time"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument force_update", value=force_update, expected_type=type_hints["force_update"])
            check_type(argname="argument no_expiry", value=no_expiry, expected_type=type_hints["no_expiry"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_name": key_name,
            "restrictions": restrictions,
        }
        if description is not None:
            self._values["description"] = description
        if expire_time is not None:
            self._values["expire_time"] = expire_time
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if force_update is not None:
            self._values["force_update"] = force_update
        if no_expiry is not None:
            self._values["no_expiry"] = no_expiry
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def key_name(self) -> builtins.str:
        '''A custom name for the API key resource.

        Requirements:

        - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).
        - Must be a unique API key name.
        - No spaces allowed. For example, ``ExampleAPIKey`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html#cfn-location-apikey-keyname
        '''
        result = self._values.get("key_name")
        assert result is not None, "Required property 'key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def restrictions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAPIKey.ApiKeyRestrictionsProperty]:
        '''The API key restrictions for the API key resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html#cfn-location-apikey-restrictions
        '''
        result = self._values.get("restrictions")
        assert result is not None, "Required property 'restrictions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAPIKey.ApiKeyRestrictionsProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Updates the description for the API key resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html#cfn-location-apikey-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expire_time(self) -> typing.Optional[builtins.str]:
        '''The optional timestamp for when the API key resource will expire in `ISO 8601 format <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html#cfn-location-apikey-expiretime
        '''
        result = self._values.get("expire_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''ForceDelete bypasses an API key's expiry conditions and deletes the key.

        Set the parameter ``true`` to delete the key or to ``false`` to not preemptively delete the API key.

        Valid values: ``true`` , or ``false`` .
        .. epigraph::

           This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html#cfn-location-apikey-forcedelete
        '''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def force_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The boolean flag to be included for updating ``ExpireTime`` or Restrictions details.

        Must be set to ``true`` to update an API key resource that has been used in the past 7 days. ``False`` if force update is not preferred.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html#cfn-location-apikey-forceupdate
        '''
        result = self._values.get("force_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def no_expiry(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the API key should expire.

        Set to ``true`` to set the API key to have no expiration time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html#cfn-location-apikey-noexpiry
        '''
        result = self._values.get("no_expiry")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Applies one or more tags to the map resource.

        A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-apikey.html#cfn-location-apikey-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPIKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnGeofenceCollection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_location.CfnGeofenceCollection",
):
    '''The ``AWS::Location::GeofenceCollection`` resource specifies the ability to detect and act when a tracked device enters or exits a defined geographical boundary known as a geofence.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html
    :cloudformationResource: AWS::Location::GeofenceCollection
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_location as location
        
        cfn_geofence_collection = location.CfnGeofenceCollection(self, "MyCfnGeofenceCollection",
            collection_name="collectionName",
        
            # the properties below are optional
            description="description",
            kms_key_id="kmsKeyId",
            pricing_plan="pricingPlan",
            pricing_plan_data_source="pricingPlanDataSource",
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
        collection_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        pricing_plan_data_source: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param collection_name: A custom name for the geofence collection. Requirements: - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). - Must be a unique geofence collection name. - No spaces allowed. For example, ``ExampleGeofenceCollection`` .
        :param description: An optional description for the geofence collection.
        :param kms_key_id: A key identifier for an `AWS KMS customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>`_ . Enter a key ID, key ARN, alias name, or alias ARN.
        :param pricing_plan: 
        :param pricing_plan_data_source: (deprecated) This shape is deprecated since 2022-02-01: Deprecated. No longer allowed.
        :param tags: Applies one or more tags to the geofence collection. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them. Format: ``"key" : "value"`` Restrictions: - Maximum 50 tags per resource - Each resource tag must be unique with a maximum of one value. - Maximum key length: 128 Unicode characters in UTF-8 - Maximum value length: 256 Unicode characters in UTF-8 - Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : /
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e0601ccc1fece7d46bccf997c94a7f51bea09a1590d5ce84823ed5c0b2041c1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGeofenceCollectionProps(
            collection_name=collection_name,
            description=description,
            kms_key_id=kms_key_id,
            pricing_plan=pricing_plan,
            pricing_plan_data_source=pricing_plan_data_source,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66134049825423372dae82a0ee8b8c0bba09bda09682513f80795605e6e0bca6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f4d7847226c9732be9ccaa062a530dac9299d5b10abbda476dd87dbeb44b817)
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
        '''The Amazon Resource Name (ARN) for the geofence collection resource.

        Used when you need to specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollectionArn")
    def attr_collection_arn(self) -> builtins.str:
        '''Synonym for ``Arn`` .

        The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection``

        :cloudformationAttribute: CollectionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollectionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''The timestamp for when the geofence collection resource was created in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''The timestamp for when the geofence collection resource was last updated in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

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
    @jsii.member(jsii_name="collectionName")
    def collection_name(self) -> builtins.str:
        '''A custom name for the geofence collection.'''
        return typing.cast(builtins.str, jsii.get(self, "collectionName"))

    @collection_name.setter
    def collection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e1fa37cb45ca3a446eacf95e0913ed3efd929171f9d39cc8468baf799adcc51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the geofence collection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cbd649bd3182fd4727374b07a6677a62cad5c3336b33bc5e81d0dce2c17e57d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''A key identifier for an `AWS KMS customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>`_ . Enter a key ID, key ARN, alias name, or alias ARN.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f66429d0739f2243b2062e0ca96d0b992ca5e6644989ca9e3620fec145d4c801)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''
        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeaf37bab42359e906370b69c4d7738d5d88e344697648948a0aafcf5751b8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlan", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlanDataSource")
    def pricing_plan_data_source(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This shape is deprecated since 2022-02-01: Deprecated.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlanDataSource"))

    @pricing_plan_data_source.setter
    def pricing_plan_data_source(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac440741201f7074f72462a372fb1e02f934a32f1d63e4645ed0506f4d874c8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlanDataSource", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Applies one or more tags to the geofence collection.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73c685a12991ff080fc342ecb024cac707829ec5c29f69506f34e69631875f71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_location.CfnGeofenceCollectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "collection_name": "collectionName",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "pricing_plan": "pricingPlan",
        "pricing_plan_data_source": "pricingPlanDataSource",
        "tags": "tags",
    },
)
class CfnGeofenceCollectionProps:
    def __init__(
        self,
        *,
        collection_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        pricing_plan_data_source: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGeofenceCollection``.

        :param collection_name: A custom name for the geofence collection. Requirements: - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). - Must be a unique geofence collection name. - No spaces allowed. For example, ``ExampleGeofenceCollection`` .
        :param description: An optional description for the geofence collection.
        :param kms_key_id: A key identifier for an `AWS KMS customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>`_ . Enter a key ID, key ARN, alias name, or alias ARN.
        :param pricing_plan: 
        :param pricing_plan_data_source: (deprecated) This shape is deprecated since 2022-02-01: Deprecated. No longer allowed.
        :param tags: Applies one or more tags to the geofence collection. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them. Format: ``"key" : "value"`` Restrictions: - Maximum 50 tags per resource - Each resource tag must be unique with a maximum of one value. - Maximum key length: 128 Unicode characters in UTF-8 - Maximum value length: 256 Unicode characters in UTF-8 - Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_location as location
            
            cfn_geofence_collection_props = location.CfnGeofenceCollectionProps(
                collection_name="collectionName",
            
                # the properties below are optional
                description="description",
                kms_key_id="kmsKeyId",
                pricing_plan="pricingPlan",
                pricing_plan_data_source="pricingPlanDataSource",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__307d0c98cf0385e786cd529fa95282bdfb460c6c7bb7e72dde3e3e36be5b809b)
            check_type(argname="argument collection_name", value=collection_name, expected_type=type_hints["collection_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument pricing_plan", value=pricing_plan, expected_type=type_hints["pricing_plan"])
            check_type(argname="argument pricing_plan_data_source", value=pricing_plan_data_source, expected_type=type_hints["pricing_plan_data_source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_name": collection_name,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if pricing_plan_data_source is not None:
            self._values["pricing_plan_data_source"] = pricing_plan_data_source
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def collection_name(self) -> builtins.str:
        '''A custom name for the geofence collection.

        Requirements:

        - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).
        - Must be a unique geofence collection name.
        - No spaces allowed. For example, ``ExampleGeofenceCollection`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-collectionname
        '''
        result = self._values.get("collection_name")
        assert result is not None, "Required property 'collection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the geofence collection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''A key identifier for an `AWS KMS customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>`_ . Enter a key ID, key ARN, alias name, or alias ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''
        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplan
        :stability: deprecated
        '''
        result = self._values.get("pricing_plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan_data_source(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This shape is deprecated since 2022-02-01: Deprecated.

        No longer allowed.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplandatasource
        :stability: deprecated
        '''
        result = self._values.get("pricing_plan_data_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Applies one or more tags to the geofence collection.

        A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.

        Format: ``"key" : "value"``

        Restrictions:

        - Maximum 50 tags per resource
        - Each resource tag must be unique with a maximum of one value.
        - Maximum key length: 128 Unicode characters in UTF-8
        - Maximum value length: 256 Unicode characters in UTF-8
        - Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-tags
        ::

        .

        - Cannot use "aws:" as a prefix for a key.
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGeofenceCollectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnMap(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_location.CfnMap",
):
    '''The ``AWS::Location::Map`` resource specifies a map resource in your AWS account, which provides map tiles of different styles sourced from global location data providers.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html
    :cloudformationResource: AWS::Location::Map
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_location as location
        
        cfn_map = location.CfnMap(self, "MyCfnMap",
            configuration=location.CfnMap.MapConfigurationProperty(
                style="style",
        
                # the properties below are optional
                custom_layers=["customLayers"],
                political_view="politicalView"
            ),
            map_name="mapName",
        
            # the properties below are optional
            description="description",
            pricing_plan="pricingPlan",
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
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMap.MapConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        map_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: Specifies the ``MapConfiguration`` , including the map style, for the map resource that you create. The map style defines the look of maps and the data provider for your map resource.
        :param map_name: The name for the map resource. Requirements: - Must contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). - Must be a unique map resource name. - No spaces allowed. For example, ``ExampleMap`` .
        :param description: An optional description for the map resource.
        :param pricing_plan: No longer used. If included, the only allowed value is ``RequestBasedUsage`` . *Allowed Values* : ``RequestBasedUsage``
        :param tags: Applies one or more tags to the map resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them. Format: ``"key" : "value"`` Restrictions: - Maximum 50 tags per resource - Each resource tag must be unique with a maximum of one value. - Maximum key length: 128 Unicode characters in UTF-8 - Maximum value length: 256 Unicode characters in UTF-8 - Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : /
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2dcb0428eb66932a1afc7be03e22130166237e903d48b7c13fc63dbc8f17b8a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMapProps(
            configuration=configuration,
            map_name=map_name,
            description=description,
            pricing_plan=pricing_plan,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9beda5dad2c7dda9e9e75c7563f1dd64ce2d95ee632f1f16c15c710cb2fcb9e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__23c81c05fd3d18494b5a67a26662df2ed22fb26a83114a2a0d33f71351eca462)
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
        '''The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:maps/ExampleMap``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''The timestamp for when the map resource was created in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrDataSource")
    def attr_data_source(self) -> builtins.str:
        '''
        :cloudformationAttribute: DataSource
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataSource"))

    @builtins.property
    @jsii.member(jsii_name="attrMapArn")
    def attr_map_arn(self) -> builtins.str:
        '''Synonym for ``Arn`` .

        The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:maps/ExampleMap``

        :cloudformationAttribute: MapArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMapArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''The timestamp for when the map resource was last updated in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

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
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnMap.MapConfigurationProperty"]:
        '''Specifies the ``MapConfiguration`` , including the map style, for the map resource that you create.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMap.MapConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnMap.MapConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a9f72d270eb9bf689ae6d9866174a230761748f72e7261987c4cc8c502029b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="mapName")
    def map_name(self) -> builtins.str:
        '''The name for the map resource.'''
        return typing.cast(builtins.str, jsii.get(self, "mapName"))

    @map_name.setter
    def map_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b14104c4a32a55719c593e2887df99cc3a37af1549a48dabd43c2e5d116df9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the map resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__031d91b8f14088e6516171c6244cb833bddde7d5749bd4d5e5ee39bfe0f17fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''No longer used.

        If included, the only allowed value is ``RequestBasedUsage`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de864d7ca8c9af6ca27a35f5fb304092560e41a384b9dd782f1dd78cc16953b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlan", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Applies one or more tags to the map resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb33fbdbbd66a87cdef71cb76784ef3bcdea2208fa231444865a3178588b36c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_location.CfnMap.MapConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "style": "style",
            "custom_layers": "customLayers",
            "political_view": "politicalView",
        },
    )
    class MapConfigurationProperty:
        def __init__(
            self,
            *,
            style: builtins.str,
            custom_layers: typing.Optional[typing.Sequence[builtins.str]] = None,
            political_view: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the map tile style selected from an available provider.

            :param style: Specifies the map style selected from an available data provider. Valid `Esri map styles <https://docs.aws.amazon.com/location/latest/developerguide/esri.html>`_ : - ``VectorEsriNavigation`` – The Esri Navigation map style, which provides a detailed basemap for the world symbolized with a custom navigation map style that's designed for use during the day in mobile devices. It also includes a richer set of places, such as shops, services, restaurants, attractions, and other points of interest. Enable the ``POI`` layer by setting it in CustomLayers to leverage the additional places data. - ``RasterEsriImagery`` – The Esri Imagery map style. A raster basemap that provides one meter or better satellite and aerial imagery in many parts of the world and lower resolution satellite imagery worldwide. - ``VectorEsriLightGrayCanvas`` – The Esri Light Gray Canvas map style, which provides a detailed vector basemap with a light gray, neutral background style with minimal colors, labels, and features that's designed to draw attention to your thematic content. - ``VectorEsriTopographic`` – The Esri Light map style, which provides a detailed vector basemap with a classic Esri map style. - ``VectorEsriStreets`` – The Esri Street Map style, which provides a detailed vector basemap for the world symbolized with a classic Esri street map style. The vector tile layer is similar in content and style to the World Street Map raster map. - ``VectorEsriDarkGrayCanvas`` – The Esri Dark Gray Canvas map style. A vector basemap with a dark gray, neutral background with minimal colors, labels, and features that's designed to draw attention to your thematic content. Valid `HERE Technologies map styles <https://docs.aws.amazon.com/location/latest/developerguide/HERE.html>`_ : - ``VectorHereExplore`` – A default HERE map style containing a neutral, global map and its features including roads, buildings, landmarks, and water features. It also now includes a fully designed map of Japan. - ``RasterHereExploreSatellite`` – A global map containing high resolution satellite imagery. - ``HybridHereExploreSatellite`` – A global map displaying the road network, street names, and city labels over satellite imagery. This style will automatically retrieve both raster and vector tiles, and your charges will be based on total tiles retrieved. .. epigraph:: Hybrid styles use both vector and raster tiles when rendering the map that you see. This means that more tiles are retrieved than when using either vector or raster tiles alone. Your charges will include all tiles retrieved. - ``VectorHereContrast`` – The HERE Contrast (Berlin) map style is a high contrast detailed base map of the world that blends 3D and 2D rendering. .. epigraph:: The ``VectorHereContrast`` style has been renamed from ``VectorHereBerlin`` . ``VectorHereBerlin`` has been deprecated, but will continue to work in applications that use it. - ``VectorHereExploreTruck`` – A global map containing truck restrictions and attributes (e.g. width / height / HAZMAT) symbolized with highlighted segments and icons on top of HERE Explore to support use cases within transport and logistics. Valid `GrabMaps map styles <https://docs.aws.amazon.com/location/latest/developerguide/grab.html>`_ : - ``VectorGrabStandardLight`` – The Grab Standard Light map style provides a basemap with detailed land use coloring, area names, roads, landmarks, and points of interest covering Southeast Asia. - ``VectorGrabStandardDark`` – The Grab Standard Dark map style provides a dark variation of the standard basemap covering Southeast Asia. .. epigraph:: Grab provides maps only for countries in Southeast Asia, and is only available in the Asia Pacific (Singapore) Region ( ``ap-southeast-1`` ). For more information, see `GrabMaps countries and area covered <https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area>`_ . Valid `Open Data map styles <https://docs.aws.amazon.com/location/latest/developerguide/open-data.html>`_ : - ``VectorOpenDataStandardLight`` – The Open Data Standard Light map style provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries. - ``VectorOpenDataStandardDark`` – Open Data Standard Dark is a dark-themed map style that provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries. - ``VectorOpenDataVisualizationLight`` – The Open Data Visualization Light map style is a light-themed style with muted colors and fewer features that aids in understanding overlaid data. - ``VectorOpenDataVisualizationDark`` – The Open Data Visualization Dark map style is a dark-themed style with muted colors and fewer features that aids in understanding overlaid data.
            :param custom_layers: Specifies the custom layers for the style. Leave unset to not enable any custom layer, or, for styles that support custom layers, you can enable layer(s), such as the ``POI`` layer for the VectorEsriNavigation style. .. epigraph:: Currenlty only ``VectorEsriNavigation`` supports CustomLayers. For more information, see `Custom Layers <https://docs.aws.amazon.com//location/latest/developerguide/map-concepts.html#map-custom-layers>`_ .
            :param political_view: Specifies the map political view selected from an available data provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_location as location
                
                map_configuration_property = location.CfnMap.MapConfigurationProperty(
                    style="style",
                
                    # the properties below are optional
                    custom_layers=["customLayers"],
                    political_view="politicalView"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f994438dc4a55ff175f7c8b92debb9548b8c21e2896a0380a521bcdba4e2a0d6)
                check_type(argname="argument style", value=style, expected_type=type_hints["style"])
                check_type(argname="argument custom_layers", value=custom_layers, expected_type=type_hints["custom_layers"])
                check_type(argname="argument political_view", value=political_view, expected_type=type_hints["political_view"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "style": style,
            }
            if custom_layers is not None:
                self._values["custom_layers"] = custom_layers
            if political_view is not None:
                self._values["political_view"] = political_view

        @builtins.property
        def style(self) -> builtins.str:
            '''Specifies the map style selected from an available data provider.

            Valid `Esri map styles <https://docs.aws.amazon.com/location/latest/developerguide/esri.html>`_ :

            - ``VectorEsriNavigation`` – The Esri Navigation map style, which provides a detailed basemap for the world symbolized with a custom navigation map style that's designed for use during the day in mobile devices. It also includes a richer set of places, such as shops, services, restaurants, attractions, and other points of interest. Enable the ``POI`` layer by setting it in CustomLayers to leverage the additional places data.
            - ``RasterEsriImagery`` – The Esri Imagery map style. A raster basemap that provides one meter or better satellite and aerial imagery in many parts of the world and lower resolution satellite imagery worldwide.
            - ``VectorEsriLightGrayCanvas`` – The Esri Light Gray Canvas map style, which provides a detailed vector basemap with a light gray, neutral background style with minimal colors, labels, and features that's designed to draw attention to your thematic content.
            - ``VectorEsriTopographic`` – The Esri Light map style, which provides a detailed vector basemap with a classic Esri map style.
            - ``VectorEsriStreets`` – The Esri Street Map style, which provides a detailed vector basemap for the world symbolized with a classic Esri street map style. The vector tile layer is similar in content and style to the World Street Map raster map.
            - ``VectorEsriDarkGrayCanvas`` – The Esri Dark Gray Canvas map style. A vector basemap with a dark gray, neutral background with minimal colors, labels, and features that's designed to draw attention to your thematic content.

            Valid `HERE Technologies map styles <https://docs.aws.amazon.com/location/latest/developerguide/HERE.html>`_ :

            - ``VectorHereExplore`` – A default HERE map style containing a neutral, global map and its features including roads, buildings, landmarks, and water features. It also now includes a fully designed map of Japan.
            - ``RasterHereExploreSatellite`` – A global map containing high resolution satellite imagery.
            - ``HybridHereExploreSatellite`` – A global map displaying the road network, street names, and city labels over satellite imagery. This style will automatically retrieve both raster and vector tiles, and your charges will be based on total tiles retrieved.

            .. epigraph::

               Hybrid styles use both vector and raster tiles when rendering the map that you see. This means that more tiles are retrieved than when using either vector or raster tiles alone. Your charges will include all tiles retrieved.

            - ``VectorHereContrast`` – The HERE Contrast (Berlin) map style is a high contrast detailed base map of the world that blends 3D and 2D rendering.

            .. epigraph::

               The ``VectorHereContrast`` style has been renamed from ``VectorHereBerlin`` . ``VectorHereBerlin`` has been deprecated, but will continue to work in applications that use it.

            - ``VectorHereExploreTruck`` – A global map containing truck restrictions and attributes (e.g. width / height / HAZMAT) symbolized with highlighted segments and icons on top of HERE Explore to support use cases within transport and logistics.

            Valid `GrabMaps map styles <https://docs.aws.amazon.com/location/latest/developerguide/grab.html>`_ :

            - ``VectorGrabStandardLight`` – The Grab Standard Light map style provides a basemap with detailed land use coloring, area names, roads, landmarks, and points of interest covering Southeast Asia.
            - ``VectorGrabStandardDark`` – The Grab Standard Dark map style provides a dark variation of the standard basemap covering Southeast Asia.

            .. epigraph::

               Grab provides maps only for countries in Southeast Asia, and is only available in the Asia Pacific (Singapore) Region ( ``ap-southeast-1`` ). For more information, see `GrabMaps countries and area covered <https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area>`_ .

            Valid `Open Data map styles <https://docs.aws.amazon.com/location/latest/developerguide/open-data.html>`_ :

            - ``VectorOpenDataStandardLight`` – The Open Data Standard Light map style provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.
            - ``VectorOpenDataStandardDark`` – Open Data Standard Dark is a dark-themed map style that provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.
            - ``VectorOpenDataVisualizationLight`` – The Open Data Visualization Light map style is a light-themed style with muted colors and fewer features that aids in understanding overlaid data.
            - ``VectorOpenDataVisualizationDark`` – The Open Data Visualization Dark map style is a dark-themed style with muted colors and fewer features that aids in understanding overlaid data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html#cfn-location-map-mapconfiguration-style
            '''
            result = self._values.get("style")
            assert result is not None, "Required property 'style' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def custom_layers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the custom layers for the style.

            Leave unset to not enable any custom layer, or, for styles that support custom layers, you can enable layer(s), such as the ``POI`` layer for the VectorEsriNavigation style.
            .. epigraph::

               Currenlty only ``VectorEsriNavigation`` supports CustomLayers. For more information, see `Custom Layers <https://docs.aws.amazon.com//location/latest/developerguide/map-concepts.html#map-custom-layers>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html#cfn-location-map-mapconfiguration-customlayers
            '''
            result = self._values.get("custom_layers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def political_view(self) -> typing.Optional[builtins.str]:
            '''Specifies the map political view selected from an available data provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html#cfn-location-map-mapconfiguration-politicalview
            '''
            result = self._values.get("political_view")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MapConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_location.CfnMapProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "map_name": "mapName",
        "description": "description",
        "pricing_plan": "pricingPlan",
        "tags": "tags",
    },
)
class CfnMapProps:
    def __init__(
        self,
        *,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMap.MapConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        map_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMap``.

        :param configuration: Specifies the ``MapConfiguration`` , including the map style, for the map resource that you create. The map style defines the look of maps and the data provider for your map resource.
        :param map_name: The name for the map resource. Requirements: - Must contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). - Must be a unique map resource name. - No spaces allowed. For example, ``ExampleMap`` .
        :param description: An optional description for the map resource.
        :param pricing_plan: No longer used. If included, the only allowed value is ``RequestBasedUsage`` . *Allowed Values* : ``RequestBasedUsage``
        :param tags: Applies one or more tags to the map resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them. Format: ``"key" : "value"`` Restrictions: - Maximum 50 tags per resource - Each resource tag must be unique with a maximum of one value. - Maximum key length: 128 Unicode characters in UTF-8 - Maximum value length: 256 Unicode characters in UTF-8 - Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_location as location
            
            cfn_map_props = location.CfnMapProps(
                configuration=location.CfnMap.MapConfigurationProperty(
                    style="style",
            
                    # the properties below are optional
                    custom_layers=["customLayers"],
                    political_view="politicalView"
                ),
                map_name="mapName",
            
                # the properties below are optional
                description="description",
                pricing_plan="pricingPlan",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__702a4eb1b8c53d553ad5479cf127f6ed1090248f0a9d4806eec0b368c1165ea8)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument map_name", value=map_name, expected_type=type_hints["map_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument pricing_plan", value=pricing_plan, expected_type=type_hints["pricing_plan"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "map_name": map_name,
        }
        if description is not None:
            self._values["description"] = description
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnMap.MapConfigurationProperty]:
        '''Specifies the ``MapConfiguration`` , including the map style, for the map resource that you create.

        The map style defines the look of maps and the data provider for your map resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnMap.MapConfigurationProperty], result)

    @builtins.property
    def map_name(self) -> builtins.str:
        '''The name for the map resource.

        Requirements:

        - Must contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).
        - Must be a unique map resource name.
        - No spaces allowed. For example, ``ExampleMap`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-mapname
        '''
        result = self._values.get("map_name")
        assert result is not None, "Required property 'map_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the map resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''No longer used. If included, the only allowed value is ``RequestBasedUsage`` .

        *Allowed Values* : ``RequestBasedUsage``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-pricingplan
        '''
        result = self._values.get("pricing_plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Applies one or more tags to the map resource.

        A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.

        Format: ``"key" : "value"``

        Restrictions:

        - Maximum 50 tags per resource
        - Each resource tag must be unique with a maximum of one value.
        - Maximum key length: 128 Unicode characters in UTF-8
        - Maximum value length: 256 Unicode characters in UTF-8
        - Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-tags
        ::

        .

        - Cannot use "aws:" as a prefix for a key.
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMapProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPlaceIndex(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_location.CfnPlaceIndex",
):
    '''Specifies a place index resource in your AWS account.

    Use a place index resource to geocode addresses and other text queries by using the ``SearchPlaceIndexForText`` operation, and reverse geocode coordinates by using the ``SearchPlaceIndexForPosition`` operation, and enable autosuggestions by using the ``SearchPlaceIndexForSuggestions`` operation.
    .. epigraph::

       If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the `AWS service terms <https://docs.aws.amazon.com/service-terms>`_ for more details.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html
    :cloudformationResource: AWS::Location::PlaceIndex
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_location as location
        
        cfn_place_index = location.CfnPlaceIndex(self, "MyCfnPlaceIndex",
            data_source="dataSource",
            index_name="indexName",
        
            # the properties below are optional
            data_source_configuration=location.CfnPlaceIndex.DataSourceConfigurationProperty(
                intended_use="intendedUse"
            ),
            description="description",
            pricing_plan="pricingPlan",
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
        data_source: builtins.str,
        index_name: builtins.str,
        data_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlaceIndex.DataSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_source: Specifies the geospatial data provider for the new place index. .. epigraph:: This field is case-sensitive. Enter the valid values as shown. For example, entering ``HERE`` returns an error. Valid values include: - ``Esri`` – For additional information about `Esri <https://docs.aws.amazon.com/location/latest/developerguide/esri.html>`_ 's coverage in your region of interest, see `Esri details on geocoding coverage <https://docs.aws.amazon.com/https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm>`_ . - ``Grab`` – Grab provides place index functionality for Southeast Asia. For additional information about `GrabMaps <https://docs.aws.amazon.com/location/latest/developerguide/grab.html>`_ ' coverage, see `GrabMaps countries and areas covered <https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area>`_ . - ``Here`` – For additional information about `HERE Technologies <https://docs.aws.amazon.com/location/latest/developerguide/HERE.html>`_ ' coverage in your region of interest, see `HERE details on goecoding coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html>`_ . .. epigraph:: If you specify HERE Technologies ( ``Here`` ) as the data provider, you may not `store results <https://docs.aws.amazon.com//location-places/latest/APIReference/API_DataSourceConfiguration.html>`_ for locations in Japan. For more information, see the `AWS Service Terms <https://docs.aws.amazon.com/service-terms/>`_ for Amazon Location Service. For additional information , see `Data providers <https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html>`_ on the *Amazon Location Service Developer Guide* .
        :param index_name: The name of the place index resource. Requirements: - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). - Must be a unique place index resource name. - No spaces allowed. For example, ``ExamplePlaceIndex`` .
        :param data_source_configuration: Specifies the data storage option requesting Places.
        :param description: The optional description for the place index resource.
        :param pricing_plan: No longer used. If included, the only allowed value is ``RequestBasedUsage`` . *Allowed Values* : ``RequestBasedUsage``
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86efa72874938a7fdd56ee75ab5f3481754256c4e7be12dd321fb8179b36168)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlaceIndexProps(
            data_source=data_source,
            index_name=index_name,
            data_source_configuration=data_source_configuration,
            description=description,
            pricing_plan=pricing_plan,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0c405c6a922a2896cb59706744382d2e74f7b74e7533c5078a63a01a0dda7f8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6e6a62d57c55981d2561a3c18c99b7b68c42dd787f2ac2a05ef607b0d5c38be)
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
        '''The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across AWS .

        - Format example: ``arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''The timestamp for when the place index resource was created in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrIndexArn")
    def attr_index_arn(self) -> builtins.str:
        '''Synonym for ``Arn`` .

        The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across AWS .

        - Format example: ``arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex``

        :cloudformationAttribute: IndexArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIndexArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''The timestamp for when the place index resource was last updated in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

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
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        '''Specifies the geospatial data provider for the new place index.'''
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7c1c6b9a81b0a961b6426f41c459172924ee226a1266f2c09e8bcee9f894dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSource", value)

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> builtins.str:
        '''The name of the place index resource.'''
        return typing.cast(builtins.str, jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80848c256675ce5115c146bfbde42fded11406ee451376e49955461fb6004b75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceConfiguration")
    def data_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlaceIndex.DataSourceConfigurationProperty"]]:
        '''Specifies the data storage option requesting Places.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlaceIndex.DataSourceConfigurationProperty"]], jsii.get(self, "dataSourceConfiguration"))

    @data_source_configuration.setter
    def data_source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlaceIndex.DataSourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4cff8053f28ed6073e2b7c62ec72627c8ffc7b98c86bc2b7c5c4e9b177d8d4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The optional description for the place index resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a59366c5536e4867cad1dd1e53981208d2606343698315f4ecfbe50ac0be1c27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''No longer used.

        If included, the only allowed value is ``RequestBasedUsage`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7653a99bc2f680ec231d78959d16db4997e472e731a68a554772f0e08b4fd925)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlan", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a88e3fcbc3fba96f937cf7669a81dcdb84f3dce7ddea1dd5143fcf5e7eaeb70e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_location.CfnPlaceIndex.DataSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"intended_use": "intendedUse"},
    )
    class DataSourceConfigurationProperty:
        def __init__(
            self,
            *,
            intended_use: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the data storage option requesting Places.

            :param intended_use: Specifies how the results of an operation will be stored by the caller. Valid values include: - ``SingleUse`` specifies that the results won't be stored. - ``Storage`` specifies that the result can be cached or stored in a database. Default value: ``SingleUse``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_location as location
                
                data_source_configuration_property = location.CfnPlaceIndex.DataSourceConfigurationProperty(
                    intended_use="intendedUse"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b631c3e00c6906f33efa721d356034e81e693d6aa037787fadb69355eaa4ef41)
                check_type(argname="argument intended_use", value=intended_use, expected_type=type_hints["intended_use"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if intended_use is not None:
                self._values["intended_use"] = intended_use

        @builtins.property
        def intended_use(self) -> typing.Optional[builtins.str]:
            '''Specifies how the results of an operation will be stored by the caller.

            Valid values include:

            - ``SingleUse`` specifies that the results won't be stored.
            - ``Storage`` specifies that the result can be cached or stored in a database.

            Default value: ``SingleUse``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html#cfn-location-placeindex-datasourceconfiguration-intendeduse
            '''
            result = self._values.get("intended_use")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_location.CfnPlaceIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_source": "dataSource",
        "index_name": "indexName",
        "data_source_configuration": "dataSourceConfiguration",
        "description": "description",
        "pricing_plan": "pricingPlan",
        "tags": "tags",
    },
)
class CfnPlaceIndexProps:
    def __init__(
        self,
        *,
        data_source: builtins.str,
        index_name: builtins.str,
        data_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlaceIndex.DataSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlaceIndex``.

        :param data_source: Specifies the geospatial data provider for the new place index. .. epigraph:: This field is case-sensitive. Enter the valid values as shown. For example, entering ``HERE`` returns an error. Valid values include: - ``Esri`` – For additional information about `Esri <https://docs.aws.amazon.com/location/latest/developerguide/esri.html>`_ 's coverage in your region of interest, see `Esri details on geocoding coverage <https://docs.aws.amazon.com/https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm>`_ . - ``Grab`` – Grab provides place index functionality for Southeast Asia. For additional information about `GrabMaps <https://docs.aws.amazon.com/location/latest/developerguide/grab.html>`_ ' coverage, see `GrabMaps countries and areas covered <https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area>`_ . - ``Here`` – For additional information about `HERE Technologies <https://docs.aws.amazon.com/location/latest/developerguide/HERE.html>`_ ' coverage in your region of interest, see `HERE details on goecoding coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html>`_ . .. epigraph:: If you specify HERE Technologies ( ``Here`` ) as the data provider, you may not `store results <https://docs.aws.amazon.com//location-places/latest/APIReference/API_DataSourceConfiguration.html>`_ for locations in Japan. For more information, see the `AWS Service Terms <https://docs.aws.amazon.com/service-terms/>`_ for Amazon Location Service. For additional information , see `Data providers <https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html>`_ on the *Amazon Location Service Developer Guide* .
        :param index_name: The name of the place index resource. Requirements: - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). - Must be a unique place index resource name. - No spaces allowed. For example, ``ExamplePlaceIndex`` .
        :param data_source_configuration: Specifies the data storage option requesting Places.
        :param description: The optional description for the place index resource.
        :param pricing_plan: No longer used. If included, the only allowed value is ``RequestBasedUsage`` . *Allowed Values* : ``RequestBasedUsage``
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_location as location
            
            cfn_place_index_props = location.CfnPlaceIndexProps(
                data_source="dataSource",
                index_name="indexName",
            
                # the properties below are optional
                data_source_configuration=location.CfnPlaceIndex.DataSourceConfigurationProperty(
                    intended_use="intendedUse"
                ),
                description="description",
                pricing_plan="pricingPlan",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa21f8e355faff509cae18242ebc62f8af877465a5ef051abbedc5885bb64cd4)
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument data_source_configuration", value=data_source_configuration, expected_type=type_hints["data_source_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument pricing_plan", value=pricing_plan, expected_type=type_hints["pricing_plan"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source": data_source,
            "index_name": index_name,
        }
        if data_source_configuration is not None:
            self._values["data_source_configuration"] = data_source_configuration
        if description is not None:
            self._values["description"] = description
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_source(self) -> builtins.str:
        '''Specifies the geospatial data provider for the new place index.

        .. epigraph::

           This field is case-sensitive. Enter the valid values as shown. For example, entering ``HERE`` returns an error.

        Valid values include:

        - ``Esri`` – For additional information about `Esri <https://docs.aws.amazon.com/location/latest/developerguide/esri.html>`_ 's coverage in your region of interest, see `Esri details on geocoding coverage <https://docs.aws.amazon.com/https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm>`_ .
        - ``Grab`` – Grab provides place index functionality for Southeast Asia. For additional information about `GrabMaps <https://docs.aws.amazon.com/location/latest/developerguide/grab.html>`_ ' coverage, see `GrabMaps countries and areas covered <https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area>`_ .
        - ``Here`` – For additional information about `HERE Technologies <https://docs.aws.amazon.com/location/latest/developerguide/HERE.html>`_ ' coverage in your region of interest, see `HERE details on goecoding coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html>`_ .

        .. epigraph::

           If you specify HERE Technologies ( ``Here`` ) as the data provider, you may not `store results <https://docs.aws.amazon.com//location-places/latest/APIReference/API_DataSourceConfiguration.html>`_ for locations in Japan. For more information, see the `AWS Service Terms <https://docs.aws.amazon.com/service-terms/>`_ for Amazon Location Service.

        For additional information , see `Data providers <https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html>`_ on the *Amazon Location Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasource
        '''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_name(self) -> builtins.str:
        '''The name of the place index resource.

        Requirements:

        - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).
        - Must be a unique place index resource name.
        - No spaces allowed. For example, ``ExamplePlaceIndex`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-indexname
        '''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPlaceIndex.DataSourceConfigurationProperty]]:
        '''Specifies the data storage option requesting Places.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasourceconfiguration
        '''
        result = self._values.get("data_source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPlaceIndex.DataSourceConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The optional description for the place index resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''No longer used. If included, the only allowed value is ``RequestBasedUsage`` .

        *Allowed Values* : ``RequestBasedUsage``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-pricingplan
        '''
        result = self._values.get("pricing_plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlaceIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnRouteCalculator(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_location.CfnRouteCalculator",
):
    '''Specifies a route calculator resource in your AWS account.

    You can send requests to a route calculator resource to estimate travel time, distance, and get directions. A route calculator sources traffic and road network data from your chosen data provider.
    .. epigraph::

       If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the `AWS service terms <https://docs.aws.amazon.com/service-terms>`_ for more details.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html
    :cloudformationResource: AWS::Location::RouteCalculator
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_location as location
        
        cfn_route_calculator = location.CfnRouteCalculator(self, "MyCfnRouteCalculator",
            calculator_name="calculatorName",
            data_source="dataSource",
        
            # the properties below are optional
            description="description",
            pricing_plan="pricingPlan",
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
        calculator_name: builtins.str,
        data_source: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param calculator_name: The name of the route calculator resource. Requirements: - Can use alphanumeric characters (A–Z, a–z, 0–9) , hyphens (-), periods (.), and underscores (_). - Must be a unique Route calculator resource name. - No spaces allowed. For example, ``ExampleRouteCalculator`` .
        :param data_source: Specifies the data provider of traffic and road network data. .. epigraph:: This field is case-sensitive. Enter the valid values as shown. For example, entering ``HERE`` returns an error. Valid values include: - ``Esri`` – For additional information about `Esri <https://docs.aws.amazon.com/location/latest/developerguide/esri.html>`_ 's coverage in your region of interest, see `Esri details on street networks and traffic coverage <https://docs.aws.amazon.com/https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm>`_ . Route calculators that use Esri as a data source only calculate routes that are shorter than 400 km. - ``Grab`` – Grab provides routing functionality for Southeast Asia. For additional information about `GrabMaps <https://docs.aws.amazon.com/location/latest/developerguide/grab.html>`_ ' coverage, see `GrabMaps countries and areas covered <https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area>`_ . - ``Here`` – For additional information about `HERE Technologies <https://docs.aws.amazon.com/location/latest/developerguide/HERE.html>`_ ' coverage in your region of interest, see `HERE car routing coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html>`_ and `HERE truck routing coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html>`_ . For additional information , see `Data providers <https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html>`_ on the *Amazon Location Service Developer Guide* .
        :param description: The optional description for the route calculator resource.
        :param pricing_plan: No longer used. If included, the only allowed value is ``RequestBasedUsage`` . *Allowed Values* : ``RequestBasedUsage``
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a900f380dbd4e0012dcb474730041f91eeaecc9218db4d6163fd730394a66f3a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRouteCalculatorProps(
            calculator_name=calculator_name,
            data_source=data_source,
            description=description,
            pricing_plan=pricing_plan,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0f206fe9bb875d2c7acae9be0a23fa0286ad54fbd1bebff69010a95bea15fec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c6188d22ee31496bd1f61ea15dd8d141313349058c043549fd0dad11d02a49b)
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
        '''The Amazon Resource Name (ARN) for the route calculator resource.

        Use the ARN when you specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:route-calculator/ExampleCalculator``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCalculatorArn")
    def attr_calculator_arn(self) -> builtins.str:
        '''Synonym for ``Arn`` .

        The Amazon Resource Name (ARN) for the route calculator resource. Use the ARN when you specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:route-calculator/ExampleCalculator``

        :cloudformationAttribute: CalculatorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCalculatorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''The timestamp for when the route calculator resource was created in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''The timestamp for when the route calculator resource was last updated in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

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
    @jsii.member(jsii_name="calculatorName")
    def calculator_name(self) -> builtins.str:
        '''The name of the route calculator resource.'''
        return typing.cast(builtins.str, jsii.get(self, "calculatorName"))

    @calculator_name.setter
    def calculator_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9501128c2291eb0596cb61fa914f8f1f6ceb251748807dce9d7b778f46355373)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "calculatorName", value)

    @builtins.property
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        '''Specifies the data provider of traffic and road network data.'''
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__facb0538b630afd7ae0f1a08a48d6f92e23fb00dc53fd3e9bdedc88b3e17b6b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSource", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The optional description for the route calculator resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d88fc3920b0a8018d893998ecb23006fd6c84ebcc44e8ca60c506b79ade39568)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''No longer used.

        If included, the only allowed value is ``RequestBasedUsage`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f40cb810c37a798bfec946670c6e7a33c338d2fe035b50de2d1bee9b1485bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlan", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74454734a6df8a4308849a60f8d80541ab1a10fc08d73d9f6faa0474841ec604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_location.CfnRouteCalculatorProps",
    jsii_struct_bases=[],
    name_mapping={
        "calculator_name": "calculatorName",
        "data_source": "dataSource",
        "description": "description",
        "pricing_plan": "pricingPlan",
        "tags": "tags",
    },
)
class CfnRouteCalculatorProps:
    def __init__(
        self,
        *,
        calculator_name: builtins.str,
        data_source: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRouteCalculator``.

        :param calculator_name: The name of the route calculator resource. Requirements: - Can use alphanumeric characters (A–Z, a–z, 0–9) , hyphens (-), periods (.), and underscores (_). - Must be a unique Route calculator resource name. - No spaces allowed. For example, ``ExampleRouteCalculator`` .
        :param data_source: Specifies the data provider of traffic and road network data. .. epigraph:: This field is case-sensitive. Enter the valid values as shown. For example, entering ``HERE`` returns an error. Valid values include: - ``Esri`` – For additional information about `Esri <https://docs.aws.amazon.com/location/latest/developerguide/esri.html>`_ 's coverage in your region of interest, see `Esri details on street networks and traffic coverage <https://docs.aws.amazon.com/https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm>`_ . Route calculators that use Esri as a data source only calculate routes that are shorter than 400 km. - ``Grab`` – Grab provides routing functionality for Southeast Asia. For additional information about `GrabMaps <https://docs.aws.amazon.com/location/latest/developerguide/grab.html>`_ ' coverage, see `GrabMaps countries and areas covered <https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area>`_ . - ``Here`` – For additional information about `HERE Technologies <https://docs.aws.amazon.com/location/latest/developerguide/HERE.html>`_ ' coverage in your region of interest, see `HERE car routing coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html>`_ and `HERE truck routing coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html>`_ . For additional information , see `Data providers <https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html>`_ on the *Amazon Location Service Developer Guide* .
        :param description: The optional description for the route calculator resource.
        :param pricing_plan: No longer used. If included, the only allowed value is ``RequestBasedUsage`` . *Allowed Values* : ``RequestBasedUsage``
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_location as location
            
            cfn_route_calculator_props = location.CfnRouteCalculatorProps(
                calculator_name="calculatorName",
                data_source="dataSource",
            
                # the properties below are optional
                description="description",
                pricing_plan="pricingPlan",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986eaab9e9d4b82fd7bedac19af61096151542baed90ee4afaad1d66b4b219c9)
            check_type(argname="argument calculator_name", value=calculator_name, expected_type=type_hints["calculator_name"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument pricing_plan", value=pricing_plan, expected_type=type_hints["pricing_plan"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "calculator_name": calculator_name,
            "data_source": data_source,
        }
        if description is not None:
            self._values["description"] = description
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def calculator_name(self) -> builtins.str:
        '''The name of the route calculator resource.

        Requirements:

        - Can use alphanumeric characters (A–Z, a–z, 0–9) , hyphens (-), periods (.), and underscores (_).
        - Must be a unique Route calculator resource name.
        - No spaces allowed. For example, ``ExampleRouteCalculator`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-calculatorname
        '''
        result = self._values.get("calculator_name")
        assert result is not None, "Required property 'calculator_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source(self) -> builtins.str:
        '''Specifies the data provider of traffic and road network data.

        .. epigraph::

           This field is case-sensitive. Enter the valid values as shown. For example, entering ``HERE`` returns an error.

        Valid values include:

        - ``Esri`` – For additional information about `Esri <https://docs.aws.amazon.com/location/latest/developerguide/esri.html>`_ 's coverage in your region of interest, see `Esri details on street networks and traffic coverage <https://docs.aws.amazon.com/https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm>`_ .

        Route calculators that use Esri as a data source only calculate routes that are shorter than 400 km.

        - ``Grab`` – Grab provides routing functionality for Southeast Asia. For additional information about `GrabMaps <https://docs.aws.amazon.com/location/latest/developerguide/grab.html>`_ ' coverage, see `GrabMaps countries and areas covered <https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area>`_ .
        - ``Here`` – For additional information about `HERE Technologies <https://docs.aws.amazon.com/location/latest/developerguide/HERE.html>`_ ' coverage in your region of interest, see `HERE car routing coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html>`_ and `HERE truck routing coverage <https://docs.aws.amazon.com/https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html>`_ .

        For additional information , see `Data providers <https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html>`_ on the *Amazon Location Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-datasource
        '''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The optional description for the route calculator resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''No longer used. If included, the only allowed value is ``RequestBasedUsage`` .

        *Allowed Values* : ``RequestBasedUsage``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-pricingplan
        '''
        result = self._values.get("pricing_plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouteCalculatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTracker(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_location.CfnTracker",
):
    '''Specifies a tracker resource in your AWS account , which lets you receive current and historical location of devices.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html
    :cloudformationResource: AWS::Location::Tracker
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_location as location
        
        cfn_tracker = location.CfnTracker(self, "MyCfnTracker",
            tracker_name="trackerName",
        
            # the properties below are optional
            description="description",
            event_bridge_enabled=False,
            kms_key_enable_geospatial_queries=False,
            kms_key_id="kmsKeyId",
            position_filtering="positionFiltering",
            pricing_plan="pricingPlan",
            pricing_plan_data_source="pricingPlanDataSource",
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
        tracker_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        event_bridge_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_key_enable_geospatial_queries: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        position_filtering: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        pricing_plan_data_source: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param tracker_name: The name for the tracker resource. Requirements: - Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_). - Must be a unique tracker resource name. - No spaces allowed. For example, ``ExampleTracker`` .
        :param description: An optional description for the tracker resource.
        :param event_bridge_enabled: 
        :param kms_key_enable_geospatial_queries: 
        :param kms_key_id: A key identifier for an `AWS KMS customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>`_ . Enter a key ID, key ARN, alias name, or alias ARN.
        :param position_filtering: Specifies the position filtering for the tracker resource. Valid values: - ``TimeBased`` - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID. - ``DistanceBased`` - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this area are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map. - ``AccuracyBased`` - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This can reduce the effects of GPS noise when displaying device trajectories on a map, and can help control your costs by reducing the number of geofence evaluations. This field is optional. If not specified, the default value is ``TimeBased`` .
        :param pricing_plan: 
        :param pricing_plan_data_source: (deprecated) This shape is deprecated since 2022-02-01: Deprecated. No longer allowed.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cd2e07bf97c42a45f9443da7edf34b075c2f9b41a262ae77aee4b2a82a30dc0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTrackerProps(
            tracker_name=tracker_name,
            description=description,
            event_bridge_enabled=event_bridge_enabled,
            kms_key_enable_geospatial_queries=kms_key_enable_geospatial_queries,
            kms_key_id=kms_key_id,
            position_filtering=position_filtering,
            pricing_plan=pricing_plan,
            pricing_plan_data_source=pricing_plan_data_source,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__606edf93b66473926b20e5a3b0af67fe5ed3f2fceae488ca1b2486f74e9beeb4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1045c636e6d3b0f9dcbb0a4661afd9d9bfe2912562fdba49a3e87a5d8e522f9)
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
        '''The Amazon Resource Name (ARN) for the tracker resource.

        Used when you need to specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:tracker/ExampleTracker``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''The timestamp for when the tracker resource was created in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrTrackerArn")
    def attr_tracker_arn(self) -> builtins.str:
        '''Synonym for ``Arn`` .

        The Amazon Resource Name (ARN) for the tracker resource. Used when you need to specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:tracker/ExampleTracker``

        :cloudformationAttribute: TrackerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTrackerArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''The timestamp for when the tracker resource was last updated in `ISO 8601 <https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html>`_ format: ``YYYY-MM-DDThh:mm:ss.sssZ`` .

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

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
    @jsii.member(jsii_name="trackerName")
    def tracker_name(self) -> builtins.str:
        '''The name for the tracker resource.'''
        return typing.cast(builtins.str, jsii.get(self, "trackerName"))

    @tracker_name.setter
    def tracker_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704fbf855c65f61aeff35b9fcc74d9758e51af0bbee363ab356fea2602f904b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackerName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the tracker resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__432656f1a3249889b4f6340d433951d4b03ec382b366b9cefc7f22db81828ad3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="eventBridgeEnabled")
    def event_bridge_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "eventBridgeEnabled"))

    @event_bridge_enabled.setter
    def event_bridge_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd4f7477042ce6ed75f0b9861b25a721854ba28f82072db60305830e07af0d42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBridgeEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyEnableGeospatialQueries")
    def kms_key_enable_geospatial_queries(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "kmsKeyEnableGeospatialQueries"))

    @kms_key_enable_geospatial_queries.setter
    def kms_key_enable_geospatial_queries(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2dd571749bac14762477ff49a8f135c7d6e5b9f96b1f45fdb2f11d55be863ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyEnableGeospatialQueries", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''A key identifier for an `AWS KMS customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>`_ . Enter a key ID, key ARN, alias name, or alias ARN.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcc29257a761669c6cc236364e363b6512c47005e61ff4201e14badc85d4b49d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="positionFiltering")
    def position_filtering(self) -> typing.Optional[builtins.str]:
        '''Specifies the position filtering for the tracker resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "positionFiltering"))

    @position_filtering.setter
    def position_filtering(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7f9e9ee70dc0e0f484224b53e37f910ac2fe681564c2ba665fb49c1f326e222)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "positionFiltering", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''
        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6ef71bd19b0038f0b7a053221674f1b6d79138bfb1150915529c7b0aefe900f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlan", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlanDataSource")
    def pricing_plan_data_source(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This shape is deprecated since 2022-02-01: Deprecated.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlanDataSource"))

    @pricing_plan_data_source.setter
    def pricing_plan_data_source(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9f5b36993f4be81b2285747fed230ab9182b4393ef3b93d823765df23324c4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlanDataSource", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd4f1b9ba5c51ac5a38d0876f790c1137595037fec38c3aacc1dd70bc872c126)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.implements(_IInspectable_c2943556)
class CfnTrackerConsumer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_location.CfnTrackerConsumer",
):
    '''The ``AWS::Location::TrackerConsumer`` resource specifies an association between a geofence collection and a tracker resource.

    The geofence collection is referred to as the *consumer* of the tracker. This allows the tracker resource to communicate location data to the linked geofence collection.
    .. epigraph::

       Currently not supported — Cross-account configurations, such as creating associations between a tracker resource in one account and a geofence collection in another account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html
    :cloudformationResource: AWS::Location::TrackerConsumer
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_location as location
        
        cfn_tracker_consumer = location.CfnTrackerConsumer(self, "MyCfnTrackerConsumer",
            consumer_arn="consumerArn",
            tracker_name="trackerName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        consumer_arn: builtins.str,
        tracker_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param consumer_arn: The Amazon Resource Name (ARN) for the geofence collection to be associated to tracker resource. Used when you need to specify a resource across all AWS . - Format example: ``arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer``
        :param tracker_name: The name for the tracker resource. Requirements: - Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_). - Must be a unique tracker resource name. - No spaces allowed. For example, ``ExampleTracker`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796f07ade0c1c21cf2be739abf72847e038c9c0f1fe6e69286fa0b51df24a022)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTrackerConsumerProps(
            consumer_arn=consumer_arn, tracker_name=tracker_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7cf03d6794740801a069f1fdfdefcd95ab283d7bba980f64a30bc78e1155809)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db67e253b286d87476fb1aa3fa7c47f96dc2e0d9269d323e1ca1f4c17fb60c85)
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
    @jsii.member(jsii_name="consumerArn")
    def consumer_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the geofence collection to be associated to tracker resource.'''
        return typing.cast(builtins.str, jsii.get(self, "consumerArn"))

    @consumer_arn.setter
    def consumer_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3101704451bf83d25aae3a96e950bccc978a403a238456dffbfa02203f3d5fad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerArn", value)

    @builtins.property
    @jsii.member(jsii_name="trackerName")
    def tracker_name(self) -> builtins.str:
        '''The name for the tracker resource.'''
        return typing.cast(builtins.str, jsii.get(self, "trackerName"))

    @tracker_name.setter
    def tracker_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa34370ea71108b33b5119b9fcb8ca5029e1349c5ec4e2fb3d74745ed6952b4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackerName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_location.CfnTrackerConsumerProps",
    jsii_struct_bases=[],
    name_mapping={"consumer_arn": "consumerArn", "tracker_name": "trackerName"},
)
class CfnTrackerConsumerProps:
    def __init__(
        self,
        *,
        consumer_arn: builtins.str,
        tracker_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnTrackerConsumer``.

        :param consumer_arn: The Amazon Resource Name (ARN) for the geofence collection to be associated to tracker resource. Used when you need to specify a resource across all AWS . - Format example: ``arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer``
        :param tracker_name: The name for the tracker resource. Requirements: - Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_). - Must be a unique tracker resource name. - No spaces allowed. For example, ``ExampleTracker`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_location as location
            
            cfn_tracker_consumer_props = location.CfnTrackerConsumerProps(
                consumer_arn="consumerArn",
                tracker_name="trackerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c4f2c66be9e9a4dcfdb7c07a9f472259b9cfbd8f7d951a99362fad4aecdf9d8)
            check_type(argname="argument consumer_arn", value=consumer_arn, expected_type=type_hints["consumer_arn"])
            check_type(argname="argument tracker_name", value=tracker_name, expected_type=type_hints["tracker_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consumer_arn": consumer_arn,
            "tracker_name": tracker_name,
        }

    @builtins.property
    def consumer_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the geofence collection to be associated to tracker resource.

        Used when you need to specify a resource across all AWS .

        - Format example: ``arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-consumerarn
        '''
        result = self._values.get("consumer_arn")
        assert result is not None, "Required property 'consumer_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tracker_name(self) -> builtins.str:
        '''The name for the tracker resource.

        Requirements:

        - Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_).
        - Must be a unique tracker resource name.
        - No spaces allowed. For example, ``ExampleTracker`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-trackername
        '''
        result = self._values.get("tracker_name")
        assert result is not None, "Required property 'tracker_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrackerConsumerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_location.CfnTrackerProps",
    jsii_struct_bases=[],
    name_mapping={
        "tracker_name": "trackerName",
        "description": "description",
        "event_bridge_enabled": "eventBridgeEnabled",
        "kms_key_enable_geospatial_queries": "kmsKeyEnableGeospatialQueries",
        "kms_key_id": "kmsKeyId",
        "position_filtering": "positionFiltering",
        "pricing_plan": "pricingPlan",
        "pricing_plan_data_source": "pricingPlanDataSource",
        "tags": "tags",
    },
)
class CfnTrackerProps:
    def __init__(
        self,
        *,
        tracker_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        event_bridge_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_key_enable_geospatial_queries: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        position_filtering: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        pricing_plan_data_source: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTracker``.

        :param tracker_name: The name for the tracker resource. Requirements: - Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_). - Must be a unique tracker resource name. - No spaces allowed. For example, ``ExampleTracker`` .
        :param description: An optional description for the tracker resource.
        :param event_bridge_enabled: 
        :param kms_key_enable_geospatial_queries: 
        :param kms_key_id: A key identifier for an `AWS KMS customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>`_ . Enter a key ID, key ARN, alias name, or alias ARN.
        :param position_filtering: Specifies the position filtering for the tracker resource. Valid values: - ``TimeBased`` - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID. - ``DistanceBased`` - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this area are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map. - ``AccuracyBased`` - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This can reduce the effects of GPS noise when displaying device trajectories on a map, and can help control your costs by reducing the number of geofence evaluations. This field is optional. If not specified, the default value is ``TimeBased`` .
        :param pricing_plan: 
        :param pricing_plan_data_source: (deprecated) This shape is deprecated since 2022-02-01: Deprecated. No longer allowed.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_location as location
            
            cfn_tracker_props = location.CfnTrackerProps(
                tracker_name="trackerName",
            
                # the properties below are optional
                description="description",
                event_bridge_enabled=False,
                kms_key_enable_geospatial_queries=False,
                kms_key_id="kmsKeyId",
                position_filtering="positionFiltering",
                pricing_plan="pricingPlan",
                pricing_plan_data_source="pricingPlanDataSource",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4963cd9bb9360f72e2ea99e0d8d6626ac02c1681099b08a5a4acc54e079dfa9)
            check_type(argname="argument tracker_name", value=tracker_name, expected_type=type_hints["tracker_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_bridge_enabled", value=event_bridge_enabled, expected_type=type_hints["event_bridge_enabled"])
            check_type(argname="argument kms_key_enable_geospatial_queries", value=kms_key_enable_geospatial_queries, expected_type=type_hints["kms_key_enable_geospatial_queries"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument position_filtering", value=position_filtering, expected_type=type_hints["position_filtering"])
            check_type(argname="argument pricing_plan", value=pricing_plan, expected_type=type_hints["pricing_plan"])
            check_type(argname="argument pricing_plan_data_source", value=pricing_plan_data_source, expected_type=type_hints["pricing_plan_data_source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tracker_name": tracker_name,
        }
        if description is not None:
            self._values["description"] = description
        if event_bridge_enabled is not None:
            self._values["event_bridge_enabled"] = event_bridge_enabled
        if kms_key_enable_geospatial_queries is not None:
            self._values["kms_key_enable_geospatial_queries"] = kms_key_enable_geospatial_queries
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if position_filtering is not None:
            self._values["position_filtering"] = position_filtering
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if pricing_plan_data_source is not None:
            self._values["pricing_plan_data_source"] = pricing_plan_data_source
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def tracker_name(self) -> builtins.str:
        '''The name for the tracker resource.

        Requirements:

        - Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_).
        - Must be a unique tracker resource name.
        - No spaces allowed. For example, ``ExampleTracker`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-trackername
        '''
        result = self._values.get("tracker_name")
        assert result is not None, "Required property 'tracker_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the tracker resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_bridge_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-eventbridgeenabled
        '''
        result = self._values.get("event_bridge_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def kms_key_enable_geospatial_queries(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-kmskeyenablegeospatialqueries
        '''
        result = self._values.get("kms_key_enable_geospatial_queries")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''A key identifier for an `AWS KMS customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>`_ . Enter a key ID, key ARN, alias name, or alias ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def position_filtering(self) -> typing.Optional[builtins.str]:
        '''Specifies the position filtering for the tracker resource.

        Valid values:

        - ``TimeBased`` - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID.
        - ``DistanceBased`` - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this area are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map.
        - ``AccuracyBased`` - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This can reduce the effects of GPS noise when displaying device trajectories on a map, and can help control your costs by reducing the number of geofence evaluations.

        This field is optional. If not specified, the default value is ``TimeBased`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-positionfiltering
        '''
        result = self._values.get("position_filtering")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''
        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplan
        :stability: deprecated
        '''
        result = self._values.get("pricing_plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan_data_source(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This shape is deprecated since 2022-02-01: Deprecated.

        No longer allowed.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplandatasource
        :stability: deprecated
        '''
        result = self._values.get("pricing_plan_data_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrackerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAPIKey",
    "CfnAPIKeyProps",
    "CfnGeofenceCollection",
    "CfnGeofenceCollectionProps",
    "CfnMap",
    "CfnMapProps",
    "CfnPlaceIndex",
    "CfnPlaceIndexProps",
    "CfnRouteCalculator",
    "CfnRouteCalculatorProps",
    "CfnTracker",
    "CfnTrackerConsumer",
    "CfnTrackerConsumerProps",
    "CfnTrackerProps",
]

publication.publish()

def _typecheckingstub__e2ae0e8c734c36fc4dfc2e50264fbc5e41cc44ca78d64c47f19cac56e4318d32(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    key_name: builtins.str,
    restrictions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAPIKey.ApiKeyRestrictionsProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    expire_time: typing.Optional[builtins.str] = None,
    force_delete: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    force_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    no_expiry: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90e4d83d582a33efc0dfeef244e5a4b84a90230cc485853b42d16a3e6f6609a7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__099c2b5d173d474236a30915cc6fc0919b6fe1cf215f99e6636485c92a9af0ca(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00e03a38669285c7b235bbd87ec7317379694b0537c3a85e4741d27c54c9d3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65682d4a834f16510a57f21e8af7c41ba661e7d0f78293abcd483f9d45afba31(
    value: typing.Union[_IResolvable_da3f097b, CfnAPIKey.ApiKeyRestrictionsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1957f4ade558178bedd1746c97b21ac5195a216695895f32ba33d6fe99216c5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8263b20b7b28c2712bf62bdacab9989763120af28d1e026f26e14f6e572ae7c9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8379f2b16717a153383f6b36ff735d0d746008205280dddfc3ffe2f253f29a2(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6402962818d046984829754f6a1e3957be1c7b7981fc92251adcdb9aaeefd493(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f2e8a3ec18117161377722f1dd02cee2566e5eb477a2de4cfbc6a270028941e(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__297a793f153416e3131543d9b1a435c125bf1b45672e8ee10841ec34b14e6d66(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c74737f1e32f7583c8c63e1c8de07d36792e8e3aee5f799d6c8a265f1a3bebb(
    *,
    allow_actions: typing.Sequence[builtins.str],
    allow_resources: typing.Sequence[builtins.str],
    allow_referers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe99c80388f80e304ec3579f14c21edc069b0865131b2673a8f49e8274c07f4(
    *,
    key_name: builtins.str,
    restrictions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAPIKey.ApiKeyRestrictionsProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    expire_time: typing.Optional[builtins.str] = None,
    force_delete: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    force_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    no_expiry: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e0601ccc1fece7d46bccf997c94a7f51bea09a1590d5ce84823ed5c0b2041c1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    collection_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    pricing_plan_data_source: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66134049825423372dae82a0ee8b8c0bba09bda09682513f80795605e6e0bca6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f4d7847226c9732be9ccaa062a530dac9299d5b10abbda476dd87dbeb44b817(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e1fa37cb45ca3a446eacf95e0913ed3efd929171f9d39cc8468baf799adcc51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cbd649bd3182fd4727374b07a6677a62cad5c3336b33bc5e81d0dce2c17e57d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f66429d0739f2243b2062e0ca96d0b992ca5e6644989ca9e3620fec145d4c801(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeaf37bab42359e906370b69c4d7738d5d88e344697648948a0aafcf5751b8c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac440741201f7074f72462a372fb1e02f934a32f1d63e4645ed0506f4d874c8e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c685a12991ff080fc342ecb024cac707829ec5c29f69506f34e69631875f71(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__307d0c98cf0385e786cd529fa95282bdfb460c6c7bb7e72dde3e3e36be5b809b(
    *,
    collection_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    pricing_plan_data_source: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2dcb0428eb66932a1afc7be03e22130166237e903d48b7c13fc63dbc8f17b8a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMap.MapConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    map_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9beda5dad2c7dda9e9e75c7563f1dd64ce2d95ee632f1f16c15c710cb2fcb9e0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23c81c05fd3d18494b5a67a26662df2ed22fb26a83114a2a0d33f71351eca462(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a9f72d270eb9bf689ae6d9866174a230761748f72e7261987c4cc8c502029b1(
    value: typing.Union[_IResolvable_da3f097b, CfnMap.MapConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b14104c4a32a55719c593e2887df99cc3a37af1549a48dabd43c2e5d116df9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__031d91b8f14088e6516171c6244cb833bddde7d5749bd4d5e5ee39bfe0f17fe8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de864d7ca8c9af6ca27a35f5fb304092560e41a384b9dd782f1dd78cc16953b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb33fbdbbd66a87cdef71cb76784ef3bcdea2208fa231444865a3178588b36c6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f994438dc4a55ff175f7c8b92debb9548b8c21e2896a0380a521bcdba4e2a0d6(
    *,
    style: builtins.str,
    custom_layers: typing.Optional[typing.Sequence[builtins.str]] = None,
    political_view: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702a4eb1b8c53d553ad5479cf127f6ed1090248f0a9d4806eec0b368c1165ea8(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMap.MapConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    map_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86efa72874938a7fdd56ee75ab5f3481754256c4e7be12dd321fb8179b36168(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_source: builtins.str,
    index_name: builtins.str,
    data_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlaceIndex.DataSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c405c6a922a2896cb59706744382d2e74f7b74e7533c5078a63a01a0dda7f8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e6a62d57c55981d2561a3c18c99b7b68c42dd787f2ac2a05ef607b0d5c38be(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7c1c6b9a81b0a961b6426f41c459172924ee226a1266f2c09e8bcee9f894dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80848c256675ce5115c146bfbde42fded11406ee451376e49955461fb6004b75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4cff8053f28ed6073e2b7c62ec72627c8ffc7b98c86bc2b7c5c4e9b177d8d4a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPlaceIndex.DataSourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a59366c5536e4867cad1dd1e53981208d2606343698315f4ecfbe50ac0be1c27(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7653a99bc2f680ec231d78959d16db4997e472e731a68a554772f0e08b4fd925(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a88e3fcbc3fba96f937cf7669a81dcdb84f3dce7ddea1dd5143fcf5e7eaeb70e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b631c3e00c6906f33efa721d356034e81e693d6aa037787fadb69355eaa4ef41(
    *,
    intended_use: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa21f8e355faff509cae18242ebc62f8af877465a5ef051abbedc5885bb64cd4(
    *,
    data_source: builtins.str,
    index_name: builtins.str,
    data_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlaceIndex.DataSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a900f380dbd4e0012dcb474730041f91eeaecc9218db4d6163fd730394a66f3a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    calculator_name: builtins.str,
    data_source: builtins.str,
    description: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f206fe9bb875d2c7acae9be0a23fa0286ad54fbd1bebff69010a95bea15fec(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c6188d22ee31496bd1f61ea15dd8d141313349058c043549fd0dad11d02a49b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9501128c2291eb0596cb61fa914f8f1f6ceb251748807dce9d7b778f46355373(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__facb0538b630afd7ae0f1a08a48d6f92e23fb00dc53fd3e9bdedc88b3e17b6b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88fc3920b0a8018d893998ecb23006fd6c84ebcc44e8ca60c506b79ade39568(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f40cb810c37a798bfec946670c6e7a33c338d2fe035b50de2d1bee9b1485bdc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74454734a6df8a4308849a60f8d80541ab1a10fc08d73d9f6faa0474841ec604(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986eaab9e9d4b82fd7bedac19af61096151542baed90ee4afaad1d66b4b219c9(
    *,
    calculator_name: builtins.str,
    data_source: builtins.str,
    description: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cd2e07bf97c42a45f9443da7edf34b075c2f9b41a262ae77aee4b2a82a30dc0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    tracker_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    event_bridge_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key_enable_geospatial_queries: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    position_filtering: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    pricing_plan_data_source: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606edf93b66473926b20e5a3b0af67fe5ed3f2fceae488ca1b2486f74e9beeb4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1045c636e6d3b0f9dcbb0a4661afd9d9bfe2912562fdba49a3e87a5d8e522f9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704fbf855c65f61aeff35b9fcc74d9758e51af0bbee363ab356fea2602f904b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432656f1a3249889b4f6340d433951d4b03ec382b366b9cefc7f22db81828ad3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd4f7477042ce6ed75f0b9861b25a721854ba28f82072db60305830e07af0d42(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2dd571749bac14762477ff49a8f135c7d6e5b9f96b1f45fdb2f11d55be863ce(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcc29257a761669c6cc236364e363b6512c47005e61ff4201e14badc85d4b49d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f9e9ee70dc0e0f484224b53e37f910ac2fe681564c2ba665fb49c1f326e222(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ef71bd19b0038f0b7a053221674f1b6d79138bfb1150915529c7b0aefe900f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9f5b36993f4be81b2285747fed230ab9182b4393ef3b93d823765df23324c4c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd4f1b9ba5c51ac5a38d0876f790c1137595037fec38c3aacc1dd70bc872c126(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796f07ade0c1c21cf2be739abf72847e038c9c0f1fe6e69286fa0b51df24a022(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    consumer_arn: builtins.str,
    tracker_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7cf03d6794740801a069f1fdfdefcd95ab283d7bba980f64a30bc78e1155809(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db67e253b286d87476fb1aa3fa7c47f96dc2e0d9269d323e1ca1f4c17fb60c85(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3101704451bf83d25aae3a96e950bccc978a403a238456dffbfa02203f3d5fad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa34370ea71108b33b5119b9fcb8ca5029e1349c5ec4e2fb3d74745ed6952b4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c4f2c66be9e9a4dcfdb7c07a9f472259b9cfbd8f7d951a99362fad4aecdf9d8(
    *,
    consumer_arn: builtins.str,
    tracker_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4963cd9bb9360f72e2ea99e0d8d6626ac02c1681099b08a5a4acc54e079dfa9(
    *,
    tracker_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    event_bridge_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key_enable_geospatial_queries: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    position_filtering: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    pricing_plan_data_source: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
