'''
# AWS IoT Greengrass Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_greengrass as greengrass
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Greengrass construct libraries](https://constructs.dev/search?q=greengrass)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Greengrass resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Greengrass.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Greengrass](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Greengrass.html).

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
class CfnConnectorDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnConnectorDefinition",
):
    '''The ``AWS::Greengrass::ConnectorDefinition`` resource represents a connector definition for AWS IoT Greengrass .

    Connector definitions are used to organize your connector definition versions.

    Connector definitions can reference multiple connector definition versions. All connector definition versions must be associated with a connector definition. Each connector definition version can contain one or more connectors.
    .. epigraph::

       When you create a connector definition, you can optionally include an initial connector definition version. To associate a connector definition version later, create an ```AWS::Greengrass::ConnectorDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html>`_ resource and specify the ID of this connector definition.

       After you create the connector definition version that contains the connectors you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # parameters: Any
        # tags: Any
        
        cfn_connector_definition = greengrass.CfnConnectorDefinition(self, "MyCfnConnectorDefinition",
            name="name",
        
            # the properties below are optional
            initial_version=greengrass.CfnConnectorDefinition.ConnectorDefinitionVersionProperty(
                connectors=[greengrass.CfnConnectorDefinition.ConnectorProperty(
                    connector_arn="connectorArn",
                    id="id",
        
                    # the properties below are optional
                    parameters=parameters
                )]
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorDefinition.ConnectorDefinitionVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the connector definition.
        :param initial_version: The connector definition version to include when the connector definition is created. A connector definition version contains a list of ```connector`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html>`_ property types. .. epigraph:: To associate a connector definition version after the connector definition is created, create an ```AWS::Greengrass::ConnectorDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html>`_ resource and specify the ID of this connector definition.
        :param tags: Application-specific metadata to attach to the connector definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481b9a854466614791f45d6769989966b8f812de4d4fa3e31d53b297fc3cf25a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorDefinitionProps(
            name=name, initial_version=initial_version, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24c07fb6ad50afe14bef1d7010d53ca0ed36ba7ee67a12442f8fefe27c993eb3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__274c71989e410af72c071839e2a648c2c533621f117a8c0e486c9527e7470195)
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
        '''The Amazon Resource Name (ARN) of the ``ConnectorDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/connectors/1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the ``ConnectorDefinition`` , such as ``1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersionArn")
    def attr_latest_version_arn(self) -> builtins.str:
        '''The ARN of the last ``ConnectorDefinitionVersion`` that was added to the ``ConnectorDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/connectors/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`` .

        :cloudformationAttribute: LatestVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the ``ConnectorDefinition`` , such as ``MyConnectorDefinition`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''The name of the connector definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab45f89ff0cfe141f0220b75cd71c3d899658dfb0c0d902360ceac2645761b8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="initialVersion")
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorDefinition.ConnectorDefinitionVersionProperty"]]:
        '''The connector definition version to include when the connector definition is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorDefinition.ConnectorDefinitionVersionProperty"]], jsii.get(self, "initialVersion"))

    @initial_version.setter
    def initial_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorDefinition.ConnectorDefinitionVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0415a38346fbe03d6f5624bc1964761ae159cabc533cd2810f1187fb94a9e76e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''Application-specific metadata to attach to the connector definition.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60332b2bd3d1f19c86feea95dba6bf261745105b22e69096e4be69004bdad03b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnConnectorDefinition.ConnectorDefinitionVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"connectors": "connectors"},
    )
    class ConnectorDefinitionVersionProperty:
        def __init__(
            self,
            *,
            connectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorDefinition.ConnectorProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A connector definition version contains a list of connectors.

            .. epigraph::

               After you create a connector definition version that contains the connectors you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

            In an AWS CloudFormation template, ``ConnectorDefinitionVersion`` is the property type of the ``InitialVersion`` property in the ```AWS::Greengrass::ConnectorDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html>`_ resource.

            :param connectors: The connectors in this version. Only one instance of a given connector can be added to a connector definition version at a time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # parameters: Any
                
                connector_definition_version_property = greengrass.CfnConnectorDefinition.ConnectorDefinitionVersionProperty(
                    connectors=[greengrass.CfnConnectorDefinition.ConnectorProperty(
                        connector_arn="connectorArn",
                        id="id",
                
                        # the properties below are optional
                        parameters=parameters
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0ebd178e9a062570c1b341d7167254254483a31aa5611c9784ea999dbf17f21)
                check_type(argname="argument connectors", value=connectors, expected_type=type_hints["connectors"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connectors": connectors,
            }

        @builtins.property
        def connectors(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnectorDefinition.ConnectorProperty"]]]:
            '''The connectors in this version.

            Only one instance of a given connector can be added to a connector definition version at a time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html#cfn-greengrass-connectordefinition-connectordefinitionversion-connectors
            '''
            result = self._values.get("connectors")
            assert result is not None, "Required property 'connectors' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnectorDefinition.ConnectorProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorDefinitionVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnConnectorDefinition.ConnectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_arn": "connectorArn",
            "id": "id",
            "parameters": "parameters",
        },
    )
    class ConnectorProperty:
        def __init__(
            self,
            *,
            connector_arn: builtins.str,
            id: builtins.str,
            parameters: typing.Any = None,
        ) -> None:
            '''Connectors are modules that provide built-in integration with local infrastructure, device protocols, AWS , and other cloud services.

            For more information, see `Integrate with Services and Protocols Using Greengrass Connectors <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Connectors`` property of the ```ConnectorDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html>`_ property type contains a list of ``Connector`` property types.

            :param connector_arn: The Amazon Resource Name (ARN) of the connector. For more information about connectors provided by AWS , see `Greengrass Connectors Provided by AWS <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-list.html>`_ .
            :param id: A descriptive or arbitrary ID for the connector. This value must be unique within the connector definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param parameters: The parameters or configuration used by the connector. For more information about connectors provided by AWS , see `Greengrass Connectors Provided by AWS <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-list.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # parameters: Any
                
                connector_property = greengrass.CfnConnectorDefinition.ConnectorProperty(
                    connector_arn="connectorArn",
                    id="id",
                
                    # the properties below are optional
                    parameters=parameters
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9296d577ecfbbed3bc2c2debdad72ad7c40138384002b64be6231a4a65308aec)
                check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connector_arn": connector_arn,
                "id": id,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def connector_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the connector.

            For more information about connectors provided by AWS , see `Greengrass Connectors Provided by AWS <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-list.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-connectorarn
            '''
            result = self._values.get("connector_arn")
            assert result is not None, "Required property 'connector_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the connector.

            This value must be unique within the connector definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''The parameters or configuration used by the connector.

            For more information about connectors provided by AWS , see `Greengrass Connectors Provided by AWS <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-list.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnConnectorDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "initial_version": "initialVersion", "tags": "tags"},
)
class CfnConnectorDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorDefinition.ConnectorDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnConnectorDefinition``.

        :param name: The name of the connector definition.
        :param initial_version: The connector definition version to include when the connector definition is created. A connector definition version contains a list of ```connector`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html>`_ property types. .. epigraph:: To associate a connector definition version after the connector definition is created, create an ```AWS::Greengrass::ConnectorDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html>`_ resource and specify the ID of this connector definition.
        :param tags: Application-specific metadata to attach to the connector definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # parameters: Any
            # tags: Any
            
            cfn_connector_definition_props = greengrass.CfnConnectorDefinitionProps(
                name="name",
            
                # the properties below are optional
                initial_version=greengrass.CfnConnectorDefinition.ConnectorDefinitionVersionProperty(
                    connectors=[greengrass.CfnConnectorDefinition.ConnectorProperty(
                        connector_arn="connectorArn",
                        id="id",
            
                        # the properties below are optional
                        parameters=parameters
                    )]
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c11896c87152b58a2cacd3ad90176b83e130f066bfcc0c1caf54e71e272e5c6c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument initial_version", value=initial_version, expected_type=type_hints["initial_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if initial_version is not None:
            self._values["initial_version"] = initial_version
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the connector definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectorDefinition.ConnectorDefinitionVersionProperty]]:
        '''The connector definition version to include when the connector definition is created.

        A connector definition version contains a list of ```connector`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html>`_ property types.
        .. epigraph::

           To associate a connector definition version after the connector definition is created, create an ```AWS::Greengrass::ConnectorDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html>`_ resource and specify the ID of this connector definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-initialversion
        '''
        result = self._values.get("initial_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectorDefinition.ConnectorDefinitionVersionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Application-specific metadata to attach to the connector definition.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConnectorDefinitionVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnConnectorDefinitionVersion",
):
    '''The ``AWS::Greengrass::ConnectorDefinitionVersion`` resource represents a connector definition version for AWS IoT Greengrass .

    A connector definition version contains a list of connectors.
    .. epigraph::

       To create a connector definition version, you must specify the ID of the connector definition that you want to associate with the version. For information about creating a connector definition, see ```AWS::Greengrass::ConnectorDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html>`_ .

       After you create a connector definition version that contains the connectors you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # parameters: Any
        
        cfn_connector_definition_version = greengrass.CfnConnectorDefinitionVersion(self, "MyCfnConnectorDefinitionVersion",
            connector_definition_id="connectorDefinitionId",
            connectors=[greengrass.CfnConnectorDefinitionVersion.ConnectorProperty(
                connector_arn="connectorArn",
                id="id",
        
                # the properties below are optional
                parameters=parameters
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        connector_definition_id: builtins.str,
        connectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorDefinitionVersion.ConnectorProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connector_definition_id: The ID of the connector definition associated with this version. This value is a GUID.
        :param connectors: The connectors in this version. Only one instance of a given connector can be added to the connector definition version at a time.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b0440a60203f7d65611b69dca729e027a591c6aa92f00dc0aebb40960143af)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorDefinitionVersionProps(
            connector_definition_id=connector_definition_id, connectors=connectors
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28930916b9351f935867712c00b802adf7b173a69fafdb3c311d8cd529a223ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bda14e12f8fd37f15240b23bb63562be66f84404eec1690445f8ff0f960d0321)
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
    @jsii.member(jsii_name="connectorDefinitionId")
    def connector_definition_id(self) -> builtins.str:
        '''The ID of the connector definition associated with this version.'''
        return typing.cast(builtins.str, jsii.get(self, "connectorDefinitionId"))

    @connector_definition_id.setter
    def connector_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46572beae401fe5e838cb0b02ec437b067f98ac0ae5835d7ef8ce870c4ac7d90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="connectors")
    def connectors(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnectorDefinitionVersion.ConnectorProperty"]]]:
        '''The connectors in this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnectorDefinitionVersion.ConnectorProperty"]]], jsii.get(self, "connectors"))

    @connectors.setter
    def connectors(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnectorDefinitionVersion.ConnectorProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ed3abea511a407254df28d178fbfb71f43dee9315c0aeca3095f062663236ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectors", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnConnectorDefinitionVersion.ConnectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_arn": "connectorArn",
            "id": "id",
            "parameters": "parameters",
        },
    )
    class ConnectorProperty:
        def __init__(
            self,
            *,
            connector_arn: builtins.str,
            id: builtins.str,
            parameters: typing.Any = None,
        ) -> None:
            '''Connectors are modules that provide built-in integration with local infrastructure, device protocols, AWS , and other cloud services.

            For more information, see `Integrate with Services and Protocols Using Greengrass Connectors <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Connectors`` property of the ```AWS::Greengrass::ConnectorDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html>`_ resource contains a list of ``Connector`` property types.

            :param connector_arn: The Amazon Resource Name (ARN) of the connector. For more information about connectors provided by AWS , see `Greengrass Connectors Provided by AWS <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-list.html>`_ .
            :param id: A descriptive or arbitrary ID for the connector. This value must be unique within the connector definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param parameters: The parameters or configuration that the connector uses. For more information about connectors provided by AWS , see `Greengrass Connectors Provided by AWS <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-list.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # parameters: Any
                
                connector_property = greengrass.CfnConnectorDefinitionVersion.ConnectorProperty(
                    connector_arn="connectorArn",
                    id="id",
                
                    # the properties below are optional
                    parameters=parameters
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d59c31c39abe32b4f18b9663d07cf39015d1cce8e87ebaa475937de0f283249d)
                check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connector_arn": connector_arn,
                "id": id,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def connector_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the connector.

            For more information about connectors provided by AWS , see `Greengrass Connectors Provided by AWS <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-list.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-connectorarn
            '''
            result = self._values.get("connector_arn")
            assert result is not None, "Required property 'connector_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the connector.

            This value must be unique within the connector definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''The parameters or configuration that the connector uses.

            For more information about connectors provided by AWS , see `Greengrass Connectors Provided by AWS <https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-list.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnConnectorDefinitionVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "connector_definition_id": "connectorDefinitionId",
        "connectors": "connectors",
    },
)
class CfnConnectorDefinitionVersionProps:
    def __init__(
        self,
        *,
        connector_definition_id: builtins.str,
        connectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorDefinitionVersion.ConnectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnConnectorDefinitionVersion``.

        :param connector_definition_id: The ID of the connector definition associated with this version. This value is a GUID.
        :param connectors: The connectors in this version. Only one instance of a given connector can be added to the connector definition version at a time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # parameters: Any
            
            cfn_connector_definition_version_props = greengrass.CfnConnectorDefinitionVersionProps(
                connector_definition_id="connectorDefinitionId",
                connectors=[greengrass.CfnConnectorDefinitionVersion.ConnectorProperty(
                    connector_arn="connectorArn",
                    id="id",
            
                    # the properties below are optional
                    parameters=parameters
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08c795265270b52b4f10228be7f4015f471c0c0039915e2b229a19aea56195a3)
            check_type(argname="argument connector_definition_id", value=connector_definition_id, expected_type=type_hints["connector_definition_id"])
            check_type(argname="argument connectors", value=connectors, expected_type=type_hints["connectors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_definition_id": connector_definition_id,
            "connectors": connectors,
        }

    @builtins.property
    def connector_definition_id(self) -> builtins.str:
        '''The ID of the connector definition associated with this version.

        This value is a GUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html#cfn-greengrass-connectordefinitionversion-connectordefinitionid
        '''
        result = self._values.get("connector_definition_id")
        assert result is not None, "Required property 'connector_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connectors(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConnectorDefinitionVersion.ConnectorProperty]]]:
        '''The connectors in this version.

        Only one instance of a given connector can be added to the connector definition version at a time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html#cfn-greengrass-connectordefinitionversion-connectors
        '''
        result = self._values.get("connectors")
        assert result is not None, "Required property 'connectors' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConnectorDefinitionVersion.ConnectorProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorDefinitionVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCoreDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnCoreDefinition",
):
    '''The ``AWS::Greengrass::CoreDefinition`` resource represents a core definition for AWS IoT Greengrass .

    Core definitions are used to organize your core definition versions.

    Core definitions can reference multiple core definition versions. All core definition versions must be associated with a core definition. Each core definition version can contain one Greengrass core.
    .. epigraph::

       When you create a core definition, you can optionally include an initial core definition version. To associate a core definition version later, create an ```AWS::Greengrass::CoreDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html>`_ resource and specify the ID of this core definition.

       After you create the core definition version that contains the core you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # tags: Any
        
        cfn_core_definition = greengrass.CfnCoreDefinition(self, "MyCfnCoreDefinition",
            name="name",
        
            # the properties below are optional
            initial_version=greengrass.CfnCoreDefinition.CoreDefinitionVersionProperty(
                cores=[greengrass.CfnCoreDefinition.CoreProperty(
                    certificate_arn="certificateArn",
                    id="id",
                    thing_arn="thingArn",
        
                    # the properties below are optional
                    sync_shadow=False
                )]
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCoreDefinition.CoreDefinitionVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the core definition.
        :param initial_version: The core definition version to include when the core definition is created. Currently, a core definition version can contain only one ```core`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html>`_ . .. epigraph:: To associate a core definition version after the core definition is created, create an ```AWS::Greengrass::CoreDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html>`_ resource and specify the ID of this core definition.
        :param tags: Application-specific metadata to attach to the core definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7fe5635b210e6632e07b82d21d8907b6d36d805b6d4fb2198f0433417d780a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCoreDefinitionProps(
            name=name, initial_version=initial_version, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64368dbb58b3df35d74d10a3113a88fb2dc06fc0237665e15968f378a8fbbd09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b38774760bbfa1d8286cc0bcbc098a0bc3dccc52ef7c7d0390f236a771e6087)
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
        '''The Amazon Resource Name (ARN) of the ``CoreDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/cores/1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the ``CoreDefinition`` , such as ``1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersionArn")
    def attr_latest_version_arn(self) -> builtins.str:
        '''The ARN of the last ``CoreDefinitionVersion`` that was added to the ``CoreDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/cores/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`` .

        :cloudformationAttribute: LatestVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the ``CoreDefinition`` , such as ``MyCoreDefinition`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''The name of the core definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac51622030b12c5c1ad466a72f36fc6ae109a83246daf2e9b37011f5db34b4b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="initialVersion")
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCoreDefinition.CoreDefinitionVersionProperty"]]:
        '''The core definition version to include when the core definition is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCoreDefinition.CoreDefinitionVersionProperty"]], jsii.get(self, "initialVersion"))

    @initial_version.setter
    def initial_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCoreDefinition.CoreDefinitionVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92abb907cfcf9216f792b317f8eb26a0b6c421a027b2e96eefee9e1fd17d6fc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''Application-specific metadata to attach to the core definition.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99697b8dad691477ff836e154bb3c9f516a73f2882f23a90d55ddc3f167aadd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnCoreDefinition.CoreDefinitionVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"cores": "cores"},
    )
    class CoreDefinitionVersionProperty:
        def __init__(
            self,
            *,
            cores: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCoreDefinition.CoreProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A core definition version contains a Greengrass `core <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html>`_ .

            .. epigraph::

               After you create a core definition version that contains the core you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

            In an AWS CloudFormation template, ``CoreDefinitionVersion`` is the property type of the ``InitialVersion`` property in the ```AWS::Greengrass::CoreDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html>`_ resource.

            :param cores: The Greengrass core in this version. Currently, the ``Cores`` property for a core definition version can contain only one core.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                core_definition_version_property = greengrass.CfnCoreDefinition.CoreDefinitionVersionProperty(
                    cores=[greengrass.CfnCoreDefinition.CoreProperty(
                        certificate_arn="certificateArn",
                        id="id",
                        thing_arn="thingArn",
                
                        # the properties below are optional
                        sync_shadow=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4ef4f67c3c3830d5b5644db7ec3e809f18d3cab655c6a7fd98232bccd93382e3)
                check_type(argname="argument cores", value=cores, expected_type=type_hints["cores"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cores": cores,
            }

        @builtins.property
        def cores(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCoreDefinition.CoreProperty"]]]:
            '''The Greengrass core in this version.

            Currently, the ``Cores`` property for a core definition version can contain only one core.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html#cfn-greengrass-coredefinition-coredefinitionversion-cores
            '''
            result = self._values.get("cores")
            assert result is not None, "Required property 'cores' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCoreDefinition.CoreProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoreDefinitionVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnCoreDefinition.CoreProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "id": "id",
            "thing_arn": "thingArn",
            "sync_shadow": "syncShadow",
        },
    )
    class CoreProperty:
        def __init__(
            self,
            *,
            certificate_arn: builtins.str,
            id: builtins.str,
            thing_arn: builtins.str,
            sync_shadow: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A core is an AWS IoT device that runs the AWS IoT Greengrass core software and manages local processes for a Greengrass group.

            For more information, see `What Is AWS IoT Greengrass ? <https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Cores`` property of the ```CoreDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html>`_ property type contains a list of ``Core`` property types. Currently, the list can contain only one core.

            :param certificate_arn: The Amazon Resource Name (ARN) of the device certificate for the core. This X.509 certificate is used to authenticate the core with AWS IoT and AWS IoT Greengrass services.
            :param id: A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param thing_arn: The ARN of the core, which is an AWS IoT device (thing).
            :param sync_shadow: Indicates whether the core's local shadow is synced with the cloud automatically. The default is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                core_property = greengrass.CfnCoreDefinition.CoreProperty(
                    certificate_arn="certificateArn",
                    id="id",
                    thing_arn="thingArn",
                
                    # the properties below are optional
                    sync_shadow=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16d7e03cdaed925e2b5ec8c65e84a5b6cf10c5209e1d1de097ab201c492621ce)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
                check_type(argname="argument sync_shadow", value=sync_shadow, expected_type=type_hints["sync_shadow"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_arn": certificate_arn,
                "id": id,
                "thing_arn": thing_arn,
            }
            if sync_shadow is not None:
                self._values["sync_shadow"] = sync_shadow

        @builtins.property
        def certificate_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the device certificate for the core.

            This X.509 certificate is used to authenticate the core with AWS IoT and AWS IoT Greengrass services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-certificatearn
            '''
            result = self._values.get("certificate_arn")
            assert result is not None, "Required property 'certificate_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the core.

            This value must be unique within the core definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def thing_arn(self) -> builtins.str:
            '''The ARN of the core, which is an AWS IoT device (thing).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-thingarn
            '''
            result = self._values.get("thing_arn")
            assert result is not None, "Required property 'thing_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sync_shadow(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the core's local shadow is synced with the cloud automatically.

            The default is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-syncshadow
            '''
            result = self._values.get("sync_shadow")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoreProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnCoreDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "initial_version": "initialVersion", "tags": "tags"},
)
class CfnCoreDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCoreDefinition.CoreDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnCoreDefinition``.

        :param name: The name of the core definition.
        :param initial_version: The core definition version to include when the core definition is created. Currently, a core definition version can contain only one ```core`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html>`_ . .. epigraph:: To associate a core definition version after the core definition is created, create an ```AWS::Greengrass::CoreDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html>`_ resource and specify the ID of this core definition.
        :param tags: Application-specific metadata to attach to the core definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # tags: Any
            
            cfn_core_definition_props = greengrass.CfnCoreDefinitionProps(
                name="name",
            
                # the properties below are optional
                initial_version=greengrass.CfnCoreDefinition.CoreDefinitionVersionProperty(
                    cores=[greengrass.CfnCoreDefinition.CoreProperty(
                        certificate_arn="certificateArn",
                        id="id",
                        thing_arn="thingArn",
            
                        # the properties below are optional
                        sync_shadow=False
                    )]
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d8127b3c34b3abe01c8efbf62b499796f709f95bf91348e64a7ab4a0d7ac3c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument initial_version", value=initial_version, expected_type=type_hints["initial_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if initial_version is not None:
            self._values["initial_version"] = initial_version
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the core definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCoreDefinition.CoreDefinitionVersionProperty]]:
        '''The core definition version to include when the core definition is created.

        Currently, a core definition version can contain only one ```core`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html>`_ .
        .. epigraph::

           To associate a core definition version after the core definition is created, create an ```AWS::Greengrass::CoreDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html>`_ resource and specify the ID of this core definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-initialversion
        '''
        result = self._values.get("initial_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCoreDefinition.CoreDefinitionVersionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Application-specific metadata to attach to the core definition.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCoreDefinitionVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnCoreDefinitionVersion",
):
    '''The ``AWS::Greengrass::CoreDefinitionVersion`` resource represents a core definition version for AWS IoT Greengrass .

    A core definition version contains a Greengrass core.
    .. epigraph::

       To create a core definition version, you must specify the ID of the core definition that you want to associate with the version. For information about creating a core definition, see ```AWS::Greengrass::CoreDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html>`_ .

       After you create a core definition version that contains the core you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        cfn_core_definition_version = greengrass.CfnCoreDefinitionVersion(self, "MyCfnCoreDefinitionVersion",
            core_definition_id="coreDefinitionId",
            cores=[greengrass.CfnCoreDefinitionVersion.CoreProperty(
                certificate_arn="certificateArn",
                id="id",
                thing_arn="thingArn",
        
                # the properties below are optional
                sync_shadow=False
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        core_definition_id: builtins.str,
        cores: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCoreDefinitionVersion.CoreProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param core_definition_id: The ID of the core definition associated with this version. This value is a GUID.
        :param cores: The Greengrass core in this version. Currently, the ``Cores`` property for a core definition version can contain only one core.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98b8071f110db36c2b93c49d75516709035bb93997aae3c35adc25c4ab4d53c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCoreDefinitionVersionProps(
            core_definition_id=core_definition_id, cores=cores
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b4e0682ef4a26ccff2d2d377b87519933191b35ee2f3c927013cb65d537b304)
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
            type_hints = typing.get_type_hints(_typecheckingstub__12d9b9142f952fb03ff2494686a42ca4db8c5b291082063611639ee867890701)
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
    @jsii.member(jsii_name="coreDefinitionId")
    def core_definition_id(self) -> builtins.str:
        '''The ID of the core definition associated with this version.'''
        return typing.cast(builtins.str, jsii.get(self, "coreDefinitionId"))

    @core_definition_id.setter
    def core_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce705d0cc1809364da37b409e24bfddfab55386d0858b4c4146d9a22a2a2f40a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="cores")
    def cores(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCoreDefinitionVersion.CoreProperty"]]]:
        '''The Greengrass core in this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCoreDefinitionVersion.CoreProperty"]]], jsii.get(self, "cores"))

    @cores.setter
    def cores(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCoreDefinitionVersion.CoreProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1bffbbd7f9c7ce8f8528729042b02d09f335ab5562e19bf5da873a4a6ae6b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cores", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnCoreDefinitionVersion.CoreProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "id": "id",
            "thing_arn": "thingArn",
            "sync_shadow": "syncShadow",
        },
    )
    class CoreProperty:
        def __init__(
            self,
            *,
            certificate_arn: builtins.str,
            id: builtins.str,
            thing_arn: builtins.str,
            sync_shadow: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A core is an AWS IoT device that runs the AWS IoT Greengrass core software and manages local processes for a Greengrass group.

            For more information, see `What Is AWS IoT Greengrass ? <https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Cores`` property of the ```AWS::Greengrass::CoreDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html>`_ resource contains a list of ``Core`` property types. Currently, the list can contain only one core.

            :param certificate_arn: The ARN of the device certificate for the core. This X.509 certificate is used to authenticate the core with AWS IoT and AWS IoT Greengrass services.
            :param id: A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param thing_arn: The Amazon Resource Name (ARN) of the core, which is an AWS IoT device (thing).
            :param sync_shadow: Indicates whether the core's local shadow is synced with the cloud automatically. The default is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                core_property = greengrass.CfnCoreDefinitionVersion.CoreProperty(
                    certificate_arn="certificateArn",
                    id="id",
                    thing_arn="thingArn",
                
                    # the properties below are optional
                    sync_shadow=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07e3ed0ad844b4ecbd124f2fc0f6fcb8c8ca64bd7f1b2ebe17ecf825baa15ea8)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
                check_type(argname="argument sync_shadow", value=sync_shadow, expected_type=type_hints["sync_shadow"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_arn": certificate_arn,
                "id": id,
                "thing_arn": thing_arn,
            }
            if sync_shadow is not None:
                self._values["sync_shadow"] = sync_shadow

        @builtins.property
        def certificate_arn(self) -> builtins.str:
            '''The ARN of the device certificate for the core.

            This X.509 certificate is used to authenticate the core with AWS IoT and AWS IoT Greengrass services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-certificatearn
            '''
            result = self._values.get("certificate_arn")
            assert result is not None, "Required property 'certificate_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the core.

            This value must be unique within the core definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def thing_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the core, which is an AWS IoT device (thing).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-thingarn
            '''
            result = self._values.get("thing_arn")
            assert result is not None, "Required property 'thing_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sync_shadow(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the core's local shadow is synced with the cloud automatically.

            The default is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-syncshadow
            '''
            result = self._values.get("sync_shadow")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoreProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnCoreDefinitionVersionProps",
    jsii_struct_bases=[],
    name_mapping={"core_definition_id": "coreDefinitionId", "cores": "cores"},
)
class CfnCoreDefinitionVersionProps:
    def __init__(
        self,
        *,
        core_definition_id: builtins.str,
        cores: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCoreDefinitionVersion.CoreProperty, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnCoreDefinitionVersion``.

        :param core_definition_id: The ID of the core definition associated with this version. This value is a GUID.
        :param cores: The Greengrass core in this version. Currently, the ``Cores`` property for a core definition version can contain only one core.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            cfn_core_definition_version_props = greengrass.CfnCoreDefinitionVersionProps(
                core_definition_id="coreDefinitionId",
                cores=[greengrass.CfnCoreDefinitionVersion.CoreProperty(
                    certificate_arn="certificateArn",
                    id="id",
                    thing_arn="thingArn",
            
                    # the properties below are optional
                    sync_shadow=False
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5ee60cab94ef477682167b25261f01a298b6e5e0bece31e1df9370f3a2f790f)
            check_type(argname="argument core_definition_id", value=core_definition_id, expected_type=type_hints["core_definition_id"])
            check_type(argname="argument cores", value=cores, expected_type=type_hints["cores"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_definition_id": core_definition_id,
            "cores": cores,
        }

    @builtins.property
    def core_definition_id(self) -> builtins.str:
        '''The ID of the core definition associated with this version.

        This value is a GUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html#cfn-greengrass-coredefinitionversion-coredefinitionid
        '''
        result = self._values.get("core_definition_id")
        assert result is not None, "Required property 'core_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cores(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCoreDefinitionVersion.CoreProperty]]]:
        '''The Greengrass core in this version.

        Currently, the ``Cores`` property for a core definition version can contain only one core.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html#cfn-greengrass-coredefinitionversion-cores
        '''
        result = self._values.get("cores")
        assert result is not None, "Required property 'cores' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCoreDefinitionVersion.CoreProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreDefinitionVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDeviceDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnDeviceDefinition",
):
    '''The ``AWS::Greengrass::DeviceDefinition`` resource represents a device definition for AWS IoT Greengrass .

    Device definitions are used to organize your device definition versions.

    Device definitions can reference multiple device definition versions. All device definition versions must be associated with a device definition. Each device definition version can contain one or more devices.
    .. epigraph::

       When you create a device definition, you can optionally include an initial device definition version. To associate a device definition version later, create an ```AWS::Greengrass::DeviceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html>`_ resource and specify the ID of this device definition.

       After you create the device definition version that contains the devices you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # tags: Any
        
        cfn_device_definition = greengrass.CfnDeviceDefinition(self, "MyCfnDeviceDefinition",
            name="name",
        
            # the properties below are optional
            initial_version=greengrass.CfnDeviceDefinition.DeviceDefinitionVersionProperty(
                devices=[greengrass.CfnDeviceDefinition.DeviceProperty(
                    certificate_arn="certificateArn",
                    id="id",
                    thing_arn="thingArn",
        
                    # the properties below are optional
                    sync_shadow=False
                )]
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeviceDefinition.DeviceDefinitionVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the device definition.
        :param initial_version: The device definition version to include when the device definition is created. A device definition version contains a list of ```device`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html>`_ property types. .. epigraph:: To associate a device definition version after the device definition is created, create an ```AWS::Greengrass::DeviceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html>`_ resource and specify the ID of this device definition.
        :param tags: Application-specific metadata to attach to the device definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6388724d13149e0aad9e17e0abeb2962bcb4c5f435c6c0744dc4914379c75ae1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeviceDefinitionProps(
            name=name, initial_version=initial_version, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42b7b2748a017da66012466c961f889765dd501d6bce1063c38a88cf58c3f181)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5718b5621957658ebf68cf3e23503ef4a017494ec185b843a1c3fd424fb6f807)
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
        '''The Amazon Resource Name (ARN) of the ``DeviceDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/devices/1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the ``DeviceDefinition`` , such as ``1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersionArn")
    def attr_latest_version_arn(self) -> builtins.str:
        '''The ARN of the last ``DeviceDefinitionVersion`` that was added to the ``DeviceDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/devices/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`` .

        :cloudformationAttribute: LatestVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the device definition.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''The name of the device definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2194bc46e61deb1c1fcc4553ae866524155d250a4d6110495f31209d88865d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="initialVersion")
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeviceDefinition.DeviceDefinitionVersionProperty"]]:
        '''The device definition version to include when the device definition is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeviceDefinition.DeviceDefinitionVersionProperty"]], jsii.get(self, "initialVersion"))

    @initial_version.setter
    def initial_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeviceDefinition.DeviceDefinitionVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860ed955c6c53de09524817b41d262c302d0a99f94c5e829c77f1df83b034260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''Application-specific metadata to attach to the device definition.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa56b64210e79fff38ab545ae87d1988b94100fdbaa646f7ebeda88559aeeacb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnDeviceDefinition.DeviceDefinitionVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"devices": "devices"},
    )
    class DeviceDefinitionVersionProperty:
        def __init__(
            self,
            *,
            devices: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeviceDefinition.DeviceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A device definition version contains a list of `devices <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html>`_ .

            .. epigraph::

               After you create a device definition version that contains the devices you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

            In an AWS CloudFormation template, ``DeviceDefinitionVersion`` is the property type of the ``InitialVersion`` property in the ```AWS::Greengrass::DeviceDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html>`_ resource.

            :param devices: The devices in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                device_definition_version_property = greengrass.CfnDeviceDefinition.DeviceDefinitionVersionProperty(
                    devices=[greengrass.CfnDeviceDefinition.DeviceProperty(
                        certificate_arn="certificateArn",
                        id="id",
                        thing_arn="thingArn",
                
                        # the properties below are optional
                        sync_shadow=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0c5ec14762edf351c870b2f17efb8d815ee293da253da248851bce6b21751ce)
                check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "devices": devices,
            }

        @builtins.property
        def devices(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeviceDefinition.DeviceProperty"]]]:
            '''The devices in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html#cfn-greengrass-devicedefinition-devicedefinitionversion-devices
            '''
            result = self._values.get("devices")
            assert result is not None, "Required property 'devices' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeviceDefinition.DeviceProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceDefinitionVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnDeviceDefinition.DeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "id": "id",
            "thing_arn": "thingArn",
            "sync_shadow": "syncShadow",
        },
    )
    class DeviceProperty:
        def __init__(
            self,
            *,
            certificate_arn: builtins.str,
            id: builtins.str,
            thing_arn: builtins.str,
            sync_shadow: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A device is an AWS IoT device (thing) that's added to a Greengrass group.

            Greengrass devices can communicate with the Greengrass core in the same group. For more information, see `What Is AWS IoT Greengrass ? <https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Devices`` property of the ```DeviceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html>`_ property type contains a list of ``Device`` property types.

            :param certificate_arn: The Amazon Resource Name (ARN) of the device certificate for the device. This X.509 certificate is used to authenticate the device with AWS IoT and AWS IoT Greengrass services.
            :param id: A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param thing_arn: The ARN of the device, which is an AWS IoT device (thing).
            :param sync_shadow: Indicates whether the device's local shadow is synced with the cloud automatically.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                device_property = greengrass.CfnDeviceDefinition.DeviceProperty(
                    certificate_arn="certificateArn",
                    id="id",
                    thing_arn="thingArn",
                
                    # the properties below are optional
                    sync_shadow=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__812e639d6663b05c08a6e0a7e6aea0c4d9cb91c3144a1113dcbf3d7933594fa4)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
                check_type(argname="argument sync_shadow", value=sync_shadow, expected_type=type_hints["sync_shadow"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_arn": certificate_arn,
                "id": id,
                "thing_arn": thing_arn,
            }
            if sync_shadow is not None:
                self._values["sync_shadow"] = sync_shadow

        @builtins.property
        def certificate_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the device certificate for the device.

            This X.509 certificate is used to authenticate the device with AWS IoT and AWS IoT Greengrass services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-certificatearn
            '''
            result = self._values.get("certificate_arn")
            assert result is not None, "Required property 'certificate_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the device.

            This value must be unique within the device definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def thing_arn(self) -> builtins.str:
            '''The ARN of the device, which is an AWS IoT device (thing).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-thingarn
            '''
            result = self._values.get("thing_arn")
            assert result is not None, "Required property 'thing_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sync_shadow(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the device's local shadow is synced with the cloud automatically.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-syncshadow
            '''
            result = self._values.get("sync_shadow")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnDeviceDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "initial_version": "initialVersion", "tags": "tags"},
)
class CfnDeviceDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceDefinition.DeviceDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnDeviceDefinition``.

        :param name: The name of the device definition.
        :param initial_version: The device definition version to include when the device definition is created. A device definition version contains a list of ```device`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html>`_ property types. .. epigraph:: To associate a device definition version after the device definition is created, create an ```AWS::Greengrass::DeviceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html>`_ resource and specify the ID of this device definition.
        :param tags: Application-specific metadata to attach to the device definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # tags: Any
            
            cfn_device_definition_props = greengrass.CfnDeviceDefinitionProps(
                name="name",
            
                # the properties below are optional
                initial_version=greengrass.CfnDeviceDefinition.DeviceDefinitionVersionProperty(
                    devices=[greengrass.CfnDeviceDefinition.DeviceProperty(
                        certificate_arn="certificateArn",
                        id="id",
                        thing_arn="thingArn",
            
                        # the properties below are optional
                        sync_shadow=False
                    )]
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7175e6a25a231dd04ec7fc7a8ba5222ad239e84c2555359e9e1779ee7dab007c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument initial_version", value=initial_version, expected_type=type_hints["initial_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if initial_version is not None:
            self._values["initial_version"] = initial_version
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the device definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeviceDefinition.DeviceDefinitionVersionProperty]]:
        '''The device definition version to include when the device definition is created.

        A device definition version contains a list of ```device`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html>`_ property types.
        .. epigraph::

           To associate a device definition version after the device definition is created, create an ```AWS::Greengrass::DeviceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html>`_ resource and specify the ID of this device definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-initialversion
        '''
        result = self._values.get("initial_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeviceDefinition.DeviceDefinitionVersionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Application-specific metadata to attach to the device definition.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDeviceDefinitionVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnDeviceDefinitionVersion",
):
    '''The ``AWS::Greengrass::DeviceDefinitionVersion`` resource represents a device definition version for AWS IoT Greengrass .

    A device definition version contains a list of devices.
    .. epigraph::

       To create a device definition version, you must specify the ID of the device definition that you want to associate with the version. For information about creating a device definition, see ```AWS::Greengrass::DeviceDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html>`_ .

       After you create a device definition version that contains the devices you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        cfn_device_definition_version = greengrass.CfnDeviceDefinitionVersion(self, "MyCfnDeviceDefinitionVersion",
            device_definition_id="deviceDefinitionId",
            devices=[greengrass.CfnDeviceDefinitionVersion.DeviceProperty(
                certificate_arn="certificateArn",
                id="id",
                thing_arn="thingArn",
        
                # the properties below are optional
                sync_shadow=False
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        device_definition_id: builtins.str,
        devices: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeviceDefinitionVersion.DeviceProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param device_definition_id: The ID of the device definition associated with this version. This value is a GUID.
        :param devices: The devices in this version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64493ebfeeb96fc14eb8e8054338af97e554d939f196f64d5d512c73ace31a93)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeviceDefinitionVersionProps(
            device_definition_id=device_definition_id, devices=devices
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75f076efee1cfe7e6a6aa35cffba776ede5eb8c3ebc6b05d12324b9ed098c8c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__82c976f156be131579618e357fb04ee79c5fa16268fa8502ebebf331489243c8)
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
    @jsii.member(jsii_name="deviceDefinitionId")
    def device_definition_id(self) -> builtins.str:
        '''The ID of the device definition associated with this version.'''
        return typing.cast(builtins.str, jsii.get(self, "deviceDefinitionId"))

    @device_definition_id.setter
    def device_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e81c0aa8405667eeeaadd67c78cb7b7ddd5bc27f106a564e32912851386e4931)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="devices")
    def devices(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeviceDefinitionVersion.DeviceProperty"]]]:
        '''The devices in this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeviceDefinitionVersion.DeviceProperty"]]], jsii.get(self, "devices"))

    @devices.setter
    def devices(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeviceDefinitionVersion.DeviceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0aabdafe61d8e2100f8e9a731798871a20d7438db750e894f114287763994f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devices", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnDeviceDefinitionVersion.DeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "id": "id",
            "thing_arn": "thingArn",
            "sync_shadow": "syncShadow",
        },
    )
    class DeviceProperty:
        def __init__(
            self,
            *,
            certificate_arn: builtins.str,
            id: builtins.str,
            thing_arn: builtins.str,
            sync_shadow: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A device is an AWS IoT device (thing) that's added to a Greengrass group.

            Greengrass devices can communicate with the Greengrass core in the same group. For more information, see `What Is AWS IoT Greengrass ? <https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Devices`` property of the ```AWS::Greengrass::DeviceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html>`_ resource contains a list of ``Device`` property types.

            :param certificate_arn: The ARN of the device certificate for the device. This X.509 certificate is used to authenticate the device with AWS IoT and AWS IoT Greengrass services.
            :param id: A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param thing_arn: The Amazon Resource Name (ARN) of the device, which is an AWS IoT device (thing).
            :param sync_shadow: Indicates whether the device's local shadow is synced with the cloud automatically.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                device_property = greengrass.CfnDeviceDefinitionVersion.DeviceProperty(
                    certificate_arn="certificateArn",
                    id="id",
                    thing_arn="thingArn",
                
                    # the properties below are optional
                    sync_shadow=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__253b05ead7f7258dbe7d542a3d84a1dcb9e7461853810ffd646f2efad7c3cd74)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
                check_type(argname="argument sync_shadow", value=sync_shadow, expected_type=type_hints["sync_shadow"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_arn": certificate_arn,
                "id": id,
                "thing_arn": thing_arn,
            }
            if sync_shadow is not None:
                self._values["sync_shadow"] = sync_shadow

        @builtins.property
        def certificate_arn(self) -> builtins.str:
            '''The ARN of the device certificate for the device.

            This X.509 certificate is used to authenticate the device with AWS IoT and AWS IoT Greengrass services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-certificatearn
            '''
            result = self._values.get("certificate_arn")
            assert result is not None, "Required property 'certificate_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the device.

            This value must be unique within the device definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def thing_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the device, which is an AWS IoT device (thing).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-thingarn
            '''
            result = self._values.get("thing_arn")
            assert result is not None, "Required property 'thing_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sync_shadow(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the device's local shadow is synced with the cloud automatically.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-syncshadow
            '''
            result = self._values.get("sync_shadow")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnDeviceDefinitionVersionProps",
    jsii_struct_bases=[],
    name_mapping={"device_definition_id": "deviceDefinitionId", "devices": "devices"},
)
class CfnDeviceDefinitionVersionProps:
    def __init__(
        self,
        *,
        device_definition_id: builtins.str,
        devices: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceDefinitionVersion.DeviceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnDeviceDefinitionVersion``.

        :param device_definition_id: The ID of the device definition associated with this version. This value is a GUID.
        :param devices: The devices in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            cfn_device_definition_version_props = greengrass.CfnDeviceDefinitionVersionProps(
                device_definition_id="deviceDefinitionId",
                devices=[greengrass.CfnDeviceDefinitionVersion.DeviceProperty(
                    certificate_arn="certificateArn",
                    id="id",
                    thing_arn="thingArn",
            
                    # the properties below are optional
                    sync_shadow=False
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ba582d02e3f46be1f7ffc866489e7b5768fda19646ac5cb6fb39be0cc3b7e09)
            check_type(argname="argument device_definition_id", value=device_definition_id, expected_type=type_hints["device_definition_id"])
            check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_definition_id": device_definition_id,
            "devices": devices,
        }

    @builtins.property
    def device_definition_id(self) -> builtins.str:
        '''The ID of the device definition associated with this version.

        This value is a GUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html#cfn-greengrass-devicedefinitionversion-devicedefinitionid
        '''
        result = self._values.get("device_definition_id")
        assert result is not None, "Required property 'device_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def devices(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeviceDefinitionVersion.DeviceProperty]]]:
        '''The devices in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html#cfn-greengrass-devicedefinitionversion-devices
        '''
        result = self._values.get("devices")
        assert result is not None, "Required property 'devices' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeviceDefinitionVersion.DeviceProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceDefinitionVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFunctionDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition",
):
    '''The ``AWS::Greengrass::FunctionDefinition`` resource represents a function definition for AWS IoT Greengrass .

    Function definitions are used to organize your function definition versions.

    Function definitions can reference multiple function definition versions. All function definition versions must be associated with a function definition. Each function definition version can contain one or more functions.
    .. epigraph::

       When you create a function definition, you can optionally include an initial function definition version. To associate a function definition version later, create an ```AWS::Greengrass::FunctionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html>`_ resource and specify the ID of this function definition.

       After you create the function definition version that contains the functions you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # tags: Any
        # variables: Any
        
        cfn_function_definition = greengrass.CfnFunctionDefinition(self, "MyCfnFunctionDefinition",
            name="name",
        
            # the properties below are optional
            initial_version=greengrass.CfnFunctionDefinition.FunctionDefinitionVersionProperty(
                functions=[greengrass.CfnFunctionDefinition.FunctionProperty(
                    function_arn="functionArn",
                    function_configuration=greengrass.CfnFunctionDefinition.FunctionConfigurationProperty(
                        encoding_type="encodingType",
                        environment=greengrass.CfnFunctionDefinition.EnvironmentProperty(
                            access_sysfs=False,
                            execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                                isolation_mode="isolationMode",
                                run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                                    gid=123,
                                    uid=123
                                )
                            ),
                            resource_access_policies=[greengrass.CfnFunctionDefinition.ResourceAccessPolicyProperty(
                                resource_id="resourceId",
        
                                # the properties below are optional
                                permission="permission"
                            )],
                            variables=variables
                        ),
                        exec_args="execArgs",
                        executable="executable",
                        memory_size=123,
                        pinned=False,
                        timeout=123
                    ),
                    id="id"
                )],
        
                # the properties below are optional
                default_config=greengrass.CfnFunctionDefinition.DefaultConfigProperty(
                    execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                        isolation_mode="isolationMode",
                        run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                            gid=123,
                            uid=123
                        )
                    )
                )
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.FunctionDefinitionVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the function definition.
        :param initial_version: The function definition version to include when the function definition is created. A function definition version contains a list of ```function`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html>`_ property types. .. epigraph:: To associate a function definition version after the function definition is created, create an ```AWS::Greengrass::FunctionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html>`_ resource and specify the ID of this function definition.
        :param tags: Application-specific metadata to attach to the function definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc054a16da2a52b953d26f46ac8928cd46a0d3b00ea138b637dba87125670b02)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFunctionDefinitionProps(
            name=name, initial_version=initial_version, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883759389b9b6062c199dfa06474e6b6eae814f3d29cb567a6c1accc041ac340)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5eb475f6df385b65a6fa5feebde3a756e64967f6ed1a1c94c355e0641d025d4)
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
        '''The Amazon Resource Name (ARN) of the ``FunctionDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/functions/1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the ``FunctionDefinition`` , such as ``1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersionArn")
    def attr_latest_version_arn(self) -> builtins.str:
        '''The ARN of the last ``FunctionDefinitionVersion`` that was added to the ``FunctionDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/functions/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`` .

        :cloudformationAttribute: LatestVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the ``FunctionDefinition`` , such as ``MyFunctionDefinition`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''The name of the function definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63f3586ebd22c8d7efa859e3b07e7a1d59b40ead5bd2fcda78d352eb33e98b21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="initialVersion")
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.FunctionDefinitionVersionProperty"]]:
        '''The function definition version to include when the function definition is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.FunctionDefinitionVersionProperty"]], jsii.get(self, "initialVersion"))

    @initial_version.setter
    def initial_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.FunctionDefinitionVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09ef946c280aa3fe299d97090ecfb5dfa4af0a16702b75c593ec39701a3cb62b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''Application-specific metadata to attach to the function definition.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de5a19ed9c188b2bb1a6eecf3c47192c7edf18069ffe0cdf6838d6eadee8effd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition.DefaultConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"execution": "execution"},
    )
    class DefaultConfigProperty:
        def __init__(
            self,
            *,
            execution: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.ExecutionProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The default configuration that applies to all Lambda functions in the function definition version.

            Individual Lambda functions can override these settings.

            In an AWS CloudFormation template, ``DefaultConfig`` is a property of the ```FunctionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html>`_ property type.

            :param execution: Configuration settings for the Lambda execution environment on the AWS IoT Greengrass core.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                default_config_property = greengrass.CfnFunctionDefinition.DefaultConfigProperty(
                    execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                        isolation_mode="isolationMode",
                        run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                            gid=123,
                            uid=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8141acc3a004423bffa1be5752871f489d86a51c46b744ac79a869e6a745c4d4)
                check_type(argname="argument execution", value=execution, expected_type=type_hints["execution"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "execution": execution,
            }

        @builtins.property
        def execution(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.ExecutionProperty"]:
            '''Configuration settings for the Lambda execution environment on the AWS IoT Greengrass core.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html#cfn-greengrass-functiondefinition-defaultconfig-execution
            '''
            result = self._values.get("execution")
            assert result is not None, "Required property 'execution' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.ExecutionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_sysfs": "accessSysfs",
            "execution": "execution",
            "resource_access_policies": "resourceAccessPolicies",
            "variables": "variables",
        },
    )
    class EnvironmentProperty:
        def __init__(
            self,
            *,
            access_sysfs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            execution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.ExecutionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resource_access_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.ResourceAccessPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            variables: typing.Any = None,
        ) -> None:
            '''The environment configuration for a Lambda function on the AWS IoT Greengrass core.

            In an AWS CloudFormation template, ``Environment`` is a property of the ```FunctionConfiguration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html>`_ property type.

            :param access_sysfs: Indicates whether the function is allowed to access the ``/sys`` directory on the core device, which allows the read device information from ``/sys`` . .. epigraph:: This property applies only to Lambda functions that run in a Greengrass container.
            :param execution: Settings for the Lambda execution environment in AWS IoT Greengrass .
            :param resource_access_policies: A list of the `resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html>`_ in the group that the function can access, with the corresponding read-only or read-write permissions. The maximum is 10 resources. .. epigraph:: This property applies only for Lambda functions that run in a Greengrass container.
            :param variables: Environment variables for the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # variables: Any
                
                environment_property = greengrass.CfnFunctionDefinition.EnvironmentProperty(
                    access_sysfs=False,
                    execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                        isolation_mode="isolationMode",
                        run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                            gid=123,
                            uid=123
                        )
                    ),
                    resource_access_policies=[greengrass.CfnFunctionDefinition.ResourceAccessPolicyProperty(
                        resource_id="resourceId",
                
                        # the properties below are optional
                        permission="permission"
                    )],
                    variables=variables
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4292cc2a15784a3b0bab48fede867f394d01dc9f076e30078fc77deaf8381cc)
                check_type(argname="argument access_sysfs", value=access_sysfs, expected_type=type_hints["access_sysfs"])
                check_type(argname="argument execution", value=execution, expected_type=type_hints["execution"])
                check_type(argname="argument resource_access_policies", value=resource_access_policies, expected_type=type_hints["resource_access_policies"])
                check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_sysfs is not None:
                self._values["access_sysfs"] = access_sysfs
            if execution is not None:
                self._values["execution"] = execution
            if resource_access_policies is not None:
                self._values["resource_access_policies"] = resource_access_policies
            if variables is not None:
                self._values["variables"] = variables

        @builtins.property
        def access_sysfs(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the function is allowed to access the ``/sys`` directory on the core device, which allows the read device information from ``/sys`` .

            .. epigraph::

               This property applies only to Lambda functions that run in a Greengrass container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-accesssysfs
            '''
            result = self._values.get("access_sysfs")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def execution(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.ExecutionProperty"]]:
            '''Settings for the Lambda execution environment in AWS IoT Greengrass .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-execution
            '''
            result = self._values.get("execution")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.ExecutionProperty"]], result)

        @builtins.property
        def resource_access_policies(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.ResourceAccessPolicyProperty"]]]]:
            '''A list of the `resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html>`_ in the group that the function can access, with the corresponding read-only or read-write permissions. The maximum is 10 resources.

            .. epigraph::

               This property applies only for Lambda functions that run in a Greengrass container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-resourceaccesspolicies
            '''
            result = self._values.get("resource_access_policies")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.ResourceAccessPolicyProperty"]]]], result)

        @builtins.property
        def variables(self) -> typing.Any:
            '''Environment variables for the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-variables
            '''
            result = self._values.get("variables")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition.ExecutionProperty",
        jsii_struct_bases=[],
        name_mapping={"isolation_mode": "isolationMode", "run_as": "runAs"},
    )
    class ExecutionProperty:
        def __init__(
            self,
            *,
            isolation_mode: typing.Optional[builtins.str] = None,
            run_as: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.RunAsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration settings for the Lambda execution environment on the AWS IoT Greengrass core.

            In an AWS CloudFormation template, ``Execution`` is a property of the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html>`_ property type for a function definition version and the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html>`_ property type for a function.

            :param isolation_mode: The containerization that the Lambda function runs in. Valid values are ``GreengrassContainer`` or ``NoContainer`` . Typically, this is ``GreengrassContainer`` . For more information, see `Containerization <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-function-containerization>`_ in the *Developer Guide* . - When set on the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property of a function definition version, this setting is used as the default containerization for all Lambda functions in the function definition version. - When set on the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property of a function, this setting applies to the individual function and overrides the default. Omit this value to run the function with the default containerization. .. epigraph:: We recommend that you run in a Greengrass container unless your business case requires that you run without containerization.
            :param run_as: The user and group permissions used to run the Lambda function. Typically, this is the ggc_user and ggc_group. For more information, see `Run as <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-access-identity.html>`_ in the *Developer Guide* . - When set on the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property of a function definition version, this setting is used as the default access identity for all Lambda functions in the function definition version. - When set on the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property of a function, this setting applies to the individual function and overrides the default. You can override the user, group, or both. Omit this value to run the function with the default permissions. .. epigraph:: Running as the root user increases risks to your data and device. Do not run as root (UID/GID=0) unless your business case requires it. For more information and requirements, see `Running a Lambda Function as Root <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-running-as-root>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                execution_property = greengrass.CfnFunctionDefinition.ExecutionProperty(
                    isolation_mode="isolationMode",
                    run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                        gid=123,
                        uid=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b70e9d861e6b33c0e42706480eb4da7187fb3ff64d5ada17a7940f9296fd2a9e)
                check_type(argname="argument isolation_mode", value=isolation_mode, expected_type=type_hints["isolation_mode"])
                check_type(argname="argument run_as", value=run_as, expected_type=type_hints["run_as"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if isolation_mode is not None:
                self._values["isolation_mode"] = isolation_mode
            if run_as is not None:
                self._values["run_as"] = run_as

        @builtins.property
        def isolation_mode(self) -> typing.Optional[builtins.str]:
            '''The containerization that the Lambda function runs in.

            Valid values are ``GreengrassContainer`` or ``NoContainer`` . Typically, this is ``GreengrassContainer`` . For more information, see `Containerization <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-function-containerization>`_ in the *Developer Guide* .

            - When set on the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property of a function definition version, this setting is used as the default containerization for all Lambda functions in the function definition version.
            - When set on the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property of a function, this setting applies to the individual function and overrides the default. Omit this value to run the function with the default containerization.

            .. epigraph::

               We recommend that you run in a Greengrass container unless your business case requires that you run without containerization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html#cfn-greengrass-functiondefinition-execution-isolationmode
            '''
            result = self._values.get("isolation_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def run_as(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.RunAsProperty"]]:
            '''The user and group permissions used to run the Lambda function.

            Typically, this is the ggc_user and ggc_group. For more information, see `Run as <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-access-identity.html>`_ in the *Developer Guide* .

            - When set on the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property of a function definition version, this setting is used as the default access identity for all Lambda functions in the function definition version.
            - When set on the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property of a function, this setting applies to the individual function and overrides the default. You can override the user, group, or both. Omit this value to run the function with the default permissions.

            .. epigraph::

               Running as the root user increases risks to your data and device. Do not run as root (UID/GID=0) unless your business case requires it. For more information and requirements, see `Running a Lambda Function as Root <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-running-as-root>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html#cfn-greengrass-functiondefinition-execution-runas
            '''
            result = self._values.get("run_as")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.RunAsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition.FunctionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encoding_type": "encodingType",
            "environment": "environment",
            "exec_args": "execArgs",
            "executable": "executable",
            "memory_size": "memorySize",
            "pinned": "pinned",
            "timeout": "timeout",
        },
    )
    class FunctionConfigurationProperty:
        def __init__(
            self,
            *,
            encoding_type: typing.Optional[builtins.str] = None,
            environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.EnvironmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            exec_args: typing.Optional[builtins.str] = None,
            executable: typing.Optional[builtins.str] = None,
            memory_size: typing.Optional[jsii.Number] = None,
            pinned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The group-specific configuration settings for a Lambda function.

            These settings configure the function's behavior in the Greengrass group. For more information, see `Controlling Execution of Greengrass Lambda Functions by Using Group-Specific Configuration <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``FunctionConfiguration`` is a property of the ```Function`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html>`_ property type.

            :param encoding_type: The expected encoding type of the input payload for the function. Valid values are ``json`` (default) and ``binary`` .
            :param environment: The environment configuration of the function.
            :param exec_args: The execution arguments.
            :param executable: The name of the function executable.
            :param memory_size: The memory size (in KB) required by the function. .. epigraph:: This property applies only to Lambda functions that run in a Greengrass container.
            :param pinned: Indicates whether the function is pinned (or *long-lived* ). Pinned functions start when the core starts and process all requests in the same container. The default value is false.
            :param timeout: The allowed execution time (in seconds) after which the function should terminate. For pinned functions, this timeout applies for each request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # variables: Any
                
                function_configuration_property = greengrass.CfnFunctionDefinition.FunctionConfigurationProperty(
                    encoding_type="encodingType",
                    environment=greengrass.CfnFunctionDefinition.EnvironmentProperty(
                        access_sysfs=False,
                        execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                            isolation_mode="isolationMode",
                            run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                                gid=123,
                                uid=123
                            )
                        ),
                        resource_access_policies=[greengrass.CfnFunctionDefinition.ResourceAccessPolicyProperty(
                            resource_id="resourceId",
                
                            # the properties below are optional
                            permission="permission"
                        )],
                        variables=variables
                    ),
                    exec_args="execArgs",
                    executable="executable",
                    memory_size=123,
                    pinned=False,
                    timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__98d434196f1da3f825c92283259908906d812252031be392844dfd7ad5a1d266)
                check_type(argname="argument encoding_type", value=encoding_type, expected_type=type_hints["encoding_type"])
                check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
                check_type(argname="argument exec_args", value=exec_args, expected_type=type_hints["exec_args"])
                check_type(argname="argument executable", value=executable, expected_type=type_hints["executable"])
                check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
                check_type(argname="argument pinned", value=pinned, expected_type=type_hints["pinned"])
                check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encoding_type is not None:
                self._values["encoding_type"] = encoding_type
            if environment is not None:
                self._values["environment"] = environment
            if exec_args is not None:
                self._values["exec_args"] = exec_args
            if executable is not None:
                self._values["executable"] = executable
            if memory_size is not None:
                self._values["memory_size"] = memory_size
            if pinned is not None:
                self._values["pinned"] = pinned
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def encoding_type(self) -> typing.Optional[builtins.str]:
            '''The expected encoding type of the input payload for the function.

            Valid values are ``json`` (default) and ``binary`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-encodingtype
            '''
            result = self._values.get("encoding_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.EnvironmentProperty"]]:
            '''The environment configuration of the function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.EnvironmentProperty"]], result)

        @builtins.property
        def exec_args(self) -> typing.Optional[builtins.str]:
            '''The execution arguments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-execargs
            '''
            result = self._values.get("exec_args")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def executable(self) -> typing.Optional[builtins.str]:
            '''The name of the function executable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-executable
            '''
            result = self._values.get("executable")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def memory_size(self) -> typing.Optional[jsii.Number]:
            '''The memory size (in KB) required by the function.

            .. epigraph::

               This property applies only to Lambda functions that run in a Greengrass container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-memorysize
            '''
            result = self._values.get("memory_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pinned(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the function is pinned (or *long-lived* ).

            Pinned functions start when the core starts and process all requests in the same container. The default value is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-pinned
            '''
            result = self._values.get("pinned")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''The allowed execution time (in seconds) after which the function should terminate.

            For pinned functions, this timeout applies for each request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition.FunctionDefinitionVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"functions": "functions", "default_config": "defaultConfig"},
    )
    class FunctionDefinitionVersionProperty:
        def __init__(
            self,
            *,
            functions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.FunctionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.DefaultConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A function definition version contains a list of functions.

            .. epigraph::

               After you create a function definition version that contains the functions you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

            In an AWS CloudFormation template, ``FunctionDefinitionVersion`` is the property type of the ``InitialVersion`` property in the ```AWS::Greengrass::FunctionDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html>`_ resource.

            :param functions: The functions in this version.
            :param default_config: The default configuration that applies to all Lambda functions in the group. Individual Lambda functions can override these settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # variables: Any
                
                function_definition_version_property = greengrass.CfnFunctionDefinition.FunctionDefinitionVersionProperty(
                    functions=[greengrass.CfnFunctionDefinition.FunctionProperty(
                        function_arn="functionArn",
                        function_configuration=greengrass.CfnFunctionDefinition.FunctionConfigurationProperty(
                            encoding_type="encodingType",
                            environment=greengrass.CfnFunctionDefinition.EnvironmentProperty(
                                access_sysfs=False,
                                execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                                    isolation_mode="isolationMode",
                                    run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                                        gid=123,
                                        uid=123
                                    )
                                ),
                                resource_access_policies=[greengrass.CfnFunctionDefinition.ResourceAccessPolicyProperty(
                                    resource_id="resourceId",
                
                                    # the properties below are optional
                                    permission="permission"
                                )],
                                variables=variables
                            ),
                            exec_args="execArgs",
                            executable="executable",
                            memory_size=123,
                            pinned=False,
                            timeout=123
                        ),
                        id="id"
                    )],
                
                    # the properties below are optional
                    default_config=greengrass.CfnFunctionDefinition.DefaultConfigProperty(
                        execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                            isolation_mode="isolationMode",
                            run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                                gid=123,
                                uid=123
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3cf2ab9fa59092d61d89f64ed51286c1ffbcc6ff91799c90c41d5102213f0f32)
                check_type(argname="argument functions", value=functions, expected_type=type_hints["functions"])
                check_type(argname="argument default_config", value=default_config, expected_type=type_hints["default_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "functions": functions,
            }
            if default_config is not None:
                self._values["default_config"] = default_config

        @builtins.property
        def functions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.FunctionProperty"]]]:
            '''The functions in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-functions
            '''
            result = self._values.get("functions")
            assert result is not None, "Required property 'functions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.FunctionProperty"]]], result)

        @builtins.property
        def default_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.DefaultConfigProperty"]]:
            '''The default configuration that applies to all Lambda functions in the group.

            Individual Lambda functions can override these settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-defaultconfig
            '''
            result = self._values.get("default_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.DefaultConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionDefinitionVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition.FunctionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_arn": "functionArn",
            "function_configuration": "functionConfiguration",
            "id": "id",
        },
    )
    class FunctionProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            function_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinition.FunctionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            id: builtins.str,
        ) -> None:
            '''A function is a Lambda function that's referenced from an AWS IoT Greengrass group.

            The function is deployed to a Greengrass core where it runs locally. For more information, see `Run Lambda Functions on the AWS IoT Greengrass Core <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-functions.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Functions`` property of the ```FunctionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html>`_ property type contains a list of ``Function`` property types.

            :param function_arn: The Amazon Resource Name (ARN) of the alias (recommended) or version of the referenced Lambda function.
            :param function_configuration: The group-specific settings of the Lambda function. These settings configure the function's behavior in the Greengrass group.
            :param id: A descriptive or arbitrary ID for the function. This value must be unique within the function definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # variables: Any
                
                function_property = greengrass.CfnFunctionDefinition.FunctionProperty(
                    function_arn="functionArn",
                    function_configuration=greengrass.CfnFunctionDefinition.FunctionConfigurationProperty(
                        encoding_type="encodingType",
                        environment=greengrass.CfnFunctionDefinition.EnvironmentProperty(
                            access_sysfs=False,
                            execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                                isolation_mode="isolationMode",
                                run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                                    gid=123,
                                    uid=123
                                )
                            ),
                            resource_access_policies=[greengrass.CfnFunctionDefinition.ResourceAccessPolicyProperty(
                                resource_id="resourceId",
                
                                # the properties below are optional
                                permission="permission"
                            )],
                            variables=variables
                        ),
                        exec_args="execArgs",
                        executable="executable",
                        memory_size=123,
                        pinned=False,
                        timeout=123
                    ),
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d06406f22f33062b37608c66ede16429af10bcb88224eaae6da351e8b512eb5)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
                check_type(argname="argument function_configuration", value=function_configuration, expected_type=type_hints["function_configuration"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_arn": function_arn,
                "function_configuration": function_configuration,
                "id": id,
            }

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the alias (recommended) or version of the referenced Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def function_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.FunctionConfigurationProperty"]:
            '''The group-specific settings of the Lambda function.

            These settings configure the function's behavior in the Greengrass group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-functionconfiguration
            '''
            result = self._values.get("function_configuration")
            assert result is not None, "Required property 'function_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinition.FunctionConfigurationProperty"], result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the function.

            This value must be unique within the function definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition.ResourceAccessPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_id": "resourceId", "permission": "permission"},
    )
    class ResourceAccessPolicyProperty:
        def __init__(
            self,
            *,
            resource_id: builtins.str,
            permission: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A list of the `resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html>`_ in the group that the function can access, with the corresponding read-only or read-write permissions. The maximum is 10 resources.

            .. epigraph::

               This property applies only to Lambda functions that run in a Greengrass container.

            In an AWS CloudFormation template, ``ResourceAccessPolicy`` is a property of the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html>`_ property type.

            :param resource_id: The ID of the resource. This ID is assigned to the resource when you create the resource definition.
            :param permission: The read-only or read-write access that the Lambda function has to the resource. Valid values are ``ro`` or ``rw`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_access_policy_property = greengrass.CfnFunctionDefinition.ResourceAccessPolicyProperty(
                    resource_id="resourceId",
                
                    # the properties below are optional
                    permission="permission"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__83ce8dcd35f15a7c52707cb20e4f653d274051d0b69be412461a84fde59d4747)
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_id": resource_id,
            }
            if permission is not None:
                self._values["permission"] = permission

        @builtins.property
        def resource_id(self) -> builtins.str:
            '''The ID of the resource.

            This ID is assigned to the resource when you create the resource definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html#cfn-greengrass-functiondefinition-resourceaccesspolicy-resourceid
            '''
            result = self._values.get("resource_id")
            assert result is not None, "Required property 'resource_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def permission(self) -> typing.Optional[builtins.str]:
            '''The read-only or read-write access that the Lambda function has to the resource.

            Valid values are ``ro`` or ``rw`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html#cfn-greengrass-functiondefinition-resourceaccesspolicy-permission
            '''
            result = self._values.get("permission")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceAccessPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinition.RunAsProperty",
        jsii_struct_bases=[],
        name_mapping={"gid": "gid", "uid": "uid"},
    )
    class RunAsProperty:
        def __init__(
            self,
            *,
            gid: typing.Optional[jsii.Number] = None,
            uid: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The access identity whose permissions are used to run the Lambda function.

            This setting overrides the default access identity that's specified for the group (by default, ggc_user and ggc_group). You can override the user, group, or both. For more information, see `Run as <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-access-identity.html>`_ in the *Developer Guide* .
            .. epigraph::

               Running as the root user increases risks to your data and device. Do not run as root (UID/GID=0) unless your business case requires it. For more information and requirements, see `Running a Lambda Function as Root <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-running-as-root>`_ .

            In an AWS CloudFormation template, ``RunAs`` is a property of the ```Execution`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html>`_ property type.

            :param gid: The group ID whose permissions are used to run the Lambda function. You can use the ``getent group`` command on your core device to look up the group ID.
            :param uid: The user ID whose permissions are used to run the Lambda function. You can use the ``getent passwd`` command on your core device to look up the user ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                run_as_property = greengrass.CfnFunctionDefinition.RunAsProperty(
                    gid=123,
                    uid=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__044b15bdedd91446b78ce0f57b82c3734bcbedd95c01454cdca47d61efccb494)
                check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
                check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if gid is not None:
                self._values["gid"] = gid
            if uid is not None:
                self._values["uid"] = uid

        @builtins.property
        def gid(self) -> typing.Optional[jsii.Number]:
            '''The group ID whose permissions are used to run the Lambda function.

            You can use the ``getent group`` command on your core device to look up the group ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html#cfn-greengrass-functiondefinition-runas-gid
            '''
            result = self._values.get("gid")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def uid(self) -> typing.Optional[jsii.Number]:
            '''The user ID whose permissions are used to run the Lambda function.

            You can use the ``getent passwd`` command on your core device to look up the user ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html#cfn-greengrass-functiondefinition-runas-uid
            '''
            result = self._values.get("uid")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunAsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "initial_version": "initialVersion", "tags": "tags"},
)
class CfnFunctionDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.FunctionDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnFunctionDefinition``.

        :param name: The name of the function definition.
        :param initial_version: The function definition version to include when the function definition is created. A function definition version contains a list of ```function`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html>`_ property types. .. epigraph:: To associate a function definition version after the function definition is created, create an ```AWS::Greengrass::FunctionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html>`_ resource and specify the ID of this function definition.
        :param tags: Application-specific metadata to attach to the function definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # tags: Any
            # variables: Any
            
            cfn_function_definition_props = greengrass.CfnFunctionDefinitionProps(
                name="name",
            
                # the properties below are optional
                initial_version=greengrass.CfnFunctionDefinition.FunctionDefinitionVersionProperty(
                    functions=[greengrass.CfnFunctionDefinition.FunctionProperty(
                        function_arn="functionArn",
                        function_configuration=greengrass.CfnFunctionDefinition.FunctionConfigurationProperty(
                            encoding_type="encodingType",
                            environment=greengrass.CfnFunctionDefinition.EnvironmentProperty(
                                access_sysfs=False,
                                execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                                    isolation_mode="isolationMode",
                                    run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                                        gid=123,
                                        uid=123
                                    )
                                ),
                                resource_access_policies=[greengrass.CfnFunctionDefinition.ResourceAccessPolicyProperty(
                                    resource_id="resourceId",
            
                                    # the properties below are optional
                                    permission="permission"
                                )],
                                variables=variables
                            ),
                            exec_args="execArgs",
                            executable="executable",
                            memory_size=123,
                            pinned=False,
                            timeout=123
                        ),
                        id="id"
                    )],
            
                    # the properties below are optional
                    default_config=greengrass.CfnFunctionDefinition.DefaultConfigProperty(
                        execution=greengrass.CfnFunctionDefinition.ExecutionProperty(
                            isolation_mode="isolationMode",
                            run_as=greengrass.CfnFunctionDefinition.RunAsProperty(
                                gid=123,
                                uid=123
                            )
                        )
                    )
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e62d17dcf2bc0d49a9e8075057460e72eae2dd41694fd8988f7dfbd7bb507a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument initial_version", value=initial_version, expected_type=type_hints["initial_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if initial_version is not None:
            self._values["initial_version"] = initial_version
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the function definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinition.FunctionDefinitionVersionProperty]]:
        '''The function definition version to include when the function definition is created.

        A function definition version contains a list of ```function`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html>`_ property types.
        .. epigraph::

           To associate a function definition version after the function definition is created, create an ```AWS::Greengrass::FunctionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html>`_ resource and specify the ID of this function definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-initialversion
        '''
        result = self._values.get("initial_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinition.FunctionDefinitionVersionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Application-specific metadata to attach to the function definition.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFunctionDefinitionVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersion",
):
    '''The ``AWS::Greengrass::FunctionDefinitionVersion`` resource represents a function definition version for AWS IoT Greengrass .

    A function definition version contains contain a list of functions.
    .. epigraph::

       To create a function definition version, you must specify the ID of the function definition that you want to associate with the version. For information about creating a function definition, see ```AWS::Greengrass::FunctionDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html>`_ .

       After you create a function definition version that contains the functions you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # variables: Any
        
        cfn_function_definition_version = greengrass.CfnFunctionDefinitionVersion(self, "MyCfnFunctionDefinitionVersion",
            function_definition_id="functionDefinitionId",
            functions=[greengrass.CfnFunctionDefinitionVersion.FunctionProperty(
                function_arn="functionArn",
                function_configuration=greengrass.CfnFunctionDefinitionVersion.FunctionConfigurationProperty(
                    encoding_type="encodingType",
                    environment=greengrass.CfnFunctionDefinitionVersion.EnvironmentProperty(
                        access_sysfs=False,
                        execution=greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                            isolation_mode="isolationMode",
                            run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                                gid=123,
                                uid=123
                            )
                        ),
                        resource_access_policies=[greengrass.CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty(
                            resource_id="resourceId",
        
                            # the properties below are optional
                            permission="permission"
                        )],
                        variables=variables
                    ),
                    exec_args="execArgs",
                    executable="executable",
                    memory_size=123,
                    pinned=False,
                    timeout=123
                ),
                id="id"
            )],
        
            # the properties below are optional
            default_config=greengrass.CfnFunctionDefinitionVersion.DefaultConfigProperty(
                execution=greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                    isolation_mode="isolationMode",
                    run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                        gid=123,
                        uid=123
                    )
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        function_definition_id: builtins.str,
        functions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinitionVersion.FunctionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinitionVersion.DefaultConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param function_definition_id: The ID of the function definition associated with this version. This value is a GUID.
        :param functions: The functions in this version.
        :param default_config: The default configuration that applies to all Lambda functions in the group. Individual Lambda functions can override these settings.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74049a58818d8fb74724e45f074f2d356fba374467a1926758e3e761c205d756)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFunctionDefinitionVersionProps(
            function_definition_id=function_definition_id,
            functions=functions,
            default_config=default_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53d31f9160e02bf734beeedf9a11d142ba8858555d274b4c85da63595775c72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea22062ecf7322056761cf0f4266b5142070757362434ce77d6180f10611daee)
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
    @jsii.member(jsii_name="functionDefinitionId")
    def function_definition_id(self) -> builtins.str:
        '''The ID of the function definition associated with this version.'''
        return typing.cast(builtins.str, jsii.get(self, "functionDefinitionId"))

    @function_definition_id.setter
    def function_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089983427f200b57e702fff54bb0b007c29cdd60772ebee7e6374971f11b5d3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="functions")
    def functions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.FunctionProperty"]]]:
        '''The functions in this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.FunctionProperty"]]], jsii.get(self, "functions"))

    @functions.setter
    def functions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.FunctionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__793cfd87f23bbd9bf6e301d174c974540fcb771743c65e05c1a0a4025bf87005)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functions", value)

    @builtins.property
    @jsii.member(jsii_name="defaultConfig")
    def default_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.DefaultConfigProperty"]]:
        '''The default configuration that applies to all Lambda functions in the group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.DefaultConfigProperty"]], jsii.get(self, "defaultConfig"))

    @default_config.setter
    def default_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.DefaultConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0390fd3aa93f9d9e878e662d53c38486d861c310d7e93ad7f1c0f86c70cee20c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersion.DefaultConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"execution": "execution"},
    )
    class DefaultConfigProperty:
        def __init__(
            self,
            *,
            execution: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinitionVersion.ExecutionProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The default configuration that applies to all Lambda functions in the function definition version.

            Individual Lambda functions can override these settings.

            In an AWS CloudFormation template, ``DefaultConfig`` is a property of the ```AWS::Greengrass::FunctionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html>`_ resource.

            :param execution: Configuration settings for the Lambda execution environment on the AWS IoT Greengrass core.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                default_config_property = greengrass.CfnFunctionDefinitionVersion.DefaultConfigProperty(
                    execution=greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                        isolation_mode="isolationMode",
                        run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                            gid=123,
                            uid=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dfacedad0a59ccb5e2eaec7676b018b92ee6862f373104646bf110f388b3e418)
                check_type(argname="argument execution", value=execution, expected_type=type_hints["execution"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "execution": execution,
            }

        @builtins.property
        def execution(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.ExecutionProperty"]:
            '''Configuration settings for the Lambda execution environment on the AWS IoT Greengrass core.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html#cfn-greengrass-functiondefinitionversion-defaultconfig-execution
            '''
            result = self._values.get("execution")
            assert result is not None, "Required property 'execution' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.ExecutionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersion.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_sysfs": "accessSysfs",
            "execution": "execution",
            "resource_access_policies": "resourceAccessPolicies",
            "variables": "variables",
        },
    )
    class EnvironmentProperty:
        def __init__(
            self,
            *,
            access_sysfs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            execution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinitionVersion.ExecutionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resource_access_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            variables: typing.Any = None,
        ) -> None:
            '''The environment configuration for a Lambda function on the AWS IoT Greengrass core.

            In an AWS CloudFormation template, ``Environment`` is a property of the ```FunctionConfiguration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html>`_ property type.

            :param access_sysfs: Indicates whether the function is allowed to access the ``/sys`` directory on the core device, which allows the read device information from ``/sys`` . .. epigraph:: This property applies only to Lambda functions that run in a Greengrass container.
            :param execution: Settings for the Lambda execution environment in AWS IoT Greengrass .
            :param resource_access_policies: A list of the `resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html>`_ in the group that the function can access, with the corresponding read-only or read-write permissions. The maximum is 10 resources. .. epigraph:: This property applies only to Lambda functions that run in a Greengrass container.
            :param variables: Environment variables for the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # variables: Any
                
                environment_property = greengrass.CfnFunctionDefinitionVersion.EnvironmentProperty(
                    access_sysfs=False,
                    execution=greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                        isolation_mode="isolationMode",
                        run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                            gid=123,
                            uid=123
                        )
                    ),
                    resource_access_policies=[greengrass.CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty(
                        resource_id="resourceId",
                
                        # the properties below are optional
                        permission="permission"
                    )],
                    variables=variables
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__955f01f10cbdbbb5ea2b4005e2fdd4b4733b2c02fd34963370b597105324bef9)
                check_type(argname="argument access_sysfs", value=access_sysfs, expected_type=type_hints["access_sysfs"])
                check_type(argname="argument execution", value=execution, expected_type=type_hints["execution"])
                check_type(argname="argument resource_access_policies", value=resource_access_policies, expected_type=type_hints["resource_access_policies"])
                check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_sysfs is not None:
                self._values["access_sysfs"] = access_sysfs
            if execution is not None:
                self._values["execution"] = execution
            if resource_access_policies is not None:
                self._values["resource_access_policies"] = resource_access_policies
            if variables is not None:
                self._values["variables"] = variables

        @builtins.property
        def access_sysfs(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the function is allowed to access the ``/sys`` directory on the core device, which allows the read device information from ``/sys`` .

            .. epigraph::

               This property applies only to Lambda functions that run in a Greengrass container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-accesssysfs
            '''
            result = self._values.get("access_sysfs")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def execution(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.ExecutionProperty"]]:
            '''Settings for the Lambda execution environment in AWS IoT Greengrass .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-execution
            '''
            result = self._values.get("execution")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.ExecutionProperty"]], result)

        @builtins.property
        def resource_access_policies(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty"]]]]:
            '''A list of the `resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html>`_ in the group that the function can access, with the corresponding read-only or read-write permissions. The maximum is 10 resources.

            .. epigraph::

               This property applies only to Lambda functions that run in a Greengrass container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-resourceaccesspolicies
            '''
            result = self._values.get("resource_access_policies")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty"]]]], result)

        @builtins.property
        def variables(self) -> typing.Any:
            '''Environment variables for the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-variables
            '''
            result = self._values.get("variables")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersion.ExecutionProperty",
        jsii_struct_bases=[],
        name_mapping={"isolation_mode": "isolationMode", "run_as": "runAs"},
    )
    class ExecutionProperty:
        def __init__(
            self,
            *,
            isolation_mode: typing.Optional[builtins.str] = None,
            run_as: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinitionVersion.RunAsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration settings for the Lambda execution environment on the AWS IoT Greengrass core.

            In an AWS CloudFormation template, ``Execution`` is a property of the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property type for a function definition version and the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property type for a function.

            :param isolation_mode: The containerization that the Lambda function runs in. Valid values are ``GreengrassContainer`` or ``NoContainer`` . Typically, this is ``GreengrassContainer`` . For more information, see `Containerization <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-function-containerization>`_ in the *Developer Guide* . - When set on the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property of a function definition version, this setting is used as the default containerization for all Lambda functions in the function definition version. - When set on the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property of a function, this setting applies to the individual function and overrides the default. Omit this value to run the function with the default containerization. .. epigraph:: We recommend that you run in a Greengrass container unless your business case requires that you run without containerization.
            :param run_as: The user and group permissions used to run the Lambda function. Typically, this is the ggc_user and ggc_group. For more information, see `Run as <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-access-identity.html>`_ in the *Developer Guide* . - When set on the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property of a function definition version, this setting is used as the default access identity for all Lambda functions in the function definition version. - When set on the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property of a function, this setting applies to the individual function and overrides the default. You can override the user, group, or both. Omit this value to run the function with the default permissions. .. epigraph:: Running as the root user increases risks to your data and device. Do not run as root (UID/GID=0) unless your business case requires it. For more information and requirements, see `Running a Lambda Function as Root <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-running-as-root>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                execution_property = greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                    isolation_mode="isolationMode",
                    run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                        gid=123,
                        uid=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d250f03acfa6e718d9c76fc540c990c972324de4f76328354b14aa9eb0e6788)
                check_type(argname="argument isolation_mode", value=isolation_mode, expected_type=type_hints["isolation_mode"])
                check_type(argname="argument run_as", value=run_as, expected_type=type_hints["run_as"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if isolation_mode is not None:
                self._values["isolation_mode"] = isolation_mode
            if run_as is not None:
                self._values["run_as"] = run_as

        @builtins.property
        def isolation_mode(self) -> typing.Optional[builtins.str]:
            '''The containerization that the Lambda function runs in.

            Valid values are ``GreengrassContainer`` or ``NoContainer`` . Typically, this is ``GreengrassContainer`` . For more information, see `Containerization <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-function-containerization>`_ in the *Developer Guide* .

            - When set on the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property of a function definition version, this setting is used as the default containerization for all Lambda functions in the function definition version.
            - When set on the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property of a function, this setting applies to the individual function and overrides the default. Omit this value to run the function with the default containerization.

            .. epigraph::

               We recommend that you run in a Greengrass container unless your business case requires that you run without containerization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html#cfn-greengrass-functiondefinitionversion-execution-isolationmode
            '''
            result = self._values.get("isolation_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def run_as(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.RunAsProperty"]]:
            '''The user and group permissions used to run the Lambda function.

            Typically, this is the ggc_user and ggc_group. For more information, see `Run as <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-access-identity.html>`_ in the *Developer Guide* .

            - When set on the ```DefaultConfig`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html>`_ property of a function definition version, this setting is used as the default access identity for all Lambda functions in the function definition version.
            - When set on the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property of a function, this setting applies to the individual function and overrides the default. You can override the user, group, or both. Omit this value to run the function with the default permissions.

            .. epigraph::

               Running as the root user increases risks to your data and device. Do not run as root (UID/GID=0) unless your business case requires it. For more information and requirements, see `Running a Lambda Function as Root <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-running-as-root>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html#cfn-greengrass-functiondefinitionversion-execution-runas
            '''
            result = self._values.get("run_as")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.RunAsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersion.FunctionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encoding_type": "encodingType",
            "environment": "environment",
            "exec_args": "execArgs",
            "executable": "executable",
            "memory_size": "memorySize",
            "pinned": "pinned",
            "timeout": "timeout",
        },
    )
    class FunctionConfigurationProperty:
        def __init__(
            self,
            *,
            encoding_type: typing.Optional[builtins.str] = None,
            environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinitionVersion.EnvironmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            exec_args: typing.Optional[builtins.str] = None,
            executable: typing.Optional[builtins.str] = None,
            memory_size: typing.Optional[jsii.Number] = None,
            pinned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The group-specific configuration settings for a Lambda function.

            These settings configure the function's behavior in the Greengrass group. For more information, see `Controlling Execution of Greengrass Lambda Functions by Using Group-Specific Configuration <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``FunctionConfiguration`` is a property of the ```Function`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html>`_ property type.

            :param encoding_type: The expected encoding type of the input payload for the function. Valid values are ``json`` (default) and ``binary`` .
            :param environment: The environment configuration of the function.
            :param exec_args: The execution arguments.
            :param executable: The name of the function executable.
            :param memory_size: The memory size (in KB) required by the function. .. epigraph:: This property applies only to Lambda functions that run in a Greengrass container.
            :param pinned: Indicates whether the function is pinned (or *long-lived* ). Pinned functions start when the core starts and process all requests in the same container. The default value is false.
            :param timeout: The allowed execution time (in seconds) after which the function should terminate. For pinned functions, this timeout applies for each request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # variables: Any
                
                function_configuration_property = greengrass.CfnFunctionDefinitionVersion.FunctionConfigurationProperty(
                    encoding_type="encodingType",
                    environment=greengrass.CfnFunctionDefinitionVersion.EnvironmentProperty(
                        access_sysfs=False,
                        execution=greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                            isolation_mode="isolationMode",
                            run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                                gid=123,
                                uid=123
                            )
                        ),
                        resource_access_policies=[greengrass.CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty(
                            resource_id="resourceId",
                
                            # the properties below are optional
                            permission="permission"
                        )],
                        variables=variables
                    ),
                    exec_args="execArgs",
                    executable="executable",
                    memory_size=123,
                    pinned=False,
                    timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0305775d160fba73e4f75590e6bf752341fc5c40b45ed63434363b50709bf554)
                check_type(argname="argument encoding_type", value=encoding_type, expected_type=type_hints["encoding_type"])
                check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
                check_type(argname="argument exec_args", value=exec_args, expected_type=type_hints["exec_args"])
                check_type(argname="argument executable", value=executable, expected_type=type_hints["executable"])
                check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
                check_type(argname="argument pinned", value=pinned, expected_type=type_hints["pinned"])
                check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encoding_type is not None:
                self._values["encoding_type"] = encoding_type
            if environment is not None:
                self._values["environment"] = environment
            if exec_args is not None:
                self._values["exec_args"] = exec_args
            if executable is not None:
                self._values["executable"] = executable
            if memory_size is not None:
                self._values["memory_size"] = memory_size
            if pinned is not None:
                self._values["pinned"] = pinned
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def encoding_type(self) -> typing.Optional[builtins.str]:
            '''The expected encoding type of the input payload for the function.

            Valid values are ``json`` (default) and ``binary`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-encodingtype
            '''
            result = self._values.get("encoding_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.EnvironmentProperty"]]:
            '''The environment configuration of the function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.EnvironmentProperty"]], result)

        @builtins.property
        def exec_args(self) -> typing.Optional[builtins.str]:
            '''The execution arguments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-execargs
            '''
            result = self._values.get("exec_args")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def executable(self) -> typing.Optional[builtins.str]:
            '''The name of the function executable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-executable
            '''
            result = self._values.get("executable")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def memory_size(self) -> typing.Optional[jsii.Number]:
            '''The memory size (in KB) required by the function.

            .. epigraph::

               This property applies only to Lambda functions that run in a Greengrass container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-memorysize
            '''
            result = self._values.get("memory_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pinned(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the function is pinned (or *long-lived* ).

            Pinned functions start when the core starts and process all requests in the same container. The default value is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-pinned
            '''
            result = self._values.get("pinned")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''The allowed execution time (in seconds) after which the function should terminate.

            For pinned functions, this timeout applies for each request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersion.FunctionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_arn": "functionArn",
            "function_configuration": "functionConfiguration",
            "id": "id",
        },
    )
    class FunctionProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            function_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionDefinitionVersion.FunctionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            id: builtins.str,
        ) -> None:
            '''A function is a Lambda function that's referenced from an AWS IoT Greengrass group.

            The function is deployed to a Greengrass core where it runs locally. For more information, see `Run Lambda Functions on the AWS IoT Greengrass Core <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-functions.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Functions`` property of the ```AWS::Greengrass::FunctionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html>`_ resource contains a list of ``Function`` property types.

            :param function_arn: The Amazon Resource Name (ARN) of the alias (recommended) or version of the referenced Lambda function.
            :param function_configuration: The group-specific settings of the Lambda function. These settings configure the function's behavior in the Greengrass group.
            :param id: A descriptive or arbitrary ID for the function. This value must be unique within the function definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                # variables: Any
                
                function_property = greengrass.CfnFunctionDefinitionVersion.FunctionProperty(
                    function_arn="functionArn",
                    function_configuration=greengrass.CfnFunctionDefinitionVersion.FunctionConfigurationProperty(
                        encoding_type="encodingType",
                        environment=greengrass.CfnFunctionDefinitionVersion.EnvironmentProperty(
                            access_sysfs=False,
                            execution=greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                                isolation_mode="isolationMode",
                                run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                                    gid=123,
                                    uid=123
                                )
                            ),
                            resource_access_policies=[greengrass.CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty(
                                resource_id="resourceId",
                
                                # the properties below are optional
                                permission="permission"
                            )],
                            variables=variables
                        ),
                        exec_args="execArgs",
                        executable="executable",
                        memory_size=123,
                        pinned=False,
                        timeout=123
                    ),
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63a9205f2a39c9362a5f7f6b72de2b4c074656b9c7a7c287a91949ece94cf5dd)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
                check_type(argname="argument function_configuration", value=function_configuration, expected_type=type_hints["function_configuration"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_arn": function_arn,
                "function_configuration": function_configuration,
                "id": id,
            }

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the alias (recommended) or version of the referenced Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def function_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.FunctionConfigurationProperty"]:
            '''The group-specific settings of the Lambda function.

            These settings configure the function's behavior in the Greengrass group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-functionconfiguration
            '''
            result = self._values.get("function_configuration")
            assert result is not None, "Required property 'function_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunctionDefinitionVersion.FunctionConfigurationProperty"], result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the function.

            This value must be unique within the function definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_id": "resourceId", "permission": "permission"},
    )
    class ResourceAccessPolicyProperty:
        def __init__(
            self,
            *,
            resource_id: builtins.str,
            permission: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A list of the `resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html>`_ in the group that the function can access, with the corresponding read-only or read-write permissions. The maximum is 10 resources.

            .. epigraph::

               This property applies only to Lambda functions that run in a Greengrass container.

            In an AWS CloudFormation template, ``ResourceAccessPolicy`` is a property of the ```Environment`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html>`_ property type.

            :param resource_id: The ID of the resource. This ID is assigned to the resource when you create the resource definition.
            :param permission: The read-only or read-write access that the Lambda function has to the resource. Valid values are ``ro`` or ``rw`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_access_policy_property = greengrass.CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty(
                    resource_id="resourceId",
                
                    # the properties below are optional
                    permission="permission"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a0c05252ba2866efa6819404f70d8c46ab9150857916aa6aabac49f53006c7b)
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_id": resource_id,
            }
            if permission is not None:
                self._values["permission"] = permission

        @builtins.property
        def resource_id(self) -> builtins.str:
            '''The ID of the resource.

            This ID is assigned to the resource when you create the resource definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html#cfn-greengrass-functiondefinitionversion-resourceaccesspolicy-resourceid
            '''
            result = self._values.get("resource_id")
            assert result is not None, "Required property 'resource_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def permission(self) -> typing.Optional[builtins.str]:
            '''The read-only or read-write access that the Lambda function has to the resource.

            Valid values are ``ro`` or ``rw`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html#cfn-greengrass-functiondefinitionversion-resourceaccesspolicy-permission
            '''
            result = self._values.get("permission")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceAccessPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersion.RunAsProperty",
        jsii_struct_bases=[],
        name_mapping={"gid": "gid", "uid": "uid"},
    )
    class RunAsProperty:
        def __init__(
            self,
            *,
            gid: typing.Optional[jsii.Number] = None,
            uid: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The user and group permissions used to run the Lambda function.

            This setting overrides the default access identity that's specified for the group (by default, ggc_user and ggc_group). You can override the user, group, or both. For more information, see `Run as <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-access-identity.html>`_ in the *Developer Guide* .
            .. epigraph::

               Running as the root user increases risks to your data and device. Do not run as root (UID/GID=0) unless your business case requires it. For more information and requirements, see `Running a Lambda Function as Root <https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-running-as-root>`_ .

            In an AWS CloudFormation template, ``RunAs`` is a property of the ```Execution`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html>`_ property type.

            :param gid: The group ID whose permissions are used to run the Lambda function. You can use the ``getent group`` command on your core device to look up the group ID.
            :param uid: The user ID whose permissions are used to run the Lambda function. You can use the ``getent passwd`` command on your core device to look up the user ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                run_as_property = greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                    gid=123,
                    uid=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5ebc14c39db2ef6662e5e8568947f430b45c6b165cfdcb6f5bd1a30fcf649a1b)
                check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
                check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if gid is not None:
                self._values["gid"] = gid
            if uid is not None:
                self._values["uid"] = uid

        @builtins.property
        def gid(self) -> typing.Optional[jsii.Number]:
            '''The group ID whose permissions are used to run the Lambda function.

            You can use the ``getent group`` command on your core device to look up the group ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html#cfn-greengrass-functiondefinitionversion-runas-gid
            '''
            result = self._values.get("gid")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def uid(self) -> typing.Optional[jsii.Number]:
            '''The user ID whose permissions are used to run the Lambda function.

            You can use the ``getent passwd`` command on your core device to look up the user ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html#cfn-greengrass-functiondefinitionversion-runas-uid
            '''
            result = self._values.get("uid")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunAsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnFunctionDefinitionVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_definition_id": "functionDefinitionId",
        "functions": "functions",
        "default_config": "defaultConfig",
    },
)
class CfnFunctionDefinitionVersionProps:
    def __init__(
        self,
        *,
        function_definition_id: builtins.str,
        functions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.FunctionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.DefaultConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFunctionDefinitionVersion``.

        :param function_definition_id: The ID of the function definition associated with this version. This value is a GUID.
        :param functions: The functions in this version.
        :param default_config: The default configuration that applies to all Lambda functions in the group. Individual Lambda functions can override these settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # variables: Any
            
            cfn_function_definition_version_props = greengrass.CfnFunctionDefinitionVersionProps(
                function_definition_id="functionDefinitionId",
                functions=[greengrass.CfnFunctionDefinitionVersion.FunctionProperty(
                    function_arn="functionArn",
                    function_configuration=greengrass.CfnFunctionDefinitionVersion.FunctionConfigurationProperty(
                        encoding_type="encodingType",
                        environment=greengrass.CfnFunctionDefinitionVersion.EnvironmentProperty(
                            access_sysfs=False,
                            execution=greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                                isolation_mode="isolationMode",
                                run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                                    gid=123,
                                    uid=123
                                )
                            ),
                            resource_access_policies=[greengrass.CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty(
                                resource_id="resourceId",
            
                                # the properties below are optional
                                permission="permission"
                            )],
                            variables=variables
                        ),
                        exec_args="execArgs",
                        executable="executable",
                        memory_size=123,
                        pinned=False,
                        timeout=123
                    ),
                    id="id"
                )],
            
                # the properties below are optional
                default_config=greengrass.CfnFunctionDefinitionVersion.DefaultConfigProperty(
                    execution=greengrass.CfnFunctionDefinitionVersion.ExecutionProperty(
                        isolation_mode="isolationMode",
                        run_as=greengrass.CfnFunctionDefinitionVersion.RunAsProperty(
                            gid=123,
                            uid=123
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e693fe342b550c60e306daaf34fb60a94c43637b204bde675069e2c09f0356)
            check_type(argname="argument function_definition_id", value=function_definition_id, expected_type=type_hints["function_definition_id"])
            check_type(argname="argument functions", value=functions, expected_type=type_hints["functions"])
            check_type(argname="argument default_config", value=default_config, expected_type=type_hints["default_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_definition_id": function_definition_id,
            "functions": functions,
        }
        if default_config is not None:
            self._values["default_config"] = default_config

    @builtins.property
    def function_definition_id(self) -> builtins.str:
        '''The ID of the function definition associated with this version.

        This value is a GUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-functiondefinitionid
        '''
        result = self._values.get("function_definition_id")
        assert result is not None, "Required property 'function_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def functions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinitionVersion.FunctionProperty]]]:
        '''The functions in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-functions
        '''
        result = self._values.get("functions")
        assert result is not None, "Required property 'functions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinitionVersion.FunctionProperty]]], result)

    @builtins.property
    def default_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinitionVersion.DefaultConfigProperty]]:
        '''The default configuration that applies to all Lambda functions in the group.

        Individual Lambda functions can override these settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-defaultconfig
        '''
        result = self._values.get("default_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinitionVersion.DefaultConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionDefinitionVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnGroup",
):
    '''AWS IoT Greengrass seamlessly extends AWS to edge devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage.

    With AWS IoT Greengrass , connected devices can run AWS Lambda functions, execute predictions based on machine learning models, keep device data in sync, and communicate with other devices securely – even when not connected to the internet. For more information, see the `Developer Guide <https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html>`_ .
    .. epigraph::

       For AWS Region support, see `AWS CloudFormation Support for AWS IoT Greengrass <https://docs.aws.amazon.com/greengrass/latest/developerguide/cloudformation-support.html>`_ in the *Developer Guide* .

    The ``AWS::Greengrass::Group`` resource represents a group in AWS IoT Greengrass . In the AWS IoT Greengrass API, groups are used to organize your group versions.

    Groups can reference multiple group versions. All group versions must be associated with a group. A group version references a device definition version, subscription definition version, and other version types that contain the components you want to deploy to a Greengrass core device.

    To deploy a group version, the group version must reference a core definition version that contains one core. Other version types are optionally included, depending on your business need.
    .. epigraph::

       When you create a group, you can optionally include an initial group version. To associate a group version later, create a ```AWS::Greengrass::GroupVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html>`_ resource and specify the ID of this group.

       To change group components (such as devices, subscriptions, or functions), you must create new versions. This is because versions are immutable. For example, to add a function, you create a function definition version that contains the new function (and all other functions that you want to deploy). Then you create a group version that references the new function definition version (and all other version types that you want to deploy).

    *Deploying a Group Version*

    After you create the group version in your AWS CloudFormation template, you can deploy it using the ```aws greengrass create-deployment`` <https://docs.aws.amazon.com/greengrass/latest/apireference/createdeployment-post.html>`_ command in the AWS CLI or from the *Greengrass* node in the AWS IoT console. To deploy a group version, you must have a Greengrass service role associated with your AWS account . For more information, see `AWS CloudFormation Support for AWS IoT Greengrass <https://docs.aws.amazon.com/greengrass/latest/developerguide/cloudformation-support.html>`_ in the *Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # tags: Any
        
        cfn_group = greengrass.CfnGroup(self, "MyCfnGroup",
            name="name",
        
            # the properties below are optional
            initial_version=greengrass.CfnGroup.GroupVersionProperty(
                connector_definition_version_arn="connectorDefinitionVersionArn",
                core_definition_version_arn="coreDefinitionVersionArn",
                device_definition_version_arn="deviceDefinitionVersionArn",
                function_definition_version_arn="functionDefinitionVersionArn",
                logger_definition_version_arn="loggerDefinitionVersionArn",
                resource_definition_version_arn="resourceDefinitionVersionArn",
                subscription_definition_version_arn="subscriptionDefinitionVersionArn"
            ),
            role_arn="roleArn",
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGroup.GroupVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the group.
        :param initial_version: The group version to include when the group is created. A group version references the Amazon Resource Name (ARN) of a core definition version, device definition version, subscription definition version, and other version types. The group version must reference a core definition version that contains one core. Other version types are optionally included, depending on your business need. .. epigraph:: To associate a group version after the group is created, create an ```AWS::Greengrass::GroupVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html>`_ resource and specify the ID of this group.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role attached to the group. This role contains the permissions that Lambda functions and connectors use to interact with other AWS services.
        :param tags: Application-specific metadata to attach to the group. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726a7d2c4960c5df3ad6e991be61efa251e71f218d0d72f1df21a3c5903ebe7f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(
            name=name, initial_version=initial_version, role_arn=role_arn, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1154c99a9c32510d4c5f12de88ee6aa74b4b71171411ee6688346f3c78d26e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__371d9153ea3fc52290ce86f5a599394cc2955ebf44fd35dce75ed6aa04a4cb03)
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
        '''The ARN of the ``Group`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/groups/1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the ``Group`` , such as ``1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersionArn")
    def attr_latest_version_arn(self) -> builtins.str:
        '''The ARN of the last ``GroupVersion`` that was added to the ``Group`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/groups/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`` .

        :cloudformationAttribute: LatestVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the ``Group`` , such as ``MyGroup`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleArn")
    def attr_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that's attached to the ``Group`` , such as ``arn:aws:iam::  :role/role-name`` .

        :cloudformationAttribute: RoleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleAttachedAt")
    def attr_role_attached_at(self) -> builtins.str:
        '''The time (in milliseconds since the epoch) when the group role was attached to the ``Group`` .

        :cloudformationAttribute: RoleAttachedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleAttachedAt"))

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
        '''The name of the group.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea2b1b818ef0cc72e4ff310dbf9eae157f92e5c04d08514478628c08a3dc867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="initialVersion")
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGroup.GroupVersionProperty"]]:
        '''The group version to include when the group is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGroup.GroupVersionProperty"]], jsii.get(self, "initialVersion"))

    @initial_version.setter
    def initial_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGroup.GroupVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a38b6bf42dcdd50e398f34bf87a366c206fb7d56a14edcfa088d38beb0169bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVersion", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role attached to the group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6675e04cf0ab21e346afb29e4e19bde19ea87ea432acc7787de29c5be10f7aa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''Application-specific metadata to attach to the group.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf681fed500903d683fa2fe379335268fbe2011999bfef05177c39ea864332eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnGroup.GroupVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_definition_version_arn": "connectorDefinitionVersionArn",
            "core_definition_version_arn": "coreDefinitionVersionArn",
            "device_definition_version_arn": "deviceDefinitionVersionArn",
            "function_definition_version_arn": "functionDefinitionVersionArn",
            "logger_definition_version_arn": "loggerDefinitionVersionArn",
            "resource_definition_version_arn": "resourceDefinitionVersionArn",
            "subscription_definition_version_arn": "subscriptionDefinitionVersionArn",
        },
    )
    class GroupVersionProperty:
        def __init__(
            self,
            *,
            connector_definition_version_arn: typing.Optional[builtins.str] = None,
            core_definition_version_arn: typing.Optional[builtins.str] = None,
            device_definition_version_arn: typing.Optional[builtins.str] = None,
            function_definition_version_arn: typing.Optional[builtins.str] = None,
            logger_definition_version_arn: typing.Optional[builtins.str] = None,
            resource_definition_version_arn: typing.Optional[builtins.str] = None,
            subscription_definition_version_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A group version in AWS IoT Greengrass , which references of a core definition version, device definition version, subscription definition version, and other version types that contain the components you want to deploy to a Greengrass core device.

            The group version must reference a core definition version that contains one core. Other version types are optionally included, depending on your business need.

            In an AWS CloudFormation template, ``GroupVersion`` is the property type of the ``InitialVersion`` property in the ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ resource.

            :param connector_definition_version_arn: The Amazon Resource Name (ARN) of the connector definition version that contains the connectors you want to deploy with the group version.
            :param core_definition_version_arn: The ARN of the core definition version that contains the core you want to deploy with the group version. Currently, the core definition version can contain only one core.
            :param device_definition_version_arn: The ARN of the device definition version that contains the devices you want to deploy with the group version.
            :param function_definition_version_arn: The ARN of the function definition version that contains the functions you want to deploy with the group version.
            :param logger_definition_version_arn: The ARN of the logger definition version that contains the loggers you want to deploy with the group version.
            :param resource_definition_version_arn: The ARN of the resource definition version that contains the resources you want to deploy with the group version.
            :param subscription_definition_version_arn: The ARN of the subscription definition version that contains the subscriptions you want to deploy with the group version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                group_version_property = greengrass.CfnGroup.GroupVersionProperty(
                    connector_definition_version_arn="connectorDefinitionVersionArn",
                    core_definition_version_arn="coreDefinitionVersionArn",
                    device_definition_version_arn="deviceDefinitionVersionArn",
                    function_definition_version_arn="functionDefinitionVersionArn",
                    logger_definition_version_arn="loggerDefinitionVersionArn",
                    resource_definition_version_arn="resourceDefinitionVersionArn",
                    subscription_definition_version_arn="subscriptionDefinitionVersionArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__23017f69761595410cb920f0188f7bac8a8a1c92bdabee3f081b74455da416fb)
                check_type(argname="argument connector_definition_version_arn", value=connector_definition_version_arn, expected_type=type_hints["connector_definition_version_arn"])
                check_type(argname="argument core_definition_version_arn", value=core_definition_version_arn, expected_type=type_hints["core_definition_version_arn"])
                check_type(argname="argument device_definition_version_arn", value=device_definition_version_arn, expected_type=type_hints["device_definition_version_arn"])
                check_type(argname="argument function_definition_version_arn", value=function_definition_version_arn, expected_type=type_hints["function_definition_version_arn"])
                check_type(argname="argument logger_definition_version_arn", value=logger_definition_version_arn, expected_type=type_hints["logger_definition_version_arn"])
                check_type(argname="argument resource_definition_version_arn", value=resource_definition_version_arn, expected_type=type_hints["resource_definition_version_arn"])
                check_type(argname="argument subscription_definition_version_arn", value=subscription_definition_version_arn, expected_type=type_hints["subscription_definition_version_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connector_definition_version_arn is not None:
                self._values["connector_definition_version_arn"] = connector_definition_version_arn
            if core_definition_version_arn is not None:
                self._values["core_definition_version_arn"] = core_definition_version_arn
            if device_definition_version_arn is not None:
                self._values["device_definition_version_arn"] = device_definition_version_arn
            if function_definition_version_arn is not None:
                self._values["function_definition_version_arn"] = function_definition_version_arn
            if logger_definition_version_arn is not None:
                self._values["logger_definition_version_arn"] = logger_definition_version_arn
            if resource_definition_version_arn is not None:
                self._values["resource_definition_version_arn"] = resource_definition_version_arn
            if subscription_definition_version_arn is not None:
                self._values["subscription_definition_version_arn"] = subscription_definition_version_arn

        @builtins.property
        def connector_definition_version_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the connector definition version that contains the connectors you want to deploy with the group version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-connectordefinitionversionarn
            '''
            result = self._values.get("connector_definition_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def core_definition_version_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the core definition version that contains the core you want to deploy with the group version.

            Currently, the core definition version can contain only one core.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-coredefinitionversionarn
            '''
            result = self._values.get("core_definition_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_definition_version_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the device definition version that contains the devices you want to deploy with the group version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-devicedefinitionversionarn
            '''
            result = self._values.get("device_definition_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def function_definition_version_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the function definition version that contains the functions you want to deploy with the group version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-functiondefinitionversionarn
            '''
            result = self._values.get("function_definition_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def logger_definition_version_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the logger definition version that contains the loggers you want to deploy with the group version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-loggerdefinitionversionarn
            '''
            result = self._values.get("logger_definition_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_definition_version_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the resource definition version that contains the resources you want to deploy with the group version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-resourcedefinitionversionarn
            '''
            result = self._values.get("resource_definition_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subscription_definition_version_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the subscription definition version that contains the subscriptions you want to deploy with the group version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-subscriptiondefinitionversionarn
            '''
            result = self._values.get("subscription_definition_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "initial_version": "initialVersion",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.GroupVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnGroup``.

        :param name: The name of the group.
        :param initial_version: The group version to include when the group is created. A group version references the Amazon Resource Name (ARN) of a core definition version, device definition version, subscription definition version, and other version types. The group version must reference a core definition version that contains one core. Other version types are optionally included, depending on your business need. .. epigraph:: To associate a group version after the group is created, create an ```AWS::Greengrass::GroupVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html>`_ resource and specify the ID of this group.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role attached to the group. This role contains the permissions that Lambda functions and connectors use to interact with other AWS services.
        :param tags: Application-specific metadata to attach to the group. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # tags: Any
            
            cfn_group_props = greengrass.CfnGroupProps(
                name="name",
            
                # the properties below are optional
                initial_version=greengrass.CfnGroup.GroupVersionProperty(
                    connector_definition_version_arn="connectorDefinitionVersionArn",
                    core_definition_version_arn="coreDefinitionVersionArn",
                    device_definition_version_arn="deviceDefinitionVersionArn",
                    function_definition_version_arn="functionDefinitionVersionArn",
                    logger_definition_version_arn="loggerDefinitionVersionArn",
                    resource_definition_version_arn="resourceDefinitionVersionArn",
                    subscription_definition_version_arn="subscriptionDefinitionVersionArn"
                ),
                role_arn="roleArn",
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__296d900be2eff5ceb398f72dfd0a58896e12fd04dd28f102a076e92f456cb9a4)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument initial_version", value=initial_version, expected_type=type_hints["initial_version"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if initial_version is not None:
            self._values["initial_version"] = initial_version
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGroup.GroupVersionProperty]]:
        '''The group version to include when the group is created.

        A group version references the Amazon Resource Name (ARN) of a core definition version, device definition version, subscription definition version, and other version types. The group version must reference a core definition version that contains one core. Other version types are optionally included, depending on your business need.
        .. epigraph::

           To associate a group version after the group is created, create an ```AWS::Greengrass::GroupVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html>`_ resource and specify the ID of this group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-initialversion
        '''
        result = self._values.get("initial_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGroup.GroupVersionProperty]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role attached to the group.

        This role contains the permissions that Lambda functions and connectors use to interact with other AWS services.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Application-specific metadata to attach to the group.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGroupVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnGroupVersion",
):
    '''The ``AWS::Greengrass::GroupVersion`` resource represents a group version in AWS IoT Greengrass .

    A group version references a core definition version, device definition version, subscription definition version, and other version types that contain the components you want to deploy to a Greengrass core device. The group version must reference a core definition version that contains one core. Other version types are optionally included, depending on your business need.
    .. epigraph::

       To create a group version, you must specify the ID of the group that you want to associate with the version. For information about creating a group, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        cfn_group_version = greengrass.CfnGroupVersion(self, "MyCfnGroupVersion",
            group_id="groupId",
        
            # the properties below are optional
            connector_definition_version_arn="connectorDefinitionVersionArn",
            core_definition_version_arn="coreDefinitionVersionArn",
            device_definition_version_arn="deviceDefinitionVersionArn",
            function_definition_version_arn="functionDefinitionVersionArn",
            logger_definition_version_arn="loggerDefinitionVersionArn",
            resource_definition_version_arn="resourceDefinitionVersionArn",
            subscription_definition_version_arn="subscriptionDefinitionVersionArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_id: builtins.str,
        connector_definition_version_arn: typing.Optional[builtins.str] = None,
        core_definition_version_arn: typing.Optional[builtins.str] = None,
        device_definition_version_arn: typing.Optional[builtins.str] = None,
        function_definition_version_arn: typing.Optional[builtins.str] = None,
        logger_definition_version_arn: typing.Optional[builtins.str] = None,
        resource_definition_version_arn: typing.Optional[builtins.str] = None,
        subscription_definition_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param group_id: The ID of the group associated with this version. This value is a GUID.
        :param connector_definition_version_arn: The Amazon Resource Name (ARN) of the connector definition version that contains the connectors you want to deploy with the group version.
        :param core_definition_version_arn: The ARN of the core definition version that contains the core you want to deploy with the group version. Currently, the core definition version can contain only one core.
        :param device_definition_version_arn: The ARN of the device definition version that contains the devices you want to deploy with the group version.
        :param function_definition_version_arn: The ARN of the function definition version that contains the functions you want to deploy with the group version.
        :param logger_definition_version_arn: The ARN of the logger definition version that contains the loggers you want to deploy with the group version.
        :param resource_definition_version_arn: The ARN of the resource definition version that contains the resources you want to deploy with the group version.
        :param subscription_definition_version_arn: The ARN of the subscription definition version that contains the subscriptions you want to deploy with the group version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e429513d4ed5c36de946aa9233f1743627bcb10cb35191a8cf2b05862bf588)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupVersionProps(
            group_id=group_id,
            connector_definition_version_arn=connector_definition_version_arn,
            core_definition_version_arn=core_definition_version_arn,
            device_definition_version_arn=device_definition_version_arn,
            function_definition_version_arn=function_definition_version_arn,
            logger_definition_version_arn=logger_definition_version_arn,
            resource_definition_version_arn=resource_definition_version_arn,
            subscription_definition_version_arn=subscription_definition_version_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2069ae3c84e6655780c7b21f27d46fb1bee9a88231128d102cc86e616b776fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__00e6e203e326396ee46b6f09d4950a4f2a60460aab9dd7801a5e998d496f282a)
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
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        '''The ID of the group associated with this version.'''
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b70513b04a0647c95bbd78b71c611749688212d95d6b7f6be24e153474ced833)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="connectorDefinitionVersionArn")
    def connector_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the connector definition version that contains the connectors you want to deploy with the group version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorDefinitionVersionArn"))

    @connector_definition_version_arn.setter
    def connector_definition_version_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b4083383be53e8192919e7978982b4c98f55ff47f025a1a51181578579b3852)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorDefinitionVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="coreDefinitionVersionArn")
    def core_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the core definition version that contains the core you want to deploy with the group version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreDefinitionVersionArn"))

    @core_definition_version_arn.setter
    def core_definition_version_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64b7407ff4176f922aa431270cee22c78db47ad08a470b616f3102fe257bdb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreDefinitionVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="deviceDefinitionVersionArn")
    def device_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the device definition version that contains the devices you want to deploy with the group version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceDefinitionVersionArn"))

    @device_definition_version_arn.setter
    def device_definition_version_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af68e21601bf6750c71f6f0c2bc6538974bed68a360dd4d6148cec732594fb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceDefinitionVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="functionDefinitionVersionArn")
    def function_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the function definition version that contains the functions you want to deploy with the group version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionDefinitionVersionArn"))

    @function_definition_version_arn.setter
    def function_definition_version_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bafc0081999bcf69f5529249f5611a5bfac796128da383e18f805601ef9f7d1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionDefinitionVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="loggerDefinitionVersionArn")
    def logger_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the logger definition version that contains the loggers you want to deploy with the group version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggerDefinitionVersionArn"))

    @logger_definition_version_arn.setter
    def logger_definition_version_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e34a3066bf41e65e71062cbc53c28ee0f3c8407b337545091f2f03096c48c2aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggerDefinitionVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="resourceDefinitionVersionArn")
    def resource_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the resource definition version that contains the resources you want to deploy with the group version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceDefinitionVersionArn"))

    @resource_definition_version_arn.setter
    def resource_definition_version_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a37b5dcc0ee3133f870c3a3fe994fa624423839bc6ae69bf0187a55c1045179)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceDefinitionVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionDefinitionVersionArn")
    def subscription_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the subscription definition version that contains the subscriptions you want to deploy with the group version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionDefinitionVersionArn"))

    @subscription_definition_version_arn.setter
    def subscription_definition_version_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__401c05e2b55805214eb63cf50bc055afc162c24db366d22d1d8583f411101e56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionDefinitionVersionArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnGroupVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_id": "groupId",
        "connector_definition_version_arn": "connectorDefinitionVersionArn",
        "core_definition_version_arn": "coreDefinitionVersionArn",
        "device_definition_version_arn": "deviceDefinitionVersionArn",
        "function_definition_version_arn": "functionDefinitionVersionArn",
        "logger_definition_version_arn": "loggerDefinitionVersionArn",
        "resource_definition_version_arn": "resourceDefinitionVersionArn",
        "subscription_definition_version_arn": "subscriptionDefinitionVersionArn",
    },
)
class CfnGroupVersionProps:
    def __init__(
        self,
        *,
        group_id: builtins.str,
        connector_definition_version_arn: typing.Optional[builtins.str] = None,
        core_definition_version_arn: typing.Optional[builtins.str] = None,
        device_definition_version_arn: typing.Optional[builtins.str] = None,
        function_definition_version_arn: typing.Optional[builtins.str] = None,
        logger_definition_version_arn: typing.Optional[builtins.str] = None,
        resource_definition_version_arn: typing.Optional[builtins.str] = None,
        subscription_definition_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroupVersion``.

        :param group_id: The ID of the group associated with this version. This value is a GUID.
        :param connector_definition_version_arn: The Amazon Resource Name (ARN) of the connector definition version that contains the connectors you want to deploy with the group version.
        :param core_definition_version_arn: The ARN of the core definition version that contains the core you want to deploy with the group version. Currently, the core definition version can contain only one core.
        :param device_definition_version_arn: The ARN of the device definition version that contains the devices you want to deploy with the group version.
        :param function_definition_version_arn: The ARN of the function definition version that contains the functions you want to deploy with the group version.
        :param logger_definition_version_arn: The ARN of the logger definition version that contains the loggers you want to deploy with the group version.
        :param resource_definition_version_arn: The ARN of the resource definition version that contains the resources you want to deploy with the group version.
        :param subscription_definition_version_arn: The ARN of the subscription definition version that contains the subscriptions you want to deploy with the group version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            cfn_group_version_props = greengrass.CfnGroupVersionProps(
                group_id="groupId",
            
                # the properties below are optional
                connector_definition_version_arn="connectorDefinitionVersionArn",
                core_definition_version_arn="coreDefinitionVersionArn",
                device_definition_version_arn="deviceDefinitionVersionArn",
                function_definition_version_arn="functionDefinitionVersionArn",
                logger_definition_version_arn="loggerDefinitionVersionArn",
                resource_definition_version_arn="resourceDefinitionVersionArn",
                subscription_definition_version_arn="subscriptionDefinitionVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3002e50fbbeb611ff50e6124b7f721785d0d1114fac032b39ef5434324657b48)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument connector_definition_version_arn", value=connector_definition_version_arn, expected_type=type_hints["connector_definition_version_arn"])
            check_type(argname="argument core_definition_version_arn", value=core_definition_version_arn, expected_type=type_hints["core_definition_version_arn"])
            check_type(argname="argument device_definition_version_arn", value=device_definition_version_arn, expected_type=type_hints["device_definition_version_arn"])
            check_type(argname="argument function_definition_version_arn", value=function_definition_version_arn, expected_type=type_hints["function_definition_version_arn"])
            check_type(argname="argument logger_definition_version_arn", value=logger_definition_version_arn, expected_type=type_hints["logger_definition_version_arn"])
            check_type(argname="argument resource_definition_version_arn", value=resource_definition_version_arn, expected_type=type_hints["resource_definition_version_arn"])
            check_type(argname="argument subscription_definition_version_arn", value=subscription_definition_version_arn, expected_type=type_hints["subscription_definition_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
        }
        if connector_definition_version_arn is not None:
            self._values["connector_definition_version_arn"] = connector_definition_version_arn
        if core_definition_version_arn is not None:
            self._values["core_definition_version_arn"] = core_definition_version_arn
        if device_definition_version_arn is not None:
            self._values["device_definition_version_arn"] = device_definition_version_arn
        if function_definition_version_arn is not None:
            self._values["function_definition_version_arn"] = function_definition_version_arn
        if logger_definition_version_arn is not None:
            self._values["logger_definition_version_arn"] = logger_definition_version_arn
        if resource_definition_version_arn is not None:
            self._values["resource_definition_version_arn"] = resource_definition_version_arn
        if subscription_definition_version_arn is not None:
            self._values["subscription_definition_version_arn"] = subscription_definition_version_arn

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The ID of the group associated with this version.

        This value is a GUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-groupid
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the connector definition version that contains the connectors you want to deploy with the group version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-connectordefinitionversionarn
        '''
        result = self._values.get("connector_definition_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the core definition version that contains the core you want to deploy with the group version.

        Currently, the core definition version can contain only one core.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-coredefinitionversionarn
        '''
        result = self._values.get("core_definition_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the device definition version that contains the devices you want to deploy with the group version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-devicedefinitionversionarn
        '''
        result = self._values.get("device_definition_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the function definition version that contains the functions you want to deploy with the group version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-functiondefinitionversionarn
        '''
        result = self._values.get("function_definition_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logger_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the logger definition version that contains the loggers you want to deploy with the group version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-loggerdefinitionversionarn
        '''
        result = self._values.get("logger_definition_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the resource definition version that contains the resources you want to deploy with the group version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-resourcedefinitionversionarn
        '''
        result = self._values.get("resource_definition_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_definition_version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the subscription definition version that contains the subscriptions you want to deploy with the group version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-subscriptiondefinitionversionarn
        '''
        result = self._values.get("subscription_definition_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLoggerDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnLoggerDefinition",
):
    '''The ``AWS::Greengrass::LoggerDefinition`` resource represents a logger definition for AWS IoT Greengrass .

    Logger definitions are used to organize your logger definition versions.

    Logger definitions can reference multiple logger definition versions. All logger definition versions must be associated with a logger definition. Each logger definition version can contain one or more loggers.
    .. epigraph::

       When you create a logger definition, you can optionally include an initial logger definition version. To associate a logger definition version later, create an ```AWS::Greengrass::LoggerDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html>`_ resource and specify the ID of this logger definition.

       After you create the logger definition version that contains the loggers you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # tags: Any
        
        cfn_logger_definition = greengrass.CfnLoggerDefinition(self, "MyCfnLoggerDefinition",
            name="name",
        
            # the properties below are optional
            initial_version=greengrass.CfnLoggerDefinition.LoggerDefinitionVersionProperty(
                loggers=[greengrass.CfnLoggerDefinition.LoggerProperty(
                    component="component",
                    id="id",
                    level="level",
                    type="type",
        
                    # the properties below are optional
                    space=123
                )]
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggerDefinition.LoggerDefinitionVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the logger definition.
        :param initial_version: The logger definition version to include when the logger definition is created. A logger definition version contains a list of ```logger`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html>`_ property types. .. epigraph:: To associate a logger definition version after the logger definition is created, create an ```AWS::Greengrass::LoggerDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html>`_ resource and specify the ID of this logger definition.
        :param tags: Application-specific metadata to attach to the logger definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3141ac6c65d7407c94dc3062e91bf204de61524d95c83b87b6aab3da0639d32)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoggerDefinitionProps(
            name=name, initial_version=initial_version, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ca6d7f3da4fbad4f376abd5d28521fed1cf98cbc7b1bdecf6ba568a679007af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b123a6c4bbc3ff9b8ce1479c01e3e2a438c7ef1a70dd2ccf41371497b257205)
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
        '''The Amazon Resource Name (ARN) of the ``LoggerDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/loggers/1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the ``LoggerDefinition`` , such as ``1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersionArn")
    def attr_latest_version_arn(self) -> builtins.str:
        '''The ARN of the last ``LoggerDefinitionVersion`` that was added to the ``LoggerDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/loggers/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`` .

        :cloudformationAttribute: LatestVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the ``LoggerDefinition`` , such as ``MyLoggerDefinition`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''The name of the logger definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03643a56201d8ee41ec6cb2d06bf4a744b44f9e140baade1eee0f8923f4de100)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="initialVersion")
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggerDefinition.LoggerDefinitionVersionProperty"]]:
        '''The logger definition version to include when the logger definition is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggerDefinition.LoggerDefinitionVersionProperty"]], jsii.get(self, "initialVersion"))

    @initial_version.setter
    def initial_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggerDefinition.LoggerDefinitionVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d933992b8def94152adabe1624210ae1c6c2ac626a5a9fd2af376a7f9128d123)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''Application-specific metadata to attach to the logger definition.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1467bdc61b875959389bcefa758a86026e2fb80e0b9db5da7327a4e0b2c1c6b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnLoggerDefinition.LoggerDefinitionVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"loggers": "loggers"},
    )
    class LoggerDefinitionVersionProperty:
        def __init__(
            self,
            *,
            loggers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggerDefinition.LoggerProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A logger definition version contains a list of `loggers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html>`_ .

            .. epigraph::

               After you create a logger definition version that contains the loggers you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

            In an AWS CloudFormation template, ``LoggerDefinitionVersion`` is the property type of the ``InitialVersion`` property in the ```AWS::Greengrass::LoggerDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html>`_ resource.

            :param loggers: The loggers in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                logger_definition_version_property = greengrass.CfnLoggerDefinition.LoggerDefinitionVersionProperty(
                    loggers=[greengrass.CfnLoggerDefinition.LoggerProperty(
                        component="component",
                        id="id",
                        level="level",
                        type="type",
                
                        # the properties below are optional
                        space=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__afb77b1dd70ac4fe4579018e45f452bb02bc14d56a2ce5d000c6bd4cc542d183)
                check_type(argname="argument loggers", value=loggers, expected_type=type_hints["loggers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "loggers": loggers,
            }

        @builtins.property
        def loggers(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLoggerDefinition.LoggerProperty"]]]:
            '''The loggers in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html#cfn-greengrass-loggerdefinition-loggerdefinitionversion-loggers
            '''
            result = self._values.get("loggers")
            assert result is not None, "Required property 'loggers' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLoggerDefinition.LoggerProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggerDefinitionVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnLoggerDefinition.LoggerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component": "component",
            "id": "id",
            "level": "level",
            "type": "type",
            "space": "space",
        },
    )
    class LoggerProperty:
        def __init__(
            self,
            *,
            component: builtins.str,
            id: builtins.str,
            level: builtins.str,
            type: builtins.str,
            space: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A logger represents logging settings for the AWS IoT Greengrass group, which can be stored in CloudWatch and the local file system of your core device.

            All log entries include a timestamp, log level, and information about the event. For more information, see `Monitoring with AWS IoT Greengrass Logs <https://docs.aws.amazon.com/greengrass/latest/developerguide/greengrass-logs-overview.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Loggers`` property of the ```LoggerDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html>`_ property type contains a list of ``Logger`` property types.

            :param component: The source of the log event. Valid values are ``GreengrassSystem`` or ``Lambda`` . When ``GreengrassSystem`` is used, events from Greengrass system components are logged. When ``Lambda`` is used, events from user-defined Lambda functions are logged.
            :param id: A descriptive or arbitrary ID for the logger. This value must be unique within the logger definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param level: The log-level threshold. Log events below this threshold are filtered out and aren't stored. Valid values are ``DEBUG`` , ``INFO`` (recommended), ``WARN`` , ``ERROR`` , or ``FATAL`` .
            :param type: The storage mechanism for log events. Valid values are ``FileSystem`` or ``AWSCloudWatch`` . When ``AWSCloudWatch`` is used, log events are sent to CloudWatch Logs . When ``FileSystem`` is used, log events are stored on the local file system.
            :param space: The amount of file space (in KB) to use when writing logs to the local file system. This property does not apply for CloudWatch Logs .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                logger_property = greengrass.CfnLoggerDefinition.LoggerProperty(
                    component="component",
                    id="id",
                    level="level",
                    type="type",
                
                    # the properties below are optional
                    space=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ef56df2cb15dd1d03dc55bf6372cddbfc94e06fb51a6d1a1422c713d37dd808c)
                check_type(argname="argument component", value=component, expected_type=type_hints["component"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument space", value=space, expected_type=type_hints["space"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "component": component,
                "id": id,
                "level": level,
                "type": type,
            }
            if space is not None:
                self._values["space"] = space

        @builtins.property
        def component(self) -> builtins.str:
            '''The source of the log event.

            Valid values are ``GreengrassSystem`` or ``Lambda`` . When ``GreengrassSystem`` is used, events from Greengrass system components are logged. When ``Lambda`` is used, events from user-defined Lambda functions are logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-component
            '''
            result = self._values.get("component")
            assert result is not None, "Required property 'component' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the logger.

            This value must be unique within the logger definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def level(self) -> builtins.str:
            '''The log-level threshold.

            Log events below this threshold are filtered out and aren't stored. Valid values are ``DEBUG`` , ``INFO`` (recommended), ``WARN`` , ``ERROR`` , or ``FATAL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-level
            '''
            result = self._values.get("level")
            assert result is not None, "Required property 'level' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The storage mechanism for log events.

            Valid values are ``FileSystem`` or ``AWSCloudWatch`` . When ``AWSCloudWatch`` is used, log events are sent to CloudWatch Logs . When ``FileSystem`` is used, log events are stored on the local file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def space(self) -> typing.Optional[jsii.Number]:
            '''The amount of file space (in KB) to use when writing logs to the local file system.

            This property does not apply for CloudWatch Logs .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-space
            '''
            result = self._values.get("space")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnLoggerDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "initial_version": "initialVersion", "tags": "tags"},
)
class CfnLoggerDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggerDefinition.LoggerDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnLoggerDefinition``.

        :param name: The name of the logger definition.
        :param initial_version: The logger definition version to include when the logger definition is created. A logger definition version contains a list of ```logger`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html>`_ property types. .. epigraph:: To associate a logger definition version after the logger definition is created, create an ```AWS::Greengrass::LoggerDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html>`_ resource and specify the ID of this logger definition.
        :param tags: Application-specific metadata to attach to the logger definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # tags: Any
            
            cfn_logger_definition_props = greengrass.CfnLoggerDefinitionProps(
                name="name",
            
                # the properties below are optional
                initial_version=greengrass.CfnLoggerDefinition.LoggerDefinitionVersionProperty(
                    loggers=[greengrass.CfnLoggerDefinition.LoggerProperty(
                        component="component",
                        id="id",
                        level="level",
                        type="type",
            
                        # the properties below are optional
                        space=123
                    )]
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__170725663bf1c1d04ae4208595550913d0157b3edd62f4ff14920f4acbfe3707)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument initial_version", value=initial_version, expected_type=type_hints["initial_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if initial_version is not None:
            self._values["initial_version"] = initial_version
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the logger definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLoggerDefinition.LoggerDefinitionVersionProperty]]:
        '''The logger definition version to include when the logger definition is created.

        A logger definition version contains a list of ```logger`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html>`_ property types.
        .. epigraph::

           To associate a logger definition version after the logger definition is created, create an ```AWS::Greengrass::LoggerDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html>`_ resource and specify the ID of this logger definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-initialversion
        '''
        result = self._values.get("initial_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLoggerDefinition.LoggerDefinitionVersionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Application-specific metadata to attach to the logger definition.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoggerDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLoggerDefinitionVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnLoggerDefinitionVersion",
):
    '''The ``AWS::Greengrass::LoggerDefinitionVersion`` resource represents a logger definition version for AWS IoT Greengrass .

    A logger definition version contains a list of loggers.
    .. epigraph::

       To create a logger definition version, you must specify the ID of the logger definition that you want to associate with the version. For information about creating a logger definition, see ```AWS::Greengrass::LoggerDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html>`_ .

       After you create a logger definition version that contains the loggers you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        cfn_logger_definition_version = greengrass.CfnLoggerDefinitionVersion(self, "MyCfnLoggerDefinitionVersion",
            logger_definition_id="loggerDefinitionId",
            loggers=[greengrass.CfnLoggerDefinitionVersion.LoggerProperty(
                component="component",
                id="id",
                level="level",
                type="type",
        
                # the properties below are optional
                space=123
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        logger_definition_id: builtins.str,
        loggers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggerDefinitionVersion.LoggerProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param logger_definition_id: The ID of the logger definition associated with this version. This value is a GUID.
        :param loggers: The loggers in this version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb45ce0812f07c5afc2310bc7a288eff7e5cdc4a5609d10f2a19f5b87faf7fe5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoggerDefinitionVersionProps(
            logger_definition_id=logger_definition_id, loggers=loggers
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e52fdc9bf427c5c69aa25405bc527eac098df7759f0f8a65d64cf2ac634260dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7a42b772a8bb7406067e698e43fd8f7d878cfc6b68255652cf2e0940da66a4f)
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
    @jsii.member(jsii_name="loggerDefinitionId")
    def logger_definition_id(self) -> builtins.str:
        '''The ID of the logger definition associated with this version.'''
        return typing.cast(builtins.str, jsii.get(self, "loggerDefinitionId"))

    @logger_definition_id.setter
    def logger_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dccc4692452b48425650c13195e73d6c200e1a8087f73abc40b4266aa7098102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggerDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="loggers")
    def loggers(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLoggerDefinitionVersion.LoggerProperty"]]]:
        '''The loggers in this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLoggerDefinitionVersion.LoggerProperty"]]], jsii.get(self, "loggers"))

    @loggers.setter
    def loggers(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLoggerDefinitionVersion.LoggerProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__935a7882eea62e6e59dbe2f8f1f89290502193c1dc3234cdc82edf49948aac83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggers", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnLoggerDefinitionVersion.LoggerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component": "component",
            "id": "id",
            "level": "level",
            "type": "type",
            "space": "space",
        },
    )
    class LoggerProperty:
        def __init__(
            self,
            *,
            component: builtins.str,
            id: builtins.str,
            level: builtins.str,
            type: builtins.str,
            space: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A logger represents logging settings for the AWS IoT Greengrass group, which can be stored in CloudWatch and the local file system of your core device.

            All log entries include a timestamp, log level, and information about the event. For more information, see `Monitoring with AWS IoT Greengrass Logs <https://docs.aws.amazon.com/greengrass/latest/developerguide/greengrass-logs-overview.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Loggers`` property of the ```AWS::Greengrass::LoggerDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html>`_ resource contains a list of ``Logger`` property types.

            :param component: The source of the log event. Valid values are ``GreengrassSystem`` or ``Lambda`` . When ``GreengrassSystem`` is used, events from Greengrass system components are logged. When ``Lambda`` is used, events from user-defined Lambda functions are logged.
            :param id: A descriptive or arbitrary ID for the logger. This value must be unique within the logger definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param level: The log-level threshold. Log events below this threshold are filtered out and aren't stored. Valid values are ``DEBUG`` , ``INFO`` (recommended), ``WARN`` , ``ERROR`` , or ``FATAL`` .
            :param type: The storage mechanism for log events. Valid values are ``FileSystem`` or ``AWSCloudWatch`` . When ``AWSCloudWatch`` is used, log events are sent to CloudWatch Logs . When ``FileSystem`` is used, log events are stored on the local file system.
            :param space: The amount of file space (in KB) to use when writing logs to the local file system. This property does not apply for CloudWatch Logs .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                logger_property = greengrass.CfnLoggerDefinitionVersion.LoggerProperty(
                    component="component",
                    id="id",
                    level="level",
                    type="type",
                
                    # the properties below are optional
                    space=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__17bd21c4fd76afa67a356eb02e70cf8770d286a8abba3a95fc65604a3e4ca18f)
                check_type(argname="argument component", value=component, expected_type=type_hints["component"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument space", value=space, expected_type=type_hints["space"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "component": component,
                "id": id,
                "level": level,
                "type": type,
            }
            if space is not None:
                self._values["space"] = space

        @builtins.property
        def component(self) -> builtins.str:
            '''The source of the log event.

            Valid values are ``GreengrassSystem`` or ``Lambda`` . When ``GreengrassSystem`` is used, events from Greengrass system components are logged. When ``Lambda`` is used, events from user-defined Lambda functions are logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-component
            '''
            result = self._values.get("component")
            assert result is not None, "Required property 'component' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the logger.

            This value must be unique within the logger definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def level(self) -> builtins.str:
            '''The log-level threshold.

            Log events below this threshold are filtered out and aren't stored. Valid values are ``DEBUG`` , ``INFO`` (recommended), ``WARN`` , ``ERROR`` , or ``FATAL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-level
            '''
            result = self._values.get("level")
            assert result is not None, "Required property 'level' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The storage mechanism for log events.

            Valid values are ``FileSystem`` or ``AWSCloudWatch`` . When ``AWSCloudWatch`` is used, log events are sent to CloudWatch Logs . When ``FileSystem`` is used, log events are stored on the local file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def space(self) -> typing.Optional[jsii.Number]:
            '''The amount of file space (in KB) to use when writing logs to the local file system.

            This property does not apply for CloudWatch Logs .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-space
            '''
            result = self._values.get("space")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnLoggerDefinitionVersionProps",
    jsii_struct_bases=[],
    name_mapping={"logger_definition_id": "loggerDefinitionId", "loggers": "loggers"},
)
class CfnLoggerDefinitionVersionProps:
    def __init__(
        self,
        *,
        logger_definition_id: builtins.str,
        loggers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggerDefinitionVersion.LoggerProperty, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnLoggerDefinitionVersion``.

        :param logger_definition_id: The ID of the logger definition associated with this version. This value is a GUID.
        :param loggers: The loggers in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            cfn_logger_definition_version_props = greengrass.CfnLoggerDefinitionVersionProps(
                logger_definition_id="loggerDefinitionId",
                loggers=[greengrass.CfnLoggerDefinitionVersion.LoggerProperty(
                    component="component",
                    id="id",
                    level="level",
                    type="type",
            
                    # the properties below are optional
                    space=123
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a55ca993c275a44b98675ba3424e4e63162b645c01b9f63544a74a467b4060a7)
            check_type(argname="argument logger_definition_id", value=logger_definition_id, expected_type=type_hints["logger_definition_id"])
            check_type(argname="argument loggers", value=loggers, expected_type=type_hints["loggers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "logger_definition_id": logger_definition_id,
            "loggers": loggers,
        }

    @builtins.property
    def logger_definition_id(self) -> builtins.str:
        '''The ID of the logger definition associated with this version.

        This value is a GUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html#cfn-greengrass-loggerdefinitionversion-loggerdefinitionid
        '''
        result = self._values.get("logger_definition_id")
        assert result is not None, "Required property 'logger_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def loggers(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLoggerDefinitionVersion.LoggerProperty]]]:
        '''The loggers in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html#cfn-greengrass-loggerdefinitionversion-loggers
        '''
        result = self._values.get("loggers")
        assert result is not None, "Required property 'loggers' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLoggerDefinitionVersion.LoggerProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoggerDefinitionVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnResourceDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition",
):
    '''The ``AWS::Greengrass::ResourceDefinition`` resource represents a resource definition for AWS IoT Greengrass .

    Resource definitions are used to organize your resource definition versions.

    Resource definitions can reference multiple resource definition versions. All resource definition versions must be associated with a resource definition. Each resource definition version can contain one or more resources. (In AWS CloudFormation , resources are named *resource instances* .)
    .. epigraph::

       When you create a resource definition, you can optionally include an initial resource definition version. To associate a resource definition version later, create an ```AWS::Greengrass::ResourceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html>`_ resource and specify the ID of this resource definition.

       After you create the resource definition version that contains the resources you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # tags: Any
        
        cfn_resource_definition = greengrass.CfnResourceDefinition(self, "MyCfnResourceDefinition",
            name="name",
        
            # the properties below are optional
            initial_version=greengrass.CfnResourceDefinition.ResourceDefinitionVersionProperty(
                resources=[greengrass.CfnResourceDefinition.ResourceInstanceProperty(
                    id="id",
                    name="name",
                    resource_data_container=greengrass.CfnResourceDefinition.ResourceDataContainerProperty(
                        local_device_resource_data=greengrass.CfnResourceDefinition.LocalDeviceResourceDataProperty(
                            source_path="sourcePath",
        
                            # the properties below are optional
                            group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                                auto_add_group_owner=False,
        
                                # the properties below are optional
                                group_owner="groupOwner"
                            )
                        ),
                        local_volume_resource_data=greengrass.CfnResourceDefinition.LocalVolumeResourceDataProperty(
                            destination_path="destinationPath",
                            source_path="sourcePath",
        
                            # the properties below are optional
                            group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                                auto_add_group_owner=False,
        
                                # the properties below are optional
                                group_owner="groupOwner"
                            )
                        ),
                        s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.S3MachineLearningModelResourceDataProperty(
                            destination_path="destinationPath",
                            s3_uri="s3Uri",
        
                            # the properties below are optional
                            owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                                group_owner="groupOwner",
                                group_permission="groupPermission"
                            )
                        ),
                        sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty(
                            destination_path="destinationPath",
                            sage_maker_job_arn="sageMakerJobArn",
        
                            # the properties below are optional
                            owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                                group_owner="groupOwner",
                                group_permission="groupPermission"
                            )
                        ),
                        secrets_manager_secret_resource_data=greengrass.CfnResourceDefinition.SecretsManagerSecretResourceDataProperty(
                            arn="arn",
        
                            # the properties below are optional
                            additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                        )
                    )
                )]
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.ResourceDefinitionVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the resource definition.
        :param initial_version: The resource definition version to include when the resource definition is created. A resource definition version contains a list of ```resource instance`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html>`_ property types. .. epigraph:: To associate a resource definition version after the resource definition is created, create an ```AWS::Greengrass::ResourceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html>`_ resource and specify the ID of this resource definition.
        :param tags: Application-specific metadata to attach to the resource definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__047c0e38fb370750fe5db940a38d857f066bb4490f8e079801f4c24d210372c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceDefinitionProps(
            name=name, initial_version=initial_version, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42977d53c22197ecb3e5aa75d8273dbffa91f7bab1c2d271a874285225a099b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a345a654c8dbd28db74cdcdaa4cf76ca9f4596ded63638879400c3589d09227)
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
        '''The Amazon Resource Name (ARN) of the ``ResourceDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/resources/1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the ``ResourceDefinition`` , such as ``1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersionArn")
    def attr_latest_version_arn(self) -> builtins.str:
        '''The ARN of the last ``ResourceDefinitionVersion`` that was added to the ``ResourceDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/resources/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`` .

        :cloudformationAttribute: LatestVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the ``ResourceDefinition`` , such as ``MyResourceDefinition`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''The name of the resource definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0256b19a6270c50864dd0afa1219a1b6be7518258daea855f19ca60744fa0d27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="initialVersion")
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDefinitionVersionProperty"]]:
        '''The resource definition version to include when the resource definition is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDefinitionVersionProperty"]], jsii.get(self, "initialVersion"))

    @initial_version.setter
    def initial_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDefinitionVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e477611b342531c61501bce71bad63149180465d67fa02234b702f1d04ed88e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''Application-specific metadata to attach to the resource definition.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f8767a6e08f9caeed0ccc0cab826c0939740af34c6b569658174c0ac9284975)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.GroupOwnerSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_add_group_owner": "autoAddGroupOwner",
            "group_owner": "groupOwner",
        },
    )
    class GroupOwnerSettingProperty:
        def __init__(
            self,
            *,
            auto_add_group_owner: typing.Union[builtins.bool, _IResolvable_da3f097b],
            group_owner: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings that define additional Linux OS group permissions to give to the Lambda function process.

            You can give the permissions of the Linux group that owns the resource or choose another Linux group. These permissions are in addition to the function's ``RunAs`` permissions.

            In an AWS CloudFormation template, ``GroupOwnerSetting`` is a property of the ```LocalDeviceResourceData`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html>`_ and ```LocalVolumeResourceData`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html>`_ property types.

            :param auto_add_group_owner: Indicates whether to give the privileges of the Linux group that owns the resource to the Lambda process. This gives the Lambda process the file access permissions of the Linux group.
            :param group_owner: The name of the Linux group whose privileges you want to add to the Lambda process. This value is ignored if ``AutoAddGroupOwner`` is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                group_owner_setting_property = greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                    auto_add_group_owner=False,
                
                    # the properties below are optional
                    group_owner="groupOwner"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dee09549db08436516a33cdfd3af7e5ad5db5fe672d89da865d7405e9d83a1b7)
                check_type(argname="argument auto_add_group_owner", value=auto_add_group_owner, expected_type=type_hints["auto_add_group_owner"])
                check_type(argname="argument group_owner", value=group_owner, expected_type=type_hints["group_owner"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "auto_add_group_owner": auto_add_group_owner,
            }
            if group_owner is not None:
                self._values["group_owner"] = group_owner

        @builtins.property
        def auto_add_group_owner(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether to give the privileges of the Linux group that owns the resource to the Lambda process.

            This gives the Lambda process the file access permissions of the Linux group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html#cfn-greengrass-resourcedefinition-groupownersetting-autoaddgroupowner
            '''
            result = self._values.get("auto_add_group_owner")
            assert result is not None, "Required property 'auto_add_group_owner' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def group_owner(self) -> typing.Optional[builtins.str]:
            '''The name of the Linux group whose privileges you want to add to the Lambda process.

            This value is ignored if ``AutoAddGroupOwner`` is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html#cfn-greengrass-resourcedefinition-groupownersetting-groupowner
            '''
            result = self._values.get("group_owner")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupOwnerSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.LocalDeviceResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_path": "sourcePath",
            "group_owner_setting": "groupOwnerSetting",
        },
    )
    class LocalDeviceResourceDataProperty:
        def __init__(
            self,
            *,
            source_path: builtins.str,
            group_owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.GroupOwnerSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for a local device resource, which represents a file under ``/dev`` .

            For more information, see `Access Local Resources with Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``LocalDeviceResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html>`_ property type.

            :param source_path: The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under ``/dev`` .
            :param group_owner_setting: Settings that define additional Linux OS group permissions to give to the Lambda function process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                local_device_resource_data_property = greengrass.CfnResourceDefinition.LocalDeviceResourceDataProperty(
                    source_path="sourcePath",
                
                    # the properties below are optional
                    group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                        auto_add_group_owner=False,
                
                        # the properties below are optional
                        group_owner="groupOwner"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__519c96577980326dba50fcff850097de74fac4e031ecd0c5b0699a683334e6e7)
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
                check_type(argname="argument group_owner_setting", value=group_owner_setting, expected_type=type_hints["group_owner_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_path": source_path,
            }
            if group_owner_setting is not None:
                self._values["group_owner_setting"] = group_owner_setting

        @builtins.property
        def source_path(self) -> builtins.str:
            '''The local absolute path of the device resource.

            The source path for a device resource can refer only to a character device or block device under ``/dev`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html#cfn-greengrass-resourcedefinition-localdeviceresourcedata-sourcepath
            '''
            result = self._values.get("source_path")
            assert result is not None, "Required property 'source_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_owner_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.GroupOwnerSettingProperty"]]:
            '''Settings that define additional Linux OS group permissions to give to the Lambda function process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html#cfn-greengrass-resourcedefinition-localdeviceresourcedata-groupownersetting
            '''
            result = self._values.get("group_owner_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.GroupOwnerSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalDeviceResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.LocalVolumeResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_path": "destinationPath",
            "source_path": "sourcePath",
            "group_owner_setting": "groupOwnerSetting",
        },
    )
    class LocalVolumeResourceDataProperty:
        def __init__(
            self,
            *,
            destination_path: builtins.str,
            source_path: builtins.str,
            group_owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.GroupOwnerSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for a local volume resource, which represents a file or directory on the root file system.

            For more information, see `Access Local Resources with Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``LocalVolumeResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html>`_ property type.

            :param destination_path: The absolute local path of the resource in the Lambda environment.
            :param source_path: The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with ``/sys`` .
            :param group_owner_setting: Settings that define additional Linux OS group permissions to give to the Lambda function process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                local_volume_resource_data_property = greengrass.CfnResourceDefinition.LocalVolumeResourceDataProperty(
                    destination_path="destinationPath",
                    source_path="sourcePath",
                
                    # the properties below are optional
                    group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                        auto_add_group_owner=False,
                
                        # the properties below are optional
                        group_owner="groupOwner"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a3bf7a5d451ecfb7a0028a5410ae5923ddd2e13f2d619750140c5474472942a)
                check_type(argname="argument destination_path", value=destination_path, expected_type=type_hints["destination_path"])
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
                check_type(argname="argument group_owner_setting", value=group_owner_setting, expected_type=type_hints["group_owner_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_path": destination_path,
                "source_path": source_path,
            }
            if group_owner_setting is not None:
                self._values["group_owner_setting"] = group_owner_setting

        @builtins.property
        def destination_path(self) -> builtins.str:
            '''The absolute local path of the resource in the Lambda environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-destinationpath
            '''
            result = self._values.get("destination_path")
            assert result is not None, "Required property 'destination_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_path(self) -> builtins.str:
            '''The local absolute path of the volume resource on the host.

            The source path for a volume resource type cannot start with ``/sys`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-sourcepath
            '''
            result = self._values.get("source_path")
            assert result is not None, "Required property 'source_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_owner_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.GroupOwnerSettingProperty"]]:
            '''Settings that define additional Linux OS group permissions to give to the Lambda function process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-groupownersetting
            '''
            result = self._values.get("group_owner_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.GroupOwnerSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalVolumeResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.ResourceDataContainerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_device_resource_data": "localDeviceResourceData",
            "local_volume_resource_data": "localVolumeResourceData",
            "s3_machine_learning_model_resource_data": "s3MachineLearningModelResourceData",
            "sage_maker_machine_learning_model_resource_data": "sageMakerMachineLearningModelResourceData",
            "secrets_manager_secret_resource_data": "secretsManagerSecretResourceData",
        },
    )
    class ResourceDataContainerProperty:
        def __init__(
            self,
            *,
            local_device_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.LocalDeviceResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            local_volume_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.LocalVolumeResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_machine_learning_model_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.S3MachineLearningModelResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sage_maker_machine_learning_model_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            secrets_manager_secret_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.SecretsManagerSecretResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A container for resource data, which defines the resource type.

            The container takes only one of the following supported resource data types: ``LocalDeviceResourceData`` , ``LocalVolumeResourceData`` , ``SageMakerMachineLearningModelResourceData`` , ``S3MachineLearningModelResourceData`` , or ``SecretsManagerSecretResourceData`` .
            .. epigraph::

               Only one resource type can be defined for a ``ResourceDataContainer`` instance.

            In an AWS CloudFormation template, ``ResourceDataContainer`` is a property of the ```ResourceInstance`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html>`_ property type.

            :param local_device_resource_data: Settings for a local device resource.
            :param local_volume_resource_data: Settings for a local volume resource.
            :param s3_machine_learning_model_resource_data: Settings for a machine learning resource stored in Amazon S3 .
            :param sage_maker_machine_learning_model_resource_data: Settings for a machine learning resource saved as an SageMaker training job.
            :param secrets_manager_secret_resource_data: Settings for a secret resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_data_container_property = greengrass.CfnResourceDefinition.ResourceDataContainerProperty(
                    local_device_resource_data=greengrass.CfnResourceDefinition.LocalDeviceResourceDataProperty(
                        source_path="sourcePath",
                
                        # the properties below are optional
                        group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                            auto_add_group_owner=False,
                
                            # the properties below are optional
                            group_owner="groupOwner"
                        )
                    ),
                    local_volume_resource_data=greengrass.CfnResourceDefinition.LocalVolumeResourceDataProperty(
                        destination_path="destinationPath",
                        source_path="sourcePath",
                
                        # the properties below are optional
                        group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                            auto_add_group_owner=False,
                
                            # the properties below are optional
                            group_owner="groupOwner"
                        )
                    ),
                    s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.S3MachineLearningModelResourceDataProperty(
                        destination_path="destinationPath",
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                            group_owner="groupOwner",
                            group_permission="groupPermission"
                        )
                    ),
                    sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty(
                        destination_path="destinationPath",
                        sage_maker_job_arn="sageMakerJobArn",
                
                        # the properties below are optional
                        owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                            group_owner="groupOwner",
                            group_permission="groupPermission"
                        )
                    ),
                    secrets_manager_secret_resource_data=greengrass.CfnResourceDefinition.SecretsManagerSecretResourceDataProperty(
                        arn="arn",
                
                        # the properties below are optional
                        additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__396357cb8698a2ab08ce94b2efcdff53c907a511665a527e7b6df7aeab58eaff)
                check_type(argname="argument local_device_resource_data", value=local_device_resource_data, expected_type=type_hints["local_device_resource_data"])
                check_type(argname="argument local_volume_resource_data", value=local_volume_resource_data, expected_type=type_hints["local_volume_resource_data"])
                check_type(argname="argument s3_machine_learning_model_resource_data", value=s3_machine_learning_model_resource_data, expected_type=type_hints["s3_machine_learning_model_resource_data"])
                check_type(argname="argument sage_maker_machine_learning_model_resource_data", value=sage_maker_machine_learning_model_resource_data, expected_type=type_hints["sage_maker_machine_learning_model_resource_data"])
                check_type(argname="argument secrets_manager_secret_resource_data", value=secrets_manager_secret_resource_data, expected_type=type_hints["secrets_manager_secret_resource_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if local_device_resource_data is not None:
                self._values["local_device_resource_data"] = local_device_resource_data
            if local_volume_resource_data is not None:
                self._values["local_volume_resource_data"] = local_volume_resource_data
            if s3_machine_learning_model_resource_data is not None:
                self._values["s3_machine_learning_model_resource_data"] = s3_machine_learning_model_resource_data
            if sage_maker_machine_learning_model_resource_data is not None:
                self._values["sage_maker_machine_learning_model_resource_data"] = sage_maker_machine_learning_model_resource_data
            if secrets_manager_secret_resource_data is not None:
                self._values["secrets_manager_secret_resource_data"] = secrets_manager_secret_resource_data

        @builtins.property
        def local_device_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.LocalDeviceResourceDataProperty"]]:
            '''Settings for a local device resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-localdeviceresourcedata
            '''
            result = self._values.get("local_device_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.LocalDeviceResourceDataProperty"]], result)

        @builtins.property
        def local_volume_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.LocalVolumeResourceDataProperty"]]:
            '''Settings for a local volume resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-localvolumeresourcedata
            '''
            result = self._values.get("local_volume_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.LocalVolumeResourceDataProperty"]], result)

        @builtins.property
        def s3_machine_learning_model_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.S3MachineLearningModelResourceDataProperty"]]:
            '''Settings for a machine learning resource stored in Amazon S3 .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-s3machinelearningmodelresourcedata
            '''
            result = self._values.get("s3_machine_learning_model_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.S3MachineLearningModelResourceDataProperty"]], result)

        @builtins.property
        def sage_maker_machine_learning_model_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty"]]:
            '''Settings for a machine learning resource saved as an SageMaker training job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-sagemakermachinelearningmodelresourcedata
            '''
            result = self._values.get("sage_maker_machine_learning_model_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty"]], result)

        @builtins.property
        def secrets_manager_secret_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.SecretsManagerSecretResourceDataProperty"]]:
            '''Settings for a secret resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-secretsmanagersecretresourcedata
            '''
            result = self._values.get("secrets_manager_secret_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.SecretsManagerSecretResourceDataProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceDataContainerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.ResourceDefinitionVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"resources": "resources"},
    )
    class ResourceDefinitionVersionProperty:
        def __init__(
            self,
            *,
            resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.ResourceInstanceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A resource definition version contains a list of resources. (In AWS CloudFormation , resources are named *resource instances* .).

            .. epigraph::

               After you create a resource definition version that contains the resources you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

            In an AWS CloudFormation template, ``ResourceDefinitionVersion`` is the property type of the ``InitialVersion`` property in the ```AWS::Greengrass::ResourceDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html>`_ resource.

            :param resources: The resources in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_definition_version_property = greengrass.CfnResourceDefinition.ResourceDefinitionVersionProperty(
                    resources=[greengrass.CfnResourceDefinition.ResourceInstanceProperty(
                        id="id",
                        name="name",
                        resource_data_container=greengrass.CfnResourceDefinition.ResourceDataContainerProperty(
                            local_device_resource_data=greengrass.CfnResourceDefinition.LocalDeviceResourceDataProperty(
                                source_path="sourcePath",
                
                                # the properties below are optional
                                group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                                    auto_add_group_owner=False,
                
                                    # the properties below are optional
                                    group_owner="groupOwner"
                                )
                            ),
                            local_volume_resource_data=greengrass.CfnResourceDefinition.LocalVolumeResourceDataProperty(
                                destination_path="destinationPath",
                                source_path="sourcePath",
                
                                # the properties below are optional
                                group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                                    auto_add_group_owner=False,
                
                                    # the properties below are optional
                                    group_owner="groupOwner"
                                )
                            ),
                            s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.S3MachineLearningModelResourceDataProperty(
                                destination_path="destinationPath",
                                s3_uri="s3Uri",
                
                                # the properties below are optional
                                owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                                    group_owner="groupOwner",
                                    group_permission="groupPermission"
                                )
                            ),
                            sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty(
                                destination_path="destinationPath",
                                sage_maker_job_arn="sageMakerJobArn",
                
                                # the properties below are optional
                                owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                                    group_owner="groupOwner",
                                    group_permission="groupPermission"
                                )
                            ),
                            secrets_manager_secret_resource_data=greengrass.CfnResourceDefinition.SecretsManagerSecretResourceDataProperty(
                                arn="arn",
                
                                # the properties below are optional
                                additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                            )
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4c2b639a854266ea9e4614285d20bfcd34ae6e76ad6b8c645cd458ea74d79b1d)
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resources": resources,
            }

        @builtins.property
        def resources(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceInstanceProperty"]]]:
            '''The resources in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html#cfn-greengrass-resourcedefinition-resourcedefinitionversion-resources
            '''
            result = self._values.get("resources")
            assert result is not None, "Required property 'resources' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceInstanceProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceDefinitionVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "group_owner": "groupOwner",
            "group_permission": "groupPermission",
        },
    )
    class ResourceDownloadOwnerSettingProperty:
        def __init__(
            self,
            *,
            group_owner: builtins.str,
            group_permission: builtins.str,
        ) -> None:
            '''The owner setting for a downloaded machine learning resource.

            For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``ResourceDownloadOwnerSetting`` is the property type of the ``OwnerSetting`` property for the ```S3MachineLearningModelResourceData`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html>`_ and ```SageMakerMachineLearningModelResourceData`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html>`_ property types.

            :param group_owner: The group owner of the machine learning resource. This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.
            :param group_permission: The permissions that the group owner has to the machine learning resource. Valid values are ``rw`` (read-write) or ``ro`` (read-only).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_download_owner_setting_property = greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                    group_owner="groupOwner",
                    group_permission="groupPermission"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ef1515394b8f7bc78aa0cb5c9c538e8d26325857332890bc231c259b12d7c585)
                check_type(argname="argument group_owner", value=group_owner, expected_type=type_hints["group_owner"])
                check_type(argname="argument group_permission", value=group_permission, expected_type=type_hints["group_permission"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "group_owner": group_owner,
                "group_permission": group_permission,
            }

        @builtins.property
        def group_owner(self) -> builtins.str:
            '''The group owner of the machine learning resource.

            This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-groupowner
            '''
            result = self._values.get("group_owner")
            assert result is not None, "Required property 'group_owner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_permission(self) -> builtins.str:
            '''The permissions that the group owner has to the machine learning resource.

            Valid values are ``rw`` (read-write) or ``ro`` (read-only).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-grouppermission
            '''
            result = self._values.get("group_permission")
            assert result is not None, "Required property 'group_permission' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceDownloadOwnerSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.ResourceInstanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "name": "name",
            "resource_data_container": "resourceDataContainer",
        },
    )
    class ResourceInstanceProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            name: builtins.str,
            resource_data_container: typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.ResourceDataContainerProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A local resource, machine learning resource, or secret resource.

            For more information, see `Access Local Resources with Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html>`_ , `Perform Machine Learning Inference <https://docs.aws.amazon.com/greengrass/latest/developerguide/ml-inference.html>`_ , and `Deploy Secrets to the AWS IoT Greengrass Core <https://docs.aws.amazon.com/greengrass/latest/developerguide/secrets.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Resources`` property of the ```AWS::Greengrass::ResourceDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html>`_ resource contains a list of ``ResourceInstance`` property types.

            :param id: A descriptive or arbitrary ID for the resource. This value must be unique within the resource definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param name: The descriptive resource name, which is displayed on the AWS IoT Greengrass console. Maximum length 128 characters with pattern [a-zA-Z0-9:_-]+. This must be unique within a Greengrass group.
            :param resource_data_container: A container for resource data. The container takes only one of the following supported resource data types: ``LocalDeviceResourceData`` , ``LocalVolumeResourceData`` , ``SageMakerMachineLearningModelResourceData`` , ``S3MachineLearningModelResourceData`` , or ``SecretsManagerSecretResourceData`` . .. epigraph:: Only one resource type can be defined for a ``ResourceDataContainer`` instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_instance_property = greengrass.CfnResourceDefinition.ResourceInstanceProperty(
                    id="id",
                    name="name",
                    resource_data_container=greengrass.CfnResourceDefinition.ResourceDataContainerProperty(
                        local_device_resource_data=greengrass.CfnResourceDefinition.LocalDeviceResourceDataProperty(
                            source_path="sourcePath",
                
                            # the properties below are optional
                            group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                                auto_add_group_owner=False,
                
                                # the properties below are optional
                                group_owner="groupOwner"
                            )
                        ),
                        local_volume_resource_data=greengrass.CfnResourceDefinition.LocalVolumeResourceDataProperty(
                            destination_path="destinationPath",
                            source_path="sourcePath",
                
                            # the properties below are optional
                            group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                                auto_add_group_owner=False,
                
                                # the properties below are optional
                                group_owner="groupOwner"
                            )
                        ),
                        s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.S3MachineLearningModelResourceDataProperty(
                            destination_path="destinationPath",
                            s3_uri="s3Uri",
                
                            # the properties below are optional
                            owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                                group_owner="groupOwner",
                                group_permission="groupPermission"
                            )
                        ),
                        sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty(
                            destination_path="destinationPath",
                            sage_maker_job_arn="sageMakerJobArn",
                
                            # the properties below are optional
                            owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                                group_owner="groupOwner",
                                group_permission="groupPermission"
                            )
                        ),
                        secrets_manager_secret_resource_data=greengrass.CfnResourceDefinition.SecretsManagerSecretResourceDataProperty(
                            arn="arn",
                
                            # the properties below are optional
                            additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5049866f9bc9b9b69029fc4e81f22c8620cd6a6cded5d5499d0011b8e4f438e)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument resource_data_container", value=resource_data_container, expected_type=type_hints["resource_data_container"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "name": name,
                "resource_data_container": resource_data_container,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the resource.

            This value must be unique within the resource definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The descriptive resource name, which is displayed on the AWS IoT Greengrass console.

            Maximum length 128 characters with pattern [a-zA-Z0-9:_-]+. This must be unique within a Greengrass group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_data_container(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDataContainerProperty"]:
            '''A container for resource data.

            The container takes only one of the following supported resource data types: ``LocalDeviceResourceData`` , ``LocalVolumeResourceData`` , ``SageMakerMachineLearningModelResourceData`` , ``S3MachineLearningModelResourceData`` , or ``SecretsManagerSecretResourceData`` .
            .. epigraph::

               Only one resource type can be defined for a ``ResourceDataContainer`` instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-resourcedatacontainer
            '''
            result = self._values.get("resource_data_container")
            assert result is not None, "Required property 'resource_data_container' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDataContainerProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceInstanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.S3MachineLearningModelResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_path": "destinationPath",
            "s3_uri": "s3Uri",
            "owner_setting": "ownerSetting",
        },
    )
    class S3MachineLearningModelResourceDataProperty:
        def __init__(
            self,
            *,
            destination_path: builtins.str,
            s3_uri: builtins.str,
            owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.ResourceDownloadOwnerSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for an Amazon S3 machine learning resource.

            For more information, see `Perform Machine Learning Inference <https://docs.aws.amazon.com/greengrass/latest/developerguide/ml-inference.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``S3MachineLearningModelResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html>`_ property type.

            :param destination_path: The absolute local path of the resource inside the Lambda environment.
            :param s3_uri: The URI of the source model in an Amazon S3 bucket. The model package must be in ``tar.gz`` or ``.zip`` format.
            :param owner_setting: The owner setting for the downloaded machine learning resource. For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                s3_machine_learning_model_resource_data_property = greengrass.CfnResourceDefinition.S3MachineLearningModelResourceDataProperty(
                    destination_path="destinationPath",
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                        group_owner="groupOwner",
                        group_permission="groupPermission"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5bb7ffbcaf0627cc8969d8e7b4223d2abe7b6803cebdf191f694ccdb20da9b1)
                check_type(argname="argument destination_path", value=destination_path, expected_type=type_hints["destination_path"])
                check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
                check_type(argname="argument owner_setting", value=owner_setting, expected_type=type_hints["owner_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_path": destination_path,
                "s3_uri": s3_uri,
            }
            if owner_setting is not None:
                self._values["owner_setting"] = owner_setting

        @builtins.property
        def destination_path(self) -> builtins.str:
            '''The absolute local path of the resource inside the Lambda environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-destinationpath
            '''
            result = self._values.get("destination_path")
            assert result is not None, "Required property 'destination_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''The URI of the source model in an Amazon S3 bucket.

            The model package must be in ``tar.gz`` or ``.zip`` format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def owner_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDownloadOwnerSettingProperty"]]:
            '''The owner setting for the downloaded machine learning resource.

            For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-ownersetting
            '''
            result = self._values.get("owner_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDownloadOwnerSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3MachineLearningModelResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_path": "destinationPath",
            "sage_maker_job_arn": "sageMakerJobArn",
            "owner_setting": "ownerSetting",
        },
    )
    class SageMakerMachineLearningModelResourceDataProperty:
        def __init__(
            self,
            *,
            destination_path: builtins.str,
            sage_maker_job_arn: builtins.str,
            owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinition.ResourceDownloadOwnerSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for an Secrets Manager machine learning resource.

            For more information, see `Perform Machine Learning Inference <https://docs.aws.amazon.com/greengrass/latest/developerguide/ml-inference.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``SageMakerMachineLearningModelResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html>`_ property type.

            :param destination_path: The absolute local path of the resource inside the Lambda environment.
            :param sage_maker_job_arn: The Amazon Resource Name (ARN) of the Amazon SageMaker training job that represents the source model.
            :param owner_setting: The owner setting for the downloaded machine learning resource. For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                sage_maker_machine_learning_model_resource_data_property = greengrass.CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty(
                    destination_path="destinationPath",
                    sage_maker_job_arn="sageMakerJobArn",
                
                    # the properties below are optional
                    owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                        group_owner="groupOwner",
                        group_permission="groupPermission"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3995e8ba195b1f7e333172d25dc3c1e984db53c31650fe725fa3554fa39e8c03)
                check_type(argname="argument destination_path", value=destination_path, expected_type=type_hints["destination_path"])
                check_type(argname="argument sage_maker_job_arn", value=sage_maker_job_arn, expected_type=type_hints["sage_maker_job_arn"])
                check_type(argname="argument owner_setting", value=owner_setting, expected_type=type_hints["owner_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_path": destination_path,
                "sage_maker_job_arn": sage_maker_job_arn,
            }
            if owner_setting is not None:
                self._values["owner_setting"] = owner_setting

        @builtins.property
        def destination_path(self) -> builtins.str:
            '''The absolute local path of the resource inside the Lambda environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-destinationpath
            '''
            result = self._values.get("destination_path")
            assert result is not None, "Required property 'destination_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sage_maker_job_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon SageMaker training job that represents the source model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-sagemakerjobarn
            '''
            result = self._values.get("sage_maker_job_arn")
            assert result is not None, "Required property 'sage_maker_job_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def owner_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDownloadOwnerSettingProperty"]]:
            '''The owner setting for the downloaded machine learning resource.

            For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-ownersetting
            '''
            result = self._values.get("owner_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinition.ResourceDownloadOwnerSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SageMakerMachineLearningModelResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinition.SecretsManagerSecretResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "additional_staging_labels_to_download": "additionalStagingLabelsToDownload",
        },
    )
    class SecretsManagerSecretResourceDataProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            additional_staging_labels_to_download: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Settings for a secret resource, which references a secret from AWS Secrets Manager .

            AWS IoT Greengrass stores a local, encrypted copy of the secret on the Greengrass core, where it can be securely accessed by connectors and Lambda functions. For more information, see `Deploy Secrets to the AWS IoT Greengrass Core <https://docs.aws.amazon.com/greengrass/latest/developerguide/secrets.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``SecretsManagerSecretResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html>`_ property type.

            :param arn: The Amazon Resource Name (ARN) of the Secrets Manager secret to make available on the core. The value of the secret's latest version (represented by the ``AWSCURRENT`` staging label) is included by default.
            :param additional_staging_labels_to_download: The staging labels whose values you want to make available on the core, in addition to ``AWSCURRENT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                secrets_manager_secret_resource_data_property = greengrass.CfnResourceDefinition.SecretsManagerSecretResourceDataProperty(
                    arn="arn",
                
                    # the properties below are optional
                    additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7665349bcf6d8c447b8247f984eb20a41ebfec207c55b6f809ba23f39db5e941)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument additional_staging_labels_to_download", value=additional_staging_labels_to_download, expected_type=type_hints["additional_staging_labels_to_download"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
            }
            if additional_staging_labels_to_download is not None:
                self._values["additional_staging_labels_to_download"] = additional_staging_labels_to_download

        @builtins.property
        def arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Secrets Manager secret to make available on the core.

            The value of the secret's latest version (represented by the ``AWSCURRENT`` staging label) is included by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinition-secretsmanagersecretresourcedata-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def additional_staging_labels_to_download(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The staging labels whose values you want to make available on the core, in addition to ``AWSCURRENT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinition-secretsmanagersecretresourcedata-additionalstaginglabelstodownload
            '''
            result = self._values.get("additional_staging_labels_to_download")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretsManagerSecretResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "initial_version": "initialVersion", "tags": "tags"},
)
class CfnResourceDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.ResourceDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceDefinition``.

        :param name: The name of the resource definition.
        :param initial_version: The resource definition version to include when the resource definition is created. A resource definition version contains a list of ```resource instance`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html>`_ property types. .. epigraph:: To associate a resource definition version after the resource definition is created, create an ```AWS::Greengrass::ResourceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html>`_ resource and specify the ID of this resource definition.
        :param tags: Application-specific metadata to attach to the resource definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # tags: Any
            
            cfn_resource_definition_props = greengrass.CfnResourceDefinitionProps(
                name="name",
            
                # the properties below are optional
                initial_version=greengrass.CfnResourceDefinition.ResourceDefinitionVersionProperty(
                    resources=[greengrass.CfnResourceDefinition.ResourceInstanceProperty(
                        id="id",
                        name="name",
                        resource_data_container=greengrass.CfnResourceDefinition.ResourceDataContainerProperty(
                            local_device_resource_data=greengrass.CfnResourceDefinition.LocalDeviceResourceDataProperty(
                                source_path="sourcePath",
            
                                # the properties below are optional
                                group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                                    auto_add_group_owner=False,
            
                                    # the properties below are optional
                                    group_owner="groupOwner"
                                )
                            ),
                            local_volume_resource_data=greengrass.CfnResourceDefinition.LocalVolumeResourceDataProperty(
                                destination_path="destinationPath",
                                source_path="sourcePath",
            
                                # the properties below are optional
                                group_owner_setting=greengrass.CfnResourceDefinition.GroupOwnerSettingProperty(
                                    auto_add_group_owner=False,
            
                                    # the properties below are optional
                                    group_owner="groupOwner"
                                )
                            ),
                            s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.S3MachineLearningModelResourceDataProperty(
                                destination_path="destinationPath",
                                s3_uri="s3Uri",
            
                                # the properties below are optional
                                owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                                    group_owner="groupOwner",
                                    group_permission="groupPermission"
                                )
                            ),
                            sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty(
                                destination_path="destinationPath",
                                sage_maker_job_arn="sageMakerJobArn",
            
                                # the properties below are optional
                                owner_setting=greengrass.CfnResourceDefinition.ResourceDownloadOwnerSettingProperty(
                                    group_owner="groupOwner",
                                    group_permission="groupPermission"
                                )
                            ),
                            secrets_manager_secret_resource_data=greengrass.CfnResourceDefinition.SecretsManagerSecretResourceDataProperty(
                                arn="arn",
            
                                # the properties below are optional
                                additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                            )
                        )
                    )]
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d19c7aa996849ae5308a845fea1be8a360b83d3ec8158f6a19c48fe68f5009)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument initial_version", value=initial_version, expected_type=type_hints["initial_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if initial_version is not None:
            self._values["initial_version"] = initial_version
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the resource definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDefinition.ResourceDefinitionVersionProperty]]:
        '''The resource definition version to include when the resource definition is created.

        A resource definition version contains a list of ```resource instance`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html>`_ property types.
        .. epigraph::

           To associate a resource definition version after the resource definition is created, create an ```AWS::Greengrass::ResourceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html>`_ resource and specify the ID of this resource definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-initialversion
        '''
        result = self._values.get("initial_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDefinition.ResourceDefinitionVersionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Application-specific metadata to attach to the resource definition.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceDefinitionVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion",
):
    '''The ``AWS::Greengrass::ResourceDefinitionVersion`` resource represents a resource definition version for AWS IoT Greengrass .

    A resource definition version contains a list of resources. (In AWS CloudFormation , resources are named *resource instances* .)
    .. epigraph::

       To create a resource definition version, you must specify the ID of the resource definition that you want to associate with the version. For information about creating a resource definition, see ```AWS::Greengrass::ResourceDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html>`_ .

       After you create a resource definition version that contains the resources you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        cfn_resource_definition_version = greengrass.CfnResourceDefinitionVersion(self, "MyCfnResourceDefinitionVersion",
            resource_definition_id="resourceDefinitionId",
            resources=[greengrass.CfnResourceDefinitionVersion.ResourceInstanceProperty(
                id="id",
                name="name",
                resource_data_container=greengrass.CfnResourceDefinitionVersion.ResourceDataContainerProperty(
                    local_device_resource_data=greengrass.CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty(
                        source_path="sourcePath",
        
                        # the properties below are optional
                        group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                            auto_add_group_owner=False,
        
                            # the properties below are optional
                            group_owner="groupOwner"
                        )
                    ),
                    local_volume_resource_data=greengrass.CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty(
                        destination_path="destinationPath",
                        source_path="sourcePath",
        
                        # the properties below are optional
                        group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                            auto_add_group_owner=False,
        
                            # the properties below are optional
                            group_owner="groupOwner"
                        )
                    ),
                    s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty(
                        destination_path="destinationPath",
                        s3_uri="s3Uri",
        
                        # the properties below are optional
                        owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                            group_owner="groupOwner",
                            group_permission="groupPermission"
                        )
                    ),
                    sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty(
                        destination_path="destinationPath",
                        sage_maker_job_arn="sageMakerJobArn",
        
                        # the properties below are optional
                        owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                            group_owner="groupOwner",
                            group_permission="groupPermission"
                        )
                    ),
                    secrets_manager_secret_resource_data=greengrass.CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty(
                        arn="arn",
        
                        # the properties below are optional
                        additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                    )
                )
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_definition_id: builtins.str,
        resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.ResourceInstanceProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_definition_id: The ID of the resource definition associated with this version. This value is a GUID.
        :param resources: The resources in this version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e106c323b7cfeaacd807745287aed9743502c2e5353d29679ad3381a494b6a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceDefinitionVersionProps(
            resource_definition_id=resource_definition_id, resources=resources
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62f5d9f4cfb364bba693491c17e35b128c2b8ee571b3a2e22a37a57beae0a3b5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5dc49d5697e9f2028c7bd3fb79a84e389f982ae6aff558a88094ca6c07cdc1ee)
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
    @jsii.member(jsii_name="resourceDefinitionId")
    def resource_definition_id(self) -> builtins.str:
        '''The ID of the resource definition associated with this version.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceDefinitionId"))

    @resource_definition_id.setter
    def resource_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62580ea31539bd91a408bb34b014f3d32df9c5903336db1a3dd73bad8e783dc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceInstanceProperty"]]]:
        '''The resources in this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceInstanceProperty"]]], jsii.get(self, "resources"))

    @resources.setter
    def resources(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceInstanceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74096283c52a878723fa8ea3375fb7a3d8f6b1924db6d17a865bc7f6ab31cce8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_add_group_owner": "autoAddGroupOwner",
            "group_owner": "groupOwner",
        },
    )
    class GroupOwnerSettingProperty:
        def __init__(
            self,
            *,
            auto_add_group_owner: typing.Union[builtins.bool, _IResolvable_da3f097b],
            group_owner: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings that define additional Linux OS group permissions to give to the Lambda function process.

            You can give the permissions of the Linux group that owns the resource or choose another Linux group. These permissions are in addition to the function's ``RunAs`` permissions.

            In an AWS CloudFormation template, ``GroupOwnerSetting`` is a property of the ```LocalDeviceResourceData`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html>`_ and ```LocalVolumeResourceData`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html>`_ property types.

            :param auto_add_group_owner: Indicates whether to give the privileges of the Linux group that owns the resource to the Lambda process. This gives the Lambda process the file access permissions of the Linux group.
            :param group_owner: The name of the Linux group whose privileges you want to add to the Lambda process. This value is ignored if ``AutoAddGroupOwner`` is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                group_owner_setting_property = greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                    auto_add_group_owner=False,
                
                    # the properties below are optional
                    group_owner="groupOwner"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a8988f1c5c6c177915d440c485ec6d617ad5fab37340bb66f4512f8046513d05)
                check_type(argname="argument auto_add_group_owner", value=auto_add_group_owner, expected_type=type_hints["auto_add_group_owner"])
                check_type(argname="argument group_owner", value=group_owner, expected_type=type_hints["group_owner"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "auto_add_group_owner": auto_add_group_owner,
            }
            if group_owner is not None:
                self._values["group_owner"] = group_owner

        @builtins.property
        def auto_add_group_owner(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether to give the privileges of the Linux group that owns the resource to the Lambda process.

            This gives the Lambda process the file access permissions of the Linux group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html#cfn-greengrass-resourcedefinitionversion-groupownersetting-autoaddgroupowner
            '''
            result = self._values.get("auto_add_group_owner")
            assert result is not None, "Required property 'auto_add_group_owner' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def group_owner(self) -> typing.Optional[builtins.str]:
            '''The name of the Linux group whose privileges you want to add to the Lambda process.

            This value is ignored if ``AutoAddGroupOwner`` is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html#cfn-greengrass-resourcedefinitionversion-groupownersetting-groupowner
            '''
            result = self._values.get("group_owner")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupOwnerSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_path": "sourcePath",
            "group_owner_setting": "groupOwnerSetting",
        },
    )
    class LocalDeviceResourceDataProperty:
        def __init__(
            self,
            *,
            source_path: builtins.str,
            group_owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.GroupOwnerSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for a local device resource, which represents a file under ``/dev`` .

            For more information, see `Access Local Resources with Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``LocalDeviceResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html>`_ property type.

            :param source_path: The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under ``/dev`` .
            :param group_owner_setting: Settings that define additional Linux OS group permissions to give to the Lambda function process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                local_device_resource_data_property = greengrass.CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty(
                    source_path="sourcePath",
                
                    # the properties below are optional
                    group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                        auto_add_group_owner=False,
                
                        # the properties below are optional
                        group_owner="groupOwner"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad1e5ad5d32a1c882a19870f66bf8426f59f3e8a4b04c0e26abd1cfd58c9da20)
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
                check_type(argname="argument group_owner_setting", value=group_owner_setting, expected_type=type_hints["group_owner_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_path": source_path,
            }
            if group_owner_setting is not None:
                self._values["group_owner_setting"] = group_owner_setting

        @builtins.property
        def source_path(self) -> builtins.str:
            '''The local absolute path of the device resource.

            The source path for a device resource can refer only to a character device or block device under ``/dev`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-sourcepath
            '''
            result = self._values.get("source_path")
            assert result is not None, "Required property 'source_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_owner_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.GroupOwnerSettingProperty"]]:
            '''Settings that define additional Linux OS group permissions to give to the Lambda function process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-groupownersetting
            '''
            result = self._values.get("group_owner_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.GroupOwnerSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalDeviceResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_path": "destinationPath",
            "source_path": "sourcePath",
            "group_owner_setting": "groupOwnerSetting",
        },
    )
    class LocalVolumeResourceDataProperty:
        def __init__(
            self,
            *,
            destination_path: builtins.str,
            source_path: builtins.str,
            group_owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.GroupOwnerSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for a local volume resource, which represents a file or directory on the root file system.

            For more information, see `Access Local Resources with Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``LocalVolumeResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html>`_ property type.

            :param destination_path: The absolute local path of the resource in the Lambda environment.
            :param source_path: The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with ``/sys`` .
            :param group_owner_setting: Settings that define additional Linux OS group permissions to give to the Lambda function process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                local_volume_resource_data_property = greengrass.CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty(
                    destination_path="destinationPath",
                    source_path="sourcePath",
                
                    # the properties below are optional
                    group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                        auto_add_group_owner=False,
                
                        # the properties below are optional
                        group_owner="groupOwner"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aba79cc6c8d101b2524627c61005b837fe8f6106d075960b72da33a2448402a1)
                check_type(argname="argument destination_path", value=destination_path, expected_type=type_hints["destination_path"])
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
                check_type(argname="argument group_owner_setting", value=group_owner_setting, expected_type=type_hints["group_owner_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_path": destination_path,
                "source_path": source_path,
            }
            if group_owner_setting is not None:
                self._values["group_owner_setting"] = group_owner_setting

        @builtins.property
        def destination_path(self) -> builtins.str:
            '''The absolute local path of the resource in the Lambda environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-destinationpath
            '''
            result = self._values.get("destination_path")
            assert result is not None, "Required property 'destination_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_path(self) -> builtins.str:
            '''The local absolute path of the volume resource on the host.

            The source path for a volume resource type cannot start with ``/sys`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-sourcepath
            '''
            result = self._values.get("source_path")
            assert result is not None, "Required property 'source_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_owner_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.GroupOwnerSettingProperty"]]:
            '''Settings that define additional Linux OS group permissions to give to the Lambda function process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-groupownersetting
            '''
            result = self._values.get("group_owner_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.GroupOwnerSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalVolumeResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.ResourceDataContainerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_device_resource_data": "localDeviceResourceData",
            "local_volume_resource_data": "localVolumeResourceData",
            "s3_machine_learning_model_resource_data": "s3MachineLearningModelResourceData",
            "sage_maker_machine_learning_model_resource_data": "sageMakerMachineLearningModelResourceData",
            "secrets_manager_secret_resource_data": "secretsManagerSecretResourceData",
        },
    )
    class ResourceDataContainerProperty:
        def __init__(
            self,
            *,
            local_device_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            local_volume_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_machine_learning_model_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sage_maker_machine_learning_model_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            secrets_manager_secret_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A container for resource data, which defines the resource type.

            The container takes only one of the following supported resource data types: ``LocalDeviceResourceData`` , ``LocalVolumeResourceData`` , ``SageMakerMachineLearningModelResourceData`` , ``S3MachineLearningModelResourceData`` , or ``SecretsManagerSecretResourceData`` .
            .. epigraph::

               Only one resource type can be defined for a ``ResourceDataContainer`` instance.

            In an AWS CloudFormation template, ``ResourceDataContainer`` is a property of the ```ResourceInstance`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html>`_ property type.

            :param local_device_resource_data: Settings for a local device resource.
            :param local_volume_resource_data: Settings for a local volume resource.
            :param s3_machine_learning_model_resource_data: Settings for a machine learning resource stored in Amazon S3 .
            :param sage_maker_machine_learning_model_resource_data: Settings for a machine learning resource saved as an SageMaker training job.
            :param secrets_manager_secret_resource_data: Settings for a secret resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_data_container_property = greengrass.CfnResourceDefinitionVersion.ResourceDataContainerProperty(
                    local_device_resource_data=greengrass.CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty(
                        source_path="sourcePath",
                
                        # the properties below are optional
                        group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                            auto_add_group_owner=False,
                
                            # the properties below are optional
                            group_owner="groupOwner"
                        )
                    ),
                    local_volume_resource_data=greengrass.CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty(
                        destination_path="destinationPath",
                        source_path="sourcePath",
                
                        # the properties below are optional
                        group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                            auto_add_group_owner=False,
                
                            # the properties below are optional
                            group_owner="groupOwner"
                        )
                    ),
                    s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty(
                        destination_path="destinationPath",
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                            group_owner="groupOwner",
                            group_permission="groupPermission"
                        )
                    ),
                    sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty(
                        destination_path="destinationPath",
                        sage_maker_job_arn="sageMakerJobArn",
                
                        # the properties below are optional
                        owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                            group_owner="groupOwner",
                            group_permission="groupPermission"
                        )
                    ),
                    secrets_manager_secret_resource_data=greengrass.CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty(
                        arn="arn",
                
                        # the properties below are optional
                        additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e1f173a21b203c0c5e80391a9ec0fbd6e1e7fc332eafdd65534039d45a1fa167)
                check_type(argname="argument local_device_resource_data", value=local_device_resource_data, expected_type=type_hints["local_device_resource_data"])
                check_type(argname="argument local_volume_resource_data", value=local_volume_resource_data, expected_type=type_hints["local_volume_resource_data"])
                check_type(argname="argument s3_machine_learning_model_resource_data", value=s3_machine_learning_model_resource_data, expected_type=type_hints["s3_machine_learning_model_resource_data"])
                check_type(argname="argument sage_maker_machine_learning_model_resource_data", value=sage_maker_machine_learning_model_resource_data, expected_type=type_hints["sage_maker_machine_learning_model_resource_data"])
                check_type(argname="argument secrets_manager_secret_resource_data", value=secrets_manager_secret_resource_data, expected_type=type_hints["secrets_manager_secret_resource_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if local_device_resource_data is not None:
                self._values["local_device_resource_data"] = local_device_resource_data
            if local_volume_resource_data is not None:
                self._values["local_volume_resource_data"] = local_volume_resource_data
            if s3_machine_learning_model_resource_data is not None:
                self._values["s3_machine_learning_model_resource_data"] = s3_machine_learning_model_resource_data
            if sage_maker_machine_learning_model_resource_data is not None:
                self._values["sage_maker_machine_learning_model_resource_data"] = sage_maker_machine_learning_model_resource_data
            if secrets_manager_secret_resource_data is not None:
                self._values["secrets_manager_secret_resource_data"] = secrets_manager_secret_resource_data

        @builtins.property
        def local_device_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty"]]:
            '''Settings for a local device resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localdeviceresourcedata
            '''
            result = self._values.get("local_device_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty"]], result)

        @builtins.property
        def local_volume_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty"]]:
            '''Settings for a local volume resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localvolumeresourcedata
            '''
            result = self._values.get("local_volume_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty"]], result)

        @builtins.property
        def s3_machine_learning_model_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty"]]:
            '''Settings for a machine learning resource stored in Amazon S3 .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-s3machinelearningmodelresourcedata
            '''
            result = self._values.get("s3_machine_learning_model_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty"]], result)

        @builtins.property
        def sage_maker_machine_learning_model_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty"]]:
            '''Settings for a machine learning resource saved as an SageMaker training job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-sagemakermachinelearningmodelresourcedata
            '''
            result = self._values.get("sage_maker_machine_learning_model_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty"]], result)

        @builtins.property
        def secrets_manager_secret_resource_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty"]]:
            '''Settings for a secret resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-secretsmanagersecretresourcedata
            '''
            result = self._values.get("secrets_manager_secret_resource_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceDataContainerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "group_owner": "groupOwner",
            "group_permission": "groupPermission",
        },
    )
    class ResourceDownloadOwnerSettingProperty:
        def __init__(
            self,
            *,
            group_owner: builtins.str,
            group_permission: builtins.str,
        ) -> None:
            '''The owner setting for a downloaded machine learning resource.

            For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``ResourceDownloadOwnerSetting`` is the property type of the ``OwnerSetting`` property for the ```S3MachineLearningModelResourceData`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html>`_ and ```SageMakerMachineLearningModelResourceData`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html>`_ property types.

            :param group_owner: The group owner of the machine learning resource. This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.
            :param group_permission: The permissions that the group owner has to the machine learning resource. Valid values are ``rw`` (read-write) or ``ro`` (read-only).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_download_owner_setting_property = greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                    group_owner="groupOwner",
                    group_permission="groupPermission"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc0a8bffe4da2c9d860929131465d097b2e15f4dec1ec670a751d2b96dd405f9)
                check_type(argname="argument group_owner", value=group_owner, expected_type=type_hints["group_owner"])
                check_type(argname="argument group_permission", value=group_permission, expected_type=type_hints["group_permission"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "group_owner": group_owner,
                "group_permission": group_permission,
            }

        @builtins.property
        def group_owner(self) -> builtins.str:
            '''The group owner of the machine learning resource.

            This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinitionversion-resourcedownloadownersetting-groupowner
            '''
            result = self._values.get("group_owner")
            assert result is not None, "Required property 'group_owner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_permission(self) -> builtins.str:
            '''The permissions that the group owner has to the machine learning resource.

            Valid values are ``rw`` (read-write) or ``ro`` (read-only).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinitionversion-resourcedownloadownersetting-grouppermission
            '''
            result = self._values.get("group_permission")
            assert result is not None, "Required property 'group_permission' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceDownloadOwnerSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.ResourceInstanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "name": "name",
            "resource_data_container": "resourceDataContainer",
        },
    )
    class ResourceInstanceProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            name: builtins.str,
            resource_data_container: typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.ResourceDataContainerProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A local resource, machine learning resource, or secret resource.

            For more information, see `Access Local Resources with Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html>`_ , `Perform Machine Learning Inference <https://docs.aws.amazon.com/greengrass/latest/developerguide/ml-inference.html>`_ , and `Deploy Secrets to the AWS IoT Greengrass Core <https://docs.aws.amazon.com/greengrass/latest/developerguide/secrets.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, the ``Resources`` property of the ```AWS::Greengrass::ResourceDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html>`_ resource contains a list of ``ResourceInstance`` property types.

            :param id: A descriptive or arbitrary ID for the resource. This value must be unique within the resource definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param name: The descriptive resource name, which is displayed on the AWS IoT Greengrass console. Maximum length 128 characters with pattern [a-zA-Z0-9:_-]+. This must be unique within a Greengrass group.
            :param resource_data_container: A container for resource data. The container takes only one of the following supported resource data types: ``LocalDeviceResourceData`` , ``LocalVolumeResourceData`` , ``SageMakerMachineLearningModelResourceData`` , ``S3MachineLearningModelResourceData`` , or ``SecretsManagerSecretResourceData`` . .. epigraph:: Only one resource type can be defined for a ``ResourceDataContainer`` instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                resource_instance_property = greengrass.CfnResourceDefinitionVersion.ResourceInstanceProperty(
                    id="id",
                    name="name",
                    resource_data_container=greengrass.CfnResourceDefinitionVersion.ResourceDataContainerProperty(
                        local_device_resource_data=greengrass.CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty(
                            source_path="sourcePath",
                
                            # the properties below are optional
                            group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                                auto_add_group_owner=False,
                
                                # the properties below are optional
                                group_owner="groupOwner"
                            )
                        ),
                        local_volume_resource_data=greengrass.CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty(
                            destination_path="destinationPath",
                            source_path="sourcePath",
                
                            # the properties below are optional
                            group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                                auto_add_group_owner=False,
                
                                # the properties below are optional
                                group_owner="groupOwner"
                            )
                        ),
                        s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty(
                            destination_path="destinationPath",
                            s3_uri="s3Uri",
                
                            # the properties below are optional
                            owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                                group_owner="groupOwner",
                                group_permission="groupPermission"
                            )
                        ),
                        sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty(
                            destination_path="destinationPath",
                            sage_maker_job_arn="sageMakerJobArn",
                
                            # the properties below are optional
                            owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                                group_owner="groupOwner",
                                group_permission="groupPermission"
                            )
                        ),
                        secrets_manager_secret_resource_data=greengrass.CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty(
                            arn="arn",
                
                            # the properties below are optional
                            additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fabb819cca9f473b88a301180b791a2610681e8c3e39303f273979230419cbb1)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument resource_data_container", value=resource_data_container, expected_type=type_hints["resource_data_container"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "name": name,
                "resource_data_container": resource_data_container,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the resource.

            This value must be unique within the resource definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The descriptive resource name, which is displayed on the AWS IoT Greengrass console.

            Maximum length 128 characters with pattern [a-zA-Z0-9:_-]+. This must be unique within a Greengrass group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_data_container(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceDataContainerProperty"]:
            '''A container for resource data.

            The container takes only one of the following supported resource data types: ``LocalDeviceResourceData`` , ``LocalVolumeResourceData`` , ``SageMakerMachineLearningModelResourceData`` , ``S3MachineLearningModelResourceData`` , or ``SecretsManagerSecretResourceData`` .
            .. epigraph::

               Only one resource type can be defined for a ``ResourceDataContainer`` instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-resourcedatacontainer
            '''
            result = self._values.get("resource_data_container")
            assert result is not None, "Required property 'resource_data_container' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceDataContainerProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceInstanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_path": "destinationPath",
            "s3_uri": "s3Uri",
            "owner_setting": "ownerSetting",
        },
    )
    class S3MachineLearningModelResourceDataProperty:
        def __init__(
            self,
            *,
            destination_path: builtins.str,
            s3_uri: builtins.str,
            owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for an Amazon S3 machine learning resource.

            For more information, see `Perform Machine Learning Inference <https://docs.aws.amazon.com/greengrass/latest/developerguide/ml-inference.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``S3MachineLearningModelResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html>`_ property type.

            :param destination_path: The absolute local path of the resource inside the Lambda environment.
            :param s3_uri: The URI of the source model in an Amazon S3 bucket. The model package must be in ``tar.gz`` or ``.zip`` format.
            :param owner_setting: The owner setting for the downloaded machine learning resource. For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                s3_machine_learning_model_resource_data_property = greengrass.CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty(
                    destination_path="destinationPath",
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                        group_owner="groupOwner",
                        group_permission="groupPermission"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7db5c429251ce7c49fb1d990fb9ac0519fcc4eb330460a7b1fe8b12ce83f3500)
                check_type(argname="argument destination_path", value=destination_path, expected_type=type_hints["destination_path"])
                check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
                check_type(argname="argument owner_setting", value=owner_setting, expected_type=type_hints["owner_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_path": destination_path,
                "s3_uri": s3_uri,
            }
            if owner_setting is not None:
                self._values["owner_setting"] = owner_setting

        @builtins.property
        def destination_path(self) -> builtins.str:
            '''The absolute local path of the resource inside the Lambda environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-destinationpath
            '''
            result = self._values.get("destination_path")
            assert result is not None, "Required property 'destination_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''The URI of the source model in an Amazon S3 bucket.

            The model package must be in ``tar.gz`` or ``.zip`` format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def owner_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty"]]:
            '''The owner setting for the downloaded machine learning resource.

            For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-ownersetting
            '''
            result = self._values.get("owner_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3MachineLearningModelResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_path": "destinationPath",
            "sage_maker_job_arn": "sageMakerJobArn",
            "owner_setting": "ownerSetting",
        },
    )
    class SageMakerMachineLearningModelResourceDataProperty:
        def __init__(
            self,
            *,
            destination_path: builtins.str,
            sage_maker_job_arn: builtins.str,
            owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for an Secrets Manager machine learning resource.

            For more information, see `Perform Machine Learning Inference <https://docs.aws.amazon.com/greengrass/latest/developerguide/ml-inference.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``SageMakerMachineLearningModelResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html>`_ property type.

            :param destination_path: The absolute local path of the resource inside the Lambda environment.
            :param sage_maker_job_arn: The Amazon Resource Name (ARN) of the Amazon SageMaker training job that represents the source model.
            :param owner_setting: The owner setting for the downloaded machine learning resource. For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                sage_maker_machine_learning_model_resource_data_property = greengrass.CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty(
                    destination_path="destinationPath",
                    sage_maker_job_arn="sageMakerJobArn",
                
                    # the properties below are optional
                    owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                        group_owner="groupOwner",
                        group_permission="groupPermission"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__733b10b4c3a727471582d5422b71ecf16f8bc7480a54f897d6d6167da4004e7d)
                check_type(argname="argument destination_path", value=destination_path, expected_type=type_hints["destination_path"])
                check_type(argname="argument sage_maker_job_arn", value=sage_maker_job_arn, expected_type=type_hints["sage_maker_job_arn"])
                check_type(argname="argument owner_setting", value=owner_setting, expected_type=type_hints["owner_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_path": destination_path,
                "sage_maker_job_arn": sage_maker_job_arn,
            }
            if owner_setting is not None:
                self._values["owner_setting"] = owner_setting

        @builtins.property
        def destination_path(self) -> builtins.str:
            '''The absolute local path of the resource inside the Lambda environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-destinationpath
            '''
            result = self._values.get("destination_path")
            assert result is not None, "Required property 'destination_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sage_maker_job_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon SageMaker training job that represents the source model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-sagemakerjobarn
            '''
            result = self._values.get("sage_maker_job_arn")
            assert result is not None, "Required property 'sage_maker_job_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def owner_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty"]]:
            '''The owner setting for the downloaded machine learning resource.

            For more information, see `Access Machine Learning Resources from Lambda Functions <https://docs.aws.amazon.com/greengrass/latest/developerguide/access-ml-resources.html>`_ in the *Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-ownersetting
            '''
            result = self._values.get("owner_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SageMakerMachineLearningModelResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "additional_staging_labels_to_download": "additionalStagingLabelsToDownload",
        },
    )
    class SecretsManagerSecretResourceDataProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            additional_staging_labels_to_download: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Settings for a secret resource, which references a secret from AWS Secrets Manager .

            AWS IoT Greengrass stores a local, encrypted copy of the secret on the Greengrass core, where it can be securely accessed by connectors and Lambda functions. For more information, see `Deploy Secrets to the AWS IoT Greengrass Core <https://docs.aws.amazon.com/greengrass/latest/developerguide/secrets.html>`_ in the *Developer Guide* .

            In an AWS CloudFormation template, ``SecretsManagerSecretResourceData`` can be used in the ```ResourceDataContainer`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html>`_ property type.

            :param arn: The Amazon Resource Name (ARN) of the Secrets Manager secret to make available on the core. The value of the secret's latest version (represented by the ``AWSCURRENT`` staging label) is included by default.
            :param additional_staging_labels_to_download: The staging labels whose values you want to make available on the core, in addition to ``AWSCURRENT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                secrets_manager_secret_resource_data_property = greengrass.CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty(
                    arn="arn",
                
                    # the properties below are optional
                    additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42b5f8b52b565c9d97f0c8313cdb4b5f55c17c63cd32aa5bdc087f665e4894a2)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument additional_staging_labels_to_download", value=additional_staging_labels_to_download, expected_type=type_hints["additional_staging_labels_to_download"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
            }
            if additional_staging_labels_to_download is not None:
                self._values["additional_staging_labels_to_download"] = additional_staging_labels_to_download

        @builtins.property
        def arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Secrets Manager secret to make available on the core.

            The value of the secret's latest version (represented by the ``AWSCURRENT`` staging label) is included by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def additional_staging_labels_to_download(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The staging labels whose values you want to make available on the core, in addition to ``AWSCURRENT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-additionalstaginglabelstodownload
            '''
            result = self._values.get("additional_staging_labels_to_download")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretsManagerSecretResourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnResourceDefinitionVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_definition_id": "resourceDefinitionId",
        "resources": "resources",
    },
)
class CfnResourceDefinitionVersionProps:
    def __init__(
        self,
        *,
        resource_definition_id: builtins.str,
        resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.ResourceInstanceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnResourceDefinitionVersion``.

        :param resource_definition_id: The ID of the resource definition associated with this version. This value is a GUID.
        :param resources: The resources in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            cfn_resource_definition_version_props = greengrass.CfnResourceDefinitionVersionProps(
                resource_definition_id="resourceDefinitionId",
                resources=[greengrass.CfnResourceDefinitionVersion.ResourceInstanceProperty(
                    id="id",
                    name="name",
                    resource_data_container=greengrass.CfnResourceDefinitionVersion.ResourceDataContainerProperty(
                        local_device_resource_data=greengrass.CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty(
                            source_path="sourcePath",
            
                            # the properties below are optional
                            group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                                auto_add_group_owner=False,
            
                                # the properties below are optional
                                group_owner="groupOwner"
                            )
                        ),
                        local_volume_resource_data=greengrass.CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty(
                            destination_path="destinationPath",
                            source_path="sourcePath",
            
                            # the properties below are optional
                            group_owner_setting=greengrass.CfnResourceDefinitionVersion.GroupOwnerSettingProperty(
                                auto_add_group_owner=False,
            
                                # the properties below are optional
                                group_owner="groupOwner"
                            )
                        ),
                        s3_machine_learning_model_resource_data=greengrass.CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty(
                            destination_path="destinationPath",
                            s3_uri="s3Uri",
            
                            # the properties below are optional
                            owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                                group_owner="groupOwner",
                                group_permission="groupPermission"
                            )
                        ),
                        sage_maker_machine_learning_model_resource_data=greengrass.CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty(
                            destination_path="destinationPath",
                            sage_maker_job_arn="sageMakerJobArn",
            
                            # the properties below are optional
                            owner_setting=greengrass.CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty(
                                group_owner="groupOwner",
                                group_permission="groupPermission"
                            )
                        ),
                        secrets_manager_secret_resource_data=greengrass.CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty(
                            arn="arn",
            
                            # the properties below are optional
                            additional_staging_labels_to_download=["additionalStagingLabelsToDownload"]
                        )
                    )
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92f249a2f06545b4d2c57aa9e2ac98fd23d4647ebf0ab39624e1bc81c067b427)
            check_type(argname="argument resource_definition_id", value=resource_definition_id, expected_type=type_hints["resource_definition_id"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_definition_id": resource_definition_id,
            "resources": resources,
        }

    @builtins.property
    def resource_definition_id(self) -> builtins.str:
        '''The ID of the resource definition associated with this version.

        This value is a GUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html#cfn-greengrass-resourcedefinitionversion-resourcedefinitionid
        '''
        result = self._values.get("resource_definition_id")
        assert result is not None, "Required property 'resource_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resources(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResourceDefinitionVersion.ResourceInstanceProperty]]]:
        '''The resources in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html#cfn-greengrass-resourcedefinitionversion-resources
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResourceDefinitionVersion.ResourceInstanceProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceDefinitionVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSubscriptionDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnSubscriptionDefinition",
):
    '''The ``AWS::Greengrass::SubscriptionDefinition`` resource represents a subscription definition for AWS IoT Greengrass .

    Subscription definitions are used to organize your subscription definition versions.

    Subscription definitions can reference multiple subscription definition versions. All subscription definition versions must be associated with a subscription definition. Each subscription definition version can contain one or more subscriptions.
    .. epigraph::

       When you create a subscription definition, you can optionally include an initial subscription definition version. To associate a subscription definition version later, create an ```AWS::Greengrass::SubscriptionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html>`_ resource and specify the ID of this subscription definition.

       After you create the subscription definition version that contains the subscriptions you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        # tags: Any
        
        cfn_subscription_definition = greengrass.CfnSubscriptionDefinition(self, "MyCfnSubscriptionDefinition",
            name="name",
        
            # the properties below are optional
            initial_version=greengrass.CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty(
                subscriptions=[greengrass.CfnSubscriptionDefinition.SubscriptionProperty(
                    id="id",
                    source="source",
                    subject="subject",
                    target="target"
                )]
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the subscription definition.
        :param initial_version: The subscription definition version to include when the subscription definition is created. A subscription definition version contains a list of ```subscription`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html>`_ property types. .. epigraph:: To associate a subscription definition version after the subscription definition is created, create an ```AWS::Greengrass::SubscriptionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html>`_ resource and specify the ID of this subscription definition.
        :param tags: Application-specific metadata to attach to the subscription definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b231a8b03315437dd52b155f4e7c1d32a92f2a3b0e6f37ae1bfae2e72938fb22)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriptionDefinitionProps(
            name=name, initial_version=initial_version, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3b55b221d1074330e22fd2822066e10cb57a859717ce6d479ff80b008c96af7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95b6fd2bcdb28de44a008408c98ea58d67bc1442faa5d9fa707802f568ddb1d2)
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
        '''The Amazon Resource Name (ARN) of the ``SubscriptionDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/subscriptions/1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the ``SubscriptionDefinition`` , such as ``1234a5b6-78cd-901e-2fgh-3i45j6k178l9`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersionArn")
    def attr_latest_version_arn(self) -> builtins.str:
        '''The ARN of the last ``SubscriptionDefinitionVersion`` that was added to the ``SubscriptionDefinition`` , such as ``arn:aws:greengrass:us-east-1:  :/greengrass/definition/subscriptions/1234a5b6-78cd-901e-2fgh-3i45j6k178l9/versions/9876ac30-4bdb-4f9d-95af-b5fdb66be1a2`` .

        :cloudformationAttribute: LatestVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the ``SubscriptionDefinition`` , such as ``MySubscriptionDefinition`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''The name of the subscription definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7419a41b1a2fd9cbc8893cf41814a9d4402f8bbf4b3926c9d4eae1050a3cb2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="initialVersion")
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty"]]:
        '''The subscription definition version to include when the subscription definition is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty"]], jsii.get(self, "initialVersion"))

    @initial_version.setter
    def initial_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb5bd9630745b54bebd6a65c27d16ed4621705d8b40d785efc3fcf8eda69d66a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''Application-specific metadata to attach to the subscription definition.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3c68b21f52fe99f3d6a88bd9e881c4d030dd6c2bef09d8ac0a05a8c5ff59c37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"subscriptions": "subscriptions"},
    )
    class SubscriptionDefinitionVersionProperty:
        def __init__(
            self,
            *,
            subscriptions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriptionDefinition.SubscriptionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A subscription definition version contains a list of `subscriptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html>`_ .

            .. epigraph::

               After you create a subscription definition version that contains the subscriptions you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

            In an AWS CloudFormation template, ``SubscriptionDefinitionVersion`` is the property type of the ``InitialVersion`` property in the ```AWS::Greengrass::SubscriptionDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html>`_ resource.

            :param subscriptions: The subscriptions in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                subscription_definition_version_property = greengrass.CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty(
                    subscriptions=[greengrass.CfnSubscriptionDefinition.SubscriptionProperty(
                        id="id",
                        source="source",
                        subject="subject",
                        target="target"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd466a90e730b214d5682e7f3c520c2a2084f5919c5b4a34dc43d11ebd863f01)
                check_type(argname="argument subscriptions", value=subscriptions, expected_type=type_hints["subscriptions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subscriptions": subscriptions,
            }

        @builtins.property
        def subscriptions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionDefinition.SubscriptionProperty"]]]:
            '''The subscriptions in this version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinition-subscriptiondefinitionversion-subscriptions
            '''
            result = self._values.get("subscriptions")
            assert result is not None, "Required property 'subscriptions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionDefinition.SubscriptionProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriptionDefinitionVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnSubscriptionDefinition.SubscriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "source": "source",
            "subject": "subject",
            "target": "target",
        },
    )
    class SubscriptionProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            source: builtins.str,
            subject: builtins.str,
            target: builtins.str,
        ) -> None:
            '''Subscriptions define how MQTT messages can be exchanged between devices, functions, and connectors in the group, and with AWS IoT or the local shadow service.

            A subscription defines a message source, message target, and a topic (or subject) that's used to route messages from the source to the target. A subscription defines the message flow in one direction, from the source to the target. For two-way communication, you must set up two subscriptions, one for each direction.

            In an AWS CloudFormation template, the ``Subscriptions`` property of the ```SubscriptionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html>`_ property type contains a list of ``Subscription`` property types.

            :param id: A descriptive or arbitrary ID for the subscription. This value must be unique within the subscription definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param source: The originator of the message. The value can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, ``cloud`` (which represents the AWS IoT cloud), or ``GGShadowService`` .
            :param subject: The MQTT topic used to route the message.
            :param target: The destination of the message. The value can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, ``cloud`` (which represents the AWS IoT cloud), or ``GGShadowService`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                subscription_property = greengrass.CfnSubscriptionDefinition.SubscriptionProperty(
                    id="id",
                    source="source",
                    subject="subject",
                    target="target"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b7552743b0092a7b8371fc4c1a1476bd190cbed44e48e0e59b996d8305d666b)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "source": source,
                "subject": subject,
                "target": target,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the subscription.

            This value must be unique within the subscription definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''The originator of the message.

            The value can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, ``cloud`` (which represents the AWS IoT cloud), or ``GGShadowService`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subject(self) -> builtins.str:
            '''The MQTT topic used to route the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-subject
            '''
            result = self._values.get("subject")
            assert result is not None, "Required property 'subject' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''The destination of the message.

            The value can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, ``cloud`` (which represents the AWS IoT cloud), or ``GGShadowService`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnSubscriptionDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "initial_version": "initialVersion", "tags": "tags"},
)
class CfnSubscriptionDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscriptionDefinition``.

        :param name: The name of the subscription definition.
        :param initial_version: The subscription definition version to include when the subscription definition is created. A subscription definition version contains a list of ```subscription`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html>`_ property types. .. epigraph:: To associate a subscription definition version after the subscription definition is created, create an ```AWS::Greengrass::SubscriptionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html>`_ resource and specify the ID of this subscription definition.
        :param tags: Application-specific metadata to attach to the subscription definition. You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* . This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates:: "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value" }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            # tags: Any
            
            cfn_subscription_definition_props = greengrass.CfnSubscriptionDefinitionProps(
                name="name",
            
                # the properties below are optional
                initial_version=greengrass.CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty(
                    subscriptions=[greengrass.CfnSubscriptionDefinition.SubscriptionProperty(
                        id="id",
                        source="source",
                        subject="subject",
                        target="target"
                    )]
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ca5b663a9b0488d2381e662e60281bd0082829ce52f3a587e6f8294d7745d98)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument initial_version", value=initial_version, expected_type=type_hints["initial_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if initial_version is not None:
            self._values["initial_version"] = initial_version
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the subscription definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty]]:
        '''The subscription definition version to include when the subscription definition is created.

        A subscription definition version contains a list of ```subscription`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html>`_ property types.
        .. epigraph::

           To associate a subscription definition version after the subscription definition is created, create an ```AWS::Greengrass::SubscriptionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html>`_ resource and specify the ID of this subscription definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-initialversion
        '''
        result = self._values.get("initial_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Application-specific metadata to attach to the subscription definition.

        You can use tags in IAM policies to control access to AWS IoT Greengrass resources. You can also use tags to categorize your resources. For more information, see `Tagging Your AWS IoT Greengrass Resources <https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html>`_ in the *Developer Guide* .

        This ``Json`` property type is processed as a map of key-value pairs. It uses the following format, which is different from most ``Tags`` implementations in AWS CloudFormation templates::

           "Tags": { "KeyName0": "value", "KeyName1": "value", "KeyName2": "value"
           }

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriptionDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSubscriptionDefinitionVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_greengrass.CfnSubscriptionDefinitionVersion",
):
    '''The ``AWS::Greengrass::SubscriptionDefinitionVersion`` resource represents a subscription definition version for AWS IoT Greengrass .

    A subscription definition version contains a list of subscriptions.
    .. epigraph::

       To create a subscription definition version, you must specify the ID of the subscription definition that you want to associate with the version. For information about creating a subscription definition, see ```AWS::Greengrass::SubscriptionDefinition`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html>`_ .

       After you create a subscription definition version that contains the subscriptions you want to deploy, you must add it to your group version. For more information, see ```AWS::Greengrass::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_greengrass as greengrass
        
        cfn_subscription_definition_version = greengrass.CfnSubscriptionDefinitionVersion(self, "MyCfnSubscriptionDefinitionVersion",
            subscription_definition_id="subscriptionDefinitionId",
            subscriptions=[greengrass.CfnSubscriptionDefinitionVersion.SubscriptionProperty(
                id="id",
                source="source",
                subject="subject",
                target="target"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        subscription_definition_id: builtins.str,
        subscriptions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriptionDefinitionVersion.SubscriptionProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param subscription_definition_id: The ID of the subscription definition associated with this version. This value is a GUID.
        :param subscriptions: The subscriptions in this version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__196d53b9c9e2e632eb88d7a7f73e15b80a4e83c869df484747f40505cd07b62a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriptionDefinitionVersionProps(
            subscription_definition_id=subscription_definition_id,
            subscriptions=subscriptions,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f5cbbce137768ad4bc517ba5824ec70d35a12d68a33dcc26d9f212c7554f8d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__74274a470594f3024a0879f542f07460bf8dbc14aba0fa410317cbfb126bf38f)
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
    @jsii.member(jsii_name="subscriptionDefinitionId")
    def subscription_definition_id(self) -> builtins.str:
        '''The ID of the subscription definition associated with this version.'''
        return typing.cast(builtins.str, jsii.get(self, "subscriptionDefinitionId"))

    @subscription_definition_id.setter
    def subscription_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9eaeca2366167091d0a98772cb6ca7a6cc6e0b9cb92f4e5f40dbbe066f0768e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptions")
    def subscriptions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionDefinitionVersion.SubscriptionProperty"]]]:
        '''The subscriptions in this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionDefinitionVersion.SubscriptionProperty"]]], jsii.get(self, "subscriptions"))

    @subscriptions.setter
    def subscriptions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionDefinitionVersion.SubscriptionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba4cd67c8807aa76b5b15f0cc7031c8c93e9db957d1dcbe2f07f9d22c3d9b57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_greengrass.CfnSubscriptionDefinitionVersion.SubscriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "source": "source",
            "subject": "subject",
            "target": "target",
        },
    )
    class SubscriptionProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            source: builtins.str,
            subject: builtins.str,
            target: builtins.str,
        ) -> None:
            '''Subscriptions define how MQTT messages can be exchanged between devices, functions, and connectors in the group, and with AWS IoT or the local shadow service.

            A subscription defines a message source, message target, and a topic (or subject) that's used to route messages from the source to the target. A subscription defines the message flow in one direction, from the source to the target. For two-way communication, you must set up two subscriptions, one for each direction.

            In an AWS CloudFormation template, the ``Subscriptions`` property of the ```AWS::Greengrass::SubscriptionDefinitionVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html>`_ resource contains a list of ``Subscription`` property types.

            :param id: A descriptive or arbitrary ID for the subscription. This value must be unique within the subscription definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .
            :param source: The originator of the message. The value can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, ``cloud`` (which represents the AWS IoT cloud), or ``GGShadowService`` .
            :param subject: The MQTT topic used to route the message.
            :param target: The destination of the message. The value can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, ``cloud`` (which represents the AWS IoT cloud), or ``GGShadowService`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_greengrass as greengrass
                
                subscription_property = greengrass.CfnSubscriptionDefinitionVersion.SubscriptionProperty(
                    id="id",
                    source="source",
                    subject="subject",
                    target="target"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d3123a4ba54f33ea17e4d551e1741ceae6c3e217ae977d2d28f5c60c81ab526)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "source": source,
                "subject": subject,
                "target": target,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''A descriptive or arbitrary ID for the subscription.

            This value must be unique within the subscription definition version. Maximum length is 128 characters with pattern ``[a-zA-Z0-9:_-]+`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''The originator of the message.

            The value can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, ``cloud`` (which represents the AWS IoT cloud), or ``GGShadowService`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subject(self) -> builtins.str:
            '''The MQTT topic used to route the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-subject
            '''
            result = self._values.get("subject")
            assert result is not None, "Required property 'subject' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''The destination of the message.

            The value can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, ``cloud`` (which represents the AWS IoT cloud), or ``GGShadowService`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_greengrass.CfnSubscriptionDefinitionVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "subscription_definition_id": "subscriptionDefinitionId",
        "subscriptions": "subscriptions",
    },
)
class CfnSubscriptionDefinitionVersionProps:
    def __init__(
        self,
        *,
        subscription_definition_id: builtins.str,
        subscriptions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionDefinitionVersion.SubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnSubscriptionDefinitionVersion``.

        :param subscription_definition_id: The ID of the subscription definition associated with this version. This value is a GUID.
        :param subscriptions: The subscriptions in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_greengrass as greengrass
            
            cfn_subscription_definition_version_props = greengrass.CfnSubscriptionDefinitionVersionProps(
                subscription_definition_id="subscriptionDefinitionId",
                subscriptions=[greengrass.CfnSubscriptionDefinitionVersion.SubscriptionProperty(
                    id="id",
                    source="source",
                    subject="subject",
                    target="target"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d59bb5054d104f51e689b37a46da9774e6b1e1bc38b16496ca8bf4a7ce90c8)
            check_type(argname="argument subscription_definition_id", value=subscription_definition_id, expected_type=type_hints["subscription_definition_id"])
            check_type(argname="argument subscriptions", value=subscriptions, expected_type=type_hints["subscriptions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscription_definition_id": subscription_definition_id,
            "subscriptions": subscriptions,
        }

    @builtins.property
    def subscription_definition_id(self) -> builtins.str:
        '''The ID of the subscription definition associated with this version.

        This value is a GUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinitionversion-subscriptiondefinitionid
        '''
        result = self._values.get("subscription_definition_id")
        assert result is not None, "Required property 'subscription_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscriptions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionDefinitionVersion.SubscriptionProperty]]]:
        '''The subscriptions in this version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinitionversion-subscriptions
        '''
        result = self._values.get("subscriptions")
        assert result is not None, "Required property 'subscriptions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionDefinitionVersion.SubscriptionProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriptionDefinitionVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnectorDefinition",
    "CfnConnectorDefinitionProps",
    "CfnConnectorDefinitionVersion",
    "CfnConnectorDefinitionVersionProps",
    "CfnCoreDefinition",
    "CfnCoreDefinitionProps",
    "CfnCoreDefinitionVersion",
    "CfnCoreDefinitionVersionProps",
    "CfnDeviceDefinition",
    "CfnDeviceDefinitionProps",
    "CfnDeviceDefinitionVersion",
    "CfnDeviceDefinitionVersionProps",
    "CfnFunctionDefinition",
    "CfnFunctionDefinitionProps",
    "CfnFunctionDefinitionVersion",
    "CfnFunctionDefinitionVersionProps",
    "CfnGroup",
    "CfnGroupProps",
    "CfnGroupVersion",
    "CfnGroupVersionProps",
    "CfnLoggerDefinition",
    "CfnLoggerDefinitionProps",
    "CfnLoggerDefinitionVersion",
    "CfnLoggerDefinitionVersionProps",
    "CfnResourceDefinition",
    "CfnResourceDefinitionProps",
    "CfnResourceDefinitionVersion",
    "CfnResourceDefinitionVersionProps",
    "CfnSubscriptionDefinition",
    "CfnSubscriptionDefinitionProps",
    "CfnSubscriptionDefinitionVersion",
    "CfnSubscriptionDefinitionVersionProps",
]

publication.publish()

def _typecheckingstub__481b9a854466614791f45d6769989966b8f812de4d4fa3e31d53b297fc3cf25a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorDefinition.ConnectorDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24c07fb6ad50afe14bef1d7010d53ca0ed36ba7ee67a12442f8fefe27c993eb3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__274c71989e410af72c071839e2a648c2c533621f117a8c0e486c9527e7470195(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab45f89ff0cfe141f0220b75cd71c3d899658dfb0c0d902360ceac2645761b8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0415a38346fbe03d6f5624bc1964761ae159cabc533cd2810f1187fb94a9e76e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectorDefinition.ConnectorDefinitionVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60332b2bd3d1f19c86feea95dba6bf261745105b22e69096e4be69004bdad03b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ebd178e9a062570c1b341d7167254254483a31aa5611c9784ea999dbf17f21(
    *,
    connectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorDefinition.ConnectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9296d577ecfbbed3bc2c2debdad72ad7c40138384002b64be6231a4a65308aec(
    *,
    connector_arn: builtins.str,
    id: builtins.str,
    parameters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c11896c87152b58a2cacd3ad90176b83e130f066bfcc0c1caf54e71e272e5c6c(
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorDefinition.ConnectorDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b0440a60203f7d65611b69dca729e027a591c6aa92f00dc0aebb40960143af(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connector_definition_id: builtins.str,
    connectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorDefinitionVersion.ConnectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28930916b9351f935867712c00b802adf7b173a69fafdb3c311d8cd529a223ce(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bda14e12f8fd37f15240b23bb63562be66f84404eec1690445f8ff0f960d0321(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46572beae401fe5e838cb0b02ec437b067f98ac0ae5835d7ef8ce870c4ac7d90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed3abea511a407254df28d178fbfb71f43dee9315c0aeca3095f062663236ce(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConnectorDefinitionVersion.ConnectorProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d59c31c39abe32b4f18b9663d07cf39015d1cce8e87ebaa475937de0f283249d(
    *,
    connector_arn: builtins.str,
    id: builtins.str,
    parameters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c795265270b52b4f10228be7f4015f471c0c0039915e2b229a19aea56195a3(
    *,
    connector_definition_id: builtins.str,
    connectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorDefinitionVersion.ConnectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7fe5635b210e6632e07b82d21d8907b6d36d805b6d4fb2198f0433417d780a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCoreDefinition.CoreDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64368dbb58b3df35d74d10a3113a88fb2dc06fc0237665e15968f378a8fbbd09(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b38774760bbfa1d8286cc0bcbc098a0bc3dccc52ef7c7d0390f236a771e6087(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac51622030b12c5c1ad466a72f36fc6ae109a83246daf2e9b37011f5db34b4b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92abb907cfcf9216f792b317f8eb26a0b6c421a027b2e96eefee9e1fd17d6fc7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCoreDefinition.CoreDefinitionVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99697b8dad691477ff836e154bb3c9f516a73f2882f23a90d55ddc3f167aadd8(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ef4f67c3c3830d5b5644db7ec3e809f18d3cab655c6a7fd98232bccd93382e3(
    *,
    cores: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCoreDefinition.CoreProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d7e03cdaed925e2b5ec8c65e84a5b6cf10c5209e1d1de097ab201c492621ce(
    *,
    certificate_arn: builtins.str,
    id: builtins.str,
    thing_arn: builtins.str,
    sync_shadow: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d8127b3c34b3abe01c8efbf62b499796f709f95bf91348e64a7ab4a0d7ac3c(
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCoreDefinition.CoreDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98b8071f110db36c2b93c49d75516709035bb93997aae3c35adc25c4ab4d53c3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    core_definition_id: builtins.str,
    cores: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCoreDefinitionVersion.CoreProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b4e0682ef4a26ccff2d2d377b87519933191b35ee2f3c927013cb65d537b304(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d9b9142f952fb03ff2494686a42ca4db8c5b291082063611639ee867890701(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce705d0cc1809364da37b409e24bfddfab55386d0858b4c4146d9a22a2a2f40a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1bffbbd7f9c7ce8f8528729042b02d09f335ab5562e19bf5da873a4a6ae6b05(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCoreDefinitionVersion.CoreProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e3ed0ad844b4ecbd124f2fc0f6fcb8c8ca64bd7f1b2ebe17ecf825baa15ea8(
    *,
    certificate_arn: builtins.str,
    id: builtins.str,
    thing_arn: builtins.str,
    sync_shadow: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5ee60cab94ef477682167b25261f01a298b6e5e0bece31e1df9370f3a2f790f(
    *,
    core_definition_id: builtins.str,
    cores: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCoreDefinitionVersion.CoreProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6388724d13149e0aad9e17e0abeb2962bcb4c5f435c6c0744dc4914379c75ae1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceDefinition.DeviceDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42b7b2748a017da66012466c961f889765dd501d6bce1063c38a88cf58c3f181(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5718b5621957658ebf68cf3e23503ef4a017494ec185b843a1c3fd424fb6f807(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2194bc46e61deb1c1fcc4553ae866524155d250a4d6110495f31209d88865d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860ed955c6c53de09524817b41d262c302d0a99f94c5e829c77f1df83b034260(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeviceDefinition.DeviceDefinitionVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa56b64210e79fff38ab545ae87d1988b94100fdbaa646f7ebeda88559aeeacb(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0c5ec14762edf351c870b2f17efb8d815ee293da253da248851bce6b21751ce(
    *,
    devices: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceDefinition.DeviceProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__812e639d6663b05c08a6e0a7e6aea0c4d9cb91c3144a1113dcbf3d7933594fa4(
    *,
    certificate_arn: builtins.str,
    id: builtins.str,
    thing_arn: builtins.str,
    sync_shadow: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7175e6a25a231dd04ec7fc7a8ba5222ad239e84c2555359e9e1779ee7dab007c(
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceDefinition.DeviceDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64493ebfeeb96fc14eb8e8054338af97e554d939f196f64d5d512c73ace31a93(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    device_definition_id: builtins.str,
    devices: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceDefinitionVersion.DeviceProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f75f076efee1cfe7e6a6aa35cffba776ede5eb8c3ebc6b05d12324b9ed098c8c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82c976f156be131579618e357fb04ee79c5fa16268fa8502ebebf331489243c8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81c0aa8405667eeeaadd67c78cb7b7ddd5bc27f106a564e32912851386e4931(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0aabdafe61d8e2100f8e9a731798871a20d7438db750e894f114287763994f9(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeviceDefinitionVersion.DeviceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253b05ead7f7258dbe7d542a3d84a1dcb9e7461853810ffd646f2efad7c3cd74(
    *,
    certificate_arn: builtins.str,
    id: builtins.str,
    thing_arn: builtins.str,
    sync_shadow: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ba582d02e3f46be1f7ffc866489e7b5768fda19646ac5cb6fb39be0cc3b7e09(
    *,
    device_definition_id: builtins.str,
    devices: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeviceDefinitionVersion.DeviceProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc054a16da2a52b953d26f46ac8928cd46a0d3b00ea138b637dba87125670b02(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.FunctionDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883759389b9b6062c199dfa06474e6b6eae814f3d29cb567a6c1accc041ac340(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5eb475f6df385b65a6fa5feebde3a756e64967f6ed1a1c94c355e0641d025d4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f3586ebd22c8d7efa859e3b07e7a1d59b40ead5bd2fcda78d352eb33e98b21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ef946c280aa3fe299d97090ecfb5dfa4af0a16702b75c593ec39701a3cb62b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinition.FunctionDefinitionVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de5a19ed9c188b2bb1a6eecf3c47192c7edf18069ffe0cdf6838d6eadee8effd(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8141acc3a004423bffa1be5752871f489d86a51c46b744ac79a869e6a745c4d4(
    *,
    execution: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.ExecutionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4292cc2a15784a3b0bab48fede867f394d01dc9f076e30078fc77deaf8381cc(
    *,
    access_sysfs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.ExecutionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_access_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.ResourceAccessPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    variables: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b70e9d861e6b33c0e42706480eb4da7187fb3ff64d5ada17a7940f9296fd2a9e(
    *,
    isolation_mode: typing.Optional[builtins.str] = None,
    run_as: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.RunAsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d434196f1da3f825c92283259908906d812252031be392844dfd7ad5a1d266(
    *,
    encoding_type: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.EnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    exec_args: typing.Optional[builtins.str] = None,
    executable: typing.Optional[builtins.str] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    pinned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cf2ab9fa59092d61d89f64ed51286c1ffbcc6ff91799c90c41d5102213f0f32(
    *,
    functions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.FunctionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.DefaultConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d06406f22f33062b37608c66ede16429af10bcb88224eaae6da351e8b512eb5(
    *,
    function_arn: builtins.str,
    function_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.FunctionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83ce8dcd35f15a7c52707cb20e4f653d274051d0b69be412461a84fde59d4747(
    *,
    resource_id: builtins.str,
    permission: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044b15bdedd91446b78ce0f57b82c3734bcbedd95c01454cdca47d61efccb494(
    *,
    gid: typing.Optional[jsii.Number] = None,
    uid: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e62d17dcf2bc0d49a9e8075057460e72eae2dd41694fd8988f7dfbd7bb507a(
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinition.FunctionDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74049a58818d8fb74724e45f074f2d356fba374467a1926758e3e761c205d756(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    function_definition_id: builtins.str,
    functions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.FunctionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.DefaultConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53d31f9160e02bf734beeedf9a11d142ba8858555d274b4c85da63595775c72(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea22062ecf7322056761cf0f4266b5142070757362434ce77d6180f10611daee(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089983427f200b57e702fff54bb0b007c29cdd60772ebee7e6374971f11b5d3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__793cfd87f23bbd9bf6e301d174c974540fcb771743c65e05c1a0a4025bf87005(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinitionVersion.FunctionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0390fd3aa93f9d9e878e662d53c38486d861c310d7e93ad7f1c0f86c70cee20c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionDefinitionVersion.DefaultConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfacedad0a59ccb5e2eaec7676b018b92ee6862f373104646bf110f388b3e418(
    *,
    execution: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.ExecutionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955f01f10cbdbbb5ea2b4005e2fdd4b4733b2c02fd34963370b597105324bef9(
    *,
    access_sysfs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.ExecutionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_access_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.ResourceAccessPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    variables: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d250f03acfa6e718d9c76fc540c990c972324de4f76328354b14aa9eb0e6788(
    *,
    isolation_mode: typing.Optional[builtins.str] = None,
    run_as: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.RunAsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0305775d160fba73e4f75590e6bf752341fc5c40b45ed63434363b50709bf554(
    *,
    encoding_type: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.EnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    exec_args: typing.Optional[builtins.str] = None,
    executable: typing.Optional[builtins.str] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    pinned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a9205f2a39c9362a5f7f6b72de2b4c074656b9c7a7c287a91949ece94cf5dd(
    *,
    function_arn: builtins.str,
    function_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.FunctionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0c05252ba2866efa6819404f70d8c46ab9150857916aa6aabac49f53006c7b(
    *,
    resource_id: builtins.str,
    permission: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ebc14c39db2ef6662e5e8568947f430b45c6b165cfdcb6f5bd1a30fcf649a1b(
    *,
    gid: typing.Optional[jsii.Number] = None,
    uid: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e693fe342b550c60e306daaf34fb60a94c43637b204bde675069e2c09f0356(
    *,
    function_definition_id: builtins.str,
    functions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.FunctionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionDefinitionVersion.DefaultConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726a7d2c4960c5df3ad6e991be61efa251e71f218d0d72f1df21a3c5903ebe7f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.GroupVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1154c99a9c32510d4c5f12de88ee6aa74b4b71171411ee6688346f3c78d26e8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__371d9153ea3fc52290ce86f5a599394cc2955ebf44fd35dce75ed6aa04a4cb03(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea2b1b818ef0cc72e4ff310dbf9eae157f92e5c04d08514478628c08a3dc867(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a38b6bf42dcdd50e398f34bf87a366c206fb7d56a14edcfa088d38beb0169bc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGroup.GroupVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6675e04cf0ab21e346afb29e4e19bde19ea87ea432acc7787de29c5be10f7aa2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf681fed500903d683fa2fe379335268fbe2011999bfef05177c39ea864332eb(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23017f69761595410cb920f0188f7bac8a8a1c92bdabee3f081b74455da416fb(
    *,
    connector_definition_version_arn: typing.Optional[builtins.str] = None,
    core_definition_version_arn: typing.Optional[builtins.str] = None,
    device_definition_version_arn: typing.Optional[builtins.str] = None,
    function_definition_version_arn: typing.Optional[builtins.str] = None,
    logger_definition_version_arn: typing.Optional[builtins.str] = None,
    resource_definition_version_arn: typing.Optional[builtins.str] = None,
    subscription_definition_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__296d900be2eff5ceb398f72dfd0a58896e12fd04dd28f102a076e92f456cb9a4(
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.GroupVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e429513d4ed5c36de946aa9233f1743627bcb10cb35191a8cf2b05862bf588(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_id: builtins.str,
    connector_definition_version_arn: typing.Optional[builtins.str] = None,
    core_definition_version_arn: typing.Optional[builtins.str] = None,
    device_definition_version_arn: typing.Optional[builtins.str] = None,
    function_definition_version_arn: typing.Optional[builtins.str] = None,
    logger_definition_version_arn: typing.Optional[builtins.str] = None,
    resource_definition_version_arn: typing.Optional[builtins.str] = None,
    subscription_definition_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2069ae3c84e6655780c7b21f27d46fb1bee9a88231128d102cc86e616b776fa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e6e203e326396ee46b6f09d4950a4f2a60460aab9dd7801a5e998d496f282a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b70513b04a0647c95bbd78b71c611749688212d95d6b7f6be24e153474ced833(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b4083383be53e8192919e7978982b4c98f55ff47f025a1a51181578579b3852(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64b7407ff4176f922aa431270cee22c78db47ad08a470b616f3102fe257bdb2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af68e21601bf6750c71f6f0c2bc6538974bed68a360dd4d6148cec732594fb4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bafc0081999bcf69f5529249f5611a5bfac796128da383e18f805601ef9f7d1b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e34a3066bf41e65e71062cbc53c28ee0f3c8407b337545091f2f03096c48c2aa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a37b5dcc0ee3133f870c3a3fe994fa624423839bc6ae69bf0187a55c1045179(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__401c05e2b55805214eb63cf50bc055afc162c24db366d22d1d8583f411101e56(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3002e50fbbeb611ff50e6124b7f721785d0d1114fac032b39ef5434324657b48(
    *,
    group_id: builtins.str,
    connector_definition_version_arn: typing.Optional[builtins.str] = None,
    core_definition_version_arn: typing.Optional[builtins.str] = None,
    device_definition_version_arn: typing.Optional[builtins.str] = None,
    function_definition_version_arn: typing.Optional[builtins.str] = None,
    logger_definition_version_arn: typing.Optional[builtins.str] = None,
    resource_definition_version_arn: typing.Optional[builtins.str] = None,
    subscription_definition_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3141ac6c65d7407c94dc3062e91bf204de61524d95c83b87b6aab3da0639d32(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggerDefinition.LoggerDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca6d7f3da4fbad4f376abd5d28521fed1cf98cbc7b1bdecf6ba568a679007af(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b123a6c4bbc3ff9b8ce1479c01e3e2a438c7ef1a70dd2ccf41371497b257205(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03643a56201d8ee41ec6cb2d06bf4a744b44f9e140baade1eee0f8923f4de100(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d933992b8def94152adabe1624210ae1c6c2ac626a5a9fd2af376a7f9128d123(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLoggerDefinition.LoggerDefinitionVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1467bdc61b875959389bcefa758a86026e2fb80e0b9db5da7327a4e0b2c1c6b3(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb77b1dd70ac4fe4579018e45f452bb02bc14d56a2ce5d000c6bd4cc542d183(
    *,
    loggers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggerDefinition.LoggerProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef56df2cb15dd1d03dc55bf6372cddbfc94e06fb51a6d1a1422c713d37dd808c(
    *,
    component: builtins.str,
    id: builtins.str,
    level: builtins.str,
    type: builtins.str,
    space: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170725663bf1c1d04ae4208595550913d0157b3edd62f4ff14920f4acbfe3707(
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggerDefinition.LoggerDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb45ce0812f07c5afc2310bc7a288eff7e5cdc4a5609d10f2a19f5b87faf7fe5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    logger_definition_id: builtins.str,
    loggers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggerDefinitionVersion.LoggerProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e52fdc9bf427c5c69aa25405bc527eac098df7759f0f8a65d64cf2ac634260dd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a42b772a8bb7406067e698e43fd8f7d878cfc6b68255652cf2e0940da66a4f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccc4692452b48425650c13195e73d6c200e1a8087f73abc40b4266aa7098102(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935a7882eea62e6e59dbe2f8f1f89290502193c1dc3234cdc82edf49948aac83(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLoggerDefinitionVersion.LoggerProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17bd21c4fd76afa67a356eb02e70cf8770d286a8abba3a95fc65604a3e4ca18f(
    *,
    component: builtins.str,
    id: builtins.str,
    level: builtins.str,
    type: builtins.str,
    space: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a55ca993c275a44b98675ba3424e4e63162b645c01b9f63544a74a467b4060a7(
    *,
    logger_definition_id: builtins.str,
    loggers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggerDefinitionVersion.LoggerProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__047c0e38fb370750fe5db940a38d857f066bb4490f8e079801f4c24d210372c3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.ResourceDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42977d53c22197ecb3e5aa75d8273dbffa91f7bab1c2d271a874285225a099b8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a345a654c8dbd28db74cdcdaa4cf76ca9f4596ded63638879400c3589d09227(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0256b19a6270c50864dd0afa1219a1b6be7518258daea855f19ca60744fa0d27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e477611b342531c61501bce71bad63149180465d67fa02234b702f1d04ed88e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDefinition.ResourceDefinitionVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f8767a6e08f9caeed0ccc0cab826c0939740af34c6b569658174c0ac9284975(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dee09549db08436516a33cdfd3af7e5ad5db5fe672d89da865d7405e9d83a1b7(
    *,
    auto_add_group_owner: typing.Union[builtins.bool, _IResolvable_da3f097b],
    group_owner: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__519c96577980326dba50fcff850097de74fac4e031ecd0c5b0699a683334e6e7(
    *,
    source_path: builtins.str,
    group_owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.GroupOwnerSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a3bf7a5d451ecfb7a0028a5410ae5923ddd2e13f2d619750140c5474472942a(
    *,
    destination_path: builtins.str,
    source_path: builtins.str,
    group_owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.GroupOwnerSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396357cb8698a2ab08ce94b2efcdff53c907a511665a527e7b6df7aeab58eaff(
    *,
    local_device_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.LocalDeviceResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    local_volume_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.LocalVolumeResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_machine_learning_model_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.S3MachineLearningModelResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sage_maker_machine_learning_model_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.SageMakerMachineLearningModelResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    secrets_manager_secret_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.SecretsManagerSecretResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c2b639a854266ea9e4614285d20bfcd34ae6e76ad6b8c645cd458ea74d79b1d(
    *,
    resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.ResourceInstanceProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1515394b8f7bc78aa0cb5c9c538e8d26325857332890bc231c259b12d7c585(
    *,
    group_owner: builtins.str,
    group_permission: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5049866f9bc9b9b69029fc4e81f22c8620cd6a6cded5d5499d0011b8e4f438e(
    *,
    id: builtins.str,
    name: builtins.str,
    resource_data_container: typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.ResourceDataContainerProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5bb7ffbcaf0627cc8969d8e7b4223d2abe7b6803cebdf191f694ccdb20da9b1(
    *,
    destination_path: builtins.str,
    s3_uri: builtins.str,
    owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.ResourceDownloadOwnerSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3995e8ba195b1f7e333172d25dc3c1e984db53c31650fe725fa3554fa39e8c03(
    *,
    destination_path: builtins.str,
    sage_maker_job_arn: builtins.str,
    owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.ResourceDownloadOwnerSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7665349bcf6d8c447b8247f984eb20a41ebfec207c55b6f809ba23f39db5e941(
    *,
    arn: builtins.str,
    additional_staging_labels_to_download: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d19c7aa996849ae5308a845fea1be8a360b83d3ec8158f6a19c48fe68f5009(
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinition.ResourceDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e106c323b7cfeaacd807745287aed9743502c2e5353d29679ad3381a494b6a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_definition_id: builtins.str,
    resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.ResourceInstanceProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62f5d9f4cfb364bba693491c17e35b128c2b8ee571b3a2e22a37a57beae0a3b5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc49d5697e9f2028c7bd3fb79a84e389f982ae6aff558a88094ca6c07cdc1ee(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62580ea31539bd91a408bb34b014f3d32df9c5903336db1a3dd73bad8e783dc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74096283c52a878723fa8ea3375fb7a3d8f6b1924db6d17a865bc7f6ab31cce8(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnResourceDefinitionVersion.ResourceInstanceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8988f1c5c6c177915d440c485ec6d617ad5fab37340bb66f4512f8046513d05(
    *,
    auto_add_group_owner: typing.Union[builtins.bool, _IResolvable_da3f097b],
    group_owner: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad1e5ad5d32a1c882a19870f66bf8426f59f3e8a4b04c0e26abd1cfd58c9da20(
    *,
    source_path: builtins.str,
    group_owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.GroupOwnerSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba79cc6c8d101b2524627c61005b837fe8f6106d075960b72da33a2448402a1(
    *,
    destination_path: builtins.str,
    source_path: builtins.str,
    group_owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.GroupOwnerSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f173a21b203c0c5e80391a9ec0fbd6e1e7fc332eafdd65534039d45a1fa167(
    *,
    local_device_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.LocalDeviceResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    local_volume_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.LocalVolumeResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_machine_learning_model_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.S3MachineLearningModelResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sage_maker_machine_learning_model_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.SageMakerMachineLearningModelResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    secrets_manager_secret_resource_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.SecretsManagerSecretResourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0a8bffe4da2c9d860929131465d097b2e15f4dec1ec670a751d2b96dd405f9(
    *,
    group_owner: builtins.str,
    group_permission: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fabb819cca9f473b88a301180b791a2610681e8c3e39303f273979230419cbb1(
    *,
    id: builtins.str,
    name: builtins.str,
    resource_data_container: typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.ResourceDataContainerProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db5c429251ce7c49fb1d990fb9ac0519fcc4eb330460a7b1fe8b12ce83f3500(
    *,
    destination_path: builtins.str,
    s3_uri: builtins.str,
    owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__733b10b4c3a727471582d5422b71ecf16f8bc7480a54f897d6d6167da4004e7d(
    *,
    destination_path: builtins.str,
    sage_maker_job_arn: builtins.str,
    owner_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.ResourceDownloadOwnerSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42b5f8b52b565c9d97f0c8313cdb4b5f55c17c63cd32aa5bdc087f665e4894a2(
    *,
    arn: builtins.str,
    additional_staging_labels_to_download: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92f249a2f06545b4d2c57aa9e2ac98fd23d4647ebf0ab39624e1bc81c067b427(
    *,
    resource_definition_id: builtins.str,
    resources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDefinitionVersion.ResourceInstanceProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b231a8b03315437dd52b155f4e7c1d32a92f2a3b0e6f37ae1bfae2e72938fb22(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3b55b221d1074330e22fd2822066e10cb57a859717ce6d479ff80b008c96af7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b6fd2bcdb28de44a008408c98ea58d67bc1442faa5d9fa707802f568ddb1d2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7419a41b1a2fd9cbc8893cf41814a9d4402f8bbf4b3926c9d4eae1050a3cb2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5bd9630745b54bebd6a65c27d16ed4621705d8b40d785efc3fcf8eda69d66a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3c68b21f52fe99f3d6a88bd9e881c4d030dd6c2bef09d8ac0a05a8c5ff59c37(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd466a90e730b214d5682e7f3c520c2a2084f5919c5b4a34dc43d11ebd863f01(
    *,
    subscriptions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionDefinition.SubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b7552743b0092a7b8371fc4c1a1476bd190cbed44e48e0e59b996d8305d666b(
    *,
    id: builtins.str,
    source: builtins.str,
    subject: builtins.str,
    target: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ca5b663a9b0488d2381e662e60281bd0082829ce52f3a587e6f8294d7745d98(
    *,
    name: builtins.str,
    initial_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionDefinition.SubscriptionDefinitionVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__196d53b9c9e2e632eb88d7a7f73e15b80a4e83c869df484747f40505cd07b62a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    subscription_definition_id: builtins.str,
    subscriptions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionDefinitionVersion.SubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f5cbbce137768ad4bc517ba5824ec70d35a12d68a33dcc26d9f212c7554f8d8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74274a470594f3024a0879f542f07460bf8dbc14aba0fa410317cbfb126bf38f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9eaeca2366167091d0a98772cb6ca7a6cc6e0b9cb92f4e5f40dbbe066f0768e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba4cd67c8807aa76b5b15f0cc7031c8c93e9db957d1dcbe2f07f9d22c3d9b57(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionDefinitionVersion.SubscriptionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3123a4ba54f33ea17e4d551e1741ceae6c3e217ae977d2d28f5c60c81ab526(
    *,
    id: builtins.str,
    source: builtins.str,
    subject: builtins.str,
    target: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d59bb5054d104f51e689b37a46da9774e6b1e1bc38b16496ca8bf4a7ce90c8(
    *,
    subscription_definition_id: builtins.str,
    subscriptions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionDefinitionVersion.SubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass
