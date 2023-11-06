'''
# Amazon GuardDuty Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_guardduty as guardduty
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for GuardDuty construct libraries](https://constructs.dev/search?q=guardduty)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::GuardDuty resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GuardDuty.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GuardDuty](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GuardDuty.html).

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
class CfnDetector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector",
):
    '''The ``AWS::GuardDuty::Detector`` resource specifies a new GuardDuty detector.

    A detector is an object that represents the GuardDuty service. A detector is required for GuardDuty to become operational.

    Make sure you use either ``DataSources`` or ``Features`` in a one request, and not both.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_detector = guardduty.CfnDetector(self, "MyCfnDetector",
            enable=False,
        
            # the properties below are optional
            data_sources=guardduty.CfnDetector.CFNDataSourceConfigurationsProperty(
                kubernetes=guardduty.CfnDetector.CFNKubernetesConfigurationProperty(
                    audit_logs=guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                        enable=False
                    )
                ),
                malware_protection=guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty(
                    scan_ec2_instance_with_findings=guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                        ebs_volumes=False
                    )
                ),
                s3_logs=guardduty.CfnDetector.CFNS3LogsConfigurationProperty(
                    enable=False
                )
            ),
            features=[guardduty.CfnDetector.FeatureConfigurationsProperty(
                additional_configuration=[guardduty.CfnDetector.FeatureAdditionalConfigurationProperty(
                    name="name",
                    status="status"
                )],
                name="name",
                status="status"
            )],
            finding_publishing_frequency="findingPublishingFrequency",
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
        enable: typing.Union[builtins.bool, _IResolvable_da3f097b],
        data_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.CFNDataSourceConfigurationsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        features: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.FeatureConfigurationsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param enable: Specifies whether the detector is to be enabled on creation.
        :param data_sources: Describes which data sources will be enabled for the detector.
        :param features: A list of features that will be configured for the detector.
        :param finding_publishing_frequency: Specifies how frequently updated findings are exported.
        :param tags: Specifies tags added to a new detector resource. Each tag consists of a key and an optional value, both of which you define. Currently, support is available only for creating and deleting a tag. No support exists for updating the tags. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4374e73b5cd2e2814bd72eb21f29547df6146e023d23ee6d5c8c8cdb4439473)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDetectorProps(
            enable=enable,
            data_sources=data_sources,
            features=features,
            finding_publishing_frequency=finding_publishing_frequency,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd13133d47f23bb91dcc2e425b360777bcd306422761af023eb8654fdc89892)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7db5a3aaacc92cdd47629478cb9f2db842f4bfb46e4ac877d9368e545bf7ab3a)
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
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Specifies whether the detector is to be enabled on creation.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, _IResolvable_da3f097b]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be1c4208def5e29bff60511511974687c29f282d57c3bb461675543b67475958)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="dataSources")
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNDataSourceConfigurationsProperty"]]:
        '''Describes which data sources will be enabled for the detector.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNDataSourceConfigurationsProperty"]], jsii.get(self, "dataSources"))

    @data_sources.setter
    def data_sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNDataSourceConfigurationsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d984644fe0d5555f018ae12b1bfbb1e875501438854ca50d249d3cd6091178f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSources", value)

    @builtins.property
    @jsii.member(jsii_name="features")
    def features(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.FeatureConfigurationsProperty"]]]]:
        '''A list of features that will be configured for the detector.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.FeatureConfigurationsProperty"]]]], jsii.get(self, "features"))

    @features.setter
    def features(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.FeatureConfigurationsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d162426268bf9dc8b5f3efea1e4d49418ad72947ae8c15de703212246d36f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "features", value)

    @builtins.property
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''Specifies how frequently updated findings are exported.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "findingPublishingFrequency"))

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05a15130d3f8d159abcddfb10123f12bf70fc091e86be777252ab49ab86dd84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingPublishingFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies tags added to a new detector resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__273b490c75e93f137bcaf4b10d4df89064d16e78f021b92c6008b18c9c74e99c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNDataSourceConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kubernetes": "kubernetes",
            "malware_protection": "malwareProtection",
            "s3_logs": "s3Logs",
        },
    )
    class CFNDataSourceConfigurationsProperty:
        def __init__(
            self,
            *,
            kubernetes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.CFNKubernetesConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            malware_protection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.CFNMalwareProtectionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.CFNS3LogsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes whether S3 data event logs, Kubernetes audit logs, or Malware Protection will be enabled as a data source when the detector is created.

            :param kubernetes: Describes which Kubernetes data sources are enabled for a detector.
            :param malware_protection: Describes whether Malware Protection will be enabled as a data source.
            :param s3_logs: Describes whether S3 data event logs are enabled as a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNData_source_configurations_property = guardduty.CfnDetector.CFNDataSourceConfigurationsProperty(
                    kubernetes=guardduty.CfnDetector.CFNKubernetesConfigurationProperty(
                        audit_logs=guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                            enable=False
                        )
                    ),
                    malware_protection=guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty(
                        scan_ec2_instance_with_findings=guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                            ebs_volumes=False
                        )
                    ),
                    s3_logs=guardduty.CfnDetector.CFNS3LogsConfigurationProperty(
                        enable=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cc6f5e6dd89fc0d30f28179b1bc893366d4b68b6eff35d1ed195ef95ea96270)
                check_type(argname="argument kubernetes", value=kubernetes, expected_type=type_hints["kubernetes"])
                check_type(argname="argument malware_protection", value=malware_protection, expected_type=type_hints["malware_protection"])
                check_type(argname="argument s3_logs", value=s3_logs, expected_type=type_hints["s3_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kubernetes is not None:
                self._values["kubernetes"] = kubernetes
            if malware_protection is not None:
                self._values["malware_protection"] = malware_protection
            if s3_logs is not None:
                self._values["s3_logs"] = s3_logs

        @builtins.property
        def kubernetes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNKubernetesConfigurationProperty"]]:
            '''Describes which Kubernetes data sources are enabled for a detector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-kubernetes
            '''
            result = self._values.get("kubernetes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNKubernetesConfigurationProperty"]], result)

        @builtins.property
        def malware_protection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNMalwareProtectionConfigurationProperty"]]:
            '''Describes whether Malware Protection will be enabled as a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-malwareprotection
            '''
            result = self._values.get("malware_protection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNMalwareProtectionConfigurationProperty"]], result)

        @builtins.property
        def s3_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNS3LogsConfigurationProperty"]]:
            '''Describes whether S3 data event logs are enabled as a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-s3logs
            '''
            result = self._values.get("s3_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNS3LogsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNDataSourceConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enable": "enable"},
    )
    class CFNKubernetesAuditLogsConfigurationProperty:
        def __init__(
            self,
            *,
            enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes which optional data sources are enabled for a detector.

            :param enable: Describes whether Kubernetes audit logs are enabled as a data source for the detector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNKubernetes_audit_logs_configuration_property = guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                    enable=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91a0cf3d36fd260bda8fbf7c652e71e3282b0a3867b477f0b4e992be46f9e9fc)
                check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable is not None:
                self._values["enable"] = enable

        @builtins.property
        def enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Describes whether Kubernetes audit logs are enabled as a data source for the detector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html#cfn-guardduty-detector-cfnkubernetesauditlogsconfiguration-enable
            '''
            result = self._values.get("enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNKubernetesAuditLogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNKubernetesConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"audit_logs": "auditLogs"},
    )
    class CFNKubernetesConfigurationProperty:
        def __init__(
            self,
            *,
            audit_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.CFNKubernetesAuditLogsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes which Kubernetes protection data sources are enabled for the detector.

            :param audit_logs: Describes whether Kubernetes audit logs are enabled as a data source for the detector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNKubernetes_configuration_property = guardduty.CfnDetector.CFNKubernetesConfigurationProperty(
                    audit_logs=guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                        enable=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__507c730ce77749f55565236ae0e0949766ee63b4e28eddebc38a59384af159d1)
                check_type(argname="argument audit_logs", value=audit_logs, expected_type=type_hints["audit_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audit_logs is not None:
                self._values["audit_logs"] = audit_logs

        @builtins.property
        def audit_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNKubernetesAuditLogsConfigurationProperty"]]:
            '''Describes whether Kubernetes audit logs are enabled as a data source for the detector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesconfiguration.html#cfn-guardduty-detector-cfnkubernetesconfiguration-auditlogs
            '''
            result = self._values.get("audit_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNKubernetesAuditLogsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNKubernetesConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scan_ec2_instance_with_findings": "scanEc2InstanceWithFindings",
        },
    )
    class CFNMalwareProtectionConfigurationProperty:
        def __init__(
            self,
            *,
            scan_ec2_instance_with_findings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes whether Malware Protection will be enabled as a data source.

            :param scan_ec2_instance_with_findings: Describes the configuration of Malware Protection for EC2 instances with findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnmalwareprotectionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNMalware_protection_configuration_property = guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty(
                    scan_ec2_instance_with_findings=guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                        ebs_volumes=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b489755354068d624ff07c4dbcaacb69f242db268771504faaf7ec08d1fa7b11)
                check_type(argname="argument scan_ec2_instance_with_findings", value=scan_ec2_instance_with_findings, expected_type=type_hints["scan_ec2_instance_with_findings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if scan_ec2_instance_with_findings is not None:
                self._values["scan_ec2_instance_with_findings"] = scan_ec2_instance_with_findings

        @builtins.property
        def scan_ec2_instance_with_findings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty"]]:
            '''Describes the configuration of Malware Protection for EC2 instances with findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnmalwareprotectionconfiguration.html#cfn-guardduty-detector-cfnmalwareprotectionconfiguration-scanec2instancewithfindings
            '''
            result = self._values.get("scan_ec2_instance_with_findings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNMalwareProtectionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNS3LogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enable": "enable"},
    )
    class CFNS3LogsConfigurationProperty:
        def __init__(
            self,
            *,
            enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes whether S3 data event logs will be enabled as a data source when the detector is created.

            :param enable: The status of S3 data event logs as a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNS3_logs_configuration_property = guardduty.CfnDetector.CFNS3LogsConfigurationProperty(
                    enable=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__273397d5fa0880c36c6aca40485efece77caba905c5a76cf0e055b3125298f05)
                check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable is not None:
                self._values["enable"] = enable

        @builtins.property
        def enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The status of S3 data event logs as a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html#cfn-guardduty-detector-cfns3logsconfiguration-enable
            '''
            result = self._values.get("enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNS3LogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"ebs_volumes": "ebsVolumes"},
    )
    class CFNScanEc2InstanceWithFindingsConfigurationProperty:
        def __init__(
            self,
            *,
            ebs_volumes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes whether Malware Protection for EC2 instances with findings will be enabled as a data source.

            :param ebs_volumes: Describes the configuration for scanning EBS volumes as data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnscanec2instancewithfindingsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                c_fNScan_ec2_instance_with_findings_configuration_property = guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                    ebs_volumes=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f726c6703e77466e481c466dc3d2680cf3ce31a2bfc0af08fdc3570849efb55a)
                check_type(argname="argument ebs_volumes", value=ebs_volumes, expected_type=type_hints["ebs_volumes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ebs_volumes is not None:
                self._values["ebs_volumes"] = ebs_volumes

        @builtins.property
        def ebs_volumes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Describes the configuration for scanning EBS volumes as data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnscanec2instancewithfindingsconfiguration.html#cfn-guardduty-detector-cfnscanec2instancewithfindingsconfiguration-ebsvolumes
            '''
            result = self._values.get("ebs_volumes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNScanEc2InstanceWithFindingsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.FeatureAdditionalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "status": "status"},
    )
    class FeatureAdditionalConfigurationProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the additional configuration for a feature.

            If you want to specify any additional configuration for your feature, it is required to provide the ``Name`` and ``Status`` for that additional configuration. For more information, see `DetectorAdditionalConfiguration <https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorAdditionalConfiguration.html>`_ .

            If you're providing additional configuration, ensure to provide the corresponding `FeatureConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-featureconfigurations.html#cfn-guardduty-detector-featureconfigurations-additionalconfiguration>`_ .

            :param name: Name of the additional configuration of a feature.
            :param status: Status of the additional configuration of a feature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-featureadditionalconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                feature_additional_configuration_property = guardduty.CfnDetector.FeatureAdditionalConfigurationProperty(
                    name="name",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb1d313a0a14310f6b849190dee89a2da63dae70d22f924dc5da548f75272d58)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the additional configuration of a feature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-featureadditionalconfiguration.html#cfn-guardduty-detector-featureadditionalconfiguration-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Status of the additional configuration of a feature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-featureadditionalconfiguration.html#cfn-guardduty-detector-featureadditionalconfiguration-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FeatureAdditionalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnDetector.FeatureConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_configuration": "additionalConfiguration",
            "name": "name",
            "status": "status",
        },
    )
    class FeatureConfigurationsProperty:
        def __init__(
            self,
            *,
            additional_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.FeatureAdditionalConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            name: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration for a feature.

            Although the ``Required`` field associated with the following properties specifies ``No`` , if you provide information for ``Name`` , you will need to provide the information for ``Status`` too. For information about the available feature configurations, see `DetectorFeatureConfiguration <https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorFeatureConfiguration.html>`_ .

            :param additional_configuration: Additional configuration of the feature.
            :param name: Name of the feature.
            :param status: Status of the feature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-featureconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                feature_configurations_property = guardduty.CfnDetector.FeatureConfigurationsProperty(
                    additional_configuration=[guardduty.CfnDetector.FeatureAdditionalConfigurationProperty(
                        name="name",
                        status="status"
                    )],
                    name="name",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f95505a43158b2ecb934d0eda3be9e00ddd25a7f5ec93e48b5a2ca2bcd6addf)
                check_type(argname="argument additional_configuration", value=additional_configuration, expected_type=type_hints["additional_configuration"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if additional_configuration is not None:
                self._values["additional_configuration"] = additional_configuration
            if name is not None:
                self._values["name"] = name
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def additional_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.FeatureAdditionalConfigurationProperty"]]]]:
            '''Additional configuration of the feature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-featureconfigurations.html#cfn-guardduty-detector-featureconfigurations-additionalconfiguration
            '''
            result = self._values.get("additional_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.FeatureAdditionalConfigurationProperty"]]]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the feature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-featureconfigurations.html#cfn-guardduty-detector-featureconfigurations-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Status of the feature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-featureconfigurations.html#cfn-guardduty-detector-featureconfigurations-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FeatureConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "enable": "enable",
        "data_sources": "dataSources",
        "features": "features",
        "finding_publishing_frequency": "findingPublishingFrequency",
        "tags": "tags",
    },
)
class CfnDetectorProps:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, _IResolvable_da3f097b],
        data_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.CFNDataSourceConfigurationsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        features: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.FeatureConfigurationsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDetector``.

        :param enable: Specifies whether the detector is to be enabled on creation.
        :param data_sources: Describes which data sources will be enabled for the detector.
        :param features: A list of features that will be configured for the detector.
        :param finding_publishing_frequency: Specifies how frequently updated findings are exported.
        :param tags: Specifies tags added to a new detector resource. Each tag consists of a key and an optional value, both of which you define. Currently, support is available only for creating and deleting a tag. No support exists for updating the tags. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_detector_props = guardduty.CfnDetectorProps(
                enable=False,
            
                # the properties below are optional
                data_sources=guardduty.CfnDetector.CFNDataSourceConfigurationsProperty(
                    kubernetes=guardduty.CfnDetector.CFNKubernetesConfigurationProperty(
                        audit_logs=guardduty.CfnDetector.CFNKubernetesAuditLogsConfigurationProperty(
                            enable=False
                        )
                    ),
                    malware_protection=guardduty.CfnDetector.CFNMalwareProtectionConfigurationProperty(
                        scan_ec2_instance_with_findings=guardduty.CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty(
                            ebs_volumes=False
                        )
                    ),
                    s3_logs=guardduty.CfnDetector.CFNS3LogsConfigurationProperty(
                        enable=False
                    )
                ),
                features=[guardduty.CfnDetector.FeatureConfigurationsProperty(
                    additional_configuration=[guardduty.CfnDetector.FeatureAdditionalConfigurationProperty(
                        name="name",
                        status="status"
                    )],
                    name="name",
                    status="status"
                )],
                finding_publishing_frequency="findingPublishingFrequency",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3914f92ec13130f6437ebb8077c96e2e1592d547cc445617fe4957f629b5cb3c)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument data_sources", value=data_sources, expected_type=type_hints["data_sources"])
            check_type(argname="argument features", value=features, expected_type=type_hints["features"])
            check_type(argname="argument finding_publishing_frequency", value=finding_publishing_frequency, expected_type=type_hints["finding_publishing_frequency"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enable": enable,
        }
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if features is not None:
            self._values["features"] = features
        if finding_publishing_frequency is not None:
            self._values["finding_publishing_frequency"] = finding_publishing_frequency
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Specifies whether the detector is to be enabled on creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
        '''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDetector.CFNDataSourceConfigurationsProperty]]:
        '''Describes which data sources will be enabled for the detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-datasources
        '''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDetector.CFNDataSourceConfigurationsProperty]], result)

    @builtins.property
    def features(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.FeatureConfigurationsProperty]]]]:
        '''A list of features that will be configured for the detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-features
        '''
        result = self._values.get("features")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.FeatureConfigurationsProperty]]]], result)

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''Specifies how frequently updated findings are exported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
        '''
        result = self._values.get("finding_publishing_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies tags added to a new detector resource.

        Each tag consists of a key and an optional value, both of which you define.

        Currently, support is available only for creating and deleting a tag. No support exists for updating the tags.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnFilter",
):
    '''The ``AWS::GuardDuty::Filter`` resource specifies a new filter defined by the provided ``findingCriteria`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        # criterion: Any
        
        cfn_filter = guardduty.CfnFilter(self, "MyCfnFilter",
            action="action",
            description="description",
            detector_id="detectorId",
            finding_criteria=guardduty.CfnFilter.FindingCriteriaProperty(
                criterion=criterion,
                item_type=guardduty.CfnFilter.ConditionProperty(
                    eq=["eq"],
                    equal_to=["equalTo"],
                    greater_than=123,
                    greater_than_or_equal=123,
                    gt=123,
                    gte=123,
                    less_than=123,
                    less_than_or_equal=123,
                    lt=123,
                    lte=123,
                    neq=["neq"],
                    not_equals=["notEquals"]
                )
            ),
            name="name",
            rank=123,
        
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
        action: builtins.str,
        description: builtins.str,
        detector_id: builtins.str,
        finding_criteria: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.FindingCriteriaProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        rank: jsii.Number,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action: Specifies the action that is to be applied to the findings that match the filter.
        :param description: The description of the filter. Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses ( ``{ }`` , ``[ ]`` , and ``( )`` ), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.
        :param detector_id: The ID of the detector belonging to the GuardDuty account that you want to create a filter for.
        :param finding_criteria: Represents the criteria to be used in the filter for querying findings.
        :param name: The name of the filter. Valid characters include period (.), underscore (_), dash (-), and alphanumeric characters. A whitespace is considered to be an invalid character.
        :param rank: Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings. The minimum value for this property is 1 and the maximum is 100. By default, filters may not be created in the same order as they are ranked. To ensure that the filters are created in the expected order, you can use an optional attribute, `DependsOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ , with the following syntax: ``"DependsOn":[ "ObjectName" ]`` .
        :param tags: The tags to be added to a new filter resource. Each tag consists of a key and an optional value, both of which you define. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__067e85819bdb865e6337a26c378c0472fa2b9e72f47dfccf0bca609928a7aea7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFilterProps(
            action=action,
            description=description,
            detector_id=detector_id,
            finding_criteria=finding_criteria,
            name=name,
            rank=rank,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44aa41d511d84a4f9e1672f1bbcbf9db9da6c8367d7cad9ea6f0e30d51c4edc1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d00911f9ef1cc2770fa371850c170d11fa5dae6c49195efa6eedf0ecc147d436)
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
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        '''Specifies the action that is to be applied to the findings that match the filter.'''
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48a346a5915bdb2f2af2271886d8088c817fdc4bbf7e9f976a58166a6d451959)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the filter.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d76609fcbed2d16e8e3d770136dd8f1d34ef69ecf949487325d62e1df3feba8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The ID of the detector belonging to the GuardDuty account that you want to create a filter for.'''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a940342f0dba5155f5628025cb840051cc96e969cc988dd60f36269d57e2ccd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnFilter.FindingCriteriaProperty"]:
        '''Represents the criteria to be used in the filter for querying findings.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFilter.FindingCriteriaProperty"], jsii.get(self, "findingCriteria"))

    @finding_criteria.setter
    def finding_criteria(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFilter.FindingCriteriaProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fbed2e2e1c4e36b77bef70f5730cf33088965585e081220ea8782f1bc6ec58e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the filter.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a919e4dbcd673724e15009ab41b3a97b27ecfabae06ad4b152e2793162be4ddc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rank")
    def rank(self) -> jsii.Number:
        '''Specifies the position of the filter in the list of current filters.'''
        return typing.cast(jsii.Number, jsii.get(self, "rank"))

    @rank.setter
    def rank(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64d9594f1beac431821c9cffe86b3daf0e0dceaacc9252ecabb10c61e6b89d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rank", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be added to a new filter resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ec0b341923b31034fd13a73457e5a7351149963826be423d3b727494075107d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnFilter.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "eq": "eq",
            "equal_to": "equalTo",
            "greater_than": "greaterThan",
            "greater_than_or_equal": "greaterThanOrEqual",
            "gt": "gt",
            "gte": "gte",
            "less_than": "lessThan",
            "less_than_or_equal": "lessThanOrEqual",
            "lt": "lt",
            "lte": "lte",
            "neq": "neq",
            "not_equals": "notEquals",
        },
    )
    class ConditionProperty:
        def __init__(
            self,
            *,
            eq: typing.Optional[typing.Sequence[builtins.str]] = None,
            equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
            greater_than: typing.Optional[jsii.Number] = None,
            greater_than_or_equal: typing.Optional[jsii.Number] = None,
            gt: typing.Optional[jsii.Number] = None,
            gte: typing.Optional[jsii.Number] = None,
            less_than: typing.Optional[jsii.Number] = None,
            less_than_or_equal: typing.Optional[jsii.Number] = None,
            lt: typing.Optional[jsii.Number] = None,
            lte: typing.Optional[jsii.Number] = None,
            neq: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the condition to apply to a single field when filtering through GuardDuty findings.

            :param eq: Represents the equal condition to apply to a single field when querying for findings.
            :param equal_to: Represents an *equal* ** condition to be applied to a single field when querying for findings.
            :param greater_than: Represents a *greater than* condition to be applied to a single field when querying for findings.
            :param greater_than_or_equal: Represents a *greater than or equal* condition to be applied to a single field when querying for findings.
            :param gt: Represents a *greater than* condition to be applied to a single field when querying for findings.
            :param gte: Represents the greater than or equal condition to apply to a single field when querying for findings.
            :param less_than: Represents a *less than* condition to be applied to a single field when querying for findings.
            :param less_than_or_equal: Represents a *less than or equal* condition to be applied to a single field when querying for findings.
            :param lt: Represents the less than condition to apply to a single field when querying for findings.
            :param lte: Represents the less than or equal condition to apply to a single field when querying for findings.
            :param neq: Represents the not equal condition to apply to a single field when querying for findings.
            :param not_equals: Represents a *not equal* ** condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                condition_property = guardduty.CfnFilter.ConditionProperty(
                    eq=["eq"],
                    equal_to=["equalTo"],
                    greater_than=123,
                    greater_than_or_equal=123,
                    gt=123,
                    gte=123,
                    less_than=123,
                    less_than_or_equal=123,
                    lt=123,
                    lte=123,
                    neq=["neq"],
                    not_equals=["notEquals"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cdf8702ee06c6a6e0f8140afbb047453bd22f56672abb17dbf2127dc944b075d)
                check_type(argname="argument eq", value=eq, expected_type=type_hints["eq"])
                check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
                check_type(argname="argument greater_than", value=greater_than, expected_type=type_hints["greater_than"])
                check_type(argname="argument greater_than_or_equal", value=greater_than_or_equal, expected_type=type_hints["greater_than_or_equal"])
                check_type(argname="argument gt", value=gt, expected_type=type_hints["gt"])
                check_type(argname="argument gte", value=gte, expected_type=type_hints["gte"])
                check_type(argname="argument less_than", value=less_than, expected_type=type_hints["less_than"])
                check_type(argname="argument less_than_or_equal", value=less_than_or_equal, expected_type=type_hints["less_than_or_equal"])
                check_type(argname="argument lt", value=lt, expected_type=type_hints["lt"])
                check_type(argname="argument lte", value=lte, expected_type=type_hints["lte"])
                check_type(argname="argument neq", value=neq, expected_type=type_hints["neq"])
                check_type(argname="argument not_equals", value=not_equals, expected_type=type_hints["not_equals"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if eq is not None:
                self._values["eq"] = eq
            if equal_to is not None:
                self._values["equal_to"] = equal_to
            if greater_than is not None:
                self._values["greater_than"] = greater_than
            if greater_than_or_equal is not None:
                self._values["greater_than_or_equal"] = greater_than_or_equal
            if gt is not None:
                self._values["gt"] = gt
            if gte is not None:
                self._values["gte"] = gte
            if less_than is not None:
                self._values["less_than"] = less_than
            if less_than_or_equal is not None:
                self._values["less_than_or_equal"] = less_than_or_equal
            if lt is not None:
                self._values["lt"] = lt
            if lte is not None:
                self._values["lte"] = lte
            if neq is not None:
                self._values["neq"] = neq
            if not_equals is not None:
                self._values["not_equals"] = not_equals

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents the equal condition to apply to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def equal_to(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents an *equal* ** condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-equals
            '''
            result = self._values.get("equal_to")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def greater_than(self) -> typing.Optional[jsii.Number]:
            '''Represents a *greater than* condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-greaterthan
            '''
            result = self._values.get("greater_than")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def greater_than_or_equal(self) -> typing.Optional[jsii.Number]:
            '''Represents a *greater than or equal* condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-greaterthanorequal
            '''
            result = self._values.get("greater_than_or_equal")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gt(self) -> typing.Optional[jsii.Number]:
            '''Represents a *greater than* condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gt
            '''
            result = self._values.get("gt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gte(self) -> typing.Optional[jsii.Number]:
            '''Represents the greater than or equal condition to apply to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gte
            '''
            result = self._values.get("gte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def less_than(self) -> typing.Optional[jsii.Number]:
            '''Represents a *less than* condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lessthan
            '''
            result = self._values.get("less_than")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def less_than_or_equal(self) -> typing.Optional[jsii.Number]:
            '''Represents a *less than or equal* condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lessthanorequal
            '''
            result = self._values.get("less_than_or_equal")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lt(self) -> typing.Optional[jsii.Number]:
            '''Represents the less than condition to apply to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lt
            '''
            result = self._values.get("lt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lte(self) -> typing.Optional[jsii.Number]:
            '''Represents the less than or equal condition to apply to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lte
            '''
            result = self._values.get("lte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents the not equal condition to apply to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-neq
            '''
            result = self._values.get("neq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_equals(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents a *not equal* ** condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-notequals
            '''
            result = self._values.get("not_equals")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_guardduty.CfnFilter.FindingCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"criterion": "criterion", "item_type": "itemType"},
    )
    class FindingCriteriaProperty:
        def __init__(
            self,
            *,
            criterion: typing.Any = None,
            item_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.ConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Represents a map of finding properties that match specified conditions and values when querying findings.

            :param criterion: Represents a map of finding properties that match specified conditions and values when querying findings. For a mapping of JSON criterion to their console equivalent see `Finding criteria <https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html#filter_criteria>`_ . The following are the available criterion: - accountId - region - confidence - id - resource.accessKeyDetails.accessKeyId - resource.accessKeyDetails.principalId - resource.accessKeyDetails.userName - resource.accessKeyDetails.userType - resource.instanceDetails.iamInstanceProfile.id - resource.instanceDetails.imageId - resource.instanceDetails.instanceId - resource.instanceDetails.outpostArn - resource.instanceDetails.networkInterfaces.ipv6Addresses - resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress - resource.instanceDetails.networkInterfaces.publicDnsName - resource.instanceDetails.networkInterfaces.publicIp - resource.instanceDetails.networkInterfaces.securityGroups.groupId - resource.instanceDetails.networkInterfaces.securityGroups.groupName - resource.instanceDetails.networkInterfaces.subnetId - resource.instanceDetails.networkInterfaces.vpcId - resource.instanceDetails.tags.key - resource.instanceDetails.tags.value - resource.resourceType - service.action.actionType - service.action.awsApiCallAction.api - service.action.awsApiCallAction.callerType - service.action.awsApiCallAction.errorCode - service.action.awsApiCallAction.remoteIpDetails.city.cityName - service.action.awsApiCallAction.remoteIpDetails.country.countryName - service.action.awsApiCallAction.remoteIpDetails.ipAddressV4 - service.action.awsApiCallAction.remoteIpDetails.organization.asn - service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg - service.action.awsApiCallAction.serviceName - service.action.dnsRequestAction.domain - service.action.networkConnectionAction.blocked - service.action.networkConnectionAction.connectionDirection - service.action.networkConnectionAction.localPortDetails.port - service.action.networkConnectionAction.protocol - service.action.networkConnectionAction.localIpDetails.ipAddressV4 - service.action.networkConnectionAction.remoteIpDetails.city.cityName - service.action.networkConnectionAction.remoteIpDetails.country.countryName - service.action.networkConnectionAction.remoteIpDetails.ipAddressV4 - service.action.networkConnectionAction.remoteIpDetails.organization.asn - service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg - service.action.networkConnectionAction.remotePortDetails.port - service.additionalInfo.threatListName - service.archived When this attribute is set to TRUE, only archived findings are listed. When it's set to FALSE, only unarchived findings are listed. When this attribute is not set, all existing findings are listed. - service.resourceRole - severity - type - updatedAt Type: ISO 8601 string format: YYYY-MM-DDTHH:MM:SS.SSSZ or YYYY-MM-DDTHH:MM:SSZ depending on whether the value contains milliseconds.
            :param item_type: Specifies the condition to be applied to a single field when filtering through findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_guardduty as guardduty
                
                # criterion: Any
                
                finding_criteria_property = guardduty.CfnFilter.FindingCriteriaProperty(
                    criterion=criterion,
                    item_type=guardduty.CfnFilter.ConditionProperty(
                        eq=["eq"],
                        equal_to=["equalTo"],
                        greater_than=123,
                        greater_than_or_equal=123,
                        gt=123,
                        gte=123,
                        less_than=123,
                        less_than_or_equal=123,
                        lt=123,
                        lte=123,
                        neq=["neq"],
                        not_equals=["notEquals"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f4804a72c05070a8a25405f065b49dd3914286fabb20ae070705b9bd755fee5)
                check_type(argname="argument criterion", value=criterion, expected_type=type_hints["criterion"])
                check_type(argname="argument item_type", value=item_type, expected_type=type_hints["item_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if criterion is not None:
                self._values["criterion"] = criterion
            if item_type is not None:
                self._values["item_type"] = item_type

        @builtins.property
        def criterion(self) -> typing.Any:
            '''Represents a map of finding properties that match specified conditions and values when querying findings.

            For a mapping of JSON criterion to their console equivalent see `Finding criteria <https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html#filter_criteria>`_ . The following are the available criterion:

            - accountId
            - region
            - confidence
            - id
            - resource.accessKeyDetails.accessKeyId
            - resource.accessKeyDetails.principalId
            - resource.accessKeyDetails.userName
            - resource.accessKeyDetails.userType
            - resource.instanceDetails.iamInstanceProfile.id
            - resource.instanceDetails.imageId
            - resource.instanceDetails.instanceId
            - resource.instanceDetails.outpostArn
            - resource.instanceDetails.networkInterfaces.ipv6Addresses
            - resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress
            - resource.instanceDetails.networkInterfaces.publicDnsName
            - resource.instanceDetails.networkInterfaces.publicIp
            - resource.instanceDetails.networkInterfaces.securityGroups.groupId
            - resource.instanceDetails.networkInterfaces.securityGroups.groupName
            - resource.instanceDetails.networkInterfaces.subnetId
            - resource.instanceDetails.networkInterfaces.vpcId
            - resource.instanceDetails.tags.key
            - resource.instanceDetails.tags.value
            - resource.resourceType
            - service.action.actionType
            - service.action.awsApiCallAction.api
            - service.action.awsApiCallAction.callerType
            - service.action.awsApiCallAction.errorCode
            - service.action.awsApiCallAction.remoteIpDetails.city.cityName
            - service.action.awsApiCallAction.remoteIpDetails.country.countryName
            - service.action.awsApiCallAction.remoteIpDetails.ipAddressV4
            - service.action.awsApiCallAction.remoteIpDetails.organization.asn
            - service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg
            - service.action.awsApiCallAction.serviceName
            - service.action.dnsRequestAction.domain
            - service.action.networkConnectionAction.blocked
            - service.action.networkConnectionAction.connectionDirection
            - service.action.networkConnectionAction.localPortDetails.port
            - service.action.networkConnectionAction.protocol
            - service.action.networkConnectionAction.localIpDetails.ipAddressV4
            - service.action.networkConnectionAction.remoteIpDetails.city.cityName
            - service.action.networkConnectionAction.remoteIpDetails.country.countryName
            - service.action.networkConnectionAction.remoteIpDetails.ipAddressV4
            - service.action.networkConnectionAction.remoteIpDetails.organization.asn
            - service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg
            - service.action.networkConnectionAction.remotePortDetails.port
            - service.additionalInfo.threatListName
            - service.archived

            When this attribute is set to TRUE, only archived findings are listed. When it's set to FALSE, only unarchived findings are listed. When this attribute is not set, all existing findings are listed.

            - service.resourceRole
            - severity
            - type
            - updatedAt

            Type: ISO 8601 string format: YYYY-MM-DDTHH:MM:SS.SSSZ or YYYY-MM-DDTHH:MM:SSZ depending on whether the value contains milliseconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-criterion
            '''
            result = self._values.get("criterion")
            return typing.cast(typing.Any, result)

        @builtins.property
        def item_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.ConditionProperty"]]:
            '''Specifies the condition to be applied to a single field when filtering through findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-itemtype
            '''
            result = self._values.get("item_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.ConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "description": "description",
        "detector_id": "detectorId",
        "finding_criteria": "findingCriteria",
        "name": "name",
        "rank": "rank",
        "tags": "tags",
    },
)
class CfnFilterProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        description: builtins.str,
        detector_id: builtins.str,
        finding_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        rank: jsii.Number,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFilter``.

        :param action: Specifies the action that is to be applied to the findings that match the filter.
        :param description: The description of the filter. Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses ( ``{ }`` , ``[ ]`` , and ``( )`` ), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.
        :param detector_id: The ID of the detector belonging to the GuardDuty account that you want to create a filter for.
        :param finding_criteria: Represents the criteria to be used in the filter for querying findings.
        :param name: The name of the filter. Valid characters include period (.), underscore (_), dash (-), and alphanumeric characters. A whitespace is considered to be an invalid character.
        :param rank: Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings. The minimum value for this property is 1 and the maximum is 100. By default, filters may not be created in the same order as they are ranked. To ensure that the filters are created in the expected order, you can use an optional attribute, `DependsOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ , with the following syntax: ``"DependsOn":[ "ObjectName" ]`` .
        :param tags: The tags to be added to a new filter resource. Each tag consists of a key and an optional value, both of which you define. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            # criterion: Any
            
            cfn_filter_props = guardduty.CfnFilterProps(
                action="action",
                description="description",
                detector_id="detectorId",
                finding_criteria=guardduty.CfnFilter.FindingCriteriaProperty(
                    criterion=criterion,
                    item_type=guardduty.CfnFilter.ConditionProperty(
                        eq=["eq"],
                        equal_to=["equalTo"],
                        greater_than=123,
                        greater_than_or_equal=123,
                        gt=123,
                        gte=123,
                        less_than=123,
                        less_than_or_equal=123,
                        lt=123,
                        lte=123,
                        neq=["neq"],
                        not_equals=["notEquals"]
                    )
                ),
                name="name",
                rank=123,
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f44ad794e7dbae18bc70d670d096dac3d980dc5e20e5c9703013ddb79dd0e03)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument finding_criteria", value=finding_criteria, expected_type=type_hints["finding_criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rank", value=rank, expected_type=type_hints["rank"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "description": description,
            "detector_id": detector_id,
            "finding_criteria": finding_criteria,
            "name": name,
            "rank": rank,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action(self) -> builtins.str:
        '''Specifies the action that is to be applied to the findings that match the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the filter.

        Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses ( ``{ }`` , ``[ ]`` , and ``( )`` ), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The ID of the detector belonging to the GuardDuty account that you want to create a filter for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def finding_criteria(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnFilter.FindingCriteriaProperty]:
        '''Represents the criteria to be used in the filter for querying findings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
        '''
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFilter.FindingCriteriaProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the filter.

        Valid characters include period (.), underscore (_), dash (-), and alphanumeric characters. A whitespace is considered to be an invalid character.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rank(self) -> jsii.Number:
        '''Specifies the position of the filter in the list of current filters.

        Also specifies the order in which this filter is applied to the findings. The minimum value for this property is 1 and the maximum is 100.

        By default, filters may not be created in the same order as they are ranked. To ensure that the filters are created in the expected order, you can use an optional attribute, `DependsOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ , with the following syntax: ``"DependsOn":[ "ObjectName" ]`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
        '''
        result = self._values.get("rank")
        assert result is not None, "Required property 'rank' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be added to a new filter resource.

        Each tag consists of a key and an optional value, both of which you define.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnIPSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnIPSet",
):
    '''The ``AWS::GuardDuty::IPSet`` resource specifies a new ``IPSet`` .

    An ``IPSet`` is a list of trusted IP addresses from which secure communication is allowed with AWS infrastructure and applications.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_iPSet = guardduty.CfnIPSet(self, "MyCfnIPSet",
            activate=False,
            detector_id="detectorId",
            format="format",
            location="location",
        
            # the properties below are optional
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
        activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param activate: Indicates whether or not GuardDuty uses the ``IPSet`` .
        :param detector_id: The unique ID of the detector of the GuardDuty account that you want to create an IPSet for.
        :param format: The format of the file that contains the IPSet.
        :param location: The URI of the file that contains the IPSet.
        :param name: The user-friendly name to identify the IPSet. Allowed characters are alphanumeric, whitespace, dash (-), and underscores (_).
        :param tags: The tags to be added to a new IP set resource. Each tag consists of a key and an optional value, both of which you define. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0c6fd2cb08b5267e6265af6fae1a30df065b4b25dc1d6d684eec9f9bb50cda0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIPSetProps(
            activate=activate,
            detector_id=detector_id,
            format=format,
            location=location,
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
            type_hints = typing.get_type_hints(_typecheckingstub__be6ba6e1eaa43e3f16c759ee0699a48221397ee1debd4d238eb87420ec7410eb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f73b8d62d57edd5bfcf01e8f9bca6587422ac96050ad46ec492d41c34ddad67d)
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
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Indicates whether or not GuardDuty uses the ``IPSet`` .'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "activate"))

    @activate.setter
    def activate(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b1596d6c0cfe12615f22b3beb59354b8df0675c2e4bc8f6df3b493378f87f7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activate", value)

    @builtins.property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty account that you want to create an IPSet for.'''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aa4bf6ad59c1223085a10fc5ece87e88253a83036d5b0e3947792ffc785a9ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''The format of the file that contains the IPSet.'''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a147943316e3241ad2b7ee0baf0504d2b75af46d5059eb5c910a2cfd6247eb2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        '''The URI of the file that contains the IPSet.'''
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eb5e4bd471d1c943ffdbb005112dd6e82668bf037c636f47fcf6933a2bbc63e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name to identify the IPSet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0128f966eac1a136f141aedcb397b96308a170e31f1d45176a39160ebf5a7a8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be added to a new IP set resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3575dce7e4be33e061dd476657db25cdd931a4eb3f742afe675edf5d4a2df5ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnIPSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "activate": "activate",
        "detector_id": "detectorId",
        "format": "format",
        "location": "location",
        "name": "name",
        "tags": "tags",
    },
)
class CfnIPSetProps:
    def __init__(
        self,
        *,
        activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIPSet``.

        :param activate: Indicates whether or not GuardDuty uses the ``IPSet`` .
        :param detector_id: The unique ID of the detector of the GuardDuty account that you want to create an IPSet for.
        :param format: The format of the file that contains the IPSet.
        :param location: The URI of the file that contains the IPSet.
        :param name: The user-friendly name to identify the IPSet. Allowed characters are alphanumeric, whitespace, dash (-), and underscores (_).
        :param tags: The tags to be added to a new IP set resource. Each tag consists of a key and an optional value, both of which you define. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_iPSet_props = guardduty.CfnIPSetProps(
                activate=False,
                detector_id="detectorId",
                format="format",
                location="location",
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f47aa340c89b95bf1878c9cb7463920b568c23940ad283e6f2c2bb481191ff38)
            check_type(argname="argument activate", value=activate, expected_type=type_hints["activate"])
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "activate": activate,
            "detector_id": detector_id,
            "format": format,
            "location": location,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def activate(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Indicates whether or not GuardDuty uses the ``IPSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        '''
        result = self._values.get("activate")
        assert result is not None, "Required property 'activate' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty account that you want to create an IPSet for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''The format of the file that contains the IPSet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The URI of the file that contains the IPSet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name to identify the IPSet.

        Allowed characters are alphanumeric, whitespace, dash (-), and underscores (_).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be added to a new IP set resource.

        Each tag consists of a key and an optional value, both of which you define.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIPSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnMaster",
):
    '''You can use the ``AWS::GuardDuty::Master`` resource in a GuardDuty member account to accept an invitation from a GuardDuty administrator account.

    The invitation to the member account must be sent prior to using the ``AWS::GuardDuty::Master`` resource to accept the administrator account's invitation. You can invite a member account by using the ``InviteMembers`` operation of the GuardDuty API, or by creating an ``AWS::GuardDuty::Member`` resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_master = guardduty.CfnMaster(self, "MyCfnMaster",
            detector_id="detectorId",
            master_id="masterId",
        
            # the properties below are optional
            invitation_id="invitationId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        detector_id: builtins.str,
        master_id: builtins.str,
        invitation_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param detector_id: The unique ID of the detector of the GuardDuty member account.
        :param master_id: The AWS account ID of the account designated as the GuardDuty administrator account.
        :param invitation_id: The ID of the invitation that is sent to the account designated as a member account. You can find the invitation ID by using the ListInvitation action of the GuardDuty API.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d03095d03ec71c014c1cfc8e78531e9220fec576d321a24de280815b0d72c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMasterProps(
            detector_id=detector_id, master_id=master_id, invitation_id=invitation_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab4a78858d36aaf352ad2ff8dfc637731dd888bdadcf22f5c50ff6c5ae0744fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb829382c0bdfda6ecbc07d3576a886cf8b80046e1127a725e9d945f109b0d41)
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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty member account.'''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c1eeac8301776a8d619633672c98988bcf0b82fe38dbcc46fa5c0286659a9d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="masterId")
    def master_id(self) -> builtins.str:
        '''The AWS account ID of the account designated as the GuardDuty administrator account.'''
        return typing.cast(builtins.str, jsii.get(self, "masterId"))

    @master_id.setter
    def master_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4840129622d8855c7daf32d5a871adc7293a471c1fbe37d7c95417e6fcecbd7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterId", value)

    @builtins.property
    @jsii.member(jsii_name="invitationId")
    def invitation_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the invitation that is sent to the account designated as a member account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invitationId"))

    @invitation_id.setter
    def invitation_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__406b3febbdc47c53592d13698f2d7656983f29af6904125a269c88c12834820a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invitationId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnMasterProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "master_id": "masterId",
        "invitation_id": "invitationId",
    },
)
class CfnMasterProps:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        master_id: builtins.str,
        invitation_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMaster``.

        :param detector_id: The unique ID of the detector of the GuardDuty member account.
        :param master_id: The AWS account ID of the account designated as the GuardDuty administrator account.
        :param invitation_id: The ID of the invitation that is sent to the account designated as a member account. You can find the invitation ID by using the ListInvitation action of the GuardDuty API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_master_props = guardduty.CfnMasterProps(
                detector_id="detectorId",
                master_id="masterId",
            
                # the properties below are optional
                invitation_id="invitationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e775fa833f1198c34b0f7ed2c1b1b0d25c6dfb50b70659b53e24aa8129f5a35)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument master_id", value=master_id, expected_type=type_hints["master_id"])
            check_type(argname="argument invitation_id", value=invitation_id, expected_type=type_hints["invitation_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "master_id": master_id,
        }
        if invitation_id is not None:
            self._values["invitation_id"] = invitation_id

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty member account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_id(self) -> builtins.str:
        '''The AWS account ID of the account designated as the GuardDuty administrator account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
        '''
        result = self._values.get("master_id")
        assert result is not None, "Required property 'master_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invitation_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the invitation that is sent to the account designated as a member account.

        You can find the invitation ID by using the ListInvitation action of the GuardDuty API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
        '''
        result = self._values.get("invitation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMasterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMember(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnMember",
):
    '''You can use the ``AWS::GuardDuty::Member`` resource to add an AWS account as a GuardDuty member account to the current GuardDuty administrator account.

    If the value of the ``Status`` property is not provided or is set to ``Created`` , a member account is created but not invited. If the value of the ``Status`` property is set to ``Invited`` , a member account is created and invited. An ``AWS::GuardDuty::Member`` resource must be created with the ``Status`` property set to ``Invited`` before the ``AWS::GuardDuty::Master`` resource can be created in a GuardDuty member account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_member = guardduty.CfnMember(self, "MyCfnMember",
            detector_id="detectorId",
            email="email",
            member_id="memberId",
        
            # the properties below are optional
            disable_email_notification=False,
            message="message",
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        detector_id: builtins.str,
        email: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        message: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param detector_id: The ID of the detector associated with the GuardDuty service to add the member to.
        :param email: The email address associated with the member account.
        :param member_id: The AWS account ID of the account to designate as a member.
        :param disable_email_notification: Specifies whether or not to disable email notification for the member account that you invite.
        :param message: The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.
        :param status: You can use the ``Status`` property to update the status of the relationship between the member account and its administrator account. Valid values are ``Created`` and ``Invited`` when using an ``AWS::GuardDuty::Member`` resource. If the value for this property is not provided or set to ``Created`` , a member account is created but not invited. If the value of this property is set to ``Invited`` , a member account is created and invited.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f44a0908d294a573f190a54e5b7ef824c88df12f421c206626106264534c4aac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMemberProps(
            detector_id=detector_id,
            email=email,
            member_id=member_id,
            disable_email_notification=disable_email_notification,
            message=message,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2c43ec84f2df433ff11133f312974d01ed724ac122b56a4ebf226a2559204a8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aed253523c72485b59fa49b2da3826b766e320b488e0889727ad37f724997039)
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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The ID of the detector associated with the GuardDuty service to add the member to.'''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d526f38412f59e2458ce2c2439621166117e2219e0b7389c37d70f65550274c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        '''The email address associated with the member account.'''
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__440534181e19dc546b7c107a5ec6269f67af73284cea8e784c8e3133ff4dbe38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> builtins.str:
        '''The AWS account ID of the account to designate as a member.'''
        return typing.cast(builtins.str, jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d66a842586ef2d5ec697ca62e59ef2af5353de489b001fb4687956e1766aac41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberId", value)

    @builtins.property
    @jsii.member(jsii_name="disableEmailNotification")
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether or not to disable email notification for the member account that you invite.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "disableEmailNotification"))

    @disable_email_notification.setter
    def disable_email_notification(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0d936d65b44cfdbfcf7b0213e06a4664e73ffce48a3399a6c5e192b98602f0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEmailNotification", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Optional[builtins.str]:
        '''The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "message"))

    @message.setter
    def message(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d3cf6dd5da6668e769e1c219e41c1cf9e7b6c786276b310d7818bbf1b0e76c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''You can use the ``Status`` property to update the status of the relationship between the member account and its administrator account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6a13c5df833c1f8928aa6ad329e356681a0e7ca00f52f83fb00c4fdc03962f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnMemberProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "email": "email",
        "member_id": "memberId",
        "disable_email_notification": "disableEmailNotification",
        "message": "message",
        "status": "status",
    },
)
class CfnMemberProps:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        email: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        message: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMember``.

        :param detector_id: The ID of the detector associated with the GuardDuty service to add the member to.
        :param email: The email address associated with the member account.
        :param member_id: The AWS account ID of the account to designate as a member.
        :param disable_email_notification: Specifies whether or not to disable email notification for the member account that you invite.
        :param message: The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.
        :param status: You can use the ``Status`` property to update the status of the relationship between the member account and its administrator account. Valid values are ``Created`` and ``Invited`` when using an ``AWS::GuardDuty::Member`` resource. If the value for this property is not provided or set to ``Created`` , a member account is created but not invited. If the value of this property is set to ``Invited`` , a member account is created and invited.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_member_props = guardduty.CfnMemberProps(
                detector_id="detectorId",
                email="email",
                member_id="memberId",
            
                # the properties below are optional
                disable_email_notification=False,
                message="message",
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__707033ab8b51a1c3cb64594f2a7e13ff03829ca7aed824af4d8509b6302ad443)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
            check_type(argname="argument disable_email_notification", value=disable_email_notification, expected_type=type_hints["disable_email_notification"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "email": email,
            "member_id": member_id,
        }
        if disable_email_notification is not None:
            self._values["disable_email_notification"] = disable_email_notification
        if message is not None:
            self._values["message"] = message
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The ID of the detector associated with the GuardDuty service to add the member to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The email address associated with the member account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(self) -> builtins.str:
        '''The AWS account ID of the account to designate as a member.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether or not to disable email notification for the member account that you invite.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
        '''
        result = self._values.get("disable_email_notification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''You can use the ``Status`` property to update the status of the relationship between the member account and its administrator account.

        Valid values are ``Created`` and ``Invited`` when using an ``AWS::GuardDuty::Member`` resource. If the value for this property is not provided or set to ``Created`` , a member account is created but not invited. If the value of this property is set to ``Invited`` , a member account is created and invited.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnThreatIntelSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_guardduty.CfnThreatIntelSet",
):
    '''The ``AWS::GuardDuty::ThreatIntelSet`` resource specifies a new ``ThreatIntelSet`` .

    A ``ThreatIntelSet`` consists of known malicious IP addresses. GuardDuty generates findings based on the ``ThreatIntelSet`` when it is activated.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_guardduty as guardduty
        
        cfn_threat_intel_set = guardduty.CfnThreatIntelSet(self, "MyCfnThreatIntelSet",
            activate=False,
            detector_id="detectorId",
            format="format",
            location="location",
        
            # the properties below are optional
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
        activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param activate: A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        :param detector_id: The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.
        :param format: The format of the file that contains the ThreatIntelSet.
        :param location: The URI of the file that contains the ThreatIntelSet.
        :param name: A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        :param tags: The tags to be added to a new threat list resource. Each tag consists of a key and an optional value, both of which you define. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e60035c0bc955afb794ee89f0439deae280bfec665014cbbd161f08566de73a7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnThreatIntelSetProps(
            activate=activate,
            detector_id=detector_id,
            format=format,
            location=location,
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d9a7dab9bf19d452d61d5fb4b5e80f876633f39a0cf5051e3a47e94c815073d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa2f2572c41477f9f21703ec5b985dde17df361473f4b639cf51e738006da367)
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
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "activate"))

    @activate.setter
    def activate(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3660f9080839cb6141a3aaf57ad04008ebbf5e29b4ee2cf7c3bcbdb94c082285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activate", value)

    @builtins.property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.'''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6198953302f0959c3d25abb6f0063fb638c6abf44a125235eafb4937065091bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''The format of the file that contains the ThreatIntelSet.'''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df3e4ea6d2ecdcdcfdf57f71eb38574c54d5e2340fc6b41e3c5752d81380474b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        '''The URI of the file that contains the ThreatIntelSet.'''
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01b8f1e578ee008d23f829009bf45a0717efeb23dd3f85345a6c6203e181177a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78860e52ab0e0d6681a85585054b7ed92f84696ec2b6a43bb90c609188bf36e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be added to a new threat list resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__213606bb8c2a17afd6b75e6224d08fd34ab33f0ef606dcd3df99402aa81754e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_guardduty.CfnThreatIntelSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "activate": "activate",
        "detector_id": "detectorId",
        "format": "format",
        "location": "location",
        "name": "name",
        "tags": "tags",
    },
)
class CfnThreatIntelSetProps:
    def __init__(
        self,
        *,
        activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnThreatIntelSet``.

        :param activate: A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        :param detector_id: The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.
        :param format: The format of the file that contains the ThreatIntelSet.
        :param location: The URI of the file that contains the ThreatIntelSet.
        :param name: A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        :param tags: The tags to be added to a new threat list resource. Each tag consists of a key and an optional value, both of which you define. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_guardduty as guardduty
            
            cfn_threat_intel_set_props = guardduty.CfnThreatIntelSetProps(
                activate=False,
                detector_id="detectorId",
                format="format",
                location="location",
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a5d0bedab8c4fad4ab288ce5a467dbe6a4d07ef2947521b14162f1e7ac218a1)
            check_type(argname="argument activate", value=activate, expected_type=type_hints["activate"])
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "activate": activate,
            "detector_id": detector_id,
            "format": format,
            "location": location,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def activate(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
        '''
        result = self._values.get("activate")
        assert result is not None, "Required property 'activate' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''The format of the file that contains the ThreatIntelSet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The URI of the file that contains the ThreatIntelSet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be added to a new threat list resource.

        Each tag consists of a key and an optional value, both of which you define.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThreatIntelSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDetector",
    "CfnDetectorProps",
    "CfnFilter",
    "CfnFilterProps",
    "CfnIPSet",
    "CfnIPSetProps",
    "CfnMaster",
    "CfnMasterProps",
    "CfnMember",
    "CfnMemberProps",
    "CfnThreatIntelSet",
    "CfnThreatIntelSetProps",
]

