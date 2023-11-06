'''
# AWS OpsWorks Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_opsworks as opsworks
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for OpsWorks construct libraries](https://constructs.dev/search?q=opsworks)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::OpsWorks resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpsWorks.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::OpsWorks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpsWorks.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnApp(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opsworks.CfnApp",
):
    '''Creates an app for a specified stack. For more information, see `Creating Apps <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`_ .

    *Required Permissions* : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opsworks as opsworks
        
        cfn_app = opsworks.CfnApp(self, "MyCfnApp",
            name="name",
            stack_id="stackId",
            type="type",
        
            # the properties below are optional
            app_source=opsworks.CfnApp.SourceProperty(
                password="password",
                revision="revision",
                ssh_key="sshKey",
                type="type",
                url="url",
                username="username"
            ),
            attributes={
                "attributes_key": "attributes"
            },
            data_sources=[opsworks.CfnApp.DataSourceProperty(
                arn="arn",
                database_name="databaseName",
                type="type"
            )],
            description="description",
            domains=["domains"],
            enable_ssl=False,
            environment=[opsworks.CfnApp.EnvironmentVariableProperty(
                key="key",
                value="value",
        
                # the properties below are optional
                secure=False
            )],
            shortname="shortname",
            ssl_configuration=opsworks.CfnApp.SslConfigurationProperty(
                certificate="certificate",
                chain="chain",
                private_key="privateKey"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        stack_id: builtins.str,
        type: builtins.str,
        app_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.SourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        data_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.DataSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ssl: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.EnvironmentVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        shortname: typing.Optional[builtins.str] = None,
        ssl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.SslConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The app name.
        :param stack_id: The stack ID.
        :param type: The app type. Each supported type is associated with a particular layer. For example, PHP applications are associated with a PHP layer. AWS OpsWorks Stacks deploys an application to those instances that are members of the corresponding layer. If your app isn't one of the standard types, or you prefer to implement your own Deploy recipes, specify ``other`` .
        :param app_source: A ``Source`` object that specifies the app repository.
        :param attributes: One or more user-defined key/value pairs to be added to the stack attributes.
        :param data_sources: The app's data source.
        :param description: A description of the app.
        :param domains: The app virtual host settings, with multiple domains separated by commas. For example: ``'www.example.com, example.com'``
        :param enable_ssl: Whether to enable SSL for the app.
        :param environment: An array of ``EnvironmentVariable`` objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instance. For more information, see `Environment Variables <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment>`_ . There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables' names, values, and protected flag values - cannot exceed 20 KB. This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, "Environment: is too large (maximum is 20KB)." .. epigraph:: If you have specified one or more environment variables, you cannot modify the stack's Chef version.
        :param shortname: The app's short name.
        :param ssl_configuration: An ``SslConfiguration`` object with the SSL configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cfc69040af8322a035060c3c2b7a93463983dd64c29f11c41157c08be717ae8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppProps(
            name=name,
            stack_id=stack_id,
            type=type,
            app_source=app_source,
            attributes=attributes,
            data_sources=data_sources,
            description=description,
            domains=domains,
            enable_ssl=enable_ssl,
            environment=environment,
            shortname=shortname,
            ssl_configuration=ssl_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ff143edbf423ab87fc5b07a79bac15afad922b4f9752bf18393dfbf1f9c9cd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c12528e296c556a11ebf8a34dd92bc4963eb767008506fae4907600da103cc0)
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
        '''The app name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a19c59d6094186b25ccb74f53b769ee4f330ac7d37adc44ca9689573bf3dbac7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''The stack ID.'''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44fcbd77f5eec62a5bc0eff1206b3965788d71cb0f98783d83060472cdbe1664)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The app type.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca84fd86e0761b50ce73d01c5dc30322ab1d89c25362406b4f8c17d6c175708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="appSource")
    def app_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.SourceProperty"]]:
        '''A ``Source`` object that specifies the app repository.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.SourceProperty"]], jsii.get(self, "appSource"))

    @app_source.setter
    def app_source(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.SourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__185dad1883ad44edf530c80eedb41525e399494340def4de222a61617999031a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSource", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''One or more user-defined key/value pairs to be added to the stack attributes.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bced3305a9b7d70a45a3681d489962e84c64c8313a37872dfa4339ac6982d92d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="dataSources")
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.DataSourceProperty"]]]]:
        '''The app's data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.DataSourceProperty"]]]], jsii.get(self, "dataSources"))

    @data_sources.setter
    def data_sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.DataSourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64566650c8e8b9d3d6b7f320ae9f2fd02d48557d1d06b6133a991557c9326de8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSources", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97d3ebf2ce216f79a04213a4062b8b76a0e788f15cba7f5019619d673cad19cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The app virtual host settings, with multiple domains separated by commas.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domains"))

    @domains.setter
    def domains(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27fab7ca15432dc0ce6185a2eef7831a65e6787482baeddb58e6de68a4dc1ca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domains", value)

    @builtins.property
    @jsii.member(jsii_name="enableSsl")
    def enable_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to enable SSL for the app.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableSsl"))

    @enable_ssl.setter
    def enable_ssl(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8518eeb92295cd7150f12a3df695529ec26a1dd47aa59533a210493d9ee8bd8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSsl", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EnvironmentVariableProperty"]]]]:
        '''An array of ``EnvironmentVariable`` objects that specify environment variables to be associated with the app.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EnvironmentVariableProperty"]]]], jsii.get(self, "environment"))

    @environment.setter
    def environment(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EnvironmentVariableProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9d5c35bc69f1bf2418216b8439788ce44352eba1ce1bd2f8c6d0ed3fa939b21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="shortname")
    def shortname(self) -> typing.Optional[builtins.str]:
        '''The app's short name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortname"))

    @shortname.setter
    def shortname(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc79da84419e543929094dc3dab262875e458ac8404232b6fd87d3306d47bf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortname", value)

    @builtins.property
    @jsii.member(jsii_name="sslConfiguration")
    def ssl_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.SslConfigurationProperty"]]:
        '''An ``SslConfiguration`` object with the SSL configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.SslConfigurationProperty"]], jsii.get(self, "sslConfiguration"))

    @ssl_configuration.setter
    def ssl_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.SslConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb8571a770edf95757d930ebc880d2330b6605dcf2c857c4616ee5cb1bd02163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnApp.DataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "database_name": "databaseName", "type": "type"},
    )
    class DataSourceProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an app's data source.

            :param arn: The data source's ARN.
            :param database_name: The database name.
            :param type: The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` , ``RdsDbInstance`` , or ``None`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                data_source_property = opsworks.CfnApp.DataSourceProperty(
                    arn="arn",
                    database_name="databaseName",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7cf45f6c19d83a84c2829e849bf67cc8df566964fcdac07b785b94c64176418d)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if database_name is not None:
                self._values["database_name"] = database_name
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The data source's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The database name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` , ``RdsDbInstance`` , or ``None`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnApp.EnvironmentVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value", "secure": "secure"},
    )
    class EnvironmentVariableProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: builtins.str,
            secure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents an app's environment variable.

            :param key: (Required) The environment variable's name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.
            :param value: (Optional) The environment variable's value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.
            :param secure: (Optional) Whether the variable's value is returned by the `DescribeApps <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeApps>`_ action. To hide an environment variable's value, set ``Secure`` to ``true`` . ``DescribeApps`` returns ``*****FILTERED*****`` instead of the actual value. The default value for ``Secure`` is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environmentvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                environment_variable_property = opsworks.CfnApp.EnvironmentVariableProperty(
                    key="key",
                    value="value",
                
                    # the properties below are optional
                    secure=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f4bf1124807563999966950a3742bd343b3bf39de03896181aff2061910ba97)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument secure", value=secure, expected_type=type_hints["secure"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }
            if secure is not None:
                self._values["secure"] = secure

        @builtins.property
        def key(self) -> builtins.str:
            '''(Required) The environment variable's name, which can consist of up to 64 characters and must be specified.

            The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environmentvariable.html#cfn-opsworks-app-environmentvariable-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''(Optional) The environment variable's value, which can be left empty.

            If you specify a value, it can contain up to 256 characters, which must all be printable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environmentvariable.html#cfn-opsworks-app-environmentvariable-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secure(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''(Optional) Whether the variable's value is returned by the `DescribeApps <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeApps>`_ action. To hide an environment variable's value, set ``Secure`` to ``true`` . ``DescribeApps`` returns ``*****FILTERED*****`` instead of the actual value. The default value for ``Secure`` is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environmentvariable.html#cfn-opsworks-app-environmentvariable-secure
            '''
            result = self._values.get("secure")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnApp.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "revision": "revision",
            "ssh_key": "sshKey",
            "type": "type",
            "url": "url",
            "username": "username",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            password: typing.Optional[builtins.str] = None,
            revision: typing.Optional[builtins.str] = None,
            ssh_key: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains the information required to retrieve an app or cookbook from a repository.

            For more information, see `Creating Apps <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`_ or `Custom Recipes and Cookbooks <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`_ .

            :param password: When included in a request, the parameter depends on the repository type. - For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. - For HTTP bundles and Subversion repositories, set ``Password`` to the password. For more information on how to safely handle IAM credentials, see ` <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`_ . In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.
            :param revision: The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
            :param ssh_key: In requests, the repository's SSH key. In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.
            :param type: The repository type.
            :param url: The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .
            :param username: This parameter depends on the repository type. - For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. - For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                source_property = opsworks.CfnApp.SourceProperty(
                    password="password",
                    revision="revision",
                    ssh_key="sshKey",
                    type="type",
                    url="url",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b809263c93f54c1b303d60d709a45fea8e430f2e2275e331f5200153d7e203e)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
                check_type(argname="argument ssh_key", value=ssh_key, expected_type=type_hints["ssh_key"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if password is not None:
                self._values["password"] = password
            if revision is not None:
                self._values["revision"] = revision
            if ssh_key is not None:
                self._values["ssh_key"] = ssh_key
            if type is not None:
                self._values["type"] = type
            if url is not None:
                self._values["url"] = url
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''When included in a request, the parameter depends on the repository type.

            - For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.
            - For HTTP bundles and Subversion repositories, set ``Password`` to the password.

            For more information on how to safely handle IAM credentials, see ` <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`_ .

            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-source.html#cfn-opsworks-app-source-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def revision(self) -> typing.Optional[builtins.str]:
            '''The application's version.

            AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-source.html#cfn-opsworks-app-source-revision
            '''
            result = self._values.get("revision")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssh_key(self) -> typing.Optional[builtins.str]:
            '''In requests, the repository's SSH key.

            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-source.html#cfn-opsworks-app-source-sshkey
            '''
            result = self._values.get("ssh_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The repository type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-source.html#cfn-opsworks-app-source-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The source URL.

            The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-source.html#cfn-opsworks-app-source-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''This parameter depends on the repository type.

            - For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.
            - For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-source.html#cfn-opsworks-app-source-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnApp.SslConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate": "certificate",
            "chain": "chain",
            "private_key": "privateKey",
        },
    )
    class SslConfigurationProperty:
        def __init__(
            self,
            *,
            certificate: typing.Optional[builtins.str] = None,
            chain: typing.Optional[builtins.str] = None,
            private_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an app's SSL configuration.

            :param certificate: The contents of the certificate's domain.crt file.
            :param chain: Optional. Can be used to specify an intermediate certificate authority key or client authentication.
            :param private_key: The private key; the contents of the certificate's domain.kex file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                ssl_configuration_property = opsworks.CfnApp.SslConfigurationProperty(
                    certificate="certificate",
                    chain="chain",
                    private_key="privateKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cfa3e28175cca76b2b379e24dd298856761e8b2b972fbefd13fb45c20bfa622a)
                check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
                check_type(argname="argument chain", value=chain, expected_type=type_hints["chain"])
                check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate is not None:
                self._values["certificate"] = certificate
            if chain is not None:
                self._values["chain"] = chain
            if private_key is not None:
                self._values["private_key"] = private_key

        @builtins.property
        def certificate(self) -> typing.Optional[builtins.str]:
            '''The contents of the certificate's domain.crt file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfiguration-certificate
            '''
            result = self._values.get("certificate")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def chain(self) -> typing.Optional[builtins.str]:
            '''Optional.

            Can be used to specify an intermediate certificate authority key or client authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfiguration-chain
            '''
            result = self._values.get("chain")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_key(self) -> typing.Optional[builtins.str]:
            '''The private key;

            the contents of the certificate's domain.kex file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfiguration-privatekey
            '''
            result = self._values.get("private_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SslConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opsworks.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "stack_id": "stackId",
        "type": "type",
        "app_source": "appSource",
        "attributes": "attributes",
        "data_sources": "dataSources",
        "description": "description",
        "domains": "domains",
        "enable_ssl": "enableSsl",
        "environment": "environment",
        "shortname": "shortname",
        "ssl_configuration": "sslConfiguration",
    },
)
class CfnAppProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        stack_id: builtins.str,
        type: builtins.str,
        app_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        data_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.DataSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ssl: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        shortname: typing.Optional[builtins.str] = None,
        ssl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.SslConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApp``.

        :param name: The app name.
        :param stack_id: The stack ID.
        :param type: The app type. Each supported type is associated with a particular layer. For example, PHP applications are associated with a PHP layer. AWS OpsWorks Stacks deploys an application to those instances that are members of the corresponding layer. If your app isn't one of the standard types, or you prefer to implement your own Deploy recipes, specify ``other`` .
        :param app_source: A ``Source`` object that specifies the app repository.
        :param attributes: One or more user-defined key/value pairs to be added to the stack attributes.
        :param data_sources: The app's data source.
        :param description: A description of the app.
        :param domains: The app virtual host settings, with multiple domains separated by commas. For example: ``'www.example.com, example.com'``
        :param enable_ssl: Whether to enable SSL for the app.
        :param environment: An array of ``EnvironmentVariable`` objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instance. For more information, see `Environment Variables <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment>`_ . There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables' names, values, and protected flag values - cannot exceed 20 KB. This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, "Environment: is too large (maximum is 20KB)." .. epigraph:: If you have specified one or more environment variables, you cannot modify the stack's Chef version.
        :param shortname: The app's short name.
        :param ssl_configuration: An ``SslConfiguration`` object with the SSL configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opsworks as opsworks
            
            cfn_app_props = opsworks.CfnAppProps(
                name="name",
                stack_id="stackId",
                type="type",
            
                # the properties below are optional
                app_source=opsworks.CfnApp.SourceProperty(
                    password="password",
                    revision="revision",
                    ssh_key="sshKey",
                    type="type",
                    url="url",
                    username="username"
                ),
                attributes={
                    "attributes_key": "attributes"
                },
                data_sources=[opsworks.CfnApp.DataSourceProperty(
                    arn="arn",
                    database_name="databaseName",
                    type="type"
                )],
                description="description",
                domains=["domains"],
                enable_ssl=False,
                environment=[opsworks.CfnApp.EnvironmentVariableProperty(
                    key="key",
                    value="value",
            
                    # the properties below are optional
                    secure=False
                )],
                shortname="shortname",
                ssl_configuration=opsworks.CfnApp.SslConfigurationProperty(
                    certificate="certificate",
                    chain="chain",
                    private_key="privateKey"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe0ae5f6e1367f942976862a375aa88ecad21e52429978b2181e9115ce82447e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument app_source", value=app_source, expected_type=type_hints["app_source"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument data_sources", value=data_sources, expected_type=type_hints["data_sources"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domains", value=domains, expected_type=type_hints["domains"])
            check_type(argname="argument enable_ssl", value=enable_ssl, expected_type=type_hints["enable_ssl"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument shortname", value=shortname, expected_type=type_hints["shortname"])
            check_type(argname="argument ssl_configuration", value=ssl_configuration, expected_type=type_hints["ssl_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "stack_id": stack_id,
            "type": type,
        }
        if app_source is not None:
            self._values["app_source"] = app_source
        if attributes is not None:
            self._values["attributes"] = attributes
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if description is not None:
            self._values["description"] = description
        if domains is not None:
            self._values["domains"] = domains
        if enable_ssl is not None:
            self._values["enable_ssl"] = enable_ssl
        if environment is not None:
            self._values["environment"] = environment
        if shortname is not None:
            self._values["shortname"] = shortname
        if ssl_configuration is not None:
            self._values["ssl_configuration"] = ssl_configuration

    @builtins.property
    def name(self) -> builtins.str:
        '''The app name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''The stack ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-stackid
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The app type.

        Each supported type is associated with a particular layer. For example, PHP applications are associated with a PHP layer. AWS OpsWorks Stacks deploys an application to those instances that are members of the corresponding layer. If your app isn't one of the standard types, or you prefer to implement your own Deploy recipes, specify ``other`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.SourceProperty]]:
        '''A ``Source`` object that specifies the app repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-appsource
        '''
        result = self._values.get("app_source")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.SourceProperty]], result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''One or more user-defined key/value pairs to be added to the stack attributes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

    @builtins.property
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.DataSourceProperty]]]]:
        '''The app's data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-datasources
        '''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.DataSourceProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the app.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The app virtual host settings, with multiple domains separated by commas.

        For example: ``'www.example.com, example.com'``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-domains
        '''
        result = self._values.get("domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to enable SSL for the app.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-enablessl
        '''
        result = self._values.get("enable_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EnvironmentVariableProperty]]]]:
        '''An array of ``EnvironmentVariable`` objects that specify environment variables to be associated with the app.

        After you deploy the app, these variables are defined on the associated app server instance. For more information, see `Environment Variables <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment>`_ .

        There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables' names, values, and protected flag values - cannot exceed 20 KB. This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, "Environment: is too large (maximum is 20KB)."
        .. epigraph::

           If you have specified one or more environment variables, you cannot modify the stack's Chef version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-environment
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EnvironmentVariableProperty]]]], result)

    @builtins.property
    def shortname(self) -> typing.Optional[builtins.str]:
        '''The app's short name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-shortname
        '''
        result = self._values.get("shortname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.SslConfigurationProperty]]:
        '''An ``SslConfiguration`` object with the SSL configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-sslconfiguration
        '''
        result = self._values.get("ssl_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.SslConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnElasticLoadBalancerAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opsworks.CfnElasticLoadBalancerAttachment",
):
    '''Attaches an Elastic Load Balancing load balancer to an AWS OpsWorks layer that you specify.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elasticloadbalancerattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opsworks as opsworks
        
        cfn_elastic_load_balancer_attachment = opsworks.CfnElasticLoadBalancerAttachment(self, "MyCfnElasticLoadBalancerAttachment",
            elastic_load_balancer_name="elasticLoadBalancerName",
            layer_id="layerId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        elastic_load_balancer_name: builtins.str,
        layer_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param elastic_load_balancer_name: The Elastic Load Balancing instance name.
        :param layer_id: The AWS OpsWorks layer ID to which the Elastic Load Balancing load balancer is attached.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__486f7e1e8e8052927626441be8be1b13d2a9ce484c4915a83fb32a7def2f835d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnElasticLoadBalancerAttachmentProps(
            elastic_load_balancer_name=elastic_load_balancer_name, layer_id=layer_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf3f53bd9cb54ef908ec70944a483b6bcfaee7dfb90c1ca4dbd915d2524c8d65)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05c4f2d60c2a89e9f4dc4b0b1a839a6f752960decc3d3eb9e49cc21748378ee6)
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
    @jsii.member(jsii_name="elasticLoadBalancerName")
    def elastic_load_balancer_name(self) -> builtins.str:
        '''The Elastic Load Balancing instance name.'''
        return typing.cast(builtins.str, jsii.get(self, "elasticLoadBalancerName"))

    @elastic_load_balancer_name.setter
    def elastic_load_balancer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f09a3b90cb26ee5103e9da8d0751d21ff83e1203e9f45fb281e8704f606f9df0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticLoadBalancerName", value)

    @builtins.property
    @jsii.member(jsii_name="layerId")
    def layer_id(self) -> builtins.str:
        '''The AWS OpsWorks layer ID to which the Elastic Load Balancing load balancer is attached.'''
        return typing.cast(builtins.str, jsii.get(self, "layerId"))

    @layer_id.setter
    def layer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07fc612753cec7293a77d1dee6f0043e104fdad08f108eeff357be2fc4d973b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layerId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opsworks.CfnElasticLoadBalancerAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "elastic_load_balancer_name": "elasticLoadBalancerName",
        "layer_id": "layerId",
    },
)
class CfnElasticLoadBalancerAttachmentProps:
    def __init__(
        self,
        *,
        elastic_load_balancer_name: builtins.str,
        layer_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnElasticLoadBalancerAttachment``.

        :param elastic_load_balancer_name: The Elastic Load Balancing instance name.
        :param layer_id: The AWS OpsWorks layer ID to which the Elastic Load Balancing load balancer is attached.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elasticloadbalancerattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opsworks as opsworks
            
            cfn_elastic_load_balancer_attachment_props = opsworks.CfnElasticLoadBalancerAttachmentProps(
                elastic_load_balancer_name="elasticLoadBalancerName",
                layer_id="layerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cce4a38411eccbc7b0088bfd31a89e80bd98022d6249e27feb26e4ee7d3e6834)
            check_type(argname="argument elastic_load_balancer_name", value=elastic_load_balancer_name, expected_type=type_hints["elastic_load_balancer_name"])
            check_type(argname="argument layer_id", value=layer_id, expected_type=type_hints["layer_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "elastic_load_balancer_name": elastic_load_balancer_name,
            "layer_id": layer_id,
        }

    @builtins.property
    def elastic_load_balancer_name(self) -> builtins.str:
        '''The Elastic Load Balancing instance name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elasticloadbalancerattachment.html#cfn-opsworks-elasticloadbalancerattachment-elasticloadbalancername
        '''
        result = self._values.get("elastic_load_balancer_name")
        assert result is not None, "Required property 'elastic_load_balancer_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def layer_id(self) -> builtins.str:
        '''The AWS OpsWorks layer ID to which the Elastic Load Balancing load balancer is attached.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elasticloadbalancerattachment.html#cfn-opsworks-elasticloadbalancerattachment-layerid
        '''
        result = self._values.get("layer_id")
        assert result is not None, "Required property 'layer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnElasticLoadBalancerAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnInstance(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opsworks.CfnInstance",
):
    '''Creates an instance in a specified stack. For more information, see `Adding an Instance to a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`_ .

    *Required Permissions* : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opsworks as opsworks
        
        cfn_instance = opsworks.CfnInstance(self, "MyCfnInstance",
            instance_type="instanceType",
            layer_ids=["layerIds"],
            stack_id="stackId",
        
            # the properties below are optional
            agent_version="agentVersion",
            ami_id="amiId",
            architecture="architecture",
            auto_scaling_type="autoScalingType",
            availability_zone="availabilityZone",
            block_device_mappings=[opsworks.CfnInstance.BlockDeviceMappingProperty(
                device_name="deviceName",
                ebs=opsworks.CfnInstance.EbsBlockDeviceProperty(
                    delete_on_termination=False,
                    iops=123,
                    snapshot_id="snapshotId",
                    volume_size=123,
                    volume_type="volumeType"
                ),
                no_device="noDevice",
                virtual_name="virtualName"
            )],
            ebs_optimized=False,
            elastic_ips=["elasticIps"],
            hostname="hostname",
            install_updates_on_boot=False,
            os="os",
            root_device_type="rootDeviceType",
            ssh_key_name="sshKeyName",
            subnet_id="subnetId",
            tenancy="tenancy",
            time_based_auto_scaling=opsworks.CfnInstance.TimeBasedAutoScalingProperty(
                friday={
                    "friday_key": "friday"
                },
                monday={
                    "monday_key": "monday"
                },
                saturday={
                    "saturday_key": "saturday"
                },
                sunday={
                    "sunday_key": "sunday"
                },
                thursday={
                    "thursday_key": "thursday"
                },
                tuesday={
                    "tuesday_key": "tuesday"
                },
                wednesday={
                    "wednesday_key": "wednesday"
                }
            ),
            virtualization_type="virtualizationType",
            volumes=["volumes"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_type: builtins.str,
        layer_ids: typing.Sequence[builtins.str],
        stack_id: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        ami_id: typing.Optional[builtins.str] = None,
        architecture: typing.Optional[builtins.str] = None,
        auto_scaling_type: typing.Optional[builtins.str] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.BlockDeviceMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        elastic_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        hostname: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        os: typing.Optional[builtins.str] = None,
        root_device_type: typing.Optional[builtins.str] = None,
        ssh_key_name: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tenancy: typing.Optional[builtins.str] = None,
        time_based_auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.TimeBasedAutoScalingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        virtualization_type: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_type: The instance type, such as ``t2.micro`` . For a list of supported instance types, open the stack in the console, choose *Instances* , and choose *+ Instance* . The *Size* list contains the currently supported types. For more information, see `Instance Families and Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`_ . The parameter values that you use to specify the various types are in the *API Name* column of the *Available Instance Types* table.
        :param layer_ids: An array that contains the instance's layer IDs.
        :param stack_id: The stack ID.
        :param agent_version: The default AWS OpsWorks Stacks agent version. You have the following options:. - ``INHERIT`` - Use the stack's default agent version setting. - *version_number* - Use the specified agent version. This value overrides the stack's default setting. To update the agent version, edit the instance configuration and specify a new version. AWS OpsWorks Stacks installs that version on the instance. The default setting is ``INHERIT`` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call `DescribeAgentVersions <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeAgentVersions>`_ . AgentVersion cannot be set to Chef 12.2.
        :param ami_id: A custom AMI ID to be used to create the instance. The AMI should be based on one of the supported operating systems. For more information, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ . .. epigraph:: If you specify a custom AMI, you must set ``Os`` to ``Custom`` .
        :param architecture: The instance architecture. The default option is ``x86_64`` . Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see `Instance Families and Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`_ .
        :param auto_scaling_type: For load-based or time-based instances, the type. Windows stacks can use only time-based instances.
        :param availability_zone: The Availability Zone of the AWS OpsWorks instance, such as ``us-east-2a`` .
        :param block_device_mappings: An array of ``BlockDeviceMapping`` objects that specify the instance's block devices. For more information, see `Block Device Mapping <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`_ . Note that block device mappings are not supported for custom AMIs.
        :param ebs_optimized: Whether to create an Amazon EBS-optimized instance.
        :param elastic_ips: A list of Elastic IP addresses to associate with the instance.
        :param hostname: The instance host name. The following are character limits for instance host names. - Linux-based instances: 63 characters - Windows-based instances: 15 characters
        :param install_updates_on_boot: Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using `CreateDeployment <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateDeployment>`_ to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. .. epigraph:: We strongly recommend using the default value of ``true`` to ensure that your instances have the latest security updates.
        :param os: The instance's operating system, which must be set to one of the following. - A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2`` , ``Amazon Linux 2018.03`` , ``Amazon Linux 2017.09`` , ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . - A supported Ubuntu operating system, such as ``Ubuntu 18.04 LTS`` , ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . - ``CentOS Linux 7`` - ``Red Hat Enterprise Linux 7`` - A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . - A custom AMI: ``Custom`` . Not all operating systems are supported with all versions of Chef. For more information about the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`_ . The default option is the current Amazon Linux version. If you set this parameter to ``Custom`` , you must use the `CreateInstance <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateInstance>`_ action's AmiId parameter to specify the custom AMI that you want to use. Block device mappings are not supported if the value is ``Custom`` . For more information about how to use custom AMIs with AWS OpsWorks Stacks, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ .
        :param root_device_type: The instance root device type. For more information, see `Storage for the Root Device <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`_ .
        :param ssh_key_name: The instance's Amazon EC2 key-pair name.
        :param subnet_id: The ID of the instance's subnet. If the stack is running in a VPC, you can use this parameter to override the stack's default subnet ID value and direct AWS OpsWorks Stacks to launch the instance in a different subnet.
        :param tenancy: The instance's tenancy option. The default option is no tenancy, or if the instance is running in a VPC, inherit tenancy settings from the VPC. The following are valid values for this parameter: ``dedicated`` , ``default`` , or ``host`` . Because there are costs associated with changes in tenancy options, we recommend that you research tenancy options before choosing them for your instances. For more information about dedicated hosts, see `Dedicated Hosts Overview <https://docs.aws.amazon.com/ec2/dedicated-hosts/>`_ and `Amazon EC2 Dedicated Hosts <https://docs.aws.amazon.com/ec2/dedicated-hosts/>`_ . For more information about dedicated instances, see `Dedicated Instances <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/dedicated-instance.html>`_ and `Amazon EC2 Dedicated Instances <https://docs.aws.amazon.com/ec2/purchasing-options/dedicated-instances/>`_ .
        :param time_based_auto_scaling: The time-based scaling configuration for the instance.
        :param virtualization_type: The instance's virtualization type, ``paravirtual`` or ``hvm`` .
        :param volumes: A list of AWS OpsWorks volume IDs to associate with the instance. For more information, see ```AWS::OpsWorks::Volume`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b34de3ee05594312f14cce61c717304294b3891e9f25d66dd351119744660a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceProps(
            instance_type=instance_type,
            layer_ids=layer_ids,
            stack_id=stack_id,
            agent_version=agent_version,
            ami_id=ami_id,
            architecture=architecture,
            auto_scaling_type=auto_scaling_type,
            availability_zone=availability_zone,
            block_device_mappings=block_device_mappings,
            ebs_optimized=ebs_optimized,
            elastic_ips=elastic_ips,
            hostname=hostname,
            install_updates_on_boot=install_updates_on_boot,
            os=os,
            root_device_type=root_device_type,
            ssh_key_name=ssh_key_name,
            subnet_id=subnet_id,
            tenancy=tenancy,
            time_based_auto_scaling=time_based_auto_scaling,
            virtualization_type=virtualization_type,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c4d2ac66c9f980cb374fd5448e1c9f04e6eb8e602bd72300ac2abeaa822a7f0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__627888c52651f1163646c543dd9a877f4373aa3e4fec84e06cd224ff01f92d0d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAvailabilityZone")
    def attr_availability_zone(self) -> builtins.str:
        '''The Availability Zone of the AWS OpsWorks instance, such as ``us-east-2a`` .

        :cloudformationAttribute: AvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAvailabilityZone"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrPrivateDnsName")
    def attr_private_dns_name(self) -> builtins.str:
        '''The private DNS name of the AWS OpsWorks instance.

        :cloudformationAttribute: PrivateDnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateDnsName"))

    @builtins.property
    @jsii.member(jsii_name="attrPrivateIp")
    def attr_private_ip(self) -> builtins.str:
        '''The private IP address of the AWS OpsWorks instance, such as ``192.0.2.0`` .

        :cloudformationAttribute: PrivateIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateIp"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicDnsName")
    def attr_public_dns_name(self) -> builtins.str:
        '''The public DNS name of the AWS OpsWorks instance.

        :cloudformationAttribute: PublicDnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicDnsName"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicIp")
    def attr_public_ip(self) -> builtins.str:
        '''The public IP address of the AWS OpsWorks instance, such as ``192.0.2.0`` .

        .. epigraph::

           Use this attribute only when the AWS OpsWorks instance is in an AWS OpsWorks layer that auto-assigns public IP addresses.

        :cloudformationAttribute: PublicIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicIp"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''The instance type, such as ``t2.micro`` . For a list of supported instance types, open the stack in the console, choose *Instances* , and choose *+ Instance* . The *Size* list contains the currently supported types. For more information, see `Instance Families and Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`_ . The parameter values that you use to specify the various types are in the *API Name* column of the *Available Instance Types* table.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__120097d25f64c78439cbbabfbd0a307245ceccef33c5aa775f39972cfb49c826)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="layerIds")
    def layer_ids(self) -> typing.List[builtins.str]:
        '''An array that contains the instance's layer IDs.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "layerIds"))

    @layer_ids.setter
    def layer_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aae9b7d675bad1f1f353a1989ad82553e5c04f98478cf56236e51d89f9959d5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layerIds", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''The stack ID.'''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6698aa3cac36413f5c5cb1d378f05f7c515d8250e3f667a264f3629a455c9041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)

    @builtins.property
    @jsii.member(jsii_name="agentVersion")
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''The default AWS OpsWorks Stacks agent version.

        You have the following options:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentVersion"))

    @agent_version.setter
    def agent_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__716a4f299d569f296c3aaae24e31a2798f5925dc5f10d1bbd86596025466008a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="amiId")
    def ami_id(self) -> typing.Optional[builtins.str]:
        '''A custom AMI ID to be used to create the instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amiId"))

    @ami_id.setter
    def ami_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b1ce00bf1946d2dbd274a57e1fe91041c0e229d88bd6323fdeada3291f4cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amiId", value)

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> typing.Optional[builtins.str]:
        '''The instance architecture.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "architecture"))

    @architecture.setter
    def architecture(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__016fd247ee893c25a899724b1d0c72804b32c2eb68c38c85818641c7c2f9757d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architecture", value)

    @builtins.property
    @jsii.member(jsii_name="autoScalingType")
    def auto_scaling_type(self) -> typing.Optional[builtins.str]:
        '''For load-based or time-based instances, the type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingType"))

    @auto_scaling_type.setter
    def auto_scaling_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21648c47cae646283b32940cd17e1a34756ac2547ce79971404274110698194d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingType", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone of the AWS OpsWorks instance, such as ``us-east-2a`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ab3a2190223656085199b9e11a0bf41abf21a19b31970f1ea3b7bf5d17ad4e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.BlockDeviceMappingProperty"]]]]:
        '''An array of ``BlockDeviceMapping`` objects that specify the instance's block devices.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.BlockDeviceMappingProperty"]]]], jsii.get(self, "blockDeviceMappings"))

    @block_device_mappings.setter
    def block_device_mappings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.BlockDeviceMappingProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e26b3e54531ea4750ebcd10acbcacbf456f6855c3b5272dfcd85ceeaa432c455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDeviceMappings", value)

    @builtins.property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to create an Amazon EBS-optimized instance.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "ebsOptimized"))

    @ebs_optimized.setter
    def ebs_optimized(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ec1bf27e5cd83c8ba7388dfe17956f009f9836f2f5afa9558fb3ba8aa872cc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptimized", value)

    @builtins.property
    @jsii.member(jsii_name="elasticIps")
    def elastic_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Elastic IP addresses to associate with the instance.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "elasticIps"))

    @elastic_ips.setter
    def elastic_ips(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__220dcfd8fd5d5ce9504430ff408ba0125b97234987629d071f0a36c70d880e2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticIps", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> typing.Optional[builtins.str]:
        '''The instance host name.

        The following are character limits for instance host names.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2b492c3f0264061d2b5ecc725ba0cd4efd2a4539e9096f19186820ffb12e432)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="installUpdatesOnBoot")
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to install operating system and package updates when the instance boots.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "installUpdatesOnBoot"))

    @install_updates_on_boot.setter
    def install_updates_on_boot(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb45fe733de533d0fde9a771368ef2623aef37105aafd42bee26dfa53e01db5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installUpdatesOnBoot", value)

    @builtins.property
    @jsii.member(jsii_name="os")
    def os(self) -> typing.Optional[builtins.str]:
        '''The instance's operating system, which must be set to one of the following.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "os"))

    @os.setter
    def os(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5333a6a2c50f73ee90d47575d7aa39dc563a43e60b92e74ff6b97a85ae59b25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "os", value)

    @builtins.property
    @jsii.member(jsii_name="rootDeviceType")
    def root_device_type(self) -> typing.Optional[builtins.str]:
        '''The instance root device type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDeviceType"))

    @root_device_type.setter
    def root_device_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86bd0a754c6aa91d4e5999754c3bb8fb64afd84e8c29778aab752763bccd291e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDeviceType", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeyName")
    def ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''The instance's Amazon EC2 key-pair name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshKeyName"))

    @ssh_key_name.setter
    def ssh_key_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff7b00fceb3aff580ec7a8bd7343bf0e8e17014dbd0c2dae2f0724091c2b591)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the instance's subnet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff9385c60c2ba9003129cceef99b78905f2a550e6956fee4acaef2bb511deb34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''The instance's tenancy option.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenancy"))

    @tenancy.setter
    def tenancy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbae61a65906b826bde0dfe6df35cc3e1f1ac8d4c197e1de1af5324c21b79745)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenancy", value)

    @builtins.property
    @jsii.member(jsii_name="timeBasedAutoScaling")
    def time_based_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.TimeBasedAutoScalingProperty"]]:
        '''The time-based scaling configuration for the instance.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.TimeBasedAutoScalingProperty"]], jsii.get(self, "timeBasedAutoScaling"))

    @time_based_auto_scaling.setter
    def time_based_auto_scaling(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.TimeBasedAutoScalingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ffbe8115388f44a1f41ec2ceb16db364e3519d629ba7a55a34bbc3a12c9a7a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeBasedAutoScaling", value)

    @builtins.property
    @jsii.member(jsii_name="virtualizationType")
    def virtualization_type(self) -> typing.Optional[builtins.str]:
        '''The instance's virtualization type, ``paravirtual`` or ``hvm`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualizationType"))

    @virtualization_type.setter
    def virtualization_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28857381916cdbcb5a292da20a83f099028eabaeda40d7622b6aa635a2f0e7e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualizationType", value)

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS OpsWorks volume IDs to associate with the instance.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "volumes"))

    @volumes.setter
    def volumes(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63137171df7805585bd838275a6375290786e3e6f18f0708cb63f579bf8861f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumes", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnInstance.BlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class BlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.EbsBlockDeviceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a block device mapping.

            This data type maps directly to the Amazon EC2 `BlockDeviceMapping <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`_ data type.

            :param device_name: The device name that is exposed to the instance, such as ``/dev/sdh`` . For the root device, you can use the explicit device name or you can set this parameter to ``ROOT_DEVICE`` and AWS OpsWorks Stacks will provide the correct device name.
            :param ebs: An ``EBSBlockDevice`` that defines how to configure an Amazon EBS volume when the instance is launched. You can specify either the ``VirtualName`` or ``Ebs`` , but not both.
            :param no_device: Suppresses the specified device included in the AMI's block device mapping.
            :param virtual_name: The virtual device name. For more information, see `BlockDeviceMapping <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`_ . You can specify either the ``VirtualName`` or ``Ebs`` , but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                block_device_mapping_property = opsworks.CfnInstance.BlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=opsworks.CfnInstance.EbsBlockDeviceProperty(
                        delete_on_termination=False,
                        iops=123,
                        snapshot_id="snapshotId",
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29f53cb18b26d4ce53cc58c51b2f50b9a2af609eeffeb17c2f393195d6f74ee8)
                check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
                check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
                check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
                check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''The device name that is exposed to the instance, such as ``/dev/sdh`` .

            For the root device, you can use the explicit device name or you can set this parameter to ``ROOT_DEVICE`` and AWS OpsWorks Stacks will provide the correct device name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.EbsBlockDeviceProperty"]]:
            '''An ``EBSBlockDevice`` that defines how to configure an Amazon EBS volume when the instance is launched.

            You can specify either the ``VirtualName`` or ``Ebs`` , but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.EbsBlockDeviceProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''Suppresses the specified device included in the AMI's block device mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''The virtual device name.

            For more information, see `BlockDeviceMapping <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`_ . You can specify either the ``VirtualName`` or ``Ebs`` , but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnInstance.EbsBlockDeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_on_termination": "deleteOnTermination",
            "iops": "iops",
            "snapshot_id": "snapshotId",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsBlockDeviceProperty:
        def __init__(
            self,
            *,
            delete_on_termination: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            iops: typing.Optional[jsii.Number] = None,
            snapshot_id: typing.Optional[builtins.str] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an Amazon EBS volume.

            This data type maps directly to the Amazon EC2 `EbsBlockDevice <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`_ data type.

            :param delete_on_termination: Whether the volume is deleted on instance termination.
            :param iops: The number of I/O operations per second (IOPS) that the volume supports. For more information, see `EbsBlockDevice <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`_ .
            :param snapshot_id: The snapshot ID.
            :param volume_size: The volume size, in GiB. For more information, see `EbsBlockDevice <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`_ .
            :param volume_type: The volume type. ``gp2`` for General Purpose (SSD) volumes, ``io1`` for Provisioned IOPS (SSD) volumes, ``st1`` for Throughput Optimized hard disk drives (HDD), ``sc1`` for Cold HDD,and ``standard`` for Magnetic volumes. If you specify the ``io1`` volume type, you must also specify a value for the ``Iops`` attribute. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1. AWS uses the default volume size (in GiB) specified in the AMI attributes to set IOPS to 50 x (volume size).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                ebs_block_device_property = opsworks.CfnInstance.EbsBlockDeviceProperty(
                    delete_on_termination=False,
                    iops=123,
                    snapshot_id="snapshotId",
                    volume_size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c551f707582f21e17ce83ff8919f39f0c4300ae1c19ef2018670b1edcc8a65a)
                check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_on_termination is not None:
                self._values["delete_on_termination"] = delete_on_termination
            if iops is not None:
                self._values["iops"] = iops
            if snapshot_id is not None:
                self._values["snapshot_id"] = snapshot_id
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def delete_on_termination(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether the volume is deleted on instance termination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-deleteontermination
            '''
            result = self._values.get("delete_on_termination")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The number of I/O operations per second (IOPS) that the volume supports.

            For more information, see `EbsBlockDevice <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def snapshot_id(self) -> typing.Optional[builtins.str]:
            '''The snapshot ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-snapshotid
            '''
            result = self._values.get("snapshot_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''The volume size, in GiB.

            For more information, see `EbsBlockDevice <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''The volume type.

            ``gp2`` for General Purpose (SSD) volumes, ``io1`` for Provisioned IOPS (SSD) volumes, ``st1`` for Throughput Optimized hard disk drives (HDD), ``sc1`` for Cold HDD,and ``standard`` for Magnetic volumes.

            If you specify the ``io1`` volume type, you must also specify a value for the ``Iops`` attribute. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1. AWS uses the default volume size (in GiB) specified in the AMI attributes to set IOPS to 50 x (volume size).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnInstance.TimeBasedAutoScalingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "friday": "friday",
            "monday": "monday",
            "saturday": "saturday",
            "sunday": "sunday",
            "thursday": "thursday",
            "tuesday": "tuesday",
            "wednesday": "wednesday",
        },
    )
    class TimeBasedAutoScalingProperty:
        def __init__(
            self,
            *,
            friday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            monday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            saturday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            sunday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            thursday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            tuesday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            wednesday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes an instance's time-based auto scaling configuration.

            :param friday: The schedule for Friday.
            :param monday: The schedule for Monday.
            :param saturday: The schedule for Saturday.
            :param sunday: The schedule for Sunday.
            :param thursday: The schedule for Thursday.
            :param tuesday: The schedule for Tuesday.
            :param wednesday: The schedule for Wednesday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                time_based_auto_scaling_property = opsworks.CfnInstance.TimeBasedAutoScalingProperty(
                    friday={
                        "friday_key": "friday"
                    },
                    monday={
                        "monday_key": "monday"
                    },
                    saturday={
                        "saturday_key": "saturday"
                    },
                    sunday={
                        "sunday_key": "sunday"
                    },
                    thursday={
                        "thursday_key": "thursday"
                    },
                    tuesday={
                        "tuesday_key": "tuesday"
                    },
                    wednesday={
                        "wednesday_key": "wednesday"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8dfcb549734883fb71a8f431ae16a65e4c926d97e9483cc865e0718bdaaae37b)
                check_type(argname="argument friday", value=friday, expected_type=type_hints["friday"])
                check_type(argname="argument monday", value=monday, expected_type=type_hints["monday"])
                check_type(argname="argument saturday", value=saturday, expected_type=type_hints["saturday"])
                check_type(argname="argument sunday", value=sunday, expected_type=type_hints["sunday"])
                check_type(argname="argument thursday", value=thursday, expected_type=type_hints["thursday"])
                check_type(argname="argument tuesday", value=tuesday, expected_type=type_hints["tuesday"])
                check_type(argname="argument wednesday", value=wednesday, expected_type=type_hints["wednesday"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if friday is not None:
                self._values["friday"] = friday
            if monday is not None:
                self._values["monday"] = monday
            if saturday is not None:
                self._values["saturday"] = saturday
            if sunday is not None:
                self._values["sunday"] = sunday
            if thursday is not None:
                self._values["thursday"] = thursday
            if tuesday is not None:
                self._values["tuesday"] = tuesday
            if wednesday is not None:
                self._values["wednesday"] = wednesday

        @builtins.property
        def friday(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The schedule for Friday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-friday
            '''
            result = self._values.get("friday")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def monday(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The schedule for Monday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-monday
            '''
            result = self._values.get("monday")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def saturday(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The schedule for Saturday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-saturday
            '''
            result = self._values.get("saturday")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def sunday(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The schedule for Sunday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-sunday
            '''
            result = self._values.get("sunday")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def thursday(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The schedule for Thursday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-thursday
            '''
            result = self._values.get("thursday")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def tuesday(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The schedule for Tuesday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-tuesday
            '''
            result = self._values.get("tuesday")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def wednesday(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The schedule for Wednesday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-wednesday
            '''
            result = self._values.get("wednesday")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedAutoScalingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opsworks.CfnInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "layer_ids": "layerIds",
        "stack_id": "stackId",
        "agent_version": "agentVersion",
        "ami_id": "amiId",
        "architecture": "architecture",
        "auto_scaling_type": "autoScalingType",
        "availability_zone": "availabilityZone",
        "block_device_mappings": "blockDeviceMappings",
        "ebs_optimized": "ebsOptimized",
        "elastic_ips": "elasticIps",
        "hostname": "hostname",
        "install_updates_on_boot": "installUpdatesOnBoot",
        "os": "os",
        "root_device_type": "rootDeviceType",
        "ssh_key_name": "sshKeyName",
        "subnet_id": "subnetId",
        "tenancy": "tenancy",
        "time_based_auto_scaling": "timeBasedAutoScaling",
        "virtualization_type": "virtualizationType",
        "volumes": "volumes",
    },
)
class CfnInstanceProps:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        layer_ids: typing.Sequence[builtins.str],
        stack_id: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        ami_id: typing.Optional[builtins.str] = None,
        architecture: typing.Optional[builtins.str] = None,
        auto_scaling_type: typing.Optional[builtins.str] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.BlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        elastic_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        hostname: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        os: typing.Optional[builtins.str] = None,
        root_device_type: typing.Optional[builtins.str] = None,
        ssh_key_name: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tenancy: typing.Optional[builtins.str] = None,
        time_based_auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.TimeBasedAutoScalingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        virtualization_type: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstance``.

        :param instance_type: The instance type, such as ``t2.micro`` . For a list of supported instance types, open the stack in the console, choose *Instances* , and choose *+ Instance* . The *Size* list contains the currently supported types. For more information, see `Instance Families and Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`_ . The parameter values that you use to specify the various types are in the *API Name* column of the *Available Instance Types* table.
        :param layer_ids: An array that contains the instance's layer IDs.
        :param stack_id: The stack ID.
        :param agent_version: The default AWS OpsWorks Stacks agent version. You have the following options:. - ``INHERIT`` - Use the stack's default agent version setting. - *version_number* - Use the specified agent version. This value overrides the stack's default setting. To update the agent version, edit the instance configuration and specify a new version. AWS OpsWorks Stacks installs that version on the instance. The default setting is ``INHERIT`` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call `DescribeAgentVersions <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeAgentVersions>`_ . AgentVersion cannot be set to Chef 12.2.
        :param ami_id: A custom AMI ID to be used to create the instance. The AMI should be based on one of the supported operating systems. For more information, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ . .. epigraph:: If you specify a custom AMI, you must set ``Os`` to ``Custom`` .
        :param architecture: The instance architecture. The default option is ``x86_64`` . Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see `Instance Families and Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`_ .
        :param auto_scaling_type: For load-based or time-based instances, the type. Windows stacks can use only time-based instances.
        :param availability_zone: The Availability Zone of the AWS OpsWorks instance, such as ``us-east-2a`` .
        :param block_device_mappings: An array of ``BlockDeviceMapping`` objects that specify the instance's block devices. For more information, see `Block Device Mapping <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`_ . Note that block device mappings are not supported for custom AMIs.
        :param ebs_optimized: Whether to create an Amazon EBS-optimized instance.
        :param elastic_ips: A list of Elastic IP addresses to associate with the instance.
        :param hostname: The instance host name. The following are character limits for instance host names. - Linux-based instances: 63 characters - Windows-based instances: 15 characters
        :param install_updates_on_boot: Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using `CreateDeployment <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateDeployment>`_ to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. .. epigraph:: We strongly recommend using the default value of ``true`` to ensure that your instances have the latest security updates.
        :param os: The instance's operating system, which must be set to one of the following. - A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2`` , ``Amazon Linux 2018.03`` , ``Amazon Linux 2017.09`` , ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . - A supported Ubuntu operating system, such as ``Ubuntu 18.04 LTS`` , ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . - ``CentOS Linux 7`` - ``Red Hat Enterprise Linux 7`` - A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . - A custom AMI: ``Custom`` . Not all operating systems are supported with all versions of Chef. For more information about the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`_ . The default option is the current Amazon Linux version. If you set this parameter to ``Custom`` , you must use the `CreateInstance <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateInstance>`_ action's AmiId parameter to specify the custom AMI that you want to use. Block device mappings are not supported if the value is ``Custom`` . For more information about how to use custom AMIs with AWS OpsWorks Stacks, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ .
        :param root_device_type: The instance root device type. For more information, see `Storage for the Root Device <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`_ .
        :param ssh_key_name: The instance's Amazon EC2 key-pair name.
        :param subnet_id: The ID of the instance's subnet. If the stack is running in a VPC, you can use this parameter to override the stack's default subnet ID value and direct AWS OpsWorks Stacks to launch the instance in a different subnet.
        :param tenancy: The instance's tenancy option. The default option is no tenancy, or if the instance is running in a VPC, inherit tenancy settings from the VPC. The following are valid values for this parameter: ``dedicated`` , ``default`` , or ``host`` . Because there are costs associated with changes in tenancy options, we recommend that you research tenancy options before choosing them for your instances. For more information about dedicated hosts, see `Dedicated Hosts Overview <https://docs.aws.amazon.com/ec2/dedicated-hosts/>`_ and `Amazon EC2 Dedicated Hosts <https://docs.aws.amazon.com/ec2/dedicated-hosts/>`_ . For more information about dedicated instances, see `Dedicated Instances <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/dedicated-instance.html>`_ and `Amazon EC2 Dedicated Instances <https://docs.aws.amazon.com/ec2/purchasing-options/dedicated-instances/>`_ .
        :param time_based_auto_scaling: The time-based scaling configuration for the instance.
        :param virtualization_type: The instance's virtualization type, ``paravirtual`` or ``hvm`` .
        :param volumes: A list of AWS OpsWorks volume IDs to associate with the instance. For more information, see ```AWS::OpsWorks::Volume`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opsworks as opsworks
            
            cfn_instance_props = opsworks.CfnInstanceProps(
                instance_type="instanceType",
                layer_ids=["layerIds"],
                stack_id="stackId",
            
                # the properties below are optional
                agent_version="agentVersion",
                ami_id="amiId",
                architecture="architecture",
                auto_scaling_type="autoScalingType",
                availability_zone="availabilityZone",
                block_device_mappings=[opsworks.CfnInstance.BlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=opsworks.CfnInstance.EbsBlockDeviceProperty(
                        delete_on_termination=False,
                        iops=123,
                        snapshot_id="snapshotId",
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )],
                ebs_optimized=False,
                elastic_ips=["elasticIps"],
                hostname="hostname",
                install_updates_on_boot=False,
                os="os",
                root_device_type="rootDeviceType",
                ssh_key_name="sshKeyName",
                subnet_id="subnetId",
                tenancy="tenancy",
                time_based_auto_scaling=opsworks.CfnInstance.TimeBasedAutoScalingProperty(
                    friday={
                        "friday_key": "friday"
                    },
                    monday={
                        "monday_key": "monday"
                    },
                    saturday={
                        "saturday_key": "saturday"
                    },
                    sunday={
                        "sunday_key": "sunday"
                    },
                    thursday={
                        "thursday_key": "thursday"
                    },
                    tuesday={
                        "tuesday_key": "tuesday"
                    },
                    wednesday={
                        "wednesday_key": "wednesday"
                    }
                ),
                virtualization_type="virtualizationType",
                volumes=["volumes"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__064c38cf60beb5ee54299be9e04fc9e0d751e94688227f7c131215ac7ef613f9)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument layer_ids", value=layer_ids, expected_type=type_hints["layer_ids"])
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
            check_type(argname="argument agent_version", value=agent_version, expected_type=type_hints["agent_version"])
            check_type(argname="argument ami_id", value=ami_id, expected_type=type_hints["ami_id"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument auto_scaling_type", value=auto_scaling_type, expected_type=type_hints["auto_scaling_type"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument elastic_ips", value=elastic_ips, expected_type=type_hints["elastic_ips"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument install_updates_on_boot", value=install_updates_on_boot, expected_type=type_hints["install_updates_on_boot"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument root_device_type", value=root_device_type, expected_type=type_hints["root_device_type"])
            check_type(argname="argument ssh_key_name", value=ssh_key_name, expected_type=type_hints["ssh_key_name"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tenancy", value=tenancy, expected_type=type_hints["tenancy"])
            check_type(argname="argument time_based_auto_scaling", value=time_based_auto_scaling, expected_type=type_hints["time_based_auto_scaling"])
            check_type(argname="argument virtualization_type", value=virtualization_type, expected_type=type_hints["virtualization_type"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
            "layer_ids": layer_ids,
            "stack_id": stack_id,
        }
        if agent_version is not None:
            self._values["agent_version"] = agent_version
        if ami_id is not None:
            self._values["ami_id"] = ami_id
        if architecture is not None:
            self._values["architecture"] = architecture
        if auto_scaling_type is not None:
            self._values["auto_scaling_type"] = auto_scaling_type
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if elastic_ips is not None:
            self._values["elastic_ips"] = elastic_ips
        if hostname is not None:
            self._values["hostname"] = hostname
        if install_updates_on_boot is not None:
            self._values["install_updates_on_boot"] = install_updates_on_boot
        if os is not None:
            self._values["os"] = os
        if root_device_type is not None:
            self._values["root_device_type"] = root_device_type
        if ssh_key_name is not None:
            self._values["ssh_key_name"] = ssh_key_name
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tenancy is not None:
            self._values["tenancy"] = tenancy
        if time_based_auto_scaling is not None:
            self._values["time_based_auto_scaling"] = time_based_auto_scaling
        if virtualization_type is not None:
            self._values["virtualization_type"] = virtualization_type
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''The instance type, such as ``t2.micro`` . For a list of supported instance types, open the stack in the console, choose *Instances* , and choose *+ Instance* . The *Size* list contains the currently supported types. For more information, see `Instance Families and Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`_ . The parameter values that you use to specify the various types are in the *API Name* column of the *Available Instance Types* table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def layer_ids(self) -> typing.List[builtins.str]:
        '''An array that contains the instance's layer IDs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-layerids
        '''
        result = self._values.get("layer_ids")
        assert result is not None, "Required property 'layer_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''The stack ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-stackid
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''The default AWS OpsWorks Stacks agent version. You have the following options:.

        - ``INHERIT`` - Use the stack's default agent version setting.
        - *version_number* - Use the specified agent version. This value overrides the stack's default setting. To update the agent version, edit the instance configuration and specify a new version. AWS OpsWorks Stacks installs that version on the instance.

        The default setting is ``INHERIT`` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call `DescribeAgentVersions <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeAgentVersions>`_ . AgentVersion cannot be set to Chef 12.2.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-agentversion
        '''
        result = self._values.get("agent_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ami_id(self) -> typing.Optional[builtins.str]:
        '''A custom AMI ID to be used to create the instance.

        The AMI should be based on one of the supported operating systems. For more information, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ .
        .. epigraph::

           If you specify a custom AMI, you must set ``Os`` to ``Custom`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-amiid
        '''
        result = self._values.get("ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def architecture(self) -> typing.Optional[builtins.str]:
        '''The instance architecture.

        The default option is ``x86_64`` . Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see `Instance Families and Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-architecture
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_scaling_type(self) -> typing.Optional[builtins.str]:
        '''For load-based or time-based instances, the type.

        Windows stacks can use only time-based instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-autoscalingtype
        '''
        result = self._values.get("auto_scaling_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone of the AWS OpsWorks instance, such as ``us-east-2a`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstance.BlockDeviceMappingProperty]]]]:
        '''An array of ``BlockDeviceMapping`` objects that specify the instance's block devices.

        For more information, see `Block Device Mapping <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`_ . Note that block device mappings are not supported for custom AMIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-blockdevicemappings
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstance.BlockDeviceMappingProperty]]]], result)

    @builtins.property
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to create an Amazon EBS-optimized instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-ebsoptimized
        '''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def elastic_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Elastic IP addresses to associate with the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-elasticips
        '''
        result = self._values.get("elastic_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''The instance host name. The following are character limits for instance host names.

        - Linux-based instances: 63 characters
        - Windows-based instances: 15 characters

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-hostname
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to install operating system and package updates when the instance boots.

        The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using `CreateDeployment <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateDeployment>`_ to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances.
        .. epigraph::

           We strongly recommend using the default value of ``true`` to ensure that your instances have the latest security updates.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-installupdatesonboot
        '''
        result = self._values.get("install_updates_on_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def os(self) -> typing.Optional[builtins.str]:
        '''The instance's operating system, which must be set to one of the following.

        - A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2`` , ``Amazon Linux 2018.03`` , ``Amazon Linux 2017.09`` , ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` .
        - A supported Ubuntu operating system, such as ``Ubuntu 18.04 LTS`` , ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` .
        - ``CentOS Linux 7``
        - ``Red Hat Enterprise Linux 7``
        - A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` .
        - A custom AMI: ``Custom`` .

        Not all operating systems are supported with all versions of Chef. For more information about the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`_ .

        The default option is the current Amazon Linux version. If you set this parameter to ``Custom`` , you must use the `CreateInstance <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateInstance>`_ action's AmiId parameter to specify the custom AMI that you want to use. Block device mappings are not supported if the value is ``Custom`` . For more information about how to use custom AMIs with AWS OpsWorks Stacks, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-os
        '''
        result = self._values.get("os")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_device_type(self) -> typing.Optional[builtins.str]:
        '''The instance root device type.

        For more information, see `Storage for the Root Device <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-rootdevicetype
        '''
        result = self._values.get("root_device_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''The instance's Amazon EC2 key-pair name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-sshkeyname
        '''
        result = self._values.get("ssh_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the instance's subnet.

        If the stack is running in a VPC, you can use this parameter to override the stack's default subnet ID value and direct AWS OpsWorks Stacks to launch the instance in a different subnet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''The instance's tenancy option.

        The default option is no tenancy, or if the instance is running in a VPC, inherit tenancy settings from the VPC. The following are valid values for this parameter: ``dedicated`` , ``default`` , or ``host`` . Because there are costs associated with changes in tenancy options, we recommend that you research tenancy options before choosing them for your instances. For more information about dedicated hosts, see `Dedicated Hosts Overview <https://docs.aws.amazon.com/ec2/dedicated-hosts/>`_ and `Amazon EC2 Dedicated Hosts <https://docs.aws.amazon.com/ec2/dedicated-hosts/>`_ . For more information about dedicated instances, see `Dedicated Instances <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/dedicated-instance.html>`_ and `Amazon EC2 Dedicated Instances <https://docs.aws.amazon.com/ec2/purchasing-options/dedicated-instances/>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-tenancy
        '''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_based_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.TimeBasedAutoScalingProperty]]:
        '''The time-based scaling configuration for the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-timebasedautoscaling
        '''
        result = self._values.get("time_based_auto_scaling")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.TimeBasedAutoScalingProperty]], result)

    @builtins.property
    def virtualization_type(self) -> typing.Optional[builtins.str]:
        '''The instance's virtualization type, ``paravirtual`` or ``hvm`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-virtualizationtype
        '''
        result = self._values.get("virtualization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS OpsWorks volume IDs to associate with the instance.

        For more information, see ```AWS::OpsWorks::Volume`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLayer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opsworks.CfnLayer",
):
    '''Creates a layer. For more information, see `How to Create a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-create.html>`_ .

    .. epigraph::

       You should use *CreateLayer* for noncustom layer types such as PHP App Server only if the stack does not have an existing layer of that type. A stack can have at most one instance of each noncustom layer; if you attempt to create a second instance, *CreateLayer* fails. A stack can have an arbitrary number of custom layers, so you can call *CreateLayer* as many times as you like for that layer type.

    *Required Permissions* : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opsworks as opsworks
        
        # custom_json: Any
        
        cfn_layer = opsworks.CfnLayer(self, "MyCfnLayer",
            auto_assign_elastic_ips=False,
            auto_assign_public_ips=False,
            enable_auto_healing=False,
            name="name",
            shortname="shortname",
            stack_id="stackId",
            type="type",
        
            # the properties below are optional
            attributes={
                "attributes_key": "attributes"
            },
            custom_instance_profile_arn="customInstanceProfileArn",
            custom_json=custom_json,
            custom_recipes=opsworks.CfnLayer.RecipesProperty(
                configure=["configure"],
                deploy=["deploy"],
                setup=["setup"],
                shutdown=["shutdown"],
                undeploy=["undeploy"]
            ),
            custom_security_group_ids=["customSecurityGroupIds"],
            install_updates_on_boot=False,
            lifecycle_event_configuration=opsworks.CfnLayer.LifecycleEventConfigurationProperty(
                shutdown_event_configuration=opsworks.CfnLayer.ShutdownEventConfigurationProperty(
                    delay_until_elb_connections_drained=False,
                    execution_timeout=123
                )
            ),
            load_based_auto_scaling=opsworks.CfnLayer.LoadBasedAutoScalingProperty(
                down_scaling=opsworks.CfnLayer.AutoScalingThresholdsProperty(
                    cpu_threshold=123,
                    ignore_metrics_time=123,
                    instance_count=123,
                    load_threshold=123,
                    memory_threshold=123,
                    thresholds_wait_time=123
                ),
                enable=False,
                up_scaling=opsworks.CfnLayer.AutoScalingThresholdsProperty(
                    cpu_threshold=123,
                    ignore_metrics_time=123,
                    instance_count=123,
                    load_threshold=123,
                    memory_threshold=123,
                    thresholds_wait_time=123
                )
            ),
            packages=["packages"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            use_ebs_optimized_instances=False,
            volume_configurations=[opsworks.CfnLayer.VolumeConfigurationProperty(
                encrypted=False,
                iops=123,
                mount_point="mountPoint",
                number_of_disks=123,
                raid_level=123,
                size=123,
                volume_type="volumeType"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        auto_assign_elastic_ips: typing.Union[builtins.bool, _IResolvable_da3f097b],
        auto_assign_public_ips: typing.Union[builtins.bool, _IResolvable_da3f097b],
        enable_auto_healing: typing.Union[builtins.bool, _IResolvable_da3f097b],
        name: builtins.str,
        shortname: builtins.str,
        stack_id: builtins.str,
        type: builtins.str,
        attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Any = None,
        custom_recipes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLayer.RecipesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        lifecycle_event_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLayer.LifecycleEventConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        load_based_auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLayer.LoadBasedAutoScalingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        volume_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLayer.VolumeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_assign_elastic_ips: Whether to automatically assign an `Elastic IP address <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`_ to the layer's instances. For more information, see `How to Edit a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`_ .
        :param auto_assign_public_ips: For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see `How to Edit a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`_ .
        :param enable_auto_healing: Whether to disable auto healing for the layer.
        :param name: The layer name, which is used by the console. Layer names can be a maximum of 32 characters.
        :param shortname: For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorks Stacks and by Chef recipes. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 32 characters, which are limited to the alphanumeric characters, '-', '_', and '.'. Built-in layer short names are defined by AWS OpsWorks Stacks. For more information, see the `Layer Reference <https://docs.aws.amazon.com/opsworks/latest/userguide/layers.html>`_ .
        :param stack_id: The layer stack ID.
        :param type: The layer type. A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.
        :param attributes: One or more user-defined key-value pairs to be added to the stack attributes. To create a cluster layer, set the ``EcsClusterArn`` attribute to the cluster's ARN.
        :param custom_instance_profile_arn: The ARN of an IAM profile to be used for the layer's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .
        :param custom_json: A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances. For more information, see `Using Custom JSON <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html>`_ . This feature is supported as of version 1.7.42 of the AWS CLI .
        :param custom_recipes: A ``LayerCustomRecipes`` object that specifies the layer custom recipes.
        :param custom_security_group_ids: An array containing the layer custom security group IDs.
        :param install_updates_on_boot: Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using `CreateDeployment <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateDeployment>`_ to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. .. epigraph:: To ensure that your instances have the latest security updates, we strongly recommend using the default value of ``true`` .
        :param lifecycle_event_configuration: A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.
        :param load_based_auto_scaling: The load-based scaling configuration for the AWS OpsWorks layer.
        :param packages: An array of ``Package`` objects that describes the layer packages.
        :param tags: Specifies one or more sets of tags (key–value pairs) to associate with this AWS OpsWorks layer. Use tags to manage your resources.
        :param use_ebs_optimized_instances: Whether to use Amazon EBS-optimized instances.
        :param volume_configurations: A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de185bdebf2e1467933cd283fec95f5a7ee02ecc41533bdbfa207c91a7c0a2f6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLayerProps(
            auto_assign_elastic_ips=auto_assign_elastic_ips,
            auto_assign_public_ips=auto_assign_public_ips,
            enable_auto_healing=enable_auto_healing,
            name=name,
            shortname=shortname,
            stack_id=stack_id,
            type=type,
            attributes=attributes,
            custom_instance_profile_arn=custom_instance_profile_arn,
            custom_json=custom_json,
            custom_recipes=custom_recipes,
            custom_security_group_ids=custom_security_group_ids,
            install_updates_on_boot=install_updates_on_boot,
            lifecycle_event_configuration=lifecycle_event_configuration,
            load_based_auto_scaling=load_based_auto_scaling,
            packages=packages,
            tags=tags,
            use_ebs_optimized_instances=use_ebs_optimized_instances,
            volume_configurations=volume_configurations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7769a3e709144e0e4d9e73a65055fcd2f8d00ee6279aa832c4c84ee943b42c6d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__769f052c927ec888e5dedc99e8521b022c0d238f66f201857a9a5305dc4c82fc)
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
    @jsii.member(jsii_name="autoAssignElasticIps")
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether to automatically assign an `Elastic IP address <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`_ to the layer's instances. For more information, see `How to Edit a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`_ .'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "autoAssignElasticIps"))

    @auto_assign_elastic_ips.setter
    def auto_assign_elastic_ips(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85978378733517803f89d7ce8ed749075b2acc8dc7d04f6b6e0c7e704d227ace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAssignElasticIps", value)

    @builtins.property
    @jsii.member(jsii_name="autoAssignPublicIps")
    def auto_assign_public_ips(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "autoAssignPublicIps"))

    @auto_assign_public_ips.setter
    def auto_assign_public_ips(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8ba55dbdeca1c05ff112a4836e57cd64cee40b72e11ac77b619cf736bfd51b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAssignPublicIps", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutoHealing")
    def enable_auto_healing(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether to disable auto healing for the layer.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "enableAutoHealing"))

    @enable_auto_healing.setter
    def enable_auto_healing(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2351ccfe7eb13aba979ae0e393a2fd47e40926de22ecf6aba42a950ceba9ccca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutoHealing", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The layer name, which is used by the console.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca8c56695fb83a676e32457bc6de19365f9c70eec1584dbc6f23606906b879d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="shortname")
    def shortname(self) -> builtins.str:
        '''For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorks Stacks and by Chef recipes.'''
        return typing.cast(builtins.str, jsii.get(self, "shortname"))

    @shortname.setter
    def shortname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846e6bcd67b109f59c3750304d8d8b6cb95ffa7b5e053a4d7f66bbb41bec35f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortname", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''The layer stack ID.'''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada31ec8e271ee88cd1fad4807bc6d4219ba3ae931955ab18863e4f5bbc716bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The layer type.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__450ddd14c164d17317234149c9d02cecfd7b8da38ff8262ee9a2fcb25becd9be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''One or more user-defined key-value pairs to be added to the stack attributes.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9395644dbf3af1a765e40fb019bf24792671a4e69e059385183e9f7d8c09cef2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="customInstanceProfileArn")
    def custom_instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM profile to be used for the layer's EC2 instances.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customInstanceProfileArn"))

    @custom_instance_profile_arn.setter
    def custom_instance_profile_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6bd9eae8e2c43a63cc326dd83cd4cf25a20c2fda16a523fe488beec31c627be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customInstanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> typing.Any:
        '''A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances.'''
        return typing.cast(typing.Any, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51213828c84c59f5b40dc3f53612fe0e252973a059400094e40e3bf915b9fc80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customJson", value)

    @builtins.property
    @jsii.member(jsii_name="customRecipes")
    def custom_recipes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.RecipesProperty"]]:
        '''A ``LayerCustomRecipes`` object that specifies the layer custom recipes.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.RecipesProperty"]], jsii.get(self, "customRecipes"))

    @custom_recipes.setter
    def custom_recipes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.RecipesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e8c90b7b1058521d04d7f21c3b8bccb95a8c0f24ba2839b2d6f0cd9595fdc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customRecipes", value)

    @builtins.property
    @jsii.member(jsii_name="customSecurityGroupIds")
    def custom_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array containing the layer custom security group IDs.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customSecurityGroupIds"))

    @custom_security_group_ids.setter
    def custom_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723bdf1798a6528f78499e56e3182d783681319599779eb826934d2c59139a04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="installUpdatesOnBoot")
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to install operating system and package updates when the instance boots.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "installUpdatesOnBoot"))

    @install_updates_on_boot.setter
    def install_updates_on_boot(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b42c4216b135b2a7074bfed5d80d9da1ba492a773d32e212a7237b6ebc391540)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "installUpdatesOnBoot", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleEventConfiguration")
    def lifecycle_event_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.LifecycleEventConfigurationProperty"]]:
        '''A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.LifecycleEventConfigurationProperty"]], jsii.get(self, "lifecycleEventConfiguration"))

    @lifecycle_event_configuration.setter
    def lifecycle_event_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.LifecycleEventConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbfa971c40efb5d7a653e36e1485b5fbe539dada94fc400376fe7e3b2cc83f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleEventConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="loadBasedAutoScaling")
    def load_based_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.LoadBasedAutoScalingProperty"]]:
        '''The load-based scaling configuration for the AWS OpsWorks layer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.LoadBasedAutoScalingProperty"]], jsii.get(self, "loadBasedAutoScaling"))

    @load_based_auto_scaling.setter
    def load_based_auto_scaling(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.LoadBasedAutoScalingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8787d1ac56a7ea2ee28e6088302bfb26415ba39511d17c7faa187287901d8aca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBasedAutoScaling", value)

    @builtins.property
    @jsii.member(jsii_name="packages")
    def packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of ``Package`` objects that describes the layer packages.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "packages"))

    @packages.setter
    def packages(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e23cd593d0b608a8a2ae24f2f02c6ee8d2c3fff203db62c80de805c29dbca4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packages", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies one or more sets of tags (key–value pairs) to associate with this AWS OpsWorks layer.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c7cab1714e0f9090eff8c2189561d0d041f66002f761e700cf53a8945ad6a1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="useEbsOptimizedInstances")
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to use Amazon EBS-optimized instances.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "useEbsOptimizedInstances"))

    @use_ebs_optimized_instances.setter
    def use_ebs_optimized_instances(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33349ab02f637b084f62e0224a27ce7354d923ff559128f7665a25e2318617ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useEbsOptimizedInstances", value)

    @builtins.property
    @jsii.member(jsii_name="volumeConfigurations")
    def volume_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLayer.VolumeConfigurationProperty"]]]]:
        '''A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLayer.VolumeConfigurationProperty"]]]], jsii.get(self, "volumeConfigurations"))

    @volume_configurations.setter
    def volume_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLayer.VolumeConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ed3702ce91b7433e1b5faab32e09d55b2da499fcfb988423341ceb00a2b770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeConfigurations", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnLayer.AutoScalingThresholdsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu_threshold": "cpuThreshold",
            "ignore_metrics_time": "ignoreMetricsTime",
            "instance_count": "instanceCount",
            "load_threshold": "loadThreshold",
            "memory_threshold": "memoryThreshold",
            "thresholds_wait_time": "thresholdsWaitTime",
        },
    )
    class AutoScalingThresholdsProperty:
        def __init__(
            self,
            *,
            cpu_threshold: typing.Optional[jsii.Number] = None,
            ignore_metrics_time: typing.Optional[jsii.Number] = None,
            instance_count: typing.Optional[jsii.Number] = None,
            load_threshold: typing.Optional[jsii.Number] = None,
            memory_threshold: typing.Optional[jsii.Number] = None,
            thresholds_wait_time: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes a load-based auto scaling upscaling or downscaling threshold configuration, which specifies when AWS OpsWorks Stacks starts or stops load-based instances.

            :param cpu_threshold: The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.
            :param ignore_metrics_time: The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.
            :param instance_count: The number of instances to add or remove when the load exceeds a threshold.
            :param load_threshold: The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see `Load (computing) <https://docs.aws.amazon.com/http://en.wikipedia.org/wiki/Load_%28computing%29>`_ .
            :param memory_threshold: The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.
            :param thresholds_wait_time: The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-autoscalingthresholds.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                auto_scaling_thresholds_property = opsworks.CfnLayer.AutoScalingThresholdsProperty(
                    cpu_threshold=123,
                    ignore_metrics_time=123,
                    instance_count=123,
                    load_threshold=123,
                    memory_threshold=123,
                    thresholds_wait_time=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__acebc56803bcaeb1947cfcc6e9e93fe43ceb2078e18ddbfd025a38603d4f7d58)
                check_type(argname="argument cpu_threshold", value=cpu_threshold, expected_type=type_hints["cpu_threshold"])
                check_type(argname="argument ignore_metrics_time", value=ignore_metrics_time, expected_type=type_hints["ignore_metrics_time"])
                check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
                check_type(argname="argument load_threshold", value=load_threshold, expected_type=type_hints["load_threshold"])
                check_type(argname="argument memory_threshold", value=memory_threshold, expected_type=type_hints["memory_threshold"])
                check_type(argname="argument thresholds_wait_time", value=thresholds_wait_time, expected_type=type_hints["thresholds_wait_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cpu_threshold is not None:
                self._values["cpu_threshold"] = cpu_threshold
            if ignore_metrics_time is not None:
                self._values["ignore_metrics_time"] = ignore_metrics_time
            if instance_count is not None:
                self._values["instance_count"] = instance_count
            if load_threshold is not None:
                self._values["load_threshold"] = load_threshold
            if memory_threshold is not None:
                self._values["memory_threshold"] = memory_threshold
            if thresholds_wait_time is not None:
                self._values["thresholds_wait_time"] = thresholds_wait_time

        @builtins.property
        def cpu_threshold(self) -> typing.Optional[jsii.Number]:
            '''The CPU utilization threshold, as a percent of the available CPU.

            A value of -1 disables the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-autoscalingthresholds.html#cfn-opsworks-layer-autoscalingthresholds-cputhreshold
            '''
            result = self._values.get("cpu_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
            '''The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events.

            For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-autoscalingthresholds.html#cfn-opsworks-layer-autoscalingthresholds-ignoremetricstime
            '''
            result = self._values.get("ignore_metrics_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def instance_count(self) -> typing.Optional[jsii.Number]:
            '''The number of instances to add or remove when the load exceeds a threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-autoscalingthresholds.html#cfn-opsworks-layer-autoscalingthresholds-instancecount
            '''
            result = self._values.get("instance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def load_threshold(self) -> typing.Optional[jsii.Number]:
            '''The load threshold.

            A value of -1 disables the threshold. For more information about how load is computed, see `Load (computing) <https://docs.aws.amazon.com/http://en.wikipedia.org/wiki/Load_%28computing%29>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-autoscalingthresholds.html#cfn-opsworks-layer-autoscalingthresholds-loadthreshold
            '''
            result = self._values.get("load_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def memory_threshold(self) -> typing.Optional[jsii.Number]:
            '''The memory utilization threshold, as a percent of the available memory.

            A value of -1 disables the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-autoscalingthresholds.html#cfn-opsworks-layer-autoscalingthresholds-memorythreshold
            '''
            result = self._values.get("memory_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-autoscalingthresholds.html#cfn-opsworks-layer-autoscalingthresholds-thresholdswaittime
            '''
            result = self._values.get("thresholds_wait_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingThresholdsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnLayer.LifecycleEventConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"shutdown_event_configuration": "shutdownEventConfiguration"},
    )
    class LifecycleEventConfigurationProperty:
        def __init__(
            self,
            *,
            shutdown_event_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLayer.ShutdownEventConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the lifecycle event configuration.

            :param shutdown_event_configuration: The Shutdown event configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                lifecycle_event_configuration_property = opsworks.CfnLayer.LifecycleEventConfigurationProperty(
                    shutdown_event_configuration=opsworks.CfnLayer.ShutdownEventConfigurationProperty(
                        delay_until_elb_connections_drained=False,
                        execution_timeout=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7e4d41a79209a667596801a266fe03f27f87757282622ff6914569435490ee0b)
                check_type(argname="argument shutdown_event_configuration", value=shutdown_event_configuration, expected_type=type_hints["shutdown_event_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if shutdown_event_configuration is not None:
                self._values["shutdown_event_configuration"] = shutdown_event_configuration

        @builtins.property
        def shutdown_event_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.ShutdownEventConfigurationProperty"]]:
            '''The Shutdown event configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html#cfn-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration
            '''
            result = self._values.get("shutdown_event_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.ShutdownEventConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleEventConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnLayer.LoadBasedAutoScalingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "down_scaling": "downScaling",
            "enable": "enable",
            "up_scaling": "upScaling",
        },
    )
    class LoadBasedAutoScalingProperty:
        def __init__(
            self,
            *,
            down_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLayer.AutoScalingThresholdsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            up_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLayer.AutoScalingThresholdsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a layer's load-based auto scaling configuration.

            :param down_scaling: An ``AutoScalingThresholds`` object that describes the downscaling configuration, which defines how and when AWS OpsWorks Stacks reduces the number of instances.
            :param enable: Whether load-based auto scaling is enabled for the layer.
            :param up_scaling: An ``AutoScalingThresholds`` object that describes the upscaling configuration, which defines how and when AWS OpsWorks Stacks increases the number of instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                load_based_auto_scaling_property = opsworks.CfnLayer.LoadBasedAutoScalingProperty(
                    down_scaling=opsworks.CfnLayer.AutoScalingThresholdsProperty(
                        cpu_threshold=123,
                        ignore_metrics_time=123,
                        instance_count=123,
                        load_threshold=123,
                        memory_threshold=123,
                        thresholds_wait_time=123
                    ),
                    enable=False,
                    up_scaling=opsworks.CfnLayer.AutoScalingThresholdsProperty(
                        cpu_threshold=123,
                        ignore_metrics_time=123,
                        instance_count=123,
                        load_threshold=123,
                        memory_threshold=123,
                        thresholds_wait_time=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c3d73f44ac3a86ed5c0f519f220ff022c6fefbedfca846c4bd6bda3db1f1a111)
                check_type(argname="argument down_scaling", value=down_scaling, expected_type=type_hints["down_scaling"])
                check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
                check_type(argname="argument up_scaling", value=up_scaling, expected_type=type_hints["up_scaling"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if down_scaling is not None:
                self._values["down_scaling"] = down_scaling
            if enable is not None:
                self._values["enable"] = enable
            if up_scaling is not None:
                self._values["up_scaling"] = up_scaling

        @builtins.property
        def down_scaling(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.AutoScalingThresholdsProperty"]]:
            '''An ``AutoScalingThresholds`` object that describes the downscaling configuration, which defines how and when AWS OpsWorks Stacks reduces the number of instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-downscaling
            '''
            result = self._values.get("down_scaling")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.AutoScalingThresholdsProperty"]], result)

        @builtins.property
        def enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether load-based auto scaling is enabled for the layer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-enable
            '''
            result = self._values.get("enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def up_scaling(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.AutoScalingThresholdsProperty"]]:
            '''An ``AutoScalingThresholds`` object that describes the upscaling configuration, which defines how and when AWS OpsWorks Stacks increases the number of instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-upscaling
            '''
            result = self._values.get("up_scaling")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLayer.AutoScalingThresholdsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoadBasedAutoScalingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnLayer.RecipesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configure": "configure",
            "deploy": "deploy",
            "setup": "setup",
            "shutdown": "shutdown",
            "undeploy": "undeploy",
        },
    )
    class RecipesProperty:
        def __init__(
            self,
            *,
            configure: typing.Optional[typing.Sequence[builtins.str]] = None,
            deploy: typing.Optional[typing.Sequence[builtins.str]] = None,
            setup: typing.Optional[typing.Sequence[builtins.str]] = None,
            shutdown: typing.Optional[typing.Sequence[builtins.str]] = None,
            undeploy: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''AWS OpsWorks Stacks supports five lifecycle events: *setup* , *configuration* , *deploy* , *undeploy* , and *shutdown* .

            For each layer, AWS OpsWorks Stacks runs a set of standard recipes for each event. In addition, you can provide custom recipes for any or all layers and events. AWS OpsWorks Stacks runs custom event recipes after the standard recipes. ``LayerCustomRecipes`` specifies the custom recipes for a particular layer to be run in response to each of the five events.

            To specify a recipe, use the cookbook's directory name in the repository followed by two colons and the recipe name, which is the recipe's file name without the .rb extension. For example: phpapp2::dbsetup specifies the dbsetup.rb recipe in the repository's phpapp2 folder.

            :param configure: An array of custom recipe names to be run following a ``configure`` event.
            :param deploy: An array of custom recipe names to be run following a ``deploy`` event.
            :param setup: An array of custom recipe names to be run following a ``setup`` event.
            :param shutdown: An array of custom recipe names to be run following a ``shutdown`` event.
            :param undeploy: An array of custom recipe names to be run following a ``undeploy`` event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                recipes_property = opsworks.CfnLayer.RecipesProperty(
                    configure=["configure"],
                    deploy=["deploy"],
                    setup=["setup"],
                    shutdown=["shutdown"],
                    undeploy=["undeploy"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e47cee19e47a49ee1c8993063e7798b7abccb6bd1dd66e69db20146863771f58)
                check_type(argname="argument configure", value=configure, expected_type=type_hints["configure"])
                check_type(argname="argument deploy", value=deploy, expected_type=type_hints["deploy"])
                check_type(argname="argument setup", value=setup, expected_type=type_hints["setup"])
                check_type(argname="argument shutdown", value=shutdown, expected_type=type_hints["shutdown"])
                check_type(argname="argument undeploy", value=undeploy, expected_type=type_hints["undeploy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if configure is not None:
                self._values["configure"] = configure
            if deploy is not None:
                self._values["deploy"] = deploy
            if setup is not None:
                self._values["setup"] = setup
            if shutdown is not None:
                self._values["shutdown"] = shutdown
            if undeploy is not None:
                self._values["undeploy"] = undeploy

        @builtins.property
        def configure(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of custom recipe names to be run following a ``configure`` event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-recipes-configure
            '''
            result = self._values.get("configure")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def deploy(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of custom recipe names to be run following a ``deploy`` event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-recipes-deploy
            '''
            result = self._values.get("deploy")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def setup(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of custom recipe names to be run following a ``setup`` event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-recipes-setup
            '''
            result = self._values.get("setup")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def shutdown(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of custom recipe names to be run following a ``shutdown`` event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-recipes-shutdown
            '''
            result = self._values.get("shutdown")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def undeploy(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of custom recipe names to be run following a ``undeploy`` event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-recipes-undeploy
            '''
            result = self._values.get("undeploy")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecipesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnLayer.ShutdownEventConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delay_until_elb_connections_drained": "delayUntilElbConnectionsDrained",
            "execution_timeout": "executionTimeout",
        },
    )
    class ShutdownEventConfigurationProperty:
        def __init__(
            self,
            *,
            delay_until_elb_connections_drained: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            execution_timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The Shutdown event configuration.

            :param delay_until_elb_connections_drained: Whether to enable Elastic Load Balancing connection draining. For more information, see `Connection Draining <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`_
            :param execution_timeout: The time, in seconds, that AWS OpsWorks Stacks waits after triggering a Shutdown event before shutting down an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-shutdowneventconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                shutdown_event_configuration_property = opsworks.CfnLayer.ShutdownEventConfigurationProperty(
                    delay_until_elb_connections_drained=False,
                    execution_timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b4b5a1198632d836216abf1c68ad55d170601286c9e14f18bb5e66d2491cbd3)
                check_type(argname="argument delay_until_elb_connections_drained", value=delay_until_elb_connections_drained, expected_type=type_hints["delay_until_elb_connections_drained"])
                check_type(argname="argument execution_timeout", value=execution_timeout, expected_type=type_hints["execution_timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delay_until_elb_connections_drained is not None:
                self._values["delay_until_elb_connections_drained"] = delay_until_elb_connections_drained
            if execution_timeout is not None:
                self._values["execution_timeout"] = execution_timeout

        @builtins.property
        def delay_until_elb_connections_drained(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to enable Elastic Load Balancing connection draining.

            For more information, see `Connection Draining <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-shutdowneventconfiguration.html#cfn-opsworks-layer-shutdowneventconfiguration-delayuntilelbconnectionsdrained
            '''
            result = self._values.get("delay_until_elb_connections_drained")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def execution_timeout(self) -> typing.Optional[jsii.Number]:
            '''The time, in seconds, that AWS OpsWorks Stacks waits after triggering a Shutdown event before shutting down an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-shutdowneventconfiguration.html#cfn-opsworks-layer-shutdowneventconfiguration-executiontimeout
            '''
            result = self._values.get("execution_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ShutdownEventConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnLayer.VolumeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encrypted": "encrypted",
            "iops": "iops",
            "mount_point": "mountPoint",
            "number_of_disks": "numberOfDisks",
            "raid_level": "raidLevel",
            "size": "size",
            "volume_type": "volumeType",
        },
    )
    class VolumeConfigurationProperty:
        def __init__(
            self,
            *,
            encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            iops: typing.Optional[jsii.Number] = None,
            mount_point: typing.Optional[builtins.str] = None,
            number_of_disks: typing.Optional[jsii.Number] = None,
            raid_level: typing.Optional[jsii.Number] = None,
            size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an Amazon EBS volume configuration.

            :param encrypted: Specifies whether an Amazon EBS volume is encrypted. For more information, see `Amazon EBS Encryption <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`_ .
            :param iops: The number of I/O operations per second (IOPS) to provision for the volume. For PIOPS volumes, the IOPS per disk. If you specify ``io1`` for the volume type, you must specify this property.
            :param mount_point: The volume mount point. For example "/dev/sdh".
            :param number_of_disks: The number of disks in the volume.
            :param raid_level: The volume `RAID level <https://docs.aws.amazon.com/http://en.wikipedia.org/wiki/Standard_RAID_levels>`_ .
            :param size: The volume size.
            :param volume_type: The volume type. For more information, see `Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`_ . - ``standard`` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB. - ``io1`` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB. - ``gp2`` - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB. - ``st1`` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB. - ``sc1`` - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                volume_configuration_property = opsworks.CfnLayer.VolumeConfigurationProperty(
                    encrypted=False,
                    iops=123,
                    mount_point="mountPoint",
                    number_of_disks=123,
                    raid_level=123,
                    size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35bb02a582c61891e39f2981442acc233a0b3ee0ff93a8df791d8e2bf0ca5950)
                check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument mount_point", value=mount_point, expected_type=type_hints["mount_point"])
                check_type(argname="argument number_of_disks", value=number_of_disks, expected_type=type_hints["number_of_disks"])
                check_type(argname="argument raid_level", value=raid_level, expected_type=type_hints["raid_level"])
                check_type(argname="argument size", value=size, expected_type=type_hints["size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if mount_point is not None:
                self._values["mount_point"] = mount_point
            if number_of_disks is not None:
                self._values["number_of_disks"] = number_of_disks
            if raid_level is not None:
                self._values["raid_level"] = raid_level
            if size is not None:
                self._values["size"] = size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether an Amazon EBS volume is encrypted.

            For more information, see `Amazon EBS Encryption <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The number of I/O operations per second (IOPS) to provision for the volume.

            For PIOPS volumes, the IOPS per disk.

            If you specify ``io1`` for the volume type, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_point(self) -> typing.Optional[builtins.str]:
            '''The volume mount point.

            For example "/dev/sdh".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-mountpoint
            '''
            result = self._values.get("mount_point")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def number_of_disks(self) -> typing.Optional[jsii.Number]:
            '''The number of disks in the volume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-numberofdisks
            '''
            result = self._values.get("number_of_disks")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def raid_level(self) -> typing.Optional[jsii.Number]:
            '''The volume `RAID level <https://docs.aws.amazon.com/http://en.wikipedia.org/wiki/Standard_RAID_levels>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-raidlevel
            '''
            result = self._values.get("raid_level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size(self) -> typing.Optional[jsii.Number]:
            '''The volume size.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-size
            '''
            result = self._values.get("size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''The volume type. For more information, see `Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`_ .

            - ``standard`` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.
            - ``io1`` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.
            - ``gp2`` - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.
            - ``st1`` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.
            - ``sc1`` - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opsworks.CfnLayerProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_assign_elastic_ips": "autoAssignElasticIps",
        "auto_assign_public_ips": "autoAssignPublicIps",
        "enable_auto_healing": "enableAutoHealing",
        "name": "name",
        "shortname": "shortname",
        "stack_id": "stackId",
        "type": "type",
        "attributes": "attributes",
        "custom_instance_profile_arn": "customInstanceProfileArn",
        "custom_json": "customJson",
        "custom_recipes": "customRecipes",
        "custom_security_group_ids": "customSecurityGroupIds",
        "install_updates_on_boot": "installUpdatesOnBoot",
        "lifecycle_event_configuration": "lifecycleEventConfiguration",
        "load_based_auto_scaling": "loadBasedAutoScaling",
        "packages": "packages",
        "tags": "tags",
        "use_ebs_optimized_instances": "useEbsOptimizedInstances",
        "volume_configurations": "volumeConfigurations",
    },
)
class CfnLayerProps:
    def __init__(
        self,
        *,
        auto_assign_elastic_ips: typing.Union[builtins.bool, _IResolvable_da3f097b],
        auto_assign_public_ips: typing.Union[builtins.bool, _IResolvable_da3f097b],
        enable_auto_healing: typing.Union[builtins.bool, _IResolvable_da3f097b],
        name: builtins.str,
        shortname: builtins.str,
        stack_id: builtins.str,
        type: builtins.str,
        attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Any = None,
        custom_recipes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.RecipesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        lifecycle_event_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.LifecycleEventConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        load_based_auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.LoadBasedAutoScalingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        volume_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.VolumeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLayer``.

        :param auto_assign_elastic_ips: Whether to automatically assign an `Elastic IP address <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`_ to the layer's instances. For more information, see `How to Edit a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`_ .
        :param auto_assign_public_ips: For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see `How to Edit a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`_ .
        :param enable_auto_healing: Whether to disable auto healing for the layer.
        :param name: The layer name, which is used by the console. Layer names can be a maximum of 32 characters.
        :param shortname: For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorks Stacks and by Chef recipes. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 32 characters, which are limited to the alphanumeric characters, '-', '_', and '.'. Built-in layer short names are defined by AWS OpsWorks Stacks. For more information, see the `Layer Reference <https://docs.aws.amazon.com/opsworks/latest/userguide/layers.html>`_ .
        :param stack_id: The layer stack ID.
        :param type: The layer type. A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.
        :param attributes: One or more user-defined key-value pairs to be added to the stack attributes. To create a cluster layer, set the ``EcsClusterArn`` attribute to the cluster's ARN.
        :param custom_instance_profile_arn: The ARN of an IAM profile to be used for the layer's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .
        :param custom_json: A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances. For more information, see `Using Custom JSON <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html>`_ . This feature is supported as of version 1.7.42 of the AWS CLI .
        :param custom_recipes: A ``LayerCustomRecipes`` object that specifies the layer custom recipes.
        :param custom_security_group_ids: An array containing the layer custom security group IDs.
        :param install_updates_on_boot: Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using `CreateDeployment <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateDeployment>`_ to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. .. epigraph:: To ensure that your instances have the latest security updates, we strongly recommend using the default value of ``true`` .
        :param lifecycle_event_configuration: A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.
        :param load_based_auto_scaling: The load-based scaling configuration for the AWS OpsWorks layer.
        :param packages: An array of ``Package`` objects that describes the layer packages.
        :param tags: Specifies one or more sets of tags (key–value pairs) to associate with this AWS OpsWorks layer. Use tags to manage your resources.
        :param use_ebs_optimized_instances: Whether to use Amazon EBS-optimized instances.
        :param volume_configurations: A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opsworks as opsworks
            
            # custom_json: Any
            
            cfn_layer_props = opsworks.CfnLayerProps(
                auto_assign_elastic_ips=False,
                auto_assign_public_ips=False,
                enable_auto_healing=False,
                name="name",
                shortname="shortname",
                stack_id="stackId",
                type="type",
            
                # the properties below are optional
                attributes={
                    "attributes_key": "attributes"
                },
                custom_instance_profile_arn="customInstanceProfileArn",
                custom_json=custom_json,
                custom_recipes=opsworks.CfnLayer.RecipesProperty(
                    configure=["configure"],
                    deploy=["deploy"],
                    setup=["setup"],
                    shutdown=["shutdown"],
                    undeploy=["undeploy"]
                ),
                custom_security_group_ids=["customSecurityGroupIds"],
                install_updates_on_boot=False,
                lifecycle_event_configuration=opsworks.CfnLayer.LifecycleEventConfigurationProperty(
                    shutdown_event_configuration=opsworks.CfnLayer.ShutdownEventConfigurationProperty(
                        delay_until_elb_connections_drained=False,
                        execution_timeout=123
                    )
                ),
                load_based_auto_scaling=opsworks.CfnLayer.LoadBasedAutoScalingProperty(
                    down_scaling=opsworks.CfnLayer.AutoScalingThresholdsProperty(
                        cpu_threshold=123,
                        ignore_metrics_time=123,
                        instance_count=123,
                        load_threshold=123,
                        memory_threshold=123,
                        thresholds_wait_time=123
                    ),
                    enable=False,
                    up_scaling=opsworks.CfnLayer.AutoScalingThresholdsProperty(
                        cpu_threshold=123,
                        ignore_metrics_time=123,
                        instance_count=123,
                        load_threshold=123,
                        memory_threshold=123,
                        thresholds_wait_time=123
                    )
                ),
                packages=["packages"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                use_ebs_optimized_instances=False,
                volume_configurations=[opsworks.CfnLayer.VolumeConfigurationProperty(
                    encrypted=False,
                    iops=123,
                    mount_point="mountPoint",
                    number_of_disks=123,
                    raid_level=123,
                    size=123,
                    volume_type="volumeType"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44c38216d74d64877783d8570f455e1bede8bb638962a7d006b49b8f741161c6)
            check_type(argname="argument auto_assign_elastic_ips", value=auto_assign_elastic_ips, expected_type=type_hints["auto_assign_elastic_ips"])
            check_type(argname="argument auto_assign_public_ips", value=auto_assign_public_ips, expected_type=type_hints["auto_assign_public_ips"])
            check_type(argname="argument enable_auto_healing", value=enable_auto_healing, expected_type=type_hints["enable_auto_healing"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument shortname", value=shortname, expected_type=type_hints["shortname"])
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument custom_instance_profile_arn", value=custom_instance_profile_arn, expected_type=type_hints["custom_instance_profile_arn"])
            check_type(argname="argument custom_json", value=custom_json, expected_type=type_hints["custom_json"])
            check_type(argname="argument custom_recipes", value=custom_recipes, expected_type=type_hints["custom_recipes"])
            check_type(argname="argument custom_security_group_ids", value=custom_security_group_ids, expected_type=type_hints["custom_security_group_ids"])
            check_type(argname="argument install_updates_on_boot", value=install_updates_on_boot, expected_type=type_hints["install_updates_on_boot"])
            check_type(argname="argument lifecycle_event_configuration", value=lifecycle_event_configuration, expected_type=type_hints["lifecycle_event_configuration"])
            check_type(argname="argument load_based_auto_scaling", value=load_based_auto_scaling, expected_type=type_hints["load_based_auto_scaling"])
            check_type(argname="argument packages", value=packages, expected_type=type_hints["packages"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument use_ebs_optimized_instances", value=use_ebs_optimized_instances, expected_type=type_hints["use_ebs_optimized_instances"])
            check_type(argname="argument volume_configurations", value=volume_configurations, expected_type=type_hints["volume_configurations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_assign_elastic_ips": auto_assign_elastic_ips,
            "auto_assign_public_ips": auto_assign_public_ips,
            "enable_auto_healing": enable_auto_healing,
            "name": name,
            "shortname": shortname,
            "stack_id": stack_id,
            "type": type,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if custom_instance_profile_arn is not None:
            self._values["custom_instance_profile_arn"] = custom_instance_profile_arn
        if custom_json is not None:
            self._values["custom_json"] = custom_json
        if custom_recipes is not None:
            self._values["custom_recipes"] = custom_recipes
        if custom_security_group_ids is not None:
            self._values["custom_security_group_ids"] = custom_security_group_ids
        if install_updates_on_boot is not None:
            self._values["install_updates_on_boot"] = install_updates_on_boot
        if lifecycle_event_configuration is not None:
            self._values["lifecycle_event_configuration"] = lifecycle_event_configuration
        if load_based_auto_scaling is not None:
            self._values["load_based_auto_scaling"] = load_based_auto_scaling
        if packages is not None:
            self._values["packages"] = packages
        if tags is not None:
            self._values["tags"] = tags
        if use_ebs_optimized_instances is not None:
            self._values["use_ebs_optimized_instances"] = use_ebs_optimized_instances
        if volume_configurations is not None:
            self._values["volume_configurations"] = volume_configurations

    @builtins.property
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether to automatically assign an `Elastic IP address <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`_ to the layer's instances. For more information, see `How to Edit a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignelasticips
        '''
        result = self._values.get("auto_assign_elastic_ips")
        assert result is not None, "Required property 'auto_assign_elastic_ips' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def auto_assign_public_ips(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances.

        For more information, see `How to Edit a Layer <https://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignpublicips
        '''
        result = self._values.get("auto_assign_public_ips")
        assert result is not None, "Required property 'auto_assign_public_ips' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def enable_auto_healing(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether to disable auto healing for the layer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-enableautohealing
        '''
        result = self._values.get("enable_auto_healing")
        assert result is not None, "Required property 'enable_auto_healing' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The layer name, which is used by the console.

        Layer names can be a maximum of 32 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shortname(self) -> builtins.str:
        '''For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorks Stacks and by Chef recipes.

        The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 32 characters, which are limited to the alphanumeric characters, '-', '_', and '.'.

        Built-in layer short names are defined by AWS OpsWorks Stacks. For more information, see the `Layer Reference <https://docs.aws.amazon.com/opsworks/latest/userguide/layers.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-shortname
        '''
        result = self._values.get("shortname")
        assert result is not None, "Required property 'shortname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''The layer stack ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-stackid
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The layer type.

        A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''One or more user-defined key-value pairs to be added to the stack attributes.

        To create a cluster layer, set the ``EcsClusterArn`` attribute to the cluster's ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

    @builtins.property
    def custom_instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM profile to be used for the layer's EC2 instances.

        For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-custominstanceprofilearn
        '''
        result = self._values.get("custom_instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_json(self) -> typing.Any:
        '''A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances.

        For more information, see `Using Custom JSON <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html>`_ . This feature is supported as of version 1.7.42 of the AWS CLI .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customjson
        '''
        result = self._values.get("custom_json")
        return typing.cast(typing.Any, result)

    @builtins.property
    def custom_recipes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.RecipesProperty]]:
        '''A ``LayerCustomRecipes`` object that specifies the layer custom recipes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customrecipes
        '''
        result = self._values.get("custom_recipes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.RecipesProperty]], result)

    @builtins.property
    def custom_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array containing the layer custom security group IDs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customsecuritygroupids
        '''
        result = self._values.get("custom_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to install operating system and package updates when the instance boots.

        The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using `CreateDeployment <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateDeployment>`_ to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances.
        .. epigraph::

           To ensure that your instances have the latest security updates, we strongly recommend using the default value of ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-installupdatesonboot
        '''
        result = self._values.get("install_updates_on_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def lifecycle_event_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.LifecycleEventConfigurationProperty]]:
        '''A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-lifecycleeventconfiguration
        '''
        result = self._values.get("lifecycle_event_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.LifecycleEventConfigurationProperty]], result)

    @builtins.property
    def load_based_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.LoadBasedAutoScalingProperty]]:
        '''The load-based scaling configuration for the AWS OpsWorks layer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-loadbasedautoscaling
        '''
        result = self._values.get("load_based_auto_scaling")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.LoadBasedAutoScalingProperty]], result)

    @builtins.property
    def packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of ``Package`` objects that describes the layer packages.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-packages
        '''
        result = self._values.get("packages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies one or more sets of tags (key–value pairs) to associate with this AWS OpsWorks layer.

        Use tags to manage your resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to use Amazon EBS-optimized instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-useebsoptimizedinstances
        '''
        result = self._values.get("use_ebs_optimized_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def volume_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLayer.VolumeConfigurationProperty]]]]:
        '''A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-volumeconfigurations
        '''
        result = self._values.get("volume_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLayer.VolumeConfigurationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLayerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStack(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opsworks.CfnStack",
):
    '''Creates a new stack. For more information, see `Create a New Stack <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-edit.html>`_ .

    *Required Permissions* : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information about user permissions, see `Managing User Permissions <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opsworks as opsworks
        
        # custom_json: Any
        
        cfn_stack = opsworks.CfnStack(self, "MyCfnStack",
            default_instance_profile_arn="defaultInstanceProfileArn",
            name="name",
            service_role_arn="serviceRoleArn",
        
            # the properties below are optional
            agent_version="agentVersion",
            attributes={
                "attributes_key": "attributes"
            },
            chef_configuration=opsworks.CfnStack.ChefConfigurationProperty(
                berkshelf_version="berkshelfVersion",
                manage_berkshelf=False
            ),
            clone_app_ids=["cloneAppIds"],
            clone_permissions=False,
            configuration_manager=opsworks.CfnStack.StackConfigurationManagerProperty(
                name="name",
                version="version"
            ),
            custom_cookbooks_source=opsworks.CfnStack.SourceProperty(
                password="password",
                revision="revision",
                ssh_key="sshKey",
                type="type",
                url="url",
                username="username"
            ),
            custom_json=custom_json,
            default_availability_zone="defaultAvailabilityZone",
            default_os="defaultOs",
            default_root_device_type="defaultRootDeviceType",
            default_ssh_key_name="defaultSshKeyName",
            default_subnet_id="defaultSubnetId",
            ecs_cluster_arn="ecsClusterArn",
            elastic_ips=[opsworks.CfnStack.ElasticIpProperty(
                ip="ip",
        
                # the properties below are optional
                name="name"
            )],
            hostname_theme="hostnameTheme",
            rds_db_instances=[opsworks.CfnStack.RdsDbInstanceProperty(
                db_password="dbPassword",
                db_user="dbUser",
                rds_db_instance_arn="rdsDbInstanceArn"
            )],
            source_stack_id="sourceStackId",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            use_custom_cookbooks=False,
            use_opsworks_security_groups=False,
            vpc_id="vpcId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        default_instance_profile_arn: builtins.str,
        name: builtins.str,
        service_role_arn: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        chef_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.ChefConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        clone_app_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        clone_permissions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        configuration_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.StackConfigurationManagerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_cookbooks_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.SourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_json: typing.Any = None,
        default_availability_zone: typing.Optional[builtins.str] = None,
        default_os: typing.Optional[builtins.str] = None,
        default_root_device_type: typing.Optional[builtins.str] = None,
        default_ssh_key_name: typing.Optional[builtins.str] = None,
        default_subnet_id: typing.Optional[builtins.str] = None,
        ecs_cluster_arn: typing.Optional[builtins.str] = None,
        elastic_ips: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.ElasticIpProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        hostname_theme: typing.Optional[builtins.str] = None,
        rds_db_instances: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStack.RdsDbInstanceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        source_stack_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param default_instance_profile_arn: The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .
        :param name: The stack name. Stack names can be a maximum of 64 characters.
        :param service_role_arn: The stack's IAM role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .
        :param agent_version: The default AWS OpsWorks Stacks agent version. You have the following options:. - Auto-update - Set this parameter to ``LATEST`` . AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available. - Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks installs that version on the stack's instances. The default setting is the most recent release of the agent. To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call `DescribeAgentVersions <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeAgentVersions>`_ . AgentVersion cannot be set to Chef 12.2. .. epigraph:: You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.
        :param attributes: One or more user-defined key-value pairs to be added to the stack attributes.
        :param chef_configuration: A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`_ .
        :param clone_app_ids: If you're cloning an AWS OpsWorks stack, a list of AWS OpsWorks application stack IDs from the source stack to include in the cloned stack.
        :param clone_permissions: If you're cloning an AWS OpsWorks stack, indicates whether to clone the source stack's permissions.
        :param configuration_manager: The configuration manager. When you create a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.
        :param custom_cookbooks_source: Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Adding Apps <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`_ or `Cookbooks and Recipes <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`_ .
        :param custom_json: A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format: ``"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"`` For more information about custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`_ .
        :param default_availability_zone: The stack's default Availability Zone, which must be in the specified region. For more information, see `Regions and Endpoints <https://docs.aws.amazon.com/general/latest/gr/rande.html>`_ . If you also specify a value for ``DefaultSubnetId`` , the subnet must be in the same zone. For more information, see the ``VpcId`` parameter description.
        :param default_os: The stack's default operating system, which is installed on every instance unless you specify a different operating system when you create the instance. You can specify one of the following. - A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2`` , ``Amazon Linux 2018.03`` , ``Amazon Linux 2017.09`` , ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . - A supported Ubuntu operating system, such as ``Ubuntu 18.04 LTS`` , ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . - ``CentOS Linux 7`` - ``Red Hat Enterprise Linux 7`` - A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . - A custom AMI: ``Custom`` . You specify the custom AMI you want to use when you create instances. For more information, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ . The default option is the current Amazon Linux version. Not all operating systems are supported with all versions of Chef. For more information about supported operating systems, see `AWS OpsWorks Stacks Operating Systems <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`_ .
        :param default_root_device_type: The default root device type. This value is the default for all instances in the stack, but you can override it when you create an instance. The default option is ``instance-store`` . For more information, see `Storage for the Root Device <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`_ .
        :param default_ssh_key_name: A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see `Using SSH to Communicate with an Instance <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html>`_ and `Managing SSH Access <https://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html>`_ . You can override this setting by specifying a different key pair, or no key pair, when you `create an instance <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`_ .
        :param default_subnet_id: The stack's default subnet ID. All instances are launched into this subnet unless you specify another subnet ID when you create the instance. This parameter is required if you specify a value for the ``VpcId`` parameter. If you also specify a value for ``DefaultAvailabilityZone`` , the subnet must be in that zone.
        :param ecs_cluster_arn: The Amazon Resource Name (ARN) of the Amazon Elastic Container Service ( Amazon ECS ) cluster to register with the AWS OpsWorks stack. .. epigraph:: If you specify a cluster that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the cluster.
        :param elastic_ips: A list of Elastic IP addresses to register with the AWS OpsWorks stack. .. epigraph:: If you specify an IP address that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the IP address.
        :param hostname_theme: The stack's host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack's instances. By default, ``HostnameTheme`` is set to ``Layer_Dependent`` , which creates host names by appending integers to the layer's short name. The other themes are: - ``Baked_Goods`` - ``Clouds`` - ``Europe_Cities`` - ``Fruits`` - ``Greek_Deities_and_Titans`` - ``Legendary_creatures_from_Japan`` - ``Planets_and_Moons`` - ``Roman_Deities`` - ``Scottish_Islands`` - ``US_Cities`` - ``Wild_Cats`` To obtain a generated host name, call ``GetHostNameSuggestion`` , which returns a host name based on the current theme.
        :param rds_db_instances: The Amazon Relational Database Service ( Amazon RDS ) database instance to register with the AWS OpsWorks stack. .. epigraph:: If you specify a database instance that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the database instance.
        :param source_stack_id: If you're cloning an AWS OpsWorks stack, the stack ID of the source AWS OpsWorks stack to clone.
        :param tags: A map that contains tag keys and tag values that are attached to a stack or layer. - The key cannot be empty. - The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : /`` - The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : /`` - Leading and trailing white spaces are trimmed from both the key and value. - A maximum of 40 tags is allowed for any resource.
        :param use_custom_cookbooks: Whether the stack uses custom cookbooks.
        :param use_opsworks_security_groups: Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack's layers. AWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With ``UseOpsworksSecurityGroups`` you can instead provide your own custom security groups. ``UseOpsworksSecurityGroups`` has the following settings: - True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group. - False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings. For more information, see `Create a New Stack <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`_ .
        :param vpc_id: The ID of the VPC that the stack is to be launched into. The VPC must be in the stack's region. All instances are launched into this VPC. You cannot change the ID later. - If your account supports EC2-Classic, the default value is ``no VPC`` . - If your account does not support EC2-Classic, the default value is the default VPC for the specified region. If the VPC ID corresponds to a default VPC and you have specified either the ``DefaultAvailabilityZone`` or the ``DefaultSubnetId`` parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively. If you specify a nondefault VPC ID, note the following: - It must belong to a VPC in your account that is in the specified region. - You must specify a value for ``DefaultSubnetId`` . For more information about how to use AWS OpsWorks Stacks with a VPC, see `Running a Stack in a VPC <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-vpc.html>`_ . For more information about default VPC and EC2-Classic, see `Supported Platforms <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bf36f6bd552e246cec8163081581d4887e2e1838c2af0dfdfec5a94265183ed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStackProps(
            default_instance_profile_arn=default_instance_profile_arn,
            name=name,
            service_role_arn=service_role_arn,
            agent_version=agent_version,
            attributes=attributes,
            chef_configuration=chef_configuration,
            clone_app_ids=clone_app_ids,
            clone_permissions=clone_permissions,
            configuration_manager=configuration_manager,
            custom_cookbooks_source=custom_cookbooks_source,
            custom_json=custom_json,
            default_availability_zone=default_availability_zone,
            default_os=default_os,
            default_root_device_type=default_root_device_type,
            default_ssh_key_name=default_ssh_key_name,
            default_subnet_id=default_subnet_id,
            ecs_cluster_arn=ecs_cluster_arn,
            elastic_ips=elastic_ips,
            hostname_theme=hostname_theme,
            rds_db_instances=rds_db_instances,
            source_stack_id=source_stack_id,
            tags=tags,
            use_custom_cookbooks=use_custom_cookbooks,
            use_opsworks_security_groups=use_opsworks_security_groups,
            vpc_id=vpc_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b361ad0a6f0d9dfac35a11da0b66f08aa9b0147967d3f53cd273d313b99dd78c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9d5d71f906760fc69e166fb118bdbe1cc995ea63682ce754be4ac9b1bcc282e)
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
    @jsii.member(jsii_name="defaultInstanceProfileArn")
    def default_instance_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances.'''
        return typing.cast(builtins.str, jsii.get(self, "defaultInstanceProfileArn"))

    @default_instance_profile_arn.setter
    def default_instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcd2146f03d53d0bae14a634773ac910108f90fe74c5850ae2cd62dcdba8ff91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultInstanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The stack name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f89b36dae98f2d94483d0e9b6f3ab58ba94d26da8024b7add02be1da0ab8971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        '''The stack's IAM role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__445f8be97bcc844a6174bad8312f2728cb0fc0c80b3485a6a065dc3dd7e8187c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="agentVersion")
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''The default AWS OpsWorks Stacks agent version.

        You have the following options:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentVersion"))

    @agent_version.setter
    def agent_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9be1597201772d629a8add01522e76bbc0e640244dde68fc6989d34c4615b757)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''One or more user-defined key-value pairs to be added to the stack attributes.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f53c27695b37fef5c31ad65f5466de830aad0d0e404b030255b9b656ad9b651)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="chefConfiguration")
    def chef_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.ChefConfigurationProperty"]]:
        '''A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`_ .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.ChefConfigurationProperty"]], jsii.get(self, "chefConfiguration"))

    @chef_configuration.setter
    def chef_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.ChefConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199cd836015029791dcb4c989b8ee7c17c9da5ef5f21511d039b62b20758d88b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "chefConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="cloneAppIds")
    def clone_app_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If you're cloning an AWS OpsWorks stack, a list of AWS OpsWorks application stack IDs from the source stack to include in the cloned stack.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cloneAppIds"))

    @clone_app_ids.setter
    def clone_app_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f94a28e6ee04321bfefa35125fa40665608f0b6f49bf1a9df27f9bb244c29a1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloneAppIds", value)

    @builtins.property
    @jsii.member(jsii_name="clonePermissions")
    def clone_permissions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you're cloning an AWS OpsWorks stack, indicates whether to clone the source stack's permissions.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "clonePermissions"))

    @clone_permissions.setter
    def clone_permissions(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39351cb814c7f03e34818b747d34f2049f3376b379272c0f23b6fa4a1729cf48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clonePermissions", value)

    @builtins.property
    @jsii.member(jsii_name="configurationManager")
    def configuration_manager(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.StackConfigurationManagerProperty"]]:
        '''The configuration manager.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.StackConfigurationManagerProperty"]], jsii.get(self, "configurationManager"))

    @configuration_manager.setter
    def configuration_manager(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.StackConfigurationManagerProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a10239804abfac0b9d5794c751a6f72e554b611f7631b0a15f7bae4472fc18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationManager", value)

    @builtins.property
    @jsii.member(jsii_name="customCookbooksSource")
    def custom_cookbooks_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.SourceProperty"]]:
        '''Contains the information required to retrieve an app or cookbook from a repository.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.SourceProperty"]], jsii.get(self, "customCookbooksSource"))

    @custom_cookbooks_source.setter
    def custom_cookbooks_source(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStack.SourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b869d48381b55b175cfbaba7ef0f8953ebdc1078d9d078e8bc09422eee78ec0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customCookbooksSource", value)

    @builtins.property
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> typing.Any:
        '''A string that contains user-defined, custom JSON.'''
        return typing.cast(typing.Any, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5afc13f67b5e304c063782f4f1baebe0e122de72c58ff0422ee442b028862b1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customJson", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAvailabilityZone")
    def default_availability_zone(self) -> typing.Optional[builtins.str]:
        '''The stack's default Availability Zone, which must be in the specified region.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAvailabilityZone"))

    @default_availability_zone.setter
    def default_availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0575d99ba2e198bd6047071bffef1370688626589013bdf50f10edad2930ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAvailabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="defaultOs")
    def default_os(self) -> typing.Optional[builtins.str]:
        '''The stack's default operating system, which is installed on every instance unless you specify a different operating system when you create the instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultOs"))

    @default_os.setter
    def default_os(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36eae94ac5dbe46e281ec3642d2992dcc3a11fd85e320a331c135b14abe1825e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultOs", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRootDeviceType")
    def default_root_device_type(self) -> typing.Optional[builtins.str]:
        '''The default root device type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRootDeviceType"))

    @default_root_device_type.setter
    def default_root_device_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75f346d6b179d1e5360e467ce27e42749aa4b2913d1009390c63dc13808f9282)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRootDeviceType", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSshKeyName")
    def default_ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''A default Amazon EC2 key pair name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSshKeyName"))

    @default_ssh_key_name.setter
    def default_ssh_key_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2de1c06c809948d02eeaef6ea6f660f45a9b01d1d97c7882090782849c6296e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSshKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSubnetId")
    def default_subnet_id(self) -> typing.Optional[builtins.str]:
        '''The stack's default subnet ID.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubnetId"))

    @default_subnet_id.setter
    def default_subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f623274426e3c785a5039bed9eae8a33b23dda8ed8becfae6480187e553118b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="ecsClusterArn")
    def ecs_cluster_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon Elastic Container Service ( Amazon ECS ) cluster to register with the AWS OpsWorks stack.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ecsClusterArn"))

    @ecs_cluster_arn.setter
    def ecs_cluster_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdd6f1f4f441686edc78cb49aa2b6a3ba64fa61be24b8b603ed59a555b80ccd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ecsClusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="elasticIps")
    def elastic_ips(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.ElasticIpProperty"]]]]:
        '''A list of Elastic IP addresses to register with the AWS OpsWorks stack.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.ElasticIpProperty"]]]], jsii.get(self, "elasticIps"))

    @elastic_ips.setter
    def elastic_ips(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.ElasticIpProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8166a03c0b2b271ef176beca6de587fdfbf1f5c676c8d7d58b600ce5bb52738b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticIps", value)

    @builtins.property
    @jsii.member(jsii_name="hostnameTheme")
    def hostname_theme(self) -> typing.Optional[builtins.str]:
        '''The stack's host name theme, with spaces replaced by underscores.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameTheme"))

    @hostname_theme.setter
    def hostname_theme(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0914ce2c4431a2766a2ec8f8ab3e2efd9e068fd797143dde5eae137cb581f725)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostnameTheme", value)

    @builtins.property
    @jsii.member(jsii_name="rdsDbInstances")
    def rds_db_instances(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.RdsDbInstanceProperty"]]]]:
        '''The Amazon Relational Database Service ( Amazon RDS ) database instance to register with the AWS OpsWorks stack.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.RdsDbInstanceProperty"]]]], jsii.get(self, "rdsDbInstances"))

    @rds_db_instances.setter
    def rds_db_instances(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStack.RdsDbInstanceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e5c5e4acdf62f9ce5d722219f3d8ea43ee54e485cbe2d141d73dcfd9b1b9b7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rdsDbInstances", value)

    @builtins.property
    @jsii.member(jsii_name="sourceStackId")
    def source_stack_id(self) -> typing.Optional[builtins.str]:
        '''If you're cloning an AWS OpsWorks stack, the stack ID of the source AWS OpsWorks stack to clone.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceStackId"))

    @source_stack_id.setter
    def source_stack_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d41d3731a853e0ecfcc8a979203fc2e807e9448c8d8cb112caa8c27b67e51c4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceStackId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a stack or layer.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b63dc4ecfd6df94a2c43b724328516c740a7518772217390f2712f6f5be41ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="useCustomCookbooks")
    def use_custom_cookbooks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the stack uses custom cookbooks.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "useCustomCookbooks"))

    @use_custom_cookbooks.setter
    def use_custom_cookbooks(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c8233bb88e60d83459f630fa2811d4e9bcbc58db4b583deecc08f372dc1753)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCustomCookbooks", value)

    @builtins.property
    @jsii.member(jsii_name="useOpsworksSecurityGroups")
    def use_opsworks_security_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack's layers.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "useOpsworksSecurityGroups"))

    @use_opsworks_security_groups.setter
    def use_opsworks_security_groups(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ac7bd4cfa5842431efd855ba2ad80900d00e084c7d85e9a5de10abac8159d5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useOpsworksSecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the VPC that the stack is to be launched into.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f99b9f1135a63819780a97a4e2a7c709c76a30d135fe4ca28a4f22083a5d73b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnStack.ChefConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "berkshelf_version": "berkshelfVersion",
            "manage_berkshelf": "manageBerkshelf",
        },
    )
    class ChefConfigurationProperty:
        def __init__(
            self,
            *,
            berkshelf_version: typing.Optional[builtins.str] = None,
            manage_berkshelf: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the Chef configuration.

            :param berkshelf_version: The Berkshelf version.
            :param manage_berkshelf: Whether to enable Berkshelf.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                chef_configuration_property = opsworks.CfnStack.ChefConfigurationProperty(
                    berkshelf_version="berkshelfVersion",
                    manage_berkshelf=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__abf9ebc10290309cd8a1b70ca75f5db34b7f4ad850a7c01823703880a958847d)
                check_type(argname="argument berkshelf_version", value=berkshelf_version, expected_type=type_hints["berkshelf_version"])
                check_type(argname="argument manage_berkshelf", value=manage_berkshelf, expected_type=type_hints["manage_berkshelf"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if berkshelf_version is not None:
                self._values["berkshelf_version"] = berkshelf_version
            if manage_berkshelf is not None:
                self._values["manage_berkshelf"] = manage_berkshelf

        @builtins.property
        def berkshelf_version(self) -> typing.Optional[builtins.str]:
            '''The Berkshelf version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-stack-chefconfiguration-berkshelfversion
            '''
            result = self._values.get("berkshelf_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manage_berkshelf(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to enable Berkshelf.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-stack-chefconfiguration-manageberkshelf
            '''
            result = self._values.get("manage_berkshelf")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChefConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnStack.ElasticIpProperty",
        jsii_struct_bases=[],
        name_mapping={"ip": "ip", "name": "name"},
    )
    class ElasticIpProperty:
        def __init__(
            self,
            *,
            ip: builtins.str,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an Elastic IP address.

            :param ip: The IP address.
            :param name: The name, which can be a maximum of 32 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                elastic_ip_property = opsworks.CfnStack.ElasticIpProperty(
                    ip="ip",
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a7ee561457c88f487ec83cc46992533784aed634d52bb7bb125bff6ac7f70a96)
                check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ip": ip,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def ip(self) -> builtins.str:
            '''The IP address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-ip
            '''
            result = self._values.get("ip")
            assert result is not None, "Required property 'ip' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name, which can be a maximum of 32 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticIpProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnStack.RdsDbInstanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "db_password": "dbPassword",
            "db_user": "dbUser",
            "rds_db_instance_arn": "rdsDbInstanceArn",
        },
    )
    class RdsDbInstanceProperty:
        def __init__(
            self,
            *,
            db_password: builtins.str,
            db_user: builtins.str,
            rds_db_instance_arn: builtins.str,
        ) -> None:
            '''Describes an Amazon RDS instance.

            :param db_password: AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.
            :param db_user: The master user name.
            :param rds_db_instance_arn: The instance's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                rds_db_instance_property = opsworks.CfnStack.RdsDbInstanceProperty(
                    db_password="dbPassword",
                    db_user="dbUser",
                    rds_db_instance_arn="rdsDbInstanceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b82360194600f18115acf75a0aa1bad6e17cc7b3258cc43567008e3cedbf5d0)
                check_type(argname="argument db_password", value=db_password, expected_type=type_hints["db_password"])
                check_type(argname="argument db_user", value=db_user, expected_type=type_hints["db_user"])
                check_type(argname="argument rds_db_instance_arn", value=rds_db_instance_arn, expected_type=type_hints["rds_db_instance_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "db_password": db_password,
                "db_user": db_user,
                "rds_db_instance_arn": rds_db_instance_arn,
            }

        @builtins.property
        def db_password(self) -> builtins.str:
            '''AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbpassword
            '''
            result = self._values.get("db_password")
            assert result is not None, "Required property 'db_password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def db_user(self) -> builtins.str:
            '''The master user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbuser
            '''
            result = self._values.get("db_user")
            assert result is not None, "Required property 'db_user' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rds_db_instance_arn(self) -> builtins.str:
            '''The instance's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-rdsdbinstancearn
            '''
            result = self._values.get("rds_db_instance_arn")
            assert result is not None, "Required property 'rds_db_instance_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RdsDbInstanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnStack.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "revision": "revision",
            "ssh_key": "sshKey",
            "type": "type",
            "url": "url",
            "username": "username",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            password: typing.Optional[builtins.str] = None,
            revision: typing.Optional[builtins.str] = None,
            ssh_key: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains the information required to retrieve an app or cookbook from a repository.

            For more information, see `Creating Apps <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`_ or `Custom Recipes and Cookbooks <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`_ .

            :param password: When included in a request, the parameter depends on the repository type. - For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. - For HTTP bundles and Subversion repositories, set ``Password`` to the password. For more information on how to safely handle IAM credentials, see ` <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`_ . In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.
            :param revision: The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
            :param ssh_key: The repository's SSH key. For more information, see `Using Git Repository SSH Keys <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-deploykeys.html>`_ in the *AWS OpsWorks User Guide* . To pass in an SSH key as a parameter, see the following example: ``"Parameters" : { "GitSSHKey" : { "Description" : "Change SSH key newlines to commas.", "Type" : "CommaDelimitedList", "NoEcho" : "true" }, ... "CustomCookbooksSource": { "Revision" : { "Ref": "GitRevision"}, "SshKey" : { "Fn::Join" : [ "\\n", { "Ref": "GitSSHKey"} ] }, "Type": "git", "Url": { "Ref": "GitURL"} } ...``
            :param type: The repository type.
            :param url: The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .
            :param username: This parameter depends on the repository type. - For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. - For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                source_property = opsworks.CfnStack.SourceProperty(
                    password="password",
                    revision="revision",
                    ssh_key="sshKey",
                    type="type",
                    url="url",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7fd7288c88143256aba1740990a9ddf652b90605d6d9df2b675539cf3f658474)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
                check_type(argname="argument ssh_key", value=ssh_key, expected_type=type_hints["ssh_key"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if password is not None:
                self._values["password"] = password
            if revision is not None:
                self._values["revision"] = revision
            if ssh_key is not None:
                self._values["ssh_key"] = ssh_key
            if type is not None:
                self._values["type"] = type
            if url is not None:
                self._values["url"] = url
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''When included in a request, the parameter depends on the repository type.

            - For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.
            - For HTTP bundles and Subversion repositories, set ``Password`` to the password.

            For more information on how to safely handle IAM credentials, see ` <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`_ .

            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-stack-source-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def revision(self) -> typing.Optional[builtins.str]:
            '''The application's version.

            AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-stack-source-revision
            '''
            result = self._values.get("revision")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssh_key(self) -> typing.Optional[builtins.str]:
            '''The repository's SSH key.

            For more information, see `Using Git Repository SSH Keys <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-deploykeys.html>`_ in the *AWS OpsWorks User Guide* . To pass in an SSH key as a parameter, see the following example:

            ``"Parameters" : { "GitSSHKey" : { "Description" : "Change SSH key newlines to commas.", "Type" : "CommaDelimitedList", "NoEcho" : "true" }, ... "CustomCookbooksSource": { "Revision" : { "Ref": "GitRevision"}, "SshKey" : { "Fn::Join" : [ "\\n", { "Ref": "GitSSHKey"} ] }, "Type": "git", "Url": { "Ref": "GitURL"} } ...``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-stack-source-sshkey
            '''
            result = self._values.get("ssh_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The repository type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-stack-source-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The source URL.

            The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-stack-source-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''This parameter depends on the repository type.

            - For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.
            - For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-stack-source-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworks.CfnStack.StackConfigurationManagerProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class StackConfigurationManagerProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration manager.

            :param name: The name. This parameter must be set to ``Chef`` .
            :param version: The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 12.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigurationmanager.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworks as opsworks
                
                stack_configuration_manager_property = opsworks.CfnStack.StackConfigurationManagerProperty(
                    name="name",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c21d7fcd41f5c5f2c62e0d7b9877b307d95ccdeece063c91c4db1d441a16ac6)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name.

            This parameter must be set to ``Chef`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigurationmanager.html#cfn-opsworks-stack-stackconfigurationmanager-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The Chef version.

            This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 12.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigurationmanager.html#cfn-opsworks-stack-stackconfigurationmanager-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StackConfigurationManagerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opsworks.CfnStackProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_instance_profile_arn": "defaultInstanceProfileArn",
        "name": "name",
        "service_role_arn": "serviceRoleArn",
        "agent_version": "agentVersion",
        "attributes": "attributes",
        "chef_configuration": "chefConfiguration",
        "clone_app_ids": "cloneAppIds",
        "clone_permissions": "clonePermissions",
        "configuration_manager": "configurationManager",
        "custom_cookbooks_source": "customCookbooksSource",
        "custom_json": "customJson",
        "default_availability_zone": "defaultAvailabilityZone",
        "default_os": "defaultOs",
        "default_root_device_type": "defaultRootDeviceType",
        "default_ssh_key_name": "defaultSshKeyName",
        "default_subnet_id": "defaultSubnetId",
        "ecs_cluster_arn": "ecsClusterArn",
        "elastic_ips": "elasticIps",
        "hostname_theme": "hostnameTheme",
        "rds_db_instances": "rdsDbInstances",
        "source_stack_id": "sourceStackId",
        "tags": "tags",
        "use_custom_cookbooks": "useCustomCookbooks",
        "use_opsworks_security_groups": "useOpsworksSecurityGroups",
        "vpc_id": "vpcId",
    },
)
class CfnStackProps:
    def __init__(
        self,
        *,
        default_instance_profile_arn: builtins.str,
        name: builtins.str,
        service_role_arn: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        chef_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ChefConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        clone_app_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        clone_permissions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        configuration_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StackConfigurationManagerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_cookbooks_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_json: typing.Any = None,
        default_availability_zone: typing.Optional[builtins.str] = None,
        default_os: typing.Optional[builtins.str] = None,
        default_root_device_type: typing.Optional[builtins.str] = None,
        default_ssh_key_name: typing.Optional[builtins.str] = None,
        default_subnet_id: typing.Optional[builtins.str] = None,
        ecs_cluster_arn: typing.Optional[builtins.str] = None,
        elastic_ips: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ElasticIpProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        hostname_theme: typing.Optional[builtins.str] = None,
        rds_db_instances: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.RdsDbInstanceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        source_stack_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnStack``.

        :param default_instance_profile_arn: The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .
        :param name: The stack name. Stack names can be a maximum of 64 characters.
        :param service_role_arn: The stack's IAM role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .
        :param agent_version: The default AWS OpsWorks Stacks agent version. You have the following options:. - Auto-update - Set this parameter to ``LATEST`` . AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available. - Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks installs that version on the stack's instances. The default setting is the most recent release of the agent. To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call `DescribeAgentVersions <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeAgentVersions>`_ . AgentVersion cannot be set to Chef 12.2. .. epigraph:: You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.
        :param attributes: One or more user-defined key-value pairs to be added to the stack attributes.
        :param chef_configuration: A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`_ .
        :param clone_app_ids: If you're cloning an AWS OpsWorks stack, a list of AWS OpsWorks application stack IDs from the source stack to include in the cloned stack.
        :param clone_permissions: If you're cloning an AWS OpsWorks stack, indicates whether to clone the source stack's permissions.
        :param configuration_manager: The configuration manager. When you create a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.
        :param custom_cookbooks_source: Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Adding Apps <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`_ or `Cookbooks and Recipes <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`_ .
        :param custom_json: A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format: ``"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"`` For more information about custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`_ .
        :param default_availability_zone: The stack's default Availability Zone, which must be in the specified region. For more information, see `Regions and Endpoints <https://docs.aws.amazon.com/general/latest/gr/rande.html>`_ . If you also specify a value for ``DefaultSubnetId`` , the subnet must be in the same zone. For more information, see the ``VpcId`` parameter description.
        :param default_os: The stack's default operating system, which is installed on every instance unless you specify a different operating system when you create the instance. You can specify one of the following. - A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2`` , ``Amazon Linux 2018.03`` , ``Amazon Linux 2017.09`` , ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . - A supported Ubuntu operating system, such as ``Ubuntu 18.04 LTS`` , ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . - ``CentOS Linux 7`` - ``Red Hat Enterprise Linux 7`` - A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . - A custom AMI: ``Custom`` . You specify the custom AMI you want to use when you create instances. For more information, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ . The default option is the current Amazon Linux version. Not all operating systems are supported with all versions of Chef. For more information about supported operating systems, see `AWS OpsWorks Stacks Operating Systems <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`_ .
        :param default_root_device_type: The default root device type. This value is the default for all instances in the stack, but you can override it when you create an instance. The default option is ``instance-store`` . For more information, see `Storage for the Root Device <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`_ .
        :param default_ssh_key_name: A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see `Using SSH to Communicate with an Instance <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html>`_ and `Managing SSH Access <https://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html>`_ . You can override this setting by specifying a different key pair, or no key pair, when you `create an instance <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`_ .
        :param default_subnet_id: The stack's default subnet ID. All instances are launched into this subnet unless you specify another subnet ID when you create the instance. This parameter is required if you specify a value for the ``VpcId`` parameter. If you also specify a value for ``DefaultAvailabilityZone`` , the subnet must be in that zone.
        :param ecs_cluster_arn: The Amazon Resource Name (ARN) of the Amazon Elastic Container Service ( Amazon ECS ) cluster to register with the AWS OpsWorks stack. .. epigraph:: If you specify a cluster that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the cluster.
        :param elastic_ips: A list of Elastic IP addresses to register with the AWS OpsWorks stack. .. epigraph:: If you specify an IP address that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the IP address.
        :param hostname_theme: The stack's host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack's instances. By default, ``HostnameTheme`` is set to ``Layer_Dependent`` , which creates host names by appending integers to the layer's short name. The other themes are: - ``Baked_Goods`` - ``Clouds`` - ``Europe_Cities`` - ``Fruits`` - ``Greek_Deities_and_Titans`` - ``Legendary_creatures_from_Japan`` - ``Planets_and_Moons`` - ``Roman_Deities`` - ``Scottish_Islands`` - ``US_Cities`` - ``Wild_Cats`` To obtain a generated host name, call ``GetHostNameSuggestion`` , which returns a host name based on the current theme.
        :param rds_db_instances: The Amazon Relational Database Service ( Amazon RDS ) database instance to register with the AWS OpsWorks stack. .. epigraph:: If you specify a database instance that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the database instance.
        :param source_stack_id: If you're cloning an AWS OpsWorks stack, the stack ID of the source AWS OpsWorks stack to clone.
        :param tags: A map that contains tag keys and tag values that are attached to a stack or layer. - The key cannot be empty. - The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : /`` - The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : /`` - Leading and trailing white spaces are trimmed from both the key and value. - A maximum of 40 tags is allowed for any resource.
        :param use_custom_cookbooks: Whether the stack uses custom cookbooks.
        :param use_opsworks_security_groups: Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack's layers. AWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With ``UseOpsworksSecurityGroups`` you can instead provide your own custom security groups. ``UseOpsworksSecurityGroups`` has the following settings: - True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group. - False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings. For more information, see `Create a New Stack <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`_ .
        :param vpc_id: The ID of the VPC that the stack is to be launched into. The VPC must be in the stack's region. All instances are launched into this VPC. You cannot change the ID later. - If your account supports EC2-Classic, the default value is ``no VPC`` . - If your account does not support EC2-Classic, the default value is the default VPC for the specified region. If the VPC ID corresponds to a default VPC and you have specified either the ``DefaultAvailabilityZone`` or the ``DefaultSubnetId`` parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively. If you specify a nondefault VPC ID, note the following: - It must belong to a VPC in your account that is in the specified region. - You must specify a value for ``DefaultSubnetId`` . For more information about how to use AWS OpsWorks Stacks with a VPC, see `Running a Stack in a VPC <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-vpc.html>`_ . For more information about default VPC and EC2-Classic, see `Supported Platforms <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opsworks as opsworks
            
            # custom_json: Any
            
            cfn_stack_props = opsworks.CfnStackProps(
                default_instance_profile_arn="defaultInstanceProfileArn",
                name="name",
                service_role_arn="serviceRoleArn",
            
                # the properties below are optional
                agent_version="agentVersion",
                attributes={
                    "attributes_key": "attributes"
                },
                chef_configuration=opsworks.CfnStack.ChefConfigurationProperty(
                    berkshelf_version="berkshelfVersion",
                    manage_berkshelf=False
                ),
                clone_app_ids=["cloneAppIds"],
                clone_permissions=False,
                configuration_manager=opsworks.CfnStack.StackConfigurationManagerProperty(
                    name="name",
                    version="version"
                ),
                custom_cookbooks_source=opsworks.CfnStack.SourceProperty(
                    password="password",
                    revision="revision",
                    ssh_key="sshKey",
                    type="type",
                    url="url",
                    username="username"
                ),
                custom_json=custom_json,
                default_availability_zone="defaultAvailabilityZone",
                default_os="defaultOs",
                default_root_device_type="defaultRootDeviceType",
                default_ssh_key_name="defaultSshKeyName",
                default_subnet_id="defaultSubnetId",
                ecs_cluster_arn="ecsClusterArn",
                elastic_ips=[opsworks.CfnStack.ElasticIpProperty(
                    ip="ip",
            
                    # the properties below are optional
                    name="name"
                )],
                hostname_theme="hostnameTheme",
                rds_db_instances=[opsworks.CfnStack.RdsDbInstanceProperty(
                    db_password="dbPassword",
                    db_user="dbUser",
                    rds_db_instance_arn="rdsDbInstanceArn"
                )],
                source_stack_id="sourceStackId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                use_custom_cookbooks=False,
                use_opsworks_security_groups=False,
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__675a36919e38f296f3b53b7679384ec86298336f087126cb5bee9e1e22a8445c)
            check_type(argname="argument default_instance_profile_arn", value=default_instance_profile_arn, expected_type=type_hints["default_instance_profile_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument agent_version", value=agent_version, expected_type=type_hints["agent_version"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument chef_configuration", value=chef_configuration, expected_type=type_hints["chef_configuration"])
            check_type(argname="argument clone_app_ids", value=clone_app_ids, expected_type=type_hints["clone_app_ids"])
            check_type(argname="argument clone_permissions", value=clone_permissions, expected_type=type_hints["clone_permissions"])
            check_type(argname="argument configuration_manager", value=configuration_manager, expected_type=type_hints["configuration_manager"])
            check_type(argname="argument custom_cookbooks_source", value=custom_cookbooks_source, expected_type=type_hints["custom_cookbooks_source"])
            check_type(argname="argument custom_json", value=custom_json, expected_type=type_hints["custom_json"])
            check_type(argname="argument default_availability_zone", value=default_availability_zone, expected_type=type_hints["default_availability_zone"])
            check_type(argname="argument default_os", value=default_os, expected_type=type_hints["default_os"])
            check_type(argname="argument default_root_device_type", value=default_root_device_type, expected_type=type_hints["default_root_device_type"])
            check_type(argname="argument default_ssh_key_name", value=default_ssh_key_name, expected_type=type_hints["default_ssh_key_name"])
            check_type(argname="argument default_subnet_id", value=default_subnet_id, expected_type=type_hints["default_subnet_id"])
            check_type(argname="argument ecs_cluster_arn", value=ecs_cluster_arn, expected_type=type_hints["ecs_cluster_arn"])
            check_type(argname="argument elastic_ips", value=elastic_ips, expected_type=type_hints["elastic_ips"])
            check_type(argname="argument hostname_theme", value=hostname_theme, expected_type=type_hints["hostname_theme"])
            check_type(argname="argument rds_db_instances", value=rds_db_instances, expected_type=type_hints["rds_db_instances"])
            check_type(argname="argument source_stack_id", value=source_stack_id, expected_type=type_hints["source_stack_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument use_custom_cookbooks", value=use_custom_cookbooks, expected_type=type_hints["use_custom_cookbooks"])
            check_type(argname="argument use_opsworks_security_groups", value=use_opsworks_security_groups, expected_type=type_hints["use_opsworks_security_groups"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_instance_profile_arn": default_instance_profile_arn,
            "name": name,
            "service_role_arn": service_role_arn,
        }
        if agent_version is not None:
            self._values["agent_version"] = agent_version
        if attributes is not None:
            self._values["attributes"] = attributes
        if chef_configuration is not None:
            self._values["chef_configuration"] = chef_configuration
        if clone_app_ids is not None:
            self._values["clone_app_ids"] = clone_app_ids
        if clone_permissions is not None:
            self._values["clone_permissions"] = clone_permissions
        if configuration_manager is not None:
            self._values["configuration_manager"] = configuration_manager
        if custom_cookbooks_source is not None:
            self._values["custom_cookbooks_source"] = custom_cookbooks_source
        if custom_json is not None:
            self._values["custom_json"] = custom_json
        if default_availability_zone is not None:
            self._values["default_availability_zone"] = default_availability_zone
        if default_os is not None:
            self._values["default_os"] = default_os
        if default_root_device_type is not None:
            self._values["default_root_device_type"] = default_root_device_type
        if default_ssh_key_name is not None:
            self._values["default_ssh_key_name"] = default_ssh_key_name
        if default_subnet_id is not None:
            self._values["default_subnet_id"] = default_subnet_id
        if ecs_cluster_arn is not None:
            self._values["ecs_cluster_arn"] = ecs_cluster_arn
        if elastic_ips is not None:
            self._values["elastic_ips"] = elastic_ips
        if hostname_theme is not None:
            self._values["hostname_theme"] = hostname_theme
        if rds_db_instances is not None:
            self._values["rds_db_instances"] = rds_db_instances
        if source_stack_id is not None:
            self._values["source_stack_id"] = source_stack_id
        if tags is not None:
            self._values["tags"] = tags
        if use_custom_cookbooks is not None:
            self._values["use_custom_cookbooks"] = use_custom_cookbooks
        if use_opsworks_security_groups is not None:
            self._values["use_opsworks_security_groups"] = use_opsworks_security_groups
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def default_instance_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances.

        For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultinstanceprofilearn
        '''
        result = self._values.get("default_instance_profile_arn")
        assert result is not None, "Required property 'default_instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The stack name.

        Stack names can be a maximum of 64 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role_arn(self) -> builtins.str:
        '''The stack's IAM role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf.

        You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. For more information about IAM ARNs, see `Using Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        assert result is not None, "Required property 'service_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''The default AWS OpsWorks Stacks agent version. You have the following options:.

        - Auto-update - Set this parameter to ``LATEST`` . AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available.
        - Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks installs that version on the stack's instances.

        The default setting is the most recent release of the agent. To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call `DescribeAgentVersions <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeAgentVersions>`_ . AgentVersion cannot be set to Chef 12.2.
        .. epigraph::

           You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-agentversion
        '''
        result = self._values.get("agent_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''One or more user-defined key-value pairs to be added to the stack attributes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

    @builtins.property
    def chef_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.ChefConfigurationProperty]]:
        '''A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-chefconfiguration
        '''
        result = self._values.get("chef_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.ChefConfigurationProperty]], result)

    @builtins.property
    def clone_app_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If you're cloning an AWS OpsWorks stack, a list of AWS OpsWorks application stack IDs from the source stack to include in the cloned stack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-cloneappids
        '''
        result = self._values.get("clone_app_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def clone_permissions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you're cloning an AWS OpsWorks stack, indicates whether to clone the source stack's permissions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-clonepermissions
        '''
        result = self._values.get("clone_permissions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def configuration_manager(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.StackConfigurationManagerProperty]]:
        '''The configuration manager.

        When you create a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-configurationmanager
        '''
        result = self._values.get("configuration_manager")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.StackConfigurationManagerProperty]], result)

    @builtins.property
    def custom_cookbooks_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.SourceProperty]]:
        '''Contains the information required to retrieve an app or cookbook from a repository.

        For more information, see `Adding Apps <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`_ or `Cookbooks and Recipes <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-customcookbookssource
        '''
        result = self._values.get("custom_cookbooks_source")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.SourceProperty]], result)

    @builtins.property
    def custom_json(self) -> typing.Any:
        '''A string that contains user-defined, custom JSON.

        It can be used to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:

        ``"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"``

        For more information about custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-customjson
        '''
        result = self._values.get("custom_json")
        return typing.cast(typing.Any, result)

    @builtins.property
    def default_availability_zone(self) -> typing.Optional[builtins.str]:
        '''The stack's default Availability Zone, which must be in the specified region.

        For more information, see `Regions and Endpoints <https://docs.aws.amazon.com/general/latest/gr/rande.html>`_ . If you also specify a value for ``DefaultSubnetId`` , the subnet must be in the same zone. For more information, see the ``VpcId`` parameter description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultavailabilityzone
        '''
        result = self._values.get("default_availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_os(self) -> typing.Optional[builtins.str]:
        '''The stack's default operating system, which is installed on every instance unless you specify a different operating system when you create the instance.

        You can specify one of the following.

        - A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2`` , ``Amazon Linux 2018.03`` , ``Amazon Linux 2017.09`` , ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` .
        - A supported Ubuntu operating system, such as ``Ubuntu 18.04 LTS`` , ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` .
        - ``CentOS Linux 7``
        - ``Red Hat Enterprise Linux 7``
        - A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` .
        - A custom AMI: ``Custom`` . You specify the custom AMI you want to use when you create instances. For more information, see `Using Custom AMIs <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`_ .

        The default option is the current Amazon Linux version. Not all operating systems are supported with all versions of Chef. For more information about supported operating systems, see `AWS OpsWorks Stacks Operating Systems <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultos
        '''
        result = self._values.get("default_os")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_root_device_type(self) -> typing.Optional[builtins.str]:
        '''The default root device type.

        This value is the default for all instances in the stack, but you can override it when you create an instance. The default option is ``instance-store`` . For more information, see `Storage for the Root Device <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultrootdevicetype
        '''
        result = self._values.get("default_root_device_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''A default Amazon EC2 key pair name.

        The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see `Using SSH to Communicate with an Instance <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html>`_ and `Managing SSH Access <https://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html>`_ . You can override this setting by specifying a different key pair, or no key pair, when you `create an instance <https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultsshkeyname
        '''
        result = self._values.get("default_ssh_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_subnet_id(self) -> typing.Optional[builtins.str]:
        '''The stack's default subnet ID.

        All instances are launched into this subnet unless you specify another subnet ID when you create the instance. This parameter is required if you specify a value for the ``VpcId`` parameter. If you also specify a value for ``DefaultAvailabilityZone`` , the subnet must be in that zone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultsubnetid
        '''
        result = self._values.get("default_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ecs_cluster_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon Elastic Container Service ( Amazon ECS ) cluster to register with the AWS OpsWorks stack.

        .. epigraph::

           If you specify a cluster that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-ecsclusterarn
        '''
        result = self._values.get("ecs_cluster_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elastic_ips(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.ElasticIpProperty]]]]:
        '''A list of Elastic IP addresses to register with the AWS OpsWorks stack.

        .. epigraph::

           If you specify an IP address that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the IP address.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-elasticips
        '''
        result = self._values.get("elastic_ips")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.ElasticIpProperty]]]], result)

    @builtins.property
    def hostname_theme(self) -> typing.Optional[builtins.str]:
        '''The stack's host name theme, with spaces replaced by underscores.

        The theme is used to generate host names for the stack's instances. By default, ``HostnameTheme`` is set to ``Layer_Dependent`` , which creates host names by appending integers to the layer's short name. The other themes are:

        - ``Baked_Goods``
        - ``Clouds``
        - ``Europe_Cities``
        - ``Fruits``
        - ``Greek_Deities_and_Titans``
        - ``Legendary_creatures_from_Japan``
        - ``Planets_and_Moons``
        - ``Roman_Deities``
        - ``Scottish_Islands``
        - ``US_Cities``
        - ``Wild_Cats``

        To obtain a generated host name, call ``GetHostNameSuggestion`` , which returns a host name based on the current theme.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-hostnametheme
        '''
        result = self._values.get("hostname_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rds_db_instances(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.RdsDbInstanceProperty]]]]:
        '''The Amazon Relational Database Service ( Amazon RDS ) database instance to register with the AWS OpsWorks stack.

        .. epigraph::

           If you specify a database instance that's registered with another AWS OpsWorks stack, AWS CloudFormation deregisters the existing association before registering the database instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-rdsdbinstances
        '''
        result = self._values.get("rds_db_instances")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.RdsDbInstanceProperty]]]], result)

    @builtins.property
    def source_stack_id(self) -> typing.Optional[builtins.str]:
        '''If you're cloning an AWS OpsWorks stack, the stack ID of the source AWS OpsWorks stack to clone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-sourcestackid
        '''
        result = self._values.get("source_stack_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a stack or layer.

        - The key cannot be empty.
        - The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : /``
        - The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : /``
        - Leading and trailing white spaces are trimmed from both the key and value.
        - A maximum of 40 tags is allowed for any resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def use_custom_cookbooks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the stack uses custom cookbooks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-usecustomcookbooks
        '''
        result = self._values.get("use_custom_cookbooks")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def use_opsworks_security_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack's layers.

        AWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With ``UseOpsworksSecurityGroups`` you can instead provide your own custom security groups. ``UseOpsworksSecurityGroups`` has the following settings:

        - True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group.
        - False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings.

        For more information, see `Create a New Stack <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-useopsworkssecuritygroups
        '''
        result = self._values.get("use_opsworks_security_groups")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the VPC that the stack is to be launched into.

        The VPC must be in the stack's region. All instances are launched into this VPC. You cannot change the ID later.

        - If your account supports EC2-Classic, the default value is ``no VPC`` .
        - If your account does not support EC2-Classic, the default value is the default VPC for the specified region.

        If the VPC ID corresponds to a default VPC and you have specified either the ``DefaultAvailabilityZone`` or the ``DefaultSubnetId`` parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively.

        If you specify a nondefault VPC ID, note the following:

        - It must belong to a VPC in your account that is in the specified region.
        - You must specify a value for ``DefaultSubnetId`` .

        For more information about how to use AWS OpsWorks Stacks with a VPC, see `Running a Stack in a VPC <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-vpc.html>`_ . For more information about default VPC and EC2-Classic, see `Supported Platforms <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-vpcid
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnUserProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opsworks.CfnUserProfile",
):
    '''Describes a user's SSH information.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opsworks as opsworks
        
        cfn_user_profile = opsworks.CfnUserProfile(self, "MyCfnUserProfile",
            iam_user_arn="iamUserArn",
        
            # the properties below are optional
            allow_self_management=False,
            ssh_public_key="sshPublicKey",
            ssh_username="sshUsername"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        iam_user_arn: builtins.str,
        allow_self_management: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ssh_public_key: typing.Optional[builtins.str] = None,
        ssh_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param iam_user_arn: The user's IAM ARN.
        :param allow_self_management: Whether users can specify their own SSH public key through the My Settings page. For more information, see `Managing User Permissions <https://docs.aws.amazon.com/opsworks/latest/userguide/security-settingsshkey.html>`_ .
        :param ssh_public_key: The user's SSH public key.
        :param ssh_username: The user's SSH user name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f841ed2cddcf6c81296cc894f86e940d11eef568430b95d1b3254394ce0adb34)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProfileProps(
            iam_user_arn=iam_user_arn,
            allow_self_management=allow_self_management,
            ssh_public_key=ssh_public_key,
            ssh_username=ssh_username,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2299d976cf9af9d070893ec6b7430487983701fdf2b290750bf77ed59a1cd17)
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
            type_hints = typing.get_type_hints(_typecheckingstub__55f5b517b73ce52986d98356734c969824ecf1d0952831a487957921991673da)
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
    @jsii.member(jsii_name="attrSshUsername")
    def attr_ssh_username(self) -> builtins.str:
        '''The user's SSH user name, as a string.

        :cloudformationAttribute: SshUsername
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSshUsername"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="iamUserArn")
    def iam_user_arn(self) -> builtins.str:
        '''The user's IAM ARN.'''
        return typing.cast(builtins.str, jsii.get(self, "iamUserArn"))

    @iam_user_arn.setter
    def iam_user_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3690d5d3f6d99859dfc161334057968dd09b0d5b9ae89605055c2fe2774cfe47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamUserArn", value)

    @builtins.property
    @jsii.member(jsii_name="allowSelfManagement")
    def allow_self_management(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether users can specify their own SSH public key through the My Settings page.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "allowSelfManagement"))

    @allow_self_management.setter
    def allow_self_management(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__128de556beee0c143ac666faced9d32f126718068e45c973130b0b1e5f8ad3e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowSelfManagement", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> typing.Optional[builtins.str]:
        '''The user's SSH public key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d0e5e7d2b5344bfdfd2e358e2f6fd6be76f752928ccf7bff0f2740fc233eac9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="sshUsername")
    def ssh_username(self) -> typing.Optional[builtins.str]:
        '''The user's SSH user name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshUsername"))

    @ssh_username.setter
    def ssh_username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8836ddb30644943ce6efae3bc2a36b644b5c82b5a34b9b1b4ea35bf9849e2e85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshUsername", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opsworks.CfnUserProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "iam_user_arn": "iamUserArn",
        "allow_self_management": "allowSelfManagement",
        "ssh_public_key": "sshPublicKey",
        "ssh_username": "sshUsername",
    },
)
class CfnUserProfileProps:
    def __init__(
        self,
        *,
        iam_user_arn: builtins.str,
        allow_self_management: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ssh_public_key: typing.Optional[builtins.str] = None,
        ssh_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnUserProfile``.

        :param iam_user_arn: The user's IAM ARN.
        :param allow_self_management: Whether users can specify their own SSH public key through the My Settings page. For more information, see `Managing User Permissions <https://docs.aws.amazon.com/opsworks/latest/userguide/security-settingsshkey.html>`_ .
        :param ssh_public_key: The user's SSH public key.
        :param ssh_username: The user's SSH user name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opsworks as opsworks
            
            cfn_user_profile_props = opsworks.CfnUserProfileProps(
                iam_user_arn="iamUserArn",
            
                # the properties below are optional
                allow_self_management=False,
                ssh_public_key="sshPublicKey",
                ssh_username="sshUsername"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c4119cda15b50587c240dbd706f63701c8bc940cdb11ef0e8c6fa341479ff30)
            check_type(argname="argument iam_user_arn", value=iam_user_arn, expected_type=type_hints["iam_user_arn"])
            check_type(argname="argument allow_self_management", value=allow_self_management, expected_type=type_hints["allow_self_management"])
            check_type(argname="argument ssh_public_key", value=ssh_public_key, expected_type=type_hints["ssh_public_key"])
            check_type(argname="argument ssh_username", value=ssh_username, expected_type=type_hints["ssh_username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iam_user_arn": iam_user_arn,
        }
        if allow_self_management is not None:
            self._values["allow_self_management"] = allow_self_management
        if ssh_public_key is not None:
            self._values["ssh_public_key"] = ssh_public_key
        if ssh_username is not None:
            self._values["ssh_username"] = ssh_username

    @builtins.property
    def iam_user_arn(self) -> builtins.str:
        '''The user's IAM ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-iamuserarn
        '''
        result = self._values.get("iam_user_arn")
        assert result is not None, "Required property 'iam_user_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_self_management(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether users can specify their own SSH public key through the My Settings page.

        For more information, see `Managing User Permissions <https://docs.aws.amazon.com/opsworks/latest/userguide/security-settingsshkey.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-allowselfmanagement
        '''
        result = self._values.get("allow_self_management")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def ssh_public_key(self) -> typing.Optional[builtins.str]:
        '''The user's SSH public key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshpublickey
        '''
        result = self._values.get("ssh_public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_username(self) -> typing.Optional[builtins.str]:
        '''The user's SSH user name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshusername
        '''
        result = self._values.get("ssh_username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnVolume(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opsworks.CfnVolume",
):
    '''Describes an instance's Amazon EBS volume.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opsworks as opsworks
        
        cfn_volume = opsworks.CfnVolume(self, "MyCfnVolume",
            ec2_volume_id="ec2VolumeId",
            stack_id="stackId",
        
            # the properties below are optional
            mount_point="mountPoint",
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ec2_volume_id: builtins.str,
        stack_id: builtins.str,
        mount_point: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ec2_volume_id: The Amazon EC2 volume ID.
        :param stack_id: The stack ID.
        :param mount_point: The volume mount point. For example, "/mnt/disk1".
        :param name: The volume name. Volume names are a maximum of 128 characters.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de0e780e9e0d4eda3a819d96c95bf8c36e8e41adc99aba36d5e3f3c53ddf411e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVolumeProps(
            ec2_volume_id=ec2_volume_id,
            stack_id=stack_id,
            mount_point=mount_point,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95d48fbb6ffdf4d1a775c146933d2aba292ef1e10e0fec5e42ab7c5ca1bf611b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2cc0d674f1df7fb399ca8775b28afc4f3744644854d328c4085eb558ea1ac20f)
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
    @jsii.member(jsii_name="ec2VolumeId")
    def ec2_volume_id(self) -> builtins.str:
        '''The Amazon EC2 volume ID.'''
        return typing.cast(builtins.str, jsii.get(self, "ec2VolumeId"))

    @ec2_volume_id.setter
    def ec2_volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e674eb595620722979b35b9a8e83d5c2e52266888ec1ae51e7c20919c71e307)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2VolumeId", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''The stack ID.'''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__405539dc8e4c5db62095fb9a3c6a20ba6ed5b40b5ba9733ecd03cf627ee30fee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)

    @builtins.property
    @jsii.member(jsii_name="mountPoint")
    def mount_point(self) -> typing.Optional[builtins.str]:
        '''The volume mount point.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPoint"))

    @mount_point.setter
    def mount_point(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d02062f7451093adc07a5a66fd778bc01992b2a7cb415288b2e20f9c7f85a062)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPoint", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ed129bda5b40c633ec64dfe0e7c2cdb5d48c7d652f80ba3114b2b4099f98441)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opsworks.CfnVolumeProps",
    jsii_struct_bases=[],
    name_mapping={
        "ec2_volume_id": "ec2VolumeId",
        "stack_id": "stackId",
        "mount_point": "mountPoint",
        "name": "name",
    },
)
class CfnVolumeProps:
    def __init__(
        self,
        *,
        ec2_volume_id: builtins.str,
        stack_id: builtins.str,
        mount_point: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVolume``.

        :param ec2_volume_id: The Amazon EC2 volume ID.
        :param stack_id: The stack ID.
        :param mount_point: The volume mount point. For example, "/mnt/disk1".
        :param name: The volume name. Volume names are a maximum of 128 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opsworks as opsworks
            
            cfn_volume_props = opsworks.CfnVolumeProps(
                ec2_volume_id="ec2VolumeId",
                stack_id="stackId",
            
                # the properties below are optional
                mount_point="mountPoint",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bf9954f0ce70eb8d07abcbf62b393f8247aa21a5f0e2ca31bf1461d3f31d76f)
            check_type(argname="argument ec2_volume_id", value=ec2_volume_id, expected_type=type_hints["ec2_volume_id"])
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
            check_type(argname="argument mount_point", value=mount_point, expected_type=type_hints["mount_point"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ec2_volume_id": ec2_volume_id,
            "stack_id": stack_id,
        }
        if mount_point is not None:
            self._values["mount_point"] = mount_point
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def ec2_volume_id(self) -> builtins.str:
        '''The Amazon EC2 volume ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-ec2volumeid
        '''
        result = self._values.get("ec2_volume_id")
        assert result is not None, "Required property 'ec2_volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''The stack ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-stackid
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_point(self) -> typing.Optional[builtins.str]:
        '''The volume mount point.

        For example, "/mnt/disk1".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-mountpoint
        '''
        result = self._values.get("mount_point")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The volume name.

        Volume names are a maximum of 128 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApp",
    "CfnAppProps",
    "CfnElasticLoadBalancerAttachment",
    "CfnElasticLoadBalancerAttachmentProps",
    "CfnInstance",
    "CfnInstanceProps",
    "CfnLayer",
    "CfnLayerProps",
    "CfnStack",
    "CfnStackProps",
    "CfnUserProfile",
    "CfnUserProfileProps",
    "CfnVolume",
    "CfnVolumeProps",
]

publication.publish()

def _typecheckingstub__9cfc69040af8322a035060c3c2b7a93463983dd64c29f11c41157c08be717ae8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    stack_id: builtins.str,
    type: builtins.str,
    app_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    data_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.DataSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_ssl: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    shortname: typing.Optional[builtins.str] = None,
    ssl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.SslConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ff143edbf423ab87fc5b07a79bac15afad922b4f9752bf18393dfbf1f9c9cd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c12528e296c556a11ebf8a34dd92bc4963eb767008506fae4907600da103cc0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a19c59d6094186b25ccb74f53b769ee4f330ac7d37adc44ca9689573bf3dbac7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44fcbd77f5eec62a5bc0eff1206b3965788d71cb0f98783d83060472cdbe1664(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca84fd86e0761b50ce73d01c5dc30322ab1d89c25362406b4f8c17d6c175708(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__185dad1883ad44edf530c80eedb41525e399494340def4de222a61617999031a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.SourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bced3305a9b7d70a45a3681d489962e84c64c8313a37872dfa4339ac6982d92d(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64566650c8e8b9d3d6b7f320ae9f2fd02d48557d1d06b6133a991557c9326de8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.DataSourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d3ebf2ce216f79a04213a4062b8b76a0e788f15cba7f5019619d673cad19cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27fab7ca15432dc0ce6185a2eef7831a65e6787482baeddb58e6de68a4dc1ca0(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8518eeb92295cd7150f12a3df695529ec26a1dd47aa59533a210493d9ee8bd8d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9d5c35bc69f1bf2418216b8439788ce44352eba1ce1bd2f8c6d0ed3fa939b21(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EnvironmentVariableProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc79da84419e543929094dc3dab262875e458ac8404232b6fd87d3306d47bf8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb8571a770edf95757d930ebc880d2330b6605dcf2c857c4616ee5cb1bd02163(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.SslConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cf45f6c19d83a84c2829e849bf67cc8df566964fcdac07b785b94c64176418d(
    *,
    arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f4bf1124807563999966950a3742bd343b3bf39de03896181aff2061910ba97(
    *,
    key: builtins.str,
    value: builtins.str,
    secure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b809263c93f54c1b303d60d709a45fea8e430f2e2275e331f5200153d7e203e(
    *,
    password: typing.Optional[builtins.str] = None,
    revision: typing.Optional[builtins.str] = None,
    ssh_key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa3e28175cca76b2b379e24dd298856761e8b2b972fbefd13fb45c20bfa622a(
    *,
    certificate: typing.Optional[builtins.str] = None,
    chain: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe0ae5f6e1367f942976862a375aa88ecad21e52429978b2181e9115ce82447e(
    *,
    name: builtins.str,
    stack_id: builtins.str,
    type: builtins.str,
    app_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    data_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.DataSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_ssl: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    shortname: typing.Optional[builtins.str] = None,
    ssl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.SslConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__486f7e1e8e8052927626441be8be1b13d2a9ce484c4915a83fb32a7def2f835d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    elastic_load_balancer_name: builtins.str,
    layer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3f53bd9cb54ef908ec70944a483b6bcfaee7dfb90c1ca4dbd915d2524c8d65(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c4f2d60c2a89e9f4dc4b0b1a839a6f752960decc3d3eb9e49cc21748378ee6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f09a3b90cb26ee5103e9da8d0751d21ff83e1203e9f45fb281e8704f606f9df0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fc612753cec7293a77d1dee6f0043e104fdad08f108eeff357be2fc4d973b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce4a38411eccbc7b0088bfd31a89e80bd98022d6249e27feb26e4ee7d3e6834(
    *,
    elastic_load_balancer_name: builtins.str,
    layer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b34de3ee05594312f14cce61c717304294b3891e9f25d66dd351119744660a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_type: builtins.str,
    layer_ids: typing.Sequence[builtins.str],
    stack_id: builtins.str,
    agent_version: typing.Optional[builtins.str] = None,
    ami_id: typing.Optional[builtins.str] = None,
    architecture: typing.Optional[builtins.str] = None,
    auto_scaling_type: typing.Optional[builtins.str] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.BlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    elastic_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    hostname: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    os: typing.Optional[builtins.str] = None,
    root_device_type: typing.Optional[builtins.str] = None,
    ssh_key_name: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tenancy: typing.Optional[builtins.str] = None,
    time_based_auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.TimeBasedAutoScalingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    virtualization_type: typing.Optional[builtins.str] = None,
    volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4d2ac66c9f980cb374fd5448e1c9f04e6eb8e602bd72300ac2abeaa822a7f0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627888c52651f1163646c543dd9a877f4373aa3e4fec84e06cd224ff01f92d0d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__120097d25f64c78439cbbabfbd0a307245ceccef33c5aa775f39972cfb49c826(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae9b7d675bad1f1f353a1989ad82553e5c04f98478cf56236e51d89f9959d5f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6698aa3cac36413f5c5cb1d378f05f7c515d8250e3f667a264f3629a455c9041(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__716a4f299d569f296c3aaae24e31a2798f5925dc5f10d1bbd86596025466008a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b1ce00bf1946d2dbd274a57e1fe91041c0e229d88bd6323fdeada3291f4cd6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016fd247ee893c25a899724b1d0c72804b32c2eb68c38c85818641c7c2f9757d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21648c47cae646283b32940cd17e1a34756ac2547ce79971404274110698194d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ab3a2190223656085199b9e11a0bf41abf21a19b31970f1ea3b7bf5d17ad4e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e26b3e54531ea4750ebcd10acbcacbf456f6855c3b5272dfcd85ceeaa432c455(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstance.BlockDeviceMappingProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ec1bf27e5cd83c8ba7388dfe17956f009f9836f2f5afa9558fb3ba8aa872cc7(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220dcfd8fd5d5ce9504430ff408ba0125b97234987629d071f0a36c70d880e2f(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b492c3f0264061d2b5ecc725ba0cd4efd2a4539e9096f19186820ffb12e432(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb45fe733de533d0fde9a771368ef2623aef37105aafd42bee26dfa53e01db5(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5333a6a2c50f73ee90d47575d7aa39dc563a43e60b92e74ff6b97a85ae59b25(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86bd0a754c6aa91d4e5999754c3bb8fb64afd84e8c29778aab752763bccd291e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff7b00fceb3aff580ec7a8bd7343bf0e8e17014dbd0c2dae2f0724091c2b591(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9385c60c2ba9003129cceef99b78905f2a550e6956fee4acaef2bb511deb34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbae61a65906b826bde0dfe6df35cc3e1f1ac8d4c197e1de1af5324c21b79745(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ffbe8115388f44a1f41ec2ceb16db364e3519d629ba7a55a34bbc3a12c9a7a1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.TimeBasedAutoScalingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28857381916cdbcb5a292da20a83f099028eabaeda40d7622b6aa635a2f0e7e0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63137171df7805585bd838275a6375290786e3e6f18f0708cb63f579bf8861f2(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f53cb18b26d4ce53cc58c51b2f50b9a2af609eeffeb17c2f393195d6f74ee8(
    *,
    device_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.EbsBlockDeviceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_device: typing.Optional[builtins.str] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c551f707582f21e17ce83ff8919f39f0c4300ae1c19ef2018670b1edcc8a65a(
    *,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dfcb549734883fb71a8f431ae16a65e4c926d97e9483cc865e0718bdaaae37b(
    *,
    friday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    monday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    saturday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    sunday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    thursday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    tuesday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    wednesday: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__064c38cf60beb5ee54299be9e04fc9e0d751e94688227f7c131215ac7ef613f9(
    *,
    instance_type: builtins.str,
    layer_ids: typing.Sequence[builtins.str],
    stack_id: builtins.str,
    agent_version: typing.Optional[builtins.str] = None,
    ami_id: typing.Optional[builtins.str] = None,
    architecture: typing.Optional[builtins.str] = None,
    auto_scaling_type: typing.Optional[builtins.str] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.BlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    elastic_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    hostname: typing.Optional[builtins.str] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    os: typing.Optional[builtins.str] = None,
    root_device_type: typing.Optional[builtins.str] = None,
    ssh_key_name: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tenancy: typing.Optional[builtins.str] = None,
    time_based_auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.TimeBasedAutoScalingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    virtualization_type: typing.Optional[builtins.str] = None,
    volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de185bdebf2e1467933cd283fec95f5a7ee02ecc41533bdbfa207c91a7c0a2f6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_assign_elastic_ips: typing.Union[builtins.bool, _IResolvable_da3f097b],
    auto_assign_public_ips: typing.Union[builtins.bool, _IResolvable_da3f097b],
    enable_auto_healing: typing.Union[builtins.bool, _IResolvable_da3f097b],
    name: builtins.str,
    shortname: builtins.str,
    stack_id: builtins.str,
    type: builtins.str,
    attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Any = None,
    custom_recipes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.RecipesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    lifecycle_event_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.LifecycleEventConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.LoadBasedAutoScalingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    packages: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    volume_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.VolumeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7769a3e709144e0e4d9e73a65055fcd2f8d00ee6279aa832c4c84ee943b42c6d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__769f052c927ec888e5dedc99e8521b022c0d238f66f201857a9a5305dc4c82fc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85978378733517803f89d7ce8ed749075b2acc8dc7d04f6b6e0c7e704d227ace(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ba55dbdeca1c05ff112a4836e57cd64cee40b72e11ac77b619cf736bfd51b1(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2351ccfe7eb13aba979ae0e393a2fd47e40926de22ecf6aba42a950ceba9ccca(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca8c56695fb83a676e32457bc6de19365f9c70eec1584dbc6f23606906b879d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846e6bcd67b109f59c3750304d8d8b6cb95ffa7b5e053a4d7f66bbb41bec35f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada31ec8e271ee88cd1fad4807bc6d4219ba3ae931955ab18863e4f5bbc716bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450ddd14c164d17317234149c9d02cecfd7b8da38ff8262ee9a2fcb25becd9be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9395644dbf3af1a765e40fb019bf24792671a4e69e059385183e9f7d8c09cef2(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6bd9eae8e2c43a63cc326dd83cd4cf25a20c2fda16a523fe488beec31c627be(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51213828c84c59f5b40dc3f53612fe0e252973a059400094e40e3bf915b9fc80(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e8c90b7b1058521d04d7f21c3b8bccb95a8c0f24ba2839b2d6f0cd9595fdc4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.RecipesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723bdf1798a6528f78499e56e3182d783681319599779eb826934d2c59139a04(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b42c4216b135b2a7074bfed5d80d9da1ba492a773d32e212a7237b6ebc391540(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbfa971c40efb5d7a653e36e1485b5fbe539dada94fc400376fe7e3b2cc83f34(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.LifecycleEventConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8787d1ac56a7ea2ee28e6088302bfb26415ba39511d17c7faa187287901d8aca(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLayer.LoadBasedAutoScalingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e23cd593d0b608a8a2ae24f2f02c6ee8d2c3fff203db62c80de805c29dbca4b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7cab1714e0f9090eff8c2189561d0d041f66002f761e700cf53a8945ad6a1c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33349ab02f637b084f62e0224a27ce7354d923ff559128f7665a25e2318617ee(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ed3702ce91b7433e1b5faab32e09d55b2da499fcfb988423341ceb00a2b770(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLayer.VolumeConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acebc56803bcaeb1947cfcc6e9e93fe43ceb2078e18ddbfd025a38603d4f7d58(
    *,
    cpu_threshold: typing.Optional[jsii.Number] = None,
    ignore_metrics_time: typing.Optional[jsii.Number] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    load_threshold: typing.Optional[jsii.Number] = None,
    memory_threshold: typing.Optional[jsii.Number] = None,
    thresholds_wait_time: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e4d41a79209a667596801a266fe03f27f87757282622ff6914569435490ee0b(
    *,
    shutdown_event_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.ShutdownEventConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d73f44ac3a86ed5c0f519f220ff022c6fefbedfca846c4bd6bda3db1f1a111(
    *,
    down_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.AutoScalingThresholdsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    up_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.AutoScalingThresholdsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e47cee19e47a49ee1c8993063e7798b7abccb6bd1dd66e69db20146863771f58(
    *,
    configure: typing.Optional[typing.Sequence[builtins.str]] = None,
    deploy: typing.Optional[typing.Sequence[builtins.str]] = None,
    setup: typing.Optional[typing.Sequence[builtins.str]] = None,
    shutdown: typing.Optional[typing.Sequence[builtins.str]] = None,
    undeploy: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b4b5a1198632d836216abf1c68ad55d170601286c9e14f18bb5e66d2491cbd3(
    *,
    delay_until_elb_connections_drained: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35bb02a582c61891e39f2981442acc233a0b3ee0ff93a8df791d8e2bf0ca5950(
    *,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    mount_point: typing.Optional[builtins.str] = None,
    number_of_disks: typing.Optional[jsii.Number] = None,
    raid_level: typing.Optional[jsii.Number] = None,
    size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c38216d74d64877783d8570f455e1bede8bb638962a7d006b49b8f741161c6(
    *,
    auto_assign_elastic_ips: typing.Union[builtins.bool, _IResolvable_da3f097b],
    auto_assign_public_ips: typing.Union[builtins.bool, _IResolvable_da3f097b],
    enable_auto_healing: typing.Union[builtins.bool, _IResolvable_da3f097b],
    name: builtins.str,
    shortname: builtins.str,
    stack_id: builtins.str,
    type: builtins.str,
    attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    custom_instance_profile_arn: typing.Optional[builtins.str] = None,
    custom_json: typing.Any = None,
    custom_recipes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.RecipesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    lifecycle_event_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.LifecycleEventConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    load_based_auto_scaling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.LoadBasedAutoScalingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    packages: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    volume_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayer.VolumeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf36f6bd552e246cec8163081581d4887e2e1838c2af0dfdfec5a94265183ed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_instance_profile_arn: builtins.str,
    name: builtins.str,
    service_role_arn: builtins.str,
    agent_version: typing.Optional[builtins.str] = None,
    attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    chef_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ChefConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    clone_app_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    clone_permissions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    configuration_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StackConfigurationManagerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_cookbooks_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_json: typing.Any = None,
    default_availability_zone: typing.Optional[builtins.str] = None,
    default_os: typing.Optional[builtins.str] = None,
    default_root_device_type: typing.Optional[builtins.str] = None,
    default_ssh_key_name: typing.Optional[builtins.str] = None,
    default_subnet_id: typing.Optional[builtins.str] = None,
    ecs_cluster_arn: typing.Optional[builtins.str] = None,
    elastic_ips: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ElasticIpProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    hostname_theme: typing.Optional[builtins.str] = None,
    rds_db_instances: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.RdsDbInstanceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_stack_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b361ad0a6f0d9dfac35a11da0b66f08aa9b0147967d3f53cd273d313b99dd78c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d5d71f906760fc69e166fb118bdbe1cc995ea63682ce754be4ac9b1bcc282e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcd2146f03d53d0bae14a634773ac910108f90fe74c5850ae2cd62dcdba8ff91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f89b36dae98f2d94483d0e9b6f3ab58ba94d26da8024b7add02be1da0ab8971(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445f8be97bcc844a6174bad8312f2728cb0fc0c80b3485a6a065dc3dd7e8187c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be1597201772d629a8add01522e76bbc0e640244dde68fc6989d34c4615b757(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f53c27695b37fef5c31ad65f5466de830aad0d0e404b030255b9b656ad9b651(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199cd836015029791dcb4c989b8ee7c17c9da5ef5f21511d039b62b20758d88b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.ChefConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f94a28e6ee04321bfefa35125fa40665608f0b6f49bf1a9df27f9bb244c29a1a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39351cb814c7f03e34818b747d34f2049f3376b379272c0f23b6fa4a1729cf48(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a10239804abfac0b9d5794c751a6f72e554b611f7631b0a15f7bae4472fc18(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.StackConfigurationManagerProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b869d48381b55b175cfbaba7ef0f8953ebdc1078d9d078e8bc09422eee78ec0d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStack.SourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5afc13f67b5e304c063782f4f1baebe0e122de72c58ff0422ee442b028862b1f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0575d99ba2e198bd6047071bffef1370688626589013bdf50f10edad2930ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36eae94ac5dbe46e281ec3642d2992dcc3a11fd85e320a331c135b14abe1825e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f346d6b179d1e5360e467ce27e42749aa4b2913d1009390c63dc13808f9282(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2de1c06c809948d02eeaef6ea6f660f45a9b01d1d97c7882090782849c6296e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f623274426e3c785a5039bed9eae8a33b23dda8ed8becfae6480187e553118b2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdd6f1f4f441686edc78cb49aa2b6a3ba64fa61be24b8b603ed59a555b80ccd1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8166a03c0b2b271ef176beca6de587fdfbf1f5c676c8d7d58b600ce5bb52738b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.ElasticIpProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0914ce2c4431a2766a2ec8f8ab3e2efd9e068fd797143dde5eae137cb581f725(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e5c5e4acdf62f9ce5d722219f3d8ea43ee54e485cbe2d141d73dcfd9b1b9b7d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStack.RdsDbInstanceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41d3731a853e0ecfcc8a979203fc2e807e9448c8d8cb112caa8c27b67e51c4b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b63dc4ecfd6df94a2c43b724328516c740a7518772217390f2712f6f5be41ae(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c8233bb88e60d83459f630fa2811d4e9bcbc58db4b583deecc08f372dc1753(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ac7bd4cfa5842431efd855ba2ad80900d00e084c7d85e9a5de10abac8159d5f(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f99b9f1135a63819780a97a4e2a7c709c76a30d135fe4ca28a4f22083a5d73b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf9ebc10290309cd8a1b70ca75f5db34b7f4ad850a7c01823703880a958847d(
    *,
    berkshelf_version: typing.Optional[builtins.str] = None,
    manage_berkshelf: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ee561457c88f487ec83cc46992533784aed634d52bb7bb125bff6ac7f70a96(
    *,
    ip: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b82360194600f18115acf75a0aa1bad6e17cc7b3258cc43567008e3cedbf5d0(
    *,
    db_password: builtins.str,
    db_user: builtins.str,
    rds_db_instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd7288c88143256aba1740990a9ddf652b90605d6d9df2b675539cf3f658474(
    *,
    password: typing.Optional[builtins.str] = None,
    revision: typing.Optional[builtins.str] = None,
    ssh_key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c21d7fcd41f5c5f2c62e0d7b9877b307d95ccdeece063c91c4db1d441a16ac6(
    *,
    name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__675a36919e38f296f3b53b7679384ec86298336f087126cb5bee9e1e22a8445c(
    *,
    default_instance_profile_arn: builtins.str,
    name: builtins.str,
    service_role_arn: builtins.str,
    agent_version: typing.Optional[builtins.str] = None,
    attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    chef_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ChefConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    clone_app_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    clone_permissions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    configuration_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.StackConfigurationManagerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_cookbooks_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_json: typing.Any = None,
    default_availability_zone: typing.Optional[builtins.str] = None,
    default_os: typing.Optional[builtins.str] = None,
    default_root_device_type: typing.Optional[builtins.str] = None,
    default_ssh_key_name: typing.Optional[builtins.str] = None,
    default_subnet_id: typing.Optional[builtins.str] = None,
    ecs_cluster_arn: typing.Optional[builtins.str] = None,
    elastic_ips: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.ElasticIpProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    hostname_theme: typing.Optional[builtins.str] = None,
    rds_db_instances: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStack.RdsDbInstanceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_stack_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f841ed2cddcf6c81296cc894f86e940d11eef568430b95d1b3254394ce0adb34(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    iam_user_arn: builtins.str,
    allow_self_management: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ssh_public_key: typing.Optional[builtins.str] = None,
    ssh_username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2299d976cf9af9d070893ec6b7430487983701fdf2b290750bf77ed59a1cd17(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55f5b517b73ce52986d98356734c969824ecf1d0952831a487957921991673da(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3690d5d3f6d99859dfc161334057968dd09b0d5b9ae89605055c2fe2774cfe47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__128de556beee0c143ac666faced9d32f126718068e45c973130b0b1e5f8ad3e3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d0e5e7d2b5344bfdfd2e358e2f6fd6be76f752928ccf7bff0f2740fc233eac9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8836ddb30644943ce6efae3bc2a36b644b5c82b5a34b9b1b4ea35bf9849e2e85(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c4119cda15b50587c240dbd706f63701c8bc940cdb11ef0e8c6fa341479ff30(
    *,
    iam_user_arn: builtins.str,
    allow_self_management: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ssh_public_key: typing.Optional[builtins.str] = None,
    ssh_username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de0e780e9e0d4eda3a819d96c95bf8c36e8e41adc99aba36d5e3f3c53ddf411e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ec2_volume_id: builtins.str,
    stack_id: builtins.str,
    mount_point: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d48fbb6ffdf4d1a775c146933d2aba292ef1e10e0fec5e42ab7c5ca1bf611b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc0d674f1df7fb399ca8775b28afc4f3744644854d328c4085eb558ea1ac20f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e674eb595620722979b35b9a8e83d5c2e52266888ec1ae51e7c20919c71e307(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405539dc8e4c5db62095fb9a3c6a20ba6ed5b40b5ba9733ecd03cf627ee30fee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d02062f7451093adc07a5a66fd778bc01992b2a7cb415288b2e20f9c7f85a062(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed129bda5b40c633ec64dfe0e7c2cdb5d48c7d652f80ba3114b2b4099f98441(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bf9954f0ce70eb8d07abcbf62b393f8247aa21a5f0e2ca31bf1461d3f31d76f(
    *,
    ec2_volume_id: builtins.str,
    stack_id: builtins.str,
    mount_point: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
