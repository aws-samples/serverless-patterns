'''
# Amazon AppStream 2.0 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_appstream as appstream
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppStream construct libraries](https://constructs.dev/search?q=appstream)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppStream resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppStream.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppStream.html).

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
class CfnAppBlock(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnAppBlock",
):
    '''This resource creates an app block.

    App blocks store details about the virtual hard disk that contains the files for the application in an S3 bucket. It also stores the setup script with details about how to mount the virtual hard disk. App blocks are only supported for Elastic fleets.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html
    :cloudformationResource: AWS::AppStream::AppBlock
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_app_block = appstream.CfnAppBlock(self, "MyCfnAppBlock",
            name="name",
            source_s3_location=appstream.CfnAppBlock.S3LocationProperty(
                s3_bucket="s3Bucket",
        
                # the properties below are optional
                s3_key="s3Key"
            ),
        
            # the properties below are optional
            description="description",
            display_name="displayName",
            packaging_type="packagingType",
            post_setup_script_details=appstream.CfnAppBlock.ScriptDetailsProperty(
                executable_path="executablePath",
                script_s3_location=appstream.CfnAppBlock.S3LocationProperty(
                    s3_bucket="s3Bucket",
        
                    # the properties below are optional
                    s3_key="s3Key"
                ),
                timeout_in_seconds=123,
        
                # the properties below are optional
                executable_parameters="executableParameters"
            ),
            setup_script_details=appstream.CfnAppBlock.ScriptDetailsProperty(
                executable_path="executablePath",
                script_s3_location=appstream.CfnAppBlock.S3LocationProperty(
                    s3_bucket="s3Bucket",
        
                    # the properties below are optional
                    s3_key="s3Key"
                ),
                timeout_in_seconds=123,
        
                # the properties below are optional
                executable_parameters="executableParameters"
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
        name: builtins.str,
        source_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAppBlock.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        packaging_type: typing.Optional[builtins.str] = None,
        post_setup_script_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAppBlock.ScriptDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        setup_script_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAppBlock.ScriptDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the app block. *Pattern* : ``^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$``
        :param source_s3_location: The source S3 location of the app block.
        :param description: The description of the app block.
        :param display_name: The display name of the app block.
        :param packaging_type: The packaging type of the app block.
        :param post_setup_script_details: The post setup script details of the app block.
        :param setup_script_details: The setup script details of the app block.
        :param tags: The tags of the app block.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41cea9e42ea830db5b0d999c409efe33186557a7bb3be96abafb06fba47482c9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppBlockProps(
            name=name,
            source_s3_location=source_s3_location,
            description=description,
            display_name=display_name,
            packaging_type=packaging_type,
            post_setup_script_details=post_setup_script_details,
            setup_script_details=setup_script_details,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ef0c832915a964995aef2c59ffa4492185116744601f84186bb724561d2bf7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d32d2a9da5d96e63b2ca346390b8f58c00ce6fbf8704303679cd9e77c84c363b)
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
        '''The ARN of the app block.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''The time when the app block was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

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
        '''The name of the app block.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7ecda575988f84aef9017ebbc9caa5b673bb06457ea5362157d745c55bb2f5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceS3Location")
    def source_s3_location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAppBlock.S3LocationProperty"]:
        '''The source S3 location of the app block.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAppBlock.S3LocationProperty"], jsii.get(self, "sourceS3Location"))

    @source_s3_location.setter
    def source_s3_location(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAppBlock.S3LocationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a504881240dbb8e4d49a5c3509bd9afb394356e43746a04d59cfeedc8ca2949)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the app block.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88e9d4134f7f7352e3e69141d073b4571541a079a733164dada584671a936918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the app block.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6346454c9b1e9f0b74872f97613850d9892e436b8e479fff337895c59a6885f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="packagingType")
    def packaging_type(self) -> typing.Optional[builtins.str]:
        '''The packaging type of the app block.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packagingType"))

    @packaging_type.setter
    def packaging_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b46503228b5203f79b0306e550d548542da93d07ce7c0094df440dcdf94c8164)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packagingType", value)

    @builtins.property
    @jsii.member(jsii_name="postSetupScriptDetails")
    def post_setup_script_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAppBlock.ScriptDetailsProperty"]]:
        '''The post setup script details of the app block.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAppBlock.ScriptDetailsProperty"]], jsii.get(self, "postSetupScriptDetails"))

    @post_setup_script_details.setter
    def post_setup_script_details(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAppBlock.ScriptDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b19b4dc43a42401721ecc3c51a40c838ce7167fe3ecd27eae1eb5639adcdd3d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postSetupScriptDetails", value)

    @builtins.property
    @jsii.member(jsii_name="setupScriptDetails")
    def setup_script_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAppBlock.ScriptDetailsProperty"]]:
        '''The setup script details of the app block.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAppBlock.ScriptDetailsProperty"]], jsii.get(self, "setupScriptDetails"))

    @setup_script_details.setter
    def setup_script_details(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAppBlock.ScriptDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d14e1522f81e1c48d4360cf330cdfac3f189fc416e28492b7d675d522f79a41c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setupScriptDetails", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags of the app block.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44d020fa00d7c6033b8a7317dffe2fc57d25861244d1c79a52394344ee58e3a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnAppBlock.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_bucket": "s3Bucket", "s3_key": "s3Key"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            s3_bucket: builtins.str,
            s3_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The S3 location of the app block.

            :param s3_bucket: The S3 bucket of the app block.
            :param s3_key: The S3 key of the S3 object of the virtual hard disk. This is required when it's used by ``SetupScriptDetails`` and ``PostSetupScriptDetails`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                s3_location_property = appstream.CfnAppBlock.S3LocationProperty(
                    s3_bucket="s3Bucket",
                
                    # the properties below are optional
                    s3_key="s3Key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3984118729e2d72b9f813b24157e458bdc05747e70cacda34fd5c17fb557da0)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
            }
            if s3_key is not None:
                self._values["s3_key"] = s3_key

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The S3 bucket of the app block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-s3location.html#cfn-appstream-appblock-s3location-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> typing.Optional[builtins.str]:
            '''The S3 key of the S3 object of the virtual hard disk.

            This is required when it's used by ``SetupScriptDetails`` and ``PostSetupScriptDetails`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-s3location.html#cfn-appstream-appblock-s3location-s3key
            '''
            result = self._values.get("s3_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnAppBlock.ScriptDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "executable_path": "executablePath",
            "script_s3_location": "scriptS3Location",
            "timeout_in_seconds": "timeoutInSeconds",
            "executable_parameters": "executableParameters",
        },
    )
    class ScriptDetailsProperty:
        def __init__(
            self,
            *,
            executable_path: builtins.str,
            script_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAppBlock.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
            timeout_in_seconds: jsii.Number,
            executable_parameters: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the script.

            :param executable_path: The run path for the script.
            :param script_s3_location: The S3 object location of the script.
            :param timeout_in_seconds: The run timeout, in seconds, for the script.
            :param executable_parameters: The parameters used in the run path for the script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                script_details_property = appstream.CfnAppBlock.ScriptDetailsProperty(
                    executable_path="executablePath",
                    script_s3_location=appstream.CfnAppBlock.S3LocationProperty(
                        s3_bucket="s3Bucket",
                
                        # the properties below are optional
                        s3_key="s3Key"
                    ),
                    timeout_in_seconds=123,
                
                    # the properties below are optional
                    executable_parameters="executableParameters"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44b4987276279c543e86060c2474d9b8d33b9395331f346758fe51e79a75d78c)
                check_type(argname="argument executable_path", value=executable_path, expected_type=type_hints["executable_path"])
                check_type(argname="argument script_s3_location", value=script_s3_location, expected_type=type_hints["script_s3_location"])
                check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
                check_type(argname="argument executable_parameters", value=executable_parameters, expected_type=type_hints["executable_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "executable_path": executable_path,
                "script_s3_location": script_s3_location,
                "timeout_in_seconds": timeout_in_seconds,
            }
            if executable_parameters is not None:
                self._values["executable_parameters"] = executable_parameters

        @builtins.property
        def executable_path(self) -> builtins.str:
            '''The run path for the script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html#cfn-appstream-appblock-scriptdetails-executablepath
            '''
            result = self._values.get("executable_path")
            assert result is not None, "Required property 'executable_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def script_s3_location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAppBlock.S3LocationProperty"]:
            '''The S3 object location of the script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html#cfn-appstream-appblock-scriptdetails-scripts3location
            '''
            result = self._values.get("script_s3_location")
            assert result is not None, "Required property 'script_s3_location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAppBlock.S3LocationProperty"], result)

        @builtins.property
        def timeout_in_seconds(self) -> jsii.Number:
            '''The run timeout, in seconds, for the script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html#cfn-appstream-appblock-scriptdetails-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            assert result is not None, "Required property 'timeout_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def executable_parameters(self) -> typing.Optional[builtins.str]:
            '''The parameters used in the run path for the script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html#cfn-appstream-appblock-scriptdetails-executableparameters
            '''
            result = self._values.get("executable_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScriptDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAppBlockBuilder(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnAppBlockBuilder",
):
    '''Creates an app block builder.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html
    :cloudformationResource: AWS::AppStream::AppBlockBuilder
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_app_block_builder = appstream.CfnAppBlockBuilder(self, "MyCfnAppBlockBuilder",
            instance_type="instanceType",
            name="name",
            platform="platform",
            vpc_config=appstream.CfnAppBlockBuilder.VpcConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            ),
        
            # the properties below are optional
            access_endpoints=[appstream.CfnAppBlockBuilder.AccessEndpointProperty(
                endpoint_type="endpointType",
                vpce_id="vpceId"
            )],
            app_block_arns=["appBlockArns"],
            description="description",
            display_name="displayName",
            enable_default_internet_access=False,
            iam_role_arn="iamRoleArn",
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
        instance_type: builtins.str,
        name: builtins.str,
        platform: builtins.str,
        vpc_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAppBlockBuilder.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAppBlockBuilder.AccessEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        app_block_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_type: The instance type of the app block builder.
        :param name: The name of the app block builder.
        :param platform: The platform of the app block builder. *Allowed values* : ``WINDOWS_SERVER_2019``
        :param vpc_config: The VPC configuration for the app block builder.
        :param access_endpoints: The access endpoints of the app block builder.
        :param app_block_arns: The ARN of the app block. *Maximum* : ``1``
        :param description: The description of the app block builder.
        :param display_name: The display name of the app block builder.
        :param enable_default_internet_access: Indicates whether default internet access is enabled for the app block builder.
        :param iam_role_arn: The ARN of the IAM role that is applied to the app block builder.
        :param tags: The tags of the app block builder.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2dbe872e5cba24425b73eff2bd90d7b1c6af7a2b3b47d455ff4683fb5c3b559)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppBlockBuilderProps(
            instance_type=instance_type,
            name=name,
            platform=platform,
            vpc_config=vpc_config,
            access_endpoints=access_endpoints,
            app_block_arns=app_block_arns,
            description=description,
            display_name=display_name,
            enable_default_internet_access=enable_default_internet_access,
            iam_role_arn=iam_role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__560ef45e47870972c6b9d1538088c62bf2a04bfeb5ca9a51c7fe0b65e8ec8511)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d3986dbb1b3fffafc9f179d356205fdd37785ebd341b7f3bdb113b697cda7c3)
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
        '''The ARN of the app block builder.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''The time when the app block builder was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

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
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''The instance type of the app block builder.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f21b6ecd30e303361f359d504ba6d4430fa39df00d8db479a13a42cafb98fae1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the app block builder.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d93595f1388c9e3a643d55562aceb2635a4d08dfc401ab918be963bd34d37fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        '''The platform of the app block builder.'''
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b091d87f29dcb5d30e2004be0e23c286ac25a0d91972c2a15f504513758f527)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAppBlockBuilder.VpcConfigProperty"]:
        '''The VPC configuration for the app block builder.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAppBlockBuilder.VpcConfigProperty"], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAppBlockBuilder.VpcConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__180d8c618c42d04568f892dee70a7790f7e99eeb61d519960b3b033c12cfe689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @builtins.property
    @jsii.member(jsii_name="accessEndpoints")
    def access_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAppBlockBuilder.AccessEndpointProperty"]]]]:
        '''The access endpoints of the app block builder.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAppBlockBuilder.AccessEndpointProperty"]]]], jsii.get(self, "accessEndpoints"))

    @access_endpoints.setter
    def access_endpoints(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAppBlockBuilder.AccessEndpointProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0c2370cdeeba05804fa6dd3f03d3862ece8f691558c77fb2a589df46ab16118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="appBlockArns")
    def app_block_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the app block.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "appBlockArns"))

    @app_block_arns.setter
    def app_block_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf5cb8b2ccd8f98c58e0fb8358a949225e23002425ae28212a658e15797b9d92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appBlockArns", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the app block builder.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__182b4edd83508ba66a0f582b454b58fa740d47820caf28e86a8ab22c5b227d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the app block builder.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc53127e490e484f1257f25a433fbbd6130ffe2bee9e0368471246d58d6ee95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enableDefaultInternetAccess")
    def enable_default_internet_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether default internet access is enabled for the app block builder.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableDefaultInternetAccess"))

    @enable_default_internet_access.setter
    def enable_default_internet_access(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47484d5ec55d944eba05db1c12e9dd2dbf40de14a4080c6840d63d110ec36bbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDefaultInternetAccess", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that is applied to the app block builder.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be31238972433ba4e0bfd240749782ef85ea23f117dfd179b56cff0e355e3634)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags of the app block builder.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7e7e62dce5b776582e32baec62848ca5111cb28b2742ac5e7e945e0160279c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnAppBlockBuilder.AccessEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_type": "endpointType", "vpce_id": "vpceId"},
    )
    class AccessEndpointProperty:
        def __init__(
            self,
            *,
            endpoint_type: builtins.str,
            vpce_id: builtins.str,
        ) -> None:
            '''Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

            :param endpoint_type: The type of interface endpoint.
            :param vpce_id: The identifier (ID) of the VPC in which the interface endpoint is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-accessendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                access_endpoint_property = appstream.CfnAppBlockBuilder.AccessEndpointProperty(
                    endpoint_type="endpointType",
                    vpce_id="vpceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__39fcf5386df3e63b3df8d03a9fbecf60ced2b40b3644175eba767c428a336b47)
                check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
                check_type(argname="argument vpce_id", value=vpce_id, expected_type=type_hints["vpce_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint_type": endpoint_type,
                "vpce_id": vpce_id,
            }

        @builtins.property
        def endpoint_type(self) -> builtins.str:
            '''The type of interface endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-accessendpoint.html#cfn-appstream-appblockbuilder-accessendpoint-endpointtype
            '''
            result = self._values.get("endpoint_type")
            assert result is not None, "Required property 'endpoint_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpce_id(self) -> builtins.str:
            '''The identifier (ID) of the VPC in which the interface endpoint is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-accessendpoint.html#cfn-appstream-appblockbuilder-accessendpoint-vpceid
            '''
            result = self._values.get("vpce_id")
            assert result is not None, "Required property 'vpce_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnAppBlockBuilder.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes VPC configuration information for fleets and image builders.

            :param security_group_ids: The identifiers of the security groups for the fleet or image builder.
            :param subnet_ids: The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                vpc_config_property = appstream.CfnAppBlockBuilder.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__23900099939292b49034d4a7bcee1e44ad2bddaf629079b514d80ab283d4f3a5)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The identifiers of the security groups for the fleet or image builder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-vpcconfig.html#cfn-appstream-appblockbuilder-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance.

            Fleet instances use one or more subnets. Image builder instances use one subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-vpcconfig.html#cfn-appstream-appblockbuilder-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnAppBlockBuilderProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "name": "name",
        "platform": "platform",
        "vpc_config": "vpcConfig",
        "access_endpoints": "accessEndpoints",
        "app_block_arns": "appBlockArns",
        "description": "description",
        "display_name": "displayName",
        "enable_default_internet_access": "enableDefaultInternetAccess",
        "iam_role_arn": "iamRoleArn",
        "tags": "tags",
    },
)
class CfnAppBlockBuilderProps:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        name: builtins.str,
        platform: builtins.str,
        vpc_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlockBuilder.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlockBuilder.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        app_block_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAppBlockBuilder``.

        :param instance_type: The instance type of the app block builder.
        :param name: The name of the app block builder.
        :param platform: The platform of the app block builder. *Allowed values* : ``WINDOWS_SERVER_2019``
        :param vpc_config: The VPC configuration for the app block builder.
        :param access_endpoints: The access endpoints of the app block builder.
        :param app_block_arns: The ARN of the app block. *Maximum* : ``1``
        :param description: The description of the app block builder.
        :param display_name: The display name of the app block builder.
        :param enable_default_internet_access: Indicates whether default internet access is enabled for the app block builder.
        :param iam_role_arn: The ARN of the IAM role that is applied to the app block builder.
        :param tags: The tags of the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_app_block_builder_props = appstream.CfnAppBlockBuilderProps(
                instance_type="instanceType",
                name="name",
                platform="platform",
                vpc_config=appstream.CfnAppBlockBuilder.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                ),
            
                # the properties below are optional
                access_endpoints=[appstream.CfnAppBlockBuilder.AccessEndpointProperty(
                    endpoint_type="endpointType",
                    vpce_id="vpceId"
                )],
                app_block_arns=["appBlockArns"],
                description="description",
                display_name="displayName",
                enable_default_internet_access=False,
                iam_role_arn="iamRoleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e788750b4b78274a373182d9b8ff84f13602b9b9ce827c99dbbbeefc73304b62)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
            check_type(argname="argument access_endpoints", value=access_endpoints, expected_type=type_hints["access_endpoints"])
            check_type(argname="argument app_block_arns", value=app_block_arns, expected_type=type_hints["app_block_arns"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument enable_default_internet_access", value=enable_default_internet_access, expected_type=type_hints["enable_default_internet_access"])
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
            "name": name,
            "platform": platform,
            "vpc_config": vpc_config,
        }
        if access_endpoints is not None:
            self._values["access_endpoints"] = access_endpoints
        if app_block_arns is not None:
            self._values["app_block_arns"] = app_block_arns
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if enable_default_internet_access is not None:
            self._values["enable_default_internet_access"] = enable_default_internet_access
        if iam_role_arn is not None:
            self._values["iam_role_arn"] = iam_role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''The instance type of the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platform(self) -> builtins.str:
        '''The platform of the app block builder.

        *Allowed values* : ``WINDOWS_SERVER_2019``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-platform
        '''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAppBlockBuilder.VpcConfigProperty]:
        '''The VPC configuration for the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-vpcconfig
        '''
        result = self._values.get("vpc_config")
        assert result is not None, "Required property 'vpc_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAppBlockBuilder.VpcConfigProperty], result)

    @builtins.property
    def access_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAppBlockBuilder.AccessEndpointProperty]]]]:
        '''The access endpoints of the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-accessendpoints
        '''
        result = self._values.get("access_endpoints")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAppBlockBuilder.AccessEndpointProperty]]]], result)

    @builtins.property
    def app_block_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the app block.

        *Maximum* : ``1``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-appblockarns
        '''
        result = self._values.get("app_block_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_default_internet_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether default internet access is enabled for the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-enabledefaultinternetaccess
        '''
        result = self._values.get("enable_default_internet_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that is applied to the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-iamrolearn
        '''
        result = self._values.get("iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags of the app block builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppBlockBuilderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnAppBlockProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_s3_location": "sourceS3Location",
        "description": "description",
        "display_name": "displayName",
        "packaging_type": "packagingType",
        "post_setup_script_details": "postSetupScriptDetails",
        "setup_script_details": "setupScriptDetails",
        "tags": "tags",
    },
)
class CfnAppBlockProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        source_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        packaging_type: typing.Optional[builtins.str] = None,
        post_setup_script_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.ScriptDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        setup_script_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.ScriptDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAppBlock``.

        :param name: The name of the app block. *Pattern* : ``^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$``
        :param source_s3_location: The source S3 location of the app block.
        :param description: The description of the app block.
        :param display_name: The display name of the app block.
        :param packaging_type: The packaging type of the app block.
        :param post_setup_script_details: The post setup script details of the app block.
        :param setup_script_details: The setup script details of the app block.
        :param tags: The tags of the app block.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_app_block_props = appstream.CfnAppBlockProps(
                name="name",
                source_s3_location=appstream.CfnAppBlock.S3LocationProperty(
                    s3_bucket="s3Bucket",
            
                    # the properties below are optional
                    s3_key="s3Key"
                ),
            
                # the properties below are optional
                description="description",
                display_name="displayName",
                packaging_type="packagingType",
                post_setup_script_details=appstream.CfnAppBlock.ScriptDetailsProperty(
                    executable_path="executablePath",
                    script_s3_location=appstream.CfnAppBlock.S3LocationProperty(
                        s3_bucket="s3Bucket",
            
                        # the properties below are optional
                        s3_key="s3Key"
                    ),
                    timeout_in_seconds=123,
            
                    # the properties below are optional
                    executable_parameters="executableParameters"
                ),
                setup_script_details=appstream.CfnAppBlock.ScriptDetailsProperty(
                    executable_path="executablePath",
                    script_s3_location=appstream.CfnAppBlock.S3LocationProperty(
                        s3_bucket="s3Bucket",
            
                        # the properties below are optional
                        s3_key="s3Key"
                    ),
                    timeout_in_seconds=123,
            
                    # the properties below are optional
                    executable_parameters="executableParameters"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d81fb9c3e1fcc7b221dbc8290b04501b1af7d21a103a5dacb19c8221493f37f1)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_s3_location", value=source_s3_location, expected_type=type_hints["source_s3_location"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument packaging_type", value=packaging_type, expected_type=type_hints["packaging_type"])
            check_type(argname="argument post_setup_script_details", value=post_setup_script_details, expected_type=type_hints["post_setup_script_details"])
            check_type(argname="argument setup_script_details", value=setup_script_details, expected_type=type_hints["setup_script_details"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "source_s3_location": source_s3_location,
        }
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if packaging_type is not None:
            self._values["packaging_type"] = packaging_type
        if post_setup_script_details is not None:
            self._values["post_setup_script_details"] = post_setup_script_details
        if setup_script_details is not None:
            self._values["setup_script_details"] = setup_script_details
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the app block.

        *Pattern* : ``^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_s3_location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAppBlock.S3LocationProperty]:
        '''The source S3 location of the app block.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-sources3location
        '''
        result = self._values.get("source_s3_location")
        assert result is not None, "Required property 'source_s3_location' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAppBlock.S3LocationProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the app block.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the app block.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def packaging_type(self) -> typing.Optional[builtins.str]:
        '''The packaging type of the app block.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-packagingtype
        '''
        result = self._values.get("packaging_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_setup_script_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAppBlock.ScriptDetailsProperty]]:
        '''The post setup script details of the app block.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-postsetupscriptdetails
        '''
        result = self._values.get("post_setup_script_details")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAppBlock.ScriptDetailsProperty]], result)

    @builtins.property
    def setup_script_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAppBlock.ScriptDetailsProperty]]:
        '''The setup script details of the app block.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-setupscriptdetails
        '''
        result = self._values.get("setup_script_details")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAppBlock.ScriptDetailsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags of the app block.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppBlockProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnApplication",
):
    '''This resource creates an application.

    Applications store the details about how to launch applications on streaming instances. This is only supported for Elastic fleets.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html
    :cloudformationResource: AWS::AppStream::Application
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_application = appstream.CfnApplication(self, "MyCfnApplication",
            app_block_arn="appBlockArn",
            icon_s3_location=appstream.CfnApplication.S3LocationProperty(
                s3_bucket="s3Bucket",
                s3_key="s3Key"
            ),
            instance_families=["instanceFamilies"],
            launch_path="launchPath",
            name="name",
            platforms=["platforms"],
        
            # the properties below are optional
            attributes_to_delete=["attributesToDelete"],
            description="description",
            display_name="displayName",
            launch_parameters="launchParameters",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            working_directory="workingDirectory"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        app_block_arn: builtins.str,
        icon_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
        instance_families: typing.Sequence[builtins.str],
        launch_path: builtins.str,
        name: builtins.str,
        platforms: typing.Sequence[builtins.str],
        attributes_to_delete: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        launch_parameters: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_block_arn: The app block ARN with which the application should be associated.
        :param icon_s3_location: The icon S3 location of the application.
        :param instance_families: The instance families the application supports. *Allowed Values* : ``GENERAL_PURPOSE`` | ``GRAPHICS_G4``
        :param launch_path: The launch path of the application.
        :param name: The name of the application. This name is visible to users when a name is not specified in the DisplayName property. *Pattern* : ``^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$``
        :param platforms: The platforms the application supports. *Allowed Values* : ``WINDOWS_SERVER_2019`` | ``AMAZON_LINUX2``
        :param attributes_to_delete: A list of attributes to delete from an application.
        :param description: The description of the application.
        :param display_name: The display name of the application. This name is visible to users in the application catalog.
        :param launch_parameters: The launch parameters of the application.
        :param tags: The tags of the application.
        :param working_directory: The working directory of the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9009fa37c2ae00864d9c32d96617498f6fbd69d6e961b9ed0d57b66ea8a5aa1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            app_block_arn=app_block_arn,
            icon_s3_location=icon_s3_location,
            instance_families=instance_families,
            launch_path=launch_path,
            name=name,
            platforms=platforms,
            attributes_to_delete=attributes_to_delete,
            description=description,
            display_name=display_name,
            launch_parameters=launch_parameters,
            tags=tags,
            working_directory=working_directory,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bf37e6c9ebba93b6a20dd8c55575bfc26f65f587453e4fec87a3350335fdb30)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d9ff0358639f98e3ffd67a11c5427b0ccf256c68f482d14513971d5bc203aad)
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
        '''The ARN of the application.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''The time when the application was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

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
    @jsii.member(jsii_name="appBlockArn")
    def app_block_arn(self) -> builtins.str:
        '''The app block ARN with which the application should be associated.'''
        return typing.cast(builtins.str, jsii.get(self, "appBlockArn"))

    @app_block_arn.setter
    def app_block_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afcbe3239165a897dd7ad3a3fb56bb3ff4580d04e8314de0bec6b8d3e41adeb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appBlockArn", value)

    @builtins.property
    @jsii.member(jsii_name="iconS3Location")
    def icon_s3_location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnApplication.S3LocationProperty"]:
        '''The icon S3 location of the application.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApplication.S3LocationProperty"], jsii.get(self, "iconS3Location"))

    @icon_s3_location.setter
    def icon_s3_location(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnApplication.S3LocationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d27419218adf8ae55a390ca9152b985b34509b75fa155ff05a6a369102ab5a88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iconS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="instanceFamilies")
    def instance_families(self) -> typing.List[builtins.str]:
        '''The instance families the application supports.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceFamilies"))

    @instance_families.setter
    def instance_families(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e95fdca457194dd65826ce4e71255ef17556d2d8bb11d3a670954924dbe32f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceFamilies", value)

    @builtins.property
    @jsii.member(jsii_name="launchPath")
    def launch_path(self) -> builtins.str:
        '''The launch path of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "launchPath"))

    @launch_path.setter
    def launch_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c335406efc0386216f2a85242b30ab101cf760b35a8620b10ea48dff3fde6a11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afd432f06fc6cd02ca04ce3797550366ccf6d404c3627c0362d247ddbfa2045e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="platforms")
    def platforms(self) -> typing.List[builtins.str]:
        '''The platforms the application supports.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "platforms"))

    @platforms.setter
    def platforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d99c34004e688e8f22a332a95e547b6042c8fc6a0760dcaad6c34686394a7f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platforms", value)

    @builtins.property
    @jsii.member(jsii_name="attributesToDelete")
    def attributes_to_delete(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of attributes to delete from an application.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "attributesToDelete"))

    @attributes_to_delete.setter
    def attributes_to_delete(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c745e8006ba5ff2e086ec711fad075fddbe792a8fe62ceaa7dd7e17d158fbb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributesToDelete", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c44932d7f0f284fe848233f6e1bc2a9e4f048b30f4ee940536cd8ba326dbffdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2757cdff10448b7e8c5fc4692665051f8b68fd4716ae94305bb5252b295e66ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="launchParameters")
    def launch_parameters(self) -> typing.Optional[builtins.str]:
        '''The launch parameters of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchParameters"))

    @launch_parameters.setter
    def launch_parameters(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7722e337d3920d2871f9264abb6a26bb6fb91856e56ce963442b77ebc01334a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchParameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags of the application.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef307b076d145751ab1f61dcfc9204a3570e7d2c27321158a89b936291a3acdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea002ddddf4927ba2d1d69d37cd236583ea870d351ac4f4ba1bb3b6456c69d51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDirectory", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnApplication.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_bucket": "s3Bucket", "s3_key": "s3Key"},
    )
    class S3LocationProperty:
        def __init__(self, *, s3_bucket: builtins.str, s3_key: builtins.str) -> None:
            '''The S3 location of the application icon.

            :param s3_bucket: The S3 bucket of the S3 object.
            :param s3_key: The S3 key of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-application-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                s3_location_property = appstream.CfnApplication.S3LocationProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25a8ebd800bb6d4c915d27e4699c03161df65019eb746af6eae942b742f31642)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The S3 bucket of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-application-s3location.html#cfn-appstream-application-s3location-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''The S3 key of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-application-s3location.html#cfn-appstream-application-s3location-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnApplicationEntitlementAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnApplicationEntitlementAssociation",
):
    '''Associates an application to an entitlement.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html
    :cloudformationResource: AWS::AppStream::ApplicationEntitlementAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_application_entitlement_association = appstream.CfnApplicationEntitlementAssociation(self, "MyCfnApplicationEntitlementAssociation",
            application_identifier="applicationIdentifier",
            entitlement_name="entitlementName",
            stack_name="stackName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_identifier: builtins.str,
        entitlement_name: builtins.str,
        stack_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_identifier: The identifier of the application.
        :param entitlement_name: The name of the entitlement.
        :param stack_name: The name of the stack.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1cdc188825edd09dc8b562b0fb59405ff1d3a7942b872ef7b24a3a18648602)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationEntitlementAssociationProps(
            application_identifier=application_identifier,
            entitlement_name=entitlement_name,
            stack_name=stack_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e86041351b8926af1b6fa9d6e94a9bc63d2cac6ebbe156417e48f02826ee48f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e2c4dd6d4e83da25e1ba9e622419616042c3e1f148babe9d09d07921cc19972)
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
    @jsii.member(jsii_name="applicationIdentifier")
    def application_identifier(self) -> builtins.str:
        '''The identifier of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationIdentifier"))

    @application_identifier.setter
    def application_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb6566993bed166d8777fd15b08de32b886de69d33d7e37333d92a0e6d7b667c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="entitlementName")
    def entitlement_name(self) -> builtins.str:
        '''The name of the entitlement.'''
        return typing.cast(builtins.str, jsii.get(self, "entitlementName"))

    @entitlement_name.setter
    def entitlement_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__863b971564ea879f8a7165cc88fbcf8117ce148b8625b4ce8b028fe61f62c7ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entitlementName", value)

    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        '''The name of the stack.'''
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @stack_name.setter
    def stack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__120e4482e49986c6ca616b933efc543a39747121fc631acf467d6d6530edfc26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnApplicationEntitlementAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_identifier": "applicationIdentifier",
        "entitlement_name": "entitlementName",
        "stack_name": "stackName",
    },
)
class CfnApplicationEntitlementAssociationProps:
    def __init__(
        self,
        *,
        application_identifier: builtins.str,
        entitlement_name: builtins.str,
        stack_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnApplicationEntitlementAssociation``.

        :param application_identifier: The identifier of the application.
        :param entitlement_name: The name of the entitlement.
        :param stack_name: The name of the stack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_application_entitlement_association_props = appstream.CfnApplicationEntitlementAssociationProps(
                application_identifier="applicationIdentifier",
                entitlement_name="entitlementName",
                stack_name="stackName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ed66445aef0340172777886fa668a63161e6556da0c4ddda56f9f1d4ec958ba)
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument entitlement_name", value=entitlement_name, expected_type=type_hints["entitlement_name"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_identifier": application_identifier,
            "entitlement_name": entitlement_name,
            "stack_name": stack_name,
        }

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The identifier of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html#cfn-appstream-applicationentitlementassociation-applicationidentifier
        '''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entitlement_name(self) -> builtins.str:
        '''The name of the entitlement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html#cfn-appstream-applicationentitlementassociation-entitlementname
        '''
        result = self._values.get("entitlement_name")
        assert result is not None, "Required property 'entitlement_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The name of the stack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html#cfn-appstream-applicationentitlementassociation-stackname
        '''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationEntitlementAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnApplicationFleetAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnApplicationFleetAssociation",
):
    '''This resource associates the specified application with the specified fleet.

    This is only supported for Elastic fleets.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationfleetassociation.html
    :cloudformationResource: AWS::AppStream::ApplicationFleetAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_application_fleet_association = appstream.CfnApplicationFleetAssociation(self, "MyCfnApplicationFleetAssociation",
            application_arn="applicationArn",
            fleet_name="fleetName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_arn: builtins.str,
        fleet_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_arn: The ARN of the application.
        :param fleet_name: The name of the fleet.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9dfb530d7e84f7276b2c13f4b5afbb9da758e394426c8ec880af3ce38971813)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationFleetAssociationProps(
            application_arn=application_arn, fleet_name=fleet_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a8fc6d4b86e014acd36e8f0f9ffe74fa31c53ce71ff255c2289e11e9c2606d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b68a5c4074a80a2bc5799134c0abea39b97d041de070648f2edac64131f7534)
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
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''The ARN of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @application_arn.setter
    def application_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__991b96fa7affbe3e674886c56e8c99de877d878da156c1eecdb8136f55e15535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationArn", value)

    @builtins.property
    @jsii.member(jsii_name="fleetName")
    def fleet_name(self) -> builtins.str:
        '''The name of the fleet.'''
        return typing.cast(builtins.str, jsii.get(self, "fleetName"))

    @fleet_name.setter
    def fleet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0aaa8270f20c093ca5740d4e9601ed61163065bb9b02b6ff293151ec389d60e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnApplicationFleetAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn", "fleet_name": "fleetName"},
)
class CfnApplicationFleetAssociationProps:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        fleet_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnApplicationFleetAssociation``.

        :param application_arn: The ARN of the application.
        :param fleet_name: The name of the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationfleetassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_application_fleet_association_props = appstream.CfnApplicationFleetAssociationProps(
                application_arn="applicationArn",
                fleet_name="fleetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d294820a31c019b7ec8574f34a068e3a21437c2751ab65ed99beb677455d420a)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument fleet_name", value=fleet_name, expected_type=type_hints["fleet_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "fleet_name": fleet_name,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ARN of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationfleetassociation.html#cfn-appstream-applicationfleetassociation-applicationarn
        '''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fleet_name(self) -> builtins.str:
        '''The name of the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationfleetassociation.html#cfn-appstream-applicationfleetassociation-fleetname
        '''
        result = self._values.get("fleet_name")
        assert result is not None, "Required property 'fleet_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationFleetAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_block_arn": "appBlockArn",
        "icon_s3_location": "iconS3Location",
        "instance_families": "instanceFamilies",
        "launch_path": "launchPath",
        "name": "name",
        "platforms": "platforms",
        "attributes_to_delete": "attributesToDelete",
        "description": "description",
        "display_name": "displayName",
        "launch_parameters": "launchParameters",
        "tags": "tags",
        "working_directory": "workingDirectory",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        app_block_arn: builtins.str,
        icon_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
        instance_families: typing.Sequence[builtins.str],
        launch_path: builtins.str,
        name: builtins.str,
        platforms: typing.Sequence[builtins.str],
        attributes_to_delete: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        launch_parameters: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param app_block_arn: The app block ARN with which the application should be associated.
        :param icon_s3_location: The icon S3 location of the application.
        :param instance_families: The instance families the application supports. *Allowed Values* : ``GENERAL_PURPOSE`` | ``GRAPHICS_G4``
        :param launch_path: The launch path of the application.
        :param name: The name of the application. This name is visible to users when a name is not specified in the DisplayName property. *Pattern* : ``^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$``
        :param platforms: The platforms the application supports. *Allowed Values* : ``WINDOWS_SERVER_2019`` | ``AMAZON_LINUX2``
        :param attributes_to_delete: A list of attributes to delete from an application.
        :param description: The description of the application.
        :param display_name: The display name of the application. This name is visible to users in the application catalog.
        :param launch_parameters: The launch parameters of the application.
        :param tags: The tags of the application.
        :param working_directory: The working directory of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_application_props = appstream.CfnApplicationProps(
                app_block_arn="appBlockArn",
                icon_s3_location=appstream.CfnApplication.S3LocationProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                ),
                instance_families=["instanceFamilies"],
                launch_path="launchPath",
                name="name",
                platforms=["platforms"],
            
                # the properties below are optional
                attributes_to_delete=["attributesToDelete"],
                description="description",
                display_name="displayName",
                launch_parameters="launchParameters",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                working_directory="workingDirectory"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb96c46dcf41b8bf52ccede1fadb0b2ffaef8995b618f1e0816e434f6605e2f2)
            check_type(argname="argument app_block_arn", value=app_block_arn, expected_type=type_hints["app_block_arn"])
            check_type(argname="argument icon_s3_location", value=icon_s3_location, expected_type=type_hints["icon_s3_location"])
            check_type(argname="argument instance_families", value=instance_families, expected_type=type_hints["instance_families"])
            check_type(argname="argument launch_path", value=launch_path, expected_type=type_hints["launch_path"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument platforms", value=platforms, expected_type=type_hints["platforms"])
            check_type(argname="argument attributes_to_delete", value=attributes_to_delete, expected_type=type_hints["attributes_to_delete"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument launch_parameters", value=launch_parameters, expected_type=type_hints["launch_parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_block_arn": app_block_arn,
            "icon_s3_location": icon_s3_location,
            "instance_families": instance_families,
            "launch_path": launch_path,
            "name": name,
            "platforms": platforms,
        }
        if attributes_to_delete is not None:
            self._values["attributes_to_delete"] = attributes_to_delete
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if launch_parameters is not None:
            self._values["launch_parameters"] = launch_parameters
        if tags is not None:
            self._values["tags"] = tags
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def app_block_arn(self) -> builtins.str:
        '''The app block ARN with which the application should be associated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-appblockarn
        '''
        result = self._values.get("app_block_arn")
        assert result is not None, "Required property 'app_block_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def icon_s3_location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnApplication.S3LocationProperty]:
        '''The icon S3 location of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-icons3location
        '''
        result = self._values.get("icon_s3_location")
        assert result is not None, "Required property 'icon_s3_location' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnApplication.S3LocationProperty], result)

    @builtins.property
    def instance_families(self) -> typing.List[builtins.str]:
        '''The instance families the application supports.

        *Allowed Values* : ``GENERAL_PURPOSE`` | ``GRAPHICS_G4``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-instancefamilies
        '''
        result = self._values.get("instance_families")
        assert result is not None, "Required property 'instance_families' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def launch_path(self) -> builtins.str:
        '''The launch path of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-launchpath
        '''
        result = self._values.get("launch_path")
        assert result is not None, "Required property 'launch_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the application.

        This name is visible to users when a name is not specified in the DisplayName property.

        *Pattern* : ``^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platforms(self) -> typing.List[builtins.str]:
        '''The platforms the application supports.

        *Allowed Values* : ``WINDOWS_SERVER_2019`` | ``AMAZON_LINUX2``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-platforms
        '''
        result = self._values.get("platforms")
        assert result is not None, "Required property 'platforms' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def attributes_to_delete(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of attributes to delete from an application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-attributestodelete
        '''
        result = self._values.get("attributes_to_delete")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the application.

        This name is visible to users in the application catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_parameters(self) -> typing.Optional[builtins.str]:
        '''The launch parameters of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-launchparameters
        '''
        result = self._values.get("launch_parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-workingdirectory
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDirectoryConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnDirectoryConfig",
):
    '''The ``AWS::AppStream::DirectoryConfig`` resource specifies the configuration information required to join Amazon AppStream 2.0 fleets and image builders to Microsoft Active Directory domains.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html
    :cloudformationResource: AWS::AppStream::DirectoryConfig
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_directory_config = appstream.CfnDirectoryConfig(self, "MyCfnDirectoryConfig",
            directory_name="directoryName",
            organizational_unit_distinguished_names=["organizationalUnitDistinguishedNames"],
            service_account_credentials=appstream.CfnDirectoryConfig.ServiceAccountCredentialsProperty(
                account_name="accountName",
                account_password="accountPassword"
            ),
        
            # the properties below are optional
            certificate_based_auth_properties=appstream.CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty(
                certificate_authority_arn="certificateAuthorityArn",
                status="status"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        directory_name: builtins.str,
        organizational_unit_distinguished_names: typing.Sequence[builtins.str],
        service_account_credentials: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDirectoryConfig.ServiceAccountCredentialsProperty", typing.Dict[builtins.str, typing.Any]]],
        certificate_based_auth_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param directory_name: The fully qualified name of the directory (for example, corp.example.com).
        :param organizational_unit_distinguished_names: The distinguished names of the organizational units for computer accounts.
        :param service_account_credentials: The credentials for the service account used by the streaming instance to connect to the directory. Do not use this parameter directly. Use ``ServiceAccountCredentials`` as an input parameter with ``noEcho`` as shown in the `Parameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html>`_ . For best practices information, see `Do Not Embed Credentials in Your Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html#creds>`_ .
        :param certificate_based_auth_properties: The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__038372f18e366a333df8768cd289dcbe82f03750464d283eb0ef89fcbf90577c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDirectoryConfigProps(
            directory_name=directory_name,
            organizational_unit_distinguished_names=organizational_unit_distinguished_names,
            service_account_credentials=service_account_credentials,
            certificate_based_auth_properties=certificate_based_auth_properties,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d97debe358c81c37b199083a9ccbc136be57ab6cd95df38a148a3fd2ea188f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e54e8ff33797aab702918ecb86bf9eed890a16455e3ff48b3d67bc488b6818e)
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
    @jsii.member(jsii_name="directoryName")
    def directory_name(self) -> builtins.str:
        '''The fully qualified name of the directory (for example, corp.example.com).'''
        return typing.cast(builtins.str, jsii.get(self, "directoryName"))

    @directory_name.setter
    def directory_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__671a9ec8a1b2b5d0d93643e14e6916b2417e5e73e7134aebc9f410fbb98d7c7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitDistinguishedNames")
    def organizational_unit_distinguished_names(self) -> typing.List[builtins.str]:
        '''The distinguished names of the organizational units for computer accounts.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "organizationalUnitDistinguishedNames"))

    @organizational_unit_distinguished_names.setter
    def organizational_unit_distinguished_names(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__630eb00e19cb58292c211d1a006f8dd52b859f57c892e7425b2fb0cd1f62b762)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnitDistinguishedNames", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountCredentials")
    def service_account_credentials(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDirectoryConfig.ServiceAccountCredentialsProperty"]:
        '''The credentials for the service account used by the streaming instance to connect to the directory.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDirectoryConfig.ServiceAccountCredentialsProperty"], jsii.get(self, "serviceAccountCredentials"))

    @service_account_credentials.setter
    def service_account_credentials(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDirectoryConfig.ServiceAccountCredentialsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3f17c467f37ff964c4e56ff7a5b6800877e168375f3aa44347e71dee2de5ef8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="certificateBasedAuthProperties")
    def certificate_based_auth_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty"]]:
        '''The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty"]], jsii.get(self, "certificateBasedAuthProperties"))

    @certificate_based_auth_properties.setter
    def certificate_based_auth_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89617ee3f9d3ab9cc3d861814bdbc0f0dcde8b3fb5da771e78c8feccf0a3e19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateBasedAuthProperties", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_authority_arn": "certificateAuthorityArn",
            "status": "status",
        },
    )
    class CertificateBasedAuthPropertiesProperty:
        def __init__(
            self,
            *,
            certificate_authority_arn: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances.

            :param certificate_authority_arn: The ARN of the AWS Certificate Manager Private CA resource.
            :param status: The status of the certificate-based authentication properties. Fallback is turned on by default when certificate-based authentication is *Enabled* . Fallback allows users to log in using their AD domain password if certificate-based authentication is unsuccessful, or to unlock a desktop lock screen. *Enabled_no_directory_login_fallback* enables certificate-based authentication, but does not allow users to log in using their AD domain password. Users will be disconnected to re-authenticate using certificates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-certificatebasedauthproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                certificate_based_auth_properties_property = appstream.CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty(
                    certificate_authority_arn="certificateAuthorityArn",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ffca79fb887aa55066c3b8724a3bdc6f8de1654ed6be4ef85d6468ed7ed950ca)
                check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_authority_arn is not None:
                self._values["certificate_authority_arn"] = certificate_authority_arn
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def certificate_authority_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the AWS Certificate Manager Private CA resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-certificatebasedauthproperties.html#cfn-appstream-directoryconfig-certificatebasedauthproperties-certificateauthorityarn
            '''
            result = self._values.get("certificate_authority_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the certificate-based authentication properties.

            Fallback is turned on by default when certificate-based authentication is *Enabled* . Fallback allows users to log in using their AD domain password if certificate-based authentication is unsuccessful, or to unlock a desktop lock screen. *Enabled_no_directory_login_fallback* enables certificate-based authentication, but does not allow users to log in using their AD domain password. Users will be disconnected to re-authenticate using certificates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-certificatebasedauthproperties.html#cfn-appstream-directoryconfig-certificatebasedauthproperties-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CertificateBasedAuthPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnDirectoryConfig.ServiceAccountCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_name": "accountName",
            "account_password": "accountPassword",
        },
    )
    class ServiceAccountCredentialsProperty:
        def __init__(
            self,
            *,
            account_name: builtins.str,
            account_password: builtins.str,
        ) -> None:
            '''The credentials for the service account used by the streaming instance to connect to the directory.

            :param account_name: The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
            :param account_password: The password for the account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                service_account_credentials_property = appstream.CfnDirectoryConfig.ServiceAccountCredentialsProperty(
                    account_name="accountName",
                    account_password="accountPassword"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__844f7de5d43ef3bfc92f8ee34800439d7fe27186f269bed1be021e10ee58164f)
                check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
                check_type(argname="argument account_password", value=account_password, expected_type=type_hints["account_password"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_name": account_name,
                "account_password": account_password,
            }

        @builtins.property
        def account_name(self) -> builtins.str:
            '''The user name of the account.

            This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html#cfn-appstream-directoryconfig-serviceaccountcredentials-accountname
            '''
            result = self._values.get("account_name")
            assert result is not None, "Required property 'account_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_password(self) -> builtins.str:
            '''The password for the account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html#cfn-appstream-directoryconfig-serviceaccountcredentials-accountpassword
            '''
            result = self._values.get("account_password")
            assert result is not None, "Required property 'account_password' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceAccountCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnDirectoryConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "directory_name": "directoryName",
        "organizational_unit_distinguished_names": "organizationalUnitDistinguishedNames",
        "service_account_credentials": "serviceAccountCredentials",
        "certificate_based_auth_properties": "certificateBasedAuthProperties",
    },
)
class CfnDirectoryConfigProps:
    def __init__(
        self,
        *,
        directory_name: builtins.str,
        organizational_unit_distinguished_names: typing.Sequence[builtins.str],
        service_account_credentials: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryConfig.ServiceAccountCredentialsProperty, typing.Dict[builtins.str, typing.Any]]],
        certificate_based_auth_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDirectoryConfig``.

        :param directory_name: The fully qualified name of the directory (for example, corp.example.com).
        :param organizational_unit_distinguished_names: The distinguished names of the organizational units for computer accounts.
        :param service_account_credentials: The credentials for the service account used by the streaming instance to connect to the directory. Do not use this parameter directly. Use ``ServiceAccountCredentials`` as an input parameter with ``noEcho`` as shown in the `Parameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html>`_ . For best practices information, see `Do Not Embed Credentials in Your Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html#creds>`_ .
        :param certificate_based_auth_properties: The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_directory_config_props = appstream.CfnDirectoryConfigProps(
                directory_name="directoryName",
                organizational_unit_distinguished_names=["organizationalUnitDistinguishedNames"],
                service_account_credentials=appstream.CfnDirectoryConfig.ServiceAccountCredentialsProperty(
                    account_name="accountName",
                    account_password="accountPassword"
                ),
            
                # the properties below are optional
                certificate_based_auth_properties=appstream.CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty(
                    certificate_authority_arn="certificateAuthorityArn",
                    status="status"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__578684e8816c2df1e186869cdebb5605355669857041d859dd30c2859c435801)
            check_type(argname="argument directory_name", value=directory_name, expected_type=type_hints["directory_name"])
            check_type(argname="argument organizational_unit_distinguished_names", value=organizational_unit_distinguished_names, expected_type=type_hints["organizational_unit_distinguished_names"])
            check_type(argname="argument service_account_credentials", value=service_account_credentials, expected_type=type_hints["service_account_credentials"])
            check_type(argname="argument certificate_based_auth_properties", value=certificate_based_auth_properties, expected_type=type_hints["certificate_based_auth_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory_name": directory_name,
            "organizational_unit_distinguished_names": organizational_unit_distinguished_names,
            "service_account_credentials": service_account_credentials,
        }
        if certificate_based_auth_properties is not None:
            self._values["certificate_based_auth_properties"] = certificate_based_auth_properties

    @builtins.property
    def directory_name(self) -> builtins.str:
        '''The fully qualified name of the directory (for example, corp.example.com).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html#cfn-appstream-directoryconfig-directoryname
        '''
        result = self._values.get("directory_name")
        assert result is not None, "Required property 'directory_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organizational_unit_distinguished_names(self) -> typing.List[builtins.str]:
        '''The distinguished names of the organizational units for computer accounts.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html#cfn-appstream-directoryconfig-organizationalunitdistinguishednames
        '''
        result = self._values.get("organizational_unit_distinguished_names")
        assert result is not None, "Required property 'organizational_unit_distinguished_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def service_account_credentials(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDirectoryConfig.ServiceAccountCredentialsProperty]:
        '''The credentials for the service account used by the streaming instance to connect to the directory.

        Do not use this parameter directly. Use ``ServiceAccountCredentials`` as an input parameter with ``noEcho`` as shown in the `Parameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html>`_ . For best practices information, see `Do Not Embed Credentials in Your Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html#creds>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html#cfn-appstream-directoryconfig-serviceaccountcredentials
        '''
        result = self._values.get("service_account_credentials")
        assert result is not None, "Required property 'service_account_credentials' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDirectoryConfig.ServiceAccountCredentialsProperty], result)

    @builtins.property
    def certificate_based_auth_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty]]:
        '''The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html#cfn-appstream-directoryconfig-certificatebasedauthproperties
        '''
        result = self._values.get("certificate_based_auth_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDirectoryConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEntitlement(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnEntitlement",
):
    '''Creates an entitlement to control access, based on user attributes, to specific applications within a stack.

    Entitlements apply to SAML 2.0 federated user identities. Amazon AppStream 2.0 user pool and streaming URL users are entitled to all applications in a stack. Entitlements don't apply to the desktop stream view application or to applications managed by a dynamic app provider using the Dynamic Application Framework.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html
    :cloudformationResource: AWS::AppStream::Entitlement
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_entitlement = appstream.CfnEntitlement(self, "MyCfnEntitlement",
            app_visibility="appVisibility",
            attributes=[appstream.CfnEntitlement.AttributeProperty(
                name="name",
                value="value"
            )],
            name="name",
            stack_name="stackName",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        app_visibility: builtins.str,
        attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEntitlement.AttributeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        stack_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_visibility: Specifies whether to entitle all apps or only selected apps.
        :param attributes: The attributes of the entitlement.
        :param name: The name of the entitlement.
        :param stack_name: The name of the stack.
        :param description: The description of the entitlement.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0bfa3b98fc526a6a563308a8862238ce51273e7eb19d8bbebd7a86fb7e44502)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEntitlementProps(
            app_visibility=app_visibility,
            attributes=attributes,
            name=name,
            stack_name=stack_name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c9d56192f87abfa7e1a4fabdb31d1a5e1d437fd8216f9858ffda414e951d660)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2437978a9ad12b18d2e3ddda0a06cabe403a32e8fb2c71839868ba72be02671)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''The time when the entitlement was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''The time when the entitlement was last modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="appVisibility")
    def app_visibility(self) -> builtins.str:
        '''Specifies whether to entitle all apps or only selected apps.'''
        return typing.cast(builtins.str, jsii.get(self, "appVisibility"))

    @app_visibility.setter
    def app_visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db254c441b5a86a836711719ab5bafae630e66529b39f62dee4c510a7e5d9cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEntitlement.AttributeProperty"]]]:
        '''The attributes of the entitlement.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEntitlement.AttributeProperty"]]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEntitlement.AttributeProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa3674f46bbe39146e43d1c3c58c9be8a7fa2b7972b4709b3fa29dcf86420d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the entitlement.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1b3d753cadafb7385d25d134e4181963f7a41b9f8b44225981b664b92c82d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        '''The name of the stack.'''
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @stack_name.setter
    def stack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f2d532168c00c02bedd8960de80d1d1be3ec7880a902292ec08e8f01dfc689b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the entitlement.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__545e3c21562a3817f7c25161b610d37ec5b881d014fc1d9d876354a51c3fcd29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnEntitlement.AttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class AttributeProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''An attribute that belongs to an entitlement.

            Application entitlements work by matching a supported SAML 2.0 attribute name to a value when a user identity federates to an AppStream 2.0 SAML application.

            :param name: A supported AWS IAM SAML PrincipalTag attribute that is matched to a value when a user identity federates to an AppStream 2.0 SAML application. The following are supported values: - roles - department - organization - groups - title - costCenter - userType
            :param value: A value that is matched to a supported SAML attribute name when a user identity federates to an AppStream 2.0 SAML application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-entitlement-attribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                attribute_property = appstream.CfnEntitlement.AttributeProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c09f476db6997870a53f0b29bef4fa36a8d180cbfb901e0f9e6f0fdfb04778de)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''A supported AWS IAM SAML PrincipalTag attribute that is matched to a value when a user identity federates to an AppStream 2.0 SAML application.

            The following are supported values:

            - roles
            - department
            - organization
            - groups
            - title
            - costCenter
            - userType

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-entitlement-attribute.html#cfn-appstream-entitlement-attribute-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''A value that is matched to a supported SAML attribute name when a user identity federates to an AppStream 2.0 SAML application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-entitlement-attribute.html#cfn-appstream-entitlement-attribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnEntitlementProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_visibility": "appVisibility",
        "attributes": "attributes",
        "name": "name",
        "stack_name": "stackName",
        "description": "description",
    },
)
class CfnEntitlementProps:
    def __init__(
        self,
        *,
        app_visibility: builtins.str,
        attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEntitlement.AttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        stack_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEntitlement``.

        :param app_visibility: Specifies whether to entitle all apps or only selected apps.
        :param attributes: The attributes of the entitlement.
        :param name: The name of the entitlement.
        :param stack_name: The name of the stack.
        :param description: The description of the entitlement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_entitlement_props = appstream.CfnEntitlementProps(
                app_visibility="appVisibility",
                attributes=[appstream.CfnEntitlement.AttributeProperty(
                    name="name",
                    value="value"
                )],
                name="name",
                stack_name="stackName",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e7b6ad14b42e5a4dc8b1f0be3cc48eb3f96a7fc22176cfee8fe233b842ca6c9)
            check_type(argname="argument app_visibility", value=app_visibility, expected_type=type_hints["app_visibility"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_visibility": app_visibility,
            "attributes": attributes,
            "name": name,
            "stack_name": stack_name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def app_visibility(self) -> builtins.str:
        '''Specifies whether to entitle all apps or only selected apps.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-appvisibility
        '''
        result = self._values.get("app_visibility")
        assert result is not None, "Required property 'app_visibility' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEntitlement.AttributeProperty]]]:
        '''The attributes of the entitlement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-attributes
        '''
        result = self._values.get("attributes")
        assert result is not None, "Required property 'attributes' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEntitlement.AttributeProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the entitlement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The name of the stack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-stackname
        '''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the entitlement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEntitlementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnFleet",
):
    '''The ``AWS::AppStream::Fleet`` resource creates a fleet for Amazon AppStream 2.0. A fleet consists of streaming instances that run a specified image when using Always-On or On-Demand.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html
    :cloudformationResource: AWS::AppStream::Fleet
    :exampleMetadata: infused

    Example::

        fleet = appstream.CfnFleet(self, "Fleet",
            instance_type="stream.standard.small",
            name="Fleet",
            compute_capacity=appstream.CfnFleet.ComputeCapacityProperty(
                desired_instances=1
            ),
            image_name="AppStream-AmazonLinux2-09-21-2022"
        )
        fleet.cfn_options.creation_policy = CfnCreationPolicy(
            start_fleet=True
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_type: builtins.str,
        name: builtins.str,
        compute_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ComputeCapacityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        display_name: typing.Optional[builtins.str] = None,
        domain_join_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.DomainJoinInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        idle_disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        image_arn: typing.Optional[builtins.str] = None,
        image_name: typing.Optional[builtins.str] = None,
        max_concurrent_sessions: typing.Optional[jsii.Number] = None,
        max_sessions_per_instance: typing.Optional[jsii.Number] = None,
        max_user_duration_in_seconds: typing.Optional[jsii.Number] = None,
        platform: typing.Optional[builtins.str] = None,
        session_script_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        stream_view: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        usb_device_filter_strings: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_type: The instance type to use when launching fleet instances. The following instance types are available for non-Elastic fleets:. - stream.standard.small - stream.standard.medium - stream.standard.large - stream.compute.large - stream.compute.xlarge - stream.compute.2xlarge - stream.compute.4xlarge - stream.compute.8xlarge - stream.memory.large - stream.memory.xlarge - stream.memory.2xlarge - stream.memory.4xlarge - stream.memory.8xlarge - stream.memory.z1d.large - stream.memory.z1d.xlarge - stream.memory.z1d.2xlarge - stream.memory.z1d.3xlarge - stream.memory.z1d.6xlarge - stream.memory.z1d.12xlarge - stream.graphics-design.large - stream.graphics-design.xlarge - stream.graphics-design.2xlarge - stream.graphics-design.4xlarge - stream.graphics-desktop.2xlarge - stream.graphics.g4dn.xlarge - stream.graphics.g4dn.2xlarge - stream.graphics.g4dn.4xlarge - stream.graphics.g4dn.8xlarge - stream.graphics.g4dn.12xlarge - stream.graphics.g4dn.16xlarge - stream.graphics-pro.4xlarge - stream.graphics-pro.8xlarge - stream.graphics-pro.16xlarge The following instance types are available for Elastic fleets: - stream.standard.small - stream.standard.medium
        :param name: A unique name for the fleet.
        :param compute_capacity: The desired capacity for the fleet. This is not allowed for Elastic fleets.
        :param description: The description to display.
        :param disconnect_timeout_in_seconds: The amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance. Specify a value between 60 and 36000.
        :param display_name: The fleet name to display.
        :param domain_join_info: The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain. This is not allowed for Elastic fleets.
        :param enable_default_internet_access: Enables or disables default internet access for the fleet.
        :param fleet_type: The fleet type. - **ALWAYS_ON** - Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps. - **ON_DEMAND** - Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps. - **ELASTIC** - The pool of streaming instances is managed by Amazon AppStream 2.0. When a user selects their application or desktop to launch, they will start streaming after the app block has been downloaded and mounted to a streaming instance. *Allowed Values* : ``ALWAYS_ON`` | ``ELASTIC`` | ``ON_DEMAND``
        :param iam_role_arn: The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance calls the AWS Security Token Service ``AssumeRole`` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the *appstream_machine_role* credential profile on the instance. For more information, see `Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`_ in the *Amazon AppStream 2.0 Administration Guide* .
        :param idle_disconnect_timeout_in_seconds: The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins. Users are notified before they are disconnected due to inactivity. If they try to reconnect to the streaming session before the time interval specified in ``DisconnectTimeoutInSeconds`` elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in ``IdleDisconnectTimeoutInSeconds`` elapses, they are disconnected. To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000. If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.
        :param image_arn: The ARN of the public, private, or shared image to use.
        :param image_name: The name of the image used to create the fleet.
        :param max_concurrent_sessions: The maximum number of concurrent sessions that can be run on an Elastic fleet. This setting is required for Elastic fleets, but is not used for other fleet types.
        :param max_sessions_per_instance: Max number of user sessions on an instance. This is applicable only for multi-session fleets.
        :param max_user_duration_in_seconds: The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance. Specify a value between 600 and 432000.
        :param platform: The platform of the fleet. Platform is a required setting for Elastic fleets, and is not used for other fleet types.
        :param session_script_s3_location: The S3 location of the session scripts configuration zip file. This only applies to Elastic fleets.
        :param stream_view: The AppStream 2.0 view that is displayed to your users when they stream from the fleet. When ``APP`` is specified, only the windows of applications opened by users display. When ``DESKTOP`` is specified, the standard desktop that is provided by the operating system displays. The default value is ``APP`` .
        :param tags: An array of key-value pairs.
        :param usb_device_filter_strings: The USB device filter strings that specify which USB devices a user can redirect to the fleet streaming session, when using the Windows native client. This is allowed but not required for Elastic fleets.
        :param vpc_config: The VPC configuration for the fleet. This is required for Elastic fleets, but not required for other fleet types.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__043ee41cbba03b784a0f77c0a2cc8efea9ae9147537890e0795e729547d5d4ff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFleetProps(
            instance_type=instance_type,
            name=name,
            compute_capacity=compute_capacity,
            description=description,
            disconnect_timeout_in_seconds=disconnect_timeout_in_seconds,
            display_name=display_name,
            domain_join_info=domain_join_info,
            enable_default_internet_access=enable_default_internet_access,
            fleet_type=fleet_type,
            iam_role_arn=iam_role_arn,
            idle_disconnect_timeout_in_seconds=idle_disconnect_timeout_in_seconds,
            image_arn=image_arn,
            image_name=image_name,
            max_concurrent_sessions=max_concurrent_sessions,
            max_sessions_per_instance=max_sessions_per_instance,
            max_user_duration_in_seconds=max_user_duration_in_seconds,
            platform=platform,
            session_script_s3_location=session_script_s3_location,
            stream_view=stream_view,
            tags=tags,
            usb_device_filter_strings=usb_device_filter_strings,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9a64a6d87c0b62f880d7b34e935538ef5f5648fee18223b97400ee72688a9f7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__84d551b4b29a3f115fdadd7697e1de7bb10702e2036e3a25e4556a54087e402b)
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
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''The instance type to use when launching fleet instances.

        The following instance types are available for non-Elastic fleets:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a6ef061b0bedfe2a4a7f001125bc3274c3704e34a43dc8418d62592df836097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A unique name for the fleet.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e2214e24b9fd1c11c53bebf170bcc6e7c03917559f47d5d33ea2525089fdf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="computeCapacity")
    def compute_capacity(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ComputeCapacityProperty"]]:
        '''The desired capacity for the fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ComputeCapacityProperty"]], jsii.get(self, "computeCapacity"))

    @compute_capacity.setter
    def compute_capacity(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ComputeCapacityProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50699376ca4215fbf67913c64e0ae0edb7e243785d08cef6bc529f44ca0f141a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to display.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9409234ac32054c73634d4ffe5cc51eed2d25f9373a83380b7693f06ff5a9e56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disconnectTimeoutInSeconds")
    def disconnect_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The amount of time that a streaming session remains active after users disconnect.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "disconnectTimeoutInSeconds"))

    @disconnect_timeout_in_seconds.setter
    def disconnect_timeout_in_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7b891e70c70c71b4742be14d3dd1903d0ec64bb461a57f0aa83d3997a151dfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disconnectTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The fleet name to display.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5f49946d1e23d200d37b1f8ea8f79d9757a1da17de932a0c0617ac288ddf5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="domainJoinInfo")
    def domain_join_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.DomainJoinInfoProperty"]]:
        '''The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.DomainJoinInfoProperty"]], jsii.get(self, "domainJoinInfo"))

    @domain_join_info.setter
    def domain_join_info(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.DomainJoinInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd86f9dbfba3a27b2385e8b9586bb3aa31b4e2aa0a3e91794b42a6881add1126)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainJoinInfo", value)

    @builtins.property
    @jsii.member(jsii_name="enableDefaultInternetAccess")
    def enable_default_internet_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables or disables default internet access for the fleet.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableDefaultInternetAccess"))

    @enable_default_internet_access.setter
    def enable_default_internet_access(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f219b4aa3da3a06d8016cbf3252298a91c9c2811252b39c6ac9adb9b2e3ee798)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDefaultInternetAccess", value)

    @builtins.property
    @jsii.member(jsii_name="fleetType")
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''The fleet type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fleetType"))

    @fleet_type.setter
    def fleet_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51b3228ce2b0c145877b00c8bf4eca31f4e517d5cbe1d8f39944f113c7aaabce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetType", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that is applied to the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89ee05e008a0394f50d61a211df9373128f6625ffc891f8343efa62cdde56436)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="idleDisconnectTimeoutInSeconds")
    def idle_disconnect_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleDisconnectTimeoutInSeconds"))

    @idle_disconnect_timeout_in_seconds.setter
    def idle_disconnect_timeout_in_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53b211e70fac8180eefa6a9dd10825d32317d051e002818d8c808f7cb493697e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleDisconnectTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="imageArn")
    def image_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the public, private, or shared image to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageArn"))

    @image_arn.setter
    def image_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edf3360ada81e5be766ffda88924f99bb0bc36a7f9cd324041b71f987c4ad249)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageArn", value)

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> typing.Optional[builtins.str]:
        '''The name of the image used to create the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2ecac5e12920461571674f2b4175ac2b87887d3edba0db37def3d12d002088)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentSessions")
    def max_concurrent_sessions(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of concurrent sessions that can be run on an Elastic fleet.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentSessions"))

    @max_concurrent_sessions.setter
    def max_concurrent_sessions(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cef147ceca130b53c86908dc50dff718cb362a4b25c765b783420d7115404ded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentSessions", value)

    @builtins.property
    @jsii.member(jsii_name="maxSessionsPerInstance")
    def max_sessions_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Max number of user sessions on an instance.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSessionsPerInstance"))

    @max_sessions_per_instance.setter
    def max_sessions_per_instance(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d2d0956b116cf95d995d13ffce00e3483d95f5d61d41f2e9bc4202eb0997e48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSessionsPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="maxUserDurationInSeconds")
    def max_user_duration_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of time that a streaming session can remain active, in seconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUserDurationInSeconds"))

    @max_user_duration_in_seconds.setter
    def max_user_duration_in_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb6ad7b5fa21e0983e0e093b56d8c6bae1f0e93752767339c1b9bf91621aacf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUserDurationInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> typing.Optional[builtins.str]:
        '''The platform of the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9129dd496d9b4790cdd5f195fbd566cf9b4924df5068de89d89903c26def0d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="sessionScriptS3Location")
    def session_script_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.S3LocationProperty"]]:
        '''The S3 location of the session scripts configuration zip file.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.S3LocationProperty"]], jsii.get(self, "sessionScriptS3Location"))

    @session_script_s3_location.setter
    def session_script_s3_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79935e15ee3dfe1dba785d906ccdd9a4e5895f1d61d25026dbdddf01558f5be8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionScriptS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="streamView")
    def stream_view(self) -> typing.Optional[builtins.str]:
        '''The AppStream 2.0 view that is displayed to your users when they stream from the fleet. When ``APP`` is specified, only the windows of applications opened by users display. When ``DESKTOP`` is specified, the standard desktop that is provided by the operating system displays.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamView"))

    @stream_view.setter
    def stream_view(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab9bf4177a813f1507a9cefa186c313a820bdfb89dd6791547c863e11771a203)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamView", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__839d0da01c455496fc067fbca5ed5c23c8fb170e5989a05bf711b7b574b7d416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="usbDeviceFilterStrings")
    def usb_device_filter_strings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The USB device filter strings that specify which USB devices a user can redirect to the fleet streaming session, when using the Windows native client.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "usbDeviceFilterStrings"))

    @usb_device_filter_strings.setter
    def usb_device_filter_strings(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3e185c1216c446ebc68c660e2e3cc0b3515ddb113048def6faa8bd38653a80e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usbDeviceFilterStrings", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.VpcConfigProperty"]]:
        '''The VPC configuration for the fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.VpcConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8452c6c1c918a8718280c5b321c677cd442bc97d2e69bc3f9aaa1690c901ffc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnFleet.ComputeCapacityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "desired_instances": "desiredInstances",
            "desired_sessions": "desiredSessions",
        },
    )
    class ComputeCapacityProperty:
        def __init__(
            self,
            *,
            desired_instances: typing.Optional[jsii.Number] = None,
            desired_sessions: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The desired capacity for a fleet.

            :param desired_instances: The desired number of streaming instances.
            :param desired_sessions: The desired capacity in terms of number of user sessions, for the multi-session fleet. This is not allowed for single-session fleets. When you create a fleet, you must set define either the DesiredSessions or DesiredInstances attribute, based on the type of fleet you create. You can’t define both attributes or leave both attributes blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                compute_capacity_property = appstream.CfnFleet.ComputeCapacityProperty(
                    desired_instances=123,
                    desired_sessions=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__87ca5878c0aa8c5995893aac0046342d8942452bc466a936ffbf559e60bbe3bb)
                check_type(argname="argument desired_instances", value=desired_instances, expected_type=type_hints["desired_instances"])
                check_type(argname="argument desired_sessions", value=desired_sessions, expected_type=type_hints["desired_sessions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if desired_instances is not None:
                self._values["desired_instances"] = desired_instances
            if desired_sessions is not None:
                self._values["desired_sessions"] = desired_sessions

        @builtins.property
        def desired_instances(self) -> typing.Optional[jsii.Number]:
            '''The desired number of streaming instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html#cfn-appstream-fleet-computecapacity-desiredinstances
            '''
            result = self._values.get("desired_instances")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def desired_sessions(self) -> typing.Optional[jsii.Number]:
            '''The desired capacity in terms of number of user sessions, for the multi-session fleet.

            This is not allowed for single-session fleets.

            When you create a fleet, you must set define either the DesiredSessions or DesiredInstances attribute, based on the type of fleet you create. You can’t define both attributes or leave both attributes blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html#cfn-appstream-fleet-computecapacity-desiredsessions
            '''
            result = self._values.get("desired_sessions")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeCapacityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnFleet.DomainJoinInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_name": "directoryName",
            "organizational_unit_distinguished_name": "organizationalUnitDistinguishedName",
        },
    )
    class DomainJoinInfoProperty:
        def __init__(
            self,
            *,
            directory_name: typing.Optional[builtins.str] = None,
            organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The name of the directory and organizational unit (OU) to use to join a fleet to a Microsoft Active Directory domain.

            :param directory_name: The fully qualified name of the directory (for example, corp.example.com).
            :param organizational_unit_distinguished_name: The distinguished name of the organizational unit for computer accounts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                domain_join_info_property = appstream.CfnFleet.DomainJoinInfoProperty(
                    directory_name="directoryName",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ce7aedf15d7749daa18c62b97de590b90b107ea31ce355c68f50a78346fbbe6)
                check_type(argname="argument directory_name", value=directory_name, expected_type=type_hints["directory_name"])
                check_type(argname="argument organizational_unit_distinguished_name", value=organizational_unit_distinguished_name, expected_type=type_hints["organizational_unit_distinguished_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if directory_name is not None:
                self._values["directory_name"] = directory_name
            if organizational_unit_distinguished_name is not None:
                self._values["organizational_unit_distinguished_name"] = organizational_unit_distinguished_name

        @builtins.property
        def directory_name(self) -> typing.Optional[builtins.str]:
            '''The fully qualified name of the directory (for example, corp.example.com).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html#cfn-appstream-fleet-domainjoininfo-directoryname
            '''
            result = self._values.get("directory_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit_distinguished_name(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The distinguished name of the organizational unit for computer accounts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html#cfn-appstream-fleet-domainjoininfo-organizationalunitdistinguishedname
            '''
            result = self._values.get("organizational_unit_distinguished_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainJoinInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnFleet.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_bucket": "s3Bucket", "s3_key": "s3Key"},
    )
    class S3LocationProperty:
        def __init__(self, *, s3_bucket: builtins.str, s3_key: builtins.str) -> None:
            '''Describes the S3 location.

            :param s3_bucket: The S3 bucket of the S3 object.
            :param s3_key: The S3 key of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                s3_location_property = appstream.CfnFleet.S3LocationProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aad58c387c2ce79f6cc90043caf5f503d6456bb90cde093dde2788eca29f15d9)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The S3 bucket of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-s3location.html#cfn-appstream-fleet-s3location-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''The S3 key of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-s3location.html#cfn-appstream-fleet-s3location-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnFleet.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The VPC configuration information for the fleet.

            :param security_group_ids: The identifiers of the security groups for the fleet.
            :param subnet_ids: The identifiers of the subnets to which a network interface is attached from the fleet instance. Fleet instances can use one or two subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                vpc_config_property = appstream.CfnFleet.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b84008983de6a1ed7aa5257a44cfb82723e58267dad7890bb77001fd73009f6d)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The identifiers of the security groups for the fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html#cfn-appstream-fleet-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The identifiers of the subnets to which a network interface is attached from the fleet instance.

            Fleet instances can use one or two subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html#cfn-appstream-fleet-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "name": "name",
        "compute_capacity": "computeCapacity",
        "description": "description",
        "disconnect_timeout_in_seconds": "disconnectTimeoutInSeconds",
        "display_name": "displayName",
        "domain_join_info": "domainJoinInfo",
        "enable_default_internet_access": "enableDefaultInternetAccess",
        "fleet_type": "fleetType",
        "iam_role_arn": "iamRoleArn",
        "idle_disconnect_timeout_in_seconds": "idleDisconnectTimeoutInSeconds",
        "image_arn": "imageArn",
        "image_name": "imageName",
        "max_concurrent_sessions": "maxConcurrentSessions",
        "max_sessions_per_instance": "maxSessionsPerInstance",
        "max_user_duration_in_seconds": "maxUserDurationInSeconds",
        "platform": "platform",
        "session_script_s3_location": "sessionScriptS3Location",
        "stream_view": "streamView",
        "tags": "tags",
        "usb_device_filter_strings": "usbDeviceFilterStrings",
        "vpc_config": "vpcConfig",
    },
)
class CfnFleetProps:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        name: builtins.str,
        compute_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ComputeCapacityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        display_name: typing.Optional[builtins.str] = None,
        domain_join_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.DomainJoinInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        idle_disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        image_arn: typing.Optional[builtins.str] = None,
        image_name: typing.Optional[builtins.str] = None,
        max_concurrent_sessions: typing.Optional[jsii.Number] = None,
        max_sessions_per_instance: typing.Optional[jsii.Number] = None,
        max_user_duration_in_seconds: typing.Optional[jsii.Number] = None,
        platform: typing.Optional[builtins.str] = None,
        session_script_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        stream_view: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        usb_device_filter_strings: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param instance_type: The instance type to use when launching fleet instances. The following instance types are available for non-Elastic fleets:. - stream.standard.small - stream.standard.medium - stream.standard.large - stream.compute.large - stream.compute.xlarge - stream.compute.2xlarge - stream.compute.4xlarge - stream.compute.8xlarge - stream.memory.large - stream.memory.xlarge - stream.memory.2xlarge - stream.memory.4xlarge - stream.memory.8xlarge - stream.memory.z1d.large - stream.memory.z1d.xlarge - stream.memory.z1d.2xlarge - stream.memory.z1d.3xlarge - stream.memory.z1d.6xlarge - stream.memory.z1d.12xlarge - stream.graphics-design.large - stream.graphics-design.xlarge - stream.graphics-design.2xlarge - stream.graphics-design.4xlarge - stream.graphics-desktop.2xlarge - stream.graphics.g4dn.xlarge - stream.graphics.g4dn.2xlarge - stream.graphics.g4dn.4xlarge - stream.graphics.g4dn.8xlarge - stream.graphics.g4dn.12xlarge - stream.graphics.g4dn.16xlarge - stream.graphics-pro.4xlarge - stream.graphics-pro.8xlarge - stream.graphics-pro.16xlarge The following instance types are available for Elastic fleets: - stream.standard.small - stream.standard.medium
        :param name: A unique name for the fleet.
        :param compute_capacity: The desired capacity for the fleet. This is not allowed for Elastic fleets.
        :param description: The description to display.
        :param disconnect_timeout_in_seconds: The amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance. Specify a value between 60 and 36000.
        :param display_name: The fleet name to display.
        :param domain_join_info: The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain. This is not allowed for Elastic fleets.
        :param enable_default_internet_access: Enables or disables default internet access for the fleet.
        :param fleet_type: The fleet type. - **ALWAYS_ON** - Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps. - **ON_DEMAND** - Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps. - **ELASTIC** - The pool of streaming instances is managed by Amazon AppStream 2.0. When a user selects their application or desktop to launch, they will start streaming after the app block has been downloaded and mounted to a streaming instance. *Allowed Values* : ``ALWAYS_ON`` | ``ELASTIC`` | ``ON_DEMAND``
        :param iam_role_arn: The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance calls the AWS Security Token Service ``AssumeRole`` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the *appstream_machine_role* credential profile on the instance. For more information, see `Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`_ in the *Amazon AppStream 2.0 Administration Guide* .
        :param idle_disconnect_timeout_in_seconds: The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins. Users are notified before they are disconnected due to inactivity. If they try to reconnect to the streaming session before the time interval specified in ``DisconnectTimeoutInSeconds`` elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in ``IdleDisconnectTimeoutInSeconds`` elapses, they are disconnected. To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000. If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.
        :param image_arn: The ARN of the public, private, or shared image to use.
        :param image_name: The name of the image used to create the fleet.
        :param max_concurrent_sessions: The maximum number of concurrent sessions that can be run on an Elastic fleet. This setting is required for Elastic fleets, but is not used for other fleet types.
        :param max_sessions_per_instance: Max number of user sessions on an instance. This is applicable only for multi-session fleets.
        :param max_user_duration_in_seconds: The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance. Specify a value between 600 and 432000.
        :param platform: The platform of the fleet. Platform is a required setting for Elastic fleets, and is not used for other fleet types.
        :param session_script_s3_location: The S3 location of the session scripts configuration zip file. This only applies to Elastic fleets.
        :param stream_view: The AppStream 2.0 view that is displayed to your users when they stream from the fleet. When ``APP`` is specified, only the windows of applications opened by users display. When ``DESKTOP`` is specified, the standard desktop that is provided by the operating system displays. The default value is ``APP`` .
        :param tags: An array of key-value pairs.
        :param usb_device_filter_strings: The USB device filter strings that specify which USB devices a user can redirect to the fleet streaming session, when using the Windows native client. This is allowed but not required for Elastic fleets.
        :param vpc_config: The VPC configuration for the fleet. This is required for Elastic fleets, but not required for other fleet types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html
        :exampleMetadata: infused

        Example::

            fleet = appstream.CfnFleet(self, "Fleet",
                instance_type="stream.standard.small",
                name="Fleet",
                compute_capacity=appstream.CfnFleet.ComputeCapacityProperty(
                    desired_instances=1
                ),
                image_name="AppStream-AmazonLinux2-09-21-2022"
            )
            fleet.cfn_options.creation_policy = CfnCreationPolicy(
                start_fleet=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c1696e8b6f6c109609fff783812cdcaafc37e209e10ad5c9f177ee9699fa56e)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument compute_capacity", value=compute_capacity, expected_type=type_hints["compute_capacity"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disconnect_timeout_in_seconds", value=disconnect_timeout_in_seconds, expected_type=type_hints["disconnect_timeout_in_seconds"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument domain_join_info", value=domain_join_info, expected_type=type_hints["domain_join_info"])
            check_type(argname="argument enable_default_internet_access", value=enable_default_internet_access, expected_type=type_hints["enable_default_internet_access"])
            check_type(argname="argument fleet_type", value=fleet_type, expected_type=type_hints["fleet_type"])
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument idle_disconnect_timeout_in_seconds", value=idle_disconnect_timeout_in_seconds, expected_type=type_hints["idle_disconnect_timeout_in_seconds"])
            check_type(argname="argument image_arn", value=image_arn, expected_type=type_hints["image_arn"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument max_concurrent_sessions", value=max_concurrent_sessions, expected_type=type_hints["max_concurrent_sessions"])
            check_type(argname="argument max_sessions_per_instance", value=max_sessions_per_instance, expected_type=type_hints["max_sessions_per_instance"])
            check_type(argname="argument max_user_duration_in_seconds", value=max_user_duration_in_seconds, expected_type=type_hints["max_user_duration_in_seconds"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument session_script_s3_location", value=session_script_s3_location, expected_type=type_hints["session_script_s3_location"])
            check_type(argname="argument stream_view", value=stream_view, expected_type=type_hints["stream_view"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument usb_device_filter_strings", value=usb_device_filter_strings, expected_type=type_hints["usb_device_filter_strings"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
            "name": name,
        }
        if compute_capacity is not None:
            self._values["compute_capacity"] = compute_capacity
        if description is not None:
            self._values["description"] = description
        if disconnect_timeout_in_seconds is not None:
            self._values["disconnect_timeout_in_seconds"] = disconnect_timeout_in_seconds
        if display_name is not None:
            self._values["display_name"] = display_name
        if domain_join_info is not None:
            self._values["domain_join_info"] = domain_join_info
        if enable_default_internet_access is not None:
            self._values["enable_default_internet_access"] = enable_default_internet_access
        if fleet_type is not None:
            self._values["fleet_type"] = fleet_type
        if iam_role_arn is not None:
            self._values["iam_role_arn"] = iam_role_arn
        if idle_disconnect_timeout_in_seconds is not None:
            self._values["idle_disconnect_timeout_in_seconds"] = idle_disconnect_timeout_in_seconds
        if image_arn is not None:
            self._values["image_arn"] = image_arn
        if image_name is not None:
            self._values["image_name"] = image_name
        if max_concurrent_sessions is not None:
            self._values["max_concurrent_sessions"] = max_concurrent_sessions
        if max_sessions_per_instance is not None:
            self._values["max_sessions_per_instance"] = max_sessions_per_instance
        if max_user_duration_in_seconds is not None:
            self._values["max_user_duration_in_seconds"] = max_user_duration_in_seconds
        if platform is not None:
            self._values["platform"] = platform
        if session_script_s3_location is not None:
            self._values["session_script_s3_location"] = session_script_s3_location
        if stream_view is not None:
            self._values["stream_view"] = stream_view
        if tags is not None:
            self._values["tags"] = tags
        if usb_device_filter_strings is not None:
            self._values["usb_device_filter_strings"] = usb_device_filter_strings
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''The instance type to use when launching fleet instances. The following instance types are available for non-Elastic fleets:.

        - stream.standard.small
        - stream.standard.medium
        - stream.standard.large
        - stream.compute.large
        - stream.compute.xlarge
        - stream.compute.2xlarge
        - stream.compute.4xlarge
        - stream.compute.8xlarge
        - stream.memory.large
        - stream.memory.xlarge
        - stream.memory.2xlarge
        - stream.memory.4xlarge
        - stream.memory.8xlarge
        - stream.memory.z1d.large
        - stream.memory.z1d.xlarge
        - stream.memory.z1d.2xlarge
        - stream.memory.z1d.3xlarge
        - stream.memory.z1d.6xlarge
        - stream.memory.z1d.12xlarge
        - stream.graphics-design.large
        - stream.graphics-design.xlarge
        - stream.graphics-design.2xlarge
        - stream.graphics-design.4xlarge
        - stream.graphics-desktop.2xlarge
        - stream.graphics.g4dn.xlarge
        - stream.graphics.g4dn.2xlarge
        - stream.graphics.g4dn.4xlarge
        - stream.graphics.g4dn.8xlarge
        - stream.graphics.g4dn.12xlarge
        - stream.graphics.g4dn.16xlarge
        - stream.graphics-pro.4xlarge
        - stream.graphics-pro.8xlarge
        - stream.graphics-pro.16xlarge

        The following instance types are available for Elastic fleets:

        - stream.standard.small
        - stream.standard.medium

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique name for the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compute_capacity(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ComputeCapacityProperty]]:
        '''The desired capacity for the fleet.

        This is not allowed for Elastic fleets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-computecapacity
        '''
        result = self._values.get("compute_capacity")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ComputeCapacityProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to display.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disconnect_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The amount of time that a streaming session remains active after users disconnect.

        If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.

        Specify a value between 60 and 36000.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-disconnecttimeoutinseconds
        '''
        result = self._values.get("disconnect_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The fleet name to display.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_join_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.DomainJoinInfoProperty]]:
        '''The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.

        This is not allowed for Elastic fleets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-domainjoininfo
        '''
        result = self._values.get("domain_join_info")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.DomainJoinInfoProperty]], result)

    @builtins.property
    def enable_default_internet_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables or disables default internet access for the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-enabledefaultinternetaccess
        '''
        result = self._values.get("enable_default_internet_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''The fleet type.

        - **ALWAYS_ON** - Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.
        - **ON_DEMAND** - Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.
        - **ELASTIC** - The pool of streaming instances is managed by Amazon AppStream 2.0. When a user selects their application or desktop to launch, they will start streaming after the app block has been downloaded and mounted to a streaming instance.

        *Allowed Values* : ``ALWAYS_ON`` | ``ELASTIC`` | ``ON_DEMAND``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-fleettype
        '''
        result = self._values.get("fleet_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that is applied to the fleet.

        To assume a role, the fleet instance calls the AWS Security Token Service ``AssumeRole`` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the *appstream_machine_role* credential profile on the instance.

        For more information, see `Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`_ in the *Amazon AppStream 2.0 Administration Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-iamrolearn
        '''
        result = self._values.get("iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_disconnect_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins.

        Users are notified before they are disconnected due to inactivity. If they try to reconnect to the streaming session before the time interval specified in ``DisconnectTimeoutInSeconds`` elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in ``IdleDisconnectTimeoutInSeconds`` elapses, they are disconnected.

        To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000.

        If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-idledisconnecttimeoutinseconds
        '''
        result = self._values.get("idle_disconnect_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def image_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the public, private, or shared image to use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-imagearn
        '''
        result = self._values.get("image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_name(self) -> typing.Optional[builtins.str]:
        '''The name of the image used to create the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-imagename
        '''
        result = self._values.get("image_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrent_sessions(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of concurrent sessions that can be run on an Elastic fleet.

        This setting is required for Elastic fleets, but is not used for other fleet types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-maxconcurrentsessions
        '''
        result = self._values.get("max_concurrent_sessions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_sessions_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Max number of user sessions on an instance.

        This is applicable only for multi-session fleets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-maxsessionsperinstance
        '''
        result = self._values.get("max_sessions_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_user_duration_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of time that a streaming session can remain active, in seconds.

        If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.

        Specify a value between 600 and 432000.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-maxuserdurationinseconds
        '''
        result = self._values.get("max_user_duration_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''The platform of the fleet.

        Platform is a required setting for Elastic fleets, and is not used for other fleet types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-platform
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_script_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.S3LocationProperty]]:
        '''The S3 location of the session scripts configuration zip file.

        This only applies to Elastic fleets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-sessionscripts3location
        '''
        result = self._values.get("session_script_s3_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.S3LocationProperty]], result)

    @builtins.property
    def stream_view(self) -> typing.Optional[builtins.str]:
        '''The AppStream 2.0 view that is displayed to your users when they stream from the fleet. When ``APP`` is specified, only the windows of applications opened by users display. When ``DESKTOP`` is specified, the standard desktop that is provided by the operating system displays.

        The default value is ``APP`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-streamview
        '''
        result = self._values.get("stream_view")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def usb_device_filter_strings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The USB device filter strings that specify which USB devices a user can redirect to the fleet streaming session, when using the Windows native client.

        This is allowed but not required for Elastic fleets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-usbdevicefilterstrings
        '''
        result = self._values.get("usb_device_filter_strings")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.VpcConfigProperty]]:
        '''The VPC configuration for the fleet.

        This is required for Elastic fleets, but not required for other fleet types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnImageBuilder(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnImageBuilder",
):
    '''The ``AWS::AppStream::ImageBuilder`` resource creates an image builder for Amazon AppStream 2.0. An image builder is a virtual machine that is used to create an image.

    The initial state of the image builder is ``PENDING`` . When it is ready, the state is ``RUNNING`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html
    :cloudformationResource: AWS::AppStream::ImageBuilder
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_image_builder = appstream.CfnImageBuilder(self, "MyCfnImageBuilder",
            instance_type="instanceType",
            name="name",
        
            # the properties below are optional
            access_endpoints=[appstream.CfnImageBuilder.AccessEndpointProperty(
                endpoint_type="endpointType",
                vpce_id="vpceId"
            )],
            appstream_agent_version="appstreamAgentVersion",
            description="description",
            display_name="displayName",
            domain_join_info=appstream.CfnImageBuilder.DomainJoinInfoProperty(
                directory_name="directoryName",
                organizational_unit_distinguished_name="organizationalUnitDistinguishedName"
            ),
            enable_default_internet_access=False,
            iam_role_arn="iamRoleArn",
            image_arn="imageArn",
            image_name="imageName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_config=appstream.CfnImageBuilder.VpcConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_type: builtins.str,
        name: builtins.str,
        access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageBuilder.AccessEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        appstream_agent_version: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        domain_join_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageBuilder.DomainJoinInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        image_arn: typing.Optional[builtins.str] = None,
        image_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageBuilder.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_type: The instance type to use when launching the image builder. The following instance types are available:. - stream.standard.small - stream.standard.medium - stream.standard.large - stream.compute.large - stream.compute.xlarge - stream.compute.2xlarge - stream.compute.4xlarge - stream.compute.8xlarge - stream.memory.large - stream.memory.xlarge - stream.memory.2xlarge - stream.memory.4xlarge - stream.memory.8xlarge - stream.memory.z1d.large - stream.memory.z1d.xlarge - stream.memory.z1d.2xlarge - stream.memory.z1d.3xlarge - stream.memory.z1d.6xlarge - stream.memory.z1d.12xlarge - stream.graphics-design.large - stream.graphics-design.xlarge - stream.graphics-design.2xlarge - stream.graphics-design.4xlarge - stream.graphics-desktop.2xlarge - stream.graphics.g4dn.xlarge - stream.graphics.g4dn.2xlarge - stream.graphics.g4dn.4xlarge - stream.graphics.g4dn.8xlarge - stream.graphics.g4dn.12xlarge - stream.graphics.g4dn.16xlarge - stream.graphics-pro.4xlarge - stream.graphics-pro.8xlarge - stream.graphics-pro.16xlarge
        :param name: A unique name for the image builder.
        :param access_endpoints: The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.
        :param appstream_agent_version: The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].
        :param description: The description to display.
        :param display_name: The image builder name to display.
        :param domain_join_info: The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.
        :param enable_default_internet_access: Enables or disables default internet access for the image builder.
        :param iam_role_arn: The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service ``AssumeRole`` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the *appstream_machine_role* credential profile on the instance. For more information, see `Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`_ in the *Amazon AppStream 2.0 Administration Guide* .
        :param image_arn: The ARN of the public, private, or shared image to use.
        :param image_name: The name of the image used to create the image builder.
        :param tags: An array of key-value pairs.
        :param vpc_config: The VPC configuration for the image builder. You can specify only one subnet.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25dccb4354e677f39c5c97fd983d6a76f7631b1133ab64219d2975708166efe2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnImageBuilderProps(
            instance_type=instance_type,
            name=name,
            access_endpoints=access_endpoints,
            appstream_agent_version=appstream_agent_version,
            description=description,
            display_name=display_name,
            domain_join_info=domain_join_info,
            enable_default_internet_access=enable_default_internet_access,
            iam_role_arn=iam_role_arn,
            image_arn=image_arn,
            image_name=image_name,
            tags=tags,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ec74adc688e0bdb7f0a14897529e4e6caef09d76aeb15844a23cc95502d7639)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cabc43267017cfc44ea4bbb9c3fa1ef592d580fffa6115a90205b3bb2253b503)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrStreamingUrl")
    def attr_streaming_url(self) -> builtins.str:
        '''The URL to start an image builder streaming session, returned as a string.

        :cloudformationAttribute: StreamingUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStreamingUrl"))

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
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''The instance type to use when launching the image builder.

        The following instance types are available:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__771bb6faeddd106d643f98bc3510eefbca762110055a75ca894c1a1853d7ba47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A unique name for the image builder.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c195974bec3d3620852bd27476c403eaa4214fa33dc9f1b6cd27639799fca71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="accessEndpoints")
    def access_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.AccessEndpointProperty"]]]]:
        '''The list of virtual private cloud (VPC) interface endpoint objects.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.AccessEndpointProperty"]]]], jsii.get(self, "accessEndpoints"))

    @access_endpoints.setter
    def access_endpoints(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.AccessEndpointProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__746e4a9e3f48985b9bf8079b3d895e3a8b0a7748caeb868365ff2a47e2ed9d36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="appstreamAgentVersion")
    def appstream_agent_version(self) -> typing.Optional[builtins.str]:
        '''The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appstreamAgentVersion"))

    @appstream_agent_version.setter
    def appstream_agent_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbfe60f13227554e339b92afa2a96a3531634abbc6108618cf474533196cb365)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appstreamAgentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to display.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a114f3ea3a654e9d4d760cdf7443cc73aa66b6e2b8f2c4d7d333accb36b9b88f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The image builder name to display.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a4101b60decd67001a1345c45d86ab1b421408ad10f6b8e58e966cbb1897cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="domainJoinInfo")
    def domain_join_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.DomainJoinInfoProperty"]]:
        '''The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.DomainJoinInfoProperty"]], jsii.get(self, "domainJoinInfo"))

    @domain_join_info.setter
    def domain_join_info(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.DomainJoinInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee5fc96661993bc890e05b1f0ae7eaf9202f05399a6fda1444d3b6323d544d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainJoinInfo", value)

    @builtins.property
    @jsii.member(jsii_name="enableDefaultInternetAccess")
    def enable_default_internet_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables or disables default internet access for the image builder.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableDefaultInternetAccess"))

    @enable_default_internet_access.setter
    def enable_default_internet_access(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__234082991507fccd1b51ac27db4c813ef4030635f0b32ddf3ab652b7f320fa6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDefaultInternetAccess", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that is applied to the image builder.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc542d91573c5313d5e4aa541efb2157e25e39cc082ca1991fc0e914e961471c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="imageArn")
    def image_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the public, private, or shared image to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageArn"))

    @image_arn.setter
    def image_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9661eef012d30e6482b8ebd48017128248f34a0a5b6f81200efab39a411f6b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageArn", value)

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> typing.Optional[builtins.str]:
        '''The name of the image used to create the image builder.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9671544139fb85d314712452cdf120b8083f58b155c561f6fe3cf4492bd91a05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32bb0a47350b5b67e1529a3d54fee7241fa2dab126f8e11eba610f03592bc255)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.VpcConfigProperty"]]:
        '''The VPC configuration for the image builder.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageBuilder.VpcConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e1029afa7ae41d9f4b692bbfd0623efa3755c15eb5a169b6191a4657ce20885)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnImageBuilder.AccessEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_type": "endpointType", "vpce_id": "vpceId"},
    )
    class AccessEndpointProperty:
        def __init__(
            self,
            *,
            endpoint_type: builtins.str,
            vpce_id: builtins.str,
        ) -> None:
            '''Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

            :param endpoint_type: The type of interface endpoint.
            :param vpce_id: The identifier (ID) of the VPC in which the interface endpoint is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                access_endpoint_property = appstream.CfnImageBuilder.AccessEndpointProperty(
                    endpoint_type="endpointType",
                    vpce_id="vpceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1311b50cfabf41e75ebeb9e0609a5fda76aa93594d88a9d8d050110731c3073b)
                check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
                check_type(argname="argument vpce_id", value=vpce_id, expected_type=type_hints["vpce_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint_type": endpoint_type,
                "vpce_id": vpce_id,
            }

        @builtins.property
        def endpoint_type(self) -> builtins.str:
            '''The type of interface endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html#cfn-appstream-imagebuilder-accessendpoint-endpointtype
            '''
            result = self._values.get("endpoint_type")
            assert result is not None, "Required property 'endpoint_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpce_id(self) -> builtins.str:
            '''The identifier (ID) of the VPC in which the interface endpoint is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html#cfn-appstream-imagebuilder-accessendpoint-vpceid
            '''
            result = self._values.get("vpce_id")
            assert result is not None, "Required property 'vpce_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnImageBuilder.DomainJoinInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_name": "directoryName",
            "organizational_unit_distinguished_name": "organizationalUnitDistinguishedName",
        },
    )
    class DomainJoinInfoProperty:
        def __init__(
            self,
            *,
            directory_name: typing.Optional[builtins.str] = None,
            organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

            :param directory_name: The fully qualified name of the directory (for example, corp.example.com).
            :param organizational_unit_distinguished_name: The distinguished name of the organizational unit for computer accounts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                domain_join_info_property = appstream.CfnImageBuilder.DomainJoinInfoProperty(
                    directory_name="directoryName",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4e8369c89d03719c64d2c83e51b7e08b1b75d665769bd928f11984729ab04d24)
                check_type(argname="argument directory_name", value=directory_name, expected_type=type_hints["directory_name"])
                check_type(argname="argument organizational_unit_distinguished_name", value=organizational_unit_distinguished_name, expected_type=type_hints["organizational_unit_distinguished_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if directory_name is not None:
                self._values["directory_name"] = directory_name
            if organizational_unit_distinguished_name is not None:
                self._values["organizational_unit_distinguished_name"] = organizational_unit_distinguished_name

        @builtins.property
        def directory_name(self) -> typing.Optional[builtins.str]:
            '''The fully qualified name of the directory (for example, corp.example.com).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html#cfn-appstream-imagebuilder-domainjoininfo-directoryname
            '''
            result = self._values.get("directory_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit_distinguished_name(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The distinguished name of the organizational unit for computer accounts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html#cfn-appstream-imagebuilder-domainjoininfo-organizationalunitdistinguishedname
            '''
            result = self._values.get("organizational_unit_distinguished_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainJoinInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnImageBuilder.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The VPC configuration for the image builder.

            :param security_group_ids: The identifiers of the security groups for the image builder.
            :param subnet_ids: The identifier of the subnet to which a network interface is attached from the image builder instance. An image builder instance can use one subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                vpc_config_property = appstream.CfnImageBuilder.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8d93dcafbda7cc30fc6a56bcf4eebd91a55747713e0043d6fdac8bc1f7237ce)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The identifiers of the security groups for the image builder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html#cfn-appstream-imagebuilder-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The identifier of the subnet to which a network interface is attached from the image builder instance.

            An image builder instance can use one subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html#cfn-appstream-imagebuilder-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnImageBuilderProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "name": "name",
        "access_endpoints": "accessEndpoints",
        "appstream_agent_version": "appstreamAgentVersion",
        "description": "description",
        "display_name": "displayName",
        "domain_join_info": "domainJoinInfo",
        "enable_default_internet_access": "enableDefaultInternetAccess",
        "iam_role_arn": "iamRoleArn",
        "image_arn": "imageArn",
        "image_name": "imageName",
        "tags": "tags",
        "vpc_config": "vpcConfig",
    },
)
class CfnImageBuilderProps:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        name: builtins.str,
        access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        appstream_agent_version: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        domain_join_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.DomainJoinInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        image_arn: typing.Optional[builtins.str] = None,
        image_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnImageBuilder``.

        :param instance_type: The instance type to use when launching the image builder. The following instance types are available:. - stream.standard.small - stream.standard.medium - stream.standard.large - stream.compute.large - stream.compute.xlarge - stream.compute.2xlarge - stream.compute.4xlarge - stream.compute.8xlarge - stream.memory.large - stream.memory.xlarge - stream.memory.2xlarge - stream.memory.4xlarge - stream.memory.8xlarge - stream.memory.z1d.large - stream.memory.z1d.xlarge - stream.memory.z1d.2xlarge - stream.memory.z1d.3xlarge - stream.memory.z1d.6xlarge - stream.memory.z1d.12xlarge - stream.graphics-design.large - stream.graphics-design.xlarge - stream.graphics-design.2xlarge - stream.graphics-design.4xlarge - stream.graphics-desktop.2xlarge - stream.graphics.g4dn.xlarge - stream.graphics.g4dn.2xlarge - stream.graphics.g4dn.4xlarge - stream.graphics.g4dn.8xlarge - stream.graphics.g4dn.12xlarge - stream.graphics.g4dn.16xlarge - stream.graphics-pro.4xlarge - stream.graphics-pro.8xlarge - stream.graphics-pro.16xlarge
        :param name: A unique name for the image builder.
        :param access_endpoints: The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.
        :param appstream_agent_version: The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].
        :param description: The description to display.
        :param display_name: The image builder name to display.
        :param domain_join_info: The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.
        :param enable_default_internet_access: Enables or disables default internet access for the image builder.
        :param iam_role_arn: The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service ``AssumeRole`` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the *appstream_machine_role* credential profile on the instance. For more information, see `Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`_ in the *Amazon AppStream 2.0 Administration Guide* .
        :param image_arn: The ARN of the public, private, or shared image to use.
        :param image_name: The name of the image used to create the image builder.
        :param tags: An array of key-value pairs.
        :param vpc_config: The VPC configuration for the image builder. You can specify only one subnet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_image_builder_props = appstream.CfnImageBuilderProps(
                instance_type="instanceType",
                name="name",
            
                # the properties below are optional
                access_endpoints=[appstream.CfnImageBuilder.AccessEndpointProperty(
                    endpoint_type="endpointType",
                    vpce_id="vpceId"
                )],
                appstream_agent_version="appstreamAgentVersion",
                description="description",
                display_name="displayName",
                domain_join_info=appstream.CfnImageBuilder.DomainJoinInfoProperty(
                    directory_name="directoryName",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName"
                ),
                enable_default_internet_access=False,
                iam_role_arn="iamRoleArn",
                image_arn="imageArn",
                image_name="imageName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_config=appstream.CfnImageBuilder.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f00d771423a1edbc076328e18ee5a37fbf5bb31404bdb6b4224eba3f881e4810)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument access_endpoints", value=access_endpoints, expected_type=type_hints["access_endpoints"])
            check_type(argname="argument appstream_agent_version", value=appstream_agent_version, expected_type=type_hints["appstream_agent_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument domain_join_info", value=domain_join_info, expected_type=type_hints["domain_join_info"])
            check_type(argname="argument enable_default_internet_access", value=enable_default_internet_access, expected_type=type_hints["enable_default_internet_access"])
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument image_arn", value=image_arn, expected_type=type_hints["image_arn"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
            "name": name,
        }
        if access_endpoints is not None:
            self._values["access_endpoints"] = access_endpoints
        if appstream_agent_version is not None:
            self._values["appstream_agent_version"] = appstream_agent_version
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if domain_join_info is not None:
            self._values["domain_join_info"] = domain_join_info
        if enable_default_internet_access is not None:
            self._values["enable_default_internet_access"] = enable_default_internet_access
        if iam_role_arn is not None:
            self._values["iam_role_arn"] = iam_role_arn
        if image_arn is not None:
            self._values["image_arn"] = image_arn
        if image_name is not None:
            self._values["image_name"] = image_name
        if tags is not None:
            self._values["tags"] = tags
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''The instance type to use when launching the image builder. The following instance types are available:.

        - stream.standard.small
        - stream.standard.medium
        - stream.standard.large
        - stream.compute.large
        - stream.compute.xlarge
        - stream.compute.2xlarge
        - stream.compute.4xlarge
        - stream.compute.8xlarge
        - stream.memory.large
        - stream.memory.xlarge
        - stream.memory.2xlarge
        - stream.memory.4xlarge
        - stream.memory.8xlarge
        - stream.memory.z1d.large
        - stream.memory.z1d.xlarge
        - stream.memory.z1d.2xlarge
        - stream.memory.z1d.3xlarge
        - stream.memory.z1d.6xlarge
        - stream.memory.z1d.12xlarge
        - stream.graphics-design.large
        - stream.graphics-design.xlarge
        - stream.graphics-design.2xlarge
        - stream.graphics-design.4xlarge
        - stream.graphics-desktop.2xlarge
        - stream.graphics.g4dn.xlarge
        - stream.graphics.g4dn.2xlarge
        - stream.graphics.g4dn.4xlarge
        - stream.graphics.g4dn.8xlarge
        - stream.graphics.g4dn.12xlarge
        - stream.graphics.g4dn.16xlarge
        - stream.graphics-pro.4xlarge
        - stream.graphics-pro.8xlarge
        - stream.graphics-pro.16xlarge

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique name for the image builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.AccessEndpointProperty]]]]:
        '''The list of virtual private cloud (VPC) interface endpoint objects.

        Administrators can connect to the image builder only through the specified endpoints.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-accessendpoints
        '''
        result = self._values.get("access_endpoints")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.AccessEndpointProperty]]]], result)

    @builtins.property
    def appstream_agent_version(self) -> typing.Optional[builtins.str]:
        '''The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-appstreamagentversion
        '''
        result = self._values.get("appstream_agent_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to display.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The image builder name to display.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_join_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.DomainJoinInfoProperty]]:
        '''The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-domainjoininfo
        '''
        result = self._values.get("domain_join_info")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.DomainJoinInfoProperty]], result)

    @builtins.property
    def enable_default_internet_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables or disables default internet access for the image builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-enabledefaultinternetaccess
        '''
        result = self._values.get("enable_default_internet_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that is applied to the image builder.

        To assume a role, the image builder calls the AWS Security Token Service ``AssumeRole`` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the *appstream_machine_role* credential profile on the instance.

        For more information, see `Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`_ in the *Amazon AppStream 2.0 Administration Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-iamrolearn
        '''
        result = self._values.get("iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the public, private, or shared image to use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-imagearn
        '''
        result = self._values.get("image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_name(self) -> typing.Optional[builtins.str]:
        '''The name of the image used to create the image builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-imagename
        '''
        result = self._values.get("image_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.VpcConfigProperty]]:
        '''The VPC configuration for the image builder.

        You can specify only one subnet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageBuilderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStack(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnStack",
):
    '''The ``AWS::AppStream::Stack`` resource creates a stack to start streaming applications to Amazon AppStream 2.0 users. A stack consists of an associated fleet, user access policies, and storage configurations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html
    :cloudformationResource: AWS::AppStream::Stack
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_stack = appstream.CfnStack(self, "MyCfnStack",
            access_endpoints=[appstream.CfnStack.AccessEndpointProperty(
                endpoint_type="endpointType",
                vpce_id="vpceId"
            )],
            application_settings=appstream.CfnStack.ApplicationSettingsProperty(
                enabled=False,
        
                # the properties below are optional
                settings_group="settingsGroup"
            ),
            attributes_to_delete=["attributesToDelete"],
            delete_storage_connectors=False,
            description="description",
            display_name="displayName",
            embed_host_domains=["embedHostDomains"],
            feedback_url="feedbackUrl",
            name="name",
            redirect_url="redirectUrl",
            storage_connectors=[appstream.CfnStack.StorageConnectorProperty(
                connector_type="connectorType",
        
                # the properties below are optional
                domains=["domains"],
                resource_identifier="resourceIdentifier"
            )],
            streaming_experience_settings=appstream.CfnStack.StreamingExperienceSettingsProperty(
                preferred_protocol="preferredProtocol"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_settings=[appstream.CfnStack.UserSettingProperty(
                action="action",
                permission="permission",
        
                # the properties below are optional
                maximum_length=123
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.AccessEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        application_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.ApplicationSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        attributes_to_delete: typing.Optional[typing.Sequence[builtins.str]] = None,
        delete_storage_connectors: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        embed_host_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        feedback_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        redirect_url: typing.Optional[builtins.str] = None,
        storage_connectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.StorageConnectorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        streaming_experience_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.StreamingExperienceSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.UserSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_endpoints: The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.
        :param application_settings: The persistent application settings for users of the stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.
        :param attributes_to_delete: The stack attributes to delete.
        :param delete_storage_connectors: *This parameter has been deprecated.*. Deletes the storage connectors currently enabled for the stack.
        :param description: The description to display.
        :param display_name: The stack name to display.
        :param embed_host_domains: The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.
        :param feedback_url: The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
        :param name: The name of the stack.
        :param redirect_url: The URL that users are redirected to after their streaming session ends.
        :param storage_connectors: The storage connectors to enable.
        :param streaming_experience_settings: The streaming protocol that you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.
        :param tags: An array of key-value pairs.
        :param user_settings: The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__add685d2c205e11b1f2727c7c09ea99b5fd4739effbaca1fd079659e5f37439d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStackProps(
            access_endpoints=access_endpoints,
            application_settings=application_settings,
            attributes_to_delete=attributes_to_delete,
            delete_storage_connectors=delete_storage_connectors,
            description=description,
            display_name=display_name,
            embed_host_domains=embed_host_domains,
            feedback_url=feedback_url,
            name=name,
            redirect_url=redirect_url,
            storage_connectors=storage_connectors,
            streaming_experience_settings=streaming_experience_settings,
            tags=tags,
            user_settings=user_settings,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb250bd0ddb058fba554647ecaf8a602c6ffc9518afdb0c6b6c75dcb6e673ac2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e4e065b6d01f90eee058076d521bb71fbc0a489b794e50fc75dc867f6b3c906)
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
    @jsii.member(jsii_name="accessEndpoints")
    def access_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.AccessEndpointProperty"]]]]:
        '''The list of virtual private cloud (VPC) interface endpoint objects.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.AccessEndpointProperty"]]]], jsii.get(self, "accessEndpoints"))

    @access_endpoints.setter
    def access_endpoints(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.AccessEndpointProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad9a87386d835ff4af56b6ca6b53baa12cd008bd109294050154f77511bc98cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="applicationSettings")
    def application_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.ApplicationSettingsProperty"]]:
        '''The persistent application settings for users of the stack.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.ApplicationSettingsProperty"]], jsii.get(self, "applicationSettings"))

    @application_settings.setter
    def application_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.ApplicationSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318b1e9f0d5854a3c702b5b51837caed9c2f8ef41e3bc15d8e0cdac003bf38b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationSettings", value)

    @builtins.property
    @jsii.member(jsii_name="attributesToDelete")
    def attributes_to_delete(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The stack attributes to delete.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "attributesToDelete"))

    @attributes_to_delete.setter
    def attributes_to_delete(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c273fef3acafd8229cbff7e9a2c1b03a874f74a6397ceeb316e0b9ae83ae12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributesToDelete", value)

    @builtins.property
    @jsii.member(jsii_name="deleteStorageConnectors")
    def delete_storage_connectors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''*This parameter has been deprecated.*.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deleteStorageConnectors"))

    @delete_storage_connectors.setter
    def delete_storage_connectors(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd3eed1a7554981a61b92b8848f5b531271aad947e65c20f9604a014bca0a673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteStorageConnectors", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to display.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f47b501b000d9e8d0b5a92a98d9b1b6e43924d0508d9c95323d961a8e6892b46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The stack name to display.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40d9674cac50abf3d7c71f658f161af8c5dfda7e99b6e3ed0ac5757b86f7c359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="embedHostDomains")
    def embed_host_domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "embedHostDomains"))

    @embed_host_domains.setter
    def embed_host_domains(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e724a0f54ce83bd45cd8d43d8af34006db8700d91fa4a6ccfec245ffdb2ddc97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "embedHostDomains", value)

    @builtins.property
    @jsii.member(jsii_name="feedbackUrl")
    def feedback_url(self) -> typing.Optional[builtins.str]:
        '''The URL that users are redirected to after they click the Send Feedback link.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "feedbackUrl"))

    @feedback_url.setter
    def feedback_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844efac5860b4d32faef93720e2c6a1abbcc41678d249a453e14ba3722be9904)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "feedbackUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the stack.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73280be80fedcfcb318f73a4dbe80e309ed0d2f02b7aedb45617faf540cc7511)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUrl")
    def redirect_url(self) -> typing.Optional[builtins.str]:
        '''The URL that users are redirected to after their streaming session ends.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUrl"))

    @redirect_url.setter
    def redirect_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dda375121bdfb203a69bc3a2485d69e2ee01da1e4327d7116bfac610f8927d22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="storageConnectors")
    def storage_connectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.StorageConnectorProperty"]]]]:
        '''The storage connectors to enable.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.StorageConnectorProperty"]]]], jsii.get(self, "storageConnectors"))

    @storage_connectors.setter
    def storage_connectors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.StorageConnectorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__275ea87a7dfdce8c58071ca77a17a383b5b77dc023446160cf3c8af4d0ba7238)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageConnectors", value)

    @builtins.property
    @jsii.member(jsii_name="streamingExperienceSettings")
    def streaming_experience_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.StreamingExperienceSettingsProperty"]]:
        '''The streaming protocol that you want your stack to prefer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.StreamingExperienceSettingsProperty"]], jsii.get(self, "streamingExperienceSettings"))

    @streaming_experience_settings.setter
    def streaming_experience_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.StreamingExperienceSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab82aff9577044655905fdadec884f88fa2e07d1163701496f44bb2a9903bda5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamingExperienceSettings", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d8194ace5a04925ea85c21feb9edfbcc17535be57ee024386cc650e109718ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="userSettings")
    def user_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.UserSettingProperty"]]]]:
        '''The actions that are enabled or disabled for users during their streaming sessions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.UserSettingProperty"]]]], jsii.get(self, "userSettings"))

    @user_settings.setter
    def user_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.UserSettingProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf30847a0d21a9895ed825ab61f3abb249fb73253d9806ea965739b1698fa46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userSettings", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnStack.AccessEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_type": "endpointType", "vpce_id": "vpceId"},
    )
    class AccessEndpointProperty:
        def __init__(
            self,
            *,
            endpoint_type: builtins.str,
            vpce_id: builtins.str,
        ) -> None:
            '''Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

            :param endpoint_type: The type of interface endpoint.
            :param vpce_id: The identifier (ID) of the VPC in which the interface endpoint is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                access_endpoint_property = appstream.CfnStack.AccessEndpointProperty(
                    endpoint_type="endpointType",
                    vpce_id="vpceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16b91ca2aed5404f22e03b015fd7cb7dfa614fffde2d87be465daef732bf300e)
                check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
                check_type(argname="argument vpce_id", value=vpce_id, expected_type=type_hints["vpce_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint_type": endpoint_type,
                "vpce_id": vpce_id,
            }

        @builtins.property
        def endpoint_type(self) -> builtins.str:
            '''The type of interface endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html#cfn-appstream-stack-accessendpoint-endpointtype
            '''
            result = self._values.get("endpoint_type")
            assert result is not None, "Required property 'endpoint_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpce_id(self) -> builtins.str:
            '''The identifier (ID) of the VPC in which the interface endpoint is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html#cfn-appstream-stack-accessendpoint-vpceid
            '''
            result = self._values.get("vpce_id")
            assert result is not None, "Required property 'vpce_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnStack.ApplicationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "settings_group": "settingsGroup"},
    )
    class ApplicationSettingsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            settings_group: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The persistent application settings for users of a stack.

            :param enabled: Enables or disables persistent application settings for users during their streaming sessions.
            :param settings_group: The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                application_settings_property = appstream.CfnStack.ApplicationSettingsProperty(
                    enabled=False,
                
                    # the properties below are optional
                    settings_group="settingsGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dbd2bf22e417927425b480fb9f77598b6dc3c52bceeccd8e20029d3afe1dd49e)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument settings_group", value=settings_group, expected_type=type_hints["settings_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if settings_group is not None:
                self._values["settings_group"] = settings_group

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Enables or disables persistent application settings for users during their streaming sessions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html#cfn-appstream-stack-applicationsettings-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def settings_group(self) -> typing.Optional[builtins.str]:
            '''The path prefix for the S3 bucket where users’ persistent application settings are stored.

            You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html#cfn-appstream-stack-applicationsettings-settingsgroup
            '''
            result = self._values.get("settings_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnStack.StorageConnectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_type": "connectorType",
            "domains": "domains",
            "resource_identifier": "resourceIdentifier",
        },
    )
    class StorageConnectorProperty:
        def __init__(
            self,
            *,
            connector_type: builtins.str,
            domains: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A connector that enables persistent storage for users.

            :param connector_type: The type of storage connector.
            :param domains: The names of the domains for the account.
            :param resource_identifier: The ARN of the storage connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                storage_connector_property = appstream.CfnStack.StorageConnectorProperty(
                    connector_type="connectorType",
                
                    # the properties below are optional
                    domains=["domains"],
                    resource_identifier="resourceIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5f4551020c535e3e6e3df104109b0aa10638f110819d36a938d2fea05892f89)
                check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
                check_type(argname="argument domains", value=domains, expected_type=type_hints["domains"])
                check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connector_type": connector_type,
            }
            if domains is not None:
                self._values["domains"] = domains
            if resource_identifier is not None:
                self._values["resource_identifier"] = resource_identifier

        @builtins.property
        def connector_type(self) -> builtins.str:
            '''The type of storage connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html#cfn-appstream-stack-storageconnector-connectortype
            '''
            result = self._values.get("connector_type")
            assert result is not None, "Required property 'connector_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def domains(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The names of the domains for the account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html#cfn-appstream-stack-storageconnector-domains
            '''
            result = self._values.get("domains")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_identifier(self) -> typing.Optional[builtins.str]:
            '''The ARN of the storage connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html#cfn-appstream-stack-storageconnector-resourceidentifier
            '''
            result = self._values.get("resource_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageConnectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnStack.StreamingExperienceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"preferred_protocol": "preferredProtocol"},
    )
    class StreamingExperienceSettingsProperty:
        def __init__(
            self,
            *,
            preferred_protocol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The streaming protocol that you want your stack to prefer.

            This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.

            :param preferred_protocol: The preferred protocol that you want to use while streaming your application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-streamingexperiencesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                streaming_experience_settings_property = appstream.CfnStack.StreamingExperienceSettingsProperty(
                    preferred_protocol="preferredProtocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c91289741f79afeb2e10af943a02636d21ff3e2882ecef22a76b60441af0e394)
                check_type(argname="argument preferred_protocol", value=preferred_protocol, expected_type=type_hints["preferred_protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if preferred_protocol is not None:
                self._values["preferred_protocol"] = preferred_protocol

        @builtins.property
        def preferred_protocol(self) -> typing.Optional[builtins.str]:
            '''The preferred protocol that you want to use while streaming your application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-streamingexperiencesettings.html#cfn-appstream-stack-streamingexperiencesettings-preferredprotocol
            '''
            result = self._values.get("preferred_protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamingExperienceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appstream.CfnStack.UserSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "permission": "permission",
            "maximum_length": "maximumLength",
        },
    )
    class UserSettingProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            permission: builtins.str,
            maximum_length: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies an action and whether the action is enabled or disabled for users during their streaming sessions.

            :param action: The action that is enabled or disabled.
            :param permission: Indicates whether the action is enabled or disabled.
            :param maximum_length: Specifies the number of characters that can be copied by end users from the local device to the remote session, and to the local device from the remote session. This can be specified only for the ``CLIPBOARD_COPY_FROM_LOCAL_DEVICE`` and ``CLIPBOARD_COPY_TO_LOCAL_DEVICE`` actions. This defaults to 20,971,520 (20 MB) when unspecified and the permission is ``ENABLED`` . This can't be specified when the permission is ``DISABLED`` . The value can be between 1 and 20,971,520 (20 MB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appstream as appstream
                
                user_setting_property = appstream.CfnStack.UserSettingProperty(
                    action="action",
                    permission="permission",
                
                    # the properties below are optional
                    maximum_length=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63f08d4ad1bd849bb76b897fa82448efbc7d5525adc690cc1128fc23d090e97a)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
                check_type(argname="argument maximum_length", value=maximum_length, expected_type=type_hints["maximum_length"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "permission": permission,
            }
            if maximum_length is not None:
                self._values["maximum_length"] = maximum_length

        @builtins.property
        def action(self) -> builtins.str:
            '''The action that is enabled or disabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html#cfn-appstream-stack-usersetting-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def permission(self) -> builtins.str:
            '''Indicates whether the action is enabled or disabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html#cfn-appstream-stack-usersetting-permission
            '''
            result = self._values.get("permission")
            assert result is not None, "Required property 'permission' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maximum_length(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of characters that can be copied by end users from the local device to the remote session, and to the local device from the remote session.

            This can be specified only for the ``CLIPBOARD_COPY_FROM_LOCAL_DEVICE`` and ``CLIPBOARD_COPY_TO_LOCAL_DEVICE`` actions.

            This defaults to 20,971,520 (20 MB) when unspecified and the permission is ``ENABLED`` . This can't be specified when the permission is ``DISABLED`` .

            The value can be between 1 and 20,971,520 (20 MB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html#cfn-appstream-stack-usersetting-maximumlength
            '''
            result = self._values.get("maximum_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnStackFleetAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnStackFleetAssociation",
):
    '''The ``AWS::AppStream::StackFleetAssociation`` resource associates the specified fleet with the specified stack for Amazon AppStream 2.0.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html
    :cloudformationResource: AWS::AppStream::StackFleetAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_stack_fleet_association = appstream.CfnStackFleetAssociation(self, "MyCfnStackFleetAssociation",
            fleet_name="fleetName",
            stack_name="stackName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        fleet_name: builtins.str,
        stack_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param fleet_name: The name of the fleet. To associate a fleet with a stack, you must specify a dependency on the fleet resource. For more information, see `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .
        :param stack_name: The name of the stack. To associate a fleet with a stack, you must specify a dependency on the stack resource. For more information, see `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93298a8702bdb81bee8aa40e3e8877e0f9ff694374a42c0c1997d95079c7140)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStackFleetAssociationProps(
            fleet_name=fleet_name, stack_name=stack_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d48d22fdad8c6f0375110dcf28aeec8ed277936eb365c074fcbcbc0f2e959297)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a3b4d53c3d446f718a46bdea3c087759b17cadceb19025592653406dd89c41d)
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
    @jsii.member(jsii_name="fleetName")
    def fleet_name(self) -> builtins.str:
        '''The name of the fleet.'''
        return typing.cast(builtins.str, jsii.get(self, "fleetName"))

    @fleet_name.setter
    def fleet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3954597e38e49c693cdf9002320951ac5284d459fe9df8a7bd94c418997f2942)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetName", value)

    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        '''The name of the stack.'''
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @stack_name.setter
    def stack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f091262b0bcbec47a122c68936b6834a45a0aeebefa27b699caf9d999a15b8b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnStackFleetAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"fleet_name": "fleetName", "stack_name": "stackName"},
)
class CfnStackFleetAssociationProps:
    def __init__(self, *, fleet_name: builtins.str, stack_name: builtins.str) -> None:
        '''Properties for defining a ``CfnStackFleetAssociation``.

        :param fleet_name: The name of the fleet. To associate a fleet with a stack, you must specify a dependency on the fleet resource. For more information, see `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .
        :param stack_name: The name of the stack. To associate a fleet with a stack, you must specify a dependency on the stack resource. For more information, see `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_stack_fleet_association_props = appstream.CfnStackFleetAssociationProps(
                fleet_name="fleetName",
                stack_name="stackName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1480c1a389e0a505f08c8a89fcde9176cdb68f3f06682e9ee925e2d04934be68)
            check_type(argname="argument fleet_name", value=fleet_name, expected_type=type_hints["fleet_name"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_name": fleet_name,
            "stack_name": stack_name,
        }

    @builtins.property
    def fleet_name(self) -> builtins.str:
        '''The name of the fleet.

        To associate a fleet with a stack, you must specify a dependency on the fleet resource. For more information, see `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html#cfn-appstream-stackfleetassociation-fleetname
        '''
        result = self._values.get("fleet_name")
        assert result is not None, "Required property 'fleet_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The name of the stack.

        To associate a fleet with a stack, you must specify a dependency on the stack resource. For more information, see `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html#cfn-appstream-stackfleetassociation-stackname
        '''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackFleetAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnStackProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_endpoints": "accessEndpoints",
        "application_settings": "applicationSettings",
        "attributes_to_delete": "attributesToDelete",
        "delete_storage_connectors": "deleteStorageConnectors",
        "description": "description",
        "display_name": "displayName",
        "embed_host_domains": "embedHostDomains",
        "feedback_url": "feedbackUrl",
        "name": "name",
        "redirect_url": "redirectUrl",
        "storage_connectors": "storageConnectors",
        "streaming_experience_settings": "streamingExperienceSettings",
        "tags": "tags",
        "user_settings": "userSettings",
    },
)
class CfnStackProps:
    def __init__(
        self,
        *,
        access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        application_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ApplicationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        attributes_to_delete: typing.Optional[typing.Sequence[builtins.str]] = None,
        delete_storage_connectors: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        embed_host_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        feedback_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        redirect_url: typing.Optional[builtins.str] = None,
        storage_connectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StorageConnectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        streaming_experience_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StreamingExperienceSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.UserSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStack``.

        :param access_endpoints: The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.
        :param application_settings: The persistent application settings for users of the stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.
        :param attributes_to_delete: The stack attributes to delete.
        :param delete_storage_connectors: *This parameter has been deprecated.*. Deletes the storage connectors currently enabled for the stack.
        :param description: The description to display.
        :param display_name: The stack name to display.
        :param embed_host_domains: The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.
        :param feedback_url: The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
        :param name: The name of the stack.
        :param redirect_url: The URL that users are redirected to after their streaming session ends.
        :param storage_connectors: The storage connectors to enable.
        :param streaming_experience_settings: The streaming protocol that you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.
        :param tags: An array of key-value pairs.
        :param user_settings: The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_stack_props = appstream.CfnStackProps(
                access_endpoints=[appstream.CfnStack.AccessEndpointProperty(
                    endpoint_type="endpointType",
                    vpce_id="vpceId"
                )],
                application_settings=appstream.CfnStack.ApplicationSettingsProperty(
                    enabled=False,
            
                    # the properties below are optional
                    settings_group="settingsGroup"
                ),
                attributes_to_delete=["attributesToDelete"],
                delete_storage_connectors=False,
                description="description",
                display_name="displayName",
                embed_host_domains=["embedHostDomains"],
                feedback_url="feedbackUrl",
                name="name",
                redirect_url="redirectUrl",
                storage_connectors=[appstream.CfnStack.StorageConnectorProperty(
                    connector_type="connectorType",
            
                    # the properties below are optional
                    domains=["domains"],
                    resource_identifier="resourceIdentifier"
                )],
                streaming_experience_settings=appstream.CfnStack.StreamingExperienceSettingsProperty(
                    preferred_protocol="preferredProtocol"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_settings=[appstream.CfnStack.UserSettingProperty(
                    action="action",
                    permission="permission",
            
                    # the properties below are optional
                    maximum_length=123
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f5987726340331a807da3e721dc066e307475a26a6ce0ddcd409aa8fa0fe4b7)
            check_type(argname="argument access_endpoints", value=access_endpoints, expected_type=type_hints["access_endpoints"])
            check_type(argname="argument application_settings", value=application_settings, expected_type=type_hints["application_settings"])
            check_type(argname="argument attributes_to_delete", value=attributes_to_delete, expected_type=type_hints["attributes_to_delete"])
            check_type(argname="argument delete_storage_connectors", value=delete_storage_connectors, expected_type=type_hints["delete_storage_connectors"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument embed_host_domains", value=embed_host_domains, expected_type=type_hints["embed_host_domains"])
            check_type(argname="argument feedback_url", value=feedback_url, expected_type=type_hints["feedback_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument redirect_url", value=redirect_url, expected_type=type_hints["redirect_url"])
            check_type(argname="argument storage_connectors", value=storage_connectors, expected_type=type_hints["storage_connectors"])
            check_type(argname="argument streaming_experience_settings", value=streaming_experience_settings, expected_type=type_hints["streaming_experience_settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_settings", value=user_settings, expected_type=type_hints["user_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_endpoints is not None:
            self._values["access_endpoints"] = access_endpoints
        if application_settings is not None:
            self._values["application_settings"] = application_settings
        if attributes_to_delete is not None:
            self._values["attributes_to_delete"] = attributes_to_delete
        if delete_storage_connectors is not None:
            self._values["delete_storage_connectors"] = delete_storage_connectors
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if embed_host_domains is not None:
            self._values["embed_host_domains"] = embed_host_domains
        if feedback_url is not None:
            self._values["feedback_url"] = feedback_url
        if name is not None:
            self._values["name"] = name
        if redirect_url is not None:
            self._values["redirect_url"] = redirect_url
        if storage_connectors is not None:
            self._values["storage_connectors"] = storage_connectors
        if streaming_experience_settings is not None:
            self._values["streaming_experience_settings"] = streaming_experience_settings
        if tags is not None:
            self._values["tags"] = tags
        if user_settings is not None:
            self._values["user_settings"] = user_settings

    @builtins.property
    def access_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.AccessEndpointProperty]]]]:
        '''The list of virtual private cloud (VPC) interface endpoint objects.

        Users of the stack can connect to AppStream 2.0 only through the specified endpoints.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-accessendpoints
        '''
        result = self._values.get("access_endpoints")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.AccessEndpointProperty]]]], result)

    @builtins.property
    def application_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.ApplicationSettingsProperty]]:
        '''The persistent application settings for users of the stack.

        When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-applicationsettings
        '''
        result = self._values.get("application_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.ApplicationSettingsProperty]], result)

    @builtins.property
    def attributes_to_delete(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The stack attributes to delete.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-attributestodelete
        '''
        result = self._values.get("attributes_to_delete")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def delete_storage_connectors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''*This parameter has been deprecated.*.

        Deletes the storage connectors currently enabled for the stack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-deletestorageconnectors
        '''
        result = self._values.get("delete_storage_connectors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to display.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The stack name to display.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def embed_host_domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-embedhostdomains
        '''
        result = self._values.get("embed_host_domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def feedback_url(self) -> typing.Optional[builtins.str]:
        '''The URL that users are redirected to after they click the Send Feedback link.

        If no URL is specified, no Send Feedback link is displayed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-feedbackurl
        '''
        result = self._values.get("feedback_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the stack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_url(self) -> typing.Optional[builtins.str]:
        '''The URL that users are redirected to after their streaming session ends.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-redirecturl
        '''
        result = self._values.get("redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_connectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.StorageConnectorProperty]]]]:
        '''The storage connectors to enable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-storageconnectors
        '''
        result = self._values.get("storage_connectors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.StorageConnectorProperty]]]], result)

    @builtins.property
    def streaming_experience_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.StreamingExperienceSettingsProperty]]:
        '''The streaming protocol that you want your stack to prefer.

        This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-streamingexperiencesettings
        '''
        result = self._values.get("streaming_experience_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.StreamingExperienceSettingsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.UserSettingProperty]]]]:
        '''The actions that are enabled or disabled for users during their streaming sessions.

        By default, these actions are enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-usersettings
        '''
        result = self._values.get("user_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.UserSettingProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStackUserAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnStackUserAssociation",
):
    '''The ``AWS::AppStream::StackUserAssociation`` resource associates the specified users with the specified stacks for Amazon AppStream 2.0. Users in an AppStream 2.0 user pool cannot be assigned to stacks with fleets that are joined to an Active Directory domain.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html
    :cloudformationResource: AWS::AppStream::StackUserAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_stack_user_association = appstream.CfnStackUserAssociation(self, "MyCfnStackUserAssociation",
            authentication_type="authenticationType",
            stack_name="stackName",
            user_name="userName",
        
            # the properties below are optional
            send_email_notification=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authentication_type: builtins.str,
        stack_name: builtins.str,
        user_name: builtins.str,
        send_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authentication_type: The authentication type for the user who is associated with the stack. You must specify USERPOOL.
        :param stack_name: The name of the stack that is associated with the user.
        :param user_name: The email address of the user who is associated with the stack. .. epigraph:: Users' email addresses are case-sensitive.
        :param send_email_notification: Specifies whether a welcome email is sent to a user after the user is created in the user pool.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bec854832b0f9d56be7a3fa2822fd9c3f4650fc7b55e2919217a926149ad3822)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStackUserAssociationProps(
            authentication_type=authentication_type,
            stack_name=stack_name,
            user_name=user_name,
            send_email_notification=send_email_notification,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fc440f2584146110d88e7aa205e80c9b34c5265556c539b3b2bcac8f31abb00)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd7cd42a6fc37e11b959ada6805ef35fd3c5c6c112a20143cd1906c8e925b55b)
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
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        '''The authentication type for the user who is associated with the stack.'''
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e46f1ddf20cb94c7b8afcf586155774dba52d59ef09e1c66a333238fd73c9caf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        '''The name of the stack that is associated with the user.'''
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @stack_name.setter
    def stack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1832d9f3bba153dde7b7383449d3340abc46bb8e348bb16bce8968a4abe826)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackName", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The email address of the user who is associated with the stack.'''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f5cf4643b9d3d31802d1cb1b08e3f5b2966db6bf0257fe4a730a1a1035ec0b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="sendEmailNotification")
    def send_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a welcome email is sent to a user after the user is created in the user pool.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "sendEmailNotification"))

    @send_email_notification.setter
    def send_email_notification(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3463450ee71bea209f38a68febac5e6a88747dcc544b3bea07a8a94198c6b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendEmailNotification", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnStackUserAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "stack_name": "stackName",
        "user_name": "userName",
        "send_email_notification": "sendEmailNotification",
    },
)
class CfnStackUserAssociationProps:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        stack_name: builtins.str,
        user_name: builtins.str,
        send_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStackUserAssociation``.

        :param authentication_type: The authentication type for the user who is associated with the stack. You must specify USERPOOL.
        :param stack_name: The name of the stack that is associated with the user.
        :param user_name: The email address of the user who is associated with the stack. .. epigraph:: Users' email addresses are case-sensitive.
        :param send_email_notification: Specifies whether a welcome email is sent to a user after the user is created in the user pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_stack_user_association_props = appstream.CfnStackUserAssociationProps(
                authentication_type="authenticationType",
                stack_name="stackName",
                user_name="userName",
            
                # the properties below are optional
                send_email_notification=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74aaf98b7d4c632c40e4e8dc18d65c1b406717f29b491f772b1e285eb5861fd8)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument send_email_notification", value=send_email_notification, expected_type=type_hints["send_email_notification"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
            "stack_name": stack_name,
            "user_name": user_name,
        }
        if send_email_notification is not None:
            self._values["send_email_notification"] = send_email_notification

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''The authentication type for the user who is associated with the stack.

        You must specify USERPOOL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html#cfn-appstream-stackuserassociation-authenticationtype
        '''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The name of the stack that is associated with the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html#cfn-appstream-stackuserassociation-stackname
        '''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The email address of the user who is associated with the stack.

        .. epigraph::

           Users' email addresses are case-sensitive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html#cfn-appstream-stackuserassociation-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def send_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a welcome email is sent to a user after the user is created in the user pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html#cfn-appstream-stackuserassociation-sendemailnotification
        '''
        result = self._values.get("send_email_notification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackUserAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnUser(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appstream.CfnUser",
):
    '''The ``AWS::AppStream::User`` resource creates a new user in the AppStream 2.0 user pool.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html
    :cloudformationResource: AWS::AppStream::User
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appstream as appstream
        
        cfn_user = appstream.CfnUser(self, "MyCfnUser",
            authentication_type="authenticationType",
            user_name="userName",
        
            # the properties below are optional
            first_name="firstName",
            last_name="lastName",
            message_action="messageAction"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authentication_type: builtins.str,
        user_name: builtins.str,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        message_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authentication_type: The authentication type for the user. You must specify USERPOOL.
        :param user_name: The email address of the user. Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a "user does not exist" error message displays.
        :param first_name: The first name, or given name, of the user.
        :param last_name: The last name, or surname, of the user.
        :param message_action: The action to take for the welcome email that is sent to a user after the user is created in the user pool. If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent. .. epigraph:: The temporary password in the welcome email is valid for only 7 days. If users don’t set their passwords within 7 days, you must send them a new welcome email.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__716c51c6b5353935015ec2b3097e7582be6792bda1cc35f5349c641e91cff4e3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            authentication_type=authentication_type,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            message_action=message_action,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08917d0379ee7f4fd15be088187bda263e9a310bfb855a6c2552f701536894a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__edd995bb38e7bbfc88fec5fc602141669ba590a81fd3cd1d6a9d109d5332da58)
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
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        '''The authentication type for the user.'''
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d5782def52c65e0af3cbeb4b003c99a002d38506f31afcdad4637977ce821b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The email address of the user.'''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__978b61253044095f22afb923283b01ecdcc062b909008121ce464207b23e6a90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> typing.Optional[builtins.str]:
        '''The first name, or given name, of the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bccc3305423a43aa55248d3c9fd9e654338f9317eab3d98a2d8d512e2a575072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> typing.Optional[builtins.str]:
        '''The last name, or surname, of the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e186a2f566258aa2e46f273f7866c2de4e4844214046c5fd15ffbc17cbdd6244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="messageAction")
    def message_action(self) -> typing.Optional[builtins.str]:
        '''The action to take for the welcome email that is sent to a user after the user is created in the user pool.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageAction"))

    @message_action.setter
    def message_action(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39dceea8a6664abbe00f127243f53a5951099209c0866b52a504bf3044e4241f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageAction", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appstream.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "user_name": "userName",
        "first_name": "firstName",
        "last_name": "lastName",
        "message_action": "messageAction",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        user_name: builtins.str,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        message_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnUser``.

        :param authentication_type: The authentication type for the user. You must specify USERPOOL.
        :param user_name: The email address of the user. Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a "user does not exist" error message displays.
        :param first_name: The first name, or given name, of the user.
        :param last_name: The last name, or surname, of the user.
        :param message_action: The action to take for the welcome email that is sent to a user after the user is created in the user pool. If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent. .. epigraph:: The temporary password in the welcome email is valid for only 7 days. If users don’t set their passwords within 7 days, you must send them a new welcome email.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appstream as appstream
            
            cfn_user_props = appstream.CfnUserProps(
                authentication_type="authenticationType",
                user_name="userName",
            
                # the properties below are optional
                first_name="firstName",
                last_name="lastName",
                message_action="messageAction"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59d6dce4cd4b814f53051d27e4f9e61dcb2e7cccfbc898cc602607476ea77395)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument message_action", value=message_action, expected_type=type_hints["message_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
            "user_name": user_name,
        }
        if first_name is not None:
            self._values["first_name"] = first_name
        if last_name is not None:
            self._values["last_name"] = last_name
        if message_action is not None:
            self._values["message_action"] = message_action

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''The authentication type for the user.

        You must specify USERPOOL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-authenticationtype
        '''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The email address of the user.

        Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a "user does not exist" error message displays.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_name(self) -> typing.Optional[builtins.str]:
        '''The first name, or given name, of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-firstname
        '''
        result = self._values.get("first_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_name(self) -> typing.Optional[builtins.str]:
        '''The last name, or surname, of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-lastname
        '''
        result = self._values.get("last_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_action(self) -> typing.Optional[builtins.str]:
        '''The action to take for the welcome email that is sent to a user after the user is created in the user pool.

        If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent.
        .. epigraph::

           The temporary password in the welcome email is valid for only 7 days. If users don’t set their passwords within 7 days, you must send them a new welcome email.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-messageaction
        '''
        result = self._values.get("message_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAppBlock",
    "CfnAppBlockBuilder",
    "CfnAppBlockBuilderProps",
    "CfnAppBlockProps",
    "CfnApplication",
    "CfnApplicationEntitlementAssociation",
    "CfnApplicationEntitlementAssociationProps",
    "CfnApplicationFleetAssociation",
    "CfnApplicationFleetAssociationProps",
    "CfnApplicationProps",
    "CfnDirectoryConfig",
    "CfnDirectoryConfigProps",
    "CfnEntitlement",
    "CfnEntitlementProps",
    "CfnFleet",
    "CfnFleetProps",
    "CfnImageBuilder",
    "CfnImageBuilderProps",
    "CfnStack",
    "CfnStackFleetAssociation",
    "CfnStackFleetAssociationProps",
    "CfnStackProps",
    "CfnStackUserAssociation",
    "CfnStackUserAssociationProps",
    "CfnUser",
    "CfnUserProps",
]

publication.publish()

def _typecheckingstub__41cea9e42ea830db5b0d999c409efe33186557a7bb3be96abafb06fba47482c9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    source_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    packaging_type: typing.Optional[builtins.str] = None,
    post_setup_script_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.ScriptDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    setup_script_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.ScriptDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ef0c832915a964995aef2c59ffa4492185116744601f84186bb724561d2bf7e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d32d2a9da5d96e63b2ca346390b8f58c00ce6fbf8704303679cd9e77c84c363b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ecda575988f84aef9017ebbc9caa5b673bb06457ea5362157d745c55bb2f5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a504881240dbb8e4d49a5c3509bd9afb394356e43746a04d59cfeedc8ca2949(
    value: typing.Union[_IResolvable_da3f097b, CfnAppBlock.S3LocationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88e9d4134f7f7352e3e69141d073b4571541a079a733164dada584671a936918(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6346454c9b1e9f0b74872f97613850d9892e436b8e479fff337895c59a6885f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46503228b5203f79b0306e550d548542da93d07ce7c0094df440dcdf94c8164(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b19b4dc43a42401721ecc3c51a40c838ce7167fe3ecd27eae1eb5639adcdd3d7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAppBlock.ScriptDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d14e1522f81e1c48d4360cf330cdfac3f189fc416e28492b7d675d522f79a41c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAppBlock.ScriptDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44d020fa00d7c6033b8a7317dffe2fc57d25861244d1c79a52394344ee58e3a8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3984118729e2d72b9f813b24157e458bdc05747e70cacda34fd5c17fb557da0(
    *,
    s3_bucket: builtins.str,
    s3_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b4987276279c543e86060c2474d9b8d33b9395331f346758fe51e79a75d78c(
    *,
    executable_path: builtins.str,
    script_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    timeout_in_seconds: jsii.Number,
    executable_parameters: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2dbe872e5cba24425b73eff2bd90d7b1c6af7a2b3b47d455ff4683fb5c3b559(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_type: builtins.str,
    name: builtins.str,
    platform: builtins.str,
    vpc_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlockBuilder.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlockBuilder.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    app_block_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__560ef45e47870972c6b9d1538088c62bf2a04bfeb5ca9a51c7fe0b65e8ec8511(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d3986dbb1b3fffafc9f179d356205fdd37785ebd341b7f3bdb113b697cda7c3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f21b6ecd30e303361f359d504ba6d4430fa39df00d8db479a13a42cafb98fae1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d93595f1388c9e3a643d55562aceb2635a4d08dfc401ab918be963bd34d37fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b091d87f29dcb5d30e2004be0e23c286ac25a0d91972c2a15f504513758f527(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__180d8c618c42d04568f892dee70a7790f7e99eeb61d519960b3b033c12cfe689(
    value: typing.Union[_IResolvable_da3f097b, CfnAppBlockBuilder.VpcConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c2370cdeeba05804fa6dd3f03d3862ece8f691558c77fb2a589df46ab16118(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAppBlockBuilder.AccessEndpointProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf5cb8b2ccd8f98c58e0fb8358a949225e23002425ae28212a658e15797b9d92(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__182b4edd83508ba66a0f582b454b58fa740d47820caf28e86a8ab22c5b227d82(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc53127e490e484f1257f25a433fbbd6130ffe2bee9e0368471246d58d6ee95(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47484d5ec55d944eba05db1c12e9dd2dbf40de14a4080c6840d63d110ec36bbe(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be31238972433ba4e0bfd240749782ef85ea23f117dfd179b56cff0e355e3634(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7e7e62dce5b776582e32baec62848ca5111cb28b2742ac5e7e945e0160279c6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39fcf5386df3e63b3df8d03a9fbecf60ced2b40b3644175eba767c428a336b47(
    *,
    endpoint_type: builtins.str,
    vpce_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23900099939292b49034d4a7bcee1e44ad2bddaf629079b514d80ab283d4f3a5(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e788750b4b78274a373182d9b8ff84f13602b9b9ce827c99dbbbeefc73304b62(
    *,
    instance_type: builtins.str,
    name: builtins.str,
    platform: builtins.str,
    vpc_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlockBuilder.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlockBuilder.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    app_block_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d81fb9c3e1fcc7b221dbc8290b04501b1af7d21a103a5dacb19c8221493f37f1(
    *,
    name: builtins.str,
    source_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    packaging_type: typing.Optional[builtins.str] = None,
    post_setup_script_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.ScriptDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    setup_script_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAppBlock.ScriptDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9009fa37c2ae00864d9c32d96617498f6fbd69d6e961b9ed0d57b66ea8a5aa1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_block_arn: builtins.str,
    icon_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    instance_families: typing.Sequence[builtins.str],
    launch_path: builtins.str,
    name: builtins.str,
    platforms: typing.Sequence[builtins.str],
    attributes_to_delete: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    launch_parameters: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bf37e6c9ebba93b6a20dd8c55575bfc26f65f587453e4fec87a3350335fdb30(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d9ff0358639f98e3ffd67a11c5427b0ccf256c68f482d14513971d5bc203aad(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcbe3239165a897dd7ad3a3fb56bb3ff4580d04e8314de0bec6b8d3e41adeb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d27419218adf8ae55a390ca9152b985b34509b75fa155ff05a6a369102ab5a88(
    value: typing.Union[_IResolvable_da3f097b, CfnApplication.S3LocationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e95fdca457194dd65826ce4e71255ef17556d2d8bb11d3a670954924dbe32f1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c335406efc0386216f2a85242b30ab101cf760b35a8620b10ea48dff3fde6a11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afd432f06fc6cd02ca04ce3797550366ccf6d404c3627c0362d247ddbfa2045e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d99c34004e688e8f22a332a95e547b6042c8fc6a0760dcaad6c34686394a7f9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c745e8006ba5ff2e086ec711fad075fddbe792a8fe62ceaa7dd7e17d158fbb8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c44932d7f0f284fe848233f6e1bc2a9e4f048b30f4ee940536cd8ba326dbffdf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2757cdff10448b7e8c5fc4692665051f8b68fd4716ae94305bb5252b295e66ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7722e337d3920d2871f9264abb6a26bb6fb91856e56ce963442b77ebc01334a6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef307b076d145751ab1f61dcfc9204a3570e7d2c27321158a89b936291a3acdd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea002ddddf4927ba2d1d69d37cd236583ea870d351ac4f4ba1bb3b6456c69d51(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a8ebd800bb6d4c915d27e4699c03161df65019eb746af6eae942b742f31642(
    *,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1cdc188825edd09dc8b562b0fb59405ff1d3a7942b872ef7b24a3a18648602(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_identifier: builtins.str,
    entitlement_name: builtins.str,
    stack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e86041351b8926af1b6fa9d6e94a9bc63d2cac6ebbe156417e48f02826ee48f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e2c4dd6d4e83da25e1ba9e622419616042c3e1f148babe9d09d07921cc19972(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6566993bed166d8777fd15b08de32b886de69d33d7e37333d92a0e6d7b667c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__863b971564ea879f8a7165cc88fbcf8117ce148b8625b4ce8b028fe61f62c7ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__120e4482e49986c6ca616b933efc543a39747121fc631acf467d6d6530edfc26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ed66445aef0340172777886fa668a63161e6556da0c4ddda56f9f1d4ec958ba(
    *,
    application_identifier: builtins.str,
    entitlement_name: builtins.str,
    stack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9dfb530d7e84f7276b2c13f4b5afbb9da758e394426c8ec880af3ce38971813(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_arn: builtins.str,
    fleet_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a8fc6d4b86e014acd36e8f0f9ffe74fa31c53ce71ff255c2289e11e9c2606d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b68a5c4074a80a2bc5799134c0abea39b97d041de070648f2edac64131f7534(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991b96fa7affbe3e674886c56e8c99de877d878da156c1eecdb8136f55e15535(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0aaa8270f20c093ca5740d4e9601ed61163065bb9b02b6ff293151ec389d60e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d294820a31c019b7ec8574f34a068e3a21437c2751ab65ed99beb677455d420a(
    *,
    application_arn: builtins.str,
    fleet_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb96c46dcf41b8bf52ccede1fadb0b2ffaef8995b618f1e0816e434f6605e2f2(
    *,
    app_block_arn: builtins.str,
    icon_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    instance_families: typing.Sequence[builtins.str],
    launch_path: builtins.str,
    name: builtins.str,
    platforms: typing.Sequence[builtins.str],
    attributes_to_delete: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    launch_parameters: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__038372f18e366a333df8768cd289dcbe82f03750464d283eb0ef89fcbf90577c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    directory_name: builtins.str,
    organizational_unit_distinguished_names: typing.Sequence[builtins.str],
    service_account_credentials: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryConfig.ServiceAccountCredentialsProperty, typing.Dict[builtins.str, typing.Any]]],
    certificate_based_auth_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d97debe358c81c37b199083a9ccbc136be57ab6cd95df38a148a3fd2ea188f6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e54e8ff33797aab702918ecb86bf9eed890a16455e3ff48b3d67bc488b6818e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671a9ec8a1b2b5d0d93643e14e6916b2417e5e73e7134aebc9f410fbb98d7c7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__630eb00e19cb58292c211d1a006f8dd52b859f57c892e7425b2fb0cd1f62b762(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f17c467f37ff964c4e56ff7a5b6800877e168375f3aa44347e71dee2de5ef8(
    value: typing.Union[_IResolvable_da3f097b, CfnDirectoryConfig.ServiceAccountCredentialsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89617ee3f9d3ab9cc3d861814bdbc0f0dcde8b3fb5da771e78c8feccf0a3e19(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffca79fb887aa55066c3b8724a3bdc6f8de1654ed6be4ef85d6468ed7ed950ca(
    *,
    certificate_authority_arn: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844f7de5d43ef3bfc92f8ee34800439d7fe27186f269bed1be021e10ee58164f(
    *,
    account_name: builtins.str,
    account_password: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__578684e8816c2df1e186869cdebb5605355669857041d859dd30c2859c435801(
    *,
    directory_name: builtins.str,
    organizational_unit_distinguished_names: typing.Sequence[builtins.str],
    service_account_credentials: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryConfig.ServiceAccountCredentialsProperty, typing.Dict[builtins.str, typing.Any]]],
    certificate_based_auth_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryConfig.CertificateBasedAuthPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0bfa3b98fc526a6a563308a8862238ce51273e7eb19d8bbebd7a86fb7e44502(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_visibility: builtins.str,
    attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEntitlement.AttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    stack_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c9d56192f87abfa7e1a4fabdb31d1a5e1d437fd8216f9858ffda414e951d660(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2437978a9ad12b18d2e3ddda0a06cabe403a32e8fb2c71839868ba72be02671(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db254c441b5a86a836711719ab5bafae630e66529b39f62dee4c510a7e5d9cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa3674f46bbe39146e43d1c3c58c9be8a7fa2b7972b4709b3fa29dcf86420d4(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEntitlement.AttributeProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1b3d753cadafb7385d25d134e4181963f7a41b9f8b44225981b664b92c82d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f2d532168c00c02bedd8960de80d1d1be3ec7880a902292ec08e8f01dfc689b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__545e3c21562a3817f7c25161b610d37ec5b881d014fc1d9d876354a51c3fcd29(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c09f476db6997870a53f0b29bef4fa36a8d180cbfb901e0f9e6f0fdfb04778de(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e7b6ad14b42e5a4dc8b1f0be3cc48eb3f96a7fc22176cfee8fe233b842ca6c9(
    *,
    app_visibility: builtins.str,
    attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEntitlement.AttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    stack_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__043ee41cbba03b784a0f77c0a2cc8efea9ae9147537890e0795e729547d5d4ff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_type: builtins.str,
    name: builtins.str,
    compute_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ComputeCapacityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    display_name: typing.Optional[builtins.str] = None,
    domain_join_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.DomainJoinInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    idle_disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    image_arn: typing.Optional[builtins.str] = None,
    image_name: typing.Optional[builtins.str] = None,
    max_concurrent_sessions: typing.Optional[jsii.Number] = None,
    max_sessions_per_instance: typing.Optional[jsii.Number] = None,
    max_user_duration_in_seconds: typing.Optional[jsii.Number] = None,
    platform: typing.Optional[builtins.str] = None,
    session_script_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stream_view: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    usb_device_filter_strings: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a64a6d87c0b62f880d7b34e935538ef5f5648fee18223b97400ee72688a9f7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d551b4b29a3f115fdadd7697e1de7bb10702e2036e3a25e4556a54087e402b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a6ef061b0bedfe2a4a7f001125bc3274c3704e34a43dc8418d62592df836097(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e2214e24b9fd1c11c53bebf170bcc6e7c03917559f47d5d33ea2525089fdf8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50699376ca4215fbf67913c64e0ae0edb7e243785d08cef6bc529f44ca0f141a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ComputeCapacityProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9409234ac32054c73634d4ffe5cc51eed2d25f9373a83380b7693f06ff5a9e56(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7b891e70c70c71b4742be14d3dd1903d0ec64bb461a57f0aa83d3997a151dfa(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5f49946d1e23d200d37b1f8ea8f79d9757a1da17de932a0c0617ac288ddf5b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd86f9dbfba3a27b2385e8b9586bb3aa31b4e2aa0a3e91794b42a6881add1126(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.DomainJoinInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f219b4aa3da3a06d8016cbf3252298a91c9c2811252b39c6ac9adb9b2e3ee798(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51b3228ce2b0c145877b00c8bf4eca31f4e517d5cbe1d8f39944f113c7aaabce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ee05e008a0394f50d61a211df9373128f6625ffc891f8343efa62cdde56436(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53b211e70fac8180eefa6a9dd10825d32317d051e002818d8c808f7cb493697e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edf3360ada81e5be766ffda88924f99bb0bc36a7f9cd324041b71f987c4ad249(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2ecac5e12920461571674f2b4175ac2b87887d3edba0db37def3d12d002088(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cef147ceca130b53c86908dc50dff718cb362a4b25c765b783420d7115404ded(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d2d0956b116cf95d995d13ffce00e3483d95f5d61d41f2e9bc4202eb0997e48(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6ad7b5fa21e0983e0e093b56d8c6bae1f0e93752767339c1b9bf91621aacf1(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9129dd496d9b4790cdd5f195fbd566cf9b4924df5068de89d89903c26def0d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79935e15ee3dfe1dba785d906ccdd9a4e5895f1d61d25026dbdddf01558f5be8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab9bf4177a813f1507a9cefa186c313a820bdfb89dd6791547c863e11771a203(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__839d0da01c455496fc067fbca5ed5c23c8fb170e5989a05bf711b7b574b7d416(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3e185c1216c446ebc68c660e2e3cc0b3515ddb113048def6faa8bd38653a80e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8452c6c1c918a8718280c5b321c677cd442bc97d2e69bc3f9aaa1690c901ffc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.VpcConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ca5878c0aa8c5995893aac0046342d8942452bc466a936ffbf559e60bbe3bb(
    *,
    desired_instances: typing.Optional[jsii.Number] = None,
    desired_sessions: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ce7aedf15d7749daa18c62b97de590b90b107ea31ce355c68f50a78346fbbe6(
    *,
    directory_name: typing.Optional[builtins.str] = None,
    organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad58c387c2ce79f6cc90043caf5f503d6456bb90cde093dde2788eca29f15d9(
    *,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b84008983de6a1ed7aa5257a44cfb82723e58267dad7890bb77001fd73009f6d(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c1696e8b6f6c109609fff783812cdcaafc37e209e10ad5c9f177ee9699fa56e(
    *,
    instance_type: builtins.str,
    name: builtins.str,
    compute_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ComputeCapacityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    display_name: typing.Optional[builtins.str] = None,
    domain_join_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.DomainJoinInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    idle_disconnect_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    image_arn: typing.Optional[builtins.str] = None,
    image_name: typing.Optional[builtins.str] = None,
    max_concurrent_sessions: typing.Optional[jsii.Number] = None,
    max_sessions_per_instance: typing.Optional[jsii.Number] = None,
    max_user_duration_in_seconds: typing.Optional[jsii.Number] = None,
    platform: typing.Optional[builtins.str] = None,
    session_script_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stream_view: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    usb_device_filter_strings: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25dccb4354e677f39c5c97fd983d6a76f7631b1133ab64219d2975708166efe2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_type: builtins.str,
    name: builtins.str,
    access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    appstream_agent_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    domain_join_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.DomainJoinInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    image_arn: typing.Optional[builtins.str] = None,
    image_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec74adc688e0bdb7f0a14897529e4e6caef09d76aeb15844a23cc95502d7639(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cabc43267017cfc44ea4bbb9c3fa1ef592d580fffa6115a90205b3bb2253b503(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__771bb6faeddd106d643f98bc3510eefbca762110055a75ca894c1a1853d7ba47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c195974bec3d3620852bd27476c403eaa4214fa33dc9f1b6cd27639799fca71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746e4a9e3f48985b9bf8079b3d895e3a8b0a7748caeb868365ff2a47e2ed9d36(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.AccessEndpointProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbfe60f13227554e339b92afa2a96a3531634abbc6108618cf474533196cb365(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a114f3ea3a654e9d4d760cdf7443cc73aa66b6e2b8f2c4d7d333accb36b9b88f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a4101b60decd67001a1345c45d86ab1b421408ad10f6b8e58e966cbb1897cd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee5fc96661993bc890e05b1f0ae7eaf9202f05399a6fda1444d3b6323d544d2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.DomainJoinInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234082991507fccd1b51ac27db4c813ef4030635f0b32ddf3ab652b7f320fa6f(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc542d91573c5313d5e4aa541efb2157e25e39cc082ca1991fc0e914e961471c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9661eef012d30e6482b8ebd48017128248f34a0a5b6f81200efab39a411f6b7c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9671544139fb85d314712452cdf120b8083f58b155c561f6fe3cf4492bd91a05(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32bb0a47350b5b67e1529a3d54fee7241fa2dab126f8e11eba610f03592bc255(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e1029afa7ae41d9f4b692bbfd0623efa3755c15eb5a169b6191a4657ce20885(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageBuilder.VpcConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1311b50cfabf41e75ebeb9e0609a5fda76aa93594d88a9d8d050110731c3073b(
    *,
    endpoint_type: builtins.str,
    vpce_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e8369c89d03719c64d2c83e51b7e08b1b75d665769bd928f11984729ab04d24(
    *,
    directory_name: typing.Optional[builtins.str] = None,
    organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d93dcafbda7cc30fc6a56bcf4eebd91a55747713e0043d6fdac8bc1f7237ce(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f00d771423a1edbc076328e18ee5a37fbf5bb31404bdb6b4224eba3f881e4810(
    *,
    instance_type: builtins.str,
    name: builtins.str,
    access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    appstream_agent_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    domain_join_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.DomainJoinInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_default_internet_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    image_arn: typing.Optional[builtins.str] = None,
    image_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageBuilder.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add685d2c205e11b1f2727c7c09ea99b5fd4739effbaca1fd079659e5f37439d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    application_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ApplicationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    attributes_to_delete: typing.Optional[typing.Sequence[builtins.str]] = None,
    delete_storage_connectors: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    embed_host_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    feedback_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    redirect_url: typing.Optional[builtins.str] = None,
    storage_connectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StorageConnectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    streaming_experience_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StreamingExperienceSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.UserSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb250bd0ddb058fba554647ecaf8a602c6ffc9518afdb0c6b6c75dcb6e673ac2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4e065b6d01f90eee058076d521bb71fbc0a489b794e50fc75dc867f6b3c906(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad9a87386d835ff4af56b6ca6b53baa12cd008bd109294050154f77511bc98cd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.AccessEndpointProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318b1e9f0d5854a3c702b5b51837caed9c2f8ef41e3bc15d8e0cdac003bf38b5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.ApplicationSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c273fef3acafd8229cbff7e9a2c1b03a874f74a6397ceeb316e0b9ae83ae12(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd3eed1a7554981a61b92b8848f5b531271aad947e65c20f9604a014bca0a673(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f47b501b000d9e8d0b5a92a98d9b1b6e43924d0508d9c95323d961a8e6892b46(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d9674cac50abf3d7c71f658f161af8c5dfda7e99b6e3ed0ac5757b86f7c359(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e724a0f54ce83bd45cd8d43d8af34006db8700d91fa4a6ccfec245ffdb2ddc97(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844efac5860b4d32faef93720e2c6a1abbcc41678d249a453e14ba3722be9904(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73280be80fedcfcb318f73a4dbe80e309ed0d2f02b7aedb45617faf540cc7511(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dda375121bdfb203a69bc3a2485d69e2ee01da1e4327d7116bfac610f8927d22(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__275ea87a7dfdce8c58071ca77a17a383b5b77dc023446160cf3c8af4d0ba7238(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.StorageConnectorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab82aff9577044655905fdadec884f88fa2e07d1163701496f44bb2a9903bda5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.StreamingExperienceSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d8194ace5a04925ea85c21feb9edfbcc17535be57ee024386cc650e109718ce(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf30847a0d21a9895ed825ab61f3abb249fb73253d9806ea965739b1698fa46(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.UserSettingProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16b91ca2aed5404f22e03b015fd7cb7dfa614fffde2d87be465daef732bf300e(
    *,
    endpoint_type: builtins.str,
    vpce_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd2bf22e417927425b480fb9f77598b6dc3c52bceeccd8e20029d3afe1dd49e(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    settings_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5f4551020c535e3e6e3df104109b0aa10638f110819d36a938d2fea05892f89(
    *,
    connector_type: builtins.str,
    domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c91289741f79afeb2e10af943a02636d21ff3e2882ecef22a76b60441af0e394(
    *,
    preferred_protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f08d4ad1bd849bb76b897fa82448efbc7d5525adc690cc1128fc23d090e97a(
    *,
    action: builtins.str,
    permission: builtins.str,
    maximum_length: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93298a8702bdb81bee8aa40e3e8877e0f9ff694374a42c0c1997d95079c7140(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    fleet_name: builtins.str,
    stack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48d22fdad8c6f0375110dcf28aeec8ed277936eb365c074fcbcbc0f2e959297(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3b4d53c3d446f718a46bdea3c087759b17cadceb19025592653406dd89c41d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3954597e38e49c693cdf9002320951ac5284d459fe9df8a7bd94c418997f2942(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f091262b0bcbec47a122c68936b6834a45a0aeebefa27b699caf9d999a15b8b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1480c1a389e0a505f08c8a89fcde9176cdb68f3f06682e9ee925e2d04934be68(
    *,
    fleet_name: builtins.str,
    stack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f5987726340331a807da3e721dc066e307475a26a6ce0ddcd409aa8fa0fe4b7(
    *,
    access_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.AccessEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    application_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ApplicationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    attributes_to_delete: typing.Optional[typing.Sequence[builtins.str]] = None,
    delete_storage_connectors: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    embed_host_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    feedback_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    redirect_url: typing.Optional[builtins.str] = None,
    storage_connectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StorageConnectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    streaming_experience_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StreamingExperienceSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.UserSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bec854832b0f9d56be7a3fa2822fd9c3f4650fc7b55e2919217a926149ad3822(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authentication_type: builtins.str,
    stack_name: builtins.str,
    user_name: builtins.str,
    send_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc440f2584146110d88e7aa205e80c9b34c5265556c539b3b2bcac8f31abb00(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd7cd42a6fc37e11b959ada6805ef35fd3c5c6c112a20143cd1906c8e925b55b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e46f1ddf20cb94c7b8afcf586155774dba52d59ef09e1c66a333238fd73c9caf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d1832d9f3bba153dde7b7383449d3340abc46bb8e348bb16bce8968a4abe826(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f5cf4643b9d3d31802d1cb1b08e3f5b2966db6bf0257fe4a730a1a1035ec0b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3463450ee71bea209f38a68febac5e6a88747dcc544b3bea07a8a94198c6b54(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74aaf98b7d4c632c40e4e8dc18d65c1b406717f29b491f772b1e285eb5861fd8(
    *,
    authentication_type: builtins.str,
    stack_name: builtins.str,
    user_name: builtins.str,
    send_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__716c51c6b5353935015ec2b3097e7582be6792bda1cc35f5349c641e91cff4e3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authentication_type: builtins.str,
    user_name: builtins.str,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    message_action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08917d0379ee7f4fd15be088187bda263e9a310bfb855a6c2552f701536894a6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edd995bb38e7bbfc88fec5fc602141669ba590a81fd3cd1d6a9d109d5332da58(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5782def52c65e0af3cbeb4b003c99a002d38506f31afcdad4637977ce821b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978b61253044095f22afb923283b01ecdcc062b909008121ce464207b23e6a90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bccc3305423a43aa55248d3c9fd9e654338f9317eab3d98a2d8d512e2a575072(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e186a2f566258aa2e46f273f7866c2de4e4844214046c5fd15ffbc17cbdd6244(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39dceea8a6664abbe00f127243f53a5951099209c0866b52a504bf3044e4241f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59d6dce4cd4b814f53051d27e4f9e61dcb2e7cccfbc898cc602607476ea77395(
    *,
    authentication_type: builtins.str,
    user_name: builtins.str,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    message_action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
