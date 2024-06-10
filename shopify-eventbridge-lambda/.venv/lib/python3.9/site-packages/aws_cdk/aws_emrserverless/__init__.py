'''
# AWS::EMRServerless Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_emrserverless as emrserverless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EMRServerless construct libraries](https://constructs.dev/search?q=emrserverless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EMRServerless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRServerless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EMRServerless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRServerless.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication",
):
    '''The ``AWS::EMRServerless::Application`` resource specifies an EMR Serverless application.

    An application uses open source analytics frameworks to run jobs that process data. To create an application, you must specify the release version for the open source framework version you want to use and the type of application you want, such as Apache Spark or Apache Hive. After you create an application, you can submit data processing jobs or interactive requests to it.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html
    :cloudformationResource: AWS::EMRServerless::Application
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrserverless as emrserverless
        
        # configuration_object_property_: emrserverless.CfnApplication.ConfigurationObjectProperty
        
        cfn_application = emrserverless.CfnApplication(self, "MyCfnApplication",
            release_label="releaseLabel",
            type="type",
        
            # the properties below are optional
            architecture="architecture",
            auto_start_configuration=emrserverless.CfnApplication.AutoStartConfigurationProperty(
                enabled=False
            ),
            auto_stop_configuration=emrserverless.CfnApplication.AutoStopConfigurationProperty(
                enabled=False,
                idle_timeout_minutes=123
            ),
            image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                image_uri="imageUri"
            ),
            initial_capacity=[emrserverless.CfnApplication.InitialCapacityConfigKeyValuePairProperty(
                key="key",
                value=emrserverless.CfnApplication.InitialCapacityConfigProperty(
                    worker_configuration=emrserverless.CfnApplication.WorkerConfigurationProperty(
                        cpu="cpu",
                        memory="memory",
        
                        # the properties below are optional
                        disk="disk"
                    ),
                    worker_count=123
                )
            )],
            maximum_capacity=emrserverless.CfnApplication.MaximumAllowedResourcesProperty(
                cpu="cpu",
                memory="memory",
        
                # the properties below are optional
                disk="disk"
            ),
            monitoring_configuration=emrserverless.CfnApplication.MonitoringConfigurationProperty(
                cloud_watch_logging_configuration=emrserverless.CfnApplication.CloudWatchLoggingConfigurationProperty(
                    enabled=False,
                    encryption_key_arn="encryptionKeyArn",
                    log_group_name="logGroupName",
                    log_stream_name_prefix="logStreamNamePrefix",
                    log_type_map=[emrserverless.CfnApplication.LogTypeMapKeyValuePairProperty(
                        key="key",
                        value=["value"]
                    )]
                ),
                managed_persistence_monitoring_configuration=emrserverless.CfnApplication.ManagedPersistenceMonitoringConfigurationProperty(
                    enabled=False,
                    encryption_key_arn="encryptionKeyArn"
                ),
                s3_monitoring_configuration=emrserverless.CfnApplication.S3MonitoringConfigurationProperty(
                    encryption_key_arn="encryptionKeyArn",
                    log_uri="logUri"
                )
            ),
            name="name",
            network_configuration=emrserverless.CfnApplication.NetworkConfigurationProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            ),
            runtime_configuration=[emrserverless.CfnApplication.ConfigurationObjectProperty(
                classification="classification",
        
                # the properties below are optional
                configurations=[configuration_object_property_],
                properties={
                    "properties_key": "properties"
                }
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            worker_type_specifications={
                "worker_type_specifications_key": emrserverless.CfnApplication.WorkerTypeSpecificationInputProperty(
                    image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                        image_uri="imageUri"
                    )
                )
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        release_label: builtins.str,
        type: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
        auto_start_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.AutoStartConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        auto_stop_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.AutoStopConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.ImageConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        initial_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.InitialCapacityConfigKeyValuePairProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        maximum_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.MaximumAllowedResourcesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.ConfigurationObjectProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        worker_type_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.WorkerTypeSpecificationInputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param release_label: The EMR release associated with the application.
        :param type: The type of application, such as Spark or Hive.
        :param architecture: The CPU architecture of an application.
        :param auto_start_configuration: The configuration for an application to automatically start on job submission.
        :param auto_stop_configuration: The configuration for an application to automatically stop after a certain amount of time being idle.
        :param image_configuration: The image configuration applied to all worker types.
        :param initial_capacity: The initial capacity of the application.
        :param maximum_capacity: The maximum capacity of the application. This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.
        :param monitoring_configuration: A configuration specification to be used when provisioning an application. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.
        :param name: The name of the application.
        :param network_configuration: The network configuration for customer VPC connectivity for the application.
        :param runtime_configuration: The `Configuration <https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html>`_ specifications of an application. Each configuration consists of a classification and properties. You use this parameter when creating or updating an application. To see the runtimeConfiguration object of an application, run the `GetApplication <https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html>`_ API operation.
        :param tags: The tags assigned to the application.
        :param worker_type_specifications: The specification applied to each worker type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73910249d55cbd2983a3ea1bb4666acedb0e3e84df9686bbdeecd191b5ae6373)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            release_label=release_label,
            type=type,
            architecture=architecture,
            auto_start_configuration=auto_start_configuration,
            auto_stop_configuration=auto_stop_configuration,
            image_configuration=image_configuration,
            initial_capacity=initial_capacity,
            maximum_capacity=maximum_capacity,
            monitoring_configuration=monitoring_configuration,
            name=name,
            network_configuration=network_configuration,
            runtime_configuration=runtime_configuration,
            tags=tags,
            worker_type_specifications=worker_type_specifications,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffb07c3ee5bcef7cdea2376c768ef28e4be2a5ff1b3d59792805560edbc23a53)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe1c41fe06697b2d8c071c7eb2680f90736a7d5e873109e23c86cfa1bdcce8c9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''The ID of the application, such as ``ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: ApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the project.

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
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> builtins.str:
        '''The EMR release associated with the application.'''
        return typing.cast(builtins.str, jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ddb97a434bd94c3f60161a520cb237aed52648f4fcaf12da72c9a88137afdae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of application, such as Spark or Hive.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f57e27e169be5182ad6ebed2fc50b72e6470752b0d5d5454c1d9b23bfaeaf18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> typing.Optional[builtins.str]:
        '''The CPU architecture of an application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "architecture"))

    @architecture.setter
    def architecture(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2273d6ae79032b2ac60c651e12d059c9c2d80c06c7391dab5fed7dd019ef2f8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architecture", value)

    @builtins.property
    @jsii.member(jsii_name="autoStartConfiguration")
    def auto_start_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoStartConfigurationProperty"]]:
        '''The configuration for an application to automatically start on job submission.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoStartConfigurationProperty"]], jsii.get(self, "autoStartConfiguration"))

    @auto_start_configuration.setter
    def auto_start_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoStartConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__250efc466f983b8a885240945cba35864cbd2a6767d45f9c36fd1d25d01092c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStartConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="autoStopConfiguration")
    def auto_stop_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoStopConfigurationProperty"]]:
        '''The configuration for an application to automatically stop after a certain amount of time being idle.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoStopConfigurationProperty"]], jsii.get(self, "autoStopConfiguration"))

    @auto_stop_configuration.setter
    def auto_stop_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoStopConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f1b3d83107f5e408234e2bfc84b1e4ecd5f468b8f46ba51ddf116c1b97908f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStopConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageConfiguration")
    def image_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ImageConfigurationInputProperty"]]:
        '''The image configuration applied to all worker types.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ImageConfigurationInputProperty"]], jsii.get(self, "imageConfiguration"))

    @image_configuration.setter
    def image_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ImageConfigurationInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__368a96aa7c6ff916676fe29b5a922fae846a89a5edbb8c71b20a5d60107bff71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="initialCapacity")
    def initial_capacity(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.InitialCapacityConfigKeyValuePairProperty"]]]]:
        '''The initial capacity of the application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.InitialCapacityConfigKeyValuePairProperty"]]]], jsii.get(self, "initialCapacity"))

    @initial_capacity.setter
    def initial_capacity(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.InitialCapacityConfigKeyValuePairProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba3bfbe46861fe91b5e1b2fe0373abb6e5b5f46147bf7eb286264343039f5b04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="maximumCapacity")
    def maximum_capacity(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MaximumAllowedResourcesProperty"]]:
        '''The maximum capacity of the application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MaximumAllowedResourcesProperty"]], jsii.get(self, "maximumCapacity"))

    @maximum_capacity.setter
    def maximum_capacity(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MaximumAllowedResourcesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358e38959731258abe08d7ec2ddde30c2f91167a5e3a6ed66750a800db2cf6b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MonitoringConfigurationProperty"]]:
        '''A configuration specification to be used when provisioning an application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MonitoringConfigurationProperty"]], jsii.get(self, "monitoringConfiguration"))

    @monitoring_configuration.setter
    def monitoring_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MonitoringConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9899534798dfa06d9a764edbb0466853de6132045ef162d2e77c6ee2692e88ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70ae684b6a8f75a4ea6b60c08ad238517e03708361aa167abbbe2c94dc5bb9d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.NetworkConfigurationProperty"]]:
        '''The network configuration for customer VPC connectivity for the application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.NetworkConfigurationProperty"]], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.NetworkConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c89ab319e8ae68523a39499d53338babf76d8a1fa439e7e46c3daeacb28a4bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeConfiguration")
    def runtime_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.ConfigurationObjectProperty"]]]]:
        '''The `Configuration <https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html>`_ specifications of an application. Each configuration consists of a classification and properties. You use this parameter when creating or updating an application. To see the runtimeConfiguration object of an application, run the `GetApplication <https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html>`_ API operation.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.ConfigurationObjectProperty"]]]], jsii.get(self, "runtimeConfiguration"))

    @runtime_configuration.setter
    def runtime_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.ConfigurationObjectProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8009c989bc781626fbf3067531c118d2a94649c7cd583ee7c5604a168e732dfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the application.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c62e07950c8c2fa752bd4e5ac938292f2380eb4b2fc5d19d5f5a2a46e5fc39aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workerTypeSpecifications")
    def worker_type_specifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnApplication.WorkerTypeSpecificationInputProperty"]]]]:
        '''The specification applied to each worker type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnApplication.WorkerTypeSpecificationInputProperty"]]]], jsii.get(self, "workerTypeSpecifications"))

    @worker_type_specifications.setter
    def worker_type_specifications(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnApplication.WorkerTypeSpecificationInputProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04bd95d4e436eaf679b9831515cb5d2d9cce5c8686b56c55065b2b99bd9660ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerTypeSpecifications", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.AutoStartConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class AutoStartConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Configuration for Auto Start of Application.

            :param enabled: If set to true, the Application will automatically start. Defaults to true. Default: - true

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostartconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                auto_start_configuration_property = emrserverless.CfnApplication.AutoStartConfigurationProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3408c1d905295731e672b4fc518643f3fe70d0851e610b36fc4f060f52d01567)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to true, the Application will automatically start.

            Defaults to true.

            :default: - true

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostartconfiguration.html#cfn-emrserverless-application-autostartconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoStartConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.AutoStopConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "idle_timeout_minutes": "idleTimeoutMinutes",
        },
    )
    class AutoStopConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            idle_timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration for Auto Stop of Application.

            :param enabled: If set to true, the Application will automatically stop after being idle. Defaults to true. Default: - true
            :param idle_timeout_minutes: The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                auto_stop_configuration_property = emrserverless.CfnApplication.AutoStopConfigurationProperty(
                    enabled=False,
                    idle_timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__962238425f6319f997d9db8d2fd1983e29503aa305579b2aeaee5d7d36e0e2fb)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument idle_timeout_minutes", value=idle_timeout_minutes, expected_type=type_hints["idle_timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if idle_timeout_minutes is not None:
                self._values["idle_timeout_minutes"] = idle_timeout_minutes

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to true, the Application will automatically stop after being idle.

            Defaults to true.

            :default: - true

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html#cfn-emrserverless-application-autostopconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def idle_timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The amount of time [in minutes] to wait before auto stopping the Application when idle.

            Defaults to 15 minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html#cfn-emrserverless-application-autostopconfiguration-idletimeoutminutes
            '''
            result = self._values.get("idle_timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoStopConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.CloudWatchLoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "encryption_key_arn": "encryptionKeyArn",
            "log_group_name": "logGroupName",
            "log_stream_name_prefix": "logStreamNamePrefix",
            "log_type_map": "logTypeMap",
        },
    )
    class CloudWatchLoggingConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encryption_key_arn: typing.Optional[builtins.str] = None,
            log_group_name: typing.Optional[builtins.str] = None,
            log_stream_name_prefix: typing.Optional[builtins.str] = None,
            log_type_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.LogTypeMapKeyValuePairProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The Amazon CloudWatch configuration for monitoring logs.

            You can configure your jobs to send log information to CloudWatch .

            :param enabled: Enables CloudWatch logging. Default: - false
            :param encryption_key_arn: The AWS Key Management Service (KMS) key ARN to encrypt the logs that you store in CloudWatch Logs .
            :param log_group_name: The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.
            :param log_stream_name_prefix: Prefix for the CloudWatch log stream name.
            :param log_type_map: The specific log-streams which need to be uploaded to CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-cloudwatchloggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                cloud_watch_logging_configuration_property = emrserverless.CfnApplication.CloudWatchLoggingConfigurationProperty(
                    enabled=False,
                    encryption_key_arn="encryptionKeyArn",
                    log_group_name="logGroupName",
                    log_stream_name_prefix="logStreamNamePrefix",
                    log_type_map=[emrserverless.CfnApplication.LogTypeMapKeyValuePairProperty(
                        key="key",
                        value=["value"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec71ff6297cc71f2d7e9773aafa9436f445613d427eec9083528cb272b7968c4)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_stream_name_prefix", value=log_stream_name_prefix, expected_type=type_hints["log_stream_name_prefix"])
                check_type(argname="argument log_type_map", value=log_type_map, expected_type=type_hints["log_type_map"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if encryption_key_arn is not None:
                self._values["encryption_key_arn"] = encryption_key_arn
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_stream_name_prefix is not None:
                self._values["log_stream_name_prefix"] = log_stream_name_prefix
            if log_type_map is not None:
                self._values["log_type_map"] = log_type_map

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables CloudWatch logging.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-cloudwatchloggingconfiguration.html#cfn-emrserverless-application-cloudwatchloggingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encryption_key_arn(self) -> typing.Optional[builtins.str]:
            '''The AWS Key Management Service (KMS) key ARN to encrypt the logs that you store in CloudWatch Logs .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-cloudwatchloggingconfiguration.html#cfn-emrserverless-application-cloudwatchloggingconfiguration-encryptionkeyarn
            '''
            result = self._values.get("encryption_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-cloudwatchloggingconfiguration.html#cfn-emrserverless-application-cloudwatchloggingconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_stream_name_prefix(self) -> typing.Optional[builtins.str]:
            '''Prefix for the CloudWatch log stream name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-cloudwatchloggingconfiguration.html#cfn-emrserverless-application-cloudwatchloggingconfiguration-logstreamnameprefix
            '''
            result = self._values.get("log_stream_name_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_type_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.LogTypeMapKeyValuePairProperty"]]]]:
            '''The specific log-streams which need to be uploaded to CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-cloudwatchloggingconfiguration.html#cfn-emrserverless-application-cloudwatchloggingconfiguration-logtypemap
            '''
            result = self._values.get("log_type_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.LogTypeMapKeyValuePairProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.ConfigurationObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configurations": "configurations",
            "properties": "properties",
        },
    )
    class ConfigurationObjectProperty:
        def __init__(
            self,
            *,
            classification: builtins.str,
            configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.ConfigurationObjectProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Configuration for a JobRun.

            :param classification: 
            :param configurations: 
            :param properties: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-configurationobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                # configuration_object_property_: emrserverless.CfnApplication.ConfigurationObjectProperty
                
                configuration_object_property = emrserverless.CfnApplication.ConfigurationObjectProperty(
                    classification="classification",
                
                    # the properties below are optional
                    configurations=[configuration_object_property_],
                    properties={
                        "properties_key": "properties"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6631f05a0f985523b64829ba85bb2686c8aecd114d8a1c04c994338ec0f0718)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "classification": classification,
            }
            if configurations is not None:
                self._values["configurations"] = configurations
            if properties is not None:
                self._values["properties"] = properties

        @builtins.property
        def classification(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-configurationobject.html#cfn-emrserverless-application-configurationobject-classification
            '''
            result = self._values.get("classification")
            assert result is not None, "Required property 'classification' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.ConfigurationObjectProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-configurationobject.html#cfn-emrserverless-application-configurationobject-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.ConfigurationObjectProperty"]]]], result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-configurationobject.html#cfn-emrserverless-application-configurationobject-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.ImageConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"image_uri": "imageUri"},
    )
    class ImageConfigurationInputProperty:
        def __init__(self, *, image_uri: typing.Optional[builtins.str] = None) -> None:
            '''The image configuration.

            :param image_uri: The URI of an image in the Amazon ECR registry. This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-imageconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                image_configuration_input_property = emrserverless.CfnApplication.ImageConfigurationInputProperty(
                    image_uri="imageUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f60138497ea02d9962f5b33612a58874538452fcad71efafe327c8dd4b46ee62)
                check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_uri is not None:
                self._values["image_uri"] = image_uri

        @builtins.property
        def image_uri(self) -> typing.Optional[builtins.str]:
            '''The URI of an image in the Amazon ECR registry.

            This field is required when you create a new application. If you leave this field blank in an update, Amazon EMR will remove the image configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-imageconfigurationinput.html#cfn-emrserverless-application-imageconfigurationinput-imageuri
            '''
            result = self._values.get("image_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.InitialCapacityConfigKeyValuePairProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class InitialCapacityConfigKeyValuePairProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.InitialCapacityConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param key: Worker type for an analytics framework.
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                initial_capacity_config_key_value_pair_property = emrserverless.CfnApplication.InitialCapacityConfigKeyValuePairProperty(
                    key="key",
                    value=emrserverless.CfnApplication.InitialCapacityConfigProperty(
                        worker_configuration=emrserverless.CfnApplication.WorkerConfigurationProperty(
                            cpu="cpu",
                            memory="memory",
                
                            # the properties below are optional
                            disk="disk"
                        ),
                        worker_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a670fb912d740316bb84ff842e2f70b20b264127e994454037f69be3f399f68)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''Worker type for an analytics framework.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnApplication.InitialCapacityConfigProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApplication.InitialCapacityConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InitialCapacityConfigKeyValuePairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.InitialCapacityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "worker_configuration": "workerConfiguration",
            "worker_count": "workerCount",
        },
    )
    class InitialCapacityConfigProperty:
        def __init__(
            self,
            *,
            worker_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.WorkerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            worker_count: jsii.Number,
        ) -> None:
            '''The initial capacity configuration per worker.

            :param worker_configuration: The resource configuration of the initial capacity configuration.
            :param worker_count: The number of workers in the initial capacity configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                initial_capacity_config_property = emrserverless.CfnApplication.InitialCapacityConfigProperty(
                    worker_configuration=emrserverless.CfnApplication.WorkerConfigurationProperty(
                        cpu="cpu",
                        memory="memory",
                
                        # the properties below are optional
                        disk="disk"
                    ),
                    worker_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48da54ce8c9f1ee4240ad6b62d8fe9b0e060a955f7cbba04cae2f1fbd25cfcfd)
                check_type(argname="argument worker_configuration", value=worker_configuration, expected_type=type_hints["worker_configuration"])
                check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "worker_configuration": worker_configuration,
                "worker_count": worker_count,
            }

        @builtins.property
        def worker_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnApplication.WorkerConfigurationProperty"]:
            '''The resource configuration of the initial capacity configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html#cfn-emrserverless-application-initialcapacityconfig-workerconfiguration
            '''
            result = self._values.get("worker_configuration")
            assert result is not None, "Required property 'worker_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApplication.WorkerConfigurationProperty"], result)

        @builtins.property
        def worker_count(self) -> jsii.Number:
            '''The number of workers in the initial capacity configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html#cfn-emrserverless-application-initialcapacityconfig-workercount
            '''
            result = self._values.get("worker_count")
            assert result is not None, "Required property 'worker_count' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InitialCapacityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.LogTypeMapKeyValuePairProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class LogTypeMapKeyValuePairProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param key: 
            :param value: List of Applicable values: [STDOUT, STDERR, HIVE_LOG, TEZ_AM, SYSTEM_LOGS].

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-logtypemapkeyvaluepair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                log_type_map_key_value_pair_property = emrserverless.CfnApplication.LogTypeMapKeyValuePairProperty(
                    key="key",
                    value=["value"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11de2a1a9a00f1d9b3a16e41746ea3d40e8b57bb6d0cb6b83bd8e3eddf86ff71)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-logtypemapkeyvaluepair.html#cfn-emrserverless-application-logtypemapkeyvaluepair-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.List[builtins.str]:
            '''List of Applicable values: [STDOUT, STDERR, HIVE_LOG, TEZ_AM, SYSTEM_LOGS].

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-logtypemapkeyvaluepair.html#cfn-emrserverless-application-logtypemapkeyvaluepair-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogTypeMapKeyValuePairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.ManagedPersistenceMonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "encryption_key_arn": "encryptionKeyArn"},
    )
    class ManagedPersistenceMonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encryption_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The managed log persistence configuration for a job run.

            :param enabled: Enables managed logging and defaults to true. If set to false, managed logging will be turned off. Default: - true
            :param encryption_key_arn: The KMS key ARN to encrypt the logs stored in managed log persistence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                managed_persistence_monitoring_configuration_property = emrserverless.CfnApplication.ManagedPersistenceMonitoringConfigurationProperty(
                    enabled=False,
                    encryption_key_arn="encryptionKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8787c60c8f797aeb97be0765739b01f867e4756173c68e36db977bef73482c2a)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if encryption_key_arn is not None:
                self._values["encryption_key_arn"] = encryption_key_arn

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables managed logging and defaults to true.

            If set to false, managed logging will be turned off.

            :default: - true

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration.html#cfn-emrserverless-application-managedpersistencemonitoringconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encryption_key_arn(self) -> typing.Optional[builtins.str]:
            '''The KMS key ARN to encrypt the logs stored in managed log persistence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration.html#cfn-emrserverless-application-managedpersistencemonitoringconfiguration-encryptionkeyarn
            '''
            result = self._values.get("encryption_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManagedPersistenceMonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.MaximumAllowedResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu": "cpu", "memory": "memory", "disk": "disk"},
    )
    class MaximumAllowedResourcesProperty:
        def __init__(
            self,
            *,
            cpu: builtins.str,
            memory: builtins.str,
            disk: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The maximum allowed cumulative resources for an application.

            No new resources will be created once the limit is hit.

            :param cpu: The maximum allowed CPU for an application.
            :param memory: The maximum allowed resources for an application.
            :param disk: The maximum allowed disk for an application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                maximum_allowed_resources_property = emrserverless.CfnApplication.MaximumAllowedResourcesProperty(
                    cpu="cpu",
                    memory="memory",
                
                    # the properties below are optional
                    disk="disk"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__536f69d7e03464181452f489bfb1c04d11b8e8a746a0015b74730a948e1f7189)
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
                check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cpu": cpu,
                "memory": memory,
            }
            if disk is not None:
                self._values["disk"] = disk

        @builtins.property
        def cpu(self) -> builtins.str:
            '''The maximum allowed CPU for an application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-cpu
            '''
            result = self._values.get("cpu")
            assert result is not None, "Required property 'cpu' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def memory(self) -> builtins.str:
            '''The maximum allowed resources for an application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-memory
            '''
            result = self._values.get("memory")
            assert result is not None, "Required property 'memory' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def disk(self) -> typing.Optional[builtins.str]:
            '''The maximum allowed disk for an application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-disk
            '''
            result = self._values.get("disk")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaximumAllowedResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logging_configuration": "cloudWatchLoggingConfiguration",
            "managed_persistence_monitoring_configuration": "managedPersistenceMonitoringConfiguration",
            "s3_monitoring_configuration": "s3MonitoringConfiguration",
        },
    )
    class MonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.CloudWatchLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            managed_persistence_monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.ManagedPersistenceMonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.S3MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration setting for monitoring.

            :param cloud_watch_logging_configuration: The Amazon CloudWatch configuration for monitoring logs. You can configure your jobs to send log information to CloudWatch .
            :param managed_persistence_monitoring_configuration: The managed log persistence configuration for a job run.
            :param s3_monitoring_configuration: The Amazon S3 configuration for monitoring log publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                monitoring_configuration_property = emrserverless.CfnApplication.MonitoringConfigurationProperty(
                    cloud_watch_logging_configuration=emrserverless.CfnApplication.CloudWatchLoggingConfigurationProperty(
                        enabled=False,
                        encryption_key_arn="encryptionKeyArn",
                        log_group_name="logGroupName",
                        log_stream_name_prefix="logStreamNamePrefix",
                        log_type_map=[emrserverless.CfnApplication.LogTypeMapKeyValuePairProperty(
                            key="key",
                            value=["value"]
                        )]
                    ),
                    managed_persistence_monitoring_configuration=emrserverless.CfnApplication.ManagedPersistenceMonitoringConfigurationProperty(
                        enabled=False,
                        encryption_key_arn="encryptionKeyArn"
                    ),
                    s3_monitoring_configuration=emrserverless.CfnApplication.S3MonitoringConfigurationProperty(
                        encryption_key_arn="encryptionKeyArn",
                        log_uri="logUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac64b7b17b97bdc5b470cb32b1b0c00b3bdd7d97ea83ace7e59e5eb7f78d59e6)
                check_type(argname="argument cloud_watch_logging_configuration", value=cloud_watch_logging_configuration, expected_type=type_hints["cloud_watch_logging_configuration"])
                check_type(argname="argument managed_persistence_monitoring_configuration", value=managed_persistence_monitoring_configuration, expected_type=type_hints["managed_persistence_monitoring_configuration"])
                check_type(argname="argument s3_monitoring_configuration", value=s3_monitoring_configuration, expected_type=type_hints["s3_monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logging_configuration is not None:
                self._values["cloud_watch_logging_configuration"] = cloud_watch_logging_configuration
            if managed_persistence_monitoring_configuration is not None:
                self._values["managed_persistence_monitoring_configuration"] = managed_persistence_monitoring_configuration
            if s3_monitoring_configuration is not None:
                self._values["s3_monitoring_configuration"] = s3_monitoring_configuration

        @builtins.property
        def cloud_watch_logging_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.CloudWatchLoggingConfigurationProperty"]]:
            '''The Amazon CloudWatch configuration for monitoring logs.

            You can configure your jobs to send log information to CloudWatch .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-monitoringconfiguration.html#cfn-emrserverless-application-monitoringconfiguration-cloudwatchloggingconfiguration
            '''
            result = self._values.get("cloud_watch_logging_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.CloudWatchLoggingConfigurationProperty"]], result)

        @builtins.property
        def managed_persistence_monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ManagedPersistenceMonitoringConfigurationProperty"]]:
            '''The managed log persistence configuration for a job run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-monitoringconfiguration.html#cfn-emrserverless-application-monitoringconfiguration-managedpersistencemonitoringconfiguration
            '''
            result = self._values.get("managed_persistence_monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ManagedPersistenceMonitoringConfigurationProperty"]], result)

        @builtins.property
        def s3_monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.S3MonitoringConfigurationProperty"]]:
            '''The Amazon S3 configuration for monitoring log publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-monitoringconfiguration.html#cfn-emrserverless-application-monitoringconfiguration-s3monitoringconfiguration
            '''
            result = self._values.get("s3_monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.S3MonitoringConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The network configuration for customer VPC connectivity.

            :param security_group_ids: The array of security group Ids for customer VPC connectivity.
            :param subnet_ids: The array of subnet Ids for customer VPC connectivity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                network_configuration_property = emrserverless.CfnApplication.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ea91d44b7b04faaf86e4a55badd0f26aa73aa5b6fa131753a02f8571914cda73)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The array of security group Ids for customer VPC connectivity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html#cfn-emrserverless-application-networkconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The array of subnet Ids for customer VPC connectivity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html#cfn-emrserverless-application-networkconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.S3MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_key_arn": "encryptionKeyArn", "log_uri": "logUri"},
    )
    class S3MonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_key_arn: typing.Optional[builtins.str] = None,
            log_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Amazon S3 configuration for monitoring log publishing.

            You can configure your jobs to send log information to Amazon S3.

            :param encryption_key_arn: The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.
            :param log_uri: The Amazon S3 destination URI for log publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-s3monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                s3_monitoring_configuration_property = emrserverless.CfnApplication.S3MonitoringConfigurationProperty(
                    encryption_key_arn="encryptionKeyArn",
                    log_uri="logUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c2bbffaec906451dfb8b186ca2e714bc8b38325018a5241dbe3a66e4202ffed)
                check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
                check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption_key_arn is not None:
                self._values["encryption_key_arn"] = encryption_key_arn
            if log_uri is not None:
                self._values["log_uri"] = log_uri

        @builtins.property
        def encryption_key_arn(self) -> typing.Optional[builtins.str]:
            '''The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-s3monitoringconfiguration.html#cfn-emrserverless-application-s3monitoringconfiguration-encryptionkeyarn
            '''
            result = self._values.get("encryption_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_uri(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 destination URI for log publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-s3monitoringconfiguration.html#cfn-emrserverless-application-s3monitoringconfiguration-loguri
            '''
            result = self._values.get("log_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.WorkerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu": "cpu", "memory": "memory", "disk": "disk"},
    )
    class WorkerConfigurationProperty:
        def __init__(
            self,
            *,
            cpu: builtins.str,
            memory: builtins.str,
            disk: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
            :param memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
            :param disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                worker_configuration_property = emrserverless.CfnApplication.WorkerConfigurationProperty(
                    cpu="cpu",
                    memory="memory",
                
                    # the properties below are optional
                    disk="disk"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ba87e32273a791ef8b805baf4bc9f2673318df79033c83263f0a9b3385f35de9)
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
                check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cpu": cpu,
                "memory": memory,
            }
            if disk is not None:
                self._values["disk"] = disk

        @builtins.property
        def cpu(self) -> builtins.str:
            '''Per worker CPU resource.

            vCPU is the only supported unit and specifying vCPU is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-cpu
            '''
            result = self._values.get("cpu")
            assert result is not None, "Required property 'cpu' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def memory(self) -> builtins.str:
            '''Per worker memory resource.

            GB is the only supported unit and specifying GB is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-memory
            '''
            result = self._values.get("memory")
            assert result is not None, "Required property 'memory' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def disk(self) -> typing.Optional[builtins.str]:
            '''Per worker Disk resource.

            GB is the only supported unit and specifying GB is optional

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-disk
            '''
            result = self._values.get("disk")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplication.WorkerTypeSpecificationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"image_configuration": "imageConfiguration"},
    )
    class WorkerTypeSpecificationInputProperty:
        def __init__(
            self,
            *,
            image_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.ImageConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The specifications for a worker type.

            :param image_configuration: The image configuration for a worker type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workertypespecificationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrserverless as emrserverless
                
                worker_type_specification_input_property = emrserverless.CfnApplication.WorkerTypeSpecificationInputProperty(
                    image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                        image_uri="imageUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf3faf2221f3ef2b1688f533b0a19ec0f76d5323103fca031607fc17f89bbd0c)
                check_type(argname="argument image_configuration", value=image_configuration, expected_type=type_hints["image_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_configuration is not None:
                self._values["image_configuration"] = image_configuration

        @builtins.property
        def image_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ImageConfigurationInputProperty"]]:
            '''The image configuration for a worker type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workertypespecificationinput.html#cfn-emrserverless-application-workertypespecificationinput-imageconfiguration
            '''
            result = self._values.get("image_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ImageConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkerTypeSpecificationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrserverless.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "release_label": "releaseLabel",
        "type": "type",
        "architecture": "architecture",
        "auto_start_configuration": "autoStartConfiguration",
        "auto_stop_configuration": "autoStopConfiguration",
        "image_configuration": "imageConfiguration",
        "initial_capacity": "initialCapacity",
        "maximum_capacity": "maximumCapacity",
        "monitoring_configuration": "monitoringConfiguration",
        "name": "name",
        "network_configuration": "networkConfiguration",
        "runtime_configuration": "runtimeConfiguration",
        "tags": "tags",
        "worker_type_specifications": "workerTypeSpecifications",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        release_label: builtins.str,
        type: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
        auto_start_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoStartConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        auto_stop_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoStopConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ImageConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        initial_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        maximum_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.MaximumAllowedResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ConfigurationObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        worker_type_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param release_label: The EMR release associated with the application.
        :param type: The type of application, such as Spark or Hive.
        :param architecture: The CPU architecture of an application.
        :param auto_start_configuration: The configuration for an application to automatically start on job submission.
        :param auto_stop_configuration: The configuration for an application to automatically stop after a certain amount of time being idle.
        :param image_configuration: The image configuration applied to all worker types.
        :param initial_capacity: The initial capacity of the application.
        :param maximum_capacity: The maximum capacity of the application. This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.
        :param monitoring_configuration: A configuration specification to be used when provisioning an application. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.
        :param name: The name of the application.
        :param network_configuration: The network configuration for customer VPC connectivity for the application.
        :param runtime_configuration: The `Configuration <https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html>`_ specifications of an application. Each configuration consists of a classification and properties. You use this parameter when creating or updating an application. To see the runtimeConfiguration object of an application, run the `GetApplication <https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html>`_ API operation.
        :param tags: The tags assigned to the application.
        :param worker_type_specifications: The specification applied to each worker type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrserverless as emrserverless
            
            # configuration_object_property_: emrserverless.CfnApplication.ConfigurationObjectProperty
            
            cfn_application_props = emrserverless.CfnApplicationProps(
                release_label="releaseLabel",
                type="type",
            
                # the properties below are optional
                architecture="architecture",
                auto_start_configuration=emrserverless.CfnApplication.AutoStartConfigurationProperty(
                    enabled=False
                ),
                auto_stop_configuration=emrserverless.CfnApplication.AutoStopConfigurationProperty(
                    enabled=False,
                    idle_timeout_minutes=123
                ),
                image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                    image_uri="imageUri"
                ),
                initial_capacity=[emrserverless.CfnApplication.InitialCapacityConfigKeyValuePairProperty(
                    key="key",
                    value=emrserverless.CfnApplication.InitialCapacityConfigProperty(
                        worker_configuration=emrserverless.CfnApplication.WorkerConfigurationProperty(
                            cpu="cpu",
                            memory="memory",
            
                            # the properties below are optional
                            disk="disk"
                        ),
                        worker_count=123
                    )
                )],
                maximum_capacity=emrserverless.CfnApplication.MaximumAllowedResourcesProperty(
                    cpu="cpu",
                    memory="memory",
            
                    # the properties below are optional
                    disk="disk"
                ),
                monitoring_configuration=emrserverless.CfnApplication.MonitoringConfigurationProperty(
                    cloud_watch_logging_configuration=emrserverless.CfnApplication.CloudWatchLoggingConfigurationProperty(
                        enabled=False,
                        encryption_key_arn="encryptionKeyArn",
                        log_group_name="logGroupName",
                        log_stream_name_prefix="logStreamNamePrefix",
                        log_type_map=[emrserverless.CfnApplication.LogTypeMapKeyValuePairProperty(
                            key="key",
                            value=["value"]
                        )]
                    ),
                    managed_persistence_monitoring_configuration=emrserverless.CfnApplication.ManagedPersistenceMonitoringConfigurationProperty(
                        enabled=False,
                        encryption_key_arn="encryptionKeyArn"
                    ),
                    s3_monitoring_configuration=emrserverless.CfnApplication.S3MonitoringConfigurationProperty(
                        encryption_key_arn="encryptionKeyArn",
                        log_uri="logUri"
                    )
                ),
                name="name",
                network_configuration=emrserverless.CfnApplication.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                ),
                runtime_configuration=[emrserverless.CfnApplication.ConfigurationObjectProperty(
                    classification="classification",
            
                    # the properties below are optional
                    configurations=[configuration_object_property_],
                    properties={
                        "properties_key": "properties"
                    }
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                worker_type_specifications={
                    "worker_type_specifications_key": emrserverless.CfnApplication.WorkerTypeSpecificationInputProperty(
                        image_configuration=emrserverless.CfnApplication.ImageConfigurationInputProperty(
                            image_uri="imageUri"
                        )
                    )
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3151e77334ffa97e03663b371e17d90f7842dc4da33dee36252fd84d1ee92ba)
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument auto_start_configuration", value=auto_start_configuration, expected_type=type_hints["auto_start_configuration"])
            check_type(argname="argument auto_stop_configuration", value=auto_stop_configuration, expected_type=type_hints["auto_stop_configuration"])
            check_type(argname="argument image_configuration", value=image_configuration, expected_type=type_hints["image_configuration"])
            check_type(argname="argument initial_capacity", value=initial_capacity, expected_type=type_hints["initial_capacity"])
            check_type(argname="argument maximum_capacity", value=maximum_capacity, expected_type=type_hints["maximum_capacity"])
            check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument runtime_configuration", value=runtime_configuration, expected_type=type_hints["runtime_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument worker_type_specifications", value=worker_type_specifications, expected_type=type_hints["worker_type_specifications"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "release_label": release_label,
            "type": type,
        }
        if architecture is not None:
            self._values["architecture"] = architecture
        if auto_start_configuration is not None:
            self._values["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            self._values["auto_stop_configuration"] = auto_stop_configuration
        if image_configuration is not None:
            self._values["image_configuration"] = image_configuration
        if initial_capacity is not None:
            self._values["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            self._values["maximum_capacity"] = maximum_capacity
        if monitoring_configuration is not None:
            self._values["monitoring_configuration"] = monitoring_configuration
        if name is not None:
            self._values["name"] = name
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if runtime_configuration is not None:
            self._values["runtime_configuration"] = runtime_configuration
        if tags is not None:
            self._values["tags"] = tags
        if worker_type_specifications is not None:
            self._values["worker_type_specifications"] = worker_type_specifications

    @builtins.property
    def release_label(self) -> builtins.str:
        '''The EMR release associated with the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-releaselabel
        '''
        result = self._values.get("release_label")
        assert result is not None, "Required property 'release_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of application, such as Spark or Hive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def architecture(self) -> typing.Optional[builtins.str]:
        '''The CPU architecture of an application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-architecture
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_start_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoStartConfigurationProperty]]:
        '''The configuration for an application to automatically start on job submission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-autostartconfiguration
        '''
        result = self._values.get("auto_start_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoStartConfigurationProperty]], result)

    @builtins.property
    def auto_stop_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoStopConfigurationProperty]]:
        '''The configuration for an application to automatically stop after a certain amount of time being idle.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-autostopconfiguration
        '''
        result = self._values.get("auto_stop_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoStopConfigurationProperty]], result)

    @builtins.property
    def image_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ImageConfigurationInputProperty]]:
        '''The image configuration applied to all worker types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-imageconfiguration
        '''
        result = self._values.get("image_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ImageConfigurationInputProperty]], result)

    @builtins.property
    def initial_capacity(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.InitialCapacityConfigKeyValuePairProperty]]]]:
        '''The initial capacity of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-initialcapacity
        '''
        result = self._values.get("initial_capacity")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.InitialCapacityConfigKeyValuePairProperty]]]], result)

    @builtins.property
    def maximum_capacity(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.MaximumAllowedResourcesProperty]]:
        '''The maximum capacity of the application.

        This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-maximumcapacity
        '''
        result = self._values.get("maximum_capacity")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.MaximumAllowedResourcesProperty]], result)

    @builtins.property
    def monitoring_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.MonitoringConfigurationProperty]]:
        '''A configuration specification to be used when provisioning an application.

        A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-monitoringconfiguration
        '''
        result = self._values.get("monitoring_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.MonitoringConfigurationProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.NetworkConfigurationProperty]]:
        '''The network configuration for customer VPC connectivity for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.NetworkConfigurationProperty]], result)

    @builtins.property
    def runtime_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.ConfigurationObjectProperty]]]]:
        '''The `Configuration <https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html>`_ specifications of an application. Each configuration consists of a classification and properties. You use this parameter when creating or updating an application. To see the runtimeConfiguration object of an application, run the `GetApplication <https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html>`_ API operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-runtimeconfiguration
        '''
        result = self._values.get("runtime_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.ConfigurationObjectProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def worker_type_specifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnApplication.WorkerTypeSpecificationInputProperty]]]]:
        '''The specification applied to each worker type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-workertypespecifications
        '''
        result = self._values.get("worker_type_specifications")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnApplication.WorkerTypeSpecificationInputProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
]

