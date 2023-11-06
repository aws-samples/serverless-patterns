'''
# Amazon WorkSpaces Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_workspaces as workspaces
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for WorkSpaces construct libraries](https://constructs.dev/search?q=workspaces)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::WorkSpaces resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpaces.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::WorkSpaces](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpaces.html).

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
class CfnConnectionAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspaces.CfnConnectionAlias",
):
    '''The ``AWS::WorkSpaces::ConnectionAlias`` resource specifies a connection alias.

    Connection aliases are used for cross-Region redirection. For more information, see `Cross-Region Redirection for Amazon WorkSpaces <https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspaces as workspaces
        
        cfn_connection_alias = workspaces.CfnConnectionAlias(self, "MyCfnConnectionAlias",
            connection_string="connectionString",
        
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
        connection_string: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connection_string: The connection string specified for the connection alias. The connection string must be in the form of a fully qualified domain name (FQDN), such as ``www.example.com`` .
        :param tags: The tags to associate with the connection alias.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd73d00432c1164a74beb35acf6162e3d82fa91d51a0edf8c896028b6e3c6d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectionAliasProps(connection_string=connection_string, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70d07e3ef46b7d1868d493367bae11c00c38fa0bb35cfa4e162e97b1482bf156)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d590d73fb55367a8be64477837c062053aa020d8931e1f1983124013786434f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAliasId")
    def attr_alias_id(self) -> builtins.str:
        '''The identifier of the connection alias, returned as a string.

        :cloudformationAttribute: AliasId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAliasId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociations")
    def attr_associations(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Associations
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAssociations"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionAliasState")
    def attr_connection_alias_state(self) -> builtins.str:
        '''The current state of the connection alias, returned as a string.

        :cloudformationAttribute: ConnectionAliasState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionAliasState"))

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
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> builtins.str:
        '''The connection string specified for the connection alias.'''
        return typing.cast(builtins.str, jsii.get(self, "connectionString"))

    @connection_string.setter
    def connection_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8b72c0a6880f896fe31f0555dd87dfdcce86c05579ff4a417ab736a03b4fda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionString", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to associate with the connection alias.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cf34741743106631ede324d61fdd5ed726b94e64d09574347d59201303db6f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspaces.CfnConnectionAlias.ConnectionAliasAssociationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "associated_account_id": "associatedAccountId",
            "association_status": "associationStatus",
            "connection_identifier": "connectionIdentifier",
            "resource_id": "resourceId",
        },
    )
    class ConnectionAliasAssociationProperty:
        def __init__(
            self,
            *,
            associated_account_id: typing.Optional[builtins.str] = None,
            association_status: typing.Optional[builtins.str] = None,
            connection_identifier: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param associated_account_id: 
            :param association_status: 
            :param connection_identifier: 
            :param resource_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspaces as workspaces
                
                connection_alias_association_property = workspaces.CfnConnectionAlias.ConnectionAliasAssociationProperty(
                    associated_account_id="associatedAccountId",
                    association_status="associationStatus",
                    connection_identifier="connectionIdentifier",
                    resource_id="resourceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__614a827f45558e3ee89a9937d774dc07580e2d2d88ccf9a78ea211acad9d7c19)
                check_type(argname="argument associated_account_id", value=associated_account_id, expected_type=type_hints["associated_account_id"])
                check_type(argname="argument association_status", value=association_status, expected_type=type_hints["association_status"])
                check_type(argname="argument connection_identifier", value=connection_identifier, expected_type=type_hints["connection_identifier"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if associated_account_id is not None:
                self._values["associated_account_id"] = associated_account_id
            if association_status is not None:
                self._values["association_status"] = association_status
            if connection_identifier is not None:
                self._values["connection_identifier"] = connection_identifier
            if resource_id is not None:
                self._values["resource_id"] = resource_id

        @builtins.property
        def associated_account_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associatedaccountid
            '''
            result = self._values.get("associated_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def association_status(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associationstatus
            '''
            result = self._values.get("association_status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_identifier(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-connectionidentifier
            '''
            result = self._values.get("connection_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionAliasAssociationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspaces.CfnConnectionAliasProps",
    jsii_struct_bases=[],
    name_mapping={"connection_string": "connectionString", "tags": "tags"},
)
class CfnConnectionAliasProps:
    def __init__(
        self,
        *,
        connection_string: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnectionAlias``.

        :param connection_string: The connection string specified for the connection alias. The connection string must be in the form of a fully qualified domain name (FQDN), such as ``www.example.com`` .
        :param tags: The tags to associate with the connection alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspaces as workspaces
            
            cfn_connection_alias_props = workspaces.CfnConnectionAliasProps(
                connection_string="connectionString",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33d1c548638caf6c8699dd74d5bcc8d8df516e1a0738521496aee37402727de8)
            check_type(argname="argument connection_string", value=connection_string, expected_type=type_hints["connection_string"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_string": connection_string,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connection_string(self) -> builtins.str:
        '''The connection string specified for the connection alias.

        The connection string must be in the form of a fully qualified domain name (FQDN), such as ``www.example.com`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-connectionstring
        '''
        result = self._values.get("connection_string")
        assert result is not None, "Required property 'connection_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to associate with the connection alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectionAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkspace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspaces.CfnWorkspace",
):
    '''The ``AWS::WorkSpaces::Workspace`` resource specifies a WorkSpace.

    Updates are not supported for the ``BundleId`` , ``RootVolumeEncryptionEnabled`` , ``UserVolumeEncryptionEnabled`` , or ``VolumeEncryptionKey`` properties. To update these properties, you must also update a property that triggers a replacement, such as the ``UserName`` property.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspaces as workspaces
        
        cfn_workspace = workspaces.CfnWorkspace(self, "MyCfnWorkspace",
            bundle_id="bundleId",
            directory_id="directoryId",
            user_name="userName",
        
            # the properties below are optional
            root_volume_encryption_enabled=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_volume_encryption_enabled=False,
            volume_encryption_key="volumeEncryptionKey",
            workspace_properties=workspaces.CfnWorkspace.WorkspacePropertiesProperty(
                compute_type_name="computeTypeName",
                root_volume_size_gib=123,
                running_mode="runningMode",
                running_mode_auto_stop_timeout_in_minutes=123,
                user_volume_size_gib=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bundle_id: builtins.str,
        directory_id: builtins.str,
        user_name: builtins.str,
        root_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        volume_encryption_key: typing.Optional[builtins.str] = None,
        workspace_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.WorkspacePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bundle_id: The identifier of the bundle for the WorkSpace.
        :param directory_id: The identifier of the AWS Directory Service directory for the WorkSpace.
        :param user_name: The user name of the user for the WorkSpace. This user name must exist in the AWS Directory Service directory for the WorkSpace.
        :param root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param tags: The tags for the WorkSpace.
        :param user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param volume_encryption_key: The ARN of the symmetric AWS KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.
        :param workspace_properties: The WorkSpace properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecf9321ac6e165dfc96d72b093b8636e1ff9e82acf9cea2e5176beb79bb65839)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkspaceProps(
            bundle_id=bundle_id,
            directory_id=directory_id,
            user_name=user_name,
            root_volume_encryption_enabled=root_volume_encryption_enabled,
            tags=tags,
            user_volume_encryption_enabled=user_volume_encryption_enabled,
            volume_encryption_key=volume_encryption_key,
            workspace_properties=workspace_properties,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e772192f4dd8e60f99b92beca96b37f99aca30dac13f906848601f52405c8d90)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4902c0d49db4502ddf5bb0c1b99a8dd9ce3aa66f14904ef46eb1b040033e0f6f)
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
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> builtins.str:
        '''The identifier of the bundle for the WorkSpace.'''
        return typing.cast(builtins.str, jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2f2e671a0d784d1293a9f59800a4ee9327ac8c35d2975eb4bccf99d78c24ba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleId", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        '''The identifier of the AWS Directory Service directory for the WorkSpace.'''
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__098a48aaecf371ba14035ae50fde38957b608503f7c78dc0f9568806cd61b926)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The user name of the user for the WorkSpace.'''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225037370c6d4ae1d7c6fb794db70699fb16815233054c687f769b05c6298ddc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the data stored on the root volume is encrypted.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "rootVolumeEncryptionEnabled"))

    @root_volume_encryption_enabled.setter
    def root_volume_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb29c66862be75fab751682c7102c72c4846798afbc12b529f0ece9b38719128)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootVolumeEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the WorkSpace.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f2a501e8ab3d90f102a797f62bdece7b78195c5b29e714a25825ca056f061c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the data stored on the user volume is encrypted.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "userVolumeEncryptionEnabled"))

    @user_volume_encryption_enabled.setter
    def user_volume_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bd38103f5213efdd25dca3a2f0c8dcbf665bbcfb052ef6f4c929ce79e0719d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userVolumeEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="volumeEncryptionKey")
    def volume_encryption_key(self) -> typing.Optional[builtins.str]:
        '''The ARN of the symmetric AWS KMS key used to encrypt data stored on your WorkSpace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeEncryptionKey"))

    @volume_encryption_key.setter
    def volume_encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0670847357c5e2a262f5f7ce5cb07d9b48f5d29700739766ad22e91419e89b88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeEncryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceProperties")
    def workspace_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.WorkspacePropertiesProperty"]]:
        '''The WorkSpace properties.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.WorkspacePropertiesProperty"]], jsii.get(self, "workspaceProperties"))

    @workspace_properties.setter
    def workspace_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.WorkspacePropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbfa33f0e5fe13fa6e31e4fac282721ea7584fa1e07cea2b5dc3a6a41028a2ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceProperties", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspaces.CfnWorkspace.WorkspacePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compute_type_name": "computeTypeName",
            "root_volume_size_gib": "rootVolumeSizeGib",
            "running_mode": "runningMode",
            "running_mode_auto_stop_timeout_in_minutes": "runningModeAutoStopTimeoutInMinutes",
            "user_volume_size_gib": "userVolumeSizeGib",
        },
    )
    class WorkspacePropertiesProperty:
        def __init__(
            self,
            *,
            compute_type_name: typing.Optional[builtins.str] = None,
            root_volume_size_gib: typing.Optional[jsii.Number] = None,
            running_mode: typing.Optional[builtins.str] = None,
            running_mode_auto_stop_timeout_in_minutes: typing.Optional[jsii.Number] = None,
            user_volume_size_gib: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about a WorkSpace.

            :param compute_type_name: The compute type. For more information, see `Amazon WorkSpaces Bundles <https://docs.aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`_ .
            :param root_volume_size_gib: The size of the root volume. For important information about how to modify the size of the root and user volumes, see `Modify a WorkSpace <https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html>`_ .
            :param running_mode: The running mode. For more information, see `Manage the WorkSpace Running Mode <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`_ . .. epigraph:: The ``MANUAL`` value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see `Amazon WorkSpaces Core <https://docs.aws.amazon.com/workspaces/core/>`_ .
            :param running_mode_auto_stop_timeout_in_minutes: The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
            :param user_volume_size_gib: The size of the user storage. For important information about how to modify the size of the root and user volumes, see `Modify a WorkSpace <https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspaces as workspaces
                
                workspace_properties_property = workspaces.CfnWorkspace.WorkspacePropertiesProperty(
                    compute_type_name="computeTypeName",
                    root_volume_size_gib=123,
                    running_mode="runningMode",
                    running_mode_auto_stop_timeout_in_minutes=123,
                    user_volume_size_gib=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ba35df0c40a72c6300f0149e43d82fc399d7f07da77a68563d45ca0546db330)
                check_type(argname="argument compute_type_name", value=compute_type_name, expected_type=type_hints["compute_type_name"])
                check_type(argname="argument root_volume_size_gib", value=root_volume_size_gib, expected_type=type_hints["root_volume_size_gib"])
                check_type(argname="argument running_mode", value=running_mode, expected_type=type_hints["running_mode"])
                check_type(argname="argument running_mode_auto_stop_timeout_in_minutes", value=running_mode_auto_stop_timeout_in_minutes, expected_type=type_hints["running_mode_auto_stop_timeout_in_minutes"])
                check_type(argname="argument user_volume_size_gib", value=user_volume_size_gib, expected_type=type_hints["user_volume_size_gib"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compute_type_name is not None:
                self._values["compute_type_name"] = compute_type_name
            if root_volume_size_gib is not None:
                self._values["root_volume_size_gib"] = root_volume_size_gib
            if running_mode is not None:
                self._values["running_mode"] = running_mode
            if running_mode_auto_stop_timeout_in_minutes is not None:
                self._values["running_mode_auto_stop_timeout_in_minutes"] = running_mode_auto_stop_timeout_in_minutes
            if user_volume_size_gib is not None:
                self._values["user_volume_size_gib"] = user_volume_size_gib

        @builtins.property
        def compute_type_name(self) -> typing.Optional[builtins.str]:
            '''The compute type.

            For more information, see `Amazon WorkSpaces Bundles <https://docs.aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-computetypename
            '''
            result = self._values.get("compute_type_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def root_volume_size_gib(self) -> typing.Optional[jsii.Number]:
            '''The size of the root volume.

            For important information about how to modify the size of the root and user volumes, see `Modify a WorkSpace <https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-rootvolumesizegib
            '''
            result = self._values.get("root_volume_size_gib")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def running_mode(self) -> typing.Optional[builtins.str]:
            '''The running mode. For more information, see `Manage the WorkSpace Running Mode <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`_ .

            .. epigraph::

               The ``MANUAL`` value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see `Amazon WorkSpaces Core <https://docs.aws.amazon.com/workspaces/core/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmode
            '''
            result = self._values.get("running_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def running_mode_auto_stop_timeout_in_minutes(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The time after a user logs off when WorkSpaces are automatically stopped.

            Configured in 60-minute intervals.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmodeautostoptimeoutinminutes
            '''
            result = self._values.get("running_mode_auto_stop_timeout_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def user_volume_size_gib(self) -> typing.Optional[jsii.Number]:
            '''The size of the user storage.

            For important information about how to modify the size of the root and user volumes, see `Modify a WorkSpace <https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-uservolumesizegib
            '''
            result = self._values.get("user_volume_size_gib")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkspacePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspaces.CfnWorkspaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "bundle_id": "bundleId",
        "directory_id": "directoryId",
        "user_name": "userName",
        "root_volume_encryption_enabled": "rootVolumeEncryptionEnabled",
        "tags": "tags",
        "user_volume_encryption_enabled": "userVolumeEncryptionEnabled",
        "volume_encryption_key": "volumeEncryptionKey",
        "workspace_properties": "workspaceProperties",
    },
)
class CfnWorkspaceProps:
    def __init__(
        self,
        *,
        bundle_id: builtins.str,
        directory_id: builtins.str,
        user_name: builtins.str,
        root_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        volume_encryption_key: typing.Optional[builtins.str] = None,
        workspace_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.WorkspacePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkspace``.

        :param bundle_id: The identifier of the bundle for the WorkSpace.
        :param directory_id: The identifier of the AWS Directory Service directory for the WorkSpace.
        :param user_name: The user name of the user for the WorkSpace. This user name must exist in the AWS Directory Service directory for the WorkSpace.
        :param root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param tags: The tags for the WorkSpace.
        :param user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param volume_encryption_key: The ARN of the symmetric AWS KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.
        :param workspace_properties: The WorkSpace properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspaces as workspaces
            
            cfn_workspace_props = workspaces.CfnWorkspaceProps(
                bundle_id="bundleId",
                directory_id="directoryId",
                user_name="userName",
            
                # the properties below are optional
                root_volume_encryption_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_volume_encryption_enabled=False,
                volume_encryption_key="volumeEncryptionKey",
                workspace_properties=workspaces.CfnWorkspace.WorkspacePropertiesProperty(
                    compute_type_name="computeTypeName",
                    root_volume_size_gib=123,
                    running_mode="runningMode",
                    running_mode_auto_stop_timeout_in_minutes=123,
                    user_volume_size_gib=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a25f87093526ea01aa087ea6dc9cc539b9abec4e01cf4bf21ae13159b6e31d52)
            check_type(argname="argument bundle_id", value=bundle_id, expected_type=type_hints["bundle_id"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument root_volume_encryption_enabled", value=root_volume_encryption_enabled, expected_type=type_hints["root_volume_encryption_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_volume_encryption_enabled", value=user_volume_encryption_enabled, expected_type=type_hints["user_volume_encryption_enabled"])
            check_type(argname="argument volume_encryption_key", value=volume_encryption_key, expected_type=type_hints["volume_encryption_key"])
            check_type(argname="argument workspace_properties", value=workspace_properties, expected_type=type_hints["workspace_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bundle_id": bundle_id,
            "directory_id": directory_id,
            "user_name": user_name,
        }
        if root_volume_encryption_enabled is not None:
            self._values["root_volume_encryption_enabled"] = root_volume_encryption_enabled
        if tags is not None:
            self._values["tags"] = tags
        if user_volume_encryption_enabled is not None:
            self._values["user_volume_encryption_enabled"] = user_volume_encryption_enabled
        if volume_encryption_key is not None:
            self._values["volume_encryption_key"] = volume_encryption_key
        if workspace_properties is not None:
            self._values["workspace_properties"] = workspace_properties

    @builtins.property
    def bundle_id(self) -> builtins.str:
        '''The identifier of the bundle for the WorkSpace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-bundleid
        '''
        result = self._values.get("bundle_id")
        assert result is not None, "Required property 'bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''The identifier of the AWS Directory Service directory for the WorkSpace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-directoryid
        '''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The user name of the user for the WorkSpace.

        This user name must exist in the AWS Directory Service directory for the WorkSpace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_volume_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the data stored on the root volume is encrypted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-rootvolumeencryptionenabled
        '''
        result = self._values.get("root_volume_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the WorkSpace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_volume_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the data stored on the user volume is encrypted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-uservolumeencryptionenabled
        '''
        result = self._values.get("user_volume_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def volume_encryption_key(self) -> typing.Optional[builtins.str]:
        '''The ARN of the symmetric AWS KMS key used to encrypt data stored on your WorkSpace.

        Amazon WorkSpaces does not support asymmetric KMS keys.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-volumeencryptionkey
        '''
        result = self._values.get("volume_encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.WorkspacePropertiesProperty]]:
        '''The WorkSpace properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-workspaceproperties
        '''
        result = self._values.get("workspace_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.WorkspacePropertiesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnectionAlias",
    "CfnConnectionAliasProps",
    "CfnWorkspace",
    "CfnWorkspaceProps",
]

publication.publish()

def _typecheckingstub__3fd73d00432c1164a74beb35acf6162e3d82fa91d51a0edf8c896028b6e3c6d2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connection_string: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d07e3ef46b7d1868d493367bae11c00c38fa0bb35cfa4e162e97b1482bf156(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d590d73fb55367a8be64477837c062053aa020d8931e1f1983124013786434f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8b72c0a6880f896fe31f0555dd87dfdcce86c05579ff4a417ab736a03b4fda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf34741743106631ede324d61fdd5ed726b94e64d09574347d59201303db6f9(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__614a827f45558e3ee89a9937d774dc07580e2d2d88ccf9a78ea211acad9d7c19(
    *,
    associated_account_id: typing.Optional[builtins.str] = None,
    association_status: typing.Optional[builtins.str] = None,
    connection_identifier: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33d1c548638caf6c8699dd74d5bcc8d8df516e1a0738521496aee37402727de8(
    *,
    connection_string: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf9321ac6e165dfc96d72b093b8636e1ff9e82acf9cea2e5176beb79bb65839(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bundle_id: builtins.str,
    directory_id: builtins.str,
    user_name: builtins.str,
    root_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    volume_encryption_key: typing.Optional[builtins.str] = None,
    workspace_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.WorkspacePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e772192f4dd8e60f99b92beca96b37f99aca30dac13f906848601f52405c8d90(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4902c0d49db4502ddf5bb0c1b99a8dd9ce3aa66f14904ef46eb1b040033e0f6f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f2e671a0d784d1293a9f59800a4ee9327ac8c35d2975eb4bccf99d78c24ba3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__098a48aaecf371ba14035ae50fde38957b608503f7c78dc0f9568806cd61b926(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225037370c6d4ae1d7c6fb794db70699fb16815233054c687f769b05c6298ddc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb29c66862be75fab751682c7102c72c4846798afbc12b529f0ece9b38719128(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f2a501e8ab3d90f102a797f62bdece7b78195c5b29e714a25825ca056f061c4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd38103f5213efdd25dca3a2f0c8dcbf665bbcfb052ef6f4c929ce79e0719d6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0670847357c5e2a262f5f7ce5cb07d9b48f5d29700739766ad22e91419e89b88(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbfa33f0e5fe13fa6e31e4fac282721ea7584fa1e07cea2b5dc3a6a41028a2ad(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.WorkspacePropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ba35df0c40a72c6300f0149e43d82fc399d7f07da77a68563d45ca0546db330(
    *,
    compute_type_name: typing.Optional[builtins.str] = None,
    root_volume_size_gib: typing.Optional[jsii.Number] = None,
    running_mode: typing.Optional[builtins.str] = None,
    running_mode_auto_stop_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    user_volume_size_gib: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a25f87093526ea01aa087ea6dc9cc539b9abec4e01cf4bf21ae13159b6e31d52(
    *,
    bundle_id: builtins.str,
    directory_id: builtins.str,
    user_name: builtins.str,
    root_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    volume_encryption_key: typing.Optional[builtins.str] = None,
    workspace_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.WorkspacePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
