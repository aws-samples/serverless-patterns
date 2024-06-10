'''
# Amazon EMR Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_emr as emr
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EMR construct libraries](https://constructs.dev/search?q=emr)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EMR resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMR.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EMR](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMR.html).

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
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emr.CfnCluster",
):
    '''The ``AWS::EMR::Cluster`` resource specifies an Amazon EMR cluster.

    This cluster is a collection of Amazon EC2 instances that run open source big data frameworks and applications to process and analyze vast amounts of data. For more information, see the `Amazon EMR Management Guide <https://docs.aws.amazon.com//emr/latest/ManagementGuide/>`_ .

    Amazon EMR now supports launching task instance groups and task instance fleets as part of the ``AWS::EMR::Cluster`` resource. This can be done by using the ``JobFlowInstancesConfig`` property type's ``TaskInstanceGroups`` and ``TaskInstanceFleets`` subproperties. Using these subproperties reduces delays in provisioning task nodes compared to specifying task nodes with the ``AWS::EMR::InstanceGroupConfig`` and ``AWS::EMR::InstanceFleetConfig`` resources. Please refer to the examples at the bottom of this page to learn how to use these subproperties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html
    :cloudformationResource: AWS::EMR::Cluster
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emr as emr
        
        # additional_info: Any
        # configuration_property_: emr.CfnCluster.ConfigurationProperty
        
        cfn_cluster = emr.CfnCluster(self, "MyCfnCluster",
            instances=emr.CfnCluster.JobFlowInstancesConfigProperty(
                additional_master_security_groups=["additionalMasterSecurityGroups"],
                additional_slave_security_groups=["additionalSlaveSecurityGroups"],
                core_instance_fleet=emr.CfnCluster.InstanceFleetConfigProperty(
                    instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                        instance_type="instanceType",
        
                        # the properties below are optional
                        bid_price="bidPrice",
                        bid_price_as_percentage_of_on_demand_price=123,
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
        
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
        
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        weighted_capacity=123
                    )],
                    launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                        on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                            allocation_strategy="allocationStrategy"
                        ),
                        spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                            timeout_action="timeoutAction",
                            timeout_duration_minutes=123,
        
                            # the properties below are optional
                            allocation_strategy="allocationStrategy",
                            block_duration_minutes=123
                        )
                    ),
                    name="name",
                    target_on_demand_capacity=123,
                    target_spot_capacity=123
                ),
                core_instance_group=emr.CfnCluster.InstanceGroupConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
        
                    # the properties below are optional
                    auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                        constraints=emr.CfnCluster.ScalingConstraintsProperty(
                            max_capacity=123,
                            min_capacity=123
                        ),
                        rules=[emr.CfnCluster.ScalingRuleProperty(
                            action=emr.CfnCluster.ScalingActionProperty(
                                simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                    scaling_adjustment=123,
        
                                    # the properties below are optional
                                    adjustment_type="adjustmentType",
                                    cool_down=123
                                ),
        
                                # the properties below are optional
                                market="market"
                            ),
                            name="name",
                            trigger=emr.CfnCluster.ScalingTriggerProperty(
                                cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                    comparison_operator="comparisonOperator",
                                    metric_name="metricName",
                                    period=123,
                                    threshold=123,
        
                                    # the properties below are optional
                                    dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                        key="key",
                                        value="value"
                                    )],
                                    evaluation_periods=123,
                                    namespace="namespace",
                                    statistic="statistic",
                                    unit="unit"
                                )
                            ),
        
                            # the properties below are optional
                            description="description"
                        )]
                    ),
                    bid_price="bidPrice",
                    configurations=[emr.CfnCluster.ConfigurationProperty(
                        classification="classification",
                        configuration_properties={
                            "configuration_properties_key": "configurationProperties"
                        },
                        configurations=[configuration_property_]
                    )],
                    custom_ami_id="customAmiId",
                    ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                        ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                            volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                size_in_gb=123,
                                volume_type="volumeType",
        
                                # the properties below are optional
                                iops=123,
                                throughput=123
                            ),
        
                            # the properties below are optional
                            volumes_per_instance=123
                        )],
                        ebs_optimized=False
                    ),
                    market="market",
                    name="name"
                ),
                ec2_key_name="ec2KeyName",
                ec2_subnet_id="ec2SubnetId",
                ec2_subnet_ids=["ec2SubnetIds"],
                emr_managed_master_security_group="emrManagedMasterSecurityGroup",
                emr_managed_slave_security_group="emrManagedSlaveSecurityGroup",
                hadoop_version="hadoopVersion",
                keep_job_flow_alive_when_no_steps=False,
                master_instance_fleet=emr.CfnCluster.InstanceFleetConfigProperty(
                    instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                        instance_type="instanceType",
        
                        # the properties below are optional
                        bid_price="bidPrice",
                        bid_price_as_percentage_of_on_demand_price=123,
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
        
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
        
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        weighted_capacity=123
                    )],
                    launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                        on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                            allocation_strategy="allocationStrategy"
                        ),
                        spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                            timeout_action="timeoutAction",
                            timeout_duration_minutes=123,
        
                            # the properties below are optional
                            allocation_strategy="allocationStrategy",
                            block_duration_minutes=123
                        )
                    ),
                    name="name",
                    target_on_demand_capacity=123,
                    target_spot_capacity=123
                ),
                master_instance_group=emr.CfnCluster.InstanceGroupConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
        
                    # the properties below are optional
                    auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                        constraints=emr.CfnCluster.ScalingConstraintsProperty(
                            max_capacity=123,
                            min_capacity=123
                        ),
                        rules=[emr.CfnCluster.ScalingRuleProperty(
                            action=emr.CfnCluster.ScalingActionProperty(
                                simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                    scaling_adjustment=123,
        
                                    # the properties below are optional
                                    adjustment_type="adjustmentType",
                                    cool_down=123
                                ),
        
                                # the properties below are optional
                                market="market"
                            ),
                            name="name",
                            trigger=emr.CfnCluster.ScalingTriggerProperty(
                                cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                    comparison_operator="comparisonOperator",
                                    metric_name="metricName",
                                    period=123,
                                    threshold=123,
        
                                    # the properties below are optional
                                    dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                        key="key",
                                        value="value"
                                    )],
                                    evaluation_periods=123,
                                    namespace="namespace",
                                    statistic="statistic",
                                    unit="unit"
                                )
                            ),
        
                            # the properties below are optional
                            description="description"
                        )]
                    ),
                    bid_price="bidPrice",
                    configurations=[emr.CfnCluster.ConfigurationProperty(
                        classification="classification",
                        configuration_properties={
                            "configuration_properties_key": "configurationProperties"
                        },
                        configurations=[configuration_property_]
                    )],
                    custom_ami_id="customAmiId",
                    ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                        ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                            volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                size_in_gb=123,
                                volume_type="volumeType",
        
                                # the properties below are optional
                                iops=123,
                                throughput=123
                            ),
        
                            # the properties below are optional
                            volumes_per_instance=123
                        )],
                        ebs_optimized=False
                    ),
                    market="market",
                    name="name"
                ),
                placement=emr.CfnCluster.PlacementTypeProperty(
                    availability_zone="availabilityZone"
                ),
                service_access_security_group="serviceAccessSecurityGroup",
                task_instance_fleets=[emr.CfnCluster.InstanceFleetConfigProperty(
                    instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                        instance_type="instanceType",
        
                        # the properties below are optional
                        bid_price="bidPrice",
                        bid_price_as_percentage_of_on_demand_price=123,
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
        
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
        
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        weighted_capacity=123
                    )],
                    launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                        on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                            allocation_strategy="allocationStrategy"
                        ),
                        spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                            timeout_action="timeoutAction",
                            timeout_duration_minutes=123,
        
                            # the properties below are optional
                            allocation_strategy="allocationStrategy",
                            block_duration_minutes=123
                        )
                    ),
                    name="name",
                    target_on_demand_capacity=123,
                    target_spot_capacity=123
                )],
                task_instance_groups=[emr.CfnCluster.InstanceGroupConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
        
                    # the properties below are optional
                    auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                        constraints=emr.CfnCluster.ScalingConstraintsProperty(
                            max_capacity=123,
                            min_capacity=123
                        ),
                        rules=[emr.CfnCluster.ScalingRuleProperty(
                            action=emr.CfnCluster.ScalingActionProperty(
                                simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                    scaling_adjustment=123,
        
                                    # the properties below are optional
                                    adjustment_type="adjustmentType",
                                    cool_down=123
                                ),
        
                                # the properties below are optional
                                market="market"
                            ),
                            name="name",
                            trigger=emr.CfnCluster.ScalingTriggerProperty(
                                cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                    comparison_operator="comparisonOperator",
                                    metric_name="metricName",
                                    period=123,
                                    threshold=123,
        
                                    # the properties below are optional
                                    dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                        key="key",
                                        value="value"
                                    )],
                                    evaluation_periods=123,
                                    namespace="namespace",
                                    statistic="statistic",
                                    unit="unit"
                                )
                            ),
        
                            # the properties below are optional
                            description="description"
                        )]
                    ),
                    bid_price="bidPrice",
                    configurations=[emr.CfnCluster.ConfigurationProperty(
                        classification="classification",
                        configuration_properties={
                            "configuration_properties_key": "configurationProperties"
                        },
                        configurations=[configuration_property_]
                    )],
                    custom_ami_id="customAmiId",
                    ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                        ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                            volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                size_in_gb=123,
                                volume_type="volumeType",
        
                                # the properties below are optional
                                iops=123,
                                throughput=123
                            ),
        
                            # the properties below are optional
                            volumes_per_instance=123
                        )],
                        ebs_optimized=False
                    ),
                    market="market",
                    name="name"
                )],
                termination_protected=False,
                unhealthy_node_replacement=False
            ),
            job_flow_role="jobFlowRole",
            name="name",
            service_role="serviceRole",
        
            # the properties below are optional
            additional_info=additional_info,
            applications=[emr.CfnCluster.ApplicationProperty(
                additional_info={
                    "additional_info_key": "additionalInfo"
                },
                args=["args"],
                name="name",
                version="version"
            )],
            auto_scaling_role="autoScalingRole",
            auto_termination_policy=emr.CfnCluster.AutoTerminationPolicyProperty(
                idle_timeout=123
            ),
            bootstrap_actions=[emr.CfnCluster.BootstrapActionConfigProperty(
                name="name",
                script_bootstrap_action=emr.CfnCluster.ScriptBootstrapActionConfigProperty(
                    path="path",
        
                    # the properties below are optional
                    args=["args"]
                )
            )],
            configurations=[emr.CfnCluster.ConfigurationProperty(
                classification="classification",
                configuration_properties={
                    "configuration_properties_key": "configurationProperties"
                },
                configurations=[configuration_property_]
            )],
            custom_ami_id="customAmiId",
            ebs_root_volume_iops=123,
            ebs_root_volume_size=123,
            ebs_root_volume_throughput=123,
            kerberos_attributes=emr.CfnCluster.KerberosAttributesProperty(
                kdc_admin_password="kdcAdminPassword",
                realm="realm",
        
                # the properties below are optional
                ad_domain_join_password="adDomainJoinPassword",
                ad_domain_join_user="adDomainJoinUser",
                cross_realm_trust_principal_password="crossRealmTrustPrincipalPassword"
            ),
            log_encryption_kms_key_id="logEncryptionKmsKeyId",
            log_uri="logUri",
            managed_scaling_policy=emr.CfnCluster.ManagedScalingPolicyProperty(
                compute_limits=emr.CfnCluster.ComputeLimitsProperty(
                    maximum_capacity_units=123,
                    minimum_capacity_units=123,
                    unit_type="unitType",
        
                    # the properties below are optional
                    maximum_core_capacity_units=123,
                    maximum_on_demand_capacity_units=123
                )
            ),
            os_release_label="osReleaseLabel",
            placement_group_configs=[emr.CfnCluster.PlacementGroupConfigProperty(
                instance_role="instanceRole",
        
                # the properties below are optional
                placement_strategy="placementStrategy"
            )],
            release_label="releaseLabel",
            scale_down_behavior="scaleDownBehavior",
            security_configuration="securityConfiguration",
            step_concurrency_level=123,
            steps=[emr.CfnCluster.StepConfigProperty(
                hadoop_jar_step=emr.CfnCluster.HadoopJarStepConfigProperty(
                    jar="jar",
        
                    # the properties below are optional
                    args=["args"],
                    main_class="mainClass",
                    step_properties=[emr.CfnCluster.KeyValueProperty(
                        key="key",
                        value="value"
                    )]
                ),
                name="name",
        
                # the properties below are optional
                action_on_failure="actionOnFailure"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            visible_to_all_users=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instances: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.JobFlowInstancesConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        job_flow_role: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        additional_info: typing.Any = None,
        applications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ApplicationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        auto_scaling_role: typing.Optional[builtins.str] = None,
        auto_termination_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.AutoTerminationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        bootstrap_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.BootstrapActionConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_root_volume_iops: typing.Optional[jsii.Number] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        ebs_root_volume_throughput: typing.Optional[jsii.Number] = None,
        kerberos_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.KerberosAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        managed_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ManagedScalingPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        os_release_label: typing.Optional[builtins.str] = None,
        placement_group_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.PlacementGroupConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        release_label: typing.Optional[builtins.str] = None,
        scale_down_behavior: typing.Optional[builtins.str] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        step_concurrency_level: typing.Optional[jsii.Number] = None,
        steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.StepConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instances: A specification of the number and type of Amazon EC2 instances.
        :param job_flow_role: Also called instance profile and Amazon EC2 role. An IAM role for an Amazon EMR cluster. The Amazon EC2 instances of the cluster assume this role. The default role is ``EMR_EC2_DefaultRole`` . In order to use the default role, you must have already created it using the AWS CLI or console.
        :param name: The name of the cluster. This parameter can't contain the characters <, >, $, |, or ` (backtick).
        :param service_role: The IAM role that Amazon EMR assumes in order to access AWS resources on your behalf.
        :param additional_info: A JSON string for selecting additional features.
        :param applications: The applications to install on this cluster, for example, Spark, Flink, Oozie, Zeppelin, and so on.
        :param auto_scaling_role: An IAM role for automatic scaling policies. The default role is ``EMR_AutoScaling_DefaultRole`` . The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.
        :param auto_termination_policy: An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see `Control cluster termination <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html>`_
        :param bootstrap_actions: A list of bootstrap actions to run before Hadoop starts on the cluster nodes.
        :param configurations: Applies only to Amazon EMR releases 4.x and later. The list of configurations that are supplied to the Amazon EMR cluster.
        :param custom_ami_id: Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.
        :param ebs_root_volume_iops: The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.
        :param ebs_root_volume_size: The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.
        :param ebs_root_volume_throughput: The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.
        :param kerberos_attributes: Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see `Use Kerberos Authentication <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`_ in the *Amazon EMR Management Guide* .
        :param log_encryption_kms_key_id: The AWS KMS key used for encrypting log files. This attribute is only available with Amazon EMR 5.30.0 and later, excluding Amazon EMR 6.0.0.
        :param log_uri: The path to the Amazon S3 location where logs for this cluster are stored.
        :param managed_scaling_policy: Creates or updates a managed scaling policy for an Amazon EMR cluster. The managed scaling policy defines the limits for resources, such as Amazon EC2 instances that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
        :param os_release_label: The Amazon Linux release specified in a cluster launch RunJobFlow request. If no Amazon Linux release was specified, the default Amazon Linux release is shown in the response.
        :param placement_group_configs: 
        :param release_label: The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form ``emr-x.x.x`` , where x.x.x is an Amazon EMR release version such as ``emr-5.14.0`` . For more information about Amazon EMR release versions and included application versions and features, see ` <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/>`_ . The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use ``AmiVersion`` .
        :param scale_down_behavior: The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. ``TERMINATE_AT_INSTANCE_HOUR`` indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. ``TERMINATE_AT_TASK_COMPLETION`` indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. ``TERMINATE_AT_TASK_COMPLETION`` is available only in Amazon EMR releases 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.
        :param security_configuration: The name of the security configuration applied to the cluster.
        :param step_concurrency_level: Specifies the number of steps that can be executed concurrently. The default value is ``1`` . The maximum value is ``256`` .
        :param steps: A list of steps to run.
        :param tags: A list of tags associated with a cluster.
        :param visible_to_all_users: Indicates whether the cluster is visible to all IAM users of the AWS account associated with the cluster. If this value is set to ``true`` , all IAM users of that AWS account can view and manage the cluster if they have the proper policy permissions set. If this value is ``false`` , only the IAM user that created the cluster can view and manage it. This value can be changed using the SetVisibleToAllUsers action. .. epigraph:: When you create clusters directly through the EMR console or API, this value is set to ``true`` by default. However, for ``AWS::EMR::Cluster`` resources in CloudFormation, the default is ``false`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__078ec582504b982aedaecb6e8181c3cf53ae51c1b43cd59a31f8379e104620a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            instances=instances,
            job_flow_role=job_flow_role,
            name=name,
            service_role=service_role,
            additional_info=additional_info,
            applications=applications,
            auto_scaling_role=auto_scaling_role,
            auto_termination_policy=auto_termination_policy,
            bootstrap_actions=bootstrap_actions,
            configurations=configurations,
            custom_ami_id=custom_ami_id,
            ebs_root_volume_iops=ebs_root_volume_iops,
            ebs_root_volume_size=ebs_root_volume_size,
            ebs_root_volume_throughput=ebs_root_volume_throughput,
            kerberos_attributes=kerberos_attributes,
            log_encryption_kms_key_id=log_encryption_kms_key_id,
            log_uri=log_uri,
            managed_scaling_policy=managed_scaling_policy,
            os_release_label=os_release_label,
            placement_group_configs=placement_group_configs,
            release_label=release_label,
            scale_down_behavior=scale_down_behavior,
            security_configuration=security_configuration,
            step_concurrency_level=step_concurrency_level,
            steps=steps,
            tags=tags,
            visible_to_all_users=visible_to_all_users,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bbe2decc930b4772f0407223e119030f3892221da6840065798499363723d31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee2b9fd8d133889786966e4e13fa9f42593ed4a152172b2a5f46f008717ed56a)
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
        '''The unique identifier for the cluster.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrMasterPublicDns")
    def attr_master_public_dns(self) -> builtins.str:
        '''The public DNS name of the master node (instance), such as ``ec2-12-123-123-123.us-west-2.compute.amazonaws.com`` .

        :cloudformationAttribute: MasterPublicDNS
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMasterPublicDns"))

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
    @jsii.member(jsii_name="instances")
    def instances(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.JobFlowInstancesConfigProperty"]:
        '''A specification of the number and type of Amazon EC2 instances.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.JobFlowInstancesConfigProperty"], jsii.get(self, "instances"))

    @instances.setter
    def instances(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCluster.JobFlowInstancesConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db10eb80ac95a4595d858fdb0ef7856bf908495b5881a437e2418e12ef04e2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="jobFlowRole")
    def job_flow_role(self) -> builtins.str:
        '''Also called instance profile and Amazon EC2 role.'''
        return typing.cast(builtins.str, jsii.get(self, "jobFlowRole"))

    @job_flow_role.setter
    def job_flow_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97d15d32b487b49d5a8c2e21737709401b2e456ae4a474e281d2be42453fe4e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobFlowRole", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f422fb80835fbbe27ca5ef52cdf0b51d324e042c174b5bbf7f5b6c241f060238)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        '''The IAM role that Amazon EMR assumes in order to access AWS resources on your behalf.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d66a155fe1abdff7c63e4e37d410af54a782aafe35f5b0624479ed23d224711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="additionalInfo")
    def additional_info(self) -> typing.Any:
        '''A JSON string for selecting additional features.'''
        return typing.cast(typing.Any, jsii.get(self, "additionalInfo"))

    @additional_info.setter
    def additional_info(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__348f0a3a57b5e0506d5065002305d702fe48d937d3cf7901229ca7dd35b22175)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalInfo", value)

    @builtins.property
    @jsii.member(jsii_name="applications")
    def applications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ApplicationProperty"]]]]:
        '''The applications to install on this cluster, for example, Spark, Flink, Oozie, Zeppelin, and so on.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ApplicationProperty"]]]], jsii.get(self, "applications"))

    @applications.setter
    def applications(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ApplicationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e5be2002d09889a797c9582ab789359945687c870580656dbe722e89affc8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applications", value)

    @builtins.property
    @jsii.member(jsii_name="autoScalingRole")
    def auto_scaling_role(self) -> typing.Optional[builtins.str]:
        '''An IAM role for automatic scaling policies.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingRole"))

    @auto_scaling_role.setter
    def auto_scaling_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__220e0794f7e50696a7bce5f1cf4265710a3841db26e170a75b462acb7db4953a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingRole", value)

    @builtins.property
    @jsii.member(jsii_name="autoTerminationPolicy")
    def auto_termination_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AutoTerminationPolicyProperty"]]:
        '''An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AutoTerminationPolicyProperty"]], jsii.get(self, "autoTerminationPolicy"))

    @auto_termination_policy.setter
    def auto_termination_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AutoTerminationPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9e8b03bd44a0739c6fca421ce3e85b26ae46c02940e43a578dfece166b4cbb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoTerminationPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="bootstrapActions")
    def bootstrap_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.BootstrapActionConfigProperty"]]]]:
        '''A list of bootstrap actions to run before Hadoop starts on the cluster nodes.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.BootstrapActionConfigProperty"]]]], jsii.get(self, "bootstrapActions"))

    @bootstrap_actions.setter
    def bootstrap_actions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.BootstrapActionConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a761eb62509f84f3cbdff36a01487f8fb05f47b8241a831edf6b50a7bbaff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootstrapActions", value)

    @builtins.property
    @jsii.member(jsii_name="configurations")
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]]:
        '''Applies only to Amazon EMR releases 4.x and later. The list of configurations that are supplied to the Amazon EMR cluster.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]], jsii.get(self, "configurations"))

    @configurations.setter
    def configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4961b9c02eb65b76747f3388b3687aa1f18bf2da62820618bea64915a04b6954)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurations", value)

    @builtins.property
    @jsii.member(jsii_name="customAmiId")
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAmiId"))

    @custom_ami_id.setter
    def custom_ami_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a91e39dff57dc0abc6e50e192e054139d45c74fc3bc1945999d3f9468c228a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAmiId", value)

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeIops")
    def ebs_root_volume_iops(self) -> typing.Optional[jsii.Number]:
        '''The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsRootVolumeIops"))

    @ebs_root_volume_iops.setter
    def ebs_root_volume_iops(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a5180c93c70a8f43ed9835c3357a42eafc25f6dc6c5aa034d474e2f615dd1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsRootVolumeIops", value)

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeSize")
    def ebs_root_volume_size(self) -> typing.Optional[jsii.Number]:
        '''The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsRootVolumeSize"))

    @ebs_root_volume_size.setter
    def ebs_root_volume_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1be0c0b7c99ca4316b39ef88877cc04569c66abbd6ae83da0946947f1bf063)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsRootVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeThroughput")
    def ebs_root_volume_throughput(self) -> typing.Optional[jsii.Number]:
        '''The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsRootVolumeThroughput"))

    @ebs_root_volume_throughput.setter
    def ebs_root_volume_throughput(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__951b4ef3a48c5da248736a1dd98ab6d527bce3f6de302ca2d84d41ee7e213288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsRootVolumeThroughput", value)

    @builtins.property
    @jsii.member(jsii_name="kerberosAttributes")
    def kerberos_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.KerberosAttributesProperty"]]:
        '''Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.KerberosAttributesProperty"]], jsii.get(self, "kerberosAttributes"))

    @kerberos_attributes.setter
    def kerberos_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.KerberosAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb6e8fa078ddb5d5ca597385e37e266a7ee1587d10523bea725cff21909211bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kerberosAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="logEncryptionKmsKeyId")
    def log_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key used for encrypting log files.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logEncryptionKmsKeyId"))

    @log_encryption_kms_key_id.setter
    def log_encryption_kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1529c639be8052f81bd05a31b6b01a4b1b48080f7c84fe0c477a646c6ce50a4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logEncryptionKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="logUri")
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''The path to the Amazon S3 location where logs for this cluster are stored.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logUri"))

    @log_uri.setter
    def log_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c8b1a2acb54ad4aaccda0d0052a50ac533bed40115aa8e00fc6fd90bb390c42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logUri", value)

    @builtins.property
    @jsii.member(jsii_name="managedScalingPolicy")
    def managed_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ManagedScalingPolicyProperty"]]:
        '''Creates or updates a managed scaling policy for an Amazon EMR cluster.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ManagedScalingPolicyProperty"]], jsii.get(self, "managedScalingPolicy"))

    @managed_scaling_policy.setter
    def managed_scaling_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ManagedScalingPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5679f4b15ba00e5797a6ca36888a09881f956e47615cd9f237382bdc765ab756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedScalingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="osReleaseLabel")
    def os_release_label(self) -> typing.Optional[builtins.str]:
        '''The Amazon Linux release specified in a cluster launch RunJobFlow request.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osReleaseLabel"))

    @os_release_label.setter
    def os_release_label(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d4c0fd8467e6006f700dcbf1ba5095561e1d0287c44dc0c0a3753aaeb3d7d14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osReleaseLabel", value)

    @builtins.property
    @jsii.member(jsii_name="placementGroupConfigs")
    def placement_group_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.PlacementGroupConfigProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.PlacementGroupConfigProperty"]]]], jsii.get(self, "placementGroupConfigs"))

    @placement_group_configs.setter
    def placement_group_configs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.PlacementGroupConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398553fa8e4e3f5661ed1198260a3a1fcc13ee30c6c2bc59bacdcffe873be756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementGroupConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> typing.Optional[builtins.str]:
        '''The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34f4881cac49b58e2914939050f8e5a864a826f6035515c68f81b50fc7b14ded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownBehavior")
    def scale_down_behavior(self) -> typing.Optional[builtins.str]:
        '''The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownBehavior"))

    @scale_down_behavior.setter
    def scale_down_behavior(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__443405bdf72dbf025ed25339eeb1475e84c960ad6bef75c4e466da4f43b5863b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration applied to the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__882ded38da76716522321aa83b05c78696444dba276a265637df5234777b2852)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="stepConcurrencyLevel")
    def step_concurrency_level(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of steps that can be executed concurrently.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stepConcurrencyLevel"))

    @step_concurrency_level.setter
    def step_concurrency_level(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0c077452ad77e4b3be4546305a02b64cce648e3837e39a0361e2855285b9db9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stepConcurrencyLevel", value)

    @builtins.property
    @jsii.member(jsii_name="steps")
    def steps(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.StepConfigProperty"]]]]:
        '''A list of steps to run.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.StepConfigProperty"]]]], jsii.get(self, "steps"))

    @steps.setter
    def steps(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.StepConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6535ae4fb40b89a54ff36a07d45179b7d6e5504f674a8a532cde5bea87edd59e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "steps", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags associated with a cluster.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4038da1c46af7e2d9b50fc2521906fa041359d46aa05b24162a709acb1504d63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="visibleToAllUsers")
    def visible_to_all_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the cluster is visible to all IAM users of the AWS account associated with the cluster.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "visibleToAllUsers"))

    @visible_to_all_users.setter
    def visible_to_all_users(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3181237e04f1f3e57ab37ac5dcdd9cf1f158ae1015ef97f820a75179d324a382)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleToAllUsers", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ApplicationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_info": "additionalInfo",
            "args": "args",
            "name": "name",
            "version": "version",
        },
    )
    class ApplicationProperty:
        def __init__(
            self,
            *,
            additional_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
            name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``Application`` is a property of ``AWS::EMR::Cluster`` .

            The ``Application`` property type defines the open-source big data applications for EMR to install and configure when a cluster is created.

            With Amazon EMR release version 4.0 and later, the only accepted parameter is the application ``Name`` . To pass arguments to these applications, you use configuration classifications specified using JSON objects in a ``Configuration`` property. For more information, see `Configuring Applications <https://docs.aws.amazon.com//emr/latest/ReleaseGuide/emr-configure-apps.html>`_ .

            With earlier Amazon EMR releases, the application is any AWS or third-party software that you can add to the cluster. You can specify the version of the application and arguments to pass to it. Amazon EMR accepts and forwards the argument list to the corresponding installation script as a bootstrap action argument.

            :param additional_info: This option is for advanced users only. This is meta information about clusters and applications that are used for testing and troubleshooting.
            :param args: Arguments for Amazon EMR to pass to the application.
            :param name: The name of the application.
            :param version: The version of the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-application.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                application_property = emr.CfnCluster.ApplicationProperty(
                    additional_info={
                        "additional_info_key": "additionalInfo"
                    },
                    args=["args"],
                    name="name",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf8b605c327fe9a55d7a90674524f316b8f070940e929c53e1c966b8f68a18e5)
                check_type(argname="argument additional_info", value=additional_info, expected_type=type_hints["additional_info"])
                check_type(argname="argument args", value=args, expected_type=type_hints["args"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if additional_info is not None:
                self._values["additional_info"] = additional_info
            if args is not None:
                self._values["args"] = args
            if name is not None:
                self._values["name"] = name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def additional_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''This option is for advanced users only.

            This is meta information about clusters and applications that are used for testing and troubleshooting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-application.html#cfn-emr-cluster-application-additionalinfo
            '''
            result = self._values.get("additional_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Arguments for Amazon EMR to pass to the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-application.html#cfn-emr-cluster-application-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-application.html#cfn-emr-cluster-application-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-application.html#cfn-emr-cluster-application-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.AutoScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"constraints": "constraints", "rules": "rules"},
    )
    class AutoScalingPolicyProperty:
        def __init__(
            self,
            *,
            constraints: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ScalingConstraintsProperty", typing.Dict[builtins.str, typing.Any]]],
            rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ScalingRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''``AutoScalingPolicy`` is a subproperty of ``InstanceGroupConfig`` .

            ``AutoScalingPolicy`` defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. For more information, see `Using Automatic Scaling in Amazon EMR <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-automatic-scaling.html>`_ in the *Amazon EMR Management Guide* .

            :param constraints: The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
            :param rules: The scale-in and scale-out rules that comprise the automatic scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-autoscalingpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                auto_scaling_policy_property = emr.CfnCluster.AutoScalingPolicyProperty(
                    constraints=emr.CfnCluster.ScalingConstraintsProperty(
                        max_capacity=123,
                        min_capacity=123
                    ),
                    rules=[emr.CfnCluster.ScalingRuleProperty(
                        action=emr.CfnCluster.ScalingActionProperty(
                            simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                scaling_adjustment=123,
                
                                # the properties below are optional
                                adjustment_type="adjustmentType",
                                cool_down=123
                            ),
                
                            # the properties below are optional
                            market="market"
                        ),
                        name="name",
                        trigger=emr.CfnCluster.ScalingTriggerProperty(
                            cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                comparison_operator="comparisonOperator",
                                metric_name="metricName",
                                period=123,
                                threshold=123,
                
                                # the properties below are optional
                                dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                    key="key",
                                    value="value"
                                )],
                                evaluation_periods=123,
                                namespace="namespace",
                                statistic="statistic",
                                unit="unit"
                            )
                        ),
                
                        # the properties below are optional
                        description="description"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8aa5bb304f42582274159985dd72e5294f3a513707f7460a42aafb194433c6af)
                check_type(argname="argument constraints", value=constraints, expected_type=type_hints["constraints"])
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "constraints": constraints,
                "rules": rules,
            }

        @builtins.property
        def constraints(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.ScalingConstraintsProperty"]:
            '''The upper and lower Amazon EC2 instance limits for an automatic scaling policy.

            Automatic scaling activity will not cause an instance group to grow above or below these limits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-autoscalingpolicy.html#cfn-emr-cluster-autoscalingpolicy-constraints
            '''
            result = self._values.get("constraints")
            assert result is not None, "Required property 'constraints' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.ScalingConstraintsProperty"], result)

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ScalingRuleProperty"]]]:
            '''The scale-in and scale-out rules that comprise the automatic scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-autoscalingpolicy.html#cfn-emr-cluster-autoscalingpolicy-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ScalingRuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.AutoTerminationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"idle_timeout": "idleTimeout"},
    )
    class AutoTerminationPolicyProperty:
        def __init__(
            self,
            *,
            idle_timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An auto-termination policy for an Amazon EMR cluster.

            An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see `Control cluster termination <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html>`_ .

            :param idle_timeout: Specifies the amount of idle time in seconds after which the cluster automatically terminates. You can specify a minimum of 60 seconds and a maximum of 604800 seconds (seven days).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-autoterminationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                auto_termination_policy_property = emr.CfnCluster.AutoTerminationPolicyProperty(
                    idle_timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__118dc21c4af3ce0236b744a2f6b058f706aa70e288450a8771ef8efb27c9245c)
                check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if idle_timeout is not None:
                self._values["idle_timeout"] = idle_timeout

        @builtins.property
        def idle_timeout(self) -> typing.Optional[jsii.Number]:
            '''Specifies the amount of idle time in seconds after which the cluster automatically terminates.

            You can specify a minimum of 60 seconds and a maximum of 604800 seconds (seven days).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-autoterminationpolicy.html#cfn-emr-cluster-autoterminationpolicy-idletimeout
            '''
            result = self._values.get("idle_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoTerminationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.BootstrapActionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "script_bootstrap_action": "scriptBootstrapAction",
        },
    )
    class BootstrapActionConfigProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            script_bootstrap_action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ScriptBootstrapActionConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''``BootstrapActionConfig`` is a property of ``AWS::EMR::Cluster`` that can be used to run bootstrap actions on EMR clusters.

            You can use a bootstrap action to install software and configure EC2 instances for all cluster nodes before EMR installs and configures open-source big data applications on cluster instances. For more information, see `Create Bootstrap Actions to Install Additional Software <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-plan-bootstrap.html>`_ in the *Amazon EMR Management Guide* .

            :param name: The name of the bootstrap action.
            :param script_bootstrap_action: The script run by the bootstrap action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-bootstrapactionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                bootstrap_action_config_property = emr.CfnCluster.BootstrapActionConfigProperty(
                    name="name",
                    script_bootstrap_action=emr.CfnCluster.ScriptBootstrapActionConfigProperty(
                        path="path",
                
                        # the properties below are optional
                        args=["args"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8aa9f35ad922816267708196f89ee674f80a176c000f51f281f78aeea56c3575)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument script_bootstrap_action", value=script_bootstrap_action, expected_type=type_hints["script_bootstrap_action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "script_bootstrap_action": script_bootstrap_action,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the bootstrap action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-bootstrapactionconfig.html#cfn-emr-cluster-bootstrapactionconfig-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def script_bootstrap_action(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.ScriptBootstrapActionConfigProperty"]:
            '''The script run by the bootstrap action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-bootstrapactionconfig.html#cfn-emr-cluster-bootstrapactionconfig-scriptbootstrapaction
            '''
            result = self._values.get("script_bootstrap_action")
            assert result is not None, "Required property 'script_bootstrap_action' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.ScriptBootstrapActionConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BootstrapActionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.CloudWatchAlarmDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "metric_name": "metricName",
            "period": "period",
            "threshold": "threshold",
            "dimensions": "dimensions",
            "evaluation_periods": "evaluationPeriods",
            "namespace": "namespace",
            "statistic": "statistic",
            "unit": "unit",
        },
    )
    class CloudWatchAlarmDefinitionProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            metric_name: builtins.str,
            period: jsii.Number,
            threshold: jsii.Number,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.MetricDimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            evaluation_periods: typing.Optional[jsii.Number] = None,
            namespace: typing.Optional[builtins.str] = None,
            statistic: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``CloudWatchAlarmDefinition`` is a subproperty of the ``ScalingTrigger`` property, which determines when to trigger an automatic scaling activity.

            Scaling activity begins when you satisfy the defined alarm conditions.

            :param comparison_operator: Determines how the metric specified by ``MetricName`` is compared to the value specified by ``Threshold`` .
            :param metric_name: The name of the CloudWatch metric that is watched to determine an alarm condition.
            :param period: The period, in seconds, over which the statistic is applied. CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify ``300`` .
            :param threshold: The value against which the specified statistic is compared.
            :param dimensions: A CloudWatch metric dimension.
            :param evaluation_periods: The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is ``1`` .
            :param namespace: The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .
            :param statistic: The statistic to apply to the metric associated with the alarm. The default is ``AVERAGE`` .
            :param unit: The unit of measure associated with the CloudWatch metric being watched. The value specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                cloud_watch_alarm_definition_property = emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                    comparison_operator="comparisonOperator",
                    metric_name="metricName",
                    period=123,
                    threshold=123,
                
                    # the properties below are optional
                    dimensions=[emr.CfnCluster.MetricDimensionProperty(
                        key="key",
                        value="value"
                    )],
                    evaluation_periods=123,
                    namespace="namespace",
                    statistic="statistic",
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0c6e9b1e6ddd9e7394a707f10838024730233a6162319152afb182065f469e4)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument period", value=period, expected_type=type_hints["period"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "metric_name": metric_name,
                "period": period,
                "threshold": threshold,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if evaluation_periods is not None:
                self._values["evaluation_periods"] = evaluation_periods
            if namespace is not None:
                self._values["namespace"] = namespace
            if statistic is not None:
                self._values["statistic"] = statistic
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''Determines how the metric specified by ``MetricName`` is compared to the value specified by ``Threshold`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the CloudWatch metric that is watched to determine an alarm condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''The period, in seconds, over which the statistic is applied.

            CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify ``300`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''The value against which the specified statistic is compared.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.MetricDimensionProperty"]]]]:
            '''A CloudWatch metric dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.MetricDimensionProperty"]]]], result)

        @builtins.property
        def evaluation_periods(self) -> typing.Optional[jsii.Number]:
            '''The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity.

            The default value is ``1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-evaluationperiods
            '''
            result = self._values.get("evaluation_periods")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace for the CloudWatch metric.

            The default is ``AWS/ElasticMapReduce`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def statistic(self) -> typing.Optional[builtins.str]:
            '''The statistic to apply to the metric associated with the alarm.

            The default is ``AVERAGE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-statistic
            '''
            result = self._values.get("statistic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit of measure associated with the CloudWatch metric being watched.

            The value specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-cloudwatchalarmdefinition.html#cfn-emr-cluster-cloudwatchalarmdefinition-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchAlarmDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ComputeLimitsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maximum_capacity_units": "maximumCapacityUnits",
            "minimum_capacity_units": "minimumCapacityUnits",
            "unit_type": "unitType",
            "maximum_core_capacity_units": "maximumCoreCapacityUnits",
            "maximum_on_demand_capacity_units": "maximumOnDemandCapacityUnits",
        },
    )
    class ComputeLimitsProperty:
        def __init__(
            self,
            *,
            maximum_capacity_units: jsii.Number,
            minimum_capacity_units: jsii.Number,
            unit_type: builtins.str,
            maximum_core_capacity_units: typing.Optional[jsii.Number] = None,
            maximum_on_demand_capacity_units: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The Amazon EC2 unit limits for a managed scaling policy.

            The managed scaling activity of a cluster can not be above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

            :param maximum_capacity_units: The upper boundary of Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
            :param minimum_capacity_units: The lower boundary of Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
            :param unit_type: The unit type used for specifying a managed scaling policy.
            :param maximum_core_capacity_units: The upper boundary of Amazon EC2 units for core node type in a cluster. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The core units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between core and task nodes.
            :param maximum_on_demand_capacity_units: The upper boundary of On-Demand Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The On-Demand units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between On-Demand and Spot Instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-computelimits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                compute_limits_property = emr.CfnCluster.ComputeLimitsProperty(
                    maximum_capacity_units=123,
                    minimum_capacity_units=123,
                    unit_type="unitType",
                
                    # the properties below are optional
                    maximum_core_capacity_units=123,
                    maximum_on_demand_capacity_units=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ecc8cf0c083fcbbc2c4e1910146ba4c6c959a6e36991ec830a52e0262a1b06e8)
                check_type(argname="argument maximum_capacity_units", value=maximum_capacity_units, expected_type=type_hints["maximum_capacity_units"])
                check_type(argname="argument minimum_capacity_units", value=minimum_capacity_units, expected_type=type_hints["minimum_capacity_units"])
                check_type(argname="argument unit_type", value=unit_type, expected_type=type_hints["unit_type"])
                check_type(argname="argument maximum_core_capacity_units", value=maximum_core_capacity_units, expected_type=type_hints["maximum_core_capacity_units"])
                check_type(argname="argument maximum_on_demand_capacity_units", value=maximum_on_demand_capacity_units, expected_type=type_hints["maximum_on_demand_capacity_units"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "maximum_capacity_units": maximum_capacity_units,
                "minimum_capacity_units": minimum_capacity_units,
                "unit_type": unit_type,
            }
            if maximum_core_capacity_units is not None:
                self._values["maximum_core_capacity_units"] = maximum_core_capacity_units
            if maximum_on_demand_capacity_units is not None:
                self._values["maximum_on_demand_capacity_units"] = maximum_on_demand_capacity_units

        @builtins.property
        def maximum_capacity_units(self) -> jsii.Number:
            '''The upper boundary of Amazon EC2 units.

            It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-computelimits.html#cfn-emr-cluster-computelimits-maximumcapacityunits
            '''
            result = self._values.get("maximum_capacity_units")
            assert result is not None, "Required property 'maximum_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def minimum_capacity_units(self) -> jsii.Number:
            '''The lower boundary of Amazon EC2 units.

            It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-computelimits.html#cfn-emr-cluster-computelimits-minimumcapacityunits
            '''
            result = self._values.get("minimum_capacity_units")
            assert result is not None, "Required property 'minimum_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unit_type(self) -> builtins.str:
            '''The unit type used for specifying a managed scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-computelimits.html#cfn-emr-cluster-computelimits-unittype
            '''
            result = self._values.get("unit_type")
            assert result is not None, "Required property 'unit_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maximum_core_capacity_units(self) -> typing.Optional[jsii.Number]:
            '''The upper boundary of Amazon EC2 units for core node type in a cluster.

            It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The core units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between core and task nodes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-computelimits.html#cfn-emr-cluster-computelimits-maximumcorecapacityunits
            '''
            result = self._values.get("maximum_core_capacity_units")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_on_demand_capacity_units(self) -> typing.Optional[jsii.Number]:
            '''The upper boundary of On-Demand Amazon EC2 units.

            It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The On-Demand units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between On-Demand and Spot Instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-computelimits.html#cfn-emr-cluster-computelimits-maximumondemandcapacityunits
            '''
            result = self._values.get("maximum_on_demand_capacity_units")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeLimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configuration_properties": "configurationProperties",
            "configurations": "configurations",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            classification: typing.Optional[builtins.str] = None,
            configuration_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''.. epigraph::

   Used only with Amazon EMR release 4.0 and later.

            ``Configuration`` is a subproperty of ``InstanceFleetConfig`` or ``InstanceGroupConfig`` . ``Configuration`` specifies optional configurations for customizing open-source big data applications and environment parameters. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see `Configuring Applications <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`_ in the *Amazon EMR Release Guide* .

            :param classification: The classification within a configuration.
            :param configuration_properties: A list of additional configurations to apply within a configuration object.
            :param configurations: A list of additional configurations to apply within a configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                # configuration_property_: emr.CfnCluster.ConfigurationProperty
                
                configuration_property = emr.CfnCluster.ConfigurationProperty(
                    classification="classification",
                    configuration_properties={
                        "configuration_properties_key": "configurationProperties"
                    },
                    configurations=[configuration_property_]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__762e4654096c644b1ccf34d3832fa5e53cc3647761f6d0a0ed19865f7efb39db)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument configuration_properties", value=configuration_properties, expected_type=type_hints["configuration_properties"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if classification is not None:
                self._values["classification"] = classification
            if configuration_properties is not None:
                self._values["configuration_properties"] = configuration_properties
            if configurations is not None:
                self._values["configurations"] = configurations

        @builtins.property
        def classification(self) -> typing.Optional[builtins.str]:
            '''The classification within a configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-classification
            '''
            result = self._values.get("classification")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configuration_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''A list of additional configurations to apply within a configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-configurationproperties
            '''
            result = self._values.get("configuration_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]]:
            '''A list of additional configurations to apply within a configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.EbsBlockDeviceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "volume_specification": "volumeSpecification",
            "volumes_per_instance": "volumesPerInstance",
        },
    )
    class EbsBlockDeviceConfigProperty:
        def __init__(
            self,
            *,
            volume_specification: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.VolumeSpecificationProperty", typing.Dict[builtins.str, typing.Any]]],
            volumes_per_instance: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``EbsBlockDeviceConfig`` is a subproperty of the ``EbsConfiguration`` property type.

            ``EbsBlockDeviceConfig`` defines the number and type of EBS volumes to associate with all EC2 instances in an EMR cluster.

            :param volume_specification: EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.
            :param volumes_per_instance: Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-ebsblockdeviceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                ebs_block_device_config_property = emr.CfnCluster.EbsBlockDeviceConfigProperty(
                    volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                        size_in_gb=123,
                        volume_type="volumeType",
                
                        # the properties below are optional
                        iops=123,
                        throughput=123
                    ),
                
                    # the properties below are optional
                    volumes_per_instance=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5126d3ffa8a013f43ff9f99f79a23a9a3d3aa03919b6fe5d784b7a28817bf3f0)
                check_type(argname="argument volume_specification", value=volume_specification, expected_type=type_hints["volume_specification"])
                check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "volume_specification": volume_specification,
            }
            if volumes_per_instance is not None:
                self._values["volumes_per_instance"] = volumes_per_instance

        @builtins.property
        def volume_specification(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.VolumeSpecificationProperty"]:
            '''EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-ebsblockdeviceconfig.html#cfn-emr-cluster-ebsblockdeviceconfig-volumespecification
            '''
            result = self._values.get("volume_specification")
            assert result is not None, "Required property 'volume_specification' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.VolumeSpecificationProperty"], result)

        @builtins.property
        def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
            '''Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-ebsblockdeviceconfig.html#cfn-emr-cluster-ebsblockdeviceconfig-volumesperinstance
            '''
            result = self._values.get("volumes_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.EbsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_block_device_configs": "ebsBlockDeviceConfigs",
            "ebs_optimized": "ebsOptimized",
        },
    )
    class EbsConfigurationProperty:
        def __init__(
            self,
            *,
            ebs_block_device_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EbsBlockDeviceConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''``EbsConfiguration`` is a subproperty of ``InstanceFleetConfig`` or ``InstanceGroupConfig`` .

            ``EbsConfiguration`` determines the EBS volumes to attach to EMR cluster instances.

            :param ebs_block_device_configs: An array of Amazon EBS volume specifications attached to a cluster instance.
            :param ebs_optimized: Indicates whether an Amazon EBS volume is EBS-optimized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-ebsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                ebs_configuration_property = emr.CfnCluster.EbsConfigurationProperty(
                    ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                        volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                            size_in_gb=123,
                            volume_type="volumeType",
                
                            # the properties below are optional
                            iops=123,
                            throughput=123
                        ),
                
                        # the properties below are optional
                        volumes_per_instance=123
                    )],
                    ebs_optimized=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__289a0cf33d6f771401695f26c373e2ed078bce1f2750d4690cc1d0b1c482e235)
                check_type(argname="argument ebs_block_device_configs", value=ebs_block_device_configs, expected_type=type_hints["ebs_block_device_configs"])
                check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ebs_block_device_configs is not None:
                self._values["ebs_block_device_configs"] = ebs_block_device_configs
            if ebs_optimized is not None:
                self._values["ebs_optimized"] = ebs_optimized

        @builtins.property
        def ebs_block_device_configs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.EbsBlockDeviceConfigProperty"]]]]:
            '''An array of Amazon EBS volume specifications attached to a cluster instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-ebsconfiguration.html#cfn-emr-cluster-ebsconfiguration-ebsblockdeviceconfigs
            '''
            result = self._values.get("ebs_block_device_configs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.EbsBlockDeviceConfigProperty"]]]], result)

        @builtins.property
        def ebs_optimized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether an Amazon EBS volume is EBS-optimized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-ebsconfiguration.html#cfn-emr-cluster-ebsconfiguration-ebsoptimized
            '''
            result = self._values.get("ebs_optimized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.HadoopJarStepConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "jar": "jar",
            "args": "args",
            "main_class": "mainClass",
            "step_properties": "stepProperties",
        },
    )
    class HadoopJarStepConfigProperty:
        def __init__(
            self,
            *,
            jar: builtins.str,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
            main_class: typing.Optional[builtins.str] = None,
            step_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.KeyValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``HadoopJarStepConfig`` property type specifies a job flow step consisting of a JAR file whose main function will be executed.

            The main function submits a job for the cluster to execute as a step on the master node, and then waits for the job to finish or fail before executing subsequent steps.

            :param jar: A path to a JAR file run during the step.
            :param args: A list of command line arguments passed to the JAR file's main function when executed.
            :param main_class: The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
            :param step_properties: A list of Java properties that are set when the step runs. You can use these properties to pass key-value pairs to your main function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-hadoopjarstepconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                hadoop_jar_step_config_property = emr.CfnCluster.HadoopJarStepConfigProperty(
                    jar="jar",
                
                    # the properties below are optional
                    args=["args"],
                    main_class="mainClass",
                    step_properties=[emr.CfnCluster.KeyValueProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c3086fca1cb7ccf0ee3e0ba36727f8170913cea7fcd41960c212cbe4f26f9fea)
                check_type(argname="argument jar", value=jar, expected_type=type_hints["jar"])
                check_type(argname="argument args", value=args, expected_type=type_hints["args"])
                check_type(argname="argument main_class", value=main_class, expected_type=type_hints["main_class"])
                check_type(argname="argument step_properties", value=step_properties, expected_type=type_hints["step_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "jar": jar,
            }
            if args is not None:
                self._values["args"] = args
            if main_class is not None:
                self._values["main_class"] = main_class
            if step_properties is not None:
                self._values["step_properties"] = step_properties

        @builtins.property
        def jar(self) -> builtins.str:
            '''A path to a JAR file run during the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-hadoopjarstepconfig.html#cfn-emr-cluster-hadoopjarstepconfig-jar
            '''
            result = self._values.get("jar")
            assert result is not None, "Required property 'jar' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of command line arguments passed to the JAR file's main function when executed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-hadoopjarstepconfig.html#cfn-emr-cluster-hadoopjarstepconfig-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def main_class(self) -> typing.Optional[builtins.str]:
            '''The name of the main class in the specified Java file.

            If not specified, the JAR file should specify a Main-Class in its manifest file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-hadoopjarstepconfig.html#cfn-emr-cluster-hadoopjarstepconfig-mainclass
            '''
            result = self._values.get("main_class")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def step_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.KeyValueProperty"]]]]:
            '''A list of Java properties that are set when the step runs.

            You can use these properties to pass key-value pairs to your main function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-hadoopjarstepconfig.html#cfn-emr-cluster-hadoopjarstepconfig-stepproperties
            '''
            result = self._values.get("step_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.KeyValueProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HadoopJarStepConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.InstanceFleetConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type_configs": "instanceTypeConfigs",
            "launch_specifications": "launchSpecifications",
            "name": "name",
            "target_on_demand_capacity": "targetOnDemandCapacity",
            "target_spot_capacity": "targetSpotCapacity",
        },
    )
    class InstanceFleetConfigProperty:
        def __init__(
            self,
            *,
            instance_type_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.InstanceTypeConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            launch_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.InstanceFleetProvisioningSpecificationsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
            target_on_demand_capacity: typing.Optional[jsii.Number] = None,
            target_spot_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Use ``InstanceFleetConfig`` to define instance fleets for an EMR cluster.

            A cluster can not use both instance fleets and instance groups. For more information, see `Configure Instance Fleets <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-instance-group-configuration.html>`_ in the *Amazon EMR Management Guide* .
            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

            :param instance_type_configs: The instance type configurations that define the Amazon EC2 instances in the instance fleet.
            :param launch_specifications: The launch specification for the instance fleet.
            :param name: The friendly name of the instance fleet.
            :param target_on_demand_capacity: The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. .. epigraph:: If not specified or set to 0, only Spot instances are provisioned for the instance fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.
            :param target_spot_capacity: The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When a Spot instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. .. epigraph:: If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                # configuration_property_: emr.CfnCluster.ConfigurationProperty
                
                instance_fleet_config_property = emr.CfnCluster.InstanceFleetConfigProperty(
                    instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                        instance_type="instanceType",
                
                        # the properties below are optional
                        bid_price="bidPrice",
                        bid_price_as_percentage_of_on_demand_price=123,
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
                
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
                
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        weighted_capacity=123
                    )],
                    launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                        on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                            allocation_strategy="allocationStrategy"
                        ),
                        spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                            timeout_action="timeoutAction",
                            timeout_duration_minutes=123,
                
                            # the properties below are optional
                            allocation_strategy="allocationStrategy",
                            block_duration_minutes=123
                        )
                    ),
                    name="name",
                    target_on_demand_capacity=123,
                    target_spot_capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b48fe88bfe7ab8726e3ed373177e22463a0bb5c19fdfb6f4bb239aedc4a5d1ac)
                check_type(argname="argument instance_type_configs", value=instance_type_configs, expected_type=type_hints["instance_type_configs"])
                check_type(argname="argument launch_specifications", value=launch_specifications, expected_type=type_hints["launch_specifications"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument target_on_demand_capacity", value=target_on_demand_capacity, expected_type=type_hints["target_on_demand_capacity"])
                check_type(argname="argument target_spot_capacity", value=target_spot_capacity, expected_type=type_hints["target_spot_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if instance_type_configs is not None:
                self._values["instance_type_configs"] = instance_type_configs
            if launch_specifications is not None:
                self._values["launch_specifications"] = launch_specifications
            if name is not None:
                self._values["name"] = name
            if target_on_demand_capacity is not None:
                self._values["target_on_demand_capacity"] = target_on_demand_capacity
            if target_spot_capacity is not None:
                self._values["target_spot_capacity"] = target_spot_capacity

        @builtins.property
        def instance_type_configs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceTypeConfigProperty"]]]]:
            '''The instance type configurations that define the Amazon EC2 instances in the instance fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetconfig.html#cfn-emr-cluster-instancefleetconfig-instancetypeconfigs
            '''
            result = self._values.get("instance_type_configs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceTypeConfigProperty"]]]], result)

        @builtins.property
        def launch_specifications(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceFleetProvisioningSpecificationsProperty"]]:
            '''The launch specification for the instance fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetconfig.html#cfn-emr-cluster-instancefleetconfig-launchspecifications
            '''
            result = self._values.get("launch_specifications")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceFleetProvisioningSpecificationsProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The friendly name of the instance fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetconfig.html#cfn-emr-cluster-instancefleetconfig-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
            '''The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision.

            When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
            .. epigraph::

               If not specified or set to 0, only Spot instances are provisioned for the instance fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetconfig.html#cfn-emr-cluster-instancefleetconfig-targetondemandcapacity
            '''
            result = self._values.get("target_on_demand_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
            '''The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision.

            When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When a Spot instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
            .. epigraph::

               If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetconfig.html#cfn-emr-cluster-instancefleetconfig-targetspotcapacity
            '''
            result = self._values.get("target_spot_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceFleetConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "on_demand_specification": "onDemandSpecification",
            "spot_specification": "spotSpecification",
        },
    )
    class InstanceFleetProvisioningSpecificationsProperty:
        def __init__(
            self,
            *,
            on_demand_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.OnDemandProvisioningSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            spot_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.SpotProvisioningSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''``InstanceFleetProvisioningSpecification`` is a subproperty of ``InstanceFleetConfig`` .

            ``InstanceFleetProvisioningSpecification`` defines the launch specification for Spot instances in an instance fleet, which determines the defined duration and provisioning timeout behavior for Spot instances.
            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

            :param on_demand_specification: The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy. .. epigraph:: The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.
            :param spot_specification: The launch specification for Spot instances in the fleet, which determines the defined duration, provisioning timeout behavior, and allocation strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetprovisioningspecifications.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                instance_fleet_provisioning_specifications_property = emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                    on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                        allocation_strategy="allocationStrategy"
                    ),
                    spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                        timeout_action="timeoutAction",
                        timeout_duration_minutes=123,
                
                        # the properties below are optional
                        allocation_strategy="allocationStrategy",
                        block_duration_minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b138f924cf93d1337c2cb3bdd25dfbcf94457589d616a6f7829b0bcd0a10149)
                check_type(argname="argument on_demand_specification", value=on_demand_specification, expected_type=type_hints["on_demand_specification"])
                check_type(argname="argument spot_specification", value=spot_specification, expected_type=type_hints["spot_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if on_demand_specification is not None:
                self._values["on_demand_specification"] = on_demand_specification
            if spot_specification is not None:
                self._values["spot_specification"] = spot_specification

        @builtins.property
        def on_demand_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.OnDemandProvisioningSpecificationProperty"]]:
            '''The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy.

            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetprovisioningspecifications.html#cfn-emr-cluster-instancefleetprovisioningspecifications-ondemandspecification
            '''
            result = self._values.get("on_demand_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.OnDemandProvisioningSpecificationProperty"]], result)

        @builtins.property
        def spot_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SpotProvisioningSpecificationProperty"]]:
            '''The launch specification for Spot instances in the fleet, which determines the defined duration, provisioning timeout behavior, and allocation strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancefleetprovisioningspecifications.html#cfn-emr-cluster-instancefleetprovisioningspecifications-spotspecification
            '''
            result = self._values.get("spot_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SpotProvisioningSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceFleetProvisioningSpecificationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.InstanceGroupConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "auto_scaling_policy": "autoScalingPolicy",
            "bid_price": "bidPrice",
            "configurations": "configurations",
            "custom_ami_id": "customAmiId",
            "ebs_configuration": "ebsConfiguration",
            "market": "market",
            "name": "name",
        },
    )
    class InstanceGroupConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.AutoScalingPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            bid_price: typing.Optional[builtins.str] = None,
            configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            custom_ami_id: typing.Optional[builtins.str] = None,
            ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EbsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            market: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use ``InstanceGroupConfig`` to define instance groups for an EMR cluster.

            A cluster can not use both instance groups and instance fleets. For more information, see `Create a Cluster with Instance Fleets or Uniform Instance Groups <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-instance-group-configuration.html>`_ in the *Amazon EMR Management Guide* .

            :param instance_count: Target number of instances for the instance group.
            :param instance_type: The Amazon EC2 instance type for all instances in the instance group.
            :param auto_scaling_policy: ``AutoScalingPolicy`` is a subproperty of the `InstanceGroupConfig <https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig-instancegroupconfig.html>`_ property type that specifies the constraints and rules of an automatic scaling policy in Amazon EMR . The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. Only core and task instance groups can use automatic scaling policies. For more information, see `Using Automatic Scaling in Amazon EMR <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-automatic-scaling.html>`_ .
            :param bid_price: If specified, indicates that the instance group uses Spot Instances. This is the maximum price you are willing to pay for Spot Instances. Specify ``OnDemandPrice`` to set the amount equal to the On-Demand price, or specify an amount in USD.
            :param configurations: .. epigraph:: Amazon EMR releases 4.x or later. The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).
            :param custom_ami_id: The custom AMI ID to use for the provisioned instance group.
            :param ebs_configuration: EBS configurations that will be attached to each Amazon EC2 instance in the instance group.
            :param market: Market type of the Amazon EC2 instances used to create a cluster node.
            :param name: Friendly name given to the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                # configuration_property_: emr.CfnCluster.ConfigurationProperty
                
                instance_group_config_property = emr.CfnCluster.InstanceGroupConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                
                    # the properties below are optional
                    auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                        constraints=emr.CfnCluster.ScalingConstraintsProperty(
                            max_capacity=123,
                            min_capacity=123
                        ),
                        rules=[emr.CfnCluster.ScalingRuleProperty(
                            action=emr.CfnCluster.ScalingActionProperty(
                                simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                    scaling_adjustment=123,
                
                                    # the properties below are optional
                                    adjustment_type="adjustmentType",
                                    cool_down=123
                                ),
                
                                # the properties below are optional
                                market="market"
                            ),
                            name="name",
                            trigger=emr.CfnCluster.ScalingTriggerProperty(
                                cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                    comparison_operator="comparisonOperator",
                                    metric_name="metricName",
                                    period=123,
                                    threshold=123,
                
                                    # the properties below are optional
                                    dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                        key="key",
                                        value="value"
                                    )],
                                    evaluation_periods=123,
                                    namespace="namespace",
                                    statistic="statistic",
                                    unit="unit"
                                )
                            ),
                
                            # the properties below are optional
                            description="description"
                        )]
                    ),
                    bid_price="bidPrice",
                    configurations=[emr.CfnCluster.ConfigurationProperty(
                        classification="classification",
                        configuration_properties={
                            "configuration_properties_key": "configurationProperties"
                        },
                        configurations=[configuration_property_]
                    )],
                    custom_ami_id="customAmiId",
                    ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                        ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                            volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                size_in_gb=123,
                                volume_type="volumeType",
                
                                # the properties below are optional
                                iops=123,
                                throughput=123
                            ),
                
                            # the properties below are optional
                            volumes_per_instance=123
                        )],
                        ebs_optimized=False
                    ),
                    market="market",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16e3a62519b2b5fb87993923e143b12cd90ce3e00aa04b8e01ea10a6242471d9)
                check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument auto_scaling_policy", value=auto_scaling_policy, expected_type=type_hints["auto_scaling_policy"])
                check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
                check_type(argname="argument custom_ami_id", value=custom_ami_id, expected_type=type_hints["custom_ami_id"])
                check_type(argname="argument ebs_configuration", value=ebs_configuration, expected_type=type_hints["ebs_configuration"])
                check_type(argname="argument market", value=market, expected_type=type_hints["market"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
            }
            if auto_scaling_policy is not None:
                self._values["auto_scaling_policy"] = auto_scaling_policy
            if bid_price is not None:
                self._values["bid_price"] = bid_price
            if configurations is not None:
                self._values["configurations"] = configurations
            if custom_ami_id is not None:
                self._values["custom_ami_id"] = custom_ami_id
            if ebs_configuration is not None:
                self._values["ebs_configuration"] = ebs_configuration
            if market is not None:
                self._values["market"] = market
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''Target number of instances for the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''The Amazon EC2 instance type for all instances in the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_scaling_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AutoScalingPolicyProperty"]]:
            '''``AutoScalingPolicy`` is a subproperty of the `InstanceGroupConfig <https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig-instancegroupconfig.html>`_ property type that specifies the constraints and rules of an automatic scaling policy in Amazon EMR . The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. Only core and task instance groups can use automatic scaling policies. For more information, see `Using Automatic Scaling in Amazon EMR <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-automatic-scaling.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-autoscalingpolicy
            '''
            result = self._values.get("auto_scaling_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AutoScalingPolicyProperty"]], result)

        @builtins.property
        def bid_price(self) -> typing.Optional[builtins.str]:
            '''If specified, indicates that the instance group uses Spot Instances.

            This is the maximum price you are willing to pay for Spot Instances. Specify ``OnDemandPrice`` to set the amount equal to the On-Demand price, or specify an amount in USD.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-bidprice
            '''
            result = self._values.get("bid_price")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]]:
            '''.. epigraph::

   Amazon EMR releases 4.x or later.

            The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]], result)

        @builtins.property
        def custom_ami_id(self) -> typing.Optional[builtins.str]:
            '''The custom AMI ID to use for the provisioned instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-customamiid
            '''
            result = self._values.get("custom_ami_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EbsConfigurationProperty"]]:
            '''EBS configurations that will be attached to each Amazon EC2 instance in the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-ebsconfiguration
            '''
            result = self._values.get("ebs_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EbsConfigurationProperty"]], result)

        @builtins.property
        def market(self) -> typing.Optional[builtins.str]:
            '''Market type of the Amazon EC2 instances used to create a cluster node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-market
            '''
            result = self._values.get("market")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Friendly name given to the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancegroupconfig.html#cfn-emr-cluster-instancegroupconfig-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceGroupConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.InstanceTypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "bid_price": "bidPrice",
            "bid_price_as_percentage_of_on_demand_price": "bidPriceAsPercentageOfOnDemandPrice",
            "configurations": "configurations",
            "custom_ami_id": "customAmiId",
            "ebs_configuration": "ebsConfiguration",
            "weighted_capacity": "weightedCapacity",
        },
    )
    class InstanceTypeConfigProperty:
        def __init__(
            self,
            *,
            instance_type: builtins.str,
            bid_price: typing.Optional[builtins.str] = None,
            bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
            configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            custom_ami_id: typing.Optional[builtins.str] = None,
            ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.EbsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            weighted_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''.. epigraph::

   The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

            ``InstanceTypeConfig`` is a sub-property of ``InstanceFleetConfig`` . ``InstanceTypeConfig`` determines the EC2 instances that Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities.

            :param instance_type: An Amazon EC2 instance type, such as ``m3.xlarge`` .
            :param bid_price: The bid price for each Amazon EC2 Spot Instance type as defined by ``InstanceType`` . Expressed in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.
            :param bid_price_as_percentage_of_on_demand_price: The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%). If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.
            :param configurations: A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.
            :param custom_ami_id: The custom AMI ID to use for the instance type.
            :param ebs_configuration: The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by ``InstanceType`` .
            :param weighted_capacity: The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in ``InstanceFleetConfig`` . This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancetypeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                # configuration_property_: emr.CfnCluster.ConfigurationProperty
                
                instance_type_config_property = emr.CfnCluster.InstanceTypeConfigProperty(
                    instance_type="instanceType",
                
                    # the properties below are optional
                    bid_price="bidPrice",
                    bid_price_as_percentage_of_on_demand_price=123,
                    configurations=[emr.CfnCluster.ConfigurationProperty(
                        classification="classification",
                        configuration_properties={
                            "configuration_properties_key": "configurationProperties"
                        },
                        configurations=[configuration_property_]
                    )],
                    custom_ami_id="customAmiId",
                    ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                        ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                            volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                size_in_gb=123,
                                volume_type="volumeType",
                
                                # the properties below are optional
                                iops=123,
                                throughput=123
                            ),
                
                            # the properties below are optional
                            volumes_per_instance=123
                        )],
                        ebs_optimized=False
                    ),
                    weighted_capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e04c7cf6db409085e044ff55b4223b3cfbcb9f86e3c1e3385c072880c8a6af8)
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
                check_type(argname="argument bid_price_as_percentage_of_on_demand_price", value=bid_price_as_percentage_of_on_demand_price, expected_type=type_hints["bid_price_as_percentage_of_on_demand_price"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
                check_type(argname="argument custom_ami_id", value=custom_ami_id, expected_type=type_hints["custom_ami_id"])
                check_type(argname="argument ebs_configuration", value=ebs_configuration, expected_type=type_hints["ebs_configuration"])
                check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_type": instance_type,
            }
            if bid_price is not None:
                self._values["bid_price"] = bid_price
            if bid_price_as_percentage_of_on_demand_price is not None:
                self._values["bid_price_as_percentage_of_on_demand_price"] = bid_price_as_percentage_of_on_demand_price
            if configurations is not None:
                self._values["configurations"] = configurations
            if custom_ami_id is not None:
                self._values["custom_ami_id"] = custom_ami_id
            if ebs_configuration is not None:
                self._values["ebs_configuration"] = ebs_configuration
            if weighted_capacity is not None:
                self._values["weighted_capacity"] = weighted_capacity

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''An Amazon EC2 instance type, such as ``m3.xlarge`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancetypeconfig.html#cfn-emr-cluster-instancetypeconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bid_price(self) -> typing.Optional[builtins.str]:
            '''The bid price for each Amazon EC2 Spot Instance type as defined by ``InstanceType`` .

            Expressed in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancetypeconfig.html#cfn-emr-cluster-instancetypeconfig-bidprice
            '''
            result = self._values.get("bid_price")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bid_price_as_percentage_of_on_demand_price(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by ``InstanceType`` .

            Expressed as a number (for example, 20 specifies 20%). If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancetypeconfig.html#cfn-emr-cluster-instancetypeconfig-bidpriceaspercentageofondemandprice
            '''
            result = self._values.get("bid_price_as_percentage_of_on_demand_price")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]]:
            '''A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancetypeconfig.html#cfn-emr-cluster-instancetypeconfig-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.ConfigurationProperty"]]]], result)

        @builtins.property
        def custom_ami_id(self) -> typing.Optional[builtins.str]:
            '''The custom AMI ID to use for the instance type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancetypeconfig.html#cfn-emr-cluster-instancetypeconfig-customamiid
            '''
            result = self._values.get("custom_ami_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EbsConfigurationProperty"]]:
            '''The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by ``InstanceType`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancetypeconfig.html#cfn-emr-cluster-instancetypeconfig-ebsconfiguration
            '''
            result = self._values.get("ebs_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.EbsConfigurationProperty"]], result)

        @builtins.property
        def weighted_capacity(self) -> typing.Optional[jsii.Number]:
            '''The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in ``InstanceFleetConfig`` .

            This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-instancetypeconfig.html#cfn-emr-cluster-instancetypeconfig-weightedcapacity
            '''
            result = self._values.get("weighted_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceTypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.JobFlowInstancesConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_master_security_groups": "additionalMasterSecurityGroups",
            "additional_slave_security_groups": "additionalSlaveSecurityGroups",
            "core_instance_fleet": "coreInstanceFleet",
            "core_instance_group": "coreInstanceGroup",
            "ec2_key_name": "ec2KeyName",
            "ec2_subnet_id": "ec2SubnetId",
            "ec2_subnet_ids": "ec2SubnetIds",
            "emr_managed_master_security_group": "emrManagedMasterSecurityGroup",
            "emr_managed_slave_security_group": "emrManagedSlaveSecurityGroup",
            "hadoop_version": "hadoopVersion",
            "keep_job_flow_alive_when_no_steps": "keepJobFlowAliveWhenNoSteps",
            "master_instance_fleet": "masterInstanceFleet",
            "master_instance_group": "masterInstanceGroup",
            "placement": "placement",
            "service_access_security_group": "serviceAccessSecurityGroup",
            "task_instance_fleets": "taskInstanceFleets",
            "task_instance_groups": "taskInstanceGroups",
            "termination_protected": "terminationProtected",
            "unhealthy_node_replacement": "unhealthyNodeReplacement",
        },
    )
    class JobFlowInstancesConfigProperty:
        def __init__(
            self,
            *,
            additional_master_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            additional_slave_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            core_instance_fleet: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.InstanceFleetConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            core_instance_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.InstanceGroupConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ec2_key_name: typing.Optional[builtins.str] = None,
            ec2_subnet_id: typing.Optional[builtins.str] = None,
            ec2_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            emr_managed_master_security_group: typing.Optional[builtins.str] = None,
            emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
            hadoop_version: typing.Optional[builtins.str] = None,
            keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            master_instance_fleet: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.InstanceFleetConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            master_instance_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.InstanceGroupConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            placement: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.PlacementTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_access_security_group: typing.Optional[builtins.str] = None,
            task_instance_fleets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.InstanceFleetConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            task_instance_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.InstanceGroupConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            termination_protected: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            unhealthy_node_replacement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''``JobFlowInstancesConfig`` is a property of the ``AWS::EMR::Cluster`` resource.

            ``JobFlowInstancesConfig`` defines the instance groups or instance fleets that comprise the cluster. ``JobFlowInstancesConfig`` must contain either ``InstanceFleetConfig`` or ``InstanceGroupConfig`` . They cannot be used together.

            You can now define task instance groups or task instance fleets using the ``TaskInstanceGroups`` and ``TaskInstanceFleets`` subproperties. Using these subproperties reduces delays in provisioning task nodes compared to specifying task nodes with the ``InstanceFleetConfig`` and ``InstanceGroupConfig`` resources.

            :param additional_master_security_groups: A list of additional Amazon EC2 security group IDs for the master node.
            :param additional_slave_security_groups: A list of additional Amazon EC2 security group IDs for the core and task nodes.
            :param core_instance_fleet: Describes the EC2 instances and instance configurations for the core instance fleet when using clusters with the instance fleet configuration.
            :param core_instance_group: Describes the EC2 instances and instance configurations for core instance groups when using clusters with the uniform instance group configuration.
            :param ec2_key_name: The name of the Amazon EC2 key pair that can be used to connect to the master node using SSH as the user called "hadoop.".
            :param ec2_subnet_id: Applies to clusters that use the uniform instance group configuration. To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value and your account supports EC2-Classic, the cluster launches in EC2-Classic.
            :param ec2_subnet_ids: Applies to clusters that use the instance fleet configuration. When multiple Amazon EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet. .. epigraph:: The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.
            :param emr_managed_master_security_group: The identifier of the Amazon EC2 security group for the master node. If you specify ``EmrManagedMasterSecurityGroup`` , you must also specify ``EmrManagedSlaveSecurityGroup`` .
            :param emr_managed_slave_security_group: The identifier of the Amazon EC2 security group for the core and task nodes. If you specify ``EmrManagedSlaveSecurityGroup`` , you must also specify ``EmrManagedMasterSecurityGroup`` .
            :param hadoop_version: Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop version for the cluster. Valid inputs are "0.18" (no longer maintained), "0.20" (no longer maintained), "0.20.205" (no longer maintained), "1.0.3", "2.2.0", or "2.4.0". If you do not set this value, the default of 0.18 is used, unless the ``AmiVersion`` parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.
            :param keep_job_flow_alive_when_no_steps: Specifies whether the cluster should remain available after completing all steps. Defaults to ``false`` . For more information about configuring cluster termination, see `Control Cluster Termination <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html>`_ in the *EMR Management Guide* .
            :param master_instance_fleet: Describes the EC2 instances and instance configurations for the master instance fleet when using clusters with the instance fleet configuration.
            :param master_instance_group: Describes the EC2 instances and instance configurations for the master instance group when using clusters with the uniform instance group configuration.
            :param placement: The Availability Zone in which the cluster runs.
            :param service_access_security_group: The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.
            :param task_instance_fleets: Describes the EC2 instances and instance configurations for the task instance fleets when using clusters with the instance fleet configuration. These task instance fleets are added to the cluster as part of the cluster launch. Each task instance fleet must have a unique name specified so that CloudFormation can differentiate between the task instance fleets. .. epigraph:: You can currently specify only one task instance fleet for a cluster. After creating the cluster, you can only modify the mutable properties of ``InstanceFleetConfig`` , which are ``TargetOnDemandCapacity`` and ``TargetSpotCapacity`` . Modifying any other property results in cluster replacement. > To allow a maximum of 30 Amazon EC2 instance types per fleet, include ``TaskInstanceFleets`` when you create your cluster. If you create your cluster without ``TaskInstanceFleets`` , Amazon EMR uses its default allocation strategy, which allows for a maximum of five Amazon EC2 instance types.
            :param task_instance_groups: Describes the EC2 instances and instance configurations for task instance groups when using clusters with the uniform instance group configuration. These task instance groups are added to the cluster as part of the cluster launch. Each task instance group must have a unique name specified so that CloudFormation can differentiate between the task instance groups. .. epigraph:: After creating the cluster, you can only modify the mutable properties of ``InstanceGroupConfig`` , which are ``AutoScalingPolicy`` and ``InstanceCount`` . Modifying any other property results in cluster replacement.
            :param termination_protected: Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job-flow error.
            :param unhealthy_node_replacement: Indicates whether Amazon EMR should gracefully replace core nodes that have degraded within the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                # configuration_property_: emr.CfnCluster.ConfigurationProperty
                
                job_flow_instances_config_property = emr.CfnCluster.JobFlowInstancesConfigProperty(
                    additional_master_security_groups=["additionalMasterSecurityGroups"],
                    additional_slave_security_groups=["additionalSlaveSecurityGroups"],
                    core_instance_fleet=emr.CfnCluster.InstanceFleetConfigProperty(
                        instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                            instance_type="instanceType",
                
                            # the properties below are optional
                            bid_price="bidPrice",
                            bid_price_as_percentage_of_on_demand_price=123,
                            configurations=[emr.CfnCluster.ConfigurationProperty(
                                classification="classification",
                                configuration_properties={
                                    "configuration_properties_key": "configurationProperties"
                                },
                                configurations=[configuration_property_]
                            )],
                            custom_ami_id="customAmiId",
                            ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                                ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                    volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                        size_in_gb=123,
                                        volume_type="volumeType",
                
                                        # the properties below are optional
                                        iops=123,
                                        throughput=123
                                    ),
                
                                    # the properties below are optional
                                    volumes_per_instance=123
                                )],
                                ebs_optimized=False
                            ),
                            weighted_capacity=123
                        )],
                        launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                            on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                                allocation_strategy="allocationStrategy"
                            ),
                            spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                                timeout_action="timeoutAction",
                                timeout_duration_minutes=123,
                
                                # the properties below are optional
                                allocation_strategy="allocationStrategy",
                                block_duration_minutes=123
                            )
                        ),
                        name="name",
                        target_on_demand_capacity=123,
                        target_spot_capacity=123
                    ),
                    core_instance_group=emr.CfnCluster.InstanceGroupConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                
                        # the properties below are optional
                        auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                            constraints=emr.CfnCluster.ScalingConstraintsProperty(
                                max_capacity=123,
                                min_capacity=123
                            ),
                            rules=[emr.CfnCluster.ScalingRuleProperty(
                                action=emr.CfnCluster.ScalingActionProperty(
                                    simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                        scaling_adjustment=123,
                
                                        # the properties below are optional
                                        adjustment_type="adjustmentType",
                                        cool_down=123
                                    ),
                
                                    # the properties below are optional
                                    market="market"
                                ),
                                name="name",
                                trigger=emr.CfnCluster.ScalingTriggerProperty(
                                    cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                        comparison_operator="comparisonOperator",
                                        metric_name="metricName",
                                        period=123,
                                        threshold=123,
                
                                        # the properties below are optional
                                        dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                            key="key",
                                            value="value"
                                        )],
                                        evaluation_periods=123,
                                        namespace="namespace",
                                        statistic="statistic",
                                        unit="unit"
                                    )
                                ),
                
                                # the properties below are optional
                                description="description"
                            )]
                        ),
                        bid_price="bidPrice",
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
                
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
                
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        market="market",
                        name="name"
                    ),
                    ec2_key_name="ec2KeyName",
                    ec2_subnet_id="ec2SubnetId",
                    ec2_subnet_ids=["ec2SubnetIds"],
                    emr_managed_master_security_group="emrManagedMasterSecurityGroup",
                    emr_managed_slave_security_group="emrManagedSlaveSecurityGroup",
                    hadoop_version="hadoopVersion",
                    keep_job_flow_alive_when_no_steps=False,
                    master_instance_fleet=emr.CfnCluster.InstanceFleetConfigProperty(
                        instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                            instance_type="instanceType",
                
                            # the properties below are optional
                            bid_price="bidPrice",
                            bid_price_as_percentage_of_on_demand_price=123,
                            configurations=[emr.CfnCluster.ConfigurationProperty(
                                classification="classification",
                                configuration_properties={
                                    "configuration_properties_key": "configurationProperties"
                                },
                                configurations=[configuration_property_]
                            )],
                            custom_ami_id="customAmiId",
                            ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                                ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                    volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                        size_in_gb=123,
                                        volume_type="volumeType",
                
                                        # the properties below are optional
                                        iops=123,
                                        throughput=123
                                    ),
                
                                    # the properties below are optional
                                    volumes_per_instance=123
                                )],
                                ebs_optimized=False
                            ),
                            weighted_capacity=123
                        )],
                        launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                            on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                                allocation_strategy="allocationStrategy"
                            ),
                            spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                                timeout_action="timeoutAction",
                                timeout_duration_minutes=123,
                
                                # the properties below are optional
                                allocation_strategy="allocationStrategy",
                                block_duration_minutes=123
                            )
                        ),
                        name="name",
                        target_on_demand_capacity=123,
                        target_spot_capacity=123
                    ),
                    master_instance_group=emr.CfnCluster.InstanceGroupConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                
                        # the properties below are optional
                        auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                            constraints=emr.CfnCluster.ScalingConstraintsProperty(
                                max_capacity=123,
                                min_capacity=123
                            ),
                            rules=[emr.CfnCluster.ScalingRuleProperty(
                                action=emr.CfnCluster.ScalingActionProperty(
                                    simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                        scaling_adjustment=123,
                
                                        # the properties below are optional
                                        adjustment_type="adjustmentType",
                                        cool_down=123
                                    ),
                
                                    # the properties below are optional
                                    market="market"
                                ),
                                name="name",
                                trigger=emr.CfnCluster.ScalingTriggerProperty(
                                    cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                        comparison_operator="comparisonOperator",
                                        metric_name="metricName",
                                        period=123,
                                        threshold=123,
                
                                        # the properties below are optional
                                        dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                            key="key",
                                            value="value"
                                        )],
                                        evaluation_periods=123,
                                        namespace="namespace",
                                        statistic="statistic",
                                        unit="unit"
                                    )
                                ),
                
                                # the properties below are optional
                                description="description"
                            )]
                        ),
                        bid_price="bidPrice",
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
                
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
                
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        market="market",
                        name="name"
                    ),
                    placement=emr.CfnCluster.PlacementTypeProperty(
                        availability_zone="availabilityZone"
                    ),
                    service_access_security_group="serviceAccessSecurityGroup",
                    task_instance_fleets=[emr.CfnCluster.InstanceFleetConfigProperty(
                        instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                            instance_type="instanceType",
                
                            # the properties below are optional
                            bid_price="bidPrice",
                            bid_price_as_percentage_of_on_demand_price=123,
                            configurations=[emr.CfnCluster.ConfigurationProperty(
                                classification="classification",
                                configuration_properties={
                                    "configuration_properties_key": "configurationProperties"
                                },
                                configurations=[configuration_property_]
                            )],
                            custom_ami_id="customAmiId",
                            ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                                ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                    volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                        size_in_gb=123,
                                        volume_type="volumeType",
                
                                        # the properties below are optional
                                        iops=123,
                                        throughput=123
                                    ),
                
                                    # the properties below are optional
                                    volumes_per_instance=123
                                )],
                                ebs_optimized=False
                            ),
                            weighted_capacity=123
                        )],
                        launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                            on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                                allocation_strategy="allocationStrategy"
                            ),
                            spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                                timeout_action="timeoutAction",
                                timeout_duration_minutes=123,
                
                                # the properties below are optional
                                allocation_strategy="allocationStrategy",
                                block_duration_minutes=123
                            )
                        ),
                        name="name",
                        target_on_demand_capacity=123,
                        target_spot_capacity=123
                    )],
                    task_instance_groups=[emr.CfnCluster.InstanceGroupConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                
                        # the properties below are optional
                        auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                            constraints=emr.CfnCluster.ScalingConstraintsProperty(
                                max_capacity=123,
                                min_capacity=123
                            ),
                            rules=[emr.CfnCluster.ScalingRuleProperty(
                                action=emr.CfnCluster.ScalingActionProperty(
                                    simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                        scaling_adjustment=123,
                
                                        # the properties below are optional
                                        adjustment_type="adjustmentType",
                                        cool_down=123
                                    ),
                
                                    # the properties below are optional
                                    market="market"
                                ),
                                name="name",
                                trigger=emr.CfnCluster.ScalingTriggerProperty(
                                    cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                        comparison_operator="comparisonOperator",
                                        metric_name="metricName",
                                        period=123,
                                        threshold=123,
                
                                        # the properties below are optional
                                        dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                            key="key",
                                            value="value"
                                        )],
                                        evaluation_periods=123,
                                        namespace="namespace",
                                        statistic="statistic",
                                        unit="unit"
                                    )
                                ),
                
                                # the properties below are optional
                                description="description"
                            )]
                        ),
                        bid_price="bidPrice",
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
                
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
                
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        market="market",
                        name="name"
                    )],
                    termination_protected=False,
                    unhealthy_node_replacement=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__97053e1923915e0068df7012383808d225b615a5d3590985b1aa4048ba43f0e9)
                check_type(argname="argument additional_master_security_groups", value=additional_master_security_groups, expected_type=type_hints["additional_master_security_groups"])
                check_type(argname="argument additional_slave_security_groups", value=additional_slave_security_groups, expected_type=type_hints["additional_slave_security_groups"])
                check_type(argname="argument core_instance_fleet", value=core_instance_fleet, expected_type=type_hints["core_instance_fleet"])
                check_type(argname="argument core_instance_group", value=core_instance_group, expected_type=type_hints["core_instance_group"])
                check_type(argname="argument ec2_key_name", value=ec2_key_name, expected_type=type_hints["ec2_key_name"])
                check_type(argname="argument ec2_subnet_id", value=ec2_subnet_id, expected_type=type_hints["ec2_subnet_id"])
                check_type(argname="argument ec2_subnet_ids", value=ec2_subnet_ids, expected_type=type_hints["ec2_subnet_ids"])
                check_type(argname="argument emr_managed_master_security_group", value=emr_managed_master_security_group, expected_type=type_hints["emr_managed_master_security_group"])
                check_type(argname="argument emr_managed_slave_security_group", value=emr_managed_slave_security_group, expected_type=type_hints["emr_managed_slave_security_group"])
                check_type(argname="argument hadoop_version", value=hadoop_version, expected_type=type_hints["hadoop_version"])
                check_type(argname="argument keep_job_flow_alive_when_no_steps", value=keep_job_flow_alive_when_no_steps, expected_type=type_hints["keep_job_flow_alive_when_no_steps"])
                check_type(argname="argument master_instance_fleet", value=master_instance_fleet, expected_type=type_hints["master_instance_fleet"])
                check_type(argname="argument master_instance_group", value=master_instance_group, expected_type=type_hints["master_instance_group"])
                check_type(argname="argument placement", value=placement, expected_type=type_hints["placement"])
                check_type(argname="argument service_access_security_group", value=service_access_security_group, expected_type=type_hints["service_access_security_group"])
                check_type(argname="argument task_instance_fleets", value=task_instance_fleets, expected_type=type_hints["task_instance_fleets"])
                check_type(argname="argument task_instance_groups", value=task_instance_groups, expected_type=type_hints["task_instance_groups"])
                check_type(argname="argument termination_protected", value=termination_protected, expected_type=type_hints["termination_protected"])
                check_type(argname="argument unhealthy_node_replacement", value=unhealthy_node_replacement, expected_type=type_hints["unhealthy_node_replacement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if additional_master_security_groups is not None:
                self._values["additional_master_security_groups"] = additional_master_security_groups
            if additional_slave_security_groups is not None:
                self._values["additional_slave_security_groups"] = additional_slave_security_groups
            if core_instance_fleet is not None:
                self._values["core_instance_fleet"] = core_instance_fleet
            if core_instance_group is not None:
                self._values["core_instance_group"] = core_instance_group
            if ec2_key_name is not None:
                self._values["ec2_key_name"] = ec2_key_name
            if ec2_subnet_id is not None:
                self._values["ec2_subnet_id"] = ec2_subnet_id
            if ec2_subnet_ids is not None:
                self._values["ec2_subnet_ids"] = ec2_subnet_ids
            if emr_managed_master_security_group is not None:
                self._values["emr_managed_master_security_group"] = emr_managed_master_security_group
            if emr_managed_slave_security_group is not None:
                self._values["emr_managed_slave_security_group"] = emr_managed_slave_security_group
            if hadoop_version is not None:
                self._values["hadoop_version"] = hadoop_version
            if keep_job_flow_alive_when_no_steps is not None:
                self._values["keep_job_flow_alive_when_no_steps"] = keep_job_flow_alive_when_no_steps
            if master_instance_fleet is not None:
                self._values["master_instance_fleet"] = master_instance_fleet
            if master_instance_group is not None:
                self._values["master_instance_group"] = master_instance_group
            if placement is not None:
                self._values["placement"] = placement
            if service_access_security_group is not None:
                self._values["service_access_security_group"] = service_access_security_group
            if task_instance_fleets is not None:
                self._values["task_instance_fleets"] = task_instance_fleets
            if task_instance_groups is not None:
                self._values["task_instance_groups"] = task_instance_groups
            if termination_protected is not None:
                self._values["termination_protected"] = termination_protected
            if unhealthy_node_replacement is not None:
                self._values["unhealthy_node_replacement"] = unhealthy_node_replacement

        @builtins.property
        def additional_master_security_groups(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of additional Amazon EC2 security group IDs for the master node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-additionalmastersecuritygroups
            '''
            result = self._values.get("additional_master_security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def additional_slave_security_groups(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of additional Amazon EC2 security group IDs for the core and task nodes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-additionalslavesecuritygroups
            '''
            result = self._values.get("additional_slave_security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def core_instance_fleet(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceFleetConfigProperty"]]:
            '''Describes the EC2 instances and instance configurations for the core instance fleet when using clusters with the instance fleet configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-coreinstancefleet
            '''
            result = self._values.get("core_instance_fleet")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceFleetConfigProperty"]], result)

        @builtins.property
        def core_instance_group(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceGroupConfigProperty"]]:
            '''Describes the EC2 instances and instance configurations for core instance groups when using clusters with the uniform instance group configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-coreinstancegroup
            '''
            result = self._values.get("core_instance_group")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceGroupConfigProperty"]], result)

        @builtins.property
        def ec2_key_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon EC2 key pair that can be used to connect to the master node using SSH as the user called "hadoop.".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-ec2keyname
            '''
            result = self._values.get("ec2_key_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ec2_subnet_id(self) -> typing.Optional[builtins.str]:
            '''Applies to clusters that use the uniform instance group configuration.

            To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value and your account supports EC2-Classic, the cluster launches in EC2-Classic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-ec2subnetid
            '''
            result = self._values.get("ec2_subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ec2_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Applies to clusters that use the instance fleet configuration.

            When multiple Amazon EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet.
            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-ec2subnetids
            '''
            result = self._values.get("ec2_subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def emr_managed_master_security_group(self) -> typing.Optional[builtins.str]:
            '''The identifier of the Amazon EC2 security group for the master node.

            If you specify ``EmrManagedMasterSecurityGroup`` , you must also specify ``EmrManagedSlaveSecurityGroup`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-emrmanagedmastersecuritygroup
            '''
            result = self._values.get("emr_managed_master_security_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def emr_managed_slave_security_group(self) -> typing.Optional[builtins.str]:
            '''The identifier of the Amazon EC2 security group for the core and task nodes.

            If you specify ``EmrManagedSlaveSecurityGroup`` , you must also specify ``EmrManagedMasterSecurityGroup`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-emrmanagedslavesecuritygroup
            '''
            result = self._values.get("emr_managed_slave_security_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hadoop_version(self) -> typing.Optional[builtins.str]:
            '''Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop version for the cluster. Valid inputs are "0.18" (no longer maintained), "0.20" (no longer maintained), "0.20.205" (no longer maintained), "1.0.3", "2.2.0", or "2.4.0". If you do not set this value, the default of 0.18 is used, unless the ``AmiVersion`` parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-hadoopversion
            '''
            result = self._values.get("hadoop_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def keep_job_flow_alive_when_no_steps(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the cluster should remain available after completing all steps.

            Defaults to ``false`` . For more information about configuring cluster termination, see `Control Cluster Termination <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html>`_ in the *EMR Management Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-keepjobflowalivewhennosteps
            '''
            result = self._values.get("keep_job_flow_alive_when_no_steps")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def master_instance_fleet(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceFleetConfigProperty"]]:
            '''Describes the EC2 instances and instance configurations for the master instance fleet when using clusters with the instance fleet configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-masterinstancefleet
            '''
            result = self._values.get("master_instance_fleet")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceFleetConfigProperty"]], result)

        @builtins.property
        def master_instance_group(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceGroupConfigProperty"]]:
            '''Describes the EC2 instances and instance configurations for the master instance group when using clusters with the uniform instance group configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-masterinstancegroup
            '''
            result = self._values.get("master_instance_group")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceGroupConfigProperty"]], result)

        @builtins.property
        def placement(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.PlacementTypeProperty"]]:
            '''The Availability Zone in which the cluster runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-placement
            '''
            result = self._values.get("placement")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.PlacementTypeProperty"]], result)

        @builtins.property
        def service_access_security_group(self) -> typing.Optional[builtins.str]:
            '''The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-serviceaccesssecuritygroup
            '''
            result = self._values.get("service_access_security_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def task_instance_fleets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceFleetConfigProperty"]]]]:
            '''Describes the EC2 instances and instance configurations for the task instance fleets when using clusters with the instance fleet configuration.

            These task instance fleets are added to the cluster as part of the cluster launch. Each task instance fleet must have a unique name specified so that CloudFormation can differentiate between the task instance fleets.
            .. epigraph::

               You can currently specify only one task instance fleet for a cluster. After creating the cluster, you can only modify the mutable properties of ``InstanceFleetConfig`` , which are ``TargetOnDemandCapacity`` and ``TargetSpotCapacity`` . Modifying any other property results in cluster replacement. > To allow a maximum of 30 Amazon EC2 instance types per fleet, include ``TaskInstanceFleets`` when you create your cluster. If you create your cluster without ``TaskInstanceFleets`` , Amazon EMR uses its default allocation strategy, which allows for a maximum of five Amazon EC2 instance types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-taskinstancefleets
            '''
            result = self._values.get("task_instance_fleets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceFleetConfigProperty"]]]], result)

        @builtins.property
        def task_instance_groups(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceGroupConfigProperty"]]]]:
            '''Describes the EC2 instances and instance configurations for task instance groups when using clusters with the uniform instance group configuration.

            These task instance groups are added to the cluster as part of the cluster launch. Each task instance group must have a unique name specified so that CloudFormation can differentiate between the task instance groups.
            .. epigraph::

               After creating the cluster, you can only modify the mutable properties of ``InstanceGroupConfig`` , which are ``AutoScalingPolicy`` and ``InstanceCount`` . Modifying any other property results in cluster replacement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-taskinstancegroups
            '''
            result = self._values.get("task_instance_groups")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.InstanceGroupConfigProperty"]]]], result)

        @builtins.property
        def termination_protected(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job-flow error.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-terminationprotected
            '''
            result = self._values.get("termination_protected")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def unhealthy_node_replacement(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether Amazon EMR should gracefully replace core nodes that have degraded within the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-jobflowinstancesconfig.html#cfn-emr-cluster-jobflowinstancesconfig-unhealthynodereplacement
            '''
            result = self._values.get("unhealthy_node_replacement")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobFlowInstancesConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.KerberosAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kdc_admin_password": "kdcAdminPassword",
            "realm": "realm",
            "ad_domain_join_password": "adDomainJoinPassword",
            "ad_domain_join_user": "adDomainJoinUser",
            "cross_realm_trust_principal_password": "crossRealmTrustPrincipalPassword",
        },
    )
    class KerberosAttributesProperty:
        def __init__(
            self,
            *,
            kdc_admin_password: builtins.str,
            realm: builtins.str,
            ad_domain_join_password: typing.Optional[builtins.str] = None,
            ad_domain_join_user: typing.Optional[builtins.str] = None,
            cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``KerberosAttributes`` is a property of the ``AWS::EMR::Cluster`` resource.

            ``KerberosAttributes`` define the cluster-specific Kerberos configuration when Kerberos authentication is enabled using a security configuration. The cluster-specific configuration must be compatible with the security configuration. For more information see `Use Kerberos Authentication <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`_ in the *EMR Management Guide* .

            :param kdc_admin_password: The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster.
            :param realm: The name of the Kerberos realm to which all nodes in a cluster belong. For example, ``EC2.INTERNAL`` .
            :param ad_domain_join_password: The Active Directory password for ``ADDomainJoinUser`` .
            :param ad_domain_join_user: Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain.
            :param cross_realm_trust_principal_password: Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-kerberosattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                kerberos_attributes_property = emr.CfnCluster.KerberosAttributesProperty(
                    kdc_admin_password="kdcAdminPassword",
                    realm="realm",
                
                    # the properties below are optional
                    ad_domain_join_password="adDomainJoinPassword",
                    ad_domain_join_user="adDomainJoinUser",
                    cross_realm_trust_principal_password="crossRealmTrustPrincipalPassword"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__540522543a1aa0db8a729abe18e5fa2372c90f5f9e05e3165a2dd6cd869f3bb0)
                check_type(argname="argument kdc_admin_password", value=kdc_admin_password, expected_type=type_hints["kdc_admin_password"])
                check_type(argname="argument realm", value=realm, expected_type=type_hints["realm"])
                check_type(argname="argument ad_domain_join_password", value=ad_domain_join_password, expected_type=type_hints["ad_domain_join_password"])
                check_type(argname="argument ad_domain_join_user", value=ad_domain_join_user, expected_type=type_hints["ad_domain_join_user"])
                check_type(argname="argument cross_realm_trust_principal_password", value=cross_realm_trust_principal_password, expected_type=type_hints["cross_realm_trust_principal_password"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kdc_admin_password": kdc_admin_password,
                "realm": realm,
            }
            if ad_domain_join_password is not None:
                self._values["ad_domain_join_password"] = ad_domain_join_password
            if ad_domain_join_user is not None:
                self._values["ad_domain_join_user"] = ad_domain_join_user
            if cross_realm_trust_principal_password is not None:
                self._values["cross_realm_trust_principal_password"] = cross_realm_trust_principal_password

        @builtins.property
        def kdc_admin_password(self) -> builtins.str:
            '''The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-kerberosattributes.html#cfn-emr-cluster-kerberosattributes-kdcadminpassword
            '''
            result = self._values.get("kdc_admin_password")
            assert result is not None, "Required property 'kdc_admin_password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def realm(self) -> builtins.str:
            '''The name of the Kerberos realm to which all nodes in a cluster belong.

            For example, ``EC2.INTERNAL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-kerberosattributes.html#cfn-emr-cluster-kerberosattributes-realm
            '''
            result = self._values.get("realm")
            assert result is not None, "Required property 'realm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ad_domain_join_password(self) -> typing.Optional[builtins.str]:
            '''The Active Directory password for ``ADDomainJoinUser`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-kerberosattributes.html#cfn-emr-cluster-kerberosattributes-addomainjoinpassword
            '''
            result = self._values.get("ad_domain_join_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ad_domain_join_user(self) -> typing.Optional[builtins.str]:
            '''Required only when establishing a cross-realm trust with an Active Directory domain.

            A user with sufficient privileges to join resources to the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-kerberosattributes.html#cfn-emr-cluster-kerberosattributes-addomainjoinuser
            '''
            result = self._values.get("ad_domain_join_user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cross_realm_trust_principal_password(self) -> typing.Optional[builtins.str]:
            '''Required only when establishing a cross-realm trust with a KDC in a different realm.

            The cross-realm principal password, which must be identical across realms.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-kerberosattributes.html#cfn-emr-cluster-kerberosattributes-crossrealmtrustprincipalpassword
            '''
            result = self._values.get("cross_realm_trust_principal_password")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KerberosAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.KeyValueProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class KeyValueProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``KeyValue`` is a subproperty of the ``HadoopJarStepConfig`` property type.

            ``KeyValue`` is used to pass parameters to a step.

            :param key: The unique identifier of a key-value pair.
            :param value: The value part of the identified key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-keyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                key_value_property = emr.CfnCluster.KeyValueProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0de77f42d53bb5f752f54244451586c821de421f64b6929630c898540f71641a)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-keyvalue.html#cfn-emr-cluster-keyvalue-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value part of the identified key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-keyvalue.html#cfn-emr-cluster-keyvalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ManagedScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"compute_limits": "computeLimits"},
    )
    class ManagedScalingPolicyProperty:
        def __init__(
            self,
            *,
            compute_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ComputeLimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Managed scaling policy for an Amazon EMR cluster.

            The policy specifies the limits for resources that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

            :param compute_limits: The Amazon EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster is not allowed to go above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-managedscalingpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                managed_scaling_policy_property = emr.CfnCluster.ManagedScalingPolicyProperty(
                    compute_limits=emr.CfnCluster.ComputeLimitsProperty(
                        maximum_capacity_units=123,
                        minimum_capacity_units=123,
                        unit_type="unitType",
                
                        # the properties below are optional
                        maximum_core_capacity_units=123,
                        maximum_on_demand_capacity_units=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0286741b316b450e24ed1eff9bc726fec190a69e54cee78ab3a340bcde86cafe)
                check_type(argname="argument compute_limits", value=compute_limits, expected_type=type_hints["compute_limits"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compute_limits is not None:
                self._values["compute_limits"] = compute_limits

        @builtins.property
        def compute_limits(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ComputeLimitsProperty"]]:
            '''The Amazon EC2 unit limits for a managed scaling policy.

            The managed scaling activity of a cluster is not allowed to go above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-managedscalingpolicy.html#cfn-emr-cluster-managedscalingpolicy-computelimits
            '''
            result = self._values.get("compute_limits")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.ComputeLimitsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManagedScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''``MetricDimension`` is a subproperty of the ``CloudWatchAlarmDefinition`` property type.

            ``MetricDimension`` specifies a CloudWatch dimension, which is specified with a ``Key`` ``Value`` pair. The key is known as a ``Name`` in CloudWatch. By default, Amazon EMR uses one dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID, which is ``${emr.clusterId}`` . This enables the automatic scaling rule for EMR to bootstrap when the cluster ID becomes available during cluster creation.

            :param key: The dimension name.
            :param value: The dimension value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-metricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                metric_dimension_property = emr.CfnCluster.MetricDimensionProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5489079058853fbeec63f1c1e106aede50410429a2d603a5ab90b22e3c39dca)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The dimension name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-metricdimension.html#cfn-emr-cluster-metricdimension-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The dimension value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-metricdimension.html#cfn-emr-cluster-metricdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.OnDemandProvisioningSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"allocation_strategy": "allocationStrategy"},
    )
    class OnDemandProvisioningSpecificationProperty:
        def __init__(self, *, allocation_strategy: builtins.str) -> None:
            '''The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy.

            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.

            :param allocation_strategy: Specifies the strategy to use in launching On-Demand instance fleets. Currently, the only option is ``lowest-price`` (the default), which launches the lowest price first.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-ondemandprovisioningspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                on_demand_provisioning_specification_property = emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                    allocation_strategy="allocationStrategy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a2b2b082993c86b69c150a13684b12a05c6ed2134f215a73050d14afc94e510)
                check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allocation_strategy": allocation_strategy,
            }

        @builtins.property
        def allocation_strategy(self) -> builtins.str:
            '''Specifies the strategy to use in launching On-Demand instance fleets.

            Currently, the only option is ``lowest-price`` (the default), which launches the lowest price first.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-ondemandprovisioningspecification.html#cfn-emr-cluster-ondemandprovisioningspecification-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            assert result is not None, "Required property 'allocation_strategy' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnDemandProvisioningSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.PlacementGroupConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_role": "instanceRole",
            "placement_strategy": "placementStrategy",
        },
    )
    class PlacementGroupConfigProperty:
        def __init__(
            self,
            *,
            instance_role: builtins.str,
            placement_strategy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Placement group configuration for an Amazon EMR cluster.

            The configuration specifies the placement strategy that can be applied to instance roles during cluster creation.

            To use this configuration, consider attaching managed policy AmazonElasticMapReducePlacementGroupPolicy to the Amazon EMR role.

            :param instance_role: Role of the instance in the cluster. Starting with Amazon EMR release 5.23.0, the only supported instance role is ``MASTER`` .
            :param placement_strategy: Amazon EC2 Placement Group strategy associated with instance role. Starting with Amazon EMR release 5.23.0, the only supported placement strategy is ``SPREAD`` for the ``MASTER`` instance role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-placementgroupconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                placement_group_config_property = emr.CfnCluster.PlacementGroupConfigProperty(
                    instance_role="instanceRole",
                
                    # the properties below are optional
                    placement_strategy="placementStrategy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9024d4ca1b091fc3350c52943f87c19e6db412c0ba54cd4b2061955ab335200d)
                check_type(argname="argument instance_role", value=instance_role, expected_type=type_hints["instance_role"])
                check_type(argname="argument placement_strategy", value=placement_strategy, expected_type=type_hints["placement_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_role": instance_role,
            }
            if placement_strategy is not None:
                self._values["placement_strategy"] = placement_strategy

        @builtins.property
        def instance_role(self) -> builtins.str:
            '''Role of the instance in the cluster.

            Starting with Amazon EMR release 5.23.0, the only supported instance role is ``MASTER`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-placementgroupconfig.html#cfn-emr-cluster-placementgroupconfig-instancerole
            '''
            result = self._values.get("instance_role")
            assert result is not None, "Required property 'instance_role' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def placement_strategy(self) -> typing.Optional[builtins.str]:
            '''Amazon EC2 Placement Group strategy associated with instance role.

            Starting with Amazon EMR release 5.23.0, the only supported placement strategy is ``SPREAD`` for the ``MASTER`` instance role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-placementgroupconfig.html#cfn-emr-cluster-placementgroupconfig-placementstrategy
            '''
            result = self._values.get("placement_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementGroupConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.PlacementTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"availability_zone": "availabilityZone"},
    )
    class PlacementTypeProperty:
        def __init__(self, *, availability_zone: builtins.str) -> None:
            '''``PlacementType`` is a property of the ``AWS::EMR::Cluster`` resource.

            ``PlacementType`` determines the Amazon EC2 Availability Zone configuration of the cluster (job flow).

            :param availability_zone: The Amazon EC2 Availability Zone for the cluster. ``AvailabilityZone`` is used for uniform instance groups, while ``AvailabilityZones`` (plural) is used for instance fleets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-placementtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                placement_type_property = emr.CfnCluster.PlacementTypeProperty(
                    availability_zone="availabilityZone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c2a2af5f8dbc7ce16a771e9390fe33448839574f71eaa2acb2f7b7050a1ca0da)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "availability_zone": availability_zone,
            }

        @builtins.property
        def availability_zone(self) -> builtins.str:
            '''The Amazon EC2 Availability Zone for the cluster.

            ``AvailabilityZone`` is used for uniform instance groups, while ``AvailabilityZones`` (plural) is used for instance fleets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-placementtype.html#cfn-emr-cluster-placementtype-availabilityzone
            '''
            result = self._values.get("availability_zone")
            assert result is not None, "Required property 'availability_zone' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ScalingActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "simple_scaling_policy_configuration": "simpleScalingPolicyConfiguration",
            "market": "market",
        },
    )
    class ScalingActionProperty:
        def __init__(
            self,
            *,
            simple_scaling_policy_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.SimpleScalingPolicyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            market: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``ScalingAction`` is a subproperty of the ``ScalingRule`` property type.

            ``ScalingAction`` determines the type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

            :param simple_scaling_policy_configuration: The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.
            :param market: Not available for instance groups. Instance groups use the market type specified for the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                scaling_action_property = emr.CfnCluster.ScalingActionProperty(
                    simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                        scaling_adjustment=123,
                
                        # the properties below are optional
                        adjustment_type="adjustmentType",
                        cool_down=123
                    ),
                
                    # the properties below are optional
                    market="market"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1902e04b59a5603a2ae4aafc06afece2ee3bdbd353692541d87ac7261ae3a892)
                check_type(argname="argument simple_scaling_policy_configuration", value=simple_scaling_policy_configuration, expected_type=type_hints["simple_scaling_policy_configuration"])
                check_type(argname="argument market", value=market, expected_type=type_hints["market"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "simple_scaling_policy_configuration": simple_scaling_policy_configuration,
            }
            if market is not None:
                self._values["market"] = market

        @builtins.property
        def simple_scaling_policy_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.SimpleScalingPolicyConfigurationProperty"]:
            '''The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingaction.html#cfn-emr-cluster-scalingaction-simplescalingpolicyconfiguration
            '''
            result = self._values.get("simple_scaling_policy_configuration")
            assert result is not None, "Required property 'simple_scaling_policy_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.SimpleScalingPolicyConfigurationProperty"], result)

        @builtins.property
        def market(self) -> typing.Optional[builtins.str]:
            '''Not available for instance groups.

            Instance groups use the market type specified for the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingaction.html#cfn-emr-cluster-scalingaction-market
            '''
            result = self._values.get("market")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ScalingConstraintsProperty",
        jsii_struct_bases=[],
        name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
    )
    class ScalingConstraintsProperty:
        def __init__(
            self,
            *,
            max_capacity: jsii.Number,
            min_capacity: jsii.Number,
        ) -> None:
            '''``ScalingConstraints`` is a subproperty of the ``AutoScalingPolicy`` property type.

            ``ScalingConstraints`` defines the upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activities triggered by automatic scaling rules will not cause an instance group to grow above or shrink below these limits.

            :param max_capacity: The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
            :param min_capacity: The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingconstraints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                scaling_constraints_property = emr.CfnCluster.ScalingConstraintsProperty(
                    max_capacity=123,
                    min_capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__218f86c887a6386b3a9f268232cf2402b2c01961c7dc4b1c5c54cd37b45f7f72)
                check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
                check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_capacity": max_capacity,
                "min_capacity": min_capacity,
            }

        @builtins.property
        def max_capacity(self) -> jsii.Number:
            '''The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow.

            Scale-out activities will not add instances beyond this boundary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingconstraints.html#cfn-emr-cluster-scalingconstraints-maxcapacity
            '''
            result = self._values.get("max_capacity")
            assert result is not None, "Required property 'max_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_capacity(self) -> jsii.Number:
            '''The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink.

            Scale-in activities will not terminate instances below this boundary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingconstraints.html#cfn-emr-cluster-scalingconstraints-mincapacity
            '''
            result = self._values.get("min_capacity")
            assert result is not None, "Required property 'min_capacity' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingConstraintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ScalingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "name": "name",
            "trigger": "trigger",
            "description": "description",
        },
    )
    class ScalingRuleProperty:
        def __init__(
            self,
            *,
            action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ScalingActionProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            trigger: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.ScalingTriggerProperty", typing.Dict[builtins.str, typing.Any]]],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``ScalingRule`` is a subproperty of the ``AutoScalingPolicy`` property type.

            ``ScalingRule`` defines the scale-in or scale-out rules for scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

            :param action: The conditions that trigger an automatic scaling activity.
            :param name: The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
            :param trigger: The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
            :param description: A friendly, more verbose description of the automatic scaling rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                scaling_rule_property = emr.CfnCluster.ScalingRuleProperty(
                    action=emr.CfnCluster.ScalingActionProperty(
                        simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                            scaling_adjustment=123,
                
                            # the properties below are optional
                            adjustment_type="adjustmentType",
                            cool_down=123
                        ),
                
                        # the properties below are optional
                        market="market"
                    ),
                    name="name",
                    trigger=emr.CfnCluster.ScalingTriggerProperty(
                        cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                            comparison_operator="comparisonOperator",
                            metric_name="metricName",
                            period=123,
                            threshold=123,
                
                            # the properties below are optional
                            dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                key="key",
                                value="value"
                            )],
                            evaluation_periods=123,
                            namespace="namespace",
                            statistic="statistic",
                            unit="unit"
                        )
                    ),
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0906d3de6d43ea3035952bd939199d7b858dfba3dba2c95200e70324783fce7f)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "name": name,
                "trigger": trigger,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def action(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.ScalingActionProperty"]:
            '''The conditions that trigger an automatic scaling activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingrule.html#cfn-emr-cluster-scalingrule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.ScalingActionProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name used to identify an automatic scaling rule.

            Rule names must be unique within a scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingrule.html#cfn-emr-cluster-scalingrule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def trigger(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.ScalingTriggerProperty"]:
            '''The CloudWatch alarm definition that determines when automatic scaling activity is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingrule.html#cfn-emr-cluster-scalingrule-trigger
            '''
            result = self._values.get("trigger")
            assert result is not None, "Required property 'trigger' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.ScalingTriggerProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A friendly, more verbose description of the automatic scaling rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingrule.html#cfn-emr-cluster-scalingrule-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ScalingTriggerProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_alarm_definition": "cloudWatchAlarmDefinition"},
    )
    class ScalingTriggerProperty:
        def __init__(
            self,
            *,
            cloud_watch_alarm_definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.CloudWatchAlarmDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''``ScalingTrigger`` is a subproperty of the ``ScalingRule`` property type.

            ``ScalingTrigger`` determines the conditions that trigger an automatic scaling activity.

            :param cloud_watch_alarm_definition: The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingtrigger.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                scaling_trigger_property = emr.CfnCluster.ScalingTriggerProperty(
                    cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                        comparison_operator="comparisonOperator",
                        metric_name="metricName",
                        period=123,
                        threshold=123,
                
                        # the properties below are optional
                        dimensions=[emr.CfnCluster.MetricDimensionProperty(
                            key="key",
                            value="value"
                        )],
                        evaluation_periods=123,
                        namespace="namespace",
                        statistic="statistic",
                        unit="unit"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3df2b0de5a8f69682866a7f7b93de987151394068d2650e0ae0ed982b81f2b30)
                check_type(argname="argument cloud_watch_alarm_definition", value=cloud_watch_alarm_definition, expected_type=type_hints["cloud_watch_alarm_definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_alarm_definition": cloud_watch_alarm_definition,
            }

        @builtins.property
        def cloud_watch_alarm_definition(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.CloudWatchAlarmDefinitionProperty"]:
            '''The definition of a CloudWatch metric alarm.

            When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scalingtrigger.html#cfn-emr-cluster-scalingtrigger-cloudwatchalarmdefinition
            '''
            result = self._values.get("cloud_watch_alarm_definition")
            assert result is not None, "Required property 'cloud_watch_alarm_definition' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.CloudWatchAlarmDefinitionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingTriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.ScriptBootstrapActionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path", "args": "args"},
    )
    class ScriptBootstrapActionConfigProperty:
        def __init__(
            self,
            *,
            path: builtins.str,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''``ScriptBootstrapActionConfig`` is a subproperty of the ``BootstrapActionConfig`` property type.

            ``ScriptBootstrapActionConfig`` specifies the arguments and location of the bootstrap script for EMR to run on all cluster nodes before it installs open-source big data applications on them.

            :param path: Location in Amazon S3 of the script to run during a bootstrap action.
            :param args: A list of command line arguments to pass to the bootstrap action script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scriptbootstrapactionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                script_bootstrap_action_config_property = emr.CfnCluster.ScriptBootstrapActionConfigProperty(
                    path="path",
                
                    # the properties below are optional
                    args=["args"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7fa367b9637052cae9251c15612e003865ebda21afaf560950bb477d8b49253c)
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "path": path,
            }
            if args is not None:
                self._values["args"] = args

        @builtins.property
        def path(self) -> builtins.str:
            '''Location in Amazon S3 of the script to run during a bootstrap action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scriptbootstrapactionconfig.html#cfn-emr-cluster-scriptbootstrapactionconfig-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of command line arguments to pass to the bootstrap action script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-scriptbootstrapactionconfig.html#cfn-emr-cluster-scriptbootstrapactionconfig-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScriptBootstrapActionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.SimpleScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scaling_adjustment": "scalingAdjustment",
            "adjustment_type": "adjustmentType",
            "cool_down": "coolDown",
        },
    )
    class SimpleScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            scaling_adjustment: jsii.Number,
            adjustment_type: typing.Optional[builtins.str] = None,
            cool_down: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``SimpleScalingPolicyConfiguration`` is a subproperty of the ``ScalingAction`` property type.

            ``SimpleScalingPolicyConfiguration`` determines how an automatic scaling action adds or removes instances, the cooldown period, and the number of EC2 instances that are added each time the CloudWatch metric alarm condition is satisfied.

            :param scaling_adjustment: The amount by which to scale in or scale out, based on the specified ``AdjustmentType`` . A positive value adds to the instance group's Amazon EC2 instance count while a negative number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the number should only be a positive integer. If ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.
            :param adjustment_type: The way in which Amazon EC2 instances are added (if ``ScalingAdjustment`` is a positive number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default. ``CHANGE_IN_CAPACITY`` indicates that the Amazon EC2 instance count increments or decrements by ``ScalingAdjustment`` , which should be expressed as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by the percentage specified by ``ScalingAdjustment`` , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by ``ScalingAdjustment`` , which should be expressed as a positive integer.
            :param cool_down: The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-simplescalingpolicyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                simple_scaling_policy_configuration_property = emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                    scaling_adjustment=123,
                
                    # the properties below are optional
                    adjustment_type="adjustmentType",
                    cool_down=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4ab5f63d2f26fa03522ac8c3decfe23ac709ffdb5e6d508b478156d95d4e841c)
                check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
                check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
                check_type(argname="argument cool_down", value=cool_down, expected_type=type_hints["cool_down"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "scaling_adjustment": scaling_adjustment,
            }
            if adjustment_type is not None:
                self._values["adjustment_type"] = adjustment_type
            if cool_down is not None:
                self._values["cool_down"] = cool_down

        @builtins.property
        def scaling_adjustment(self) -> jsii.Number:
            '''The amount by which to scale in or scale out, based on the specified ``AdjustmentType`` .

            A positive value adds to the instance group's Amazon EC2 instance count while a negative number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the number should only be a positive integer. If ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-simplescalingpolicyconfiguration.html#cfn-emr-cluster-simplescalingpolicyconfiguration-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            assert result is not None, "Required property 'scaling_adjustment' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def adjustment_type(self) -> typing.Optional[builtins.str]:
            '''The way in which Amazon EC2 instances are added (if ``ScalingAdjustment`` is a positive number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the scaling activity is triggered.

            ``CHANGE_IN_CAPACITY`` is the default. ``CHANGE_IN_CAPACITY`` indicates that the Amazon EC2 instance count increments or decrements by ``ScalingAdjustment`` , which should be expressed as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by the percentage specified by ``ScalingAdjustment`` , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by ``ScalingAdjustment`` , which should be expressed as a positive integer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-simplescalingpolicyconfiguration.html#cfn-emr-cluster-simplescalingpolicyconfiguration-adjustmenttype
            '''
            result = self._values.get("adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cool_down(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start.

            The default value is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-simplescalingpolicyconfiguration.html#cfn-emr-cluster-simplescalingpolicyconfiguration-cooldown
            '''
            result = self._values.get("cool_down")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SimpleScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.SpotProvisioningSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "timeout_action": "timeoutAction",
            "timeout_duration_minutes": "timeoutDurationMinutes",
            "allocation_strategy": "allocationStrategy",
            "block_duration_minutes": "blockDurationMinutes",
        },
    )
    class SpotProvisioningSpecificationProperty:
        def __init__(
            self,
            *,
            timeout_action: builtins.str,
            timeout_duration_minutes: jsii.Number,
            allocation_strategy: typing.Optional[builtins.str] = None,
            block_duration_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``SpotProvisioningSpecification`` is a subproperty of the ``InstanceFleetProvisioningSpecifications`` property type.

            ``SpotProvisioningSpecification`` determines the launch specification for Spot instances in the instance fleet, which includes the defined duration and provisioning timeout behavior.
            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

            :param timeout_action: The action to take when ``TargetSpotCapacity`` has not been fulfilled when the ``TimeoutDurationMinutes`` has expired; that is, when all Spot Instances could not be provisioned within the Spot provisioning timeout. Valid values are ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that if no Spot Instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.
            :param timeout_duration_minutes: The Spot provisioning timeout period in minutes. If Spot Instances are not provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.
            :param allocation_strategy: Specifies one of the following strategies to launch Spot Instance fleets: ``price-capacity-optimized`` , ``capacity-optimized`` , ``lowest-price`` , or ``diversified`` . For more information on the provisioning strategies, see `Allocation strategies for Spot Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html>`_ in the *Amazon EC2 User Guide for Linux Instances* . .. epigraph:: When you launch a Spot Instance fleet with the old console, it automatically launches with the ``capacity-optimized`` strategy. You can't change the allocation strategy from the old console.
            :param block_duration_minutes: The defined duration for Spot Instances (also known as Spot blocks) in minutes. When specified, the Spot Instance does not terminate before the defined duration expires, and defined duration pricing for Spot Instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot Instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates. .. epigraph:: Spot Instances with a defined duration (also known as Spot blocks) are no longer available to new customers from July 1, 2021. For customers who have previously used the feature, we will continue to support Spot Instances with a defined duration until December 31, 2022.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-spotprovisioningspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                spot_provisioning_specification_property = emr.CfnCluster.SpotProvisioningSpecificationProperty(
                    timeout_action="timeoutAction",
                    timeout_duration_minutes=123,
                
                    # the properties below are optional
                    allocation_strategy="allocationStrategy",
                    block_duration_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__208fcd2396b27638e4993cac386f565d58d969b0cecd86940902156a2329b2d9)
                check_type(argname="argument timeout_action", value=timeout_action, expected_type=type_hints["timeout_action"])
                check_type(argname="argument timeout_duration_minutes", value=timeout_duration_minutes, expected_type=type_hints["timeout_duration_minutes"])
                check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
                check_type(argname="argument block_duration_minutes", value=block_duration_minutes, expected_type=type_hints["block_duration_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "timeout_action": timeout_action,
                "timeout_duration_minutes": timeout_duration_minutes,
            }
            if allocation_strategy is not None:
                self._values["allocation_strategy"] = allocation_strategy
            if block_duration_minutes is not None:
                self._values["block_duration_minutes"] = block_duration_minutes

        @builtins.property
        def timeout_action(self) -> builtins.str:
            '''The action to take when ``TargetSpotCapacity`` has not been fulfilled when the ``TimeoutDurationMinutes`` has expired;

            that is, when all Spot Instances could not be provisioned within the Spot provisioning timeout. Valid values are ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that if no Spot Instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-spotprovisioningspecification.html#cfn-emr-cluster-spotprovisioningspecification-timeoutaction
            '''
            result = self._values.get("timeout_action")
            assert result is not None, "Required property 'timeout_action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_duration_minutes(self) -> jsii.Number:
            '''The Spot provisioning timeout period in minutes.

            If Spot Instances are not provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-spotprovisioningspecification.html#cfn-emr-cluster-spotprovisioningspecification-timeoutdurationminutes
            '''
            result = self._values.get("timeout_duration_minutes")
            assert result is not None, "Required property 'timeout_duration_minutes' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def allocation_strategy(self) -> typing.Optional[builtins.str]:
            '''Specifies one of the following strategies to launch Spot Instance fleets: ``price-capacity-optimized`` , ``capacity-optimized`` , ``lowest-price`` , or ``diversified`` .

            For more information on the provisioning strategies, see `Allocation strategies for Spot Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html>`_ in the *Amazon EC2 User Guide for Linux Instances* .
            .. epigraph::

               When you launch a Spot Instance fleet with the old console, it automatically launches with the ``capacity-optimized`` strategy. You can't change the allocation strategy from the old console.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-spotprovisioningspecification.html#cfn-emr-cluster-spotprovisioningspecification-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
            '''The defined duration for Spot Instances (also known as Spot blocks) in minutes.

            When specified, the Spot Instance does not terminate before the defined duration expires, and defined duration pricing for Spot Instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot Instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates.
            .. epigraph::

               Spot Instances with a defined duration (also known as Spot blocks) are no longer available to new customers from July 1, 2021. For customers who have previously used the feature, we will continue to support Spot Instances with a defined duration until December 31, 2022.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-spotprovisioningspecification.html#cfn-emr-cluster-spotprovisioningspecification-blockdurationminutes
            '''
            result = self._values.get("block_duration_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpotProvisioningSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.StepConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hadoop_jar_step": "hadoopJarStep",
            "name": "name",
            "action_on_failure": "actionOnFailure",
        },
    )
    class StepConfigProperty:
        def __init__(
            self,
            *,
            hadoop_jar_step: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.HadoopJarStepConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            action_on_failure: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``StepConfig`` is a property of the ``AWS::EMR::Cluster`` resource.

            The ``StepConfig`` property type specifies a cluster (job flow) step, which runs only on the master node. Steps are used to submit data processing jobs to the cluster.

            :param hadoop_jar_step: The JAR file used for the step.
            :param name: The name of the step.
            :param action_on_failure: The action to take when the cluster step fails. Possible values are ``CANCEL_AND_WAIT`` and ``CONTINUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-stepconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                step_config_property = emr.CfnCluster.StepConfigProperty(
                    hadoop_jar_step=emr.CfnCluster.HadoopJarStepConfigProperty(
                        jar="jar",
                
                        # the properties below are optional
                        args=["args"],
                        main_class="mainClass",
                        step_properties=[emr.CfnCluster.KeyValueProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    name="name",
                
                    # the properties below are optional
                    action_on_failure="actionOnFailure"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d3f0e87741e903ab6e6acc98e6f4de31edf9b395d6ec0ca0e9561069b8e799c7)
                check_type(argname="argument hadoop_jar_step", value=hadoop_jar_step, expected_type=type_hints["hadoop_jar_step"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument action_on_failure", value=action_on_failure, expected_type=type_hints["action_on_failure"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hadoop_jar_step": hadoop_jar_step,
                "name": name,
            }
            if action_on_failure is not None:
                self._values["action_on_failure"] = action_on_failure

        @builtins.property
        def hadoop_jar_step(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.HadoopJarStepConfigProperty"]:
            '''The JAR file used for the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-stepconfig.html#cfn-emr-cluster-stepconfig-hadoopjarstep
            '''
            result = self._values.get("hadoop_jar_step")
            assert result is not None, "Required property 'hadoop_jar_step' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.HadoopJarStepConfigProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-stepconfig.html#cfn-emr-cluster-stepconfig-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def action_on_failure(self) -> typing.Optional[builtins.str]:
            '''The action to take when the cluster step fails.

            Possible values are ``CANCEL_AND_WAIT`` and ``CONTINUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-stepconfig.html#cfn-emr-cluster-stepconfig-actiononfailure
            '''
            result = self._values.get("action_on_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnCluster.VolumeSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "size_in_gb": "sizeInGb",
            "volume_type": "volumeType",
            "iops": "iops",
            "throughput": "throughput",
        },
    )
    class VolumeSpecificationProperty:
        def __init__(
            self,
            *,
            size_in_gb: jsii.Number,
            volume_type: builtins.str,
            iops: typing.Optional[jsii.Number] = None,
            throughput: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``VolumeSpecification`` is a subproperty of the ``EbsBlockDeviceConfig`` property type.

            ``VolumeSecification`` determines the volume type, IOPS, and size (GiB) for EBS volumes attached to EC2 instances.

            :param size_in_gb: The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            :param volume_type: The volume type. Volume types supported are gp3, gp2, io1, st1, sc1, and standard.
            :param iops: The number of I/O operations per second (IOPS) that the volume supports.
            :param throughput: The throughput, in mebibyte per second (MiB/s). This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-volumespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                volume_specification_property = emr.CfnCluster.VolumeSpecificationProperty(
                    size_in_gb=123,
                    volume_type="volumeType",
                
                    # the properties below are optional
                    iops=123,
                    throughput=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c1d9df61da11f931c34aa6af7c0e9bf71cf070f0a0d48100f43043b2adcdbcd5)
                check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "size_in_gb": size_in_gb,
                "volume_type": volume_type,
            }
            if iops is not None:
                self._values["iops"] = iops
            if throughput is not None:
                self._values["throughput"] = throughput

        @builtins.property
        def size_in_gb(self) -> jsii.Number:
            '''The volume size, in gibibytes (GiB).

            This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-volumespecification.html#cfn-emr-cluster-volumespecification-sizeingb
            '''
            result = self._values.get("size_in_gb")
            assert result is not None, "Required property 'size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_type(self) -> builtins.str:
            '''The volume type.

            Volume types supported are gp3, gp2, io1, st1, sc1, and standard.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-volumespecification.html#cfn-emr-cluster-volumespecification-volumetype
            '''
            result = self._values.get("volume_type")
            assert result is not None, "Required property 'volume_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The number of I/O operations per second (IOPS) that the volume supports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-volumespecification.html#cfn-emr-cluster-volumespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''The throughput, in mebibyte per second (MiB/s).

            This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-volumespecification.html#cfn-emr-cluster-volumespecification-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emr.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "instances": "instances",
        "job_flow_role": "jobFlowRole",
        "name": "name",
        "service_role": "serviceRole",
        "additional_info": "additionalInfo",
        "applications": "applications",
        "auto_scaling_role": "autoScalingRole",
        "auto_termination_policy": "autoTerminationPolicy",
        "bootstrap_actions": "bootstrapActions",
        "configurations": "configurations",
        "custom_ami_id": "customAmiId",
        "ebs_root_volume_iops": "ebsRootVolumeIops",
        "ebs_root_volume_size": "ebsRootVolumeSize",
        "ebs_root_volume_throughput": "ebsRootVolumeThroughput",
        "kerberos_attributes": "kerberosAttributes",
        "log_encryption_kms_key_id": "logEncryptionKmsKeyId",
        "log_uri": "logUri",
        "managed_scaling_policy": "managedScalingPolicy",
        "os_release_label": "osReleaseLabel",
        "placement_group_configs": "placementGroupConfigs",
        "release_label": "releaseLabel",
        "scale_down_behavior": "scaleDownBehavior",
        "security_configuration": "securityConfiguration",
        "step_concurrency_level": "stepConcurrencyLevel",
        "steps": "steps",
        "tags": "tags",
        "visible_to_all_users": "visibleToAllUsers",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        instances: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.JobFlowInstancesConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        job_flow_role: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        additional_info: typing.Any = None,
        applications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ApplicationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        auto_scaling_role: typing.Optional[builtins.str] = None,
        auto_termination_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.AutoTerminationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        bootstrap_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.BootstrapActionConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_root_volume_iops: typing.Optional[jsii.Number] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        ebs_root_volume_throughput: typing.Optional[jsii.Number] = None,
        kerberos_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.KerberosAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        managed_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ManagedScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        os_release_label: typing.Optional[builtins.str] = None,
        placement_group_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.PlacementGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        release_label: typing.Optional[builtins.str] = None,
        scale_down_behavior: typing.Optional[builtins.str] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        step_concurrency_level: typing.Optional[jsii.Number] = None,
        steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.StepConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param instances: A specification of the number and type of Amazon EC2 instances.
        :param job_flow_role: Also called instance profile and Amazon EC2 role. An IAM role for an Amazon EMR cluster. The Amazon EC2 instances of the cluster assume this role. The default role is ``EMR_EC2_DefaultRole`` . In order to use the default role, you must have already created it using the AWS CLI or console.
        :param name: The name of the cluster. This parameter can't contain the characters <, >, $, |, or ` (backtick).
        :param service_role: The IAM role that Amazon EMR assumes in order to access AWS resources on your behalf.
        :param additional_info: A JSON string for selecting additional features.
        :param applications: The applications to install on this cluster, for example, Spark, Flink, Oozie, Zeppelin, and so on.
        :param auto_scaling_role: An IAM role for automatic scaling policies. The default role is ``EMR_AutoScaling_DefaultRole`` . The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.
        :param auto_termination_policy: An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see `Control cluster termination <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html>`_
        :param bootstrap_actions: A list of bootstrap actions to run before Hadoop starts on the cluster nodes.
        :param configurations: Applies only to Amazon EMR releases 4.x and later. The list of configurations that are supplied to the Amazon EMR cluster.
        :param custom_ami_id: Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.
        :param ebs_root_volume_iops: The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.
        :param ebs_root_volume_size: The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.
        :param ebs_root_volume_throughput: The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.
        :param kerberos_attributes: Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see `Use Kerberos Authentication <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`_ in the *Amazon EMR Management Guide* .
        :param log_encryption_kms_key_id: The AWS KMS key used for encrypting log files. This attribute is only available with Amazon EMR 5.30.0 and later, excluding Amazon EMR 6.0.0.
        :param log_uri: The path to the Amazon S3 location where logs for this cluster are stored.
        :param managed_scaling_policy: Creates or updates a managed scaling policy for an Amazon EMR cluster. The managed scaling policy defines the limits for resources, such as Amazon EC2 instances that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
        :param os_release_label: The Amazon Linux release specified in a cluster launch RunJobFlow request. If no Amazon Linux release was specified, the default Amazon Linux release is shown in the response.
        :param placement_group_configs: 
        :param release_label: The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form ``emr-x.x.x`` , where x.x.x is an Amazon EMR release version such as ``emr-5.14.0`` . For more information about Amazon EMR release versions and included application versions and features, see ` <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/>`_ . The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use ``AmiVersion`` .
        :param scale_down_behavior: The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. ``TERMINATE_AT_INSTANCE_HOUR`` indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. ``TERMINATE_AT_TASK_COMPLETION`` indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. ``TERMINATE_AT_TASK_COMPLETION`` is available only in Amazon EMR releases 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.
        :param security_configuration: The name of the security configuration applied to the cluster.
        :param step_concurrency_level: Specifies the number of steps that can be executed concurrently. The default value is ``1`` . The maximum value is ``256`` .
        :param steps: A list of steps to run.
        :param tags: A list of tags associated with a cluster.
        :param visible_to_all_users: Indicates whether the cluster is visible to all IAM users of the AWS account associated with the cluster. If this value is set to ``true`` , all IAM users of that AWS account can view and manage the cluster if they have the proper policy permissions set. If this value is ``false`` , only the IAM user that created the cluster can view and manage it. This value can be changed using the SetVisibleToAllUsers action. .. epigraph:: When you create clusters directly through the EMR console or API, this value is set to ``true`` by default. However, for ``AWS::EMR::Cluster`` resources in CloudFormation, the default is ``false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emr as emr
            
            # additional_info: Any
            # configuration_property_: emr.CfnCluster.ConfigurationProperty
            
            cfn_cluster_props = emr.CfnClusterProps(
                instances=emr.CfnCluster.JobFlowInstancesConfigProperty(
                    additional_master_security_groups=["additionalMasterSecurityGroups"],
                    additional_slave_security_groups=["additionalSlaveSecurityGroups"],
                    core_instance_fleet=emr.CfnCluster.InstanceFleetConfigProperty(
                        instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                            instance_type="instanceType",
            
                            # the properties below are optional
                            bid_price="bidPrice",
                            bid_price_as_percentage_of_on_demand_price=123,
                            configurations=[emr.CfnCluster.ConfigurationProperty(
                                classification="classification",
                                configuration_properties={
                                    "configuration_properties_key": "configurationProperties"
                                },
                                configurations=[configuration_property_]
                            )],
                            custom_ami_id="customAmiId",
                            ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                                ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                    volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                        size_in_gb=123,
                                        volume_type="volumeType",
            
                                        # the properties below are optional
                                        iops=123,
                                        throughput=123
                                    ),
            
                                    # the properties below are optional
                                    volumes_per_instance=123
                                )],
                                ebs_optimized=False
                            ),
                            weighted_capacity=123
                        )],
                        launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                            on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                                allocation_strategy="allocationStrategy"
                            ),
                            spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                                timeout_action="timeoutAction",
                                timeout_duration_minutes=123,
            
                                # the properties below are optional
                                allocation_strategy="allocationStrategy",
                                block_duration_minutes=123
                            )
                        ),
                        name="name",
                        target_on_demand_capacity=123,
                        target_spot_capacity=123
                    ),
                    core_instance_group=emr.CfnCluster.InstanceGroupConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
            
                        # the properties below are optional
                        auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                            constraints=emr.CfnCluster.ScalingConstraintsProperty(
                                max_capacity=123,
                                min_capacity=123
                            ),
                            rules=[emr.CfnCluster.ScalingRuleProperty(
                                action=emr.CfnCluster.ScalingActionProperty(
                                    simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                        scaling_adjustment=123,
            
                                        # the properties below are optional
                                        adjustment_type="adjustmentType",
                                        cool_down=123
                                    ),
            
                                    # the properties below are optional
                                    market="market"
                                ),
                                name="name",
                                trigger=emr.CfnCluster.ScalingTriggerProperty(
                                    cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                        comparison_operator="comparisonOperator",
                                        metric_name="metricName",
                                        period=123,
                                        threshold=123,
            
                                        # the properties below are optional
                                        dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                            key="key",
                                            value="value"
                                        )],
                                        evaluation_periods=123,
                                        namespace="namespace",
                                        statistic="statistic",
                                        unit="unit"
                                    )
                                ),
            
                                # the properties below are optional
                                description="description"
                            )]
                        ),
                        bid_price="bidPrice",
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
            
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
            
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        market="market",
                        name="name"
                    ),
                    ec2_key_name="ec2KeyName",
                    ec2_subnet_id="ec2SubnetId",
                    ec2_subnet_ids=["ec2SubnetIds"],
                    emr_managed_master_security_group="emrManagedMasterSecurityGroup",
                    emr_managed_slave_security_group="emrManagedSlaveSecurityGroup",
                    hadoop_version="hadoopVersion",
                    keep_job_flow_alive_when_no_steps=False,
                    master_instance_fleet=emr.CfnCluster.InstanceFleetConfigProperty(
                        instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                            instance_type="instanceType",
            
                            # the properties below are optional
                            bid_price="bidPrice",
                            bid_price_as_percentage_of_on_demand_price=123,
                            configurations=[emr.CfnCluster.ConfigurationProperty(
                                classification="classification",
                                configuration_properties={
                                    "configuration_properties_key": "configurationProperties"
                                },
                                configurations=[configuration_property_]
                            )],
                            custom_ami_id="customAmiId",
                            ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                                ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                    volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                        size_in_gb=123,
                                        volume_type="volumeType",
            
                                        # the properties below are optional
                                        iops=123,
                                        throughput=123
                                    ),
            
                                    # the properties below are optional
                                    volumes_per_instance=123
                                )],
                                ebs_optimized=False
                            ),
                            weighted_capacity=123
                        )],
                        launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                            on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                                allocation_strategy="allocationStrategy"
                            ),
                            spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                                timeout_action="timeoutAction",
                                timeout_duration_minutes=123,
            
                                # the properties below are optional
                                allocation_strategy="allocationStrategy",
                                block_duration_minutes=123
                            )
                        ),
                        name="name",
                        target_on_demand_capacity=123,
                        target_spot_capacity=123
                    ),
                    master_instance_group=emr.CfnCluster.InstanceGroupConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
            
                        # the properties below are optional
                        auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                            constraints=emr.CfnCluster.ScalingConstraintsProperty(
                                max_capacity=123,
                                min_capacity=123
                            ),
                            rules=[emr.CfnCluster.ScalingRuleProperty(
                                action=emr.CfnCluster.ScalingActionProperty(
                                    simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                        scaling_adjustment=123,
            
                                        # the properties below are optional
                                        adjustment_type="adjustmentType",
                                        cool_down=123
                                    ),
            
                                    # the properties below are optional
                                    market="market"
                                ),
                                name="name",
                                trigger=emr.CfnCluster.ScalingTriggerProperty(
                                    cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                        comparison_operator="comparisonOperator",
                                        metric_name="metricName",
                                        period=123,
                                        threshold=123,
            
                                        # the properties below are optional
                                        dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                            key="key",
                                            value="value"
                                        )],
                                        evaluation_periods=123,
                                        namespace="namespace",
                                        statistic="statistic",
                                        unit="unit"
                                    )
                                ),
            
                                # the properties below are optional
                                description="description"
                            )]
                        ),
                        bid_price="bidPrice",
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
            
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
            
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        market="market",
                        name="name"
                    ),
                    placement=emr.CfnCluster.PlacementTypeProperty(
                        availability_zone="availabilityZone"
                    ),
                    service_access_security_group="serviceAccessSecurityGroup",
                    task_instance_fleets=[emr.CfnCluster.InstanceFleetConfigProperty(
                        instance_type_configs=[emr.CfnCluster.InstanceTypeConfigProperty(
                            instance_type="instanceType",
            
                            # the properties below are optional
                            bid_price="bidPrice",
                            bid_price_as_percentage_of_on_demand_price=123,
                            configurations=[emr.CfnCluster.ConfigurationProperty(
                                classification="classification",
                                configuration_properties={
                                    "configuration_properties_key": "configurationProperties"
                                },
                                configurations=[configuration_property_]
                            )],
                            custom_ami_id="customAmiId",
                            ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                                ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                    volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                        size_in_gb=123,
                                        volume_type="volumeType",
            
                                        # the properties below are optional
                                        iops=123,
                                        throughput=123
                                    ),
            
                                    # the properties below are optional
                                    volumes_per_instance=123
                                )],
                                ebs_optimized=False
                            ),
                            weighted_capacity=123
                        )],
                        launch_specifications=emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty(
                            on_demand_specification=emr.CfnCluster.OnDemandProvisioningSpecificationProperty(
                                allocation_strategy="allocationStrategy"
                            ),
                            spot_specification=emr.CfnCluster.SpotProvisioningSpecificationProperty(
                                timeout_action="timeoutAction",
                                timeout_duration_minutes=123,
            
                                # the properties below are optional
                                allocation_strategy="allocationStrategy",
                                block_duration_minutes=123
                            )
                        ),
                        name="name",
                        target_on_demand_capacity=123,
                        target_spot_capacity=123
                    )],
                    task_instance_groups=[emr.CfnCluster.InstanceGroupConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
            
                        # the properties below are optional
                        auto_scaling_policy=emr.CfnCluster.AutoScalingPolicyProperty(
                            constraints=emr.CfnCluster.ScalingConstraintsProperty(
                                max_capacity=123,
                                min_capacity=123
                            ),
                            rules=[emr.CfnCluster.ScalingRuleProperty(
                                action=emr.CfnCluster.ScalingActionProperty(
                                    simple_scaling_policy_configuration=emr.CfnCluster.SimpleScalingPolicyConfigurationProperty(
                                        scaling_adjustment=123,
            
                                        # the properties below are optional
                                        adjustment_type="adjustmentType",
                                        cool_down=123
                                    ),
            
                                    # the properties below are optional
                                    market="market"
                                ),
                                name="name",
                                trigger=emr.CfnCluster.ScalingTriggerProperty(
                                    cloud_watch_alarm_definition=emr.CfnCluster.CloudWatchAlarmDefinitionProperty(
                                        comparison_operator="comparisonOperator",
                                        metric_name="metricName",
                                        period=123,
                                        threshold=123,
            
                                        # the properties below are optional
                                        dimensions=[emr.CfnCluster.MetricDimensionProperty(
                                            key="key",
                                            value="value"
                                        )],
                                        evaluation_periods=123,
                                        namespace="namespace",
                                        statistic="statistic",
                                        unit="unit"
                                    )
                                ),
            
                                # the properties below are optional
                                description="description"
                            )]
                        ),
                        bid_price="bidPrice",
                        configurations=[emr.CfnCluster.ConfigurationProperty(
                            classification="classification",
                            configuration_properties={
                                "configuration_properties_key": "configurationProperties"
                            },
                            configurations=[configuration_property_]
                        )],
                        custom_ami_id="customAmiId",
                        ebs_configuration=emr.CfnCluster.EbsConfigurationProperty(
                            ebs_block_device_configs=[emr.CfnCluster.EbsBlockDeviceConfigProperty(
                                volume_specification=emr.CfnCluster.VolumeSpecificationProperty(
                                    size_in_gb=123,
                                    volume_type="volumeType",
            
                                    # the properties below are optional
                                    iops=123,
                                    throughput=123
                                ),
            
                                # the properties below are optional
                                volumes_per_instance=123
                            )],
                            ebs_optimized=False
                        ),
                        market="market",
                        name="name"
                    )],
                    termination_protected=False,
                    unhealthy_node_replacement=False
                ),
                job_flow_role="jobFlowRole",
                name="name",
                service_role="serviceRole",
            
                # the properties below are optional
                additional_info=additional_info,
                applications=[emr.CfnCluster.ApplicationProperty(
                    additional_info={
                        "additional_info_key": "additionalInfo"
                    },
                    args=["args"],
                    name="name",
                    version="version"
                )],
                auto_scaling_role="autoScalingRole",
                auto_termination_policy=emr.CfnCluster.AutoTerminationPolicyProperty(
                    idle_timeout=123
                ),
                bootstrap_actions=[emr.CfnCluster.BootstrapActionConfigProperty(
                    name="name",
                    script_bootstrap_action=emr.CfnCluster.ScriptBootstrapActionConfigProperty(
                        path="path",
            
                        # the properties below are optional
                        args=["args"]
                    )
                )],
                configurations=[emr.CfnCluster.ConfigurationProperty(
                    classification="classification",
                    configuration_properties={
                        "configuration_properties_key": "configurationProperties"
                    },
                    configurations=[configuration_property_]
                )],
                custom_ami_id="customAmiId",
                ebs_root_volume_iops=123,
                ebs_root_volume_size=123,
                ebs_root_volume_throughput=123,
                kerberos_attributes=emr.CfnCluster.KerberosAttributesProperty(
                    kdc_admin_password="kdcAdminPassword",
                    realm="realm",
            
                    # the properties below are optional
                    ad_domain_join_password="adDomainJoinPassword",
                    ad_domain_join_user="adDomainJoinUser",
                    cross_realm_trust_principal_password="crossRealmTrustPrincipalPassword"
                ),
                log_encryption_kms_key_id="logEncryptionKmsKeyId",
                log_uri="logUri",
                managed_scaling_policy=emr.CfnCluster.ManagedScalingPolicyProperty(
                    compute_limits=emr.CfnCluster.ComputeLimitsProperty(
                        maximum_capacity_units=123,
                        minimum_capacity_units=123,
                        unit_type="unitType",
            
                        # the properties below are optional
                        maximum_core_capacity_units=123,
                        maximum_on_demand_capacity_units=123
                    )
                ),
                os_release_label="osReleaseLabel",
                placement_group_configs=[emr.CfnCluster.PlacementGroupConfigProperty(
                    instance_role="instanceRole",
            
                    # the properties below are optional
                    placement_strategy="placementStrategy"
                )],
                release_label="releaseLabel",
                scale_down_behavior="scaleDownBehavior",
                security_configuration="securityConfiguration",
                step_concurrency_level=123,
                steps=[emr.CfnCluster.StepConfigProperty(
                    hadoop_jar_step=emr.CfnCluster.HadoopJarStepConfigProperty(
                        jar="jar",
            
                        # the properties below are optional
                        args=["args"],
                        main_class="mainClass",
                        step_properties=[emr.CfnCluster.KeyValueProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    name="name",
            
                    # the properties below are optional
                    action_on_failure="actionOnFailure"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                visible_to_all_users=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25985ea8bea73f3b566e4cc44a54f891c8c64b46cf5c4fb0ac288983cd463f2f)
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument job_flow_role", value=job_flow_role, expected_type=type_hints["job_flow_role"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument additional_info", value=additional_info, expected_type=type_hints["additional_info"])
            check_type(argname="argument applications", value=applications, expected_type=type_hints["applications"])
            check_type(argname="argument auto_scaling_role", value=auto_scaling_role, expected_type=type_hints["auto_scaling_role"])
            check_type(argname="argument auto_termination_policy", value=auto_termination_policy, expected_type=type_hints["auto_termination_policy"])
            check_type(argname="argument bootstrap_actions", value=bootstrap_actions, expected_type=type_hints["bootstrap_actions"])
            check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            check_type(argname="argument custom_ami_id", value=custom_ami_id, expected_type=type_hints["custom_ami_id"])
            check_type(argname="argument ebs_root_volume_iops", value=ebs_root_volume_iops, expected_type=type_hints["ebs_root_volume_iops"])
            check_type(argname="argument ebs_root_volume_size", value=ebs_root_volume_size, expected_type=type_hints["ebs_root_volume_size"])
            check_type(argname="argument ebs_root_volume_throughput", value=ebs_root_volume_throughput, expected_type=type_hints["ebs_root_volume_throughput"])
            check_type(argname="argument kerberos_attributes", value=kerberos_attributes, expected_type=type_hints["kerberos_attributes"])
            check_type(argname="argument log_encryption_kms_key_id", value=log_encryption_kms_key_id, expected_type=type_hints["log_encryption_kms_key_id"])
            check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            check_type(argname="argument managed_scaling_policy", value=managed_scaling_policy, expected_type=type_hints["managed_scaling_policy"])
            check_type(argname="argument os_release_label", value=os_release_label, expected_type=type_hints["os_release_label"])
            check_type(argname="argument placement_group_configs", value=placement_group_configs, expected_type=type_hints["placement_group_configs"])
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument scale_down_behavior", value=scale_down_behavior, expected_type=type_hints["scale_down_behavior"])
            check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
            check_type(argname="argument step_concurrency_level", value=step_concurrency_level, expected_type=type_hints["step_concurrency_level"])
            check_type(argname="argument steps", value=steps, expected_type=type_hints["steps"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument visible_to_all_users", value=visible_to_all_users, expected_type=type_hints["visible_to_all_users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instances": instances,
            "job_flow_role": job_flow_role,
            "name": name,
            "service_role": service_role,
        }
        if additional_info is not None:
            self._values["additional_info"] = additional_info
        if applications is not None:
            self._values["applications"] = applications
        if auto_scaling_role is not None:
            self._values["auto_scaling_role"] = auto_scaling_role
        if auto_termination_policy is not None:
            self._values["auto_termination_policy"] = auto_termination_policy
        if bootstrap_actions is not None:
            self._values["bootstrap_actions"] = bootstrap_actions
        if configurations is not None:
            self._values["configurations"] = configurations
        if custom_ami_id is not None:
            self._values["custom_ami_id"] = custom_ami_id
        if ebs_root_volume_iops is not None:
            self._values["ebs_root_volume_iops"] = ebs_root_volume_iops
        if ebs_root_volume_size is not None:
            self._values["ebs_root_volume_size"] = ebs_root_volume_size
        if ebs_root_volume_throughput is not None:
            self._values["ebs_root_volume_throughput"] = ebs_root_volume_throughput
        if kerberos_attributes is not None:
            self._values["kerberos_attributes"] = kerberos_attributes
        if log_encryption_kms_key_id is not None:
            self._values["log_encryption_kms_key_id"] = log_encryption_kms_key_id
        if log_uri is not None:
            self._values["log_uri"] = log_uri
        if managed_scaling_policy is not None:
            self._values["managed_scaling_policy"] = managed_scaling_policy
        if os_release_label is not None:
            self._values["os_release_label"] = os_release_label
        if placement_group_configs is not None:
            self._values["placement_group_configs"] = placement_group_configs
        if release_label is not None:
            self._values["release_label"] = release_label
        if scale_down_behavior is not None:
            self._values["scale_down_behavior"] = scale_down_behavior
        if security_configuration is not None:
            self._values["security_configuration"] = security_configuration
        if step_concurrency_level is not None:
            self._values["step_concurrency_level"] = step_concurrency_level
        if steps is not None:
            self._values["steps"] = steps
        if tags is not None:
            self._values["tags"] = tags
        if visible_to_all_users is not None:
            self._values["visible_to_all_users"] = visible_to_all_users

    @builtins.property
    def instances(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCluster.JobFlowInstancesConfigProperty]:
        '''A specification of the number and type of Amazon EC2 instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-instances
        '''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCluster.JobFlowInstancesConfigProperty], result)

    @builtins.property
    def job_flow_role(self) -> builtins.str:
        '''Also called instance profile and Amazon EC2 role.

        An IAM role for an Amazon EMR cluster. The Amazon EC2 instances of the cluster assume this role. The default role is ``EMR_EC2_DefaultRole`` . In order to use the default role, you must have already created it using the AWS CLI or console.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-jobflowrole
        '''
        result = self._values.get("job_flow_role")
        assert result is not None, "Required property 'job_flow_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the cluster.

        This parameter can't contain the characters <, >, $, |, or ` (backtick).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''The IAM role that Amazon EMR assumes in order to access AWS resources on your behalf.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-servicerole
        '''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_info(self) -> typing.Any:
        '''A JSON string for selecting additional features.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-additionalinfo
        '''
        result = self._values.get("additional_info")
        return typing.cast(typing.Any, result)

    @builtins.property
    def applications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.ApplicationProperty]]]]:
        '''The applications to install on this cluster, for example, Spark, Flink, Oozie, Zeppelin, and so on.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-applications
        '''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.ApplicationProperty]]]], result)

    @builtins.property
    def auto_scaling_role(self) -> typing.Optional[builtins.str]:
        '''An IAM role for automatic scaling policies.

        The default role is ``EMR_AutoScaling_DefaultRole`` . The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-autoscalingrole
        '''
        result = self._values.get("auto_scaling_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_termination_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.AutoTerminationPolicyProperty]]:
        '''An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates.

        For alternative cluster termination options, see `Control cluster termination <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-autoterminationpolicy
        '''
        result = self._values.get("auto_termination_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.AutoTerminationPolicyProperty]], result)

    @builtins.property
    def bootstrap_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.BootstrapActionConfigProperty]]]]:
        '''A list of bootstrap actions to run before Hadoop starts on the cluster nodes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-bootstrapactions
        '''
        result = self._values.get("bootstrap_actions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.BootstrapActionConfigProperty]]]], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.ConfigurationProperty]]]]:
        '''Applies only to Amazon EMR releases 4.x and later. The list of configurations that are supplied to the Amazon EMR cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-configurations
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.ConfigurationProperty]]]], result)

    @builtins.property
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-customamiid
        '''
        result = self._values.get("custom_ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_root_volume_iops(self) -> typing.Optional[jsii.Number]:
        '''The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance.

        Available in Amazon EMR releases 6.15.0 and later.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-ebsrootvolumeiops
        '''
        result = self._values.get("ebs_root_volume_iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_root_volume_size(self) -> typing.Optional[jsii.Number]:
        '''The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance.

        Available in Amazon EMR releases 4.x and later.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-ebsrootvolumesize
        '''
        result = self._values.get("ebs_root_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_root_volume_throughput(self) -> typing.Optional[jsii.Number]:
        '''The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance.

        Available in Amazon EMR releases 6.15.0 and later.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-ebsrootvolumethroughput
        '''
        result = self._values.get("ebs_root_volume_throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kerberos_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.KerberosAttributesProperty]]:
        '''Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration.

        For more information see `Use Kerberos Authentication <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`_ in the *Amazon EMR Management Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-kerberosattributes
        '''
        result = self._values.get("kerberos_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.KerberosAttributesProperty]], result)

    @builtins.property
    def log_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key used for encrypting log files.

        This attribute is only available with Amazon EMR 5.30.0 and later, excluding Amazon EMR 6.0.0.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-logencryptionkmskeyid
        '''
        result = self._values.get("log_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''The path to the Amazon S3 location where logs for this cluster are stored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-loguri
        '''
        result = self._values.get("log_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ManagedScalingPolicyProperty]]:
        '''Creates or updates a managed scaling policy for an Amazon EMR cluster.

        The managed scaling policy defines the limits for resources, such as Amazon EC2 instances that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-managedscalingpolicy
        '''
        result = self._values.get("managed_scaling_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ManagedScalingPolicyProperty]], result)

    @builtins.property
    def os_release_label(self) -> typing.Optional[builtins.str]:
        '''The Amazon Linux release specified in a cluster launch RunJobFlow request.

        If no Amazon Linux release was specified, the default Amazon Linux release is shown in the response.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-osreleaselabel
        '''
        result = self._values.get("os_release_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_group_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.PlacementGroupConfigProperty]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-placementgroupconfigs
        '''
        result = self._values.get("placement_group_configs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.PlacementGroupConfigProperty]]]], result)

    @builtins.property
    def release_label(self) -> typing.Optional[builtins.str]:
        '''The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster.

        Release labels are in the form ``emr-x.x.x`` , where x.x.x is an Amazon EMR release version such as ``emr-5.14.0`` . For more information about Amazon EMR release versions and included application versions and features, see ` <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/>`_ . The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use ``AmiVersion`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-releaselabel
        '''
        result = self._values.get("release_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_behavior(self) -> typing.Optional[builtins.str]:
        '''The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized.

        ``TERMINATE_AT_INSTANCE_HOUR`` indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. ``TERMINATE_AT_TASK_COMPLETION`` indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. ``TERMINATE_AT_TASK_COMPLETION`` is available only in Amazon EMR releases 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-scaledownbehavior
        '''
        result = self._values.get("scale_down_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration applied to the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-securityconfiguration
        '''
        result = self._values.get("security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def step_concurrency_level(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of steps that can be executed concurrently.

        The default value is ``1`` . The maximum value is ``256`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-stepconcurrencylevel
        '''
        result = self._values.get("step_concurrency_level")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def steps(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.StepConfigProperty]]]]:
        '''A list of steps to run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-steps
        '''
        result = self._values.get("steps")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.StepConfigProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags associated with a cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def visible_to_all_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the cluster is visible to all IAM users of the AWS account associated with the cluster.

        If this value is set to ``true`` , all IAM users of that AWS account can view and manage the cluster if they have the proper policy permissions set. If this value is ``false`` , only the IAM user that created the cluster can view and manage it. This value can be changed using the SetVisibleToAllUsers action.
        .. epigraph::

           When you create clusters directly through the EMR console or API, this value is set to ``true`` by default. However, for ``AWS::EMR::Cluster`` resources in CloudFormation, the default is ``false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html#cfn-emr-cluster-visibletoallusers
        '''
        result = self._values.get("visible_to_all_users")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnInstanceFleetConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig",
):
    '''Use ``InstanceFleetConfig`` to define instance fleets for an EMR cluster.

    A cluster can not use both instance fleets and instance groups. For more information, see `Configure Instance Fleets <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-instance-group-configuration.html>`_ in the *Amazon EMR Management Guide* .
    .. epigraph::

       The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions. > You can currently only add a task instance fleet to a cluster with this resource. If you use this resource, CloudFormation waits for the cluster launch to complete before adding the task instance fleet to the cluster. In order to add a task instance fleet to the cluster as part of the cluster launch and minimize delays in provisioning task nodes, use the ``TaskInstanceFleets`` subproperty for the `AWS::EMR::Cluster JobFlowInstancesConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html>`_ property instead. To use this subproperty, see `AWS::EMR::Cluster <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html>`_ for examples.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html
    :cloudformationResource: AWS::EMR::InstanceFleetConfig
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emr as emr
        
        # configuration_property_: emr.CfnInstanceFleetConfig.ConfigurationProperty
        
        cfn_instance_fleet_config = emr.CfnInstanceFleetConfig(self, "MyCfnInstanceFleetConfig",
            cluster_id="clusterId",
            instance_fleet_type="instanceFleetType",
        
            # the properties below are optional
            instance_type_configs=[emr.CfnInstanceFleetConfig.InstanceTypeConfigProperty(
                instance_type="instanceType",
        
                # the properties below are optional
                bid_price="bidPrice",
                bid_price_as_percentage_of_on_demand_price=123,
                configurations=[emr.CfnInstanceFleetConfig.ConfigurationProperty(
                    classification="classification",
                    configuration_properties={
                        "configuration_properties_key": "configurationProperties"
                    },
                    configurations=[configuration_property_]
                )],
                custom_ami_id="customAmiId",
                ebs_configuration=emr.CfnInstanceFleetConfig.EbsConfigurationProperty(
                    ebs_block_device_configs=[emr.CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty(
                        volume_specification=emr.CfnInstanceFleetConfig.VolumeSpecificationProperty(
                            size_in_gb=123,
                            volume_type="volumeType",
        
                            # the properties below are optional
                            iops=123,
                            throughput=123
                        ),
        
                        # the properties below are optional
                        volumes_per_instance=123
                    )],
                    ebs_optimized=False
                ),
                weighted_capacity=123
            )],
            launch_specifications=emr.CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty(
                on_demand_specification=emr.CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty(
                    allocation_strategy="allocationStrategy"
                ),
                spot_specification=emr.CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty(
                    timeout_action="timeoutAction",
                    timeout_duration_minutes=123,
        
                    # the properties below are optional
                    allocation_strategy="allocationStrategy",
                    block_duration_minutes=123
                )
            ),
            name="name",
            target_on_demand_capacity=123,
            target_spot_capacity=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_id: builtins.str,
        instance_fleet_type: builtins.str,
        instance_type_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.InstanceTypeConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        launch_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_id: The unique identifier of the EMR cluster.
        :param instance_fleet_type: The node type that the instance fleet hosts. *Allowed Values* : TASK
        :param instance_type_configs: ``InstanceTypeConfigs`` determine the EC2 instances that Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities. .. epigraph:: The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
        :param launch_specifications: The launch specification for the instance fleet.
        :param name: The friendly name of the instance fleet.
        :param target_on_demand_capacity: The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. .. epigraph:: If not specified or set to 0, only Spot instances are provisioned for the instance fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.
        :param target_spot_capacity: The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When a Spot instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. .. epigraph:: If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25473c0968868f7cb7ae13c5d07084fdff34429497e0ea823b7527eea6ce494f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceFleetConfigProps(
            cluster_id=cluster_id,
            instance_fleet_type=instance_fleet_type,
            instance_type_configs=instance_type_configs,
            launch_specifications=launch_specifications,
            name=name,
            target_on_demand_capacity=target_on_demand_capacity,
            target_spot_capacity=target_spot_capacity,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1ed3f5cbfeb698332e274bbe7785722e739d9dec509f54283e0495cf8900e71)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e98716d54c69df2f9bc4a900903b8690bf3dbe75423a21ead9ce4d36cbd0443f)
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
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        '''The unique identifier of the EMR cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__400bee2e9ad25af5bc5503b31db6f8c647cc75941195dd29846c6d2ff917cf27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceFleetType")
    def instance_fleet_type(self) -> builtins.str:
        '''The node type that the instance fleet hosts.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceFleetType"))

    @instance_fleet_type.setter
    def instance_fleet_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e599502a138f8a9158bcc5bbc77fd3cb1fa6aacdcda3c340c2bc35cdb54c5ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceFleetType", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.InstanceTypeConfigProperty"]]]]:
        '''``InstanceTypeConfigs`` determine the EC2 instances that Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.InstanceTypeConfigProperty"]]]], jsii.get(self, "instanceTypeConfigs"))

    @instance_type_configs.setter
    def instance_type_configs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.InstanceTypeConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__888820cb4f4a0c9a1efd66dd14e34f331d9e75498488017d37693b4ca8f07e10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTypeConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty"]]:
        '''The launch specification for the instance fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty"]], jsii.get(self, "launchSpecifications"))

    @launch_specifications.setter
    def launch_specifications(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__037e3da780812285c831d0eb45598c2c6a76b22d073c1e4a83b5d4529a0e479c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchSpecifications", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The friendly name of the instance fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46de029a613d830d1cd5aafc306617484db5e788259a5eb5e20ddfdb18290125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetOnDemandCapacity"))

    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__822a16f54dafb22c28528e47fdb7a49930c485e6f54b9eeb4a03467e03af3a7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetOnDemandCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacity")
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetSpotCapacity"))

    @target_spot_capacity.setter
    def target_spot_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8c47404264830e50e7ddaef51024f8f530b123b3a2c96dd8fc19683b81e6fc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSpotCapacity", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configuration_properties": "configurationProperties",
            "configurations": "configurations",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            classification: typing.Optional[builtins.str] = None,
            configuration_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''.. epigraph::

   Used only with Amazon EMR release 4.0 and later.

            ``Configuration`` specifies optional configurations for customizing open-source big data applications and environment parameters. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see `Configuring Applications <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`_ in the *Amazon EMR Release Guide* .

            :param classification: The classification within a configuration.
            :param configuration_properties: Within a configuration classification, a set of properties that represent the settings that you want to change in the configuration file. Duplicates not allowed.
            :param configurations: A list of additional configurations to apply within a configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                # configuration_property_: emr.CfnInstanceFleetConfig.ConfigurationProperty
                
                configuration_property = emr.CfnInstanceFleetConfig.ConfigurationProperty(
                    classification="classification",
                    configuration_properties={
                        "configuration_properties_key": "configurationProperties"
                    },
                    configurations=[configuration_property_]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cb99c46a2e6804e68d48ee2a2882e72c00713be16c2a7eb0c1ffda179a4964d)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument configuration_properties", value=configuration_properties, expected_type=type_hints["configuration_properties"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if classification is not None:
                self._values["classification"] = classification
            if configuration_properties is not None:
                self._values["configuration_properties"] = configuration_properties
            if configurations is not None:
                self._values["configurations"] = configurations

        @builtins.property
        def classification(self) -> typing.Optional[builtins.str]:
            '''The classification within a configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-configuration.html#cfn-emr-instancefleetconfig-configuration-classification
            '''
            result = self._values.get("classification")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configuration_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Within a configuration classification, a set of properties that represent the settings that you want to change in the configuration file.

            Duplicates not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-configuration.html#cfn-emr-instancefleetconfig-configuration-configurationproperties
            '''
            result = self._values.get("configuration_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.ConfigurationProperty"]]]]:
            '''A list of additional configurations to apply within a configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-configuration.html#cfn-emr-instancefleetconfig-configuration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.ConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "volume_specification": "volumeSpecification",
            "volumes_per_instance": "volumesPerInstance",
        },
    )
    class EbsBlockDeviceConfigProperty:
        def __init__(
            self,
            *,
            volume_specification: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.VolumeSpecificationProperty", typing.Dict[builtins.str, typing.Any]]],
            volumes_per_instance: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``EbsBlockDeviceConfig`` is a subproperty of the ``EbsConfiguration`` property type.

            ``EbsBlockDeviceConfig`` defines the number and type of EBS volumes to associate with all EC2 instances in an EMR cluster.

            :param volume_specification: EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.
            :param volumes_per_instance: Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                ebs_block_device_config_property = emr.CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty(
                    volume_specification=emr.CfnInstanceFleetConfig.VolumeSpecificationProperty(
                        size_in_gb=123,
                        volume_type="volumeType",
                
                        # the properties below are optional
                        iops=123,
                        throughput=123
                    ),
                
                    # the properties below are optional
                    volumes_per_instance=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3279a4aeccde870f13ef700abffb5a21dac69394e7342602659de2e9d001b6fb)
                check_type(argname="argument volume_specification", value=volume_specification, expected_type=type_hints["volume_specification"])
                check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "volume_specification": volume_specification,
            }
            if volumes_per_instance is not None:
                self._values["volumes_per_instance"] = volumes_per_instance

        @builtins.property
        def volume_specification(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.VolumeSpecificationProperty"]:
            '''EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig.html#cfn-emr-instancefleetconfig-ebsblockdeviceconfig-volumespecification
            '''
            result = self._values.get("volume_specification")
            assert result is not None, "Required property 'volume_specification' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.VolumeSpecificationProperty"], result)

        @builtins.property
        def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
            '''Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig.html#cfn-emr-instancefleetconfig-ebsblockdeviceconfig-volumesperinstance
            '''
            result = self._values.get("volumes_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig.EbsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_block_device_configs": "ebsBlockDeviceConfigs",
            "ebs_optimized": "ebsOptimized",
        },
    )
    class EbsConfigurationProperty:
        def __init__(
            self,
            *,
            ebs_block_device_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''``EbsConfiguration`` determines the EBS volumes to attach to EMR cluster instances.

            :param ebs_block_device_configs: An array of Amazon EBS volume specifications attached to a cluster instance.
            :param ebs_optimized: Indicates whether an Amazon EBS volume is EBS-optimized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-ebsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                ebs_configuration_property = emr.CfnInstanceFleetConfig.EbsConfigurationProperty(
                    ebs_block_device_configs=[emr.CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty(
                        volume_specification=emr.CfnInstanceFleetConfig.VolumeSpecificationProperty(
                            size_in_gb=123,
                            volume_type="volumeType",
                
                            # the properties below are optional
                            iops=123,
                            throughput=123
                        ),
                
                        # the properties below are optional
                        volumes_per_instance=123
                    )],
                    ebs_optimized=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7c01313df17cf722f93042eafce67680bfdf5243bba4058c5cc9d54139c1124)
                check_type(argname="argument ebs_block_device_configs", value=ebs_block_device_configs, expected_type=type_hints["ebs_block_device_configs"])
                check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ebs_block_device_configs is not None:
                self._values["ebs_block_device_configs"] = ebs_block_device_configs
            if ebs_optimized is not None:
                self._values["ebs_optimized"] = ebs_optimized

        @builtins.property
        def ebs_block_device_configs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty"]]]]:
            '''An array of Amazon EBS volume specifications attached to a cluster instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-ebsconfiguration.html#cfn-emr-instancefleetconfig-ebsconfiguration-ebsblockdeviceconfigs
            '''
            result = self._values.get("ebs_block_device_configs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty"]]]], result)

        @builtins.property
        def ebs_optimized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether an Amazon EBS volume is EBS-optimized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-ebsconfiguration.html#cfn-emr-instancefleetconfig-ebsconfiguration-ebsoptimized
            '''
            result = self._values.get("ebs_optimized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "on_demand_specification": "onDemandSpecification",
            "spot_specification": "spotSpecification",
        },
    )
    class InstanceFleetProvisioningSpecificationsProperty:
        def __init__(
            self,
            *,
            on_demand_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            spot_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''.. epigraph::

   The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

            ``InstanceTypeConfig`` is a sub-property of ``InstanceFleetConfig`` . ``InstanceTypeConfig`` determines the EC2 instances that Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities.

            :param on_demand_specification: The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy. .. epigraph:: The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.
            :param spot_specification: The launch specification for Spot instances in the fleet, which determines the defined duration, provisioning timeout behavior, and allocation strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                instance_fleet_provisioning_specifications_property = emr.CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty(
                    on_demand_specification=emr.CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty(
                        allocation_strategy="allocationStrategy"
                    ),
                    spot_specification=emr.CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty(
                        timeout_action="timeoutAction",
                        timeout_duration_minutes=123,
                
                        # the properties below are optional
                        allocation_strategy="allocationStrategy",
                        block_duration_minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__08a22ec5152d77e43e0a91e7ac72349bff7b323c77ba7af7b916a7565bc1a759)
                check_type(argname="argument on_demand_specification", value=on_demand_specification, expected_type=type_hints["on_demand_specification"])
                check_type(argname="argument spot_specification", value=spot_specification, expected_type=type_hints["spot_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if on_demand_specification is not None:
                self._values["on_demand_specification"] = on_demand_specification
            if spot_specification is not None:
                self._values["spot_specification"] = spot_specification

        @builtins.property
        def on_demand_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty"]]:
            '''The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy.

            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications.html#cfn-emr-instancefleetconfig-instancefleetprovisioningspecifications-ondemandspecification
            '''
            result = self._values.get("on_demand_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty"]], result)

        @builtins.property
        def spot_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty"]]:
            '''The launch specification for Spot instances in the fleet, which determines the defined duration, provisioning timeout behavior, and allocation strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancefleetprovisioningspecifications.html#cfn-emr-instancefleetconfig-instancefleetprovisioningspecifications-spotspecification
            '''
            result = self._values.get("spot_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceFleetProvisioningSpecificationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig.InstanceTypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "bid_price": "bidPrice",
            "bid_price_as_percentage_of_on_demand_price": "bidPriceAsPercentageOfOnDemandPrice",
            "configurations": "configurations",
            "custom_ami_id": "customAmiId",
            "ebs_configuration": "ebsConfiguration",
            "weighted_capacity": "weightedCapacity",
        },
    )
    class InstanceTypeConfigProperty:
        def __init__(
            self,
            *,
            instance_type: builtins.str,
            bid_price: typing.Optional[builtins.str] = None,
            bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
            configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            custom_ami_id: typing.Optional[builtins.str] = None,
            ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceFleetConfig.EbsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            weighted_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``InstanceType`` config is a subproperty of ``InstanceFleetConfig`` .

            An instance type configuration specifies each instance type in an instance fleet. The configuration determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities.
            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

            :param instance_type: An Amazon EC2 instance type, such as ``m3.xlarge`` .
            :param bid_price: The bid price for each Amazon EC2 Spot Instance type as defined by ``InstanceType`` . Expressed in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.
            :param bid_price_as_percentage_of_on_demand_price: The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%). If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.
            :param configurations: .. epigraph:: Amazon EMR releases 4.x or later. An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see `Configuring Applications <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`_ .
            :param custom_ami_id: The custom AMI ID to use for the instance type.
            :param ebs_configuration: The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by ``InstanceType`` .
            :param weighted_capacity: The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in ``InstanceFleetConfig`` . This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancetypeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                # configuration_property_: emr.CfnInstanceFleetConfig.ConfigurationProperty
                
                instance_type_config_property = emr.CfnInstanceFleetConfig.InstanceTypeConfigProperty(
                    instance_type="instanceType",
                
                    # the properties below are optional
                    bid_price="bidPrice",
                    bid_price_as_percentage_of_on_demand_price=123,
                    configurations=[emr.CfnInstanceFleetConfig.ConfigurationProperty(
                        classification="classification",
                        configuration_properties={
                            "configuration_properties_key": "configurationProperties"
                        },
                        configurations=[configuration_property_]
                    )],
                    custom_ami_id="customAmiId",
                    ebs_configuration=emr.CfnInstanceFleetConfig.EbsConfigurationProperty(
                        ebs_block_device_configs=[emr.CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty(
                            volume_specification=emr.CfnInstanceFleetConfig.VolumeSpecificationProperty(
                                size_in_gb=123,
                                volume_type="volumeType",
                
                                # the properties below are optional
                                iops=123,
                                throughput=123
                            ),
                
                            # the properties below are optional
                            volumes_per_instance=123
                        )],
                        ebs_optimized=False
                    ),
                    weighted_capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__051c3b44a825d0f79c73260ba9c4b6395a44dae707c2d0ae1291df31ee520108)
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
                check_type(argname="argument bid_price_as_percentage_of_on_demand_price", value=bid_price_as_percentage_of_on_demand_price, expected_type=type_hints["bid_price_as_percentage_of_on_demand_price"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
                check_type(argname="argument custom_ami_id", value=custom_ami_id, expected_type=type_hints["custom_ami_id"])
                check_type(argname="argument ebs_configuration", value=ebs_configuration, expected_type=type_hints["ebs_configuration"])
                check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_type": instance_type,
            }
            if bid_price is not None:
                self._values["bid_price"] = bid_price
            if bid_price_as_percentage_of_on_demand_price is not None:
                self._values["bid_price_as_percentage_of_on_demand_price"] = bid_price_as_percentage_of_on_demand_price
            if configurations is not None:
                self._values["configurations"] = configurations
            if custom_ami_id is not None:
                self._values["custom_ami_id"] = custom_ami_id
            if ebs_configuration is not None:
                self._values["ebs_configuration"] = ebs_configuration
            if weighted_capacity is not None:
                self._values["weighted_capacity"] = weighted_capacity

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''An Amazon EC2 instance type, such as ``m3.xlarge`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancetypeconfig.html#cfn-emr-instancefleetconfig-instancetypeconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bid_price(self) -> typing.Optional[builtins.str]:
            '''The bid price for each Amazon EC2 Spot Instance type as defined by ``InstanceType`` .

            Expressed in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancetypeconfig.html#cfn-emr-instancefleetconfig-instancetypeconfig-bidprice
            '''
            result = self._values.get("bid_price")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bid_price_as_percentage_of_on_demand_price(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by ``InstanceType`` .

            Expressed as a number (for example, 20 specifies 20%). If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancetypeconfig.html#cfn-emr-instancefleetconfig-instancetypeconfig-bidpriceaspercentageofondemandprice
            '''
            result = self._values.get("bid_price_as_percentage_of_on_demand_price")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.ConfigurationProperty"]]]]:
            '''.. epigraph::

   Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see `Configuring Applications <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancetypeconfig.html#cfn-emr-instancefleetconfig-instancetypeconfig-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.ConfigurationProperty"]]]], result)

        @builtins.property
        def custom_ami_id(self) -> typing.Optional[builtins.str]:
            '''The custom AMI ID to use for the instance type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancetypeconfig.html#cfn-emr-instancefleetconfig-instancetypeconfig-customamiid
            '''
            result = self._values.get("custom_ami_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.EbsConfigurationProperty"]]:
            '''The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by ``InstanceType`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancetypeconfig.html#cfn-emr-instancefleetconfig-instancetypeconfig-ebsconfiguration
            '''
            result = self._values.get("ebs_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceFleetConfig.EbsConfigurationProperty"]], result)

        @builtins.property
        def weighted_capacity(self) -> typing.Optional[jsii.Number]:
            '''The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in ``InstanceFleetConfig`` .

            This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-instancetypeconfig.html#cfn-emr-instancefleetconfig-instancetypeconfig-weightedcapacity
            '''
            result = self._values.get("weighted_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceTypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"allocation_strategy": "allocationStrategy"},
    )
    class OnDemandProvisioningSpecificationProperty:
        def __init__(self, *, allocation_strategy: builtins.str) -> None:
            '''The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy.

            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.

            :param allocation_strategy: Specifies the strategy to use in launching On-Demand instance fleets. Currently, the only option is ``lowest-price`` (the default), which launches the lowest price first.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                on_demand_provisioning_specification_property = emr.CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty(
                    allocation_strategy="allocationStrategy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf71b5c7658598ec550bf1195bd742cbfb6e455c0c782143392a53f88bfdf172)
                check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allocation_strategy": allocation_strategy,
            }

        @builtins.property
        def allocation_strategy(self) -> builtins.str:
            '''Specifies the strategy to use in launching On-Demand instance fleets.

            Currently, the only option is ``lowest-price`` (the default), which launches the lowest price first.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification.html#cfn-emr-instancefleetconfig-ondemandprovisioningspecification-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            assert result is not None, "Required property 'allocation_strategy' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnDemandProvisioningSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "timeout_action": "timeoutAction",
            "timeout_duration_minutes": "timeoutDurationMinutes",
            "allocation_strategy": "allocationStrategy",
            "block_duration_minutes": "blockDurationMinutes",
        },
    )
    class SpotProvisioningSpecificationProperty:
        def __init__(
            self,
            *,
            timeout_action: builtins.str,
            timeout_duration_minutes: jsii.Number,
            allocation_strategy: typing.Optional[builtins.str] = None,
            block_duration_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``SpotProvisioningSpecification`` is a subproperty of the ``InstanceFleetProvisioningSpecifications`` property type.

            ``SpotProvisioningSpecification`` determines the launch specification for Spot instances in the instance fleet, which includes the defined duration and provisioning timeout behavior.
            .. epigraph::

               The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

            :param timeout_action: The action to take when ``TargetSpotCapacity`` has not been fulfilled when the ``TimeoutDurationMinutes`` has expired; that is, when all Spot Instances could not be provisioned within the Spot provisioning timeout. Valid values are ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that if no Spot Instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.
            :param timeout_duration_minutes: The Spot provisioning timeout period in minutes. If Spot Instances are not provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.
            :param allocation_strategy: Specifies one of the following strategies to launch Spot Instance fleets: ``price-capacity-optimized`` , ``capacity-optimized`` , ``lowest-price`` , or ``diversified`` . For more information on the provisioning strategies, see `Allocation strategies for Spot Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html>`_ in the *Amazon EC2 User Guide for Linux Instances* . .. epigraph:: When you launch a Spot Instance fleet with the old console, it automatically launches with the ``capacity-optimized`` strategy. You can't change the allocation strategy from the old console.
            :param block_duration_minutes: The defined duration for Spot Instances (also known as Spot blocks) in minutes. When specified, the Spot Instance does not terminate before the defined duration expires, and defined duration pricing for Spot Instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot Instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates. .. epigraph:: Spot Instances with a defined duration (also known as Spot blocks) are no longer available to new customers from July 1, 2021. For customers who have previously used the feature, we will continue to support Spot Instances with a defined duration until December 31, 2022.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-spotprovisioningspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                spot_provisioning_specification_property = emr.CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty(
                    timeout_action="timeoutAction",
                    timeout_duration_minutes=123,
                
                    # the properties below are optional
                    allocation_strategy="allocationStrategy",
                    block_duration_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6b61d9945e0ef7f9b80bb5d1375dc8b2f9f8655abbb01833fe74ef1cafbfcd8d)
                check_type(argname="argument timeout_action", value=timeout_action, expected_type=type_hints["timeout_action"])
                check_type(argname="argument timeout_duration_minutes", value=timeout_duration_minutes, expected_type=type_hints["timeout_duration_minutes"])
                check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
                check_type(argname="argument block_duration_minutes", value=block_duration_minutes, expected_type=type_hints["block_duration_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "timeout_action": timeout_action,
                "timeout_duration_minutes": timeout_duration_minutes,
            }
            if allocation_strategy is not None:
                self._values["allocation_strategy"] = allocation_strategy
            if block_duration_minutes is not None:
                self._values["block_duration_minutes"] = block_duration_minutes

        @builtins.property
        def timeout_action(self) -> builtins.str:
            '''The action to take when ``TargetSpotCapacity`` has not been fulfilled when the ``TimeoutDurationMinutes`` has expired;

            that is, when all Spot Instances could not be provisioned within the Spot provisioning timeout. Valid values are ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that if no Spot Instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-spotprovisioningspecification.html#cfn-emr-instancefleetconfig-spotprovisioningspecification-timeoutaction
            '''
            result = self._values.get("timeout_action")
            assert result is not None, "Required property 'timeout_action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_duration_minutes(self) -> jsii.Number:
            '''The Spot provisioning timeout period in minutes.

            If Spot Instances are not provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-spotprovisioningspecification.html#cfn-emr-instancefleetconfig-spotprovisioningspecification-timeoutdurationminutes
            '''
            result = self._values.get("timeout_duration_minutes")
            assert result is not None, "Required property 'timeout_duration_minutes' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def allocation_strategy(self) -> typing.Optional[builtins.str]:
            '''Specifies one of the following strategies to launch Spot Instance fleets: ``price-capacity-optimized`` , ``capacity-optimized`` , ``lowest-price`` , or ``diversified`` .

            For more information on the provisioning strategies, see `Allocation strategies for Spot Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html>`_ in the *Amazon EC2 User Guide for Linux Instances* .
            .. epigraph::

               When you launch a Spot Instance fleet with the old console, it automatically launches with the ``capacity-optimized`` strategy. You can't change the allocation strategy from the old console.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-spotprovisioningspecification.html#cfn-emr-instancefleetconfig-spotprovisioningspecification-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
            '''The defined duration for Spot Instances (also known as Spot blocks) in minutes.

            When specified, the Spot Instance does not terminate before the defined duration expires, and defined duration pricing for Spot Instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot Instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates.
            .. epigraph::

               Spot Instances with a defined duration (also known as Spot blocks) are no longer available to new customers from July 1, 2021. For customers who have previously used the feature, we will continue to support Spot Instances with a defined duration until December 31, 2022.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-spotprovisioningspecification.html#cfn-emr-instancefleetconfig-spotprovisioningspecification-blockdurationminutes
            '''
            result = self._values.get("block_duration_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpotProvisioningSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfig.VolumeSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "size_in_gb": "sizeInGb",
            "volume_type": "volumeType",
            "iops": "iops",
            "throughput": "throughput",
        },
    )
    class VolumeSpecificationProperty:
        def __init__(
            self,
            *,
            size_in_gb: jsii.Number,
            volume_type: builtins.str,
            iops: typing.Optional[jsii.Number] = None,
            throughput: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``VolumeSpecification`` is a subproperty of the ``EbsBlockDeviceConfig`` property type.

            ``VolumeSecification`` determines the volume type, IOPS, and size (GiB) for EBS volumes attached to EC2 instances.

            :param size_in_gb: The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            :param volume_type: The volume type. Volume types supported are gp3, gp2, io1, st1, sc1, and standard.
            :param iops: The number of I/O operations per second (IOPS) that the volume supports.
            :param throughput: The throughput, in mebibyte per second (MiB/s). This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-volumespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                volume_specification_property = emr.CfnInstanceFleetConfig.VolumeSpecificationProperty(
                    size_in_gb=123,
                    volume_type="volumeType",
                
                    # the properties below are optional
                    iops=123,
                    throughput=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cbcefec98bf4df26aee8c4c32035c6379883a9a1f189bbc763cba54f8f73d579)
                check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "size_in_gb": size_in_gb,
                "volume_type": volume_type,
            }
            if iops is not None:
                self._values["iops"] = iops
            if throughput is not None:
                self._values["throughput"] = throughput

        @builtins.property
        def size_in_gb(self) -> jsii.Number:
            '''The volume size, in gibibytes (GiB).

            This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-volumespecification.html#cfn-emr-instancefleetconfig-volumespecification-sizeingb
            '''
            result = self._values.get("size_in_gb")
            assert result is not None, "Required property 'size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_type(self) -> builtins.str:
            '''The volume type.

            Volume types supported are gp3, gp2, io1, st1, sc1, and standard.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-volumespecification.html#cfn-emr-instancefleetconfig-volumespecification-volumetype
            '''
            result = self._values.get("volume_type")
            assert result is not None, "Required property 'volume_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The number of I/O operations per second (IOPS) that the volume supports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-volumespecification.html#cfn-emr-instancefleetconfig-volumespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''The throughput, in mebibyte per second (MiB/s).

            This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancefleetconfig-volumespecification.html#cfn-emr-instancefleetconfig-volumespecification-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emr.CfnInstanceFleetConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_id": "clusterId",
        "instance_fleet_type": "instanceFleetType",
        "instance_type_configs": "instanceTypeConfigs",
        "launch_specifications": "launchSpecifications",
        "name": "name",
        "target_on_demand_capacity": "targetOnDemandCapacity",
        "target_spot_capacity": "targetSpotCapacity",
    },
)
class CfnInstanceFleetConfigProps:
    def __init__(
        self,
        *,
        cluster_id: builtins.str,
        instance_fleet_type: builtins.str,
        instance_type_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.InstanceTypeConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        launch_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceFleetConfig``.

        :param cluster_id: The unique identifier of the EMR cluster.
        :param instance_fleet_type: The node type that the instance fleet hosts. *Allowed Values* : TASK
        :param instance_type_configs: ``InstanceTypeConfigs`` determine the EC2 instances that Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities. .. epigraph:: The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
        :param launch_specifications: The launch specification for the instance fleet.
        :param name: The friendly name of the instance fleet.
        :param target_on_demand_capacity: The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. .. epigraph:: If not specified or set to 0, only Spot instances are provisioned for the instance fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.
        :param target_spot_capacity: The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When a Spot instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. .. epigraph:: If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emr as emr
            
            # configuration_property_: emr.CfnInstanceFleetConfig.ConfigurationProperty
            
            cfn_instance_fleet_config_props = emr.CfnInstanceFleetConfigProps(
                cluster_id="clusterId",
                instance_fleet_type="instanceFleetType",
            
                # the properties below are optional
                instance_type_configs=[emr.CfnInstanceFleetConfig.InstanceTypeConfigProperty(
                    instance_type="instanceType",
            
                    # the properties below are optional
                    bid_price="bidPrice",
                    bid_price_as_percentage_of_on_demand_price=123,
                    configurations=[emr.CfnInstanceFleetConfig.ConfigurationProperty(
                        classification="classification",
                        configuration_properties={
                            "configuration_properties_key": "configurationProperties"
                        },
                        configurations=[configuration_property_]
                    )],
                    custom_ami_id="customAmiId",
                    ebs_configuration=emr.CfnInstanceFleetConfig.EbsConfigurationProperty(
                        ebs_block_device_configs=[emr.CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty(
                            volume_specification=emr.CfnInstanceFleetConfig.VolumeSpecificationProperty(
                                size_in_gb=123,
                                volume_type="volumeType",
            
                                # the properties below are optional
                                iops=123,
                                throughput=123
                            ),
            
                            # the properties below are optional
                            volumes_per_instance=123
                        )],
                        ebs_optimized=False
                    ),
                    weighted_capacity=123
                )],
                launch_specifications=emr.CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty(
                    on_demand_specification=emr.CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty(
                        allocation_strategy="allocationStrategy"
                    ),
                    spot_specification=emr.CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty(
                        timeout_action="timeoutAction",
                        timeout_duration_minutes=123,
            
                        # the properties below are optional
                        allocation_strategy="allocationStrategy",
                        block_duration_minutes=123
                    )
                ),
                name="name",
                target_on_demand_capacity=123,
                target_spot_capacity=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3f5c77adfe4a2c26c531874c0df7d744af995801149e28623e666dfb6bf26b6)
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument instance_fleet_type", value=instance_fleet_type, expected_type=type_hints["instance_fleet_type"])
            check_type(argname="argument instance_type_configs", value=instance_type_configs, expected_type=type_hints["instance_type_configs"])
            check_type(argname="argument launch_specifications", value=launch_specifications, expected_type=type_hints["launch_specifications"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_on_demand_capacity", value=target_on_demand_capacity, expected_type=type_hints["target_on_demand_capacity"])
            check_type(argname="argument target_spot_capacity", value=target_spot_capacity, expected_type=type_hints["target_spot_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
            "instance_fleet_type": instance_fleet_type,
        }
        if instance_type_configs is not None:
            self._values["instance_type_configs"] = instance_type_configs
        if launch_specifications is not None:
            self._values["launch_specifications"] = launch_specifications
        if name is not None:
            self._values["name"] = name
        if target_on_demand_capacity is not None:
            self._values["target_on_demand_capacity"] = target_on_demand_capacity
        if target_spot_capacity is not None:
            self._values["target_spot_capacity"] = target_spot_capacity

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''The unique identifier of the EMR cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html#cfn-emr-instancefleetconfig-clusterid
        '''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_fleet_type(self) -> builtins.str:
        '''The node type that the instance fleet hosts.

        *Allowed Values* : TASK

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html#cfn-emr-instancefleetconfig-instancefleettype
        '''
        result = self._values.get("instance_fleet_type")
        assert result is not None, "Required property 'instance_fleet_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceFleetConfig.InstanceTypeConfigProperty]]]]:
        '''``InstanceTypeConfigs`` determine the EC2 instances that Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities.

        .. epigraph::

           The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html#cfn-emr-instancefleetconfig-instancetypeconfigs
        '''
        result = self._values.get("instance_type_configs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceFleetConfig.InstanceTypeConfigProperty]]]], result)

    @builtins.property
    def launch_specifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty]]:
        '''The launch specification for the instance fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html#cfn-emr-instancefleetconfig-launchspecifications
        '''
        result = self._values.get("launch_specifications")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The friendly name of the instance fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html#cfn-emr-instancefleetconfig-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision.

        When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
        .. epigraph::

           If not specified or set to 0, only Spot instances are provisioned for the instance fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html#cfn-emr-instancefleetconfig-targetondemandcapacity
        '''
        result = self._values.get("target_on_demand_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision.

        When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by ``InstanceTypeConfig`` . Each instance configuration has a specified ``WeightedCapacity`` . When a Spot instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
        .. epigraph::

           If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancefleetconfig.html#cfn-emr-instancefleetconfig-targetspotcapacity
        '''
        result = self._values.get("target_spot_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceFleetConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnInstanceGroupConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig",
):
    '''Use ``InstanceGroupConfig`` to define instance groups for an EMR cluster.

    A cluster can not use both instance groups and instance fleets. For more information, see `Create a Cluster with Instance Fleets or Uniform Instance Groups <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-instance-group-configuration.html>`_ in the *Amazon EMR Management Guide* .
    .. epigraph::

       You can currently only add task instance groups to a cluster with this resource. If you use this resource, CloudFormation waits for the cluster launch to complete before adding the task instance group to the cluster. In order to add task instance groups to the cluster as part of the cluster launch and minimize delays in provisioning task nodes, use the ``TaskInstanceGroups`` subproperty for the `AWS::EMR::Cluster JobFlowInstancesConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html>`_ property instead. To use this subproperty, see `AWS::EMR::Cluster <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html>`_ for examples.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html
    :cloudformationResource: AWS::EMR::InstanceGroupConfig
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emr as emr
        
        # configuration_property_: emr.CfnInstanceGroupConfig.ConfigurationProperty
        
        cfn_instance_group_config = emr.CfnInstanceGroupConfig(self, "MyCfnInstanceGroupConfig",
            instance_count=123,
            instance_role="instanceRole",
            instance_type="instanceType",
            job_flow_id="jobFlowId",
        
            # the properties below are optional
            auto_scaling_policy=emr.CfnInstanceGroupConfig.AutoScalingPolicyProperty(
                constraints=emr.CfnInstanceGroupConfig.ScalingConstraintsProperty(
                    max_capacity=123,
                    min_capacity=123
                ),
                rules=[emr.CfnInstanceGroupConfig.ScalingRuleProperty(
                    action=emr.CfnInstanceGroupConfig.ScalingActionProperty(
                        simple_scaling_policy_configuration=emr.CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty(
                            scaling_adjustment=123,
        
                            # the properties below are optional
                            adjustment_type="adjustmentType",
                            cool_down=123
                        ),
        
                        # the properties below are optional
                        market="market"
                    ),
                    name="name",
                    trigger=emr.CfnInstanceGroupConfig.ScalingTriggerProperty(
                        cloud_watch_alarm_definition=emr.CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty(
                            comparison_operator="comparisonOperator",
                            metric_name="metricName",
                            period=123,
                            threshold=123,
        
                            # the properties below are optional
                            dimensions=[emr.CfnInstanceGroupConfig.MetricDimensionProperty(
                                key="key",
                                value="value"
                            )],
                            evaluation_periods=123,
                            namespace="namespace",
                            statistic="statistic",
                            unit="unit"
                        )
                    ),
        
                    # the properties below are optional
                    description="description"
                )]
            ),
            bid_price="bidPrice",
            configurations=[emr.CfnInstanceGroupConfig.ConfigurationProperty(
                classification="classification",
                configuration_properties={
                    "configuration_properties_key": "configurationProperties"
                },
                configurations=[configuration_property_]
            )],
            custom_ami_id="customAmiId",
            ebs_configuration=emr.CfnInstanceGroupConfig.EbsConfigurationProperty(
                ebs_block_device_configs=[emr.CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty(
                    volume_specification=emr.CfnInstanceGroupConfig.VolumeSpecificationProperty(
                        size_in_gb=123,
                        volume_type="volumeType",
        
                        # the properties below are optional
                        iops=123,
                        throughput=123
                    ),
        
                    # the properties below are optional
                    volumes_per_instance=123
                )],
                ebs_optimized=False
            ),
            market="market",
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_count: jsii.Number,
        instance_role: builtins.str,
        instance_type: builtins.str,
        job_flow_id: builtins.str,
        auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.AutoScalingPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        bid_price: typing.Optional[builtins.str] = None,
        configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.EbsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        market: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_count: Target number of instances for the instance group.
        :param instance_role: The role of the instance group in the cluster. *Allowed Values* : TASK
        :param instance_type: The Amazon EC2 instance type for all instances in the instance group.
        :param job_flow_id: The ID of an Amazon EMR cluster that you want to associate this instance group with.
        :param auto_scaling_policy: ``AutoScalingPolicy`` is a subproperty of ``InstanceGroupConfig`` . ``AutoScalingPolicy`` defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. For more information, see `Using Automatic Scaling in Amazon EMR <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-automatic-scaling.html>`_ in the *Amazon EMR Management Guide* .
        :param bid_price: If specified, indicates that the instance group uses Spot Instances. This is the maximum price you are willing to pay for Spot Instances. Specify ``OnDemandPrice`` to set the amount equal to the On-Demand price, or specify an amount in USD.
        :param configurations: .. epigraph:: Amazon EMR releases 4.x or later. The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).
        :param custom_ami_id: The custom AMI ID to use for the provisioned instance group.
        :param ebs_configuration: ``EbsConfiguration`` determines the EBS volumes to attach to EMR cluster instances.
        :param market: Market type of the Amazon EC2 instances used to create a cluster node.
        :param name: Friendly name given to the instance group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b03c1e96b01aafd31c257702f4a9ed7a4281e8d9ba0f2f19a20ccc53465d08e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceGroupConfigProps(
            instance_count=instance_count,
            instance_role=instance_role,
            instance_type=instance_type,
            job_flow_id=job_flow_id,
            auto_scaling_policy=auto_scaling_policy,
            bid_price=bid_price,
            configurations=configurations,
            custom_ami_id=custom_ami_id,
            ebs_configuration=ebs_configuration,
            market=market,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1de17e348f1473656fa16b6154e6ecc550f06d756f34e0dd16848f80c72fe2bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6c371e1ed73cea2b17a5b42ab80c40254e3489b4218c3d85de868719ecf4c39)
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
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        '''Target number of instances for the instance group.'''
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a56b526bb946892e98d3d7d2b105ae4d7b95c59bf23590bba4cb3f57e014a87b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceRole")
    def instance_role(self) -> builtins.str:
        '''The role of the instance group in the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceRole"))

    @instance_role.setter
    def instance_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d176dc92e6cc9a7943f8591598418735b47fe6599a6a87375ce8047e23f2582c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceRole", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''The Amazon EC2 instance type for all instances in the instance group.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce5c0de0de6b187413fc259ce830ca1a4cb07874c4e2e4614d43b9806c442a8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="jobFlowId")
    def job_flow_id(self) -> builtins.str:
        '''The ID of an Amazon EMR cluster that you want to associate this instance group with.'''
        return typing.cast(builtins.str, jsii.get(self, "jobFlowId"))

    @job_flow_id.setter
    def job_flow_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69245f4d15e2a5dae10e27b298ff011d20580fac579b2b51dfb574b9538d9552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobFlowId", value)

    @builtins.property
    @jsii.member(jsii_name="autoScalingPolicy")
    def auto_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.AutoScalingPolicyProperty"]]:
        '''``AutoScalingPolicy`` is a subproperty of ``InstanceGroupConfig`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.AutoScalingPolicyProperty"]], jsii.get(self, "autoScalingPolicy"))

    @auto_scaling_policy.setter
    def auto_scaling_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.AutoScalingPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ef90a0dcff109aaa0f7a46baf739816f26a3ccb9669240606f89552508d0ca8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''If specified, indicates that the instance group uses Spot Instances.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab690714e1919e92ed20dc7aa3e5315a2b1bfbcee89fc65c09ea7168c130b1dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="configurations")
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ConfigurationProperty"]]]]:
        '''.. epigraph::

   Amazon EMR releases 4.x or later.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ConfigurationProperty"]]]], jsii.get(self, "configurations"))

    @configurations.setter
    def configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0131144525f35798c3b6081d980630003a3d1b9f1c3aae652f676206e8aeaa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurations", value)

    @builtins.property
    @jsii.member(jsii_name="customAmiId")
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''The custom AMI ID to use for the provisioned instance group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAmiId"))

    @custom_ami_id.setter
    def custom_ami_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__303cab696a08592b720c8e8be64275a3bbf6b789e1077ee4c162c6c0712653e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAmiId", value)

    @builtins.property
    @jsii.member(jsii_name="ebsConfiguration")
    def ebs_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.EbsConfigurationProperty"]]:
        '''``EbsConfiguration`` determines the EBS volumes to attach to EMR cluster instances.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.EbsConfigurationProperty"]], jsii.get(self, "ebsConfiguration"))

    @ebs_configuration.setter
    def ebs_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.EbsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07cf75fd968a10f65fd11c71b6efc052932bd414a38416da34ccff0a4335fd8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="market")
    def market(self) -> typing.Optional[builtins.str]:
        '''Market type of the Amazon EC2 instances used to create a cluster node.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "market"))

    @market.setter
    def market(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05359e9787323de816895b743b6af3dd8f21fcc6a67f534dd7684d66581d93c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "market", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Friendly name given to the instance group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58871e6eae621e6fbe1e15c4166ad29e07293a9a1d2305d7fe9ca365634fb809)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.AutoScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"constraints": "constraints", "rules": "rules"},
    )
    class AutoScalingPolicyProperty:
        def __init__(
            self,
            *,
            constraints: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.ScalingConstraintsProperty", typing.Dict[builtins.str, typing.Any]]],
            rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.ScalingRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''``AutoScalingPolicy`` defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric.

            For more information, see `Using Automatic Scaling in Amazon EMR <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-automatic-scaling.html>`_ in the *Amazon EMR Management Guide* .

            :param constraints: The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
            :param rules: The scale-in and scale-out rules that comprise the automatic scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-autoscalingpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                auto_scaling_policy_property = emr.CfnInstanceGroupConfig.AutoScalingPolicyProperty(
                    constraints=emr.CfnInstanceGroupConfig.ScalingConstraintsProperty(
                        max_capacity=123,
                        min_capacity=123
                    ),
                    rules=[emr.CfnInstanceGroupConfig.ScalingRuleProperty(
                        action=emr.CfnInstanceGroupConfig.ScalingActionProperty(
                            simple_scaling_policy_configuration=emr.CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty(
                                scaling_adjustment=123,
                
                                # the properties below are optional
                                adjustment_type="adjustmentType",
                                cool_down=123
                            ),
                
                            # the properties below are optional
                            market="market"
                        ),
                        name="name",
                        trigger=emr.CfnInstanceGroupConfig.ScalingTriggerProperty(
                            cloud_watch_alarm_definition=emr.CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty(
                                comparison_operator="comparisonOperator",
                                metric_name="metricName",
                                period=123,
                                threshold=123,
                
                                # the properties below are optional
                                dimensions=[emr.CfnInstanceGroupConfig.MetricDimensionProperty(
                                    key="key",
                                    value="value"
                                )],
                                evaluation_periods=123,
                                namespace="namespace",
                                statistic="statistic",
                                unit="unit"
                            )
                        ),
                
                        # the properties below are optional
                        description="description"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ccf52c4a35db129b92c587555ec8d0f67a3d97092e5307fa0ddcb0b2106c137)
                check_type(argname="argument constraints", value=constraints, expected_type=type_hints["constraints"])
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "constraints": constraints,
                "rules": rules,
            }

        @builtins.property
        def constraints(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ScalingConstraintsProperty"]:
            '''The upper and lower Amazon EC2 instance limits for an automatic scaling policy.

            Automatic scaling activity will not cause an instance group to grow above or below these limits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-autoscalingpolicy.html#cfn-emr-instancegroupconfig-autoscalingpolicy-constraints
            '''
            result = self._values.get("constraints")
            assert result is not None, "Required property 'constraints' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ScalingConstraintsProperty"], result)

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ScalingRuleProperty"]]]:
            '''The scale-in and scale-out rules that comprise the automatic scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-autoscalingpolicy.html#cfn-emr-instancegroupconfig-autoscalingpolicy-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ScalingRuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "metric_name": "metricName",
            "period": "period",
            "threshold": "threshold",
            "dimensions": "dimensions",
            "evaluation_periods": "evaluationPeriods",
            "namespace": "namespace",
            "statistic": "statistic",
            "unit": "unit",
        },
    )
    class CloudWatchAlarmDefinitionProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            metric_name: builtins.str,
            period: jsii.Number,
            threshold: jsii.Number,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.MetricDimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            evaluation_periods: typing.Optional[jsii.Number] = None,
            namespace: typing.Optional[builtins.str] = None,
            statistic: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``CloudWatchAlarmDefinition`` is a subproperty of the ``ScalingTrigger`` property, which determines when to trigger an automatic scaling activity.

            Scaling activity begins when you satisfy the defined alarm conditions.

            :param comparison_operator: Determines how the metric specified by ``MetricName`` is compared to the value specified by ``Threshold`` .
            :param metric_name: The name of the CloudWatch metric that is watched to determine an alarm condition.
            :param period: The period, in seconds, over which the statistic is applied. CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify ``300`` .
            :param threshold: The value against which the specified statistic is compared.
            :param dimensions: A CloudWatch metric dimension.
            :param evaluation_periods: The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is ``1`` .
            :param namespace: The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .
            :param statistic: The statistic to apply to the metric associated with the alarm. The default is ``AVERAGE`` .
            :param unit: The unit of measure associated with the CloudWatch metric being watched. The value specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                cloud_watch_alarm_definition_property = emr.CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty(
                    comparison_operator="comparisonOperator",
                    metric_name="metricName",
                    period=123,
                    threshold=123,
                
                    # the properties below are optional
                    dimensions=[emr.CfnInstanceGroupConfig.MetricDimensionProperty(
                        key="key",
                        value="value"
                    )],
                    evaluation_periods=123,
                    namespace="namespace",
                    statistic="statistic",
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5ef36d052fd1c73f3c150fc370cea09f7f8cfa0fed7c5d3618650d6f138e57d9)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument period", value=period, expected_type=type_hints["period"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "metric_name": metric_name,
                "period": period,
                "threshold": threshold,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if evaluation_periods is not None:
                self._values["evaluation_periods"] = evaluation_periods
            if namespace is not None:
                self._values["namespace"] = namespace
            if statistic is not None:
                self._values["statistic"] = statistic
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''Determines how the metric specified by ``MetricName`` is compared to the value specified by ``Threshold`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the CloudWatch metric that is watched to determine an alarm condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''The period, in seconds, over which the statistic is applied.

            CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify ``300`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''The value against which the specified statistic is compared.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.MetricDimensionProperty"]]]]:
            '''A CloudWatch metric dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.MetricDimensionProperty"]]]], result)

        @builtins.property
        def evaluation_periods(self) -> typing.Optional[jsii.Number]:
            '''The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity.

            The default value is ``1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-evaluationperiods
            '''
            result = self._values.get("evaluation_periods")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace for the CloudWatch metric.

            The default is ``AWS/ElasticMapReduce`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def statistic(self) -> typing.Optional[builtins.str]:
            '''The statistic to apply to the metric associated with the alarm.

            The default is ``AVERAGE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-statistic
            '''
            result = self._values.get("statistic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit of measure associated with the CloudWatch metric being watched.

            The value specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-emr-instancegroupconfig-cloudwatchalarmdefinition-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchAlarmDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configuration_properties": "configurationProperties",
            "configurations": "configurations",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            classification: typing.Optional[builtins.str] = None,
            configuration_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''``Configurations`` is a property of the ``AWS::EMR::Cluster`` resource that specifies the configuration of applications on an Amazon EMR cluster.

            Configurations are optional. You can use them to have EMR customize applications and software bundled with Amazon EMR when a cluster is created. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see `Configuring Applications <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`_ .
            .. epigraph::

               Applies only to Amazon EMR releases 4.0 and later.

            :param classification: The classification within a configuration.
            :param configuration_properties: Within a configuration classification, a set of properties that represent the settings that you want to change in the configuration file. Duplicates not allowed.
            :param configurations: A list of additional configurations to apply within a configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                # configuration_property_: emr.CfnInstanceGroupConfig.ConfigurationProperty
                
                configuration_property = emr.CfnInstanceGroupConfig.ConfigurationProperty(
                    classification="classification",
                    configuration_properties={
                        "configuration_properties_key": "configurationProperties"
                    },
                    configurations=[configuration_property_]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ac2b0b1a65e34f3c9e098b6f75c278daa93d377b96cededa4517b4fa7759d9e)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument configuration_properties", value=configuration_properties, expected_type=type_hints["configuration_properties"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if classification is not None:
                self._values["classification"] = classification
            if configuration_properties is not None:
                self._values["configuration_properties"] = configuration_properties
            if configurations is not None:
                self._values["configurations"] = configurations

        @builtins.property
        def classification(self) -> typing.Optional[builtins.str]:
            '''The classification within a configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-configuration.html#cfn-emr-instancegroupconfig-configuration-classification
            '''
            result = self._values.get("classification")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configuration_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Within a configuration classification, a set of properties that represent the settings that you want to change in the configuration file.

            Duplicates not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-configuration.html#cfn-emr-instancegroupconfig-configuration-configurationproperties
            '''
            result = self._values.get("configuration_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ConfigurationProperty"]]]]:
            '''A list of additional configurations to apply within a configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-configuration.html#cfn-emr-instancegroupconfig-configuration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "volume_specification": "volumeSpecification",
            "volumes_per_instance": "volumesPerInstance",
        },
    )
    class EbsBlockDeviceConfigProperty:
        def __init__(
            self,
            *,
            volume_specification: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.VolumeSpecificationProperty", typing.Dict[builtins.str, typing.Any]]],
            volumes_per_instance: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration of requested EBS block device associated with the instance group with count of volumes that are associated to every instance.

            :param volume_specification: EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.
            :param volumes_per_instance: Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                ebs_block_device_config_property = emr.CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty(
                    volume_specification=emr.CfnInstanceGroupConfig.VolumeSpecificationProperty(
                        size_in_gb=123,
                        volume_type="volumeType",
                
                        # the properties below are optional
                        iops=123,
                        throughput=123
                    ),
                
                    # the properties below are optional
                    volumes_per_instance=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ee72789132b4e90a1d6a90327a95ec789abc3a6724fa23b1de25280e805781c2)
                check_type(argname="argument volume_specification", value=volume_specification, expected_type=type_hints["volume_specification"])
                check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "volume_specification": volume_specification,
            }
            if volumes_per_instance is not None:
                self._values["volumes_per_instance"] = volumes_per_instance

        @builtins.property
        def volume_specification(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.VolumeSpecificationProperty"]:
            '''EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig.html#cfn-emr-instancegroupconfig-ebsblockdeviceconfig-volumespecification
            '''
            result = self._values.get("volume_specification")
            assert result is not None, "Required property 'volume_specification' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.VolumeSpecificationProperty"], result)

        @builtins.property
        def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
            '''Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig.html#cfn-emr-instancegroupconfig-ebsblockdeviceconfig-volumesperinstance
            '''
            result = self._values.get("volumes_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.EbsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_block_device_configs": "ebsBlockDeviceConfigs",
            "ebs_optimized": "ebsOptimized",
        },
    )
    class EbsConfigurationProperty:
        def __init__(
            self,
            *,
            ebs_block_device_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The Amazon EBS configuration of a cluster instance.

            :param ebs_block_device_configs: An array of Amazon EBS volume specifications attached to a cluster instance.
            :param ebs_optimized: Indicates whether an Amazon EBS volume is EBS-optimized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-ebsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                ebs_configuration_property = emr.CfnInstanceGroupConfig.EbsConfigurationProperty(
                    ebs_block_device_configs=[emr.CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty(
                        volume_specification=emr.CfnInstanceGroupConfig.VolumeSpecificationProperty(
                            size_in_gb=123,
                            volume_type="volumeType",
                
                            # the properties below are optional
                            iops=123,
                            throughput=123
                        ),
                
                        # the properties below are optional
                        volumes_per_instance=123
                    )],
                    ebs_optimized=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0f334f21b45a80c7afc87361f15a522c7fcfaa41b4f7ab73dce958c051806dc9)
                check_type(argname="argument ebs_block_device_configs", value=ebs_block_device_configs, expected_type=type_hints["ebs_block_device_configs"])
                check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ebs_block_device_configs is not None:
                self._values["ebs_block_device_configs"] = ebs_block_device_configs
            if ebs_optimized is not None:
                self._values["ebs_optimized"] = ebs_optimized

        @builtins.property
        def ebs_block_device_configs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty"]]]]:
            '''An array of Amazon EBS volume specifications attached to a cluster instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-ebsconfiguration.html#cfn-emr-instancegroupconfig-ebsconfiguration-ebsblockdeviceconfigs
            '''
            result = self._values.get("ebs_block_device_configs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty"]]]], result)

        @builtins.property
        def ebs_optimized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether an Amazon EBS volume is EBS-optimized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-ebsconfiguration.html#cfn-emr-instancegroupconfig-ebsconfiguration-ebsoptimized
            '''
            result = self._values.get("ebs_optimized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''``MetricDimension`` is a subproperty of the ``CloudWatchAlarmDefinition`` property type.

            ``MetricDimension`` specifies a CloudWatch dimension, which is specified with a ``Key`` ``Value`` pair. The key is known as a ``Name`` in CloudWatch. By default, Amazon EMR uses one dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID, which is ``${emr.clusterId}`` . This enables the automatic scaling rule for EMR to bootstrap when the cluster ID becomes available during cluster creation.

            :param key: The dimension name.
            :param value: The dimension value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-metricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                metric_dimension_property = emr.CfnInstanceGroupConfig.MetricDimensionProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c2113ac9fdc707bb27249d54043fd206f25a93101010e5b771e1e0958839cdc0)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The dimension name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-metricdimension.html#cfn-emr-instancegroupconfig-metricdimension-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The dimension value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-metricdimension.html#cfn-emr-instancegroupconfig-metricdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.ScalingActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "simple_scaling_policy_configuration": "simpleScalingPolicyConfiguration",
            "market": "market",
        },
    )
    class ScalingActionProperty:
        def __init__(
            self,
            *,
            simple_scaling_policy_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            market: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``ScalingAction`` is a subproperty of the ``ScalingRule`` property type.

            ``ScalingAction`` determines the type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

            :param simple_scaling_policy_configuration: The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.
            :param market: Not available for instance groups. Instance groups use the market type specified for the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                scaling_action_property = emr.CfnInstanceGroupConfig.ScalingActionProperty(
                    simple_scaling_policy_configuration=emr.CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty(
                        scaling_adjustment=123,
                
                        # the properties below are optional
                        adjustment_type="adjustmentType",
                        cool_down=123
                    ),
                
                    # the properties below are optional
                    market="market"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__724cf187947d5b03301bf75eb59a7228254024fd628805c879916c536c7c6051)
                check_type(argname="argument simple_scaling_policy_configuration", value=simple_scaling_policy_configuration, expected_type=type_hints["simple_scaling_policy_configuration"])
                check_type(argname="argument market", value=market, expected_type=type_hints["market"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "simple_scaling_policy_configuration": simple_scaling_policy_configuration,
            }
            if market is not None:
                self._values["market"] = market

        @builtins.property
        def simple_scaling_policy_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty"]:
            '''The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingaction.html#cfn-emr-instancegroupconfig-scalingaction-simplescalingpolicyconfiguration
            '''
            result = self._values.get("simple_scaling_policy_configuration")
            assert result is not None, "Required property 'simple_scaling_policy_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty"], result)

        @builtins.property
        def market(self) -> typing.Optional[builtins.str]:
            '''Not available for instance groups.

            Instance groups use the market type specified for the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingaction.html#cfn-emr-instancegroupconfig-scalingaction-market
            '''
            result = self._values.get("market")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.ScalingConstraintsProperty",
        jsii_struct_bases=[],
        name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
    )
    class ScalingConstraintsProperty:
        def __init__(
            self,
            *,
            max_capacity: jsii.Number,
            min_capacity: jsii.Number,
        ) -> None:
            '''``ScalingConstraints`` is a subproperty of the ``AutoScalingPolicy`` property type.

            ``ScalingConstraints`` defines the upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activities triggered by automatic scaling rules will not cause an instance group to grow above or shrink below these limits.

            :param max_capacity: The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
            :param min_capacity: The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingconstraints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                scaling_constraints_property = emr.CfnInstanceGroupConfig.ScalingConstraintsProperty(
                    max_capacity=123,
                    min_capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6ff3b5d35320ac919544d56e90ea12239b9eb3d0d7419c51f8fb0d37bc989b5)
                check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
                check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_capacity": max_capacity,
                "min_capacity": min_capacity,
            }

        @builtins.property
        def max_capacity(self) -> jsii.Number:
            '''The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow.

            Scale-out activities will not add instances beyond this boundary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingconstraints.html#cfn-emr-instancegroupconfig-scalingconstraints-maxcapacity
            '''
            result = self._values.get("max_capacity")
            assert result is not None, "Required property 'max_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_capacity(self) -> jsii.Number:
            '''The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink.

            Scale-in activities will not terminate instances below this boundary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingconstraints.html#cfn-emr-instancegroupconfig-scalingconstraints-mincapacity
            '''
            result = self._values.get("min_capacity")
            assert result is not None, "Required property 'min_capacity' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingConstraintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.ScalingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "name": "name",
            "trigger": "trigger",
            "description": "description",
        },
    )
    class ScalingRuleProperty:
        def __init__(
            self,
            *,
            action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.ScalingActionProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            trigger: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.ScalingTriggerProperty", typing.Dict[builtins.str, typing.Any]]],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``ScalingRule`` is a subproperty of the ``AutoScalingPolicy`` property type.

            ``ScalingRule`` defines the scale-in or scale-out rules for scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

            :param action: The conditions that trigger an automatic scaling activity.
            :param name: The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
            :param trigger: The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
            :param description: A friendly, more verbose description of the automatic scaling rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                scaling_rule_property = emr.CfnInstanceGroupConfig.ScalingRuleProperty(
                    action=emr.CfnInstanceGroupConfig.ScalingActionProperty(
                        simple_scaling_policy_configuration=emr.CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty(
                            scaling_adjustment=123,
                
                            # the properties below are optional
                            adjustment_type="adjustmentType",
                            cool_down=123
                        ),
                
                        # the properties below are optional
                        market="market"
                    ),
                    name="name",
                    trigger=emr.CfnInstanceGroupConfig.ScalingTriggerProperty(
                        cloud_watch_alarm_definition=emr.CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty(
                            comparison_operator="comparisonOperator",
                            metric_name="metricName",
                            period=123,
                            threshold=123,
                
                            # the properties below are optional
                            dimensions=[emr.CfnInstanceGroupConfig.MetricDimensionProperty(
                                key="key",
                                value="value"
                            )],
                            evaluation_periods=123,
                            namespace="namespace",
                            statistic="statistic",
                            unit="unit"
                        )
                    ),
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e22fd5263f7ede9f4022ec6e5f459bb132aca11720ec7f0ee2967d60e7c1ba80)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "name": name,
                "trigger": trigger,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def action(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ScalingActionProperty"]:
            '''The conditions that trigger an automatic scaling activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingrule.html#cfn-emr-instancegroupconfig-scalingrule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ScalingActionProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name used to identify an automatic scaling rule.

            Rule names must be unique within a scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingrule.html#cfn-emr-instancegroupconfig-scalingrule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def trigger(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ScalingTriggerProperty"]:
            '''The CloudWatch alarm definition that determines when automatic scaling activity is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingrule.html#cfn-emr-instancegroupconfig-scalingrule-trigger
            '''
            result = self._values.get("trigger")
            assert result is not None, "Required property 'trigger' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.ScalingTriggerProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A friendly, more verbose description of the automatic scaling rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingrule.html#cfn-emr-instancegroupconfig-scalingrule-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.ScalingTriggerProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_alarm_definition": "cloudWatchAlarmDefinition"},
    )
    class ScalingTriggerProperty:
        def __init__(
            self,
            *,
            cloud_watch_alarm_definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''``ScalingTrigger`` is a subproperty of the ``ScalingRule`` property type.

            ``ScalingTrigger`` determines the conditions that trigger an automatic scaling activity.

            :param cloud_watch_alarm_definition: The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingtrigger.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                scaling_trigger_property = emr.CfnInstanceGroupConfig.ScalingTriggerProperty(
                    cloud_watch_alarm_definition=emr.CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty(
                        comparison_operator="comparisonOperator",
                        metric_name="metricName",
                        period=123,
                        threshold=123,
                
                        # the properties below are optional
                        dimensions=[emr.CfnInstanceGroupConfig.MetricDimensionProperty(
                            key="key",
                            value="value"
                        )],
                        evaluation_periods=123,
                        namespace="namespace",
                        statistic="statistic",
                        unit="unit"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5071bc066eda67f0957ff3f0cfffd8ee81b66fdad65755907ee755e7ac063c3d)
                check_type(argname="argument cloud_watch_alarm_definition", value=cloud_watch_alarm_definition, expected_type=type_hints["cloud_watch_alarm_definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_alarm_definition": cloud_watch_alarm_definition,
            }

        @builtins.property
        def cloud_watch_alarm_definition(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty"]:
            '''The definition of a CloudWatch metric alarm.

            When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-scalingtrigger.html#cfn-emr-instancegroupconfig-scalingtrigger-cloudwatchalarmdefinition
            '''
            result = self._values.get("cloud_watch_alarm_definition")
            assert result is not None, "Required property 'cloud_watch_alarm_definition' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingTriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scaling_adjustment": "scalingAdjustment",
            "adjustment_type": "adjustmentType",
            "cool_down": "coolDown",
        },
    )
    class SimpleScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            scaling_adjustment: jsii.Number,
            adjustment_type: typing.Optional[builtins.str] = None,
            cool_down: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``SimpleScalingPolicyConfiguration`` is a subproperty of the ``ScalingAction`` property type.

            ``SimpleScalingPolicyConfiguration`` determines how an automatic scaling action adds or removes instances, the cooldown period, and the number of EC2 instances that are added each time the CloudWatch metric alarm condition is satisfied.

            :param scaling_adjustment: The amount by which to scale in or scale out, based on the specified ``AdjustmentType`` . A positive value adds to the instance group's Amazon EC2 instance count while a negative number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the number should only be a positive integer. If ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.
            :param adjustment_type: The way in which Amazon EC2 instances are added (if ``ScalingAdjustment`` is a positive number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default. ``CHANGE_IN_CAPACITY`` indicates that the Amazon EC2 instance count increments or decrements by ``ScalingAdjustment`` , which should be expressed as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by the percentage specified by ``ScalingAdjustment`` , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by ``ScalingAdjustment`` , which should be expressed as a positive integer.
            :param cool_down: The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                simple_scaling_policy_configuration_property = emr.CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty(
                    scaling_adjustment=123,
                
                    # the properties below are optional
                    adjustment_type="adjustmentType",
                    cool_down=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6268a4e2bfec2bdc60b96553635aab203a6017b3189fca1955213d254af9194c)
                check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
                check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
                check_type(argname="argument cool_down", value=cool_down, expected_type=type_hints["cool_down"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "scaling_adjustment": scaling_adjustment,
            }
            if adjustment_type is not None:
                self._values["adjustment_type"] = adjustment_type
            if cool_down is not None:
                self._values["cool_down"] = cool_down

        @builtins.property
        def scaling_adjustment(self) -> jsii.Number:
            '''The amount by which to scale in or scale out, based on the specified ``AdjustmentType`` .

            A positive value adds to the instance group's Amazon EC2 instance count while a negative number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the number should only be a positive integer. If ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            assert result is not None, "Required property 'scaling_adjustment' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def adjustment_type(self) -> typing.Optional[builtins.str]:
            '''The way in which Amazon EC2 instances are added (if ``ScalingAdjustment`` is a positive number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the scaling activity is triggered.

            ``CHANGE_IN_CAPACITY`` is the default. ``CHANGE_IN_CAPACITY`` indicates that the Amazon EC2 instance count increments or decrements by ``ScalingAdjustment`` , which should be expressed as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by the percentage specified by ``ScalingAdjustment`` , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by ``ScalingAdjustment`` , which should be expressed as a positive integer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-adjustmenttype
            '''
            result = self._values.get("adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cool_down(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start.

            The default value is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-cooldown
            '''
            result = self._values.get("cool_down")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SimpleScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfig.VolumeSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "size_in_gb": "sizeInGb",
            "volume_type": "volumeType",
            "iops": "iops",
            "throughput": "throughput",
        },
    )
    class VolumeSpecificationProperty:
        def __init__(
            self,
            *,
            size_in_gb: jsii.Number,
            volume_type: builtins.str,
            iops: typing.Optional[jsii.Number] = None,
            throughput: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``VolumeSpecification`` is a subproperty of the ``EbsBlockDeviceConfig`` property type.

            ``VolumeSecification`` determines the volume type, IOPS, and size (GiB) for EBS volumes attached to EC2 instances.

            :param size_in_gb: The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            :param volume_type: The volume type. Volume types supported are gp3, gp2, io1, st1, sc1, and standard.
            :param iops: The number of I/O operations per second (IOPS) that the volume supports.
            :param throughput: The throughput, in mebibyte per second (MiB/s). This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-volumespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                volume_specification_property = emr.CfnInstanceGroupConfig.VolumeSpecificationProperty(
                    size_in_gb=123,
                    volume_type="volumeType",
                
                    # the properties below are optional
                    iops=123,
                    throughput=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__243316d3b741ddf8c20750398e178fdc490d62e22eb2efacb27623b9fd5ad95c)
                check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "size_in_gb": size_in_gb,
                "volume_type": volume_type,
            }
            if iops is not None:
                self._values["iops"] = iops
            if throughput is not None:
                self._values["throughput"] = throughput

        @builtins.property
        def size_in_gb(self) -> jsii.Number:
            '''The volume size, in gibibytes (GiB).

            This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-volumespecification.html#cfn-emr-instancegroupconfig-volumespecification-sizeingb
            '''
            result = self._values.get("size_in_gb")
            assert result is not None, "Required property 'size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_type(self) -> builtins.str:
            '''The volume type.

            Volume types supported are gp3, gp2, io1, st1, sc1, and standard.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-volumespecification.html#cfn-emr-instancegroupconfig-volumespecification-volumetype
            '''
            result = self._values.get("volume_type")
            assert result is not None, "Required property 'volume_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The number of I/O operations per second (IOPS) that the volume supports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-volumespecification.html#cfn-emr-instancegroupconfig-volumespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''The throughput, in mebibyte per second (MiB/s).

            This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-instancegroupconfig-volumespecification.html#cfn-emr-instancegroupconfig-volumespecification-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emr.CfnInstanceGroupConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_count": "instanceCount",
        "instance_role": "instanceRole",
        "instance_type": "instanceType",
        "job_flow_id": "jobFlowId",
        "auto_scaling_policy": "autoScalingPolicy",
        "bid_price": "bidPrice",
        "configurations": "configurations",
        "custom_ami_id": "customAmiId",
        "ebs_configuration": "ebsConfiguration",
        "market": "market",
        "name": "name",
    },
)
class CfnInstanceGroupConfigProps:
    def __init__(
        self,
        *,
        instance_count: jsii.Number,
        instance_role: builtins.str,
        instance_type: builtins.str,
        job_flow_id: builtins.str,
        auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        bid_price: typing.Optional[builtins.str] = None,
        configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.EbsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        market: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceGroupConfig``.

        :param instance_count: Target number of instances for the instance group.
        :param instance_role: The role of the instance group in the cluster. *Allowed Values* : TASK
        :param instance_type: The Amazon EC2 instance type for all instances in the instance group.
        :param job_flow_id: The ID of an Amazon EMR cluster that you want to associate this instance group with.
        :param auto_scaling_policy: ``AutoScalingPolicy`` is a subproperty of ``InstanceGroupConfig`` . ``AutoScalingPolicy`` defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. For more information, see `Using Automatic Scaling in Amazon EMR <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-automatic-scaling.html>`_ in the *Amazon EMR Management Guide* .
        :param bid_price: If specified, indicates that the instance group uses Spot Instances. This is the maximum price you are willing to pay for Spot Instances. Specify ``OnDemandPrice`` to set the amount equal to the On-Demand price, or specify an amount in USD.
        :param configurations: .. epigraph:: Amazon EMR releases 4.x or later. The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).
        :param custom_ami_id: The custom AMI ID to use for the provisioned instance group.
        :param ebs_configuration: ``EbsConfiguration`` determines the EBS volumes to attach to EMR cluster instances.
        :param market: Market type of the Amazon EC2 instances used to create a cluster node.
        :param name: Friendly name given to the instance group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emr as emr
            
            # configuration_property_: emr.CfnInstanceGroupConfig.ConfigurationProperty
            
            cfn_instance_group_config_props = emr.CfnInstanceGroupConfigProps(
                instance_count=123,
                instance_role="instanceRole",
                instance_type="instanceType",
                job_flow_id="jobFlowId",
            
                # the properties below are optional
                auto_scaling_policy=emr.CfnInstanceGroupConfig.AutoScalingPolicyProperty(
                    constraints=emr.CfnInstanceGroupConfig.ScalingConstraintsProperty(
                        max_capacity=123,
                        min_capacity=123
                    ),
                    rules=[emr.CfnInstanceGroupConfig.ScalingRuleProperty(
                        action=emr.CfnInstanceGroupConfig.ScalingActionProperty(
                            simple_scaling_policy_configuration=emr.CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty(
                                scaling_adjustment=123,
            
                                # the properties below are optional
                                adjustment_type="adjustmentType",
                                cool_down=123
                            ),
            
                            # the properties below are optional
                            market="market"
                        ),
                        name="name",
                        trigger=emr.CfnInstanceGroupConfig.ScalingTriggerProperty(
                            cloud_watch_alarm_definition=emr.CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty(
                                comparison_operator="comparisonOperator",
                                metric_name="metricName",
                                period=123,
                                threshold=123,
            
                                # the properties below are optional
                                dimensions=[emr.CfnInstanceGroupConfig.MetricDimensionProperty(
                                    key="key",
                                    value="value"
                                )],
                                evaluation_periods=123,
                                namespace="namespace",
                                statistic="statistic",
                                unit="unit"
                            )
                        ),
            
                        # the properties below are optional
                        description="description"
                    )]
                ),
                bid_price="bidPrice",
                configurations=[emr.CfnInstanceGroupConfig.ConfigurationProperty(
                    classification="classification",
                    configuration_properties={
                        "configuration_properties_key": "configurationProperties"
                    },
                    configurations=[configuration_property_]
                )],
                custom_ami_id="customAmiId",
                ebs_configuration=emr.CfnInstanceGroupConfig.EbsConfigurationProperty(
                    ebs_block_device_configs=[emr.CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty(
                        volume_specification=emr.CfnInstanceGroupConfig.VolumeSpecificationProperty(
                            size_in_gb=123,
                            volume_type="volumeType",
            
                            # the properties below are optional
                            iops=123,
                            throughput=123
                        ),
            
                        # the properties below are optional
                        volumes_per_instance=123
                    )],
                    ebs_optimized=False
                ),
                market="market",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9a4a8b0692b3ed59bf418552ec7f58ae67ef7b9ad41b00ecca1de4f841b4f5f)
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument instance_role", value=instance_role, expected_type=type_hints["instance_role"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument job_flow_id", value=job_flow_id, expected_type=type_hints["job_flow_id"])
            check_type(argname="argument auto_scaling_policy", value=auto_scaling_policy, expected_type=type_hints["auto_scaling_policy"])
            check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
            check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            check_type(argname="argument custom_ami_id", value=custom_ami_id, expected_type=type_hints["custom_ami_id"])
            check_type(argname="argument ebs_configuration", value=ebs_configuration, expected_type=type_hints["ebs_configuration"])
            check_type(argname="argument market", value=market, expected_type=type_hints["market"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_count": instance_count,
            "instance_role": instance_role,
            "instance_type": instance_type,
            "job_flow_id": job_flow_id,
        }
        if auto_scaling_policy is not None:
            self._values["auto_scaling_policy"] = auto_scaling_policy
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if configurations is not None:
            self._values["configurations"] = configurations
        if custom_ami_id is not None:
            self._values["custom_ami_id"] = custom_ami_id
        if ebs_configuration is not None:
            self._values["ebs_configuration"] = ebs_configuration
        if market is not None:
            self._values["market"] = market
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def instance_count(self) -> jsii.Number:
        '''Target number of instances for the instance group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancecount
        '''
        result = self._values.get("instance_count")
        assert result is not None, "Required property 'instance_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance_role(self) -> builtins.str:
        '''The role of the instance group in the cluster.

        *Allowed Values* : TASK

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancerole
        '''
        result = self._values.get("instance_role")
        assert result is not None, "Required property 'instance_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''The Amazon EC2 instance type for all instances in the instance group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_flow_id(self) -> builtins.str:
        '''The ID of an Amazon EMR cluster that you want to associate this instance group with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-jobflowid
        '''
        result = self._values.get("job_flow_id")
        assert result is not None, "Required property 'job_flow_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.AutoScalingPolicyProperty]]:
        '''``AutoScalingPolicy`` is a subproperty of ``InstanceGroupConfig`` .

        ``AutoScalingPolicy`` defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. For more information, see `Using Automatic Scaling in Amazon EMR <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-automatic-scaling.html>`_ in the *Amazon EMR Management Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-autoscalingpolicy
        '''
        result = self._values.get("auto_scaling_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.AutoScalingPolicyProperty]], result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''If specified, indicates that the instance group uses Spot Instances.

        This is the maximum price you are willing to pay for Spot Instances. Specify ``OnDemandPrice`` to set the amount equal to the On-Demand price, or specify an amount in USD.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-bidprice
        '''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.ConfigurationProperty]]]]:
        '''.. epigraph::

   Amazon EMR releases 4.x or later.

        The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-configurations
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.ConfigurationProperty]]]], result)

    @builtins.property
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''The custom AMI ID to use for the provisioned instance group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-customamiid
        '''
        result = self._values.get("custom_ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.EbsConfigurationProperty]]:
        '''``EbsConfiguration`` determines the EBS volumes to attach to EMR cluster instances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-ebsconfiguration
        '''
        result = self._values.get("ebs_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.EbsConfigurationProperty]], result)

    @builtins.property
    def market(self) -> typing.Optional[builtins.str]:
        '''Market type of the Amazon EC2 instances used to create a cluster node.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-market
        '''
        result = self._values.get("market")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Friendly name given to the instance group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceGroupConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSecurityConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emr.CfnSecurityConfiguration",
):
    '''Use a ``SecurityConfiguration`` resource to configure data encryption, Kerberos authentication (available in Amazon EMR release version 5.10.0 and later), and Amazon S3 authorization for EMRFS (available in EMR 5.10.0 and later). You can re-use a security configuration for any number of clusters in your account. For more information and example security configuration JSON objects, see `Create a Security Configuration <https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-create-security-configuration.html>`_ in the *Amazon EMR Management Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html
    :cloudformationResource: AWS::EMR::SecurityConfiguration
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_emr as emr
        
        
        cfn_security_configuration = emr.CfnSecurityConfiguration(self, "EmrSecurityConfiguration",
            name="AddStepRuntimeRoleSecConfig",
            security_configuration=JSON.parse("""
                    {
                      "AuthorizationConfiguration": {
                          "IAMConfiguration": {
                              "EnableApplicationScopedIAMRole": true,
                              "ApplicationScopedIAMRoleConfiguration":
                                  {
                                      "PropagateSourceIdentity": true
                                  }
                          },
                          "LakeFormationConfiguration": {
                              "AuthorizedSessionTagValue": "Amazon EMR"
                          }
                      }
                    }""")
        )
        
        task = tasks.EmrCreateCluster(self, "Create Cluster",
            instances=tasks.EmrCreateCluster.InstancesConfigProperty(),
            name=sfn.TaskInput.from_json_path_at("$.ClusterName").value,
            security_configuration=cfn_security_configuration.name
        )
        
        execution_role = iam.Role(self, "Role",
            assumed_by=iam.ArnPrincipal(task.cluster_role.role_arn)
        )
        
        execution_role.assume_role_policy.add_statements(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                principals=[task.cluster_role
                ],
                actions=["sts:SetSourceIdentity"
                ]
            ),
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                principals=[task.cluster_role
                ],
                actions=["sts:TagSession"
                ],
                conditions={
                    "StringEquals": {
                        "aws:RequestTag/LakeFormationAuthorizedCaller": "Amazon EMR"
                    }
                }
            ))
        
        tasks.EmrAddStep(self, "Task",
            cluster_id="ClusterId",
            execution_role_arn=execution_role.role_arn,
            name="StepName",
            jar="Jar",
            action_on_failure=tasks.ActionOnFailure.CONTINUE
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        security_configuration: typing.Any,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_configuration: The security configuration details in JSON format.
        :param name: The name of the security configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1cd635a9a933efd41bee8e26ecb06319993c2aa7e459d0f829c5f4dfc58cfd3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityConfigurationProps(
            security_configuration=security_configuration, name=name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da2a55d9947c59bcec537c0802a40401320b5d449dfc60b08045fa36fb13f4ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c082b9ccfa1abd822893594a5e87725508bfea7dc1f24c5da500060202b08e9)
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
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> typing.Any:
        '''The security configuration details in JSON format.'''
        return typing.cast(typing.Any, jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7354895da5b819c64c60ddab0fd091d5bb8338e636d169481d06071803d0542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63794c5d363b5670a95b0dc55f674f81972d2ee1de87f02f8020599aecac3fef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emr.CfnSecurityConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"security_configuration": "securityConfiguration", "name": "name"},
)
class CfnSecurityConfigurationProps:
    def __init__(
        self,
        *,
        security_configuration: typing.Any,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityConfiguration``.

        :param security_configuration: The security configuration details in JSON format.
        :param name: The name of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_emr as emr
            
            
            cfn_security_configuration = emr.CfnSecurityConfiguration(self, "EmrSecurityConfiguration",
                name="AddStepRuntimeRoleSecConfig",
                security_configuration=JSON.parse("""
                        {
                          "AuthorizationConfiguration": {
                              "IAMConfiguration": {
                                  "EnableApplicationScopedIAMRole": true,
                                  "ApplicationScopedIAMRoleConfiguration":
                                      {
                                          "PropagateSourceIdentity": true
                                      }
                              },
                              "LakeFormationConfiguration": {
                                  "AuthorizedSessionTagValue": "Amazon EMR"
                              }
                          }
                        }""")
            )
            
            task = tasks.EmrCreateCluster(self, "Create Cluster",
                instances=tasks.EmrCreateCluster.InstancesConfigProperty(),
                name=sfn.TaskInput.from_json_path_at("$.ClusterName").value,
                security_configuration=cfn_security_configuration.name
            )
            
            execution_role = iam.Role(self, "Role",
                assumed_by=iam.ArnPrincipal(task.cluster_role.role_arn)
            )
            
            execution_role.assume_role_policy.add_statements(
                iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    principals=[task.cluster_role
                    ],
                    actions=["sts:SetSourceIdentity"
                    ]
                ),
                iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    principals=[task.cluster_role
                    ],
                    actions=["sts:TagSession"
                    ],
                    conditions={
                        "StringEquals": {
                            "aws:RequestTag/LakeFormationAuthorizedCaller": "Amazon EMR"
                        }
                    }
                ))
            
            tasks.EmrAddStep(self, "Task",
                cluster_id="ClusterId",
                execution_role_arn=execution_role.role_arn,
                name="StepName",
                jar="Jar",
                action_on_failure=tasks.ActionOnFailure.CONTINUE
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__570e3d1d3bfab50b7c899148aae497fe36ce7f411f3a6bce1adbda62b5b3610d)
            check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_configuration": security_configuration,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def security_configuration(self) -> typing.Any:
        '''The security configuration details in JSON format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-securityconfiguration
        '''
        result = self._values.get("security_configuration")
        assert result is not None, "Required property 'security_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStep(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emr.CfnStep",
):
    '''Use ``Step`` to specify a cluster (job flow) step, which runs only on the master node.

    Steps are used to submit data processing jobs to a cluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html
    :cloudformationResource: AWS::EMR::Step
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emr as emr
        
        cfn_step = emr.CfnStep(self, "MyCfnStep",
            action_on_failure="actionOnFailure",
            hadoop_jar_step=emr.CfnStep.HadoopJarStepConfigProperty(
                jar="jar",
        
                # the properties below are optional
                args=["args"],
                main_class="mainClass",
                step_properties=[emr.CfnStep.KeyValueProperty(
                    key="key",
                    value="value"
                )]
            ),
            job_flow_id="jobFlowId",
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        action_on_failure: builtins.str,
        hadoop_jar_step: typing.Union[_IResolvable_da3f097b, typing.Union["CfnStep.HadoopJarStepConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        job_flow_id: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action_on_failure: This specifies what action to take when the cluster step fails. Possible values are ``CANCEL_AND_WAIT`` and ``CONTINUE`` .
        :param hadoop_jar_step: The ``HadoopJarStepConfig`` property type specifies a job flow step consisting of a JAR file whose main function will be executed. The main function submits a job for the cluster to execute as a step on the master node, and then waits for the job to finish or fail before executing subsequent steps.
        :param job_flow_id: A string that uniquely identifies the cluster (job flow).
        :param name: The name of the cluster step.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56108bb804f44dbb5230a71c020ff2994411f1d5f6f4226d7d5f948d62af211e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStepProps(
            action_on_failure=action_on_failure,
            hadoop_jar_step=hadoop_jar_step,
            job_flow_id=job_flow_id,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78d97da37e72bd1bfccd5d003f6661e19aad059f59b1713075323b6ecf0eaa3d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d849d8f81968063aa29a34df211088e584a4a24f713c36ff0a67515ffe9ba8c)
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
        '''The identifier of the cluster step.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="actionOnFailure")
    def action_on_failure(self) -> builtins.str:
        '''This specifies what action to take when the cluster step fails.'''
        return typing.cast(builtins.str, jsii.get(self, "actionOnFailure"))

    @action_on_failure.setter
    def action_on_failure(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8246842b6fd3a6be5c74b6bfbc1bdfc328b214cf32fb8108cc06cf5793ea2a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionOnFailure", value)

    @builtins.property
    @jsii.member(jsii_name="hadoopJarStep")
    def hadoop_jar_step(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnStep.HadoopJarStepConfigProperty"]:
        '''The ``HadoopJarStepConfig`` property type specifies a job flow step consisting of a JAR file whose main function will be executed.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnStep.HadoopJarStepConfigProperty"], jsii.get(self, "hadoopJarStep"))

    @hadoop_jar_step.setter
    def hadoop_jar_step(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnStep.HadoopJarStepConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ec64ae90b5233e23c51213eae7a3c1c03f9b635bef0f8e61032198c670bc9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hadoopJarStep", value)

    @builtins.property
    @jsii.member(jsii_name="jobFlowId")
    def job_flow_id(self) -> builtins.str:
        '''A string that uniquely identifies the cluster (job flow).'''
        return typing.cast(builtins.str, jsii.get(self, "jobFlowId"))

    @job_flow_id.setter
    def job_flow_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99aff04b3096ab830115c2e81c573c3777b7b1cd6b5ba49de734510fe54bd41f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobFlowId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the cluster step.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c3d15d09a73ee52be1d687a48f7a81900a69ccc44fb1cabb8a54adfa580c22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnStep.HadoopJarStepConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "jar": "jar",
            "args": "args",
            "main_class": "mainClass",
            "step_properties": "stepProperties",
        },
    )
    class HadoopJarStepConfigProperty:
        def __init__(
            self,
            *,
            jar: builtins.str,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
            main_class: typing.Optional[builtins.str] = None,
            step_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStep.KeyValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A job flow step consisting of a JAR file whose main function will be executed.

            The main function submits a job for Hadoop to execute and waits for the job to finish or fail.

            :param jar: A path to a JAR file run during the step.
            :param args: A list of command line arguments passed to the JAR file's main function when executed.
            :param main_class: The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
            :param step_properties: A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                hadoop_jar_step_config_property = emr.CfnStep.HadoopJarStepConfigProperty(
                    jar="jar",
                
                    # the properties below are optional
                    args=["args"],
                    main_class="mainClass",
                    step_properties=[emr.CfnStep.KeyValueProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__17116dab64c1f998800a3972016d6de90f0339e27d783be01c9aa002d894436e)
                check_type(argname="argument jar", value=jar, expected_type=type_hints["jar"])
                check_type(argname="argument args", value=args, expected_type=type_hints["args"])
                check_type(argname="argument main_class", value=main_class, expected_type=type_hints["main_class"])
                check_type(argname="argument step_properties", value=step_properties, expected_type=type_hints["step_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "jar": jar,
            }
            if args is not None:
                self._values["args"] = args
            if main_class is not None:
                self._values["main_class"] = main_class
            if step_properties is not None:
                self._values["step_properties"] = step_properties

        @builtins.property
        def jar(self) -> builtins.str:
            '''A path to a JAR file run during the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html#cfn-emr-step-hadoopjarstepconfig-jar
            '''
            result = self._values.get("jar")
            assert result is not None, "Required property 'jar' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of command line arguments passed to the JAR file's main function when executed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html#cfn-emr-step-hadoopjarstepconfig-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def main_class(self) -> typing.Optional[builtins.str]:
            '''The name of the main class in the specified Java file.

            If not specified, the JAR file should specify a Main-Class in its manifest file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html#cfn-emr-step-hadoopjarstepconfig-mainclass
            '''
            result = self._values.get("main_class")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def step_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStep.KeyValueProperty"]]]]:
            '''A list of Java properties that are set when the step runs.

            You can use these properties to pass key value pairs to your main function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-hadoopjarstepconfig.html#cfn-emr-step-hadoopjarstepconfig-stepproperties
            '''
            result = self._values.get("step_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStep.KeyValueProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HadoopJarStepConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emr.CfnStep.KeyValueProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class KeyValueProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``KeyValue`` is a subproperty of the ``HadoopJarStepConfig`` property type.

            ``KeyValue`` is used to pass parameters to a step.

            :param key: The unique identifier of a key-value pair.
            :param value: The value part of the identified key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-keyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emr as emr
                
                key_value_property = emr.CfnStep.KeyValueProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c45d46cddf4cc72fa52f0b95e0f250b3363c3d0ca8542a73ce888bcefb498379)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-keyvalue.html#cfn-emr-step-keyvalue-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value part of the identified key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-step-keyvalue.html#cfn-emr-step-keyvalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emr.CfnStepProps",
    jsii_struct_bases=[],
    name_mapping={
        "action_on_failure": "actionOnFailure",
        "hadoop_jar_step": "hadoopJarStep",
        "job_flow_id": "jobFlowId",
        "name": "name",
    },
)
class CfnStepProps:
    def __init__(
        self,
        *,
        action_on_failure: builtins.str,
        hadoop_jar_step: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStep.HadoopJarStepConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        job_flow_id: builtins.str,
        name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnStep``.

        :param action_on_failure: This specifies what action to take when the cluster step fails. Possible values are ``CANCEL_AND_WAIT`` and ``CONTINUE`` .
        :param hadoop_jar_step: The ``HadoopJarStepConfig`` property type specifies a job flow step consisting of a JAR file whose main function will be executed. The main function submits a job for the cluster to execute as a step on the master node, and then waits for the job to finish or fail before executing subsequent steps.
        :param job_flow_id: A string that uniquely identifies the cluster (job flow).
        :param name: The name of the cluster step.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emr as emr
            
            cfn_step_props = emr.CfnStepProps(
                action_on_failure="actionOnFailure",
                hadoop_jar_step=emr.CfnStep.HadoopJarStepConfigProperty(
                    jar="jar",
            
                    # the properties below are optional
                    args=["args"],
                    main_class="mainClass",
                    step_properties=[emr.CfnStep.KeyValueProperty(
                        key="key",
                        value="value"
                    )]
                ),
                job_flow_id="jobFlowId",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2487faa6f9278ced3b5fd2fab8e549b354a836990eb23096f7fd91d5e28230d)
            check_type(argname="argument action_on_failure", value=action_on_failure, expected_type=type_hints["action_on_failure"])
            check_type(argname="argument hadoop_jar_step", value=hadoop_jar_step, expected_type=type_hints["hadoop_jar_step"])
            check_type(argname="argument job_flow_id", value=job_flow_id, expected_type=type_hints["job_flow_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_on_failure": action_on_failure,
            "hadoop_jar_step": hadoop_jar_step,
            "job_flow_id": job_flow_id,
            "name": name,
        }

    @builtins.property
    def action_on_failure(self) -> builtins.str:
        '''This specifies what action to take when the cluster step fails.

        Possible values are ``CANCEL_AND_WAIT`` and ``CONTINUE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-emr-step-actiononfailure
        '''
        result = self._values.get("action_on_failure")
        assert result is not None, "Required property 'action_on_failure' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hadoop_jar_step(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnStep.HadoopJarStepConfigProperty]:
        '''The ``HadoopJarStepConfig`` property type specifies a job flow step consisting of a JAR file whose main function will be executed.

        The main function submits a job for the cluster to execute as a step on the master node, and then waits for the job to finish or fail before executing subsequent steps.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-emr-step-hadoopjarstep
        '''
        result = self._values.get("hadoop_jar_step")
        assert result is not None, "Required property 'hadoop_jar_step' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnStep.HadoopJarStepConfigProperty], result)

    @builtins.property
    def job_flow_id(self) -> builtins.str:
        '''A string that uniquely identifies the cluster (job flow).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-emr-step-jobflowid
        '''
        result = self._values.get("job_flow_id")
        assert result is not None, "Required property 'job_flow_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the cluster step.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-emr-step-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStepProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStudio(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emr.CfnStudio",
):
    '''The ``AWS::EMR::Studio`` resource specifies an Amazon EMR Studio.

    An EMR Studio is a web-based, integrated development environment for fully managed Jupyter notebooks that run on Amazon EMR clusters. For more information, see the `*Amazon EMR Management Guide* <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html
    :cloudformationResource: AWS::EMR::Studio
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emr as emr
        
        cfn_studio = emr.CfnStudio(self, "MyCfnStudio",
            auth_mode="authMode",
            default_s3_location="defaultS3Location",
            engine_security_group_id="engineSecurityGroupId",
            name="name",
            service_role="serviceRole",
            subnet_ids=["subnetIds"],
            vpc_id="vpcId",
            workspace_security_group_id="workspaceSecurityGroupId",
        
            # the properties below are optional
            description="description",
            encryption_key_arn="encryptionKeyArn",
            idc_instance_arn="idcInstanceArn",
            idc_user_assignment="idcUserAssignment",
            idp_auth_url="idpAuthUrl",
            idp_relay_state_parameter_name="idpRelayStateParameterName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trusted_identity_propagation_enabled=False,
            user_role="userRole"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        auth_mode: builtins.str,
        default_s3_location: builtins.str,
        engine_security_group_id: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        workspace_security_group_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        idc_instance_arn: typing.Optional[builtins.str] = None,
        idc_user_assignment: typing.Optional[builtins.str] = None,
        idp_auth_url: typing.Optional[builtins.str] = None,
        idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trusted_identity_propagation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        user_role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auth_mode: Specifies whether the Studio authenticates users using IAM Identity Center or IAM.
        :param default_s3_location: The Amazon S3 location to back up EMR Studio Workspaces and notebook files.
        :param engine_security_group_id: The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by ``VpcId`` .
        :param name: A descriptive name for the Amazon EMR Studio.
        :param service_role: The Amazon Resource Name (ARN) of the IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.
        :param subnet_ids: A list of subnet IDs to associate with the Amazon EMR Studio. A Studio can have a maximum of 5 subnets. The subnets must belong to the VPC specified by ``VpcId`` . Studio users can create a Workspace in any of the specified subnets.
        :param vpc_id: The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.
        :param workspace_security_group_id: The ID of the Workspace security group associated with the Amazon EMR Studio. The Workspace security group allows outbound network traffic to resources in the Engine security group and to the internet.
        :param description: A detailed description of the Amazon EMR Studio.
        :param encryption_key_arn: The AWS KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.
        :param idc_instance_arn: The ARN of the IAM Identity Center instance the Studio application belongs to.
        :param idc_user_assignment: Indicates whether the Studio has ``REQUIRED`` or ``OPTIONAL`` IAM Identity Center user assignment. If the value is set to ``REQUIRED`` , users must be explicitly assigned to the Studio application to access the Studio.
        :param idp_auth_url: Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.
        :param idp_relay_state_parameter_name: The name of your identity provider's ``RelayState`` parameter.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param trusted_identity_propagation_enabled: Indicates whether the Studio has Trusted identity propagation enabled. The default value is ``false`` .
        :param user_role: The Amazon Resource Name (ARN) of the IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies. You only need to specify ``UserRole`` when you set ``AuthMode`` to ``SSO`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5fa63dd56ed829e4898f84009809f50f4125ac18a4dd04d1928420267568a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStudioProps(
            auth_mode=auth_mode,
            default_s3_location=default_s3_location,
            engine_security_group_id=engine_security_group_id,
            name=name,
            service_role=service_role,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            workspace_security_group_id=workspace_security_group_id,
            description=description,
            encryption_key_arn=encryption_key_arn,
            idc_instance_arn=idc_instance_arn,
            idc_user_assignment=idc_user_assignment,
            idp_auth_url=idp_auth_url,
            idp_relay_state_parameter_name=idp_relay_state_parameter_name,
            tags=tags,
            trusted_identity_propagation_enabled=trusted_identity_propagation_enabled,
            user_role=user_role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12811625403d85ab8e027c82784f88c03aadb1a85e1a21e6db4a277a59011534)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ff2c045eee2499998e72b32d6123b1b4b00a854ea2337ba6394499ce8db13a7)
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
        '''The Amazon Resource Name (ARN) of the Amazon EMR Studio.

        For example: ``arn:aws:elasticmapreduce:us-east-1:653XXXXXXXXX:studio/es-EXAMPLE12345678XXXXXXXXXXX`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStudioId")
    def attr_studio_id(self) -> builtins.str:
        '''The ID of the Amazon EMR Studio.

        For example: ``es-EXAMPLE12345678XXXXXXXXXXX`` .

        :cloudformationAttribute: StudioId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStudioId"))

    @builtins.property
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''The unique access URL of the Amazon EMR Studio.

        For example: ``https://es-EXAMPLE12345678XXXXXXXXXXX.emrstudio-prod.us-east-1.amazonaws.com`` .

        :cloudformationAttribute: Url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

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
    @jsii.member(jsii_name="authMode")
    def auth_mode(self) -> builtins.str:
        '''Specifies whether the Studio authenticates users using IAM Identity Center or IAM.'''
        return typing.cast(builtins.str, jsii.get(self, "authMode"))

    @auth_mode.setter
    def auth_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29b15ad22555e04d2d23005c30126435e4966620a2c12755f0b0fdd6726aa11e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMode", value)

    @builtins.property
    @jsii.member(jsii_name="defaultS3Location")
    def default_s3_location(self) -> builtins.str:
        '''The Amazon S3 location to back up EMR Studio Workspaces and notebook files.'''
        return typing.cast(builtins.str, jsii.get(self, "defaultS3Location"))

    @default_s3_location.setter
    def default_s3_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbb47bd6bd91d8355415cdc4cfdba08f13b080cf9846d2422d09e8b62265748c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="engineSecurityGroupId")
    def engine_security_group_id(self) -> builtins.str:
        '''The ID of the Amazon EMR Studio Engine security group.'''
        return typing.cast(builtins.str, jsii.get(self, "engineSecurityGroupId"))

    @engine_security_group_id.setter
    def engine_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90414b22e6e56647e9dbf693bbce0fdae1c28c236ecd929441a47f2d0f435d5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineSecurityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A descriptive name for the Amazon EMR Studio.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d52feab7f5ee099c16a0c05ed2b3e7cee18c472c41ac764589c397b620b299)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that will be assumed by the Amazon EMR Studio.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde7348c01a014ad19a7b3939357f0a15ad6204c8bfbe78489ef31850e579062)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''A list of subnet IDs to associate with the Amazon EMR Studio.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__838f9f7dee3119f5c14aec74fc776ee2d173f127e4c1405cf253a925c408ae27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e38a2a11b003b0f2c09b646ba28b0e59e56e5f4f7217dbedff8c6c3108b678f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> builtins.str:
        '''The ID of the Workspace security group associated with the Amazon EMR Studio.'''
        return typing.cast(builtins.str, jsii.get(self, "workspaceSecurityGroupId"))

    @workspace_security_group_id.setter
    def workspace_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6702095c850e5c6efc6f9b86ca71364b17fad2b801e0c3aa76a7482e99a295b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceSecurityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A detailed description of the Amazon EMR Studio.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b57cfedf6d1b9357fb99a22fb68853be1bf68349d342ae1b382a911a55e0a0e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyArn")
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyArn"))

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a934c05c196d0eda57d2ba0bd9c2811612942f47baa70b9def4583964bf21ef7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="idcInstanceArn")
    def idc_instance_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM Identity Center instance the Studio application belongs to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idcInstanceArn"))

    @idc_instance_arn.setter
    def idc_instance_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac14b0d933a01aa925ef079cc75e4ff2fb649c283f4c3356a21f14dae6f52d24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idcInstanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="idcUserAssignment")
    def idc_user_assignment(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the Studio has ``REQUIRED`` or ``OPTIONAL`` IAM Identity Center user assignment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idcUserAssignment"))

    @idc_user_assignment.setter
    def idc_user_assignment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96ab30aad484feea76068949481bec25db0a532494456bfbb1db494aebf3926)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idcUserAssignment", value)

    @builtins.property
    @jsii.member(jsii_name="idpAuthUrl")
    def idp_auth_url(self) -> typing.Optional[builtins.str]:
        '''Your identity provider's authentication endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpAuthUrl"))

    @idp_auth_url.setter
    def idp_auth_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bdf046decc7d9dcf4942916a9fd82f3ddf403adfc79905c187b32915e71a92e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpAuthUrl", value)

    @builtins.property
    @jsii.member(jsii_name="idpRelayStateParameterName")
    def idp_relay_state_parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of your identity provider's ``RelayState`` parameter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpRelayStateParameterName"))

    @idp_relay_state_parameter_name.setter
    def idp_relay_state_parameter_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1cfcbc2226f4548db4b1c3cdf608c158cf7718b53ca11e14bae09dd099353f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpRelayStateParameterName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93c87ee05567302bb00141c45d4f778440c0196380fbcf0ea86580e0f69c98ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="trustedIdentityPropagationEnabled")
    def trusted_identity_propagation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the Studio has Trusted identity propagation enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "trustedIdentityPropagationEnabled"))

    @trusted_identity_propagation_enabled.setter
    def trusted_identity_propagation_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d97a907912a2a6d42177e06668874b62f8bb494e07b5e9659287db646faa1236)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedIdentityPropagationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="userRole")
    def user_role(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM user role that will be assumed by users and groups logged in to a Studio.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userRole"))

    @user_role.setter
    def user_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4497b6d90d344f7cce9a12d862f813109f2ee695a175caef4ea9fba74f1175a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userRole", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emr.CfnStudioProps",
    jsii_struct_bases=[],
    name_mapping={
        "auth_mode": "authMode",
        "default_s3_location": "defaultS3Location",
        "engine_security_group_id": "engineSecurityGroupId",
        "name": "name",
        "service_role": "serviceRole",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "workspace_security_group_id": "workspaceSecurityGroupId",
        "description": "description",
        "encryption_key_arn": "encryptionKeyArn",
        "idc_instance_arn": "idcInstanceArn",
        "idc_user_assignment": "idcUserAssignment",
        "idp_auth_url": "idpAuthUrl",
        "idp_relay_state_parameter_name": "idpRelayStateParameterName",
        "tags": "tags",
        "trusted_identity_propagation_enabled": "trustedIdentityPropagationEnabled",
        "user_role": "userRole",
    },
)
class CfnStudioProps:
    def __init__(
        self,
        *,
        auth_mode: builtins.str,
        default_s3_location: builtins.str,
        engine_security_group_id: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        workspace_security_group_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        idc_instance_arn: typing.Optional[builtins.str] = None,
        idc_user_assignment: typing.Optional[builtins.str] = None,
        idp_auth_url: typing.Optional[builtins.str] = None,
        idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trusted_identity_propagation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        user_role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnStudio``.

        :param auth_mode: Specifies whether the Studio authenticates users using IAM Identity Center or IAM.
        :param default_s3_location: The Amazon S3 location to back up EMR Studio Workspaces and notebook files.
        :param engine_security_group_id: The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by ``VpcId`` .
        :param name: A descriptive name for the Amazon EMR Studio.
        :param service_role: The Amazon Resource Name (ARN) of the IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.
        :param subnet_ids: A list of subnet IDs to associate with the Amazon EMR Studio. A Studio can have a maximum of 5 subnets. The subnets must belong to the VPC specified by ``VpcId`` . Studio users can create a Workspace in any of the specified subnets.
        :param vpc_id: The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.
        :param workspace_security_group_id: The ID of the Workspace security group associated with the Amazon EMR Studio. The Workspace security group allows outbound network traffic to resources in the Engine security group and to the internet.
        :param description: A detailed description of the Amazon EMR Studio.
        :param encryption_key_arn: The AWS KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.
        :param idc_instance_arn: The ARN of the IAM Identity Center instance the Studio application belongs to.
        :param idc_user_assignment: Indicates whether the Studio has ``REQUIRED`` or ``OPTIONAL`` IAM Identity Center user assignment. If the value is set to ``REQUIRED`` , users must be explicitly assigned to the Studio application to access the Studio.
        :param idp_auth_url: Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.
        :param idp_relay_state_parameter_name: The name of your identity provider's ``RelayState`` parameter.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param trusted_identity_propagation_enabled: Indicates whether the Studio has Trusted identity propagation enabled. The default value is ``false`` .
        :param user_role: The Amazon Resource Name (ARN) of the IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies. You only need to specify ``UserRole`` when you set ``AuthMode`` to ``SSO`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emr as emr
            
            cfn_studio_props = emr.CfnStudioProps(
                auth_mode="authMode",
                default_s3_location="defaultS3Location",
                engine_security_group_id="engineSecurityGroupId",
                name="name",
                service_role="serviceRole",
                subnet_ids=["subnetIds"],
                vpc_id="vpcId",
                workspace_security_group_id="workspaceSecurityGroupId",
            
                # the properties below are optional
                description="description",
                encryption_key_arn="encryptionKeyArn",
                idc_instance_arn="idcInstanceArn",
                idc_user_assignment="idcUserAssignment",
                idp_auth_url="idpAuthUrl",
                idp_relay_state_parameter_name="idpRelayStateParameterName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trusted_identity_propagation_enabled=False,
                user_role="userRole"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e54f46221565a48807a50ddbb87f328aa43352455931a5089f5484c2263b30f4)
            check_type(argname="argument auth_mode", value=auth_mode, expected_type=type_hints["auth_mode"])
            check_type(argname="argument default_s3_location", value=default_s3_location, expected_type=type_hints["default_s3_location"])
            check_type(argname="argument engine_security_group_id", value=engine_security_group_id, expected_type=type_hints["engine_security_group_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument workspace_security_group_id", value=workspace_security_group_id, expected_type=type_hints["workspace_security_group_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
            check_type(argname="argument idc_instance_arn", value=idc_instance_arn, expected_type=type_hints["idc_instance_arn"])
            check_type(argname="argument idc_user_assignment", value=idc_user_assignment, expected_type=type_hints["idc_user_assignment"])
            check_type(argname="argument idp_auth_url", value=idp_auth_url, expected_type=type_hints["idp_auth_url"])
            check_type(argname="argument idp_relay_state_parameter_name", value=idp_relay_state_parameter_name, expected_type=type_hints["idp_relay_state_parameter_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trusted_identity_propagation_enabled", value=trusted_identity_propagation_enabled, expected_type=type_hints["trusted_identity_propagation_enabled"])
            check_type(argname="argument user_role", value=user_role, expected_type=type_hints["user_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_mode": auth_mode,
            "default_s3_location": default_s3_location,
            "engine_security_group_id": engine_security_group_id,
            "name": name,
            "service_role": service_role,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
            "workspace_security_group_id": workspace_security_group_id,
        }
        if description is not None:
            self._values["description"] = description
        if encryption_key_arn is not None:
            self._values["encryption_key_arn"] = encryption_key_arn
        if idc_instance_arn is not None:
            self._values["idc_instance_arn"] = idc_instance_arn
        if idc_user_assignment is not None:
            self._values["idc_user_assignment"] = idc_user_assignment
        if idp_auth_url is not None:
            self._values["idp_auth_url"] = idp_auth_url
        if idp_relay_state_parameter_name is not None:
            self._values["idp_relay_state_parameter_name"] = idp_relay_state_parameter_name
        if tags is not None:
            self._values["tags"] = tags
        if trusted_identity_propagation_enabled is not None:
            self._values["trusted_identity_propagation_enabled"] = trusted_identity_propagation_enabled
        if user_role is not None:
            self._values["user_role"] = user_role

    @builtins.property
    def auth_mode(self) -> builtins.str:
        '''Specifies whether the Studio authenticates users using IAM Identity Center or IAM.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-authmode
        '''
        result = self._values.get("auth_mode")
        assert result is not None, "Required property 'auth_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_s3_location(self) -> builtins.str:
        '''The Amazon S3 location to back up EMR Studio Workspaces and notebook files.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-defaults3location
        '''
        result = self._values.get("default_s3_location")
        assert result is not None, "Required property 'default_s3_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_security_group_id(self) -> builtins.str:
        '''The ID of the Amazon EMR Studio Engine security group.

        The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by ``VpcId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-enginesecuritygroupid
        '''
        result = self._values.get("engine_security_group_id")
        assert result is not None, "Required property 'engine_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive name for the Amazon EMR Studio.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that will be assumed by the Amazon EMR Studio.

        The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-servicerole
        '''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''A list of subnet IDs to associate with the Amazon EMR Studio.

        A Studio can have a maximum of 5 subnets. The subnets must belong to the VPC specified by ``VpcId`` . Studio users can create a Workspace in any of the specified subnets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_security_group_id(self) -> builtins.str:
        '''The ID of the Workspace security group associated with the Amazon EMR Studio.

        The Workspace security group allows outbound network traffic to resources in the Engine security group and to the internet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-workspacesecuritygroupid
        '''
        result = self._values.get("workspace_security_group_id")
        assert result is not None, "Required property 'workspace_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A detailed description of the Amazon EMR Studio.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-encryptionkeyarn
        '''
        result = self._values.get("encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idc_instance_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM Identity Center instance the Studio application belongs to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idcinstancearn
        '''
        result = self._values.get("idc_instance_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idc_user_assignment(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the Studio has ``REQUIRED`` or ``OPTIONAL`` IAM Identity Center user assignment.

        If the value is set to ``REQUIRED`` , users must be explicitly assigned to the Studio application to access the Studio.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idcuserassignment
        '''
        result = self._values.get("idc_user_assignment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_auth_url(self) -> typing.Optional[builtins.str]:
        '''Your identity provider's authentication endpoint.

        Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idpauthurl
        '''
        result = self._values.get("idp_auth_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_relay_state_parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of your identity provider's ``RelayState`` parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idprelaystateparametername
        '''
        result = self._values.get("idp_relay_state_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def trusted_identity_propagation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the Studio has Trusted identity propagation enabled.

        The default value is ``false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-trustedidentitypropagationenabled
        '''
        result = self._values.get("trusted_identity_propagation_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def user_role(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM user role that will be assumed by users and groups logged in to a Studio.

        The permissions attached to this IAM role can be scoped down for each user or group using session policies. You only need to specify ``UserRole`` when you set ``AuthMode`` to ``SSO`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-userrole
        '''
        result = self._values.get("user_role")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStudioProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStudioSessionMapping(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emr.CfnStudioSessionMapping",
):
    '''The ``AWS::EMR::StudioSessionMapping`` resource is an Amazon EMR resource type that maps a user or group to the Amazon EMR Studio specified by ``StudioId`` , and applies a session policy that defines Studio permissions for that user or group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html
    :cloudformationResource: AWS::EMR::StudioSessionMapping
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emr as emr
        
        cfn_studio_session_mapping = emr.CfnStudioSessionMapping(self, "MyCfnStudioSessionMapping",
            identity_name="identityName",
            identity_type="identityType",
            session_policy_arn="sessionPolicyArn",
            studio_id="studioId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        identity_name: builtins.str,
        identity_type: builtins.str,
        session_policy_arn: builtins.str,
        studio_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param identity_name: The name of the user or group. For more information, see `UserName <https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName>`_ and `DisplayName <https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName>`_ in the *IAM Identity Center Identity Store API Reference* .
        :param identity_type: Specifies whether the identity to map to the Amazon EMR Studio is a user or a group.
        :param session_policy_arn: The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group. Session policies refine Studio user permissions without the need to use multiple IAM user roles. For more information, see `Create an EMR Studio user role with session policies <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-user-role.html>`_ in the *Amazon EMR Management Guide* .
        :param studio_id: The ID of the Amazon EMR Studio to which the user or group will be mapped.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e47b505b0a4a624d7bbc7e6f0b97d1cb4bc72a6ca97f9fba72f1fd63a5544d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStudioSessionMappingProps(
            identity_name=identity_name,
            identity_type=identity_type,
            session_policy_arn=session_policy_arn,
            studio_id=studio_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__153edf7b110ebe9d0c9cd9ba4efa10acec007161e12e38d6e9b66a4f81fd64d0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adc7c9cb99a4061de76a53ac99eca669470f2c63506aa6313684786d25560afd)
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
    @jsii.member(jsii_name="identityName")
    def identity_name(self) -> builtins.str:
        '''The name of the user or group.'''
        return typing.cast(builtins.str, jsii.get(self, "identityName"))

    @identity_name.setter
    def identity_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5feea587008e0e1c0549b46859852be4a2ae481e639401abe2b886234153fc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityName", value)

    @builtins.property
    @jsii.member(jsii_name="identityType")
    def identity_type(self) -> builtins.str:
        '''Specifies whether the identity to map to the Amazon EMR Studio is a user or a group.'''
        return typing.cast(builtins.str, jsii.get(self, "identityType"))

    @identity_type.setter
    def identity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e7e1b5f29fb4ef82a3f45ccd1dc1210bfec29f167cd477284aa3b96257256b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityType", value)

    @builtins.property
    @jsii.member(jsii_name="sessionPolicyArn")
    def session_policy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group.'''
        return typing.cast(builtins.str, jsii.get(self, "sessionPolicyArn"))

    @session_policy_arn.setter
    def session_policy_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3859eb45dacb565c5ba65788173f464996ebc788e3cc6302de95fb0f00ef960)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionPolicyArn", value)

    @builtins.property
    @jsii.member(jsii_name="studioId")
    def studio_id(self) -> builtins.str:
        '''The ID of the Amazon EMR Studio to which the user or group will be mapped.'''
        return typing.cast(builtins.str, jsii.get(self, "studioId"))

    @studio_id.setter
    def studio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce585291954018d8d1dc1c7c090b303e853cefe2e95a5e5948014cb2d1a8f9a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "studioId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emr.CfnStudioSessionMappingProps",
    jsii_struct_bases=[],
    name_mapping={
        "identity_name": "identityName",
        "identity_type": "identityType",
        "session_policy_arn": "sessionPolicyArn",
        "studio_id": "studioId",
    },
)
class CfnStudioSessionMappingProps:
    def __init__(
        self,
        *,
        identity_name: builtins.str,
        identity_type: builtins.str,
        session_policy_arn: builtins.str,
        studio_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnStudioSessionMapping``.

        :param identity_name: The name of the user or group. For more information, see `UserName <https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName>`_ and `DisplayName <https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName>`_ in the *IAM Identity Center Identity Store API Reference* .
        :param identity_type: Specifies whether the identity to map to the Amazon EMR Studio is a user or a group.
        :param session_policy_arn: The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group. Session policies refine Studio user permissions without the need to use multiple IAM user roles. For more information, see `Create an EMR Studio user role with session policies <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-user-role.html>`_ in the *Amazon EMR Management Guide* .
        :param studio_id: The ID of the Amazon EMR Studio to which the user or group will be mapped.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emr as emr
            
            cfn_studio_session_mapping_props = emr.CfnStudioSessionMappingProps(
                identity_name="identityName",
                identity_type="identityType",
                session_policy_arn="sessionPolicyArn",
                studio_id="studioId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a27468aac05a78cc17d6ec5e8f062d7c22a5b3bf56f44d8c6c90edc8a69a63e8)
            check_type(argname="argument identity_name", value=identity_name, expected_type=type_hints["identity_name"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
            check_type(argname="argument session_policy_arn", value=session_policy_arn, expected_type=type_hints["session_policy_arn"])
            check_type(argname="argument studio_id", value=studio_id, expected_type=type_hints["studio_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_name": identity_name,
            "identity_type": identity_type,
            "session_policy_arn": session_policy_arn,
            "studio_id": studio_id,
        }

    @builtins.property
    def identity_name(self) -> builtins.str:
        '''The name of the user or group.

        For more information, see `UserName <https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName>`_ and `DisplayName <https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName>`_ in the *IAM Identity Center Identity Store API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-identityname
        '''
        result = self._values.get("identity_name")
        assert result is not None, "Required property 'identity_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_type(self) -> builtins.str:
        '''Specifies whether the identity to map to the Amazon EMR Studio is a user or a group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-identitytype
        '''
        result = self._values.get("identity_type")
        assert result is not None, "Required property 'identity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def session_policy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group.

        Session policies refine Studio user permissions without the need to use multiple IAM user roles. For more information, see `Create an EMR Studio user role with session policies <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-user-role.html>`_ in the *Amazon EMR Management Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-sessionpolicyarn
        '''
        result = self._values.get("session_policy_arn")
        assert result is not None, "Required property 'session_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''The ID of the Amazon EMR Studio to which the user or group will be mapped.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-studioid
        '''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStudioSessionMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnWALWorkspace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emr.CfnWALWorkspace",
):
    '''A WAL workspace is a logical container of write-ahead logs (WALs).

    All WALs in Amazon EMR WAL are encapsulated by a WAL workspace.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-walworkspace.html
    :cloudformationResource: AWS::EMR::WALWorkspace
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emr as emr
        
        cfn_wALWorkspace = emr.CfnWALWorkspace(self, "MyCfnWALWorkspace",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            wal_workspace_name="walWorkspaceName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        wal_workspace_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param tags: You can add tags when you create a new workspace. You can add, remove, or list tags from an active workspace, but you can't update tags. Instead, remove the tag and add a new one. For more information, see see `Tag your Amazon EMR WAL workspaces <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal.html#emr-hbase-wal-tagging>`_ .
        :param wal_workspace_name: The name of the WAL workspace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1985a11480d9771f4adca96d86b169aa02281678db75bca99cae188da64db2af)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWALWorkspaceProps(tags=tags, wal_workspace_name=wal_workspace_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecd0531bb1865d8e422006dd70518e7e6c3206a1606b5c3c0b65c97287946fb5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fee275f760ca07b82a676d0d77ce668eff171e2b3d5ce80fd4e2914f6edb7a2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''You can add tags when you create a new workspace.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__851c8fb8c44fa83f73dc5f006c4f65169726f6269fd062e84490d5cf26077add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="walWorkspaceName")
    def wal_workspace_name(self) -> typing.Optional[builtins.str]:
        '''The name of the WAL workspace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "walWorkspaceName"))

    @wal_workspace_name.setter
    def wal_workspace_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b841633928ec99eb6a369ad7d4f47c19b8160c69cd85540afdfe71238c44294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "walWorkspaceName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emr.CfnWALWorkspaceProps",
    jsii_struct_bases=[],
    name_mapping={"tags": "tags", "wal_workspace_name": "walWorkspaceName"},
)
class CfnWALWorkspaceProps:
    def __init__(
        self,
        *,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        wal_workspace_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWALWorkspace``.

        :param tags: You can add tags when you create a new workspace. You can add, remove, or list tags from an active workspace, but you can't update tags. Instead, remove the tag and add a new one. For more information, see see `Tag your Amazon EMR WAL workspaces <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal.html#emr-hbase-wal-tagging>`_ .
        :param wal_workspace_name: The name of the WAL workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-walworkspace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emr as emr
            
            cfn_wALWorkspace_props = emr.CfnWALWorkspaceProps(
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                wal_workspace_name="walWorkspaceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8593d9ac6a9a21fa49785102c4fc75235b74c034abaedb20ce93a44ec6d66c63)
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument wal_workspace_name", value=wal_workspace_name, expected_type=type_hints["wal_workspace_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tags is not None:
            self._values["tags"] = tags
        if wal_workspace_name is not None:
            self._values["wal_workspace_name"] = wal_workspace_name

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''You can add tags when you create a new workspace.

        You can add, remove, or list tags from an active workspace, but you can't update tags. Instead, remove the tag and add a new one. For more information, see see `Tag your Amazon EMR WAL workspaces <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal.html#emr-hbase-wal-tagging>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-walworkspace.html#cfn-emr-walworkspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def wal_workspace_name(self) -> typing.Optional[builtins.str]:
        '''The name of the WAL workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-walworkspace.html#cfn-emr-walworkspace-walworkspacename
        '''
        result = self._values.get("wal_workspace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWALWorkspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
    "CfnInstanceFleetConfig",
    "CfnInstanceFleetConfigProps",
    "CfnInstanceGroupConfig",
    "CfnInstanceGroupConfigProps",
    "CfnSecurityConfiguration",
    "CfnSecurityConfigurationProps",
    "CfnStep",
    "CfnStepProps",
    "CfnStudio",
    "CfnStudioProps",
    "CfnStudioSessionMapping",
    "CfnStudioSessionMappingProps",
    "CfnWALWorkspace",
    "CfnWALWorkspaceProps",
]

publication.publish()

def _typecheckingstub__078ec582504b982aedaecb6e8181c3cf53ae51c1b43cd59a31f8379e104620a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instances: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.JobFlowInstancesConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    job_flow_role: builtins.str,
    name: builtins.str,
    service_role: builtins.str,
    additional_info: typing.Any = None,
    applications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ApplicationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    auto_scaling_role: typing.Optional[builtins.str] = None,
    auto_termination_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.AutoTerminationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bootstrap_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.BootstrapActionConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_root_volume_iops: typing.Optional[jsii.Number] = None,
    ebs_root_volume_size: typing.Optional[jsii.Number] = None,
    ebs_root_volume_throughput: typing.Optional[jsii.Number] = None,
    kerberos_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.KerberosAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    log_uri: typing.Optional[builtins.str] = None,
    managed_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ManagedScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    os_release_label: typing.Optional[builtins.str] = None,
    placement_group_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.PlacementGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    release_label: typing.Optional[builtins.str] = None,
    scale_down_behavior: typing.Optional[builtins.str] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    step_concurrency_level: typing.Optional[jsii.Number] = None,
    steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.StepConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    visible_to_all_users: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bbe2decc930b4772f0407223e119030f3892221da6840065798499363723d31(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee2b9fd8d133889786966e4e13fa9f42593ed4a152172b2a5f46f008717ed56a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db10eb80ac95a4595d858fdb0ef7856bf908495b5881a437e2418e12ef04e2f(
    value: typing.Union[_IResolvable_da3f097b, CfnCluster.JobFlowInstancesConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d15d32b487b49d5a8c2e21737709401b2e456ae4a474e281d2be42453fe4e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f422fb80835fbbe27ca5ef52cdf0b51d324e042c174b5bbf7f5b6c241f060238(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d66a155fe1abdff7c63e4e37d410af54a782aafe35f5b0624479ed23d224711(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348f0a3a57b5e0506d5065002305d702fe48d937d3cf7901229ca7dd35b22175(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e5be2002d09889a797c9582ab789359945687c870580656dbe722e89affc8a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.ApplicationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220e0794f7e50696a7bce5f1cf4265710a3841db26e170a75b462acb7db4953a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e8b03bd44a0739c6fca421ce3e85b26ae46c02940e43a578dfece166b4cbb3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.AutoTerminationPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a761eb62509f84f3cbdff36a01487f8fb05f47b8241a831edf6b50a7bbaff9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.BootstrapActionConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4961b9c02eb65b76747f3388b3687aa1f18bf2da62820618bea64915a04b6954(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.ConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a91e39dff57dc0abc6e50e192e054139d45c74fc3bc1945999d3f9468c228a5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a5180c93c70a8f43ed9835c3357a42eafc25f6dc6c5aa034d474e2f615dd1f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1be0c0b7c99ca4316b39ef88877cc04569c66abbd6ae83da0946947f1bf063(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__951b4ef3a48c5da248736a1dd98ab6d527bce3f6de302ca2d84d41ee7e213288(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb6e8fa078ddb5d5ca597385e37e266a7ee1587d10523bea725cff21909211bd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.KerberosAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1529c639be8052f81bd05a31b6b01a4b1b48080f7c84fe0c477a646c6ce50a4e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c8b1a2acb54ad4aaccda0d0052a50ac533bed40115aa8e00fc6fd90bb390c42(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5679f4b15ba00e5797a6ca36888a09881f956e47615cd9f237382bdc765ab756(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.ManagedScalingPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d4c0fd8467e6006f700dcbf1ba5095561e1d0287c44dc0c0a3753aaeb3d7d14(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398553fa8e4e3f5661ed1198260a3a1fcc13ee30c6c2bc59bacdcffe873be756(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.PlacementGroupConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f4881cac49b58e2914939050f8e5a864a826f6035515c68f81b50fc7b14ded(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__443405bdf72dbf025ed25339eeb1475e84c960ad6bef75c4e466da4f43b5863b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882ded38da76716522321aa83b05c78696444dba276a265637df5234777b2852(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0c077452ad77e4b3be4546305a02b64cce648e3837e39a0361e2855285b9db9(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6535ae4fb40b89a54ff36a07d45179b7d6e5504f674a8a532cde5bea87edd59e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCluster.StepConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4038da1c46af7e2d9b50fc2521906fa041359d46aa05b24162a709acb1504d63(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3181237e04f1f3e57ab37ac5dcdd9cf1f158ae1015ef97f820a75179d324a382(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf8b605c327fe9a55d7a90674524f316b8f070940e929c53e1c966b8f68a18e5(
    *,
    additional_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa5bb304f42582274159985dd72e5294f3a513707f7460a42aafb194433c6af(
    *,
    constraints: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ScalingConstraintsProperty, typing.Dict[builtins.str, typing.Any]]],
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ScalingRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__118dc21c4af3ce0236b744a2f6b058f706aa70e288450a8771ef8efb27c9245c(
    *,
    idle_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa9f35ad922816267708196f89ee674f80a176c000f51f281f78aeea56c3575(
    *,
    name: builtins.str,
    script_bootstrap_action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ScriptBootstrapActionConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c6e9b1e6ddd9e7394a707f10838024730233a6162319152afb182065f469e4(
    *,
    comparison_operator: builtins.str,
    metric_name: builtins.str,
    period: jsii.Number,
    threshold: jsii.Number,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.MetricDimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    namespace: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc8cf0c083fcbbc2c4e1910146ba4c6c959a6e36991ec830a52e0262a1b06e8(
    *,
    maximum_capacity_units: jsii.Number,
    minimum_capacity_units: jsii.Number,
    unit_type: builtins.str,
    maximum_core_capacity_units: typing.Optional[jsii.Number] = None,
    maximum_on_demand_capacity_units: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__762e4654096c644b1ccf34d3832fa5e53cc3647761f6d0a0ed19865f7efb39db(
    *,
    classification: typing.Optional[builtins.str] = None,
    configuration_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5126d3ffa8a013f43ff9f99f79a23a9a3d3aa03919b6fe5d784b7a28817bf3f0(
    *,
    volume_specification: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.VolumeSpecificationProperty, typing.Dict[builtins.str, typing.Any]]],
    volumes_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289a0cf33d6f771401695f26c373e2ed078bce1f2750d4690cc1d0b1c482e235(
    *,
    ebs_block_device_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EbsBlockDeviceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3086fca1cb7ccf0ee3e0ba36727f8170913cea7fcd41960c212cbe4f26f9fea(
    *,
    jar: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    main_class: typing.Optional[builtins.str] = None,
    step_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.KeyValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b48fe88bfe7ab8726e3ed373177e22463a0bb5c19fdfb6f4bb239aedc4a5d1ac(
    *,
    instance_type_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.InstanceTypeConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    launch_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.InstanceFleetProvisioningSpecificationsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_on_demand_capacity: typing.Optional[jsii.Number] = None,
    target_spot_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b138f924cf93d1337c2cb3bdd25dfbcf94457589d616a6f7829b0bcd0a10149(
    *,
    on_demand_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.OnDemandProvisioningSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    spot_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SpotProvisioningSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e3a62519b2b5fb87993923e143b12cd90ce3e00aa04b8e01ea10a6242471d9(
    *,
    instance_count: jsii.Number,
    instance_type: builtins.str,
    auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bid_price: typing.Optional[builtins.str] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EbsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    market: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e04c7cf6db409085e044ff55b4223b3cfbcb9f86e3c1e3385c072880c8a6af8(
    *,
    instance_type: builtins.str,
    bid_price: typing.Optional[builtins.str] = None,
    bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.EbsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    weighted_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97053e1923915e0068df7012383808d225b615a5d3590985b1aa4048ba43f0e9(
    *,
    additional_master_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    additional_slave_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    core_instance_fleet: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.InstanceFleetConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    core_instance_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.InstanceGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ec2_key_name: typing.Optional[builtins.str] = None,
    ec2_subnet_id: typing.Optional[builtins.str] = None,
    ec2_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    emr_managed_master_security_group: typing.Optional[builtins.str] = None,
    emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
    hadoop_version: typing.Optional[builtins.str] = None,
    keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    master_instance_fleet: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.InstanceFleetConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    master_instance_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.InstanceGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    placement: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.PlacementTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_access_security_group: typing.Optional[builtins.str] = None,
    task_instance_fleets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.InstanceFleetConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    task_instance_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.InstanceGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    termination_protected: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    unhealthy_node_replacement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__540522543a1aa0db8a729abe18e5fa2372c90f5f9e05e3165a2dd6cd869f3bb0(
    *,
    kdc_admin_password: builtins.str,
    realm: builtins.str,
    ad_domain_join_password: typing.Optional[builtins.str] = None,
    ad_domain_join_user: typing.Optional[builtins.str] = None,
    cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de77f42d53bb5f752f54244451586c821de421f64b6929630c898540f71641a(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0286741b316b450e24ed1eff9bc726fec190a69e54cee78ab3a340bcde86cafe(
    *,
    compute_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ComputeLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5489079058853fbeec63f1c1e106aede50410429a2d603a5ab90b22e3c39dca(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2b2b082993c86b69c150a13684b12a05c6ed2134f215a73050d14afc94e510(
    *,
    allocation_strategy: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9024d4ca1b091fc3350c52943f87c19e6db412c0ba54cd4b2061955ab335200d(
    *,
    instance_role: builtins.str,
    placement_strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a2af5f8dbc7ce16a771e9390fe33448839574f71eaa2acb2f7b7050a1ca0da(
    *,
    availability_zone: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1902e04b59a5603a2ae4aafc06afece2ee3bdbd353692541d87ac7261ae3a892(
    *,
    simple_scaling_policy_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SimpleScalingPolicyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    market: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__218f86c887a6386b3a9f268232cf2402b2c01961c7dc4b1c5c54cd37b45f7f72(
    *,
    max_capacity: jsii.Number,
    min_capacity: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0906d3de6d43ea3035952bd939199d7b858dfba3dba2c95200e70324783fce7f(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ScalingActionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    trigger: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ScalingTriggerProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df2b0de5a8f69682866a7f7b93de987151394068d2650e0ae0ed982b81f2b30(
    *,
    cloud_watch_alarm_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.CloudWatchAlarmDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa367b9637052cae9251c15612e003865ebda21afaf560950bb477d8b49253c(
    *,
    path: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ab5f63d2f26fa03522ac8c3decfe23ac709ffdb5e6d508b478156d95d4e841c(
    *,
    scaling_adjustment: jsii.Number,
    adjustment_type: typing.Optional[builtins.str] = None,
    cool_down: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__208fcd2396b27638e4993cac386f565d58d969b0cecd86940902156a2329b2d9(
    *,
    timeout_action: builtins.str,
    timeout_duration_minutes: jsii.Number,
    allocation_strategy: typing.Optional[builtins.str] = None,
    block_duration_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3f0e87741e903ab6e6acc98e6f4de31edf9b395d6ec0ca0e9561069b8e799c7(
    *,
    hadoop_jar_step: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.HadoopJarStepConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    action_on_failure: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d9df61da11f931c34aa6af7c0e9bf71cf070f0a0d48100f43043b2adcdbcd5(
    *,
    size_in_gb: jsii.Number,
    volume_type: builtins.str,
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25985ea8bea73f3b566e4cc44a54f891c8c64b46cf5c4fb0ac288983cd463f2f(
    *,
    instances: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.JobFlowInstancesConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    job_flow_role: builtins.str,
    name: builtins.str,
    service_role: builtins.str,
    additional_info: typing.Any = None,
    applications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ApplicationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    auto_scaling_role: typing.Optional[builtins.str] = None,
    auto_termination_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.AutoTerminationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bootstrap_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.BootstrapActionConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_root_volume_iops: typing.Optional[jsii.Number] = None,
    ebs_root_volume_size: typing.Optional[jsii.Number] = None,
    ebs_root_volume_throughput: typing.Optional[jsii.Number] = None,
    kerberos_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.KerberosAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    log_uri: typing.Optional[builtins.str] = None,
    managed_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.ManagedScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    os_release_label: typing.Optional[builtins.str] = None,
    placement_group_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.PlacementGroupConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    release_label: typing.Optional[builtins.str] = None,
    scale_down_behavior: typing.Optional[builtins.str] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    step_concurrency_level: typing.Optional[jsii.Number] = None,
    steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.StepConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    visible_to_all_users: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25473c0968868f7cb7ae13c5d07084fdff34429497e0ea823b7527eea6ce494f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_id: builtins.str,
    instance_fleet_type: builtins.str,
    instance_type_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.InstanceTypeConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    launch_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_on_demand_capacity: typing.Optional[jsii.Number] = None,
    target_spot_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ed3f5cbfeb698332e274bbe7785722e739d9dec509f54283e0495cf8900e71(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e98716d54c69df2f9bc4a900903b8690bf3dbe75423a21ead9ce4d36cbd0443f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__400bee2e9ad25af5bc5503b31db6f8c647cc75941195dd29846c6d2ff917cf27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e599502a138f8a9158bcc5bbc77fd3cb1fa6aacdcda3c340c2bc35cdb54c5ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888820cb4f4a0c9a1efd66dd14e34f331d9e75498488017d37693b4ca8f07e10(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceFleetConfig.InstanceTypeConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__037e3da780812285c831d0eb45598c2c6a76b22d073c1e4a83b5d4529a0e479c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46de029a613d830d1cd5aafc306617484db5e788259a5eb5e20ddfdb18290125(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822a16f54dafb22c28528e47fdb7a49930c485e6f54b9eeb4a03467e03af3a7a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c47404264830e50e7ddaef51024f8f530b123b3a2c96dd8fc19683b81e6fc0(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb99c46a2e6804e68d48ee2a2882e72c00713be16c2a7eb0c1ffda179a4964d(
    *,
    classification: typing.Optional[builtins.str] = None,
    configuration_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3279a4aeccde870f13ef700abffb5a21dac69394e7342602659de2e9d001b6fb(
    *,
    volume_specification: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.VolumeSpecificationProperty, typing.Dict[builtins.str, typing.Any]]],
    volumes_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c01313df17cf722f93042eafce67680bfdf5243bba4058c5cc9d54139c1124(
    *,
    ebs_block_device_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a22ec5152d77e43e0a91e7ac72349bff7b323c77ba7af7b916a7565bc1a759(
    *,
    on_demand_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    spot_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__051c3b44a825d0f79c73260ba9c4b6395a44dae707c2d0ae1291df31ee520108(
    *,
    instance_type: builtins.str,
    bid_price: typing.Optional[builtins.str] = None,
    bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.EbsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    weighted_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf71b5c7658598ec550bf1195bd742cbfb6e455c0c782143392a53f88bfdf172(
    *,
    allocation_strategy: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b61d9945e0ef7f9b80bb5d1375dc8b2f9f8655abbb01833fe74ef1cafbfcd8d(
    *,
    timeout_action: builtins.str,
    timeout_duration_minutes: jsii.Number,
    allocation_strategy: typing.Optional[builtins.str] = None,
    block_duration_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbcefec98bf4df26aee8c4c32035c6379883a9a1f189bbc763cba54f8f73d579(
    *,
    size_in_gb: jsii.Number,
    volume_type: builtins.str,
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f5c77adfe4a2c26c531874c0df7d744af995801149e28623e666dfb6bf26b6(
    *,
    cluster_id: builtins.str,
    instance_fleet_type: builtins.str,
    instance_type_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.InstanceTypeConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    launch_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_on_demand_capacity: typing.Optional[jsii.Number] = None,
    target_spot_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b03c1e96b01aafd31c257702f4a9ed7a4281e8d9ba0f2f19a20ccc53465d08e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_count: jsii.Number,
    instance_role: builtins.str,
    instance_type: builtins.str,
    job_flow_id: builtins.str,
    auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bid_price: typing.Optional[builtins.str] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.EbsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    market: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1de17e348f1473656fa16b6154e6ecc550f06d756f34e0dd16848f80c72fe2bd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c371e1ed73cea2b17a5b42ab80c40254e3489b4218c3d85de868719ecf4c39(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a56b526bb946892e98d3d7d2b105ae4d7b95c59bf23590bba4cb3f57e014a87b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d176dc92e6cc9a7943f8591598418735b47fe6599a6a87375ce8047e23f2582c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5c0de0de6b187413fc259ce830ca1a4cb07874c4e2e4614d43b9806c442a8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69245f4d15e2a5dae10e27b298ff011d20580fac579b2b51dfb574b9538d9552(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef90a0dcff109aaa0f7a46baf739816f26a3ccb9669240606f89552508d0ca8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.AutoScalingPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab690714e1919e92ed20dc7aa3e5315a2b1bfbcee89fc65c09ea7168c130b1dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0131144525f35798c3b6081d980630003a3d1b9f1c3aae652f676206e8aeaa8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.ConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__303cab696a08592b720c8e8be64275a3bbf6b789e1077ee4c162c6c0712653e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07cf75fd968a10f65fd11c71b6efc052932bd414a38416da34ccff0a4335fd8e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceGroupConfig.EbsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05359e9787323de816895b743b6af3dd8f21fcc6a67f534dd7684d66581d93c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58871e6eae621e6fbe1e15c4166ad29e07293a9a1d2305d7fe9ca365634fb809(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ccf52c4a35db129b92c587555ec8d0f67a3d97092e5307fa0ddcb0b2106c137(
    *,
    constraints: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.ScalingConstraintsProperty, typing.Dict[builtins.str, typing.Any]]],
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.ScalingRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ef36d052fd1c73f3c150fc370cea09f7f8cfa0fed7c5d3618650d6f138e57d9(
    *,
    comparison_operator: builtins.str,
    metric_name: builtins.str,
    period: jsii.Number,
    threshold: jsii.Number,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.MetricDimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    namespace: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ac2b0b1a65e34f3c9e098b6f75c278daa93d377b96cededa4517b4fa7759d9e(
    *,
    classification: typing.Optional[builtins.str] = None,
    configuration_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee72789132b4e90a1d6a90327a95ec789abc3a6724fa23b1de25280e805781c2(
    *,
    volume_specification: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.VolumeSpecificationProperty, typing.Dict[builtins.str, typing.Any]]],
    volumes_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f334f21b45a80c7afc87361f15a522c7fcfaa41b4f7ab73dce958c051806dc9(
    *,
    ebs_block_device_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2113ac9fdc707bb27249d54043fd206f25a93101010e5b771e1e0958839cdc0(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__724cf187947d5b03301bf75eb59a7228254024fd628805c879916c536c7c6051(
    *,
    simple_scaling_policy_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    market: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ff3b5d35320ac919544d56e90ea12239b9eb3d0d7419c51f8fb0d37bc989b5(
    *,
    max_capacity: jsii.Number,
    min_capacity: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22fd5263f7ede9f4022ec6e5f459bb132aca11720ec7f0ee2967d60e7c1ba80(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.ScalingActionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    trigger: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.ScalingTriggerProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5071bc066eda67f0957ff3f0cfffd8ee81b66fdad65755907ee755e7ac063c3d(
    *,
    cloud_watch_alarm_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6268a4e2bfec2bdc60b96553635aab203a6017b3189fca1955213d254af9194c(
    *,
    scaling_adjustment: jsii.Number,
    adjustment_type: typing.Optional[builtins.str] = None,
    cool_down: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__243316d3b741ddf8c20750398e178fdc490d62e22eb2efacb27623b9fd5ad95c(
    *,
    size_in_gb: jsii.Number,
    volume_type: builtins.str,
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9a4a8b0692b3ed59bf418552ec7f58ae67ef7b9ad41b00ecca1de4f841b4f5f(
    *,
    instance_count: jsii.Number,
    instance_role: builtins.str,
    instance_type: builtins.str,
    job_flow_id: builtins.str,
    auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bid_price: typing.Optional[builtins.str] = None,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    ebs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceGroupConfig.EbsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    market: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1cd635a9a933efd41bee8e26ecb06319993c2aa7e459d0f829c5f4dfc58cfd3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_configuration: typing.Any,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da2a55d9947c59bcec537c0802a40401320b5d449dfc60b08045fa36fb13f4ea(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c082b9ccfa1abd822893594a5e87725508bfea7dc1f24c5da500060202b08e9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7354895da5b819c64c60ddab0fd091d5bb8338e636d169481d06071803d0542(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63794c5d363b5670a95b0dc55f674f81972d2ee1de87f02f8020599aecac3fef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__570e3d1d3bfab50b7c899148aae497fe36ce7f411f3a6bce1adbda62b5b3610d(
    *,
    security_configuration: typing.Any,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56108bb804f44dbb5230a71c020ff2994411f1d5f6f4226d7d5f948d62af211e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action_on_failure: builtins.str,
    hadoop_jar_step: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStep.HadoopJarStepConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    job_flow_id: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d97da37e72bd1bfccd5d003f6661e19aad059f59b1713075323b6ecf0eaa3d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d849d8f81968063aa29a34df211088e584a4a24f713c36ff0a67515ffe9ba8c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8246842b6fd3a6be5c74b6bfbc1bdfc328b214cf32fb8108cc06cf5793ea2a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ec64ae90b5233e23c51213eae7a3c1c03f9b635bef0f8e61032198c670bc9a(
    value: typing.Union[_IResolvable_da3f097b, CfnStep.HadoopJarStepConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99aff04b3096ab830115c2e81c573c3777b7b1cd6b5ba49de734510fe54bd41f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c3d15d09a73ee52be1d687a48f7a81900a69ccc44fb1cabb8a54adfa580c22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17116dab64c1f998800a3972016d6de90f0339e27d783be01c9aa002d894436e(
    *,
    jar: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    main_class: typing.Optional[builtins.str] = None,
    step_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStep.KeyValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45d46cddf4cc72fa52f0b95e0f250b3363c3d0ca8542a73ce888bcefb498379(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2487faa6f9278ced3b5fd2fab8e549b354a836990eb23096f7fd91d5e28230d(
    *,
    action_on_failure: builtins.str,
    hadoop_jar_step: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStep.HadoopJarStepConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    job_flow_id: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5fa63dd56ed829e4898f84009809f50f4125ac18a4dd04d1928420267568a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auth_mode: builtins.str,
    default_s3_location: builtins.str,
    engine_security_group_id: builtins.str,
    name: builtins.str,
    service_role: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    workspace_security_group_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    idc_instance_arn: typing.Optional[builtins.str] = None,
    idc_user_assignment: typing.Optional[builtins.str] = None,
    idp_auth_url: typing.Optional[builtins.str] = None,
    idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trusted_identity_propagation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    user_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12811625403d85ab8e027c82784f88c03aadb1a85e1a21e6db4a277a59011534(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ff2c045eee2499998e72b32d6123b1b4b00a854ea2337ba6394499ce8db13a7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29b15ad22555e04d2d23005c30126435e4966620a2c12755f0b0fdd6726aa11e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbb47bd6bd91d8355415cdc4cfdba08f13b080cf9846d2422d09e8b62265748c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90414b22e6e56647e9dbf693bbce0fdae1c28c236ecd929441a47f2d0f435d5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d52feab7f5ee099c16a0c05ed2b3e7cee18c472c41ac764589c397b620b299(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde7348c01a014ad19a7b3939357f0a15ad6204c8bfbe78489ef31850e579062(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__838f9f7dee3119f5c14aec74fc776ee2d173f127e4c1405cf253a925c408ae27(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e38a2a11b003b0f2c09b646ba28b0e59e56e5f4f7217dbedff8c6c3108b678f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6702095c850e5c6efc6f9b86ca71364b17fad2b801e0c3aa76a7482e99a295b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b57cfedf6d1b9357fb99a22fb68853be1bf68349d342ae1b382a911a55e0a0e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a934c05c196d0eda57d2ba0bd9c2811612942f47baa70b9def4583964bf21ef7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac14b0d933a01aa925ef079cc75e4ff2fb649c283f4c3356a21f14dae6f52d24(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96ab30aad484feea76068949481bec25db0a532494456bfbb1db494aebf3926(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bdf046decc7d9dcf4942916a9fd82f3ddf403adfc79905c187b32915e71a92e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1cfcbc2226f4548db4b1c3cdf608c158cf7718b53ca11e14bae09dd099353f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93c87ee05567302bb00141c45d4f778440c0196380fbcf0ea86580e0f69c98ad(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d97a907912a2a6d42177e06668874b62f8bb494e07b5e9659287db646faa1236(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4497b6d90d344f7cce9a12d862f813109f2ee695a175caef4ea9fba74f1175a8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e54f46221565a48807a50ddbb87f328aa43352455931a5089f5484c2263b30f4(
    *,
    auth_mode: builtins.str,
    default_s3_location: builtins.str,
    engine_security_group_id: builtins.str,
    name: builtins.str,
    service_role: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    workspace_security_group_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    idc_instance_arn: typing.Optional[builtins.str] = None,
    idc_user_assignment: typing.Optional[builtins.str] = None,
    idp_auth_url: typing.Optional[builtins.str] = None,
    idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trusted_identity_propagation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    user_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e47b505b0a4a624d7bbc7e6f0b97d1cb4bc72a6ca97f9fba72f1fd63a5544d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identity_name: builtins.str,
    identity_type: builtins.str,
    session_policy_arn: builtins.str,
    studio_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__153edf7b110ebe9d0c9cd9ba4efa10acec007161e12e38d6e9b66a4f81fd64d0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc7c9cb99a4061de76a53ac99eca669470f2c63506aa6313684786d25560afd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5feea587008e0e1c0549b46859852be4a2ae481e639401abe2b886234153fc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e7e1b5f29fb4ef82a3f45ccd1dc1210bfec29f167cd477284aa3b96257256b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3859eb45dacb565c5ba65788173f464996ebc788e3cc6302de95fb0f00ef960(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce585291954018d8d1dc1c7c090b303e853cefe2e95a5e5948014cb2d1a8f9a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a27468aac05a78cc17d6ec5e8f062d7c22a5b3bf56f44d8c6c90edc8a69a63e8(
    *,
    identity_name: builtins.str,
    identity_type: builtins.str,
    session_policy_arn: builtins.str,
    studio_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1985a11480d9771f4adca96d86b169aa02281678db75bca99cae188da64db2af(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    wal_workspace_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd0531bb1865d8e422006dd70518e7e6c3206a1606b5c3c0b65c97287946fb5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fee275f760ca07b82a676d0d77ce668eff171e2b3d5ce80fd4e2914f6edb7a2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__851c8fb8c44fa83f73dc5f006c4f65169726f6269fd062e84490d5cf26077add(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b841633928ec99eb6a369ad7d4f47c19b8160c69cd85540afdfe71238c44294(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8593d9ac6a9a21fa49785102c4fc75235b74c034abaedb20ce93a44ec6d66c63(
    *,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    wal_workspace_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