publication.publish()

def _typecheckingstub__73910249d55cbd2983a3ea1bb4666acedb0e3e84df9686bbdeecd191b5ae6373(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    release_label: builtins.str,
    type: builtins.str,
    architecture: typing.Optional[builtins.str] = None,
    auto_start_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoStartConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_stop_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoStopConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ImageConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    initial_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    maximum_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.MaximumAllowedResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ConfigurationObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_type_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffb07c3ee5bcef7cdea2376c768ef28e4be2a5ff1b3d59792805560edbc23a53(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe1c41fe06697b2d8c071c7eb2680f90736a7d5e873109e23c86cfa1bdcce8c9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ddb97a434bd94c3f60161a520cb237aed52648f4fcaf12da72c9a88137afdae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f57e27e169be5182ad6ebed2fc50b72e6470752b0d5d5454c1d9b23bfaeaf18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2273d6ae79032b2ac60c651e12d059c9c2d80c06c7391dab5fed7dd019ef2f8d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__250efc466f983b8a885240945cba35864cbd2a6767d45f9c36fd1d25d01092c1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoStartConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1b3d83107f5e408234e2bfc84b1e4ecd5f468b8f46ba51ddf116c1b97908f3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoStopConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__368a96aa7c6ff916676fe29b5a922fae846a89a5edbb8c71b20a5d60107bff71(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ImageConfigurationInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3bfbe46861fe91b5e1b2fe0373abb6e5b5f46147bf7eb286264343039f5b04(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.InitialCapacityConfigKeyValuePairProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358e38959731258abe08d7ec2ddde30c2f91167a5e3a6ed66750a800db2cf6b2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.MaximumAllowedResourcesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9899534798dfa06d9a764edbb0466853de6132045ef162d2e77c6ee2692e88ab(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.MonitoringConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ae684b6a8f75a4ea6b60c08ad238517e03708361aa167abbbe2c94dc5bb9d6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c89ab319e8ae68523a39499d53338babf76d8a1fa439e7e46c3daeacb28a4bc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.NetworkConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8009c989bc781626fbf3067531c118d2a94649c7cd583ee7c5604a168e732dfa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.ConfigurationObjectProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c62e07950c8c2fa752bd4e5ac938292f2380eb4b2fc5d19d5f5a2a46e5fc39aa(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04bd95d4e436eaf679b9831515cb5d2d9cce5c8686b56c55065b2b99bd9660ea(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnApplication.WorkerTypeSpecificationInputProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3408c1d905295731e672b4fc518643f3fe70d0851e610b36fc4f060f52d01567(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__962238425f6319f997d9db8d2fd1983e29503aa305579b2aeaee5d7d36e0e2fb(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    idle_timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec71ff6297cc71f2d7e9773aafa9436f445613d427eec9083528cb272b7968c4(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name_prefix: typing.Optional[builtins.str] = None,
    log_type_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.LogTypeMapKeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6631f05a0f985523b64829ba85bb2686c8aecd114d8a1c04c994338ec0f0718(
    *,
    classification: builtins.str,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ConfigurationObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f60138497ea02d9962f5b33612a58874538452fcad71efafe327c8dd4b46ee62(
    *,
    image_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a670fb912d740316bb84ff842e2f70b20b264127e994454037f69be3f399f68(
    *,
    key: builtins.str,
    value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.InitialCapacityConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48da54ce8c9f1ee4240ad6b62d8fe9b0e060a955f7cbba04cae2f1fbd25cfcfd(
    *,
    worker_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.WorkerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    worker_count: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11de2a1a9a00f1d9b3a16e41746ea3d40e8b57bb6d0cb6b83bd8e3eddf86ff71(
    *,
    key: builtins.str,
    value: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8787c60c8f797aeb97be0765739b01f867e4756173c68e36db977bef73482c2a(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536f69d7e03464181452f489bfb1c04d11b8e8a746a0015b74730a948e1f7189(
    *,
    cpu: builtins.str,
    memory: builtins.str,
    disk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac64b7b17b97bdc5b470cb32b1b0c00b3bdd7d97ea83ace7e59e5eb7f78d59e6(
    *,
    cloud_watch_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.CloudWatchLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_persistence_monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ManagedPersistenceMonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.S3MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea91d44b7b04faaf86e4a55badd0f26aa73aa5b6fa131753a02f8571914cda73(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c2bbffaec906451dfb8b186ca2e714bc8b38325018a5241dbe3a66e4202ffed(
    *,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    log_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba87e32273a791ef8b805baf4bc9f2673318df79033c83263f0a9b3385f35de9(
    *,
    cpu: builtins.str,
    memory: builtins.str,
    disk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf3faf2221f3ef2b1688f533b0a19ec0f76d5323103fca031607fc17f89bbd0c(
    *,
    image_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ImageConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3151e77334ffa97e03663b371e17d90f7842dc4da33dee36252fd84d1ee92ba(
    *,
    release_label: builtins.str,
    type: builtins.str,
    architecture: typing.Optional[builtins.str] = None,
    auto_start_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoStartConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_stop_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoStopConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ImageConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    initial_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.InitialCapacityConfigKeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    maximum_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.MaximumAllowedResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ConfigurationObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_type_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.WorkerTypeSpecificationInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