publication.publish()

def _typecheckingstub__d4374e73b5cd2e2814bd72eb21f29547df6146e023d23ee6d5c8c8cdb4439473(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    enable: typing.Union[builtins.bool, _IResolvable_da3f097b],
    data_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.CFNDataSourceConfigurationsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    features: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.FeatureConfigurationsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_publishing_frequency: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd13133d47f23bb91dcc2e425b360777bcd306422761af023eb8654fdc89892(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db5a3aaacc92cdd47629478cb9f2db842f4bfb46e4ac877d9368e545bf7ab3a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1c4208def5e29bff60511511974687c29f282d57c3bb461675543b67475958(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d984644fe0d5555f018ae12b1bfbb1e875501438854ca50d249d3cd6091178f1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDetector.CFNDataSourceConfigurationsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d162426268bf9dc8b5f3efea1e4d49418ad72947ae8c15de703212246d36f5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.FeatureConfigurationsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05a15130d3f8d159abcddfb10123f12bf70fc091e86be777252ab49ab86dd84(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__273b490c75e93f137bcaf4b10d4df89064d16e78f021b92c6008b18c9c74e99c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc6f5e6dd89fc0d30f28179b1bc893366d4b68b6eff35d1ed195ef95ea96270(
    *,
    kubernetes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.CFNKubernetesConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    malware_protection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.CFNMalwareProtectionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.CFNS3LogsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a0cf3d36fd260bda8fbf7c652e71e3282b0a3867b477f0b4e992be46f9e9fc(
    *,
    enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__507c730ce77749f55565236ae0e0949766ee63b4e28eddebc38a59384af159d1(
    *,
    audit_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.CFNKubernetesAuditLogsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b489755354068d624ff07c4dbcaacb69f242db268771504faaf7ec08d1fa7b11(
    *,
    scan_ec2_instance_with_findings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.CFNScanEc2InstanceWithFindingsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__273397d5fa0880c36c6aca40485efece77caba905c5a76cf0e055b3125298f05(
    *,
    enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f726c6703e77466e481c466dc3d2680cf3ce31a2bfc0af08fdc3570849efb55a(
    *,
    ebs_volumes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb1d313a0a14310f6b849190dee89a2da63dae70d22f924dc5da548f75272d58(
    *,
    name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f95505a43158b2ecb934d0eda3be9e00ddd25a7f5ec93e48b5a2ca2bcd6addf(
    *,
    additional_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.FeatureAdditionalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3914f92ec13130f6437ebb8077c96e2e1592d547cc445617fe4957f629b5cb3c(
    *,
    enable: typing.Union[builtins.bool, _IResolvable_da3f097b],
    data_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.CFNDataSourceConfigurationsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    features: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.FeatureConfigurationsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_publishing_frequency: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__067e85819bdb865e6337a26c378c0472fa2b9e72f47dfccf0bca609928a7aea7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action: builtins.str,
    description: builtins.str,
    detector_id: builtins.str,
    finding_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    rank: jsii.Number,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44aa41d511d84a4f9e1672f1bbcbf9db9da6c8367d7cad9ea6f0e30d51c4edc1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d00911f9ef1cc2770fa371850c170d11fa5dae6c49195efa6eedf0ecc147d436(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48a346a5915bdb2f2af2271886d8088c817fdc4bbf7e9f976a58166a6d451959(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76609fcbed2d16e8e3d770136dd8f1d34ef69ecf949487325d62e1df3feba8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a940342f0dba5155f5628025cb840051cc96e969cc988dd60f36269d57e2ccd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fbed2e2e1c4e36b77bef70f5730cf33088965585e081220ea8782f1bc6ec58e(
    value: typing.Union[_IResolvable_da3f097b, CfnFilter.FindingCriteriaProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a919e4dbcd673724e15009ab41b3a97b27ecfabae06ad4b152e2793162be4ddc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64d9594f1beac431821c9cffe86b3daf0e0dceaacc9252ecabb10c61e6b89d8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec0b341923b31034fd13a73457e5a7351149963826be423d3b727494075107d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf8702ee06c6a6e0f8140afbb047453bd22f56672abb17dbf2127dc944b075d(
    *,
    eq: typing.Optional[typing.Sequence[builtins.str]] = None,
    equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
    greater_than: typing.Optional[jsii.Number] = None,
    greater_than_or_equal: typing.Optional[jsii.Number] = None,
    gt: typing.Optional[jsii.Number] = None,
    gte: typing.Optional[jsii.Number] = None,
    less_than: typing.Optional[jsii.Number] = None,
    less_than_or_equal: typing.Optional[jsii.Number] = None,
    lt: typing.Optional[jsii.Number] = None,
    lte: typing.Optional[jsii.Number] = None,
    neq: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4804a72c05070a8a25405f065b49dd3914286fabb20ae070705b9bd755fee5(
    *,
    criterion: typing.Any = None,
    item_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.ConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f44ad794e7dbae18bc70d670d096dac3d980dc5e20e5c9703013ddb79dd0e03(
    *,
    action: builtins.str,
    description: builtins.str,
    detector_id: builtins.str,
    finding_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    rank: jsii.Number,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c6fd2cb08b5267e6265af6fae1a30df065b4b25dc1d6d684eec9f9bb50cda0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
    detector_id: builtins.str,
    format: builtins.str,
    location: builtins.str,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be6ba6e1eaa43e3f16c759ee0699a48221397ee1debd4d238eb87420ec7410eb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f73b8d62d57edd5bfcf01e8f9bca6587422ac96050ad46ec492d41c34ddad67d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1596d6c0cfe12615f22b3beb59354b8df0675c2e4bc8f6df3b493378f87f7c(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aa4bf6ad59c1223085a10fc5ece87e88253a83036d5b0e3947792ffc785a9ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a147943316e3241ad2b7ee0baf0504d2b75af46d5059eb5c910a2cfd6247eb2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eb5e4bd471d1c943ffdbb005112dd6e82668bf037c636f47fcf6933a2bbc63e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0128f966eac1a136f141aedcb397b96308a170e31f1d45176a39160ebf5a7a8f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3575dce7e4be33e061dd476657db25cdd931a4eb3f742afe675edf5d4a2df5ce(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f47aa340c89b95bf1878c9cb7463920b568c23940ad283e6f2c2bb481191ff38(
    *,
    activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
    detector_id: builtins.str,
    format: builtins.str,
    location: builtins.str,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d03095d03ec71c014c1cfc8e78531e9220fec576d321a24de280815b0d72c0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    detector_id: builtins.str,
    master_id: builtins.str,
    invitation_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab4a78858d36aaf352ad2ff8dfc637731dd888bdadcf22f5c50ff6c5ae0744fb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb829382c0bdfda6ecbc07d3576a886cf8b80046e1127a725e9d945f109b0d41(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c1eeac8301776a8d619633672c98988bcf0b82fe38dbcc46fa5c0286659a9d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4840129622d8855c7daf32d5a871adc7293a471c1fbe37d7c95417e6fcecbd7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__406b3febbdc47c53592d13698f2d7656983f29af6904125a269c88c12834820a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e775fa833f1198c34b0f7ed2c1b1b0d25c6dfb50b70659b53e24aa8129f5a35(
    *,
    detector_id: builtins.str,
    master_id: builtins.str,
    invitation_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44a0908d294a573f190a54e5b7ef824c88df12f421c206626106264534c4aac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    detector_id: builtins.str,
    email: builtins.str,
    member_id: builtins.str,
    disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    message: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2c43ec84f2df433ff11133f312974d01ed724ac122b56a4ebf226a2559204a8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed253523c72485b59fa49b2da3826b766e320b488e0889727ad37f724997039(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d526f38412f59e2458ce2c2439621166117e2219e0b7389c37d70f65550274c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__440534181e19dc546b7c107a5ec6269f67af73284cea8e784c8e3133ff4dbe38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d66a842586ef2d5ec697ca62e59ef2af5353de489b001fb4687956e1766aac41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d936d65b44cfdbfcf7b0213e06a4664e73ffce48a3399a6c5e192b98602f0e(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d3cf6dd5da6668e769e1c219e41c1cf9e7b6c786276b310d7818bbf1b0e76c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6a13c5df833c1f8928aa6ad329e356681a0e7ca00f52f83fb00c4fdc03962f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__707033ab8b51a1c3cb64594f2a7e13ff03829ca7aed824af4d8509b6302ad443(
    *,
    detector_id: builtins.str,
    email: builtins.str,
    member_id: builtins.str,
    disable_email_notification: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    message: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e60035c0bc955afb794ee89f0439deae280bfec665014cbbd161f08566de73a7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
    detector_id: builtins.str,
    format: builtins.str,
    location: builtins.str,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d9a7dab9bf19d452d61d5fb4b5e80f876633f39a0cf5051e3a47e94c815073d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa2f2572c41477f9f21703ec5b985dde17df361473f4b639cf51e738006da367(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3660f9080839cb6141a3aaf57ad04008ebbf5e29b4ee2cf7c3bcbdb94c082285(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6198953302f0959c3d25abb6f0063fb638c6abf44a125235eafb4937065091bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3e4ea6d2ecdcdcfdf57f71eb38574c54d5e2340fc6b41e3c5752d81380474b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b8f1e578ee008d23f829009bf45a0717efeb23dd3f85345a6c6203e181177a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78860e52ab0e0d6681a85585054b7ed92f84696ec2b6a43bb90c609188bf36e6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__213606bb8c2a17afd6b75e6224d08fd34ab33f0ef606dcd3df99402aa81754e0(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a5d0bedab8c4fad4ab288ce5a467dbe6a4d07ef2947521b14162f1e7ac218a1(
    *,
    activate: typing.Union[builtins.bool, _IResolvable_da3f097b],
    detector_id: builtins.str,
    format: builtins.str,
    location: builtins.str,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
