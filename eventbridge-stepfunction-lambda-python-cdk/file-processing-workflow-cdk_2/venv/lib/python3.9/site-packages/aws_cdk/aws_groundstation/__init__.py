'''
# AWS::GroundStation Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_groundstation as groundstation
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for GroundStation construct libraries](https://constructs.dev/search?q=groundstation)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::GroundStation resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GroundStation.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GroundStation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GroundStation.html).

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
class CfnConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig",
):
    '''Creates a ``Config`` with the specified parameters.

    Config objects provide Ground Station with the details necessary in order to schedule and execute satellite contacts.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_groundstation as groundstation
        
        cfn_config = groundstation.CfnConfig(self, "MyCfnConfig",
            config_data=groundstation.CfnConfig.ConfigDataProperty(
                antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                ),
                antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                    decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                ),
                antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    ),
                    target_eirp=groundstation.CfnConfig.EirpProperty(
                        units="units",
                        value=123
                    ),
                    transmit_disabled=False
                ),
                dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                    dataflow_endpoint_name="dataflowEndpointName",
                    dataflow_endpoint_region="dataflowEndpointRegion"
                ),
                s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                    bucket_arn="bucketArn",
                    prefix="prefix",
                    role_arn="roleArn"
                ),
                tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                    autotrack="autotrack"
                ),
                uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                    antenna_uplink_config_arn="antennaUplinkConfigArn",
                    enabled=False
                )
            ),
            name="name",
        
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
        config_data: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.ConfigDataProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param config_data: Object containing the parameters of a config. Only one subtype may be specified per config. See the subtype definitions for a description of each config subtype.
        :param name: The name of the config object.
        :param tags: Tags assigned to a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13b5342b1ca67f4a4ccbf4e2d71441ec8ac6775411c783b3c9c933f4caeaeb44)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigProps(config_data=config_data, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3cdfd5eb2baaf5f01fe9f7913185faf70d134acf441b89c112df84fd2f1db8a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd40941f885360d05e2643d3d6f98380b40caebf76d694523c46c112050eb127)
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
        '''The ARN of the config, such as ``arn:aws:groundstation:us-east-2:1234567890:config/tracking/9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the config, such as ``9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of the config, such as ``tracking`` .

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

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
    @jsii.member(jsii_name="configData")
    def config_data(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConfig.ConfigDataProperty"]:
        '''Object containing the parameters of a config.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfig.ConfigDataProperty"], jsii.get(self, "configData"))

    @config_data.setter
    def config_data(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConfig.ConfigDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1563feeaa37deb3f7ed7d57717d9cfb0c9d0d00d4203ece4f573e5ceaf951329)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configData", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the config object.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e45ad42a1b16a7ac4346df0c4eb4ef210effbe14d6f3a655aeb196609bb41609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags assigned to a resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5239786ac786ccdad1f55bd40cbcac2fd2c846b2a7de2861dbb7b912f8c930a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.AntennaDownlinkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"spectrum_config": "spectrumConfig"},
    )
    class AntennaDownlinkConfigProperty:
        def __init__(
            self,
            *,
            spectrum_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.SpectrumConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should configure an antenna for downlink during a contact.

            Use an antenna downlink config in a mission profile to receive the downlink data in raw DigIF format.

            :param spectrum_config: Defines the spectrum configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                antenna_downlink_config_property = groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__95c9bb891616bdcd84a4fa4a4632dbc784f0eb088325a7f017b16d8b07182f9f)
                check_type(argname="argument spectrum_config", value=spectrum_config, expected_type=type_hints["spectrum_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.SpectrumConfigProperty"]]:
            '''Defines the spectrum configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html#cfn-groundstation-config-antennadownlinkconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.SpectrumConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaDownlinkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "decode_config": "decodeConfig",
            "demodulation_config": "demodulationConfig",
            "spectrum_config": "spectrumConfig",
        },
    )
    class AntennaDownlinkDemodDecodeConfigProperty:
        def __init__(
            self,
            *,
            decode_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.DecodeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            demodulation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.DemodulationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            spectrum_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.SpectrumConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should configure an antenna for downlink during a contact.

            Use an antenna downlink demod decode config in a mission profile to receive the downlink data that has been demodulated and decoded.

            :param decode_config: Defines how the RF signal will be decoded.
            :param demodulation_config: Defines how the RF signal will be demodulated.
            :param spectrum_config: Defines the spectrum configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                antenna_downlink_demod_decode_config_property = groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                    decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ebe67adf126f560718d80fe7b470120098ad348e65acc48056db851ebe85ca63)
                check_type(argname="argument decode_config", value=decode_config, expected_type=type_hints["decode_config"])
                check_type(argname="argument demodulation_config", value=demodulation_config, expected_type=type_hints["demodulation_config"])
                check_type(argname="argument spectrum_config", value=spectrum_config, expected_type=type_hints["spectrum_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if decode_config is not None:
                self._values["decode_config"] = decode_config
            if demodulation_config is not None:
                self._values["demodulation_config"] = demodulation_config
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config

        @builtins.property
        def decode_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.DecodeConfigProperty"]]:
            '''Defines how the RF signal will be decoded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-decodeconfig
            '''
            result = self._values.get("decode_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.DecodeConfigProperty"]], result)

        @builtins.property
        def demodulation_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.DemodulationConfigProperty"]]:
            '''Defines how the RF signal will be demodulated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-demodulationconfig
            '''
            result = self._values.get("demodulation_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.DemodulationConfigProperty"]], result)

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.SpectrumConfigProperty"]]:
            '''Defines the spectrum configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.SpectrumConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaDownlinkDemodDecodeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.AntennaUplinkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "spectrum_config": "spectrumConfig",
            "target_eirp": "targetEirp",
            "transmit_disabled": "transmitDisabled",
        },
    )
    class AntennaUplinkConfigProperty:
        def __init__(
            self,
            *,
            spectrum_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.UplinkSpectrumConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            target_eirp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.EirpProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            transmit_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should configure an antenna for uplink during a contact.

            :param spectrum_config: Defines the spectrum configuration.
            :param target_eirp: The equivalent isotropically radiated power (EIRP) to use for uplink transmissions. Valid values are between 20.0 to 50.0 dBW.
            :param transmit_disabled: Whether or not uplink transmit is disabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                antenna_uplink_config_property = groundstation.CfnConfig.AntennaUplinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    ),
                    target_eirp=groundstation.CfnConfig.EirpProperty(
                        units="units",
                        value=123
                    ),
                    transmit_disabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55cd1298db9810d3b2cd585a075bd274d81baff7309375a8f1f1bcd888166878)
                check_type(argname="argument spectrum_config", value=spectrum_config, expected_type=type_hints["spectrum_config"])
                check_type(argname="argument target_eirp", value=target_eirp, expected_type=type_hints["target_eirp"])
                check_type(argname="argument transmit_disabled", value=transmit_disabled, expected_type=type_hints["transmit_disabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config
            if target_eirp is not None:
                self._values["target_eirp"] = target_eirp
            if transmit_disabled is not None:
                self._values["transmit_disabled"] = transmit_disabled

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.UplinkSpectrumConfigProperty"]]:
            '''Defines the spectrum configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.UplinkSpectrumConfigProperty"]], result)

        @builtins.property
        def target_eirp(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.EirpProperty"]]:
            '''The equivalent isotropically radiated power (EIRP) to use for uplink transmissions.

            Valid values are between 20.0 to 50.0 dBW.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-targeteirp
            '''
            result = self._values.get("target_eirp")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.EirpProperty"]], result)

        @builtins.property
        def transmit_disabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not uplink transmit is disabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-transmitdisabled
            '''
            result = self._values.get("transmit_disabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaUplinkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.ConfigDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "antenna_downlink_config": "antennaDownlinkConfig",
            "antenna_downlink_demod_decode_config": "antennaDownlinkDemodDecodeConfig",
            "antenna_uplink_config": "antennaUplinkConfig",
            "dataflow_endpoint_config": "dataflowEndpointConfig",
            "s3_recording_config": "s3RecordingConfig",
            "tracking_config": "trackingConfig",
            "uplink_echo_config": "uplinkEchoConfig",
        },
    )
    class ConfigDataProperty:
        def __init__(
            self,
            *,
            antenna_downlink_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.AntennaDownlinkConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            antenna_downlink_demod_decode_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.AntennaDownlinkDemodDecodeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            antenna_uplink_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.AntennaUplinkConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dataflow_endpoint_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.DataflowEndpointConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.S3RecordingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            tracking_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.TrackingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            uplink_echo_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.UplinkEchoConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Config objects provide information to Ground Station about how to configure the antenna and how data flows during a contact.

            :param antenna_downlink_config: Provides information for an antenna downlink config object. Antenna downlink config objects are used to provide parameters for downlinks where no demodulation or decoding is performed by Ground Station (RF over IP downlinks).
            :param antenna_downlink_demod_decode_config: Provides information for a downlink demod decode config object. Downlink demod decode config objects are used to provide parameters for downlinks where the Ground Station service will demodulate and decode the downlinked data.
            :param antenna_uplink_config: Provides information for an uplink config object. Uplink config objects are used to provide parameters for uplink contacts.
            :param dataflow_endpoint_config: Provides information for a dataflow endpoint config object. Dataflow endpoint config objects are used to provide parameters about which IP endpoint(s) to use during a contact. Dataflow endpoints are where Ground Station sends data during a downlink contact and where Ground Station receives data to send to the satellite during an uplink contact.
            :param s3_recording_config: Provides information for an S3 recording config object. S3 recording config objects are used to provide parameters for S3 recording during downlink contacts.
            :param tracking_config: Provides information for a tracking config object. Tracking config objects are used to provide parameters about how to track the satellite through the sky during a contact.
            :param uplink_echo_config: Provides information for an uplink echo config object. Uplink echo config objects are used to provide parameters for uplink echo during uplink contacts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                config_data_property = groundstation.CfnConfig.ConfigDataProperty(
                    antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                        decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        ),
                        target_eirp=groundstation.CfnConfig.EirpProperty(
                            units="units",
                            value=123
                        ),
                        transmit_disabled=False
                    ),
                    dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                        dataflow_endpoint_name="dataflowEndpointName",
                        dataflow_endpoint_region="dataflowEndpointRegion"
                    ),
                    s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                        bucket_arn="bucketArn",
                        prefix="prefix",
                        role_arn="roleArn"
                    ),
                    tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                        autotrack="autotrack"
                    ),
                    uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                        antenna_uplink_config_arn="antennaUplinkConfigArn",
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c161ef31a785b644c7c9cc8f223e10dcb0af1ba0e4a29303d7c17d85b3cbe192)
                check_type(argname="argument antenna_downlink_config", value=antenna_downlink_config, expected_type=type_hints["antenna_downlink_config"])
                check_type(argname="argument antenna_downlink_demod_decode_config", value=antenna_downlink_demod_decode_config, expected_type=type_hints["antenna_downlink_demod_decode_config"])
                check_type(argname="argument antenna_uplink_config", value=antenna_uplink_config, expected_type=type_hints["antenna_uplink_config"])
                check_type(argname="argument dataflow_endpoint_config", value=dataflow_endpoint_config, expected_type=type_hints["dataflow_endpoint_config"])
                check_type(argname="argument s3_recording_config", value=s3_recording_config, expected_type=type_hints["s3_recording_config"])
                check_type(argname="argument tracking_config", value=tracking_config, expected_type=type_hints["tracking_config"])
                check_type(argname="argument uplink_echo_config", value=uplink_echo_config, expected_type=type_hints["uplink_echo_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if antenna_downlink_config is not None:
                self._values["antenna_downlink_config"] = antenna_downlink_config
            if antenna_downlink_demod_decode_config is not None:
                self._values["antenna_downlink_demod_decode_config"] = antenna_downlink_demod_decode_config
            if antenna_uplink_config is not None:
                self._values["antenna_uplink_config"] = antenna_uplink_config
            if dataflow_endpoint_config is not None:
                self._values["dataflow_endpoint_config"] = dataflow_endpoint_config
            if s3_recording_config is not None:
                self._values["s3_recording_config"] = s3_recording_config
            if tracking_config is not None:
                self._values["tracking_config"] = tracking_config
            if uplink_echo_config is not None:
                self._values["uplink_echo_config"] = uplink_echo_config

        @builtins.property
        def antenna_downlink_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.AntennaDownlinkConfigProperty"]]:
            '''Provides information for an antenna downlink config object.

            Antenna downlink config objects are used to provide parameters for downlinks where no demodulation or decoding is performed by Ground Station (RF over IP downlinks).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennadownlinkconfig
            '''
            result = self._values.get("antenna_downlink_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.AntennaDownlinkConfigProperty"]], result)

        @builtins.property
        def antenna_downlink_demod_decode_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.AntennaDownlinkDemodDecodeConfigProperty"]]:
            '''Provides information for a downlink demod decode config object.

            Downlink demod decode config objects are used to provide parameters for downlinks where the Ground Station service will demodulate and decode the downlinked data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennadownlinkdemoddecodeconfig
            '''
            result = self._values.get("antenna_downlink_demod_decode_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.AntennaDownlinkDemodDecodeConfigProperty"]], result)

        @builtins.property
        def antenna_uplink_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.AntennaUplinkConfigProperty"]]:
            '''Provides information for an uplink config object.

            Uplink config objects are used to provide parameters for uplink contacts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennauplinkconfig
            '''
            result = self._values.get("antenna_uplink_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.AntennaUplinkConfigProperty"]], result)

        @builtins.property
        def dataflow_endpoint_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.DataflowEndpointConfigProperty"]]:
            '''Provides information for a dataflow endpoint config object.

            Dataflow endpoint config objects are used to provide parameters about which IP endpoint(s) to use during a contact. Dataflow endpoints are where Ground Station sends data during a downlink contact and where Ground Station receives data to send to the satellite during an uplink contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-dataflowendpointconfig
            '''
            result = self._values.get("dataflow_endpoint_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.DataflowEndpointConfigProperty"]], result)

        @builtins.property
        def s3_recording_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.S3RecordingConfigProperty"]]:
            '''Provides information for an S3 recording config object.

            S3 recording config objects are used to provide parameters for S3 recording during downlink contacts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-s3recordingconfig
            '''
            result = self._values.get("s3_recording_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.S3RecordingConfigProperty"]], result)

        @builtins.property
        def tracking_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.TrackingConfigProperty"]]:
            '''Provides information for a tracking config object.

            Tracking config objects are used to provide parameters about how to track the satellite through the sky during a contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-trackingconfig
            '''
            result = self._values.get("tracking_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.TrackingConfigProperty"]], result)

        @builtins.property
        def uplink_echo_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.UplinkEchoConfigProperty"]]:
            '''Provides information for an uplink echo config object.

            Uplink echo config objects are used to provide parameters for uplink echo during uplink contacts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-uplinkechoconfig
            '''
            result = self._values.get("uplink_echo_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.UplinkEchoConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.DataflowEndpointConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dataflow_endpoint_name": "dataflowEndpointName",
            "dataflow_endpoint_region": "dataflowEndpointRegion",
        },
    )
    class DataflowEndpointConfigProperty:
        def __init__(
            self,
            *,
            dataflow_endpoint_name: typing.Optional[builtins.str] = None,
            dataflow_endpoint_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information to AWS Ground Station about which IP endpoints to use during a contact.

            :param dataflow_endpoint_name: The name of the dataflow endpoint to use during contacts.
            :param dataflow_endpoint_region: The region of the dataflow endpoint to use during contacts. When omitted, Ground Station will use the region of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                dataflow_endpoint_config_property = groundstation.CfnConfig.DataflowEndpointConfigProperty(
                    dataflow_endpoint_name="dataflowEndpointName",
                    dataflow_endpoint_region="dataflowEndpointRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__99a763bb26b6623e715887bdc54f3c7ceed9bfb9f5a794e1721c1518d6679eae)
                check_type(argname="argument dataflow_endpoint_name", value=dataflow_endpoint_name, expected_type=type_hints["dataflow_endpoint_name"])
                check_type(argname="argument dataflow_endpoint_region", value=dataflow_endpoint_region, expected_type=type_hints["dataflow_endpoint_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dataflow_endpoint_name is not None:
                self._values["dataflow_endpoint_name"] = dataflow_endpoint_name
            if dataflow_endpoint_region is not None:
                self._values["dataflow_endpoint_region"] = dataflow_endpoint_region

        @builtins.property
        def dataflow_endpoint_name(self) -> typing.Optional[builtins.str]:
            '''The name of the dataflow endpoint to use during contacts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointname
            '''
            result = self._values.get("dataflow_endpoint_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dataflow_endpoint_region(self) -> typing.Optional[builtins.str]:
            '''The region of the dataflow endpoint to use during contacts.

            When omitted, Ground Station will use the region of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointregion
            '''
            result = self._values.get("dataflow_endpoint_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEndpointConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.DecodeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"unvalidated_json": "unvalidatedJson"},
    )
    class DecodeConfigProperty:
        def __init__(
            self,
            *,
            unvalidated_json: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines decoding settings.

            :param unvalidated_json: The decoding settings are in JSON format and define a set of steps to perform to decode the data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                decode_config_property = groundstation.CfnConfig.DecodeConfigProperty(
                    unvalidated_json="unvalidatedJson"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__324f5ec78c0ce70a0c2b16edd19232cbe81a59b2c1577339462358e74d607c12)
                check_type(argname="argument unvalidated_json", value=unvalidated_json, expected_type=type_hints["unvalidated_json"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if unvalidated_json is not None:
                self._values["unvalidated_json"] = unvalidated_json

        @builtins.property
        def unvalidated_json(self) -> typing.Optional[builtins.str]:
            '''The decoding settings are in JSON format and define a set of steps to perform to decode the data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html#cfn-groundstation-config-decodeconfig-unvalidatedjson
            '''
            result = self._values.get("unvalidated_json")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DecodeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.DemodulationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"unvalidated_json": "unvalidatedJson"},
    )
    class DemodulationConfigProperty:
        def __init__(
            self,
            *,
            unvalidated_json: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines demodulation settings.

            :param unvalidated_json: The demodulation settings are in JSON format and define parameters for demodulation, for example which modulation scheme (e.g. PSK, QPSK, etc.) and matched filter to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                demodulation_config_property = groundstation.CfnConfig.DemodulationConfigProperty(
                    unvalidated_json="unvalidatedJson"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41995b227ea3e4e9f0b14b63def99efc04e280b4295dd4e9584328affb2eb70e)
                check_type(argname="argument unvalidated_json", value=unvalidated_json, expected_type=type_hints["unvalidated_json"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if unvalidated_json is not None:
                self._values["unvalidated_json"] = unvalidated_json

        @builtins.property
        def unvalidated_json(self) -> typing.Optional[builtins.str]:
            '''The demodulation settings are in JSON format and define parameters for demodulation, for example which modulation scheme (e.g. PSK, QPSK, etc.) and matched filter to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html#cfn-groundstation-config-demodulationconfig-unvalidatedjson
            '''
            result = self._values.get("unvalidated_json")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DemodulationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.EirpProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class EirpProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Defines an equivalent isotropically radiated power (EIRP).

            :param units: The units of the EIRP.
            :param value: The value of the EIRP. Valid values are between 20.0 to 50.0 dBW.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                eirp_property = groundstation.CfnConfig.EirpProperty(
                    units="units",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c514bdd7e81420fa1de45f624e9738b0420c9e0adc054d3749c647a5f1a0b336)
                check_type(argname="argument units", value=units, expected_type=type_hints["units"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''The units of the EIRP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html#cfn-groundstation-config-eirp-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The value of the EIRP.

            Valid values are between 20.0 to 50.0 dBW.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html#cfn-groundstation-config-eirp-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EirpProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.FrequencyBandwidthProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class FrequencyBandwidthProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Defines a bandwidth.

            :param units: The units of the bandwidth.
            :param value: The value of the bandwidth. AWS Ground Station currently has the following bandwidth limitations:. - For ``AntennaDownlinkDemodDecodeconfig`` , valid values are between 125 kHz to 650 MHz. - For ``AntennaDownlinkconfig`` , valid values are between 10 kHz to 54 MHz. - For ``AntennaUplinkConfig`` , valid values are between 10 kHz to 54 MHz.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                frequency_bandwidth_property = groundstation.CfnConfig.FrequencyBandwidthProperty(
                    units="units",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6607539aa17b23364cc0c5de62d53ab10b2588b4a397b71ff9a1510aefbc8763)
                check_type(argname="argument units", value=units, expected_type=type_hints["units"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''The units of the bandwidth.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html#cfn-groundstation-config-frequencybandwidth-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The value of the bandwidth. AWS Ground Station currently has the following bandwidth limitations:.

            - For ``AntennaDownlinkDemodDecodeconfig`` , valid values are between 125 kHz to 650 MHz.
            - For ``AntennaDownlinkconfig`` , valid values are between 10 kHz to 54 MHz.
            - For ``AntennaUplinkConfig`` , valid values are between 10 kHz to 54 MHz.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html#cfn-groundstation-config-frequencybandwidth-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrequencyBandwidthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.FrequencyProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class FrequencyProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Defines a frequency.

            :param units: The units of the frequency.
            :param value: The value of the frequency. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                frequency_property = groundstation.CfnConfig.FrequencyProperty(
                    units="units",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__54cacafc58427db742615b0fe5104ac687a9a80afc40f92de682c2897f73b0f5)
                check_type(argname="argument units", value=units, expected_type=type_hints["units"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''The units of the frequency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html#cfn-groundstation-config-frequency-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The value of the frequency.

            Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html#cfn-groundstation-config-frequency-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrequencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.S3RecordingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "prefix": "prefix",
            "role_arn": "roleArn",
        },
    )
    class S3RecordingConfigProperty:
        def __init__(
            self,
            *,
            bucket_arn: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should save downlink data to S3.

            :param bucket_arn: S3 Bucket where the data is written. The name of the S3 Bucket provided must begin with ``aws-groundstation`` .
            :param prefix: The prefix of the S3 data object. If you choose to use any optional keys for substitution, these values will be replaced with the corresponding information from your contact details. For example, a prefix of ``{satellite_id}/{year}/{month}/{day}/`` will replaced with ``fake_satellite_id/2021/01/10/`` *Optional keys for substitution* : ``{satellite_id}`` | ``{config-name}`` | ``{config-id}`` | ``{year}`` | ``{month}`` | ``{day}``
            :param role_arn: Defines the ARN of the role assumed for putting archives to S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                s3_recording_config_property = groundstation.CfnConfig.S3RecordingConfigProperty(
                    bucket_arn="bucketArn",
                    prefix="prefix",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a434f8f9b58e6e79e140ec69b10fe3b638c9dd796407130b206d6328c3b092d3)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_arn is not None:
                self._values["bucket_arn"] = bucket_arn
            if prefix is not None:
                self._values["prefix"] = prefix
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def bucket_arn(self) -> typing.Optional[builtins.str]:
            '''S3 Bucket where the data is written.

            The name of the S3 Bucket provided must begin with ``aws-groundstation`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-bucketarn
            '''
            result = self._values.get("bucket_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The prefix of the S3 data object.

            If you choose to use any optional keys for substitution, these values will be replaced with the corresponding information from your contact details. For example, a prefix of ``{satellite_id}/{year}/{month}/{day}/`` will replaced with ``fake_satellite_id/2021/01/10/``

            *Optional keys for substitution* : ``{satellite_id}`` | ``{config-name}`` | ``{config-id}`` | ``{year}`` | ``{month}`` | ``{day}``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''Defines the ARN of the role assumed for putting archives to S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3RecordingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.SpectrumConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bandwidth": "bandwidth",
            "center_frequency": "centerFrequency",
            "polarization": "polarization",
        },
    )
    class SpectrumConfigProperty:
        def __init__(
            self,
            *,
            bandwidth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.FrequencyBandwidthProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            center_frequency: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.FrequencyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            polarization: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a spectrum.

            :param bandwidth: The bandwidth of the spectrum. AWS Ground Station currently has the following bandwidth limitations:. - For ``AntennaDownlinkDemodDecodeconfig`` , valid values are between 125 kHz to 650 MHz. - For ``AntennaDownlinkconfig`` , valid values are between 10 kHz to 54 MHz. - For ``AntennaUplinkConfig`` , valid values are between 10 kHz to 54 MHz.
            :param center_frequency: The center frequency of the spectrum. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.
            :param polarization: The polarization of the spectrum. Valid values are ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` . Capturing both ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` polarization requires two separate configs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                spectrum_config_property = groundstation.CfnConfig.SpectrumConfigProperty(
                    bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                        units="units",
                        value=123
                    ),
                    center_frequency=groundstation.CfnConfig.FrequencyProperty(
                        units="units",
                        value=123
                    ),
                    polarization="polarization"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cdff7bad914262ea88134e28b4653bf1192cb3dab1012e32f318a75dba095e8a)
                check_type(argname="argument bandwidth", value=bandwidth, expected_type=type_hints["bandwidth"])
                check_type(argname="argument center_frequency", value=center_frequency, expected_type=type_hints["center_frequency"])
                check_type(argname="argument polarization", value=polarization, expected_type=type_hints["polarization"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bandwidth is not None:
                self._values["bandwidth"] = bandwidth
            if center_frequency is not None:
                self._values["center_frequency"] = center_frequency
            if polarization is not None:
                self._values["polarization"] = polarization

        @builtins.property
        def bandwidth(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.FrequencyBandwidthProperty"]]:
            '''The bandwidth of the spectrum. AWS Ground Station currently has the following bandwidth limitations:.

            - For ``AntennaDownlinkDemodDecodeconfig`` , valid values are between 125 kHz to 650 MHz.
            - For ``AntennaDownlinkconfig`` , valid values are between 10 kHz to 54 MHz.
            - For ``AntennaUplinkConfig`` , valid values are between 10 kHz to 54 MHz.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-bandwidth
            '''
            result = self._values.get("bandwidth")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.FrequencyBandwidthProperty"]], result)

        @builtins.property
        def center_frequency(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.FrequencyProperty"]]:
            '''The center frequency of the spectrum.

            Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-centerfrequency
            '''
            result = self._values.get("center_frequency")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.FrequencyProperty"]], result)

        @builtins.property
        def polarization(self) -> typing.Optional[builtins.str]:
            '''The polarization of the spectrum.

            Valid values are ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` . Capturing both ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` polarization requires two separate configs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-polarization
            '''
            result = self._values.get("polarization")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpectrumConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.TrackingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"autotrack": "autotrack"},
    )
    class TrackingConfigProperty:
        def __init__(self, *, autotrack: typing.Optional[builtins.str] = None) -> None:
            '''Provides information about how AWS Ground Station should track the satellite through the sky during a contact.

            :param autotrack: Specifies whether or not to use autotrack. ``REMOVED`` specifies that program track should only be used during the contact. ``PREFERRED`` specifies that autotracking is preferred during the contact but fallback to program track if the signal is lost. ``REQUIRED`` specifies that autotracking is required during the contact and not to use program track if the signal is lost.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                tracking_config_property = groundstation.CfnConfig.TrackingConfigProperty(
                    autotrack="autotrack"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed1a7eb46212500aac5b18d6aa5e4a9a69548192e39da2f23d9e5d6301bcd6ac)
                check_type(argname="argument autotrack", value=autotrack, expected_type=type_hints["autotrack"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if autotrack is not None:
                self._values["autotrack"] = autotrack

        @builtins.property
        def autotrack(self) -> typing.Optional[builtins.str]:
            '''Specifies whether or not to use autotrack.

            ``REMOVED`` specifies that program track should only be used during the contact. ``PREFERRED`` specifies that autotracking is preferred during the contact but fallback to program track if the signal is lost. ``REQUIRED`` specifies that autotracking is required during the contact and not to use program track if the signal is lost.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html#cfn-groundstation-config-trackingconfig-autotrack
            '''
            result = self._values.get("autotrack")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrackingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.UplinkEchoConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "antenna_uplink_config_arn": "antennaUplinkConfigArn",
            "enabled": "enabled",
        },
    )
    class UplinkEchoConfigProperty:
        def __init__(
            self,
            *,
            antenna_uplink_config_arn: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Provides information about how AWS Ground Station should echo back uplink transmissions to a dataflow endpoint.

            :param antenna_uplink_config_arn: Defines the ARN of the uplink config to echo back to a dataflow endpoint.
            :param enabled: Whether or not uplink echo is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                uplink_echo_config_property = groundstation.CfnConfig.UplinkEchoConfigProperty(
                    antenna_uplink_config_arn="antennaUplinkConfigArn",
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__193d0e509b29608b5001e27835cf0767adff51dea5067bffff37a3d9d26ae405)
                check_type(argname="argument antenna_uplink_config_arn", value=antenna_uplink_config_arn, expected_type=type_hints["antenna_uplink_config_arn"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if antenna_uplink_config_arn is not None:
                self._values["antenna_uplink_config_arn"] = antenna_uplink_config_arn
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def antenna_uplink_config_arn(self) -> typing.Optional[builtins.str]:
            '''Defines the ARN of the uplink config to echo back to a dataflow endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html#cfn-groundstation-config-uplinkechoconfig-antennauplinkconfigarn
            '''
            result = self._values.get("antenna_uplink_config_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not uplink echo is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html#cfn-groundstation-config-uplinkechoconfig-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UplinkEchoConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.UplinkSpectrumConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "center_frequency": "centerFrequency",
            "polarization": "polarization",
        },
    )
    class UplinkSpectrumConfigProperty:
        def __init__(
            self,
            *,
            center_frequency: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfig.FrequencyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            polarization: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a uplink spectrum.

            :param center_frequency: The center frequency of the spectrum. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.
            :param polarization: The polarization of the spectrum. Valid values are ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                uplink_spectrum_config_property = groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                    center_frequency=groundstation.CfnConfig.FrequencyProperty(
                        units="units",
                        value=123
                    ),
                    polarization="polarization"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__27edccf82a0971febe19a69f59300574fa0a8a86e8860e33b5b5b5fac0eafdbc)
                check_type(argname="argument center_frequency", value=center_frequency, expected_type=type_hints["center_frequency"])
                check_type(argname="argument polarization", value=polarization, expected_type=type_hints["polarization"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if center_frequency is not None:
                self._values["center_frequency"] = center_frequency
            if polarization is not None:
                self._values["polarization"] = polarization

        @builtins.property
        def center_frequency(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.FrequencyProperty"]]:
            '''The center frequency of the spectrum.

            Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html#cfn-groundstation-config-uplinkspectrumconfig-centerfrequency
            '''
            result = self._values.get("center_frequency")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfig.FrequencyProperty"]], result)

        @builtins.property
        def polarization(self) -> typing.Optional[builtins.str]:
            '''The polarization of the spectrum.

            Valid values are ``"RIGHT_HAND"`` and ``"LEFT_HAND"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html#cfn-groundstation-config-uplinkspectrumconfig-polarization
            '''
            result = self._values.get("polarization")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UplinkSpectrumConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_groundstation.CfnConfigProps",
    jsii_struct_bases=[],
    name_mapping={"config_data": "configData", "name": "name", "tags": "tags"},
)
class CfnConfigProps:
    def __init__(
        self,
        *,
        config_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.ConfigDataProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfig``.

        :param config_data: Object containing the parameters of a config. Only one subtype may be specified per config. See the subtype definitions for a description of each config subtype.
        :param name: The name of the config object.
        :param tags: Tags assigned to a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_groundstation as groundstation
            
            cfn_config_props = groundstation.CfnConfigProps(
                config_data=groundstation.CfnConfig.ConfigDataProperty(
                    antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                        decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        ),
                        target_eirp=groundstation.CfnConfig.EirpProperty(
                            units="units",
                            value=123
                        ),
                        transmit_disabled=False
                    ),
                    dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                        dataflow_endpoint_name="dataflowEndpointName",
                        dataflow_endpoint_region="dataflowEndpointRegion"
                    ),
                    s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                        bucket_arn="bucketArn",
                        prefix="prefix",
                        role_arn="roleArn"
                    ),
                    tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                        autotrack="autotrack"
                    ),
                    uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                        antenna_uplink_config_arn="antennaUplinkConfigArn",
                        enabled=False
                    )
                ),
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed41d945f02014619043ab4e725d6fc3de8df5c042bab0ce35128c1603f4ea25)
            check_type(argname="argument config_data", value=config_data, expected_type=type_hints["config_data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_data": config_data,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def config_data(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConfig.ConfigDataProperty]:
        '''Object containing the parameters of a config.

        Only one subtype may be specified per config. See the subtype definitions for a description of each config subtype.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-configdata
        '''
        result = self._values.get("config_data")
        assert result is not None, "Required property 'config_data' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConfig.ConfigDataProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the config object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags assigned to a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDataflowEndpointGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup",
):
    '''Creates a Dataflow Endpoint Group request.

    Dataflow endpoint groups contain a list of endpoints. When the name of a dataflow endpoint group is specified in a mission profile, the Ground Station service will connect to the endpoints and flow data during a contact.

    For more information about dataflow endpoint groups, see `Dataflow Endpoint Groups <https://docs.aws.amazon.com/ground-station/latest/ug/dataflowendpointgroups.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_groundstation as groundstation
        
        cfn_dataflow_endpoint_group = groundstation.CfnDataflowEndpointGroup(self, "MyCfnDataflowEndpointGroup",
            endpoint_details=[groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                aws_ground_station_agent_endpoint=groundstation.CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty(
                    agent_status="agentStatus",
                    audit_results="auditResults",
                    egress_address=groundstation.CfnDataflowEndpointGroup.ConnectionDetailsProperty(
                        mtu=123,
                        socket_address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                            name="name",
                            port=123
                        )
                    ),
                    ingress_address=groundstation.CfnDataflowEndpointGroup.RangedConnectionDetailsProperty(
                        mtu=123,
                        socket_address=groundstation.CfnDataflowEndpointGroup.RangedSocketAddressProperty(
                            name="name",
                            port_range=groundstation.CfnDataflowEndpointGroup.IntegerRangeProperty(
                                maximum=123,
                                minimum=123
                            )
                        )
                    ),
                    name="name"
                ),
                endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                    address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                        name="name",
                        port=123
                    ),
                    mtu=123,
                    name="name"
                ),
                security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )],
        
            # the properties below are optional
            contact_post_pass_duration_seconds=123,
            contact_pre_pass_duration_seconds=123,
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
        endpoint_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", typing.Dict[builtins.str, typing.Any]]]]],
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param endpoint_details: List of Endpoint Details, containing address and port for each endpoint.
        :param contact_post_pass_duration_seconds: Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a ``POSTPASS`` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the ``POSTPASS`` state.
        :param contact_pre_pass_duration_seconds: Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a ``PREPASS`` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the ``PREPASS`` state.
        :param tags: Tags assigned to a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__669b82a6c91e9541f061b9397341fc4b6628a648faf22449b040ab31e2879b6f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataflowEndpointGroupProps(
            endpoint_details=endpoint_details,
            contact_post_pass_duration_seconds=contact_post_pass_duration_seconds,
            contact_pre_pass_duration_seconds=contact_pre_pass_duration_seconds,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17d9bea099cdcd1099da7284180003b79769ad1588e3964f28fb913d498709f5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__301a06069694a715f2320416d1088ceb197833a8e20246ccb97b1aa5fb5dbb31)
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
        '''The ARN of the dataflow endpoint group, such as ``arn:aws:groundstation:us-east-2:1234567890:dataflow-endpoint-group/9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''UUID of a dataflow endpoint group.

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
    @jsii.member(jsii_name="endpointDetails")
    def endpoint_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.EndpointDetailsProperty"]]]:
        '''List of Endpoint Details, containing address and port for each endpoint.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.EndpointDetailsProperty"]]], jsii.get(self, "endpointDetails"))

    @endpoint_details.setter
    def endpoint_details(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.EndpointDetailsProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__605270fdb212e4afd622fd5047d2f46f173b44dc28a4370f48d78fa181366952)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointDetails", value)

    @builtins.property
    @jsii.member(jsii_name="contactPostPassDurationSeconds")
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a ``POSTPASS`` state.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPostPassDurationSeconds"))

    @contact_post_pass_duration_seconds.setter
    def contact_post_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25ef1c7229baacb918baea79312842d531006cf929111fa27c27bd2a0f2730f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPostPassDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="contactPrePassDurationSeconds")
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a ``PREPASS`` state.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPrePassDurationSeconds"))

    @contact_pre_pass_duration_seconds.setter
    def contact_pre_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d824833236777cd2417ffad0f69012adcf6aab076829d4fc012bb6bf35c092f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPrePassDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags assigned to a resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91f97011b987224f8e61448ddca1df20f67e7b2188ee8ce55208bdeb4bbc53a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "agent_status": "agentStatus",
            "audit_results": "auditResults",
            "egress_address": "egressAddress",
            "ingress_address": "ingressAddress",
            "name": "name",
        },
    )
    class AwsGroundStationAgentEndpointProperty:
        def __init__(
            self,
            *,
            agent_status: typing.Optional[builtins.str] = None,
            audit_results: typing.Optional[builtins.str] = None,
            egress_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.ConnectionDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ingress_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.RangedConnectionDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param agent_status: 
            :param audit_results: 
            :param egress_address: 
            :param ingress_address: 
            :param name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                aws_ground_station_agent_endpoint_property = groundstation.CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty(
                    agent_status="agentStatus",
                    audit_results="auditResults",
                    egress_address=groundstation.CfnDataflowEndpointGroup.ConnectionDetailsProperty(
                        mtu=123,
                        socket_address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                            name="name",
                            port=123
                        )
                    ),
                    ingress_address=groundstation.CfnDataflowEndpointGroup.RangedConnectionDetailsProperty(
                        mtu=123,
                        socket_address=groundstation.CfnDataflowEndpointGroup.RangedSocketAddressProperty(
                            name="name",
                            port_range=groundstation.CfnDataflowEndpointGroup.IntegerRangeProperty(
                                maximum=123,
                                minimum=123
                            )
                        )
                    ),
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ee0748f1ecb5781e9a01db9f02fc9c03f466d2eb8031790fd920a9b59c3a7efe)
                check_type(argname="argument agent_status", value=agent_status, expected_type=type_hints["agent_status"])
                check_type(argname="argument audit_results", value=audit_results, expected_type=type_hints["audit_results"])
                check_type(argname="argument egress_address", value=egress_address, expected_type=type_hints["egress_address"])
                check_type(argname="argument ingress_address", value=ingress_address, expected_type=type_hints["ingress_address"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if agent_status is not None:
                self._values["agent_status"] = agent_status
            if audit_results is not None:
                self._values["audit_results"] = audit_results
            if egress_address is not None:
                self._values["egress_address"] = egress_address
            if ingress_address is not None:
                self._values["ingress_address"] = ingress_address
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def agent_status(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-agentstatus
            '''
            result = self._values.get("agent_status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audit_results(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-auditresults
            '''
            result = self._values.get("audit_results")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def egress_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.ConnectionDetailsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-egressaddress
            '''
            result = self._values.get("egress_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.ConnectionDetailsProperty"]], result)

        @builtins.property
        def ingress_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.RangedConnectionDetailsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-ingressaddress
            '''
            result = self._values.get("ingress_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.RangedConnectionDetailsProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsGroundStationAgentEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.ConnectionDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"mtu": "mtu", "socket_address": "socketAddress"},
    )
    class ConnectionDetailsProperty:
        def __init__(
            self,
            *,
            mtu: typing.Optional[jsii.Number] = None,
            socket_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.SocketAddressProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param mtu: 
            :param socket_address: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-connectiondetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                connection_details_property = groundstation.CfnDataflowEndpointGroup.ConnectionDetailsProperty(
                    mtu=123,
                    socket_address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                        name="name",
                        port=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac92ba18922e7f50fbd2fb44b481647516ad2ecad36a6ecdb41418e911572b8c)
                check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
                check_type(argname="argument socket_address", value=socket_address, expected_type=type_hints["socket_address"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if mtu is not None:
                self._values["mtu"] = mtu
            if socket_address is not None:
                self._values["socket_address"] = socket_address

        @builtins.property
        def mtu(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-connectiondetails.html#cfn-groundstation-dataflowendpointgroup-connectiondetails-mtu
            '''
            result = self._values.get("mtu")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def socket_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.SocketAddressProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-connectiondetails.html#cfn-groundstation-dataflowendpointgroup-connectiondetails-socketaddress
            '''
            result = self._values.get("socket_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.SocketAddressProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "mtu": "mtu", "name": "name"},
    )
    class DataflowEndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.SocketAddressProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mtu: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information such as socket address and name that defines an endpoint.

            :param address: The address and port of an endpoint.
            :param mtu: Maximum transmission unit (MTU) size in bytes of a dataflow endpoint. Valid values are between 1400 and 1500. A default value of 1500 is used if not set.
            :param name: The endpoint name. When listing available contacts for a satellite, Ground Station searches for a dataflow endpoint whose name matches the value specified by the dataflow endpoint config of the selected mission profile. If no matching dataflow endpoints are found then Ground Station will not display any available contacts for the satellite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                dataflow_endpoint_property = groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                    address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                        name="name",
                        port=123
                    ),
                    mtu=123,
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc9f5226d94e906b56ccb5e58d75ed0e8d68881429608741bde8890f51ab8be0)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if mtu is not None:
                self._values["mtu"] = mtu
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.SocketAddressProperty"]]:
            '''The address and port of an endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.SocketAddressProperty"]], result)

        @builtins.property
        def mtu(self) -> typing.Optional[jsii.Number]:
            '''Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.

            Valid values are between 1400 and 1500. A default value of 1500 is used if not set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-mtu
            '''
            result = self._values.get("mtu")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The endpoint name.

            When listing available contacts for a satellite, Ground Station searches for a dataflow endpoint whose name matches the value specified by the dataflow endpoint config of the selected mission profile. If no matching dataflow endpoints are found then Ground Station will not display any available contacts for the satellite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_ground_station_agent_endpoint": "awsGroundStationAgentEndpoint",
            "endpoint": "endpoint",
            "security_details": "securityDetails",
        },
    )
    class EndpointDetailsProperty:
        def __init__(
            self,
            *,
            aws_ground_station_agent_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.DataflowEndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            security_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.SecurityDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The security details and endpoint information.

            :param aws_ground_station_agent_endpoint: 
            :param endpoint: Information about the endpoint such as name and the endpoint address.
            :param security_details: The role ARN, and IDs for security groups and subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                endpoint_details_property = groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                    aws_ground_station_agent_endpoint=groundstation.CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty(
                        agent_status="agentStatus",
                        audit_results="auditResults",
                        egress_address=groundstation.CfnDataflowEndpointGroup.ConnectionDetailsProperty(
                            mtu=123,
                            socket_address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                                name="name",
                                port=123
                            )
                        ),
                        ingress_address=groundstation.CfnDataflowEndpointGroup.RangedConnectionDetailsProperty(
                            mtu=123,
                            socket_address=groundstation.CfnDataflowEndpointGroup.RangedSocketAddressProperty(
                                name="name",
                                port_range=groundstation.CfnDataflowEndpointGroup.IntegerRangeProperty(
                                    maximum=123,
                                    minimum=123
                                )
                            )
                        ),
                        name="name"
                    ),
                    endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                        address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                            name="name",
                            port=123
                        ),
                        mtu=123,
                        name="name"
                    ),
                    security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce6c1b639a398c895dfc66055f50eec9eabd79db1d993d794e1fd73150b96712)
                check_type(argname="argument aws_ground_station_agent_endpoint", value=aws_ground_station_agent_endpoint, expected_type=type_hints["aws_ground_station_agent_endpoint"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument security_details", value=security_details, expected_type=type_hints["security_details"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_ground_station_agent_endpoint is not None:
                self._values["aws_ground_station_agent_endpoint"] = aws_ground_station_agent_endpoint
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if security_details is not None:
                self._values["security_details"] = security_details

        @builtins.property
        def aws_ground_station_agent_endpoint(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-awsgroundstationagentendpoint
            '''
            result = self._values.get("aws_ground_station_agent_endpoint")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty"]], result)

        @builtins.property
        def endpoint(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.DataflowEndpointProperty"]]:
            '''Information about the endpoint such as name and the endpoint address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.DataflowEndpointProperty"]], result)

        @builtins.property
        def security_details(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.SecurityDetailsProperty"]]:
            '''The role ARN, and IDs for security groups and subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-securitydetails
            '''
            result = self._values.get("security_details")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.SecurityDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.IntegerRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"maximum": "maximum", "minimum": "minimum"},
    )
    class IntegerRangeProperty:
        def __init__(
            self,
            *,
            maximum: typing.Optional[jsii.Number] = None,
            minimum: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param maximum: 
            :param minimum: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-integerrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                integer_range_property = groundstation.CfnDataflowEndpointGroup.IntegerRangeProperty(
                    maximum=123,
                    minimum=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b49c491018c49abebdb9e07f6263ac4ee58dd70f1dde65fa0408a3d33522a05a)
                check_type(argname="argument maximum", value=maximum, expected_type=type_hints["maximum"])
                check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if maximum is not None:
                self._values["maximum"] = maximum
            if minimum is not None:
                self._values["minimum"] = minimum

        @builtins.property
        def maximum(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-integerrange.html#cfn-groundstation-dataflowendpointgroup-integerrange-maximum
            '''
            result = self._values.get("maximum")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-integerrange.html#cfn-groundstation-dataflowendpointgroup-integerrange-minimum
            '''
            result = self._values.get("minimum")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegerRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.RangedConnectionDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"mtu": "mtu", "socket_address": "socketAddress"},
    )
    class RangedConnectionDetailsProperty:
        def __init__(
            self,
            *,
            mtu: typing.Optional[jsii.Number] = None,
            socket_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.RangedSocketAddressProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param mtu: 
            :param socket_address: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedconnectiondetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                ranged_connection_details_property = groundstation.CfnDataflowEndpointGroup.RangedConnectionDetailsProperty(
                    mtu=123,
                    socket_address=groundstation.CfnDataflowEndpointGroup.RangedSocketAddressProperty(
                        name="name",
                        port_range=groundstation.CfnDataflowEndpointGroup.IntegerRangeProperty(
                            maximum=123,
                            minimum=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f4718a299592e9341c9edaea65909a5d521ddfd0baf97317c55e21c1a1cde5b4)
                check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
                check_type(argname="argument socket_address", value=socket_address, expected_type=type_hints["socket_address"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if mtu is not None:
                self._values["mtu"] = mtu
            if socket_address is not None:
                self._values["socket_address"] = socket_address

        @builtins.property
        def mtu(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedconnectiondetails.html#cfn-groundstation-dataflowendpointgroup-rangedconnectiondetails-mtu
            '''
            result = self._values.get("mtu")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def socket_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.RangedSocketAddressProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedconnectiondetails.html#cfn-groundstation-dataflowendpointgroup-rangedconnectiondetails-socketaddress
            '''
            result = self._values.get("socket_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.RangedSocketAddressProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RangedConnectionDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.RangedSocketAddressProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "port_range": "portRange"},
    )
    class RangedSocketAddressProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataflowEndpointGroup.IntegerRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param name: 
            :param port_range: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                ranged_socket_address_property = groundstation.CfnDataflowEndpointGroup.RangedSocketAddressProperty(
                    name="name",
                    port_range=groundstation.CfnDataflowEndpointGroup.IntegerRangeProperty(
                        maximum=123,
                        minimum=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0279ec5e3dff22baf12b2c0289e5035186ce86688371a640b24790d608a5b33)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if port_range is not None:
                self._values["port_range"] = port_range

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress.html#cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port_range(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.IntegerRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress.html#cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-portrange
            '''
            result = self._values.get("port_range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataflowEndpointGroup.IntegerRangeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RangedSocketAddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class SecurityDetailsProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Information about IAM roles, subnets, and security groups needed for this DataflowEndpointGroup.

            :param role_arn: The ARN of a role which Ground Station has permission to assume, such as ``arn:aws:iam::1234567890:role/DataDeliveryServiceRole`` . Ground Station will assume this role and create an ENI in your VPC on the specified subnet upon creation of a dataflow endpoint group. This ENI is used as the ingress/egress point for data streamed during a satellite contact.
            :param security_group_ids: The security group Ids of the security role, such as ``sg-1234567890abcdef0`` .
            :param subnet_ids: The subnet Ids of the security details, such as ``subnet-12345678`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                security_details_property = groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__220180d1b2cf36fe04713aaee0c3fe3a558c4c874399dd27305560fd323a8137)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of a role which Ground Station has permission to assume, such as ``arn:aws:iam::1234567890:role/DataDeliveryServiceRole`` .

            Ground Station will assume this role and create an ENI in your VPC on the specified subnet upon creation of a dataflow endpoint group. This ENI is used as the ingress/egress point for data streamed during a satellite contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The security group Ids of the security role, such as ``sg-1234567890abcdef0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The subnet Ids of the security details, such as ``subnet-12345678`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecurityDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.SocketAddressProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "port": "port"},
    )
    class SocketAddressProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The address of the endpoint, such as ``192.168.1.1`` .

            :param name: The name of the endpoint, such as ``Endpoint 1`` .
            :param port: The port of the endpoint, such as ``55888`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                socket_address_property = groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                    name="name",
                    port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0be1cdd898189d7b0a27924e382d426d33c11750a250da2b52f6b3ef9e323767)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the endpoint, such as ``Endpoint 1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html#cfn-groundstation-dataflowendpointgroup-socketaddress-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port of the endpoint, such as ``55888`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html#cfn-groundstation-dataflowendpointgroup-socketaddress-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SocketAddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_details": "endpointDetails",
        "contact_post_pass_duration_seconds": "contactPostPassDurationSeconds",
        "contact_pre_pass_duration_seconds": "contactPrePassDurationSeconds",
        "tags": "tags",
    },
)
class CfnDataflowEndpointGroupProps:
    def __init__(
        self,
        *,
        endpoint_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]]]]],
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataflowEndpointGroup``.

        :param endpoint_details: List of Endpoint Details, containing address and port for each endpoint.
        :param contact_post_pass_duration_seconds: Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a ``POSTPASS`` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the ``POSTPASS`` state.
        :param contact_pre_pass_duration_seconds: Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a ``PREPASS`` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the ``PREPASS`` state.
        :param tags: Tags assigned to a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_groundstation as groundstation
            
            cfn_dataflow_endpoint_group_props = groundstation.CfnDataflowEndpointGroupProps(
                endpoint_details=[groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                    aws_ground_station_agent_endpoint=groundstation.CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty(
                        agent_status="agentStatus",
                        audit_results="auditResults",
                        egress_address=groundstation.CfnDataflowEndpointGroup.ConnectionDetailsProperty(
                            mtu=123,
                            socket_address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                                name="name",
                                port=123
                            )
                        ),
                        ingress_address=groundstation.CfnDataflowEndpointGroup.RangedConnectionDetailsProperty(
                            mtu=123,
                            socket_address=groundstation.CfnDataflowEndpointGroup.RangedSocketAddressProperty(
                                name="name",
                                port_range=groundstation.CfnDataflowEndpointGroup.IntegerRangeProperty(
                                    maximum=123,
                                    minimum=123
                                )
                            )
                        ),
                        name="name"
                    ),
                    endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                        address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                            name="name",
                            port=123
                        ),
                        mtu=123,
                        name="name"
                    ),
                    security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )],
            
                # the properties below are optional
                contact_post_pass_duration_seconds=123,
                contact_pre_pass_duration_seconds=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__063930c43a6ff97faaee9a4c322e7e786cb86ec9ca51ac8c6d171f9a49195f51)
            check_type(argname="argument endpoint_details", value=endpoint_details, expected_type=type_hints["endpoint_details"])
            check_type(argname="argument contact_post_pass_duration_seconds", value=contact_post_pass_duration_seconds, expected_type=type_hints["contact_post_pass_duration_seconds"])
            check_type(argname="argument contact_pre_pass_duration_seconds", value=contact_pre_pass_duration_seconds, expected_type=type_hints["contact_pre_pass_duration_seconds"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_details": endpoint_details,
        }
        if contact_post_pass_duration_seconds is not None:
            self._values["contact_post_pass_duration_seconds"] = contact_post_pass_duration_seconds
        if contact_pre_pass_duration_seconds is not None:
            self._values["contact_pre_pass_duration_seconds"] = contact_pre_pass_duration_seconds
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def endpoint_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataflowEndpointGroup.EndpointDetailsProperty]]]:
        '''List of Endpoint Details, containing address and port for each endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-endpointdetails
        '''
        result = self._values.get("endpoint_details")
        assert result is not None, "Required property 'endpoint_details' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataflowEndpointGroup.EndpointDetailsProperty]]], result)

    @builtins.property
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a ``POSTPASS`` state.

        A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the ``POSTPASS`` state.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-contactpostpassdurationseconds
        '''
        result = self._values.get("contact_post_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a ``PREPASS`` state.

        A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the ``PREPASS`` state.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-contactprepassdurationseconds
        '''
        result = self._values.get("contact_pre_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags assigned to a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataflowEndpointGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMissionProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_groundstation.CfnMissionProfile",
):
    '''Mission profiles specify parameters and provide references to config objects to define how Ground Station lists and executes contacts.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_groundstation as groundstation
        
        cfn_mission_profile = groundstation.CfnMissionProfile(self, "MyCfnMissionProfile",
            dataflow_edges=[groundstation.CfnMissionProfile.DataflowEdgeProperty(
                destination="destination",
                source="source"
            )],
            minimum_viable_contact_duration_seconds=123,
            name="name",
            tracking_config_arn="trackingConfigArn",
        
            # the properties below are optional
            contact_post_pass_duration_seconds=123,
            contact_pre_pass_duration_seconds=123,
            streams_kms_key=groundstation.CfnMissionProfile.StreamsKmsKeyProperty(
                kms_alias_arn="kmsAliasArn",
                kms_key_arn="kmsKeyArn"
            ),
            streams_kms_role="streamsKmsRole",
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
        dataflow_edges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMissionProfile.DataflowEdgeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        minimum_viable_contact_duration_seconds: jsii.Number,
        name: builtins.str,
        tracking_config_arn: builtins.str,
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        streams_kms_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMissionProfile.StreamsKmsKeyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        streams_kms_role: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dataflow_edges: A list containing lists of config ARNs. Each list of config ARNs is an edge, with a "from" config and a "to" config.
        :param minimum_viable_contact_duration_seconds: Minimum length of a contact in seconds that Ground Station will return when listing contacts. Ground Station will not return contacts shorter than this duration.
        :param name: The name of the mission profile.
        :param tracking_config_arn: The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.
        :param contact_post_pass_duration_seconds: Amount of time in seconds after a contact ends that you’d like to receive a CloudWatch Event indicating the pass has finished. For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_
        :param contact_pre_pass_duration_seconds: Amount of time in seconds prior to contact start that you'd like to receive a CloudWatch Event indicating an upcoming pass. For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_
        :param streams_kms_key: 
        :param streams_kms_role: The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.
        :param tags: Tags assigned to the mission profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8c20b1debe7b2cad3b5475e1d2b3d48fdf917b223b50d168e430ffa9502d0c4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMissionProfileProps(
            dataflow_edges=dataflow_edges,
            minimum_viable_contact_duration_seconds=minimum_viable_contact_duration_seconds,
            name=name,
            tracking_config_arn=tracking_config_arn,
            contact_post_pass_duration_seconds=contact_post_pass_duration_seconds,
            contact_pre_pass_duration_seconds=contact_pre_pass_duration_seconds,
            streams_kms_key=streams_kms_key,
            streams_kms_role=streams_kms_role,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef8971e1911aa9fe50dbe99fdbc8302ee8d00a40604a425305b2a2a8e4d8aa41)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c4f7cdc9483b5e2132ea81c776a7d9db90f8d6ba862c492fb197a9e040d59aa)
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
        '''The ARN of the mission profile, such as ``arn:aws:groundstation:us-east-2:1234567890:mission-profile/9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the mission profile, such as ``9940bf3b-d2ba-427e-9906-842b5e5d2296`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRegion")
    def attr_region(self) -> builtins.str:
        '''The region of the mission profile.

        :cloudformationAttribute: Region
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegion"))

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
    @jsii.member(jsii_name="dataflowEdges")
    def dataflow_edges(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMissionProfile.DataflowEdgeProperty"]]]:
        '''A list containing lists of config ARNs.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMissionProfile.DataflowEdgeProperty"]]], jsii.get(self, "dataflowEdges"))

    @dataflow_edges.setter
    def dataflow_edges(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMissionProfile.DataflowEdgeProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43bc20ed2a3d495db8c8b44a4e70f977393b7a6c9733040eeb7509592d7adda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataflowEdges", value)

    @builtins.property
    @jsii.member(jsii_name="minimumViableContactDurationSeconds")
    def minimum_viable_contact_duration_seconds(self) -> jsii.Number:
        '''Minimum length of a contact in seconds that Ground Station will return when listing contacts.'''
        return typing.cast(jsii.Number, jsii.get(self, "minimumViableContactDurationSeconds"))

    @minimum_viable_contact_duration_seconds.setter
    def minimum_viable_contact_duration_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03a884cd9e5b04447dbd311900e4a2d4bdc5e38d5b2b0e125c3aba5bcec92ff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumViableContactDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the mission profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da85a08a8a0b9b15f9e752862bd4dbbc57a69e050e2333199e52b7ac4fe113f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="trackingConfigArn")
    def tracking_config_arn(self) -> builtins.str:
        '''The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.'''
        return typing.cast(builtins.str, jsii.get(self, "trackingConfigArn"))

    @tracking_config_arn.setter
    def tracking_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28aebc57aca2f7c9aa21bd709cd68a9bffcc22e5b67419f3b600315cf8fd2903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackingConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="contactPostPassDurationSeconds")
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in seconds after a contact ends that you’d like to receive a CloudWatch Event indicating the pass has finished.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPostPassDurationSeconds"))

    @contact_post_pass_duration_seconds.setter
    def contact_post_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13ce886f0dccbdf43268a4de6f9502652f9fffeed67b564a8ba59a7f63fbc913)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPostPassDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="contactPrePassDurationSeconds")
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in seconds prior to contact start that you'd like to receive a CloudWatch Event indicating an upcoming pass.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPrePassDurationSeconds"))

    @contact_pre_pass_duration_seconds.setter
    def contact_pre_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d03eb5a896813d3d91f9b9192b83e7419b6393d8563a899e8cca36e8e4612f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPrePassDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="streamsKmsKey")
    def streams_kms_key(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMissionProfile.StreamsKmsKeyProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMissionProfile.StreamsKmsKeyProperty"]], jsii.get(self, "streamsKmsKey"))

    @streams_kms_key.setter
    def streams_kms_key(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMissionProfile.StreamsKmsKeyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__207e70bf5d230a887fe9bbaff20bf2acd3b70bbddcaee80fc84f715f95423e2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamsKmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="streamsKmsRole")
    def streams_kms_role(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamsKmsRole"))

    @streams_kms_role.setter
    def streams_kms_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd9fad80bfcf5d543fced97a8013a1b93e5d432d78e5d48475d6a2eb1a0eae70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamsKmsRole", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags assigned to the mission profile.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b63fbf7e02cfd3cabb495b47d8b525e2d0166b8195e578f79a444bec82c3b76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnMissionProfile.DataflowEdgeProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "source": "source"},
    )
    class DataflowEdgeProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A dataflow edge defines from where and to where data will flow during a contact.

            :param destination: The ARN of the destination for this dataflow edge. For example, specify the ARN of a dataflow endpoint config for a downlink edge or an antenna uplink config for an uplink edge.
            :param source: The ARN of the source for this dataflow edge. For example, specify the ARN of an antenna downlink config for a downlink edge or a dataflow endpoint config for an uplink edge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                dataflow_edge_property = groundstation.CfnMissionProfile.DataflowEdgeProperty(
                    destination="destination",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b247611cb700acbb2d198be2f48ab39f22bafbf3844a6363be6523b5edf8ed1c)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            '''The ARN of the destination for this dataflow edge.

            For example, specify the ARN of a dataflow endpoint config for a downlink edge or an antenna uplink config for an uplink edge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html#cfn-groundstation-missionprofile-dataflowedge-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''The ARN of the source for this dataflow edge.

            For example, specify the ARN of an antenna downlink config for a downlink edge or a dataflow endpoint config for an uplink edge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html#cfn-groundstation-missionprofile-dataflowedge-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEdgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnMissionProfile.StreamsKmsKeyProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_alias_arn": "kmsAliasArn", "kms_key_arn": "kmsKeyArn"},
    )
    class StreamsKmsKeyProperty:
        def __init__(
            self,
            *,
            kms_alias_arn: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param kms_alias_arn: 
            :param kms_key_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-streamskmskey.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                streams_kms_key_property = groundstation.CfnMissionProfile.StreamsKmsKeyProperty(
                    kms_alias_arn="kmsAliasArn",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b72d6af08de28c6ebdf730f46ed7f026b1f417a505f1cd3c52737731cc4f6d0)
                check_type(argname="argument kms_alias_arn", value=kms_alias_arn, expected_type=type_hints["kms_alias_arn"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_alias_arn is not None:
                self._values["kms_alias_arn"] = kms_alias_arn
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def kms_alias_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-streamskmskey.html#cfn-groundstation-missionprofile-streamskmskey-kmsaliasarn
            '''
            result = self._values.get("kms_alias_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-streamskmskey.html#cfn-groundstation-missionprofile-streamskmskey-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamsKmsKeyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_groundstation.CfnMissionProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataflow_edges": "dataflowEdges",
        "minimum_viable_contact_duration_seconds": "minimumViableContactDurationSeconds",
        "name": "name",
        "tracking_config_arn": "trackingConfigArn",
        "contact_post_pass_duration_seconds": "contactPostPassDurationSeconds",
        "contact_pre_pass_duration_seconds": "contactPrePassDurationSeconds",
        "streams_kms_key": "streamsKmsKey",
        "streams_kms_role": "streamsKmsRole",
        "tags": "tags",
    },
)
class CfnMissionProfileProps:
    def __init__(
        self,
        *,
        dataflow_edges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMissionProfile.DataflowEdgeProperty, typing.Dict[builtins.str, typing.Any]]]]],
        minimum_viable_contact_duration_seconds: jsii.Number,
        name: builtins.str,
        tracking_config_arn: builtins.str,
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        streams_kms_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMissionProfile.StreamsKmsKeyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        streams_kms_role: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMissionProfile``.

        :param dataflow_edges: A list containing lists of config ARNs. Each list of config ARNs is an edge, with a "from" config and a "to" config.
        :param minimum_viable_contact_duration_seconds: Minimum length of a contact in seconds that Ground Station will return when listing contacts. Ground Station will not return contacts shorter than this duration.
        :param name: The name of the mission profile.
        :param tracking_config_arn: The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.
        :param contact_post_pass_duration_seconds: Amount of time in seconds after a contact ends that you’d like to receive a CloudWatch Event indicating the pass has finished. For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_
        :param contact_pre_pass_duration_seconds: Amount of time in seconds prior to contact start that you'd like to receive a CloudWatch Event indicating an upcoming pass. For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_
        :param streams_kms_key: 
        :param streams_kms_role: The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.
        :param tags: Tags assigned to the mission profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_groundstation as groundstation
            
            cfn_mission_profile_props = groundstation.CfnMissionProfileProps(
                dataflow_edges=[groundstation.CfnMissionProfile.DataflowEdgeProperty(
                    destination="destination",
                    source="source"
                )],
                minimum_viable_contact_duration_seconds=123,
                name="name",
                tracking_config_arn="trackingConfigArn",
            
                # the properties below are optional
                contact_post_pass_duration_seconds=123,
                contact_pre_pass_duration_seconds=123,
                streams_kms_key=groundstation.CfnMissionProfile.StreamsKmsKeyProperty(
                    kms_alias_arn="kmsAliasArn",
                    kms_key_arn="kmsKeyArn"
                ),
                streams_kms_role="streamsKmsRole",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb791267f06ed92ca1c83c1b6ade129961c1c9de1a7d2ef1d57b3df27b191ab0)
            check_type(argname="argument dataflow_edges", value=dataflow_edges, expected_type=type_hints["dataflow_edges"])
            check_type(argname="argument minimum_viable_contact_duration_seconds", value=minimum_viable_contact_duration_seconds, expected_type=type_hints["minimum_viable_contact_duration_seconds"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tracking_config_arn", value=tracking_config_arn, expected_type=type_hints["tracking_config_arn"])
            check_type(argname="argument contact_post_pass_duration_seconds", value=contact_post_pass_duration_seconds, expected_type=type_hints["contact_post_pass_duration_seconds"])
            check_type(argname="argument contact_pre_pass_duration_seconds", value=contact_pre_pass_duration_seconds, expected_type=type_hints["contact_pre_pass_duration_seconds"])
            check_type(argname="argument streams_kms_key", value=streams_kms_key, expected_type=type_hints["streams_kms_key"])
            check_type(argname="argument streams_kms_role", value=streams_kms_role, expected_type=type_hints["streams_kms_role"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataflow_edges": dataflow_edges,
            "minimum_viable_contact_duration_seconds": minimum_viable_contact_duration_seconds,
            "name": name,
            "tracking_config_arn": tracking_config_arn,
        }
        if contact_post_pass_duration_seconds is not None:
            self._values["contact_post_pass_duration_seconds"] = contact_post_pass_duration_seconds
        if contact_pre_pass_duration_seconds is not None:
            self._values["contact_pre_pass_duration_seconds"] = contact_pre_pass_duration_seconds
        if streams_kms_key is not None:
            self._values["streams_kms_key"] = streams_kms_key
        if streams_kms_role is not None:
            self._values["streams_kms_role"] = streams_kms_role
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dataflow_edges(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMissionProfile.DataflowEdgeProperty]]]:
        '''A list containing lists of config ARNs.

        Each list of config ARNs is an edge, with a "from" config and a "to" config.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-dataflowedges
        '''
        result = self._values.get("dataflow_edges")
        assert result is not None, "Required property 'dataflow_edges' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMissionProfile.DataflowEdgeProperty]]], result)

    @builtins.property
    def minimum_viable_contact_duration_seconds(self) -> jsii.Number:
        '''Minimum length of a contact in seconds that Ground Station will return when listing contacts.

        Ground Station will not return contacts shorter than this duration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-minimumviablecontactdurationseconds
        '''
        result = self._values.get("minimum_viable_contact_duration_seconds")
        assert result is not None, "Required property 'minimum_viable_contact_duration_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the mission profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tracking_config_arn(self) -> builtins.str:
        '''The ARN of a tracking config objects that defines how to track the satellite through the sky during a contact.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-trackingconfigarn
        '''
        result = self._values.get("tracking_config_arn")
        assert result is not None, "Required property 'tracking_config_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in seconds after a contact ends that you’d like to receive a CloudWatch Event indicating the pass has finished.

        For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactpostpassdurationseconds
        '''
        result = self._values.get("contact_post_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Amount of time in seconds prior to contact start that you'd like to receive a CloudWatch Event indicating an upcoming pass.

        For more information on CloudWatch Events, see the `What Is CloudWatch Events? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactprepassdurationseconds
        '''
        result = self._values.get("contact_pre_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def streams_kms_key(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMissionProfile.StreamsKmsKeyProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-streamskmskey
        '''
        result = self._values.get("streams_kms_key")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMissionProfile.StreamsKmsKeyProperty]], result)

    @builtins.property
    def streams_kms_role(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-streamskmsrole
        '''
        result = self._values.get("streams_kms_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags assigned to the mission profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMissionProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfig",
    "CfnConfigProps",
    "CfnDataflowEndpointGroup",
    "CfnDataflowEndpointGroupProps",
    "CfnMissionProfile",
    "CfnMissionProfileProps",
]

publication.publish()

def _typecheckingstub__13b5342b1ca67f4a4ccbf4e2d71441ec8ac6775411c783b3c9c933f4caeaeb44(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    config_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.ConfigDataProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3cdfd5eb2baaf5f01fe9f7913185faf70d134acf441b89c112df84fd2f1db8a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd40941f885360d05e2643d3d6f98380b40caebf76d694523c46c112050eb127(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1563feeaa37deb3f7ed7d57717d9cfb0c9d0d00d4203ece4f573e5ceaf951329(
    value: typing.Union[_IResolvable_da3f097b, CfnConfig.ConfigDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e45ad42a1b16a7ac4346df0c4eb4ef210effbe14d6f3a655aeb196609bb41609(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5239786ac786ccdad1f55bd40cbcac2fd2c846b2a7de2861dbb7b912f8c930a0(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95c9bb891616bdcd84a4fa4a4632dbc784f0eb088325a7f017b16d8b07182f9f(
    *,
    spectrum_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.SpectrumConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe67adf126f560718d80fe7b470120098ad348e65acc48056db851ebe85ca63(
    *,
    decode_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.DecodeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    demodulation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.DemodulationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    spectrum_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.SpectrumConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55cd1298db9810d3b2cd585a075bd274d81baff7309375a8f1f1bcd888166878(
    *,
    spectrum_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.UplinkSpectrumConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_eirp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.EirpProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    transmit_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c161ef31a785b644c7c9cc8f223e10dcb0af1ba0e4a29303d7c17d85b3cbe192(
    *,
    antenna_downlink_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.AntennaDownlinkConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    antenna_downlink_demod_decode_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.AntennaDownlinkDemodDecodeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    antenna_uplink_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.AntennaUplinkConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dataflow_endpoint_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.DataflowEndpointConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.S3RecordingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.TrackingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    uplink_echo_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.UplinkEchoConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99a763bb26b6623e715887bdc54f3c7ceed9bfb9f5a794e1721c1518d6679eae(
    *,
    dataflow_endpoint_name: typing.Optional[builtins.str] = None,
    dataflow_endpoint_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324f5ec78c0ce70a0c2b16edd19232cbe81a59b2c1577339462358e74d607c12(
    *,
    unvalidated_json: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41995b227ea3e4e9f0b14b63def99efc04e280b4295dd4e9584328affb2eb70e(
    *,
    unvalidated_json: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c514bdd7e81420fa1de45f624e9738b0420c9e0adc054d3749c647a5f1a0b336(
    *,
    units: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6607539aa17b23364cc0c5de62d53ab10b2588b4a397b71ff9a1510aefbc8763(
    *,
    units: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54cacafc58427db742615b0fe5104ac687a9a80afc40f92de682c2897f73b0f5(
    *,
    units: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a434f8f9b58e6e79e140ec69b10fe3b638c9dd796407130b206d6328c3b092d3(
    *,
    bucket_arn: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdff7bad914262ea88134e28b4653bf1192cb3dab1012e32f318a75dba095e8a(
    *,
    bandwidth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.FrequencyBandwidthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    center_frequency: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.FrequencyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    polarization: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed1a7eb46212500aac5b18d6aa5e4a9a69548192e39da2f23d9e5d6301bcd6ac(
    *,
    autotrack: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__193d0e509b29608b5001e27835cf0767adff51dea5067bffff37a3d9d26ae405(
    *,
    antenna_uplink_config_arn: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27edccf82a0971febe19a69f59300574fa0a8a86e8860e33b5b5b5fac0eafdbc(
    *,
    center_frequency: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.FrequencyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    polarization: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed41d945f02014619043ab4e725d6fc3de8df5c042bab0ce35128c1603f4ea25(
    *,
    config_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfig.ConfigDataProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__669b82a6c91e9541f061b9397341fc4b6628a648faf22449b040ab31e2879b6f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    endpoint_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]]]]],
    contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d9bea099cdcd1099da7284180003b79769ad1588e3964f28fb913d498709f5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__301a06069694a715f2320416d1088ceb197833a8e20246ccb97b1aa5fb5dbb31(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__605270fdb212e4afd622fd5047d2f46f173b44dc28a4370f48d78fa181366952(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataflowEndpointGroup.EndpointDetailsProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25ef1c7229baacb918baea79312842d531006cf929111fa27c27bd2a0f2730f8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d824833236777cd2417ffad0f69012adcf6aab076829d4fc012bb6bf35c092f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91f97011b987224f8e61448ddca1df20f67e7b2188ee8ce55208bdeb4bbc53a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee0748f1ecb5781e9a01db9f02fc9c03f466d2eb8031790fd920a9b59c3a7efe(
    *,
    agent_status: typing.Optional[builtins.str] = None,
    audit_results: typing.Optional[builtins.str] = None,
    egress_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.ConnectionDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.RangedConnectionDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac92ba18922e7f50fbd2fb44b481647516ad2ecad36a6ecdb41418e911572b8c(
    *,
    mtu: typing.Optional[jsii.Number] = None,
    socket_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.SocketAddressProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9f5226d94e906b56ccb5e58d75ed0e8d68881429608741bde8890f51ab8be0(
    *,
    address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.SocketAddressProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mtu: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce6c1b639a398c895dfc66055f50eec9eabd79db1d993d794e1fd73150b96712(
    *,
    aws_ground_station_agent_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.AwsGroundStationAgentEndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.DataflowEndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.SecurityDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49c491018c49abebdb9e07f6263ac4ee58dd70f1dde65fa0408a3d33522a05a(
    *,
    maximum: typing.Optional[jsii.Number] = None,
    minimum: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4718a299592e9341c9edaea65909a5d521ddfd0baf97317c55e21c1a1cde5b4(
    *,
    mtu: typing.Optional[jsii.Number] = None,
    socket_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.RangedSocketAddressProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0279ec5e3dff22baf12b2c0289e5035186ce86688371a640b24790d608a5b33(
    *,
    name: typing.Optional[builtins.str] = None,
    port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.IntegerRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220180d1b2cf36fe04713aaee0c3fe3a558c4c874399dd27305560fd323a8137(
    *,
    role_arn: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be1cdd898189d7b0a27924e382d426d33c11750a250da2b52f6b3ef9e323767(
    *,
    name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__063930c43a6ff97faaee9a4c322e7e786cb86ec9ca51ac8c6d171f9a49195f51(
    *,
    endpoint_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]]]]],
    contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8c20b1debe7b2cad3b5475e1d2b3d48fdf917b223b50d168e430ffa9502d0c4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dataflow_edges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMissionProfile.DataflowEdgeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    minimum_viable_contact_duration_seconds: jsii.Number,
    name: builtins.str,
    tracking_config_arn: builtins.str,
    contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    streams_kms_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMissionProfile.StreamsKmsKeyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    streams_kms_role: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef8971e1911aa9fe50dbe99fdbc8302ee8d00a40604a425305b2a2a8e4d8aa41(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c4f7cdc9483b5e2132ea81c776a7d9db90f8d6ba862c492fb197a9e040d59aa(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43bc20ed2a3d495db8c8b44a4e70f977393b7a6c9733040eeb7509592d7adda(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMissionProfile.DataflowEdgeProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a884cd9e5b04447dbd311900e4a2d4bdc5e38d5b2b0e125c3aba5bcec92ff5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da85a08a8a0b9b15f9e752862bd4dbbc57a69e050e2333199e52b7ac4fe113f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28aebc57aca2f7c9aa21bd709cd68a9bffcc22e5b67419f3b600315cf8fd2903(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ce886f0dccbdf43268a4de6f9502652f9fffeed67b564a8ba59a7f63fbc913(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d03eb5a896813d3d91f9b9192b83e7419b6393d8563a899e8cca36e8e4612f5(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__207e70bf5d230a887fe9bbaff20bf2acd3b70bbddcaee80fc84f715f95423e2f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMissionProfile.StreamsKmsKeyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd9fad80bfcf5d543fced97a8013a1b93e5d432d78e5d48475d6a2eb1a0eae70(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b63fbf7e02cfd3cabb495b47d8b525e2d0166b8195e578f79a444bec82c3b76(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b247611cb700acbb2d198be2f48ab39f22bafbf3844a6363be6523b5edf8ed1c(
    *,
    destination: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b72d6af08de28c6ebdf730f46ed7f026b1f417a505f1cd3c52737731cc4f6d0(
    *,
    kms_alias_arn: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb791267f06ed92ca1c83c1b6ade129961c1c9de1a7d2ef1d57b3df27b191ab0(
    *,
    dataflow_edges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMissionProfile.DataflowEdgeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    minimum_viable_contact_duration_seconds: jsii.Number,
    name: builtins.str,
    tracking_config_arn: builtins.str,
    contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
    streams_kms_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMissionProfile.StreamsKmsKeyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    streams_kms_role: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
