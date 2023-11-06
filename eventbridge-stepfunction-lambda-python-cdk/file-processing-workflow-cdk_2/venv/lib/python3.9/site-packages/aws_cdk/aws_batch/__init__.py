'''
# AWS Batch Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_batch as batch
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Batch construct libraries](https://constructs.dev/search?q=batch)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Batch resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Batch.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-batch-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Batch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Batch.html).

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
class CfnComputeEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment",
):
    '''The ``AWS::Batch::ComputeEnvironment`` resource defines your AWS Batch compute environment.

    You can define ``MANAGED`` or ``UNMANAGED`` compute environments. ``MANAGED`` compute environments can use Amazon EC2 or AWS Fargate resources. ``UNMANAGED`` compute environments can only use EC2 resources. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .

    In a managed compute environment, AWS Batch manages the capacity and instance types of the compute resources within the environment. This is based on the compute resource specification that you define or the `launch template <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>`_ that you specify when you create the compute environment. You can choose either to use EC2 On-Demand Instances and EC2 Spot Instances, or to use Fargate and Fargate Spot capacity in your managed compute environment. You can optionally set a maximum price so that Spot Instances only launch when the Spot Instance price is below a specified percentage of the On-Demand price.
    .. epigraph::

       Multi-node parallel jobs are not supported on Spot Instances.

    In an unmanaged compute environment, you can manage your own EC2 compute resources and have a lot of flexibility with how you configure your compute resources. For example, you can use custom AMI. However, you need to verify that your AMI meets the Amazon ECS container instance AMI specification. For more information, see `container instance AMIs <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container_instance_AMIs.html>`_ in the *Amazon Elastic Container Service Developer Guide* . After you have created your unmanaged compute environment, you can use the `DescribeComputeEnvironments <https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeComputeEnvironments.html>`_ operation to find the Amazon ECS cluster that is associated with it. Then, manually launch your container instances into that Amazon ECS cluster. For more information, see `Launching an Amazon ECS container instance <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
    .. epigraph::

       To create a compute environment that uses EKS resources, the caller must have permissions to call ``eks:DescribeCluster`` . > AWS Batch doesn't upgrade the AMIs in a compute environment after it's created except under specific conditions. For example, it doesn't automatically update the AMIs when a newer version of the Amazon ECS optimized AMI is available. Therefore, you're responsible for the management of the guest operating system (including updates and security patches) and any additional application software or utilities that you install on the compute resources. There are two ways to use a new AMI for your AWS Batch jobs. The original method is to complete these steps:

       - Create a new compute environment with the new AMI.
       - Add the compute environment to an existing job queue.
       - Remove the earlier compute environment from your job queue.
       - Delete the earlier compute environment.

       In April 2022, AWS Batch added enhanced support for updating compute environments. For example, the ``UpdateComputeEnvironent`` API lets you use the ``ReplaceComputeEnvironment`` property to dynamically update compute environment parameters such as the launch template or instance type without replacement. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

       To use the enhanced updating of compute environments to update AMIs, follow these rules:

       - Either do not set the `ServiceRole <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-servicerole>`_ property or set it to the *AWSServiceRoleForBatch* service-linked role.
       - Set the `AllocationStrategy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ property to ``BEST_FIT_PROGRESSIVE`` or ``SPOT_CAPACITY_OPTIMIZED`` .
       - Set the `ReplaceComputeEnvironment <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-replacecomputeenvironment>`_ property to ``false`` .

       .. epigraph::

          Set the ``ReplaceComputeEnvironment`` property to ``false`` if the compute environment uses the ``BEST_FIT`` allocation strategy. > If the ``ReplaceComputeEnvironment`` property is set to ``false`` , you might receive an error message when you update the CFN template for a compute environment. This issue occurs if the updated ``desiredvcpus`` value is less than the current ``desiredvcpus`` value. As a workaround, delete the ``desiredvcpus`` value from the updated template or use the ``minvcpus`` property to manage the number of vCPUs. For information, see `Error message when you update the ``DesiredvCpus`` setting <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#error-desired-vcpus-update>`_ .

       - Set the `UpdateToLatestImageVersion <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ property to ``true`` . This property is used when you update a compute environment. The `UpdateToLatestImageVersion <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ property is ignored when you create a compute environment.
       - Either do not specify an image ID in `ImageId <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ or `ImageIdOverride <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imageidoverride>`_ properties, or in the launch template identified by the `Launch Template <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ property. In that case AWS Batch will select the latest Amazon ECS optimized AMI supported by AWS Batch at the time the infrastructure update is initiated. Alternatively you can specify the AMI ID in the ``ImageId`` or ``ImageIdOverride`` properties, or the launch template identified by the ``LaunchTemplate`` properties. Changing any of these properties will trigger an infrastructure update.

       If these rules are followed, any update that triggers an infrastructure update will cause the AMI ID to be re-selected. If the `Version <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-version>`_ property of the `LaunchTemplateSpecification <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html>`_ is set to ``$Latest`` or ``$Default`` , the latest or default version of the launch template will be evaluated up at the time of the infrastructure update, even if the ``LaunchTemplateSpecification`` was not updated.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_batch as batch
        
        cfn_compute_environment = batch.CfnComputeEnvironment(self, "MyCfnComputeEnvironment",
            type="type",
        
            # the properties below are optional
            compute_environment_name="computeEnvironmentName",
            compute_resources=batch.CfnComputeEnvironment.ComputeResourcesProperty(
                maxv_cpus=123,
                subnets=["subnets"],
                type="type",
        
                # the properties below are optional
                allocation_strategy="allocationStrategy",
                bid_percentage=123,
                desiredv_cpus=123,
                ec2_configuration=[batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty(
                    image_type="imageType",
        
                    # the properties below are optional
                    image_id_override="imageIdOverride",
                    image_kubernetes_version="imageKubernetesVersion"
                )],
                ec2_key_pair="ec2KeyPair",
                image_id="imageId",
                instance_role="instanceRole",
                instance_types=["instanceTypes"],
                launch_template=batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    version="version"
                ),
                minv_cpus=123,
                placement_group="placementGroup",
                security_group_ids=["securityGroupIds"],
                spot_iam_fleet_role="spotIamFleetRole",
                tags={
                    "tags_key": "tags"
                },
                update_to_latest_image_version=False
            ),
            eks_configuration=batch.CfnComputeEnvironment.EksConfigurationProperty(
                eks_cluster_arn="eksClusterArn",
                kubernetes_namespace="kubernetesNamespace"
            ),
            replace_compute_environment=False,
            service_role="serviceRole",
            state="state",
            tags={
                "tags_key": "tags"
            },
            unmanagedv_cpus=123,
            update_policy=batch.CfnComputeEnvironment.UpdatePolicyProperty(
                job_execution_timeout_minutes=123,
                terminate_jobs_on_update=False
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        compute_environment_name: typing.Optional[builtins.str] = None,
        compute_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeEnvironment.ComputeResourcesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        eks_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeEnvironment.EksConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        replace_compute_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        service_role: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        unmanagedv_cpus: typing.Optional[jsii.Number] = None,
        update_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeEnvironment.UpdatePolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param type: The type of the compute environment: ``MANAGED`` or ``UNMANAGED`` . For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .
        :param compute_environment_name: The name for your compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param compute_resources: The ComputeResources property type specifies details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .
        :param eks_configuration: The details for the Amazon EKS cluster that supports the compute environment.
        :param replace_compute_environment: Specifies whether the compute environment is replaced if an update is made that requires replacing the instances in the compute environment. The default value is ``true`` . To enable more properties to be updated, set this property to ``false`` . When changing the value of this property to ``false`` , do not change any other properties at the same time. If other properties are changed at the same time, and the change needs to be rolled back but it can't, it's possible for the stack to go into the ``UPDATE_ROLLBACK_FAILED`` state. You can't update a stack that is in the ``UPDATE_ROLLBACK_FAILED`` state. However, if you can continue to roll it back, you can return the stack to its original settings and then try to update it again. For more information, see `Continue rolling back an update <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`_ in the *AWS CloudFormation User Guide* . The properties that can't be changed without replacing the compute environment are in the ```ComputeResources`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html>`_ property type: ```AllocationStrategy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ , ```BidPercentage`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage>`_ , ```Ec2Configuration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```ImageId`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ , ```InstanceRole`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole>`_ , ```InstanceTypes`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes>`_ , ```LaunchTemplate`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ , ```MaxvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus>`_ , ```MinvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus>`_ , ```PlacementGroup`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup>`_ , ```SecurityGroupIds`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids>`_ , ```Subnets`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets>`_ , `Tags <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags>`_ , ```Type`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type>`_ , and ```UpdateToLatestImageVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ . Default: - true
        :param service_role: The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf. For more information, see `AWS Batch service IAM role <https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html>`_ in the *AWS Batch User Guide* . .. epigraph:: If your account already created the AWS Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the AWS Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the AWS Batch service-linked role in your account. If your specified role has a path other than ``/`` , then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` , specify ``/foo/bar`` as the role name. For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* . .. epigraph:: Depending on how you created your AWS Batch service role, its ARN might contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
        :param state: The state of the compute environment. If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues. If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand. If the state is ``DISABLED`` , then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state don't scale out. .. epigraph:: Compute environments in a ``DISABLED`` state may continue to incur billing charges. To prevent additional charges, turn off and then delete the compute environment. For more information, see `State <https://docs.aws.amazon.com/batch/latest/userguide/compute_environment_parameters.html#compute_environment_state>`_ in the *AWS Batch User Guide* . When an instance is idle, the instance scales down to the ``minvCpus`` value. However, the instance size doesn't change. For example, consider a ``c5.8xlarge`` instance with a ``minvCpus`` value of ``4`` and a ``desiredvCpus`` value of ``36`` . This instance doesn't scale down to a ``c5.large`` instance.
        :param tags: The tags applied to the compute environment.
        :param unmanagedv_cpus: The maximum number of vCPUs for an unmanaged compute environment. This parameter is only used for fair share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair share job queue, no vCPU capacity is reserved. .. epigraph:: This parameter is only supported when the ``type`` parameter is set to ``UNMANAGED`` .
        :param update_policy: Specifies the infrastructure update policy for the compute environment. For more information about infrastructure updates, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3892141757a3fffc40366f3b0a3472c965c97710a96f3bb61a3618dd43af76e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComputeEnvironmentProps(
            type=type,
            compute_environment_name=compute_environment_name,
            compute_resources=compute_resources,
            eks_configuration=eks_configuration,
            replace_compute_environment=replace_compute_environment,
            service_role=service_role,
            state=state,
            tags=tags,
            unmanagedv_cpus=unmanagedv_cpus,
            update_policy=update_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__181dea136575948e2334f9ffce96122ded2c4edc304f6835d519b8a40e411e4e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d72cf2605a93f743b750e273ccea4c1be6e5210af9e44b94c6722180f03040d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrComputeEnvironmentArn")
    def attr_compute_environment_arn(self) -> builtins.str:
        '''Returns the compute environment ARN, such as ``batch: *us-east-1* : *111122223333* :compute-environment/ *ComputeEnvironmentName*`` .

        :cloudformationAttribute: ComputeEnvironmentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComputeEnvironmentArn"))

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
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the compute environment: ``MANAGED`` or ``UNMANAGED`` .'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af58b33143bf1d8d98a3c10df145b0898751e739fa8cabe1763160d50bc3d730)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="computeEnvironmentName")
    def compute_environment_name(self) -> typing.Optional[builtins.str]:
        '''The name for your compute environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeEnvironmentName"))

    @compute_environment_name.setter
    def compute_environment_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__703e5e791be63f407384e398bda6c05261d86a114fb52955ac953213dc086558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeEnvironmentName", value)

    @builtins.property
    @jsii.member(jsii_name="computeResources")
    def compute_resources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.ComputeResourcesProperty"]]:
        '''The ComputeResources property type specifies details of the compute resources managed by the compute environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.ComputeResourcesProperty"]], jsii.get(self, "computeResources"))

    @compute_resources.setter
    def compute_resources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.ComputeResourcesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa0f8cbb024617b335ccf7af8884568ad91340203512578a8d682adfdfce5cd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeResources", value)

    @builtins.property
    @jsii.member(jsii_name="eksConfiguration")
    def eks_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.EksConfigurationProperty"]]:
        '''The details for the Amazon EKS cluster that supports the compute environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.EksConfigurationProperty"]], jsii.get(self, "eksConfiguration"))

    @eks_configuration.setter
    def eks_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.EksConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__896771848c9977e1ce30b550c3e02c1b1e7e047a645b3eb92c3d6d3bcf2ef1cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eksConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="replaceComputeEnvironment")
    def replace_compute_environment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the compute environment is replaced if an update is made that requires replacing the instances in the compute environment.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "replaceComputeEnvironment"))

    @replace_compute_environment.setter
    def replace_compute_environment(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f7a9dd96ed6e9e51373fc67bf7c1cfa4f89dea1d9ec4216da0ee3a471c21879)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replaceComputeEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> typing.Optional[builtins.str]:
        '''The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__682bb80f66d8c5016b985338436d49dc6155bd7a11dc1567d1a6478eddb9fc94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the compute environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30039c901207ae322b43ee9582a8efa812de586638692e722a62baa18097a10d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags applied to the compute environment.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd461eb02586f268eaf0fc0a27581016dd596744fdebffc9a80af4b63a998bd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="unmanagedvCpus")
    def unmanagedv_cpus(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of vCPUs for an unmanaged compute environment.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unmanagedvCpus"))

    @unmanagedv_cpus.setter
    def unmanagedv_cpus(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e874461559bd593606ec74eed9b2200a045433519c0ec8ec8d62a53f967da17a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unmanagedvCpus", value)

    @builtins.property
    @jsii.member(jsii_name="updatePolicy")
    def update_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.UpdatePolicyProperty"]]:
        '''Specifies the infrastructure update policy for the compute environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.UpdatePolicyProperty"]], jsii.get(self, "updatePolicy"))

    @update_policy.setter
    def update_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.UpdatePolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39e9319d6ed789d3e7f527a145e7be0671311d4703680199b29ca8aef5635e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatePolicy", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.ComputeResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maxv_cpus": "maxvCpus",
            "subnets": "subnets",
            "type": "type",
            "allocation_strategy": "allocationStrategy",
            "bid_percentage": "bidPercentage",
            "desiredv_cpus": "desiredvCpus",
            "ec2_configuration": "ec2Configuration",
            "ec2_key_pair": "ec2KeyPair",
            "image_id": "imageId",
            "instance_role": "instanceRole",
            "instance_types": "instanceTypes",
            "launch_template": "launchTemplate",
            "minv_cpus": "minvCpus",
            "placement_group": "placementGroup",
            "security_group_ids": "securityGroupIds",
            "spot_iam_fleet_role": "spotIamFleetRole",
            "tags": "tags",
            "update_to_latest_image_version": "updateToLatestImageVersion",
        },
    )
    class ComputeResourcesProperty:
        def __init__(
            self,
            *,
            maxv_cpus: jsii.Number,
            subnets: typing.Sequence[builtins.str],
            type: builtins.str,
            allocation_strategy: typing.Optional[builtins.str] = None,
            bid_percentage: typing.Optional[jsii.Number] = None,
            desiredv_cpus: typing.Optional[jsii.Number] = None,
            ec2_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeEnvironment.Ec2ConfigurationObjectProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ec2_key_pair: typing.Optional[builtins.str] = None,
            image_id: typing.Optional[builtins.str] = None,
            instance_role: typing.Optional[builtins.str] = None,
            instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeEnvironment.LaunchTemplateSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            minv_cpus: typing.Optional[jsii.Number] = None,
            placement_group: typing.Optional[builtins.str] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            spot_iam_fleet_role: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            update_to_latest_image_version: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Details about the compute resources managed by the compute environment.

            This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .

            :param maxv_cpus: The maximum number of Amazon EC2 vCPUs that an environment can reach. .. epigraph:: With both ``BEST_FIT_PROGRESSIVE`` and ``SPOT_CAPACITY_OPTIMIZED`` allocation strategies using On-Demand or Spot Instances, and the ``BEST_FIT`` strategy using Spot Instances, AWS Batch might need to exceed ``maxvCpus`` to meet your capacity requirements. In this event, AWS Batch never exceeds ``maxvCpus`` by more than a single instance. That is, no more than a single instance from among those specified in your compute environment.
            :param subnets: The VPC subnets where the compute resources are launched. Fargate compute resources can contain up to 16 subnets. For Fargate compute resources, providing an empty list will be handled as if this parameter wasn't specified and no change is made. For EC2 compute resources, providing an empty list removes the VPC subnets from the compute resource. For more information, see `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon VPC User Guide* . When updating a compute environment, changing the VPC subnets requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: AWS Batch on Amazon EC2 and AWS Batch on Amazon EKS support Local Zones. For more information, see `Local Zones <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones>`_ in the *Amazon EC2 User Guide for Linux Instances* , `Amazon EKS and AWS Local Zones <https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html>`_ in the *Amazon EKS User Guide* and `Amazon ECS clusters in Local Zones, Wavelength Zones, and AWS Outposts <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html#clusters-local-zones>`_ in the *Amazon ECS Developer Guide* . AWS Batch on Fargate doesn't currently support Local Zones.
            :param type: The type of compute environment: ``EC2`` , ``SPOT`` , ``FARGATE`` , or ``FARGATE_SPOT`` . For more information, see `Compute environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* . If you choose ``SPOT`` , you must also specify an Amazon EC2 Spot Fleet role with the ``spotIamFleetRole`` parameter. For more information, see `Amazon EC2 spot fleet role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`_ in the *AWS Batch User Guide* . When updating compute environment, changing the type of a compute environment requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . When updating the type of a compute environment, changing between ``EC2`` and ``SPOT`` or between ``FARGATE`` and ``FARGATE_SPOT`` will initiate an infrastructure update, but if you switch between ``EC2`` and ``FARGATE`` , AWS CloudFormation will create a new compute environment.
            :param allocation_strategy: The allocation strategy to use for the compute resource if not enough instances of the best fitting instance type can be allocated. This might be because of availability of the instance type in the Region or `Amazon EC2 service limits <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ . For more information, see `Allocation strategies <https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html>`_ in the *AWS Batch User Guide* . When updating a compute environment, changing the allocation strategy requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . ``BEST_FIT`` is not supported when updating a compute environment. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified. - **BEST_FIT (default)** - AWS Batch selects an instance type that best fits the needs of the jobs with a preference for the lowest-cost instance type. If additional instances of the selected instance type aren't available, AWS Batch waits for the additional instances to be available. If there aren't enough instances available, or if the user is reaching `Amazon EC2 service limits <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ then additional jobs aren't run until the currently running jobs have completed. This allocation strategy keeps costs lower but can limit scaling. If you are using Spot Fleets with ``BEST_FIT`` then the Spot Fleet IAM role must be specified. - **BEST_FIT_PROGRESSIVE** - AWS Batch will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types with a lower cost per unit vCPU. If additional instances of the previously selected instance types aren't available, AWS Batch will select new instance types. - **SPOT_CAPACITY_OPTIMIZED** - AWS Batch will select one or more instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types that are less likely to be interrupted. This allocation strategy is only available for Spot Instance compute resources. With both ``BEST_FIT_PROGRESSIVE`` and ``SPOT_CAPACITY_OPTIMIZED`` allocation strategies using On-Demand or Spot Instances, and the ``BEST_FIT`` strategy using Spot Instances, AWS Batch might need to go above ``maxvCpus`` to meet your capacity requirements. In this event, AWS Batch never exceeds ``maxvCpus`` by more than a single instance.
            :param bid_percentage: The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, the Spot price must be less than 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. For most use cases, we recommend leaving this field empty. When updating a compute environment, changing the bid percentage requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
            :param desiredv_cpus: The desired number of vCPUS in the compute environment. AWS Batch modifies this value between the minimum and maximum values based on job queue demand. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it. > AWS Batch doesn't support changing the desired number of vCPUs of an existing compute environment. Don't specify this parameter for compute environments using Amazon EKS clusters. > When you update the ``desiredvCpus`` setting, the value must be between the ``minvCpus`` and ``maxvCpus`` values. Additionally, the updated ``desiredvCpus`` value must be greater than or equal to the current ``desiredvCpus`` value. For more information, see `Troubleshooting AWS Batch <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#error-desired-vcpus-update>`_ in the *AWS Batch User Guide* .
            :param ec2_configuration: Provides information used to select Amazon Machine Images (AMIs) for EC2 instances in the compute environment. If ``Ec2Configuration`` isn't specified, the default is ``ECS_AL2`` . When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . To remove the EC2 configuration and any custom AMI ID specified in ``imageIdOverride`` , set this value to an empty string. One or two values can be provided. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
            :param ec2_key_pair: The Amazon EC2 key pair that's used for instances launched in the compute environment. You can use this key pair to log in to your instances with SSH. To remove the Amazon EC2 key pair, set this value to an empty string. When updating a compute environment, changing the EC2 key pair requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
            :param image_id: The Amazon Machine Image (AMI) ID used for instances launched in the compute environment. This parameter is overridden by the ``imageIdOverride`` member of the ``Ec2Configuration`` structure. To remove the custom AMI ID and use the default AMI ID, set this value to an empty string. When updating a compute environment, changing the AMI ID requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it. > The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param instance_role: The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ``*ecsInstanceRole*`` or ``arn:aws:iam:: *<aws_account_id>* :instance-profile/ *ecsInstanceRole*`` . For more information, see `Amazon ECS instance role <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`_ in the *AWS Batch User Guide* . When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
            :param instance_types: The instances types that can be launched. You can specify instance families to launch any instance type within those families (for example, ``c5`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose ``optimal`` to select instance types (from the C4, M4, and R4 instance families) that match the demand of your job queues. When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it. > When you create a compute environment, the instance types that you select for the compute environment must share the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment. > Currently, ``optimal`` uses instance types from the C4, M4, and R4 instance families. In Regions that don't have instance types from those instance families, instance types from the C5, M5, and R5 instance families are used.
            :param launch_template: The launch template to use for your compute resources. Any other compute resource parameters that you specify in a `CreateComputeEnvironment <https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html>`_ API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see `Launch Template Support <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`_ in the ** . Removing the launch template from a compute environment will not remove the AMI specified in the launch template. In order to update the AMI specified in a launch template, the ``updateToLatestImageVersion`` parameter must be set to ``true`` . When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the ** . .. epigraph:: This parameter isn't applicable to jobs running on Fargate resources, and shouldn't be specified.
            :param minv_cpus: The minimum number of vCPUs that an environment should maintain (even if the compute environment is ``DISABLED`` ). .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
            :param placement_group: The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see `Placement groups <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`_ in the *Amazon EC2 User Guide for Linux Instances* . When updating a compute environment, changing the placement group requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
            :param security_group_ids: The Amazon EC2 security groups that are associated with instances launched in the compute environment. This parameter is required for Fargate compute resources, where it can contain up to 5 security groups. For Fargate compute resources, providing an empty list is handled as if this parameter wasn't specified and no change is made. For EC2 compute resources, providing an empty list removes the security groups from the compute resource. When updating a compute environment, changing the EC2 security groups requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            :param spot_iam_fleet_role: The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment. This role is required if the allocation strategy set to ``BEST_FIT`` or if the allocation strategy isn't specified. For more information, see `Amazon EC2 spot fleet role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it. > To tag your Spot Instances on creation, the Spot Fleet IAM role specified here must use the newer *AmazonEC2SpotFleetTaggingRole* managed policy. The previously recommended *AmazonEC2SpotFleetRole* managed policy doesn't have the required permissions to tag Spot Instances. For more information, see `Spot instances not tagged on creation <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#spot-instance-no-tag>`_ in the *AWS Batch User Guide* .
            :param tags: Key-value pair tags to be applied to EC2 resources that are launched in the compute environment. For AWS Batch , these take the form of ``"String1": "String2"`` , where ``String1`` is the tag key and ``String2`` is the tag value-for example, ``{ "Name": "Batch Instance - C4OnDemand" }`` . This is helpful for recognizing your Batch instances in the Amazon EC2 console. These tags aren't seen when using the AWS Batch ``ListTagsForResource`` API operation. When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.
            :param update_to_latest_image_version: Specifies whether the AMI ID is updated to the latest one that's supported by AWS Batch when the compute environment has an infrastructure update. The default value is ``false`` . .. epigraph:: An AMI ID can either be specified in the ``imageId`` or ``imageIdOverride`` parameters or be determined by the launch template that's specified in the ``launchTemplate`` parameter. If an AMI ID is specified any of these ways, this parameter is ignored. For more information about to update AMI IDs during an infrastructure update, see `Updating the AMI ID <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html#updating-compute-environments-ami>`_ in the *AWS Batch User Guide* . When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                compute_resources_property = batch.CfnComputeEnvironment.ComputeResourcesProperty(
                    maxv_cpus=123,
                    subnets=["subnets"],
                    type="type",
                
                    # the properties below are optional
                    allocation_strategy="allocationStrategy",
                    bid_percentage=123,
                    desiredv_cpus=123,
                    ec2_configuration=[batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty(
                        image_type="imageType",
                
                        # the properties below are optional
                        image_id_override="imageIdOverride",
                        image_kubernetes_version="imageKubernetesVersion"
                    )],
                    ec2_key_pair="ec2KeyPair",
                    image_id="imageId",
                    instance_role="instanceRole",
                    instance_types=["instanceTypes"],
                    launch_template=batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty(
                        launch_template_id="launchTemplateId",
                        launch_template_name="launchTemplateName",
                        version="version"
                    ),
                    minv_cpus=123,
                    placement_group="placementGroup",
                    security_group_ids=["securityGroupIds"],
                    spot_iam_fleet_role="spotIamFleetRole",
                    tags={
                        "tags_key": "tags"
                    },
                    update_to_latest_image_version=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e554c6eb00e2d197fa806c35d70007a7590c1c363259e3e48971f0671e0e85f)
                check_type(argname="argument maxv_cpus", value=maxv_cpus, expected_type=type_hints["maxv_cpus"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
                check_type(argname="argument bid_percentage", value=bid_percentage, expected_type=type_hints["bid_percentage"])
                check_type(argname="argument desiredv_cpus", value=desiredv_cpus, expected_type=type_hints["desiredv_cpus"])
                check_type(argname="argument ec2_configuration", value=ec2_configuration, expected_type=type_hints["ec2_configuration"])
                check_type(argname="argument ec2_key_pair", value=ec2_key_pair, expected_type=type_hints["ec2_key_pair"])
                check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
                check_type(argname="argument instance_role", value=instance_role, expected_type=type_hints["instance_role"])
                check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
                check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
                check_type(argname="argument minv_cpus", value=minv_cpus, expected_type=type_hints["minv_cpus"])
                check_type(argname="argument placement_group", value=placement_group, expected_type=type_hints["placement_group"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument spot_iam_fleet_role", value=spot_iam_fleet_role, expected_type=type_hints["spot_iam_fleet_role"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
                check_type(argname="argument update_to_latest_image_version", value=update_to_latest_image_version, expected_type=type_hints["update_to_latest_image_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "maxv_cpus": maxv_cpus,
                "subnets": subnets,
                "type": type,
            }
            if allocation_strategy is not None:
                self._values["allocation_strategy"] = allocation_strategy
            if bid_percentage is not None:
                self._values["bid_percentage"] = bid_percentage
            if desiredv_cpus is not None:
                self._values["desiredv_cpus"] = desiredv_cpus
            if ec2_configuration is not None:
                self._values["ec2_configuration"] = ec2_configuration
            if ec2_key_pair is not None:
                self._values["ec2_key_pair"] = ec2_key_pair
            if image_id is not None:
                self._values["image_id"] = image_id
            if instance_role is not None:
                self._values["instance_role"] = instance_role
            if instance_types is not None:
                self._values["instance_types"] = instance_types
            if launch_template is not None:
                self._values["launch_template"] = launch_template
            if minv_cpus is not None:
                self._values["minv_cpus"] = minv_cpus
            if placement_group is not None:
                self._values["placement_group"] = placement_group
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if spot_iam_fleet_role is not None:
                self._values["spot_iam_fleet_role"] = spot_iam_fleet_role
            if tags is not None:
                self._values["tags"] = tags
            if update_to_latest_image_version is not None:
                self._values["update_to_latest_image_version"] = update_to_latest_image_version

        @builtins.property
        def maxv_cpus(self) -> jsii.Number:
            '''The maximum number of Amazon EC2 vCPUs that an environment can reach.

            .. epigraph::

               With both ``BEST_FIT_PROGRESSIVE`` and ``SPOT_CAPACITY_OPTIMIZED`` allocation strategies using On-Demand or Spot Instances, and the ``BEST_FIT`` strategy using Spot Instances, AWS Batch might need to exceed ``maxvCpus`` to meet your capacity requirements. In this event, AWS Batch never exceeds ``maxvCpus`` by more than a single instance. That is, no more than a single instance from among those specified in your compute environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus
            '''
            result = self._values.get("maxv_cpus")
            assert result is not None, "Required property 'maxv_cpus' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''The VPC subnets where the compute resources are launched.

            Fargate compute resources can contain up to 16 subnets. For Fargate compute resources, providing an empty list will be handled as if this parameter wasn't specified and no change is made. For EC2 compute resources, providing an empty list removes the VPC subnets from the compute resource. For more information, see `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon VPC User Guide* .

            When updating a compute environment, changing the VPC subnets requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               AWS Batch on Amazon EC2 and AWS Batch on Amazon EKS support Local Zones. For more information, see `Local Zones <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones>`_ in the *Amazon EC2 User Guide for Linux Instances* , `Amazon EKS and AWS Local Zones <https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html>`_ in the *Amazon EKS User Guide* and `Amazon ECS clusters in Local Zones, Wavelength Zones, and AWS Outposts <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html#clusters-local-zones>`_ in the *Amazon ECS Developer Guide* .

               AWS Batch on Fargate doesn't currently support Local Zones.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of compute environment: ``EC2`` , ``SPOT`` , ``FARGATE`` , or ``FARGATE_SPOT`` .

            For more information, see `Compute environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .

            If you choose ``SPOT`` , you must also specify an Amazon EC2 Spot Fleet role with the ``spotIamFleetRole`` parameter. For more information, see `Amazon EC2 spot fleet role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`_ in the *AWS Batch User Guide* .

            When updating compute environment, changing the type of a compute environment requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            When updating the type of a compute environment, changing between ``EC2`` and ``SPOT`` or between ``FARGATE`` and ``FARGATE_SPOT`` will initiate an infrastructure update, but if you switch between ``EC2`` and ``FARGATE`` , AWS CloudFormation will create a new compute environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allocation_strategy(self) -> typing.Optional[builtins.str]:
            '''The allocation strategy to use for the compute resource if not enough instances of the best fitting instance type can be allocated.

            This might be because of availability of the instance type in the Region or `Amazon EC2 service limits <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ . For more information, see `Allocation strategies <https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html>`_ in the *AWS Batch User Guide* .

            When updating a compute environment, changing the allocation strategy requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . ``BEST_FIT`` is not supported when updating a compute environment.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources, and shouldn't be specified.

            - **BEST_FIT (default)** - AWS Batch selects an instance type that best fits the needs of the jobs with a preference for the lowest-cost instance type. If additional instances of the selected instance type aren't available, AWS Batch waits for the additional instances to be available. If there aren't enough instances available, or if the user is reaching `Amazon EC2 service limits <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ then additional jobs aren't run until the currently running jobs have completed. This allocation strategy keeps costs lower but can limit scaling. If you are using Spot Fleets with ``BEST_FIT`` then the Spot Fleet IAM role must be specified.
            - **BEST_FIT_PROGRESSIVE** - AWS Batch will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types with a lower cost per unit vCPU. If additional instances of the previously selected instance types aren't available, AWS Batch will select new instance types.
            - **SPOT_CAPACITY_OPTIMIZED** - AWS Batch will select one or more instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types that are less likely to be interrupted. This allocation strategy is only available for Spot Instance compute resources.

            With both ``BEST_FIT_PROGRESSIVE`` and ``SPOT_CAPACITY_OPTIMIZED`` allocation strategies using On-Demand or Spot Instances, and the ``BEST_FIT`` strategy using Spot Instances, AWS Batch might need to go above ``maxvCpus`` to meet your capacity requirements. In this event, AWS Batch never exceeds ``maxvCpus`` by more than a single instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bid_percentage(self) -> typing.Optional[jsii.Number]:
            '''The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched.

            For example, if your maximum percentage is 20%, the Spot price must be less than 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. For most use cases, we recommend leaving this field empty.

            When updating a compute environment, changing the bid percentage requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage
            '''
            result = self._values.get("bid_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def desiredv_cpus(self) -> typing.Optional[jsii.Number]:
            '''The desired number of vCPUS in the compute environment.

            AWS Batch modifies this value between the minimum and maximum values based on job queue demand.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it. > AWS Batch doesn't support changing the desired number of vCPUs of an existing compute environment. Don't specify this parameter for compute environments using Amazon EKS clusters. > When you update the ``desiredvCpus`` setting, the value must be between the ``minvCpus`` and ``maxvCpus`` values.

               Additionally, the updated ``desiredvCpus`` value must be greater than or equal to the current ``desiredvCpus`` value. For more information, see `Troubleshooting AWS Batch <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#error-desired-vcpus-update>`_ in the *AWS Batch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-desiredvcpus
            '''
            result = self._values.get("desiredv_cpus")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ec2_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.Ec2ConfigurationObjectProperty"]]]]:
            '''Provides information used to select Amazon Machine Images (AMIs) for EC2 instances in the compute environment.

            If ``Ec2Configuration`` isn't specified, the default is ``ECS_AL2`` .

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . To remove the EC2 configuration and any custom AMI ID specified in ``imageIdOverride`` , set this value to an empty string.

            One or two values can be provided.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration
            '''
            result = self._values.get("ec2_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.Ec2ConfigurationObjectProperty"]]]], result)

        @builtins.property
        def ec2_key_pair(self) -> typing.Optional[builtins.str]:
            '''The Amazon EC2 key pair that's used for instances launched in the compute environment.

            You can use this key pair to log in to your instances with SSH. To remove the Amazon EC2 key pair, set this value to an empty string.

            When updating a compute environment, changing the EC2 key pair requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair
            '''
            result = self._values.get("ec2_key_pair")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.

            This parameter is overridden by the ``imageIdOverride`` member of the ``Ec2Configuration`` structure. To remove the custom AMI ID and use the default AMI ID, set this value to an empty string.

            When updating a compute environment, changing the AMI ID requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it. > The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid
            '''
            result = self._values.get("image_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_role(self) -> typing.Optional[builtins.str]:
            '''The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment.

            You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ``*ecsInstanceRole*`` or ``arn:aws:iam:: *<aws_account_id>* :instance-profile/ *ecsInstanceRole*`` . For more information, see `Amazon ECS instance role <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`_ in the *AWS Batch User Guide* .

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole
            '''
            result = self._values.get("instance_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The instances types that can be launched.

            You can specify instance families to launch any instance type within those families (for example, ``c5`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose ``optimal`` to select instance types (from the C4, M4, and R4 instance families) that match the demand of your job queues.

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it. > When you create a compute environment, the instance types that you select for the compute environment must share the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment. > Currently, ``optimal`` uses instance types from the C4, M4, and R4 instance families. In Regions that don't have instance types from those instance families, instance types from the C5, M5, and R5 instance families are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes
            '''
            result = self._values.get("instance_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def launch_template(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.LaunchTemplateSpecificationProperty"]]:
            '''The launch template to use for your compute resources.

            Any other compute resource parameters that you specify in a `CreateComputeEnvironment <https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html>`_ API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see `Launch Template Support <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`_ in the ** . Removing the launch template from a compute environment will not remove the AMI specified in the launch template. In order to update the AMI specified in a launch template, the ``updateToLatestImageVersion`` parameter must be set to ``true`` .

            When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the ** .
            .. epigraph::

               This parameter isn't applicable to jobs running on Fargate resources, and shouldn't be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate
            '''
            result = self._values.get("launch_template")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeEnvironment.LaunchTemplateSpecificationProperty"]], result)

        @builtins.property
        def minv_cpus(self) -> typing.Optional[jsii.Number]:
            '''The minimum number of vCPUs that an environment should maintain (even if the compute environment is ``DISABLED`` ).

            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus
            '''
            result = self._values.get("minv_cpus")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def placement_group(self) -> typing.Optional[builtins.str]:
            '''The Amazon EC2 placement group to associate with your compute resources.

            If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see `Placement groups <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`_ in the *Amazon EC2 User Guide for Linux Instances* .

            When updating a compute environment, changing the placement group requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup
            '''
            result = self._values.get("placement_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Amazon EC2 security groups that are associated with instances launched in the compute environment.

            This parameter is required for Fargate compute resources, where it can contain up to 5 security groups. For Fargate compute resources, providing an empty list is handled as if this parameter wasn't specified and no change is made. For EC2 compute resources, providing an empty list removes the security groups from the compute resource.

            When updating a compute environment, changing the EC2 security groups requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def spot_iam_fleet_role(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment.

            This role is required if the allocation strategy set to ``BEST_FIT`` or if the allocation strategy isn't specified. For more information, see `Amazon EC2 spot fleet role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it. > To tag your Spot Instances on creation, the Spot Fleet IAM role specified here must use the newer *AmazonEC2SpotFleetTaggingRole* managed policy. The previously recommended *AmazonEC2SpotFleetRole* managed policy doesn't have the required permissions to tag Spot Instances. For more information, see `Spot instances not tagged on creation <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#spot-instance-no-tag>`_ in the *AWS Batch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-spotiamfleetrole
            '''
            result = self._values.get("spot_iam_fleet_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
            '''Key-value pair tags to be applied to EC2 resources that are launched in the compute environment.

            For AWS Batch , these take the form of ``"String1": "String2"`` , where ``String1`` is the tag key and ``String2`` is the tag value-for example, ``{ "Name": "Batch Instance - C4OnDemand" }`` . This is helpful for recognizing your Batch instances in the Amazon EC2 console. These tags aren't seen when using the AWS Batch ``ListTagsForResource`` API operation.

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

        @builtins.property
        def update_to_latest_image_version(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the AMI ID is updated to the latest one that's supported by AWS Batch when the compute environment has an infrastructure update.

            The default value is ``false`` .
            .. epigraph::

               An AMI ID can either be specified in the ``imageId`` or ``imageIdOverride`` parameters or be determined by the launch template that's specified in the ``launchTemplate`` parameter. If an AMI ID is specified any of these ways, this parameter is ignored. For more information about to update AMI IDs during an infrastructure update, see `Updating the AMI ID <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html#updating-compute-environments-ami>`_ in the *AWS Batch User Guide* .

            When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion
            '''
            result = self._values.get("update_to_latest_image_version")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_type": "imageType",
            "image_id_override": "imageIdOverride",
            "image_kubernetes_version": "imageKubernetesVersion",
        },
    )
    class Ec2ConfigurationObjectProperty:
        def __init__(
            self,
            *,
            image_type: builtins.str,
            image_id_override: typing.Optional[builtins.str] = None,
            image_kubernetes_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information used to select Amazon Machine Images (AMIs) for instances in the compute environment.

            If ``Ec2Configuration`` isn't specified, the default is ``ECS_AL2`` ( `Amazon Linux 2 <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ ).
            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources.

            :param image_type: The image type to match with the instance type to select an AMI. The supported values are different for ``ECS`` and ``EKS`` resources. - **ECS** - If the ``imageIdOverride`` parameter isn't specified, then a recent `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ ( ``ECS_AL2`` ) is used. If a new image type is specified in an update, but neither an ``imageId`` nor a ``imageIdOverride`` parameter is specified, then the latest Amazon ECS optimized AMI for that image type that's supported by AWS Batch is used. - **ECS_AL2** - `Amazon Linux 2 <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ : Default for all non-GPU instance families. - **ECS_AL2_NVIDIA** - `Amazon Linux 2 (GPU) <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#gpuami>`_ : Default for all GPU instance families (for example ``P4`` and ``G4`` ) and can be used for all non AWS Graviton-based instance types. - **ECS_AL1** - `Amazon Linux <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#alami>`_ . Amazon Linux has reached the end-of-life of standard support. For more information, see `Amazon Linux AMI <https://docs.aws.amazon.com/amazon-linux-ami/>`_ . - **EKS** - If the ``imageIdOverride`` parameter isn't specified, then a recent `Amazon EKS-optimized Amazon Linux AMI <https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html>`_ ( ``EKS_AL2`` ) is used. If a new image type is specified in an update, but neither an ``imageId`` nor a ``imageIdOverride`` parameter is specified, then the latest Amazon EKS optimized AMI for that image type that AWS Batch supports is used. - **EKS_AL2** - `Amazon Linux 2 <https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html>`_ : Default for all non-GPU instance families. - **EKS_AL2_NVIDIA** - `Amazon Linux 2 (accelerated) <https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html>`_ : Default for all GPU instance families (for example, ``P4`` and ``G4`` ) and can be used for all non AWS Graviton-based instance types.
            :param image_id_override: The AMI ID used for instances launched in the compute environment that match the image type. This setting overrides the ``imageId`` set in the ``computeResource`` object. .. epigraph:: The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param image_kubernetes_version: The Kubernetes version for the compute environment. If you don't specify a value, the latest version that AWS Batch supports is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                ec2_configuration_object_property = batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty(
                    image_type="imageType",
                
                    # the properties below are optional
                    image_id_override="imageIdOverride",
                    image_kubernetes_version="imageKubernetesVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce3b98c061a5de7793f276c675aa6c48c626a13d8debc8bf1a12f74113040fcb)
                check_type(argname="argument image_type", value=image_type, expected_type=type_hints["image_type"])
                check_type(argname="argument image_id_override", value=image_id_override, expected_type=type_hints["image_id_override"])
                check_type(argname="argument image_kubernetes_version", value=image_kubernetes_version, expected_type=type_hints["image_kubernetes_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "image_type": image_type,
            }
            if image_id_override is not None:
                self._values["image_id_override"] = image_id_override
            if image_kubernetes_version is not None:
                self._values["image_kubernetes_version"] = image_kubernetes_version

        @builtins.property
        def image_type(self) -> builtins.str:
            '''The image type to match with the instance type to select an AMI.

            The supported values are different for ``ECS`` and ``EKS`` resources.

            - **ECS** - If the ``imageIdOverride`` parameter isn't specified, then a recent `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ ( ``ECS_AL2`` ) is used. If a new image type is specified in an update, but neither an ``imageId`` nor a ``imageIdOverride`` parameter is specified, then the latest Amazon ECS optimized AMI for that image type that's supported by AWS Batch is used.
            - **ECS_AL2** - `Amazon Linux 2 <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`_ : Default for all non-GPU instance families.
            - **ECS_AL2_NVIDIA** - `Amazon Linux 2 (GPU) <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#gpuami>`_ : Default for all GPU instance families (for example ``P4`` and ``G4`` ) and can be used for all non AWS Graviton-based instance types.
            - **ECS_AL1** - `Amazon Linux <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#alami>`_ . Amazon Linux has reached the end-of-life of standard support. For more information, see `Amazon Linux AMI <https://docs.aws.amazon.com/amazon-linux-ami/>`_ .
            - **EKS** - If the ``imageIdOverride`` parameter isn't specified, then a recent `Amazon EKS-optimized Amazon Linux AMI <https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html>`_ ( ``EKS_AL2`` ) is used. If a new image type is specified in an update, but neither an ``imageId`` nor a ``imageIdOverride`` parameter is specified, then the latest Amazon EKS optimized AMI for that image type that AWS Batch supports is used.
            - **EKS_AL2** - `Amazon Linux 2 <https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html>`_ : Default for all non-GPU instance families.
            - **EKS_AL2_NVIDIA** - `Amazon Linux 2 (accelerated) <https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html>`_ : Default for all GPU instance families (for example, ``P4`` and ``G4`` ) and can be used for all non AWS Graviton-based instance types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imagetype
            '''
            result = self._values.get("image_type")
            assert result is not None, "Required property 'image_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_id_override(self) -> typing.Optional[builtins.str]:
            '''The AMI ID used for instances launched in the compute environment that match the image type.

            This setting overrides the ``imageId`` set in the ``computeResource`` object.
            .. epigraph::

               The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see `Amazon ECS-optimized Amazon Linux 2 AMI <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imageidoverride
            '''
            result = self._values.get("image_id_override")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_kubernetes_version(self) -> typing.Optional[builtins.str]:
            '''The Kubernetes version for the compute environment.

            If you don't specify a value, the latest version that AWS Batch supports is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imagekubernetesversion
            '''
            result = self._values.get("image_kubernetes_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ec2ConfigurationObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.EksConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "eks_cluster_arn": "eksClusterArn",
            "kubernetes_namespace": "kubernetesNamespace",
        },
    )
    class EksConfigurationProperty:
        def __init__(
            self,
            *,
            eks_cluster_arn: builtins.str,
            kubernetes_namespace: builtins.str,
        ) -> None:
            '''Configuration for the Amazon EKS cluster that supports the AWS Batch compute environment.

            The cluster must exist before the compute environment can be created.

            :param eks_cluster_arn: The Amazon Resource Name (ARN) of the Amazon EKS cluster. An example is ``arn: *aws* :eks: *us-east-1* : *123456789012* :cluster/ *ClusterForBatch*`` .
            :param kubernetes_namespace: The namespace of the Amazon EKS cluster. AWS Batch manages pods in this namespace. The value can't left empty or null. It must be fewer than 64 characters long, can't be set to ``default`` , can't start with " ``kube-`` ," and must match this regular expression: ``^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`` . For more information, see `Namespaces <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>`_ in the Kubernetes documentation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-eksconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                eks_configuration_property = batch.CfnComputeEnvironment.EksConfigurationProperty(
                    eks_cluster_arn="eksClusterArn",
                    kubernetes_namespace="kubernetesNamespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d01293eced89171b858aec2adc4c3362e7bc583fff04c8572350b492d38c641)
                check_type(argname="argument eks_cluster_arn", value=eks_cluster_arn, expected_type=type_hints["eks_cluster_arn"])
                check_type(argname="argument kubernetes_namespace", value=kubernetes_namespace, expected_type=type_hints["kubernetes_namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "eks_cluster_arn": eks_cluster_arn,
                "kubernetes_namespace": kubernetes_namespace,
            }

        @builtins.property
        def eks_cluster_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon EKS cluster.

            An example is ``arn: *aws* :eks: *us-east-1* : *123456789012* :cluster/ *ClusterForBatch*`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-eksconfiguration.html#cfn-batch-computeenvironment-eksconfiguration-eksclusterarn
            '''
            result = self._values.get("eks_cluster_arn")
            assert result is not None, "Required property 'eks_cluster_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kubernetes_namespace(self) -> builtins.str:
            '''The namespace of the Amazon EKS cluster.

            AWS Batch manages pods in this namespace. The value can't left empty or null. It must be fewer than 64 characters long, can't be set to ``default`` , can't start with " ``kube-`` ," and must match this regular expression: ``^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`` . For more information, see `Namespaces <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>`_ in the Kubernetes documentation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-eksconfiguration.html#cfn-batch-computeenvironment-eksconfiguration-kubernetesnamespace
            '''
            result = self._values.get("kubernetes_namespace")
            assert result is not None, "Required property 'kubernetes_namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "launch_template_id": "launchTemplateId",
            "launch_template_name": "launchTemplateName",
            "version": "version",
        },
    )
    class LaunchTemplateSpecificationProperty:
        def __init__(
            self,
            *,
            launch_template_id: typing.Optional[builtins.str] = None,
            launch_template_name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that represents a launch template that's associated with a compute resource.

            You must specify either the launch template ID or launch template name in the request, but not both.

            If security groups are specified using both the ``securityGroupIds`` parameter of ``CreateComputeEnvironment`` and the launch template, the values in the ``securityGroupIds`` parameter of ``CreateComputeEnvironment`` will be used.
            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources.

            :param launch_template_id: The ID of the launch template.
            :param launch_template_name: The name of the launch template.
            :param version: The version number of the launch template, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , the latest version of the launch template is used. If the value is ``$Default`` , the default version of the launch template is used. .. epigraph:: If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the ``updateToLatestImageVersion`` parameter for the compute environment is set to ``true`` . During an infrastructure update, if either ``$Latest`` or ``$Default`` is specified, AWS Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* . Default: ``$Default`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                launch_template_specification_property = batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e2a48b24f0297afff0df36a352af2f9856ad8fac713d1ecbc2161d0b968651da)
                check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
                check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None:
                self._values["launch_template_name"] = launch_template_name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the launch template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_name(self) -> typing.Optional[builtins.str]:
            '''The name of the launch template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplatename
            '''
            result = self._values.get("launch_template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version number of the launch template, ``$Latest`` , or ``$Default`` .

            If the value is ``$Latest`` , the latest version of the launch template is used. If the value is ``$Default`` , the default version of the launch template is used.
            .. epigraph::

               If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the ``updateToLatestImageVersion`` parameter for the compute environment is set to ``true`` . During an infrastructure update, if either ``$Latest`` or ``$Default`` is specified, AWS Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            Default: ``$Default`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchTemplateSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironment.UpdatePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "job_execution_timeout_minutes": "jobExecutionTimeoutMinutes",
            "terminate_jobs_on_update": "terminateJobsOnUpdate",
        },
    )
    class UpdatePolicyProperty:
        def __init__(
            self,
            *,
            job_execution_timeout_minutes: typing.Optional[jsii.Number] = None,
            terminate_jobs_on_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies the infrastructure update policy for the compute environment.

            For more information about infrastructure updates, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

            :param job_execution_timeout_minutes: Specifies the job timeout (in minutes) when the compute environment infrastructure is updated. The default value is 30. Default: - 30
            :param terminate_jobs_on_update: Specifies whether jobs are automatically terminated when the computer environment infrastructure is updated. The default value is ``false`` . Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                update_policy_property = batch.CfnComputeEnvironment.UpdatePolicyProperty(
                    job_execution_timeout_minutes=123,
                    terminate_jobs_on_update=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f01f930e5e22d80ed490169089dfdbf2f416fdeb6b3ae57212518ae0b70b5e3)
                check_type(argname="argument job_execution_timeout_minutes", value=job_execution_timeout_minutes, expected_type=type_hints["job_execution_timeout_minutes"])
                check_type(argname="argument terminate_jobs_on_update", value=terminate_jobs_on_update, expected_type=type_hints["terminate_jobs_on_update"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if job_execution_timeout_minutes is not None:
                self._values["job_execution_timeout_minutes"] = job_execution_timeout_minutes
            if terminate_jobs_on_update is not None:
                self._values["terminate_jobs_on_update"] = terminate_jobs_on_update

        @builtins.property
        def job_execution_timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''Specifies the job timeout (in minutes) when the compute environment infrastructure is updated.

            The default value is 30.

            :default: - 30

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html#cfn-batch-computeenvironment-updatepolicy-jobexecutiontimeoutminutes
            '''
            result = self._values.get("job_execution_timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def terminate_jobs_on_update(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether jobs are automatically terminated when the computer environment infrastructure is updated.

            The default value is ``false`` .

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html#cfn-batch-computeenvironment-updatepolicy-terminatejobsonupdate
            '''
            result = self._values.get("terminate_jobs_on_update")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdatePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_batch.CfnComputeEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "compute_environment_name": "computeEnvironmentName",
        "compute_resources": "computeResources",
        "eks_configuration": "eksConfiguration",
        "replace_compute_environment": "replaceComputeEnvironment",
        "service_role": "serviceRole",
        "state": "state",
        "tags": "tags",
        "unmanagedv_cpus": "unmanagedvCpus",
        "update_policy": "updatePolicy",
    },
)
class CfnComputeEnvironmentProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        compute_environment_name: typing.Optional[builtins.str] = None,
        compute_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.ComputeResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        eks_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.EksConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        replace_compute_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        service_role: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        unmanagedv_cpus: typing.Optional[jsii.Number] = None,
        update_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.UpdatePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnComputeEnvironment``.

        :param type: The type of the compute environment: ``MANAGED`` or ``UNMANAGED`` . For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .
        :param compute_environment_name: The name for your compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param compute_resources: The ComputeResources property type specifies details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .
        :param eks_configuration: The details for the Amazon EKS cluster that supports the compute environment.
        :param replace_compute_environment: Specifies whether the compute environment is replaced if an update is made that requires replacing the instances in the compute environment. The default value is ``true`` . To enable more properties to be updated, set this property to ``false`` . When changing the value of this property to ``false`` , do not change any other properties at the same time. If other properties are changed at the same time, and the change needs to be rolled back but it can't, it's possible for the stack to go into the ``UPDATE_ROLLBACK_FAILED`` state. You can't update a stack that is in the ``UPDATE_ROLLBACK_FAILED`` state. However, if you can continue to roll it back, you can return the stack to its original settings and then try to update it again. For more information, see `Continue rolling back an update <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`_ in the *AWS CloudFormation User Guide* . The properties that can't be changed without replacing the compute environment are in the ```ComputeResources`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html>`_ property type: ```AllocationStrategy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ , ```BidPercentage`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage>`_ , ```Ec2Configuration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```ImageId`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ , ```InstanceRole`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole>`_ , ```InstanceTypes`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes>`_ , ```LaunchTemplate`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ , ```MaxvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus>`_ , ```MinvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus>`_ , ```PlacementGroup`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup>`_ , ```SecurityGroupIds`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids>`_ , ```Subnets`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets>`_ , `Tags <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags>`_ , ```Type`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type>`_ , and ```UpdateToLatestImageVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ . Default: - true
        :param service_role: The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf. For more information, see `AWS Batch service IAM role <https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html>`_ in the *AWS Batch User Guide* . .. epigraph:: If your account already created the AWS Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the AWS Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the AWS Batch service-linked role in your account. If your specified role has a path other than ``/`` , then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` , specify ``/foo/bar`` as the role name. For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* . .. epigraph:: Depending on how you created your AWS Batch service role, its ARN might contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
        :param state: The state of the compute environment. If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues. If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand. If the state is ``DISABLED`` , then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state don't scale out. .. epigraph:: Compute environments in a ``DISABLED`` state may continue to incur billing charges. To prevent additional charges, turn off and then delete the compute environment. For more information, see `State <https://docs.aws.amazon.com/batch/latest/userguide/compute_environment_parameters.html#compute_environment_state>`_ in the *AWS Batch User Guide* . When an instance is idle, the instance scales down to the ``minvCpus`` value. However, the instance size doesn't change. For example, consider a ``c5.8xlarge`` instance with a ``minvCpus`` value of ``4`` and a ``desiredvCpus`` value of ``36`` . This instance doesn't scale down to a ``c5.large`` instance.
        :param tags: The tags applied to the compute environment.
        :param unmanagedv_cpus: The maximum number of vCPUs for an unmanaged compute environment. This parameter is only used for fair share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair share job queue, no vCPU capacity is reserved. .. epigraph:: This parameter is only supported when the ``type`` parameter is set to ``UNMANAGED`` .
        :param update_policy: Specifies the infrastructure update policy for the compute environment. For more information about infrastructure updates, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_batch as batch
            
            cfn_compute_environment_props = batch.CfnComputeEnvironmentProps(
                type="type",
            
                # the properties below are optional
                compute_environment_name="computeEnvironmentName",
                compute_resources=batch.CfnComputeEnvironment.ComputeResourcesProperty(
                    maxv_cpus=123,
                    subnets=["subnets"],
                    type="type",
            
                    # the properties below are optional
                    allocation_strategy="allocationStrategy",
                    bid_percentage=123,
                    desiredv_cpus=123,
                    ec2_configuration=[batch.CfnComputeEnvironment.Ec2ConfigurationObjectProperty(
                        image_type="imageType",
            
                        # the properties below are optional
                        image_id_override="imageIdOverride",
                        image_kubernetes_version="imageKubernetesVersion"
                    )],
                    ec2_key_pair="ec2KeyPair",
                    image_id="imageId",
                    instance_role="instanceRole",
                    instance_types=["instanceTypes"],
                    launch_template=batch.CfnComputeEnvironment.LaunchTemplateSpecificationProperty(
                        launch_template_id="launchTemplateId",
                        launch_template_name="launchTemplateName",
                        version="version"
                    ),
                    minv_cpus=123,
                    placement_group="placementGroup",
                    security_group_ids=["securityGroupIds"],
                    spot_iam_fleet_role="spotIamFleetRole",
                    tags={
                        "tags_key": "tags"
                    },
                    update_to_latest_image_version=False
                ),
                eks_configuration=batch.CfnComputeEnvironment.EksConfigurationProperty(
                    eks_cluster_arn="eksClusterArn",
                    kubernetes_namespace="kubernetesNamespace"
                ),
                replace_compute_environment=False,
                service_role="serviceRole",
                state="state",
                tags={
                    "tags_key": "tags"
                },
                unmanagedv_cpus=123,
                update_policy=batch.CfnComputeEnvironment.UpdatePolicyProperty(
                    job_execution_timeout_minutes=123,
                    terminate_jobs_on_update=False
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a81ed1de03c840384ae49a0a4dbeb244507d2327c304fc093af8d720954eb257)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument compute_environment_name", value=compute_environment_name, expected_type=type_hints["compute_environment_name"])
            check_type(argname="argument compute_resources", value=compute_resources, expected_type=type_hints["compute_resources"])
            check_type(argname="argument eks_configuration", value=eks_configuration, expected_type=type_hints["eks_configuration"])
            check_type(argname="argument replace_compute_environment", value=replace_compute_environment, expected_type=type_hints["replace_compute_environment"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument unmanagedv_cpus", value=unmanagedv_cpus, expected_type=type_hints["unmanagedv_cpus"])
            check_type(argname="argument update_policy", value=update_policy, expected_type=type_hints["update_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if compute_environment_name is not None:
            self._values["compute_environment_name"] = compute_environment_name
        if compute_resources is not None:
            self._values["compute_resources"] = compute_resources
        if eks_configuration is not None:
            self._values["eks_configuration"] = eks_configuration
        if replace_compute_environment is not None:
            self._values["replace_compute_environment"] = replace_compute_environment
        if service_role is not None:
            self._values["service_role"] = service_role
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if unmanagedv_cpus is not None:
            self._values["unmanagedv_cpus"] = unmanagedv_cpus
        if update_policy is not None:
            self._values["update_policy"] = update_policy

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the compute environment: ``MANAGED`` or ``UNMANAGED`` .

        For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the *AWS Batch User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compute_environment_name(self) -> typing.Optional[builtins.str]:
        '''The name for your compute environment.

        It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-computeenvironmentname
        '''
        result = self._values.get("compute_environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compute_resources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.ComputeResourcesProperty]]:
        '''The ComputeResources property type specifies details of the compute resources managed by the compute environment.

        This parameter is required for managed compute environments. For more information, see `Compute Environments <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`_ in the ** .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-computeresources
        '''
        result = self._values.get("compute_resources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.ComputeResourcesProperty]], result)

    @builtins.property
    def eks_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.EksConfigurationProperty]]:
        '''The details for the Amazon EKS cluster that supports the compute environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-eksconfiguration
        '''
        result = self._values.get("eks_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.EksConfigurationProperty]], result)

    @builtins.property
    def replace_compute_environment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the compute environment is replaced if an update is made that requires replacing the instances in the compute environment.

        The default value is ``true`` . To enable more properties to be updated, set this property to ``false`` . When changing the value of this property to ``false`` , do not change any other properties at the same time. If other properties are changed at the same time, and the change needs to be rolled back but it can't, it's possible for the stack to go into the ``UPDATE_ROLLBACK_FAILED`` state. You can't update a stack that is in the ``UPDATE_ROLLBACK_FAILED`` state. However, if you can continue to roll it back, you can return the stack to its original settings and then try to update it again. For more information, see `Continue rolling back an update <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`_ in the *AWS CloudFormation User Guide* .

        The properties that can't be changed without replacing the compute environment are in the ```ComputeResources`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html>`_ property type: ```AllocationStrategy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy>`_ , ```BidPercentage`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage>`_ , ```Ec2Configuration`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```Ec2KeyPair`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair>`_ , ```ImageId`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid>`_ , ```InstanceRole`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole>`_ , ```InstanceTypes`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes>`_ , ```LaunchTemplate`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate>`_ , ```MaxvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus>`_ , ```MinvCpus`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus>`_ , ```PlacementGroup`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup>`_ , ```SecurityGroupIds`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids>`_ , ```Subnets`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets>`_ , `Tags <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags>`_ , ```Type`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type>`_ , and ```UpdateToLatestImageVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion>`_ .

        :default: - true

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-replacecomputeenvironment
        '''
        result = self._values.get("replace_compute_environment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def service_role(self) -> typing.Optional[builtins.str]:
        '''The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

        For more information, see `AWS Batch service IAM role <https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html>`_ in the *AWS Batch User Guide* .
        .. epigraph::

           If your account already created the AWS Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the AWS Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the AWS Batch service-linked role in your account.

        If your specified role has a path other than ``/`` , then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` , specify ``/foo/bar`` as the role name. For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* .
        .. epigraph::

           Depending on how you created your AWS Batch service role, its ARN might contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN doesn't use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-servicerole
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the compute environment.

        If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.

        If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.

        If the state is ``DISABLED`` , then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state don't scale out.
        .. epigraph::

           Compute environments in a ``DISABLED`` state may continue to incur billing charges. To prevent additional charges, turn off and then delete the compute environment. For more information, see `State <https://docs.aws.amazon.com/batch/latest/userguide/compute_environment_parameters.html#compute_environment_state>`_ in the *AWS Batch User Guide* .

        When an instance is idle, the instance scales down to the ``minvCpus`` value. However, the instance size doesn't change. For example, consider a ``c5.8xlarge`` instance with a ``minvCpus`` value of ``4`` and a ``desiredvCpus`` value of ``36`` . This instance doesn't scale down to a ``c5.large`` instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags applied to the compute environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def unmanagedv_cpus(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of vCPUs for an unmanaged compute environment.

        This parameter is only used for fair share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair share job queue, no vCPU capacity is reserved.
        .. epigraph::

           This parameter is only supported when the ``type`` parameter is set to ``UNMANAGED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-unmanagedvcpus
        '''
        result = self._values.get("unmanagedv_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def update_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.UpdatePolicyProperty]]:
        '''Specifies the infrastructure update policy for the compute environment.

        For more information about infrastructure updates, see `Updating compute environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`_ in the *AWS Batch User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-updatepolicy
        '''
        result = self._values.get("update_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.UpdatePolicyProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComputeEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnJobDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition",
):
    '''The ``AWS::Batch::JobDefinition`` resource specifies the parameters for an AWS Batch job definition.

    For more information, see `Job Definitions <https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html>`_ in the ** .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_batch as batch
        
        # labels: Any
        # limits: Any
        # options: Any
        # parameters: Any
        # requests: Any
        # tags: Any
        
        cfn_job_definition = batch.CfnJobDefinition(self, "MyCfnJobDefinition",
            type="type",
        
            # the properties below are optional
            container_properties=batch.CfnJobDefinition.ContainerPropertiesProperty(
                image="image",
        
                # the properties below are optional
                command=["command"],
                environment=[batch.CfnJobDefinition.EnvironmentProperty(
                    name="name",
                    value="value"
                )],
                ephemeral_storage=batch.CfnJobDefinition.EphemeralStorageProperty(
                    size_in_gi_b=123
                ),
                execution_role_arn="executionRoleArn",
                fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                    platform_version="platformVersion"
                ),
                instance_type="instanceType",
                job_role_arn="jobRoleArn",
                linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                    devices=[batch.CfnJobDefinition.DeviceProperty(
                        container_path="containerPath",
                        host_path="hostPath",
                        permissions=["permissions"]
                    )],
                    init_process_enabled=False,
                    max_swap=123,
                    shared_memory_size=123,
                    swappiness=123,
                    tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                        container_path="containerPath",
                        size=123,
        
                        # the properties below are optional
                        mount_options=["mountOptions"]
                    )]
                ),
                log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                    log_driver="logDriver",
        
                    # the properties below are optional
                    options=options,
                    secret_options=[batch.CfnJobDefinition.SecretProperty(
                        name="name",
                        value_from="valueFrom"
                    )]
                ),
                memory=123,
                mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                    container_path="containerPath",
                    read_only=False,
                    source_volume="sourceVolume"
                )],
                network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                    assign_public_ip="assignPublicIp"
                ),
                privileged=False,
                readonly_root_filesystem=False,
                resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                    type="type",
                    value="value"
                )],
                runtime_platform=batch.CfnJobDefinition.RuntimePlatformProperty(
                    cpu_architecture="cpuArchitecture",
                    operating_system_family="operatingSystemFamily"
                ),
                secrets=[batch.CfnJobDefinition.SecretProperty(
                    name="name",
                    value_from="valueFrom"
                )],
                ulimits=[batch.CfnJobDefinition.UlimitProperty(
                    hard_limit=123,
                    name="name",
                    soft_limit=123
                )],
                user="user",
                vcpus=123,
                volumes=[batch.CfnJobDefinition.VolumesProperty(
                    efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                        file_system_id="fileSystemId",
        
                        # the properties below are optional
                        authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                            access_point_id="accessPointId",
                            iam="iam"
                        ),
                        root_directory="rootDirectory",
                        transit_encryption="transitEncryption",
                        transit_encryption_port=123
                    ),
                    host=batch.CfnJobDefinition.VolumesHostProperty(
                        source_path="sourcePath"
                    ),
                    name="name"
                )]
            ),
            eks_properties=batch.CfnJobDefinition.EksPropertiesProperty(
                pod_properties=batch.CfnJobDefinition.PodPropertiesProperty(
                    containers=[batch.CfnJobDefinition.EksContainerProperty(
                        image="image",
        
                        # the properties below are optional
                        args=["args"],
                        command=["command"],
                        env=[batch.CfnJobDefinition.EksContainerEnvironmentVariableProperty(
                            name="name",
        
                            # the properties below are optional
                            value="value"
                        )],
                        image_pull_policy="imagePullPolicy",
                        name="name",
                        resources=batch.CfnJobDefinition.ResourcesProperty(
                            limits=limits,
                            requests=requests
                        ),
                        security_context=batch.CfnJobDefinition.SecurityContextProperty(
                            privileged=False,
                            read_only_root_filesystem=False,
                            run_as_group=123,
                            run_as_non_root=False,
                            run_as_user=123
                        ),
                        volume_mounts=[batch.CfnJobDefinition.EksContainerVolumeMountProperty(
                            mount_path="mountPath",
                            name="name",
                            read_only=False
                        )]
                    )],
                    dns_policy="dnsPolicy",
                    host_network=False,
                    metadata=batch.CfnJobDefinition.MetadataProperty(
                        labels=labels
                    ),
                    service_account_name="serviceAccountName",
                    volumes=[batch.CfnJobDefinition.EksVolumeProperty(
                        name="name",
        
                        # the properties below are optional
                        empty_dir=batch.CfnJobDefinition.EmptyDirProperty(
                            medium="medium",
                            size_limit="sizeLimit"
                        ),
                        host_path=batch.CfnJobDefinition.HostPathProperty(
                            path="path"
                        ),
                        secret=batch.CfnJobDefinition.EksSecretProperty(
                            secret_name="secretName",
        
                            # the properties below are optional
                            optional=False
                        )
                    )]
                )
            ),
            job_definition_name="jobDefinitionName",
            node_properties=batch.CfnJobDefinition.NodePropertiesProperty(
                main_node=123,
                node_range_properties=[batch.CfnJobDefinition.NodeRangePropertyProperty(
                    target_nodes="targetNodes",
        
                    # the properties below are optional
                    container=batch.CfnJobDefinition.ContainerPropertiesProperty(
                        image="image",
        
                        # the properties below are optional
                        command=["command"],
                        environment=[batch.CfnJobDefinition.EnvironmentProperty(
                            name="name",
                            value="value"
                        )],
                        ephemeral_storage=batch.CfnJobDefinition.EphemeralStorageProperty(
                            size_in_gi_b=123
                        ),
                        execution_role_arn="executionRoleArn",
                        fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                            platform_version="platformVersion"
                        ),
                        instance_type="instanceType",
                        job_role_arn="jobRoleArn",
                        linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                            devices=[batch.CfnJobDefinition.DeviceProperty(
                                container_path="containerPath",
                                host_path="hostPath",
                                permissions=["permissions"]
                            )],
                            init_process_enabled=False,
                            max_swap=123,
                            shared_memory_size=123,
                            swappiness=123,
                            tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                                container_path="containerPath",
                                size=123,
        
                                # the properties below are optional
                                mount_options=["mountOptions"]
                            )]
                        ),
                        log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                            log_driver="logDriver",
        
                            # the properties below are optional
                            options=options,
                            secret_options=[batch.CfnJobDefinition.SecretProperty(
                                name="name",
                                value_from="valueFrom"
                            )]
                        ),
                        memory=123,
                        mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                            container_path="containerPath",
                            read_only=False,
                            source_volume="sourceVolume"
                        )],
                        network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                            assign_public_ip="assignPublicIp"
                        ),
                        privileged=False,
                        readonly_root_filesystem=False,
                        resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                            type="type",
                            value="value"
                        )],
                        runtime_platform=batch.CfnJobDefinition.RuntimePlatformProperty(
                            cpu_architecture="cpuArchitecture",
                            operating_system_family="operatingSystemFamily"
                        ),
                        secrets=[batch.CfnJobDefinition.SecretProperty(
                            name="name",
                            value_from="valueFrom"
                        )],
                        ulimits=[batch.CfnJobDefinition.UlimitProperty(
                            hard_limit=123,
                            name="name",
                            soft_limit=123
                        )],
                        user="user",
                        vcpus=123,
                        volumes=[batch.CfnJobDefinition.VolumesProperty(
                            efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                                file_system_id="fileSystemId",
        
                                # the properties below are optional
                                authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                    access_point_id="accessPointId",
                                    iam="iam"
                                ),
                                root_directory="rootDirectory",
                                transit_encryption="transitEncryption",
                                transit_encryption_port=123
                            ),
                            host=batch.CfnJobDefinition.VolumesHostProperty(
                                source_path="sourcePath"
                            ),
                            name="name"
                        )]
                    )
                )],
                num_nodes=123
            ),
            parameters=parameters,
            platform_capabilities=["platformCapabilities"],
            propagate_tags=False,
            retry_strategy=batch.CfnJobDefinition.RetryStrategyProperty(
                attempts=123,
                evaluate_on_exit=[batch.CfnJobDefinition.EvaluateOnExitProperty(
                    action="action",
        
                    # the properties below are optional
                    on_exit_code="onExitCode",
                    on_reason="onReason",
                    on_status_reason="onStatusReason"
                )]
            ),
            scheduling_priority=123,
            tags=tags,
            timeout=batch.CfnJobDefinition.TimeoutProperty(
                attempt_duration_seconds=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        container_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.ContainerPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        eks_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EksPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        job_definition_name: typing.Optional[builtins.str] = None,
        node_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.NodePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        parameters: typing.Any = None,
        platform_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        propagate_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        retry_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.RetryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        scheduling_priority: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        timeout: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.TimeoutProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param type: The type of job definition. For more information about multi-node parallel jobs, see `Creating a multi-node parallel job definition <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html>`_ in the *AWS Batch User Guide* . .. epigraph:: If the job is run on Fargate resources, then ``multinode`` isn't supported.
        :param container_properties: An object with various properties specific to Amazon ECS based jobs. Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified.
        :param eks_properties: An object with various properties that are specific to Amazon EKS based jobs. Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified.
        :param job_definition_name: The name of the job definition.
        :param node_properties: An object with various properties that are specific to multi-node parallel jobs. Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified. .. epigraph:: If the job runs on Fargate resources, don't specify ``nodeProperties`` . Use ``containerProperties`` instead.
        :param parameters: Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see `Job definition parameters <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`_ in the *AWS Batch User Guide* .
        :param platform_capabilities: The platform capabilities required by the job definition. If no value is specified, it defaults to ``EC2`` . Jobs run on Fargate resources specify ``FARGATE`` .
        :param propagate_tags: Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the ``FAILED`` state.
        :param retry_strategy: The retry strategy to use for failed jobs that are submitted with this job definition.
        :param scheduling_priority: The scheduling priority of the job definition. This only affects jobs in job queues with a fair share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.
        :param tags: The tags that are applied to the job definition.
        :param timeout: The timeout time for jobs that are submitted with this job definition. After the amount of time you specify passes, AWS Batch terminates your jobs if they aren't finished.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37959c68856ab28ea1a57515db976bc2215806d52c75f6166834df6ae651417f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobDefinitionProps(
            type=type,
            container_properties=container_properties,
            eks_properties=eks_properties,
            job_definition_name=job_definition_name,
            node_properties=node_properties,
            parameters=parameters,
            platform_capabilities=platform_capabilities,
            propagate_tags=propagate_tags,
            retry_strategy=retry_strategy,
            scheduling_priority=scheduling_priority,
            tags=tags,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84b6af858f7642dbc10029a34c2ed90c61a840b3c9d8a639fbe0690b4aa593d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__710ae17567654ca123f279efb5ee033134bde1c49217d5abca4db2e98435f076)
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
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of job definition.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c96b92c09c064b55548b6669735edc8ffa8187ffae08746200ea2113f36cdcc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="containerProperties")
    def container_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ContainerPropertiesProperty"]]:
        '''An object with various properties specific to Amazon ECS based jobs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ContainerPropertiesProperty"]], jsii.get(self, "containerProperties"))

    @container_properties.setter
    def container_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ContainerPropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69a394e899a3c712c6499f6fcffa98702eb3ab7de5e4489e6e69fb85ae55491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerProperties", value)

    @builtins.property
    @jsii.member(jsii_name="eksProperties")
    def eks_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksPropertiesProperty"]]:
        '''An object with various properties that are specific to Amazon EKS based jobs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksPropertiesProperty"]], jsii.get(self, "eksProperties"))

    @eks_properties.setter
    def eks_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksPropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca04be0ba694eb2f262cad48402ba7bf94953530d02c650e2679b1f91498c346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eksProperties", value)

    @builtins.property
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job definition.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f628b65bca30d37b13950af18cab324471321abe3a2e97c363552c0adbe924)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property
    @jsii.member(jsii_name="nodeProperties")
    def node_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.NodePropertiesProperty"]]:
        '''An object with various properties that are specific to multi-node parallel jobs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.NodePropertiesProperty"]], jsii.get(self, "nodeProperties"))

    @node_properties.setter
    def node_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.NodePropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9d18dd3dda5e5761ec3a8f3c7af96598c179ac9f1bca0af0078b6aee12c880b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeProperties", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''Default parameters or parameter substitution placeholders that are set in the job definition.'''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dfa67937c5c5c585d3dedec8653cb0633c802b99afaa23545e8fcc71bf4ef88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="platformCapabilities")
    def platform_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The platform capabilities required by the job definition.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "platformCapabilities"))

    @platform_capabilities.setter
    def platform_capabilities(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df387fd03e7b9707eac2330bd1c2776f56a71ead17f60e9cc8606c21591b2cca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__269e7fe24ddc93928c4ed8726528871fc789de7275942860c547acd761f99025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value)

    @builtins.property
    @jsii.member(jsii_name="retryStrategy")
    def retry_strategy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.RetryStrategyProperty"]]:
        '''The retry strategy to use for failed jobs that are submitted with this job definition.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.RetryStrategyProperty"]], jsii.get(self, "retryStrategy"))

    @retry_strategy.setter
    def retry_strategy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.RetryStrategyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ac615dba37cd2b5a6e9d6f8cdd4b6beef51ff826d65fe0b5cdc31685de03def)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="schedulingPriority")
    def scheduling_priority(self) -> typing.Optional[jsii.Number]:
        '''The scheduling priority of the job definition.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "schedulingPriority"))

    @scheduling_priority.setter
    def scheduling_priority(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba2bfccdff2acf2f90d4e7a4965d8dcb1ae572e2c9cbd92260bf928e42d7e01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingPriority", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The tags that are applied to the job definition.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e523eed1bbd28b55b217e2df4a08d397d7fea1eab9961fca2a86f1f43fb0631f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.TimeoutProperty"]]:
        '''The timeout time for jobs that are submitted with this job definition.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.TimeoutProperty"]], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.TimeoutProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa7b04ecd9d9f8e9c609d704cda9a2176a378049913a70b741c06702f6586c79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.AuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"access_point_id": "accessPointId", "iam": "iam"},
    )
    class AuthorizationConfigProperty:
        def __init__(
            self,
            *,
            access_point_id: typing.Optional[builtins.str] = None,
            iam: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The authorization configuration details for the Amazon EFS file system.

            :param access_point_id: The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the ``EFSVolumeConfiguration`` must either be omitted or set to ``/`` which enforces the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the ``EFSVolumeConfiguration`` . For more information, see `Working with Amazon EFS access points <https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html>`_ in the *Amazon Elastic File System User Guide* .
            :param iam: Whether or not to use the AWS Batch job IAM role defined in a job definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the ``EFSVolumeConfiguration`` . If this parameter is omitted, the default value of ``DISABLED`` is used. For more information, see `Using Amazon EFS access points <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints>`_ in the *AWS Batch User Guide* . EFS IAM authorization requires that ``TransitEncryption`` be ``ENABLED`` and that a ``JobRoleArn`` is specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                authorization_config_property = batch.CfnJobDefinition.AuthorizationConfigProperty(
                    access_point_id="accessPointId",
                    iam="iam"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a944ff69de809bc564eb18b81b5fe5aaf841b525a61c70b907da2a96bd8d9b10)
                check_type(argname="argument access_point_id", value=access_point_id, expected_type=type_hints["access_point_id"])
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_point_id is not None:
                self._values["access_point_id"] = access_point_id
            if iam is not None:
                self._values["iam"] = iam

        @builtins.property
        def access_point_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon EFS access point ID to use.

            If an access point is specified, the root directory value specified in the ``EFSVolumeConfiguration`` must either be omitted or set to ``/`` which enforces the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the ``EFSVolumeConfiguration`` . For more information, see `Working with Amazon EFS access points <https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html>`_ in the *Amazon Elastic File System User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html#cfn-batch-jobdefinition-authorizationconfig-accesspointid
            '''
            result = self._values.get("access_point_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iam(self) -> typing.Optional[builtins.str]:
            '''Whether or not to use the AWS Batch job IAM role defined in a job definition when mounting the Amazon EFS file system.

            If enabled, transit encryption must be enabled in the ``EFSVolumeConfiguration`` . If this parameter is omitted, the default value of ``DISABLED`` is used. For more information, see `Using Amazon EFS access points <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints>`_ in the *AWS Batch User Guide* . EFS IAM authorization requires that ``TransitEncryption`` be ``ENABLED`` and that a ``JobRoleArn`` is specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html#cfn-batch-jobdefinition-authorizationconfig-iam
            '''
            result = self._values.get("iam")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.ContainerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image": "image",
            "command": "command",
            "environment": "environment",
            "ephemeral_storage": "ephemeralStorage",
            "execution_role_arn": "executionRoleArn",
            "fargate_platform_configuration": "fargatePlatformConfiguration",
            "instance_type": "instanceType",
            "job_role_arn": "jobRoleArn",
            "linux_parameters": "linuxParameters",
            "log_configuration": "logConfiguration",
            "memory": "memory",
            "mount_points": "mountPoints",
            "network_configuration": "networkConfiguration",
            "privileged": "privileged",
            "readonly_root_filesystem": "readonlyRootFilesystem",
            "resource_requirements": "resourceRequirements",
            "runtime_platform": "runtimePlatform",
            "secrets": "secrets",
            "ulimits": "ulimits",
            "user": "user",
            "vcpus": "vcpus",
            "volumes": "volumes",
        },
    )
    class ContainerPropertiesProperty:
        def __init__(
            self,
            *,
            image: builtins.str,
            command: typing.Optional[typing.Sequence[builtins.str]] = None,
            environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EnvironmentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ephemeral_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EphemeralStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            execution_role_arn: typing.Optional[builtins.str] = None,
            fargate_platform_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.FargatePlatformConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            instance_type: typing.Optional[builtins.str] = None,
            job_role_arn: typing.Optional[builtins.str] = None,
            linux_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.LinuxParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            memory: typing.Optional[jsii.Number] = None,
            mount_points: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.MountPointsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            privileged: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            readonly_root_filesystem: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            resource_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.ResourceRequirementProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            runtime_platform: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.RuntimePlatformProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            secrets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.SecretProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ulimits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.UlimitProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            user: typing.Optional[builtins.str] = None,
            vcpus: typing.Optional[jsii.Number] = None,
            volumes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.VolumesProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Container properties are used for Amazon ECS based job definitions.

            These properties to describe the container that's launched as part of a job.

            :param image: The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with ``*repository-url* / *image* : *tag*`` . It can be 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), underscores (_), colons (:), periods (.), forward slashes (/), and number signs (#). This parameter maps to ``Image`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``IMAGE`` parameter of `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: Docker image architecture must match the processor architecture of the compute resources that they're scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources. - Images in Amazon ECR Public repositories use the full ``registry/repository[:tag]`` or ``registry/repository[@digest]`` naming conventions. For example, ``public.ecr.aws/ *registry_alias* / *my-web-app* : *latest*`` . - Images in Amazon ECR repositories use the full registry and repository URI (for example, ``123456789012.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ). - Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). - Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). - Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ).
            :param command: The command that's passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``COMMAND`` parameter to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . For more information, see `https://docs.docker.com/engine/reference/builder/#cmd <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/builder/#cmd>`_ .
            :param environment: The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--env`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: We don't recommend using plaintext environment variables for sensitive information, such as credential data. > Environment variables cannot start with " ``AWS_BATCH`` ". This naming convention is reserved for variables that AWS Batch sets.
            :param ephemeral_storage: The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate .
            :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see `AWS Batch execution IAM role <https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html>`_ in the *AWS Batch User Guide* .
            :param fargate_platform_configuration: The platform configuration for jobs that are running on Fargate resources. Jobs that are running on EC2 resources must not specify this parameter.
            :param instance_type: The instance type to use for a multi-node parallel job. All node groups in a multi-node parallel job must use the same instance type. .. epigraph:: This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.
            :param job_role_arn: The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions. For more information, see `IAM roles for tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param linux_parameters: Linux-specific modifications that are applied to the container, such as details for device mappings.
            :param log_configuration: The log configuration specification for the container. This parameter maps to ``LogConfig`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--log-driver`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.aws.amazon.com/https://docs.docker.com/engine/admin/logging/overview/>`_ in the Docker documentation. .. epigraph:: AWS Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the ``LogConfiguration`` data type). This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"`` .. epigraph:: The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS container agent configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param memory: This parameter is deprecated, use ``resourceRequirements`` to specify the memory requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, it's terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.
            :param mount_points: The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--volume`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            :param network_configuration: The network configuration for jobs that are running on Fargate resources. Jobs that are running on EC2 resources must not specify this parameter.
            :param privileged: When this parameter is true, the container is given elevated permissions on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--privileged`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . The default value is false. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as false.
            :param readonly_root_filesystem: When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--read-only`` option to ``docker run`` .
            :param resource_requirements: The type and amount of resources to assign to a container. The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .
            :param runtime_platform: 
            :param secrets: The secrets for the container. For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .
            :param ulimits: A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--ulimit`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
            :param user: The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--user`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            :param vcpus: This parameter is deprecated, use ``resourceRequirements`` to specify the vCPU requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs running on EC2 resources, it specifies the number of vCPUs reserved for the job. Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.
            :param volumes: A list of data volumes used in a job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # options: Any
                
                container_properties_property = batch.CfnJobDefinition.ContainerPropertiesProperty(
                    image="image",
                
                    # the properties below are optional
                    command=["command"],
                    environment=[batch.CfnJobDefinition.EnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    ephemeral_storage=batch.CfnJobDefinition.EphemeralStorageProperty(
                        size_in_gi_b=123
                    ),
                    execution_role_arn="executionRoleArn",
                    fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                        platform_version="platformVersion"
                    ),
                    instance_type="instanceType",
                    job_role_arn="jobRoleArn",
                    linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                        devices=[batch.CfnJobDefinition.DeviceProperty(
                            container_path="containerPath",
                            host_path="hostPath",
                            permissions=["permissions"]
                        )],
                        init_process_enabled=False,
                        max_swap=123,
                        shared_memory_size=123,
                        swappiness=123,
                        tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                            container_path="containerPath",
                            size=123,
                
                            # the properties below are optional
                            mount_options=["mountOptions"]
                        )]
                    ),
                    log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                        log_driver="logDriver",
                
                        # the properties below are optional
                        options=options,
                        secret_options=[batch.CfnJobDefinition.SecretProperty(
                            name="name",
                            value_from="valueFrom"
                        )]
                    ),
                    memory=123,
                    mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                        container_path="containerPath",
                        read_only=False,
                        source_volume="sourceVolume"
                    )],
                    network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                        assign_public_ip="assignPublicIp"
                    ),
                    privileged=False,
                    readonly_root_filesystem=False,
                    resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                        type="type",
                        value="value"
                    )],
                    runtime_platform=batch.CfnJobDefinition.RuntimePlatformProperty(
                        cpu_architecture="cpuArchitecture",
                        operating_system_family="operatingSystemFamily"
                    ),
                    secrets=[batch.CfnJobDefinition.SecretProperty(
                        name="name",
                        value_from="valueFrom"
                    )],
                    ulimits=[batch.CfnJobDefinition.UlimitProperty(
                        hard_limit=123,
                        name="name",
                        soft_limit=123
                    )],
                    user="user",
                    vcpus=123,
                    volumes=[batch.CfnJobDefinition.VolumesProperty(
                        efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                            file_system_id="fileSystemId",
                
                            # the properties below are optional
                            authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                access_point_id="accessPointId",
                                iam="iam"
                            ),
                            root_directory="rootDirectory",
                            transit_encryption="transitEncryption",
                            transit_encryption_port=123
                        ),
                        host=batch.CfnJobDefinition.VolumesHostProperty(
                            source_path="sourcePath"
                        ),
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09b3c38642739790560033cae597f009c106d353ddc5faf85f6a7bf4891ac4d1)
                check_type(argname="argument image", value=image, expected_type=type_hints["image"])
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
                check_type(argname="argument ephemeral_storage", value=ephemeral_storage, expected_type=type_hints["ephemeral_storage"])
                check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
                check_type(argname="argument fargate_platform_configuration", value=fargate_platform_configuration, expected_type=type_hints["fargate_platform_configuration"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument job_role_arn", value=job_role_arn, expected_type=type_hints["job_role_arn"])
                check_type(argname="argument linux_parameters", value=linux_parameters, expected_type=type_hints["linux_parameters"])
                check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
                check_type(argname="argument mount_points", value=mount_points, expected_type=type_hints["mount_points"])
                check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
                check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
                check_type(argname="argument readonly_root_filesystem", value=readonly_root_filesystem, expected_type=type_hints["readonly_root_filesystem"])
                check_type(argname="argument resource_requirements", value=resource_requirements, expected_type=type_hints["resource_requirements"])
                check_type(argname="argument runtime_platform", value=runtime_platform, expected_type=type_hints["runtime_platform"])
                check_type(argname="argument secrets", value=secrets, expected_type=type_hints["secrets"])
                check_type(argname="argument ulimits", value=ulimits, expected_type=type_hints["ulimits"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
                check_type(argname="argument vcpus", value=vcpus, expected_type=type_hints["vcpus"])
                check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "image": image,
            }
            if command is not None:
                self._values["command"] = command
            if environment is not None:
                self._values["environment"] = environment
            if ephemeral_storage is not None:
                self._values["ephemeral_storage"] = ephemeral_storage
            if execution_role_arn is not None:
                self._values["execution_role_arn"] = execution_role_arn
            if fargate_platform_configuration is not None:
                self._values["fargate_platform_configuration"] = fargate_platform_configuration
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if job_role_arn is not None:
                self._values["job_role_arn"] = job_role_arn
            if linux_parameters is not None:
                self._values["linux_parameters"] = linux_parameters
            if log_configuration is not None:
                self._values["log_configuration"] = log_configuration
            if memory is not None:
                self._values["memory"] = memory
            if mount_points is not None:
                self._values["mount_points"] = mount_points
            if network_configuration is not None:
                self._values["network_configuration"] = network_configuration
            if privileged is not None:
                self._values["privileged"] = privileged
            if readonly_root_filesystem is not None:
                self._values["readonly_root_filesystem"] = readonly_root_filesystem
            if resource_requirements is not None:
                self._values["resource_requirements"] = resource_requirements
            if runtime_platform is not None:
                self._values["runtime_platform"] = runtime_platform
            if secrets is not None:
                self._values["secrets"] = secrets
            if ulimits is not None:
                self._values["ulimits"] = ulimits
            if user is not None:
                self._values["user"] = user
            if vcpus is not None:
                self._values["vcpus"] = vcpus
            if volumes is not None:
                self._values["volumes"] = volumes

        @builtins.property
        def image(self) -> builtins.str:
            '''The image used to start a container.

            This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with ``*repository-url* / *image* : *tag*`` . It can be 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), underscores (_), colons (:), periods (.), forward slashes (/), and number signs (#). This parameter maps to ``Image`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``IMAGE`` parameter of `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               Docker image architecture must match the processor architecture of the compute resources that they're scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.

            - Images in Amazon ECR Public repositories use the full ``registry/repository[:tag]`` or ``registry/repository[@digest]`` naming conventions. For example, ``public.ecr.aws/ *registry_alias* / *my-web-app* : *latest*`` .
            - Images in Amazon ECR repositories use the full registry and repository URI (for example, ``123456789012.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).
            - Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ).
            - Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ).
            - Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-image
            '''
            result = self._values.get("image")
            assert result is not None, "Required property 'image' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The command that's passed to the container.

            This parameter maps to ``Cmd`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``COMMAND`` parameter to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . For more information, see `https://docs.docker.com/engine/reference/builder/#cmd <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/builder/#cmd>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-command
            '''
            result = self._values.get("command")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EnvironmentProperty"]]]]:
            '''The environment variables to pass to a container.

            This parameter maps to ``Env`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--env`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               We don't recommend using plaintext environment variables for sensitive information, such as credential data. > Environment variables cannot start with " ``AWS_BATCH`` ". This naming convention is reserved for variables that AWS Batch sets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EnvironmentProperty"]]]], result)

        @builtins.property
        def ephemeral_storage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EphemeralStorageProperty"]]:
            '''The amount of ephemeral storage to allocate for the task.

            This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-ephemeralstorage
            '''
            result = self._values.get("ephemeral_storage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EphemeralStorageProperty"]], result)

        @builtins.property
        def execution_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume.

            For jobs that run on Fargate resources, you must provide an execution role. For more information, see `AWS Batch execution IAM role <https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html>`_ in the *AWS Batch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-executionrolearn
            '''
            result = self._values.get("execution_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fargate_platform_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.FargatePlatformConfigurationProperty"]]:
            '''The platform configuration for jobs that are running on Fargate resources.

            Jobs that are running on EC2 resources must not specify this parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-fargateplatformconfiguration
            '''
            result = self._values.get("fargate_platform_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.FargatePlatformConfigurationProperty"]], result)

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''The instance type to use for a multi-node parallel job.

            All node groups in a multi-node parallel job must use the same instance type.
            .. epigraph::

               This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def job_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.

            For more information, see `IAM roles for tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-jobrolearn
            '''
            result = self._values.get("job_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def linux_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.LinuxParametersProperty"]]:
            '''Linux-specific modifications that are applied to the container, such as details for device mappings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-linuxparameters
            '''
            result = self._values.get("linux_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.LinuxParametersProperty"]], result)

        @builtins.property
        def log_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.LogConfigurationProperty"]]:
            '''The log configuration specification for the container.

            This parameter maps to ``LogConfig`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--log-driver`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.aws.amazon.com/https://docs.docker.com/engine/admin/logging/overview/>`_ in the Docker documentation.
            .. epigraph::

               AWS Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the ``LogConfiguration`` data type).

            This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``
            .. epigraph::

               The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS container agent configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-logconfiguration
            '''
            result = self._values.get("log_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.LogConfigurationProperty"]], result)

        @builtins.property
        def memory(self) -> typing.Optional[jsii.Number]:
            '''This parameter is deprecated, use ``resourceRequirements`` to specify the memory requirements for the job definition.

            It's not supported for jobs running on Fargate resources. For jobs that run on EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, it's terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_points(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.MountPointsProperty"]]]]:
            '''The mount points for data volumes in your container.

            This parameter maps to ``Volumes`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--volume`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-mountpoints
            '''
            result = self._values.get("mount_points")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.MountPointsProperty"]]]], result)

        @builtins.property
        def network_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.NetworkConfigurationProperty"]]:
            '''The network configuration for jobs that are running on Fargate resources.

            Jobs that are running on EC2 resources must not specify this parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-networkconfiguration
            '''
            result = self._values.get("network_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.NetworkConfigurationProperty"]], result)

        @builtins.property
        def privileged(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When this parameter is true, the container is given elevated permissions on the host container instance (similar to the ``root`` user).

            This parameter maps to ``Privileged`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--privileged`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . The default value is false.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-privileged
            '''
            result = self._values.get("privileged")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def readonly_root_filesystem(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When this parameter is true, the container is given read-only access to its root file system.

            This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--read-only`` option to ``docker run`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-readonlyrootfilesystem
            '''
            result = self._values.get("readonly_root_filesystem")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def resource_requirements(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ResourceRequirementProperty"]]]]:
            '''The type and amount of resources to assign to a container.

            The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-resourcerequirements
            '''
            result = self._values.get("resource_requirements")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ResourceRequirementProperty"]]]], result)

        @builtins.property
        def runtime_platform(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.RuntimePlatformProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-runtimeplatform
            '''
            result = self._values.get("runtime_platform")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.RuntimePlatformProperty"]], result)

        @builtins.property
        def secrets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.SecretProperty"]]]]:
            '''The secrets for the container.

            For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-secrets
            '''
            result = self._values.get("secrets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.SecretProperty"]]]], result)

        @builtins.property
        def ulimits(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.UlimitProperty"]]]]:
            '''A list of ``ulimits`` to set in the container.

            This parameter maps to ``Ulimits`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--ulimit`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-ulimits
            '''
            result = self._values.get("ulimits")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.UlimitProperty"]]]], result)

        @builtins.property
        def user(self) -> typing.Optional[builtins.str]:
            '''The user name to use inside the container.

            This parameter maps to ``User`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--user`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-user
            '''
            result = self._values.get("user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vcpus(self) -> typing.Optional[jsii.Number]:
            '''This parameter is deprecated, use ``resourceRequirements`` to specify the vCPU requirements for the job definition.

            It's not supported for jobs running on Fargate resources. For jobs running on EC2 resources, it specifies the number of vCPUs reserved for the job.

            Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-vcpus
            '''
            result = self._values.get("vcpus")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volumes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.VolumesProperty"]]]]:
            '''A list of data volumes used in a job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-volumes
            '''
            result = self._values.get("volumes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.VolumesProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.DeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_path": "containerPath",
            "host_path": "hostPath",
            "permissions": "permissions",
        },
    )
    class DeviceProperty:
        def __init__(
            self,
            *,
            container_path: typing.Optional[builtins.str] = None,
            host_path: typing.Optional[builtins.str] = None,
            permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''An object that represents a container instance host device.

            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :param container_path: The path inside the container that's used to expose the host device. By default, the ``hostPath`` value is used.
            :param host_path: The path for the device on the host container instance.
            :param permissions: The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                device_property = batch.CfnJobDefinition.DeviceProperty(
                    container_path="containerPath",
                    host_path="hostPath",
                    permissions=["permissions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__adbf78805f7f3d50af2c331ead7e1f53e092ea7a76782151236bad4f3bfc77b0)
                check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
                check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
                check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_path is not None:
                self._values["container_path"] = container_path
            if host_path is not None:
                self._values["host_path"] = host_path
            if permissions is not None:
                self._values["permissions"] = permissions

        @builtins.property
        def container_path(self) -> typing.Optional[builtins.str]:
            '''The path inside the container that's used to expose the host device.

            By default, the ``hostPath`` value is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-containerpath
            '''
            result = self._values.get("container_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def host_path(self) -> typing.Optional[builtins.str]:
            '''The path for the device on the host container instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-hostpath
            '''
            result = self._values.get("host_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The explicit permissions to provide to the container for the device.

            By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-permissions
            '''
            result = self._values.get("permissions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EfsVolumeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "file_system_id": "fileSystemId",
            "authorization_config": "authorizationConfig",
            "root_directory": "rootDirectory",
            "transit_encryption": "transitEncryption",
            "transit_encryption_port": "transitEncryptionPort",
        },
    )
    class EfsVolumeConfigurationProperty:
        def __init__(
            self,
            *,
            file_system_id: builtins.str,
            authorization_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.AuthorizationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            root_directory: typing.Optional[builtins.str] = None,
            transit_encryption: typing.Optional[builtins.str] = None,
            transit_encryption_port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''This is used when you're using an Amazon Elastic File System file system for job storage.

            For more information, see `Amazon EFS Volumes <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html>`_ in the *AWS Batch User Guide* .

            :param file_system_id: The Amazon EFS file system ID to use.
            :param authorization_config: The authorization configuration details for the Amazon EFS file system.
            :param root_directory: The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying ``/`` has the same effect as omitting this parameter. The maximum length is 4,096 characters. .. epigraph:: If an EFS access point is specified in the ``authorizationConfig`` , the root directory parameter must either be omitted or set to ``/`` , which enforces the path set on the Amazon EFS access point.
            :param transit_encryption: Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of ``DISABLED`` is used. For more information, see `Encrypting data in transit <https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html>`_ in the *Amazon Elastic File System User Guide* .
            :param transit_encryption_port: The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you don't specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see `EFS mount helper <https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html>`_ in the *Amazon Elastic File System User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                efs_volume_configuration_property = batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                    file_system_id="fileSystemId",
                
                    # the properties below are optional
                    authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                        access_point_id="accessPointId",
                        iam="iam"
                    ),
                    root_directory="rootDirectory",
                    transit_encryption="transitEncryption",
                    transit_encryption_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f673b085b46133477cd372799511104e89e28bf34ac0f6255020b20ef8b7e3e0)
                check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
                check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
                check_type(argname="argument transit_encryption", value=transit_encryption, expected_type=type_hints["transit_encryption"])
                check_type(argname="argument transit_encryption_port", value=transit_encryption_port, expected_type=type_hints["transit_encryption_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "file_system_id": file_system_id,
            }
            if authorization_config is not None:
                self._values["authorization_config"] = authorization_config
            if root_directory is not None:
                self._values["root_directory"] = root_directory
            if transit_encryption is not None:
                self._values["transit_encryption"] = transit_encryption
            if transit_encryption_port is not None:
                self._values["transit_encryption_port"] = transit_encryption_port

        @builtins.property
        def file_system_id(self) -> builtins.str:
            '''The Amazon EFS file system ID to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-filesystemid
            '''
            result = self._values.get("file_system_id")
            assert result is not None, "Required property 'file_system_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.AuthorizationConfigProperty"]]:
            '''The authorization configuration details for the Amazon EFS file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.AuthorizationConfigProperty"]], result)

        @builtins.property
        def root_directory(self) -> typing.Optional[builtins.str]:
            '''The directory within the Amazon EFS file system to mount as the root directory inside the host.

            If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying ``/`` has the same effect as omitting this parameter. The maximum length is 4,096 characters.
            .. epigraph::

               If an EFS access point is specified in the ``authorizationConfig`` , the root directory parameter must either be omitted or set to ``/`` , which enforces the path set on the Amazon EFS access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-rootdirectory
            '''
            result = self._values.get("root_directory")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transit_encryption(self) -> typing.Optional[builtins.str]:
            '''Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server.

            Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of ``DISABLED`` is used. For more information, see `Encrypting data in transit <https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html>`_ in the *Amazon Elastic File System User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-transitencryption
            '''
            result = self._values.get("transit_encryption")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transit_encryption_port(self) -> typing.Optional[jsii.Number]:
            '''The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server.

            If you don't specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see `EFS mount helper <https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html>`_ in the *Amazon Elastic File System User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-transitencryptionport
            '''
            result = self._values.get("transit_encryption_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EfsVolumeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EksContainerEnvironmentVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EksContainerEnvironmentVariableProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An environment variable.

            :param name: The name of the environment variable.
            :param value: The value of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                eks_container_environment_variable_property = batch.CfnJobDefinition.EksContainerEnvironmentVariableProperty(
                    name="name",
                
                    # the properties below are optional
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__daaaeed078e13c29ac34da5a79bab4c04e8767edaf6d6a60877918a94797c218)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable.html#cfn-batch-jobdefinition-ekscontainerenvironmentvariable-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable.html#cfn-batch-jobdefinition-ekscontainerenvironmentvariable-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksContainerEnvironmentVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EksContainerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image": "image",
            "args": "args",
            "command": "command",
            "env": "env",
            "image_pull_policy": "imagePullPolicy",
            "name": "name",
            "resources": "resources",
            "security_context": "securityContext",
            "volume_mounts": "volumeMounts",
        },
    )
    class EksContainerProperty:
        def __init__(
            self,
            *,
            image: builtins.str,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
            command: typing.Optional[typing.Sequence[builtins.str]] = None,
            env: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EksContainerEnvironmentVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            image_pull_policy: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.ResourcesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            security_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.SecurityContextProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            volume_mounts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EksContainerVolumeMountProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''EKS container properties are used in job definitions for Amazon EKS based job definitions to describe the properties for a container node in the pod that's launched as part of a job.

            This can't be specified for Amazon ECS based job definitions.

            :param image: The Docker image used to start the container.
            :param args: An array of arguments to the entrypoint. If this isn't specified, the ``CMD`` of the container image is used. This corresponds to the ``args`` member in the `Entrypoint <https://docs.aws.amazon.com/https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint>`_ portion of the `Pod <https://docs.aws.amazon.com/https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/>`_ in Kubernetes. Environment variable references are expanded using the container's environment. If the referenced environment variable doesn't exist, the reference in the command isn't changed. For example, if the reference is to " ``$(NAME1)`` " and the ``NAME1`` environment variable doesn't exist, the command string will remain " ``$(NAME1)`` ." ``$$`` is replaced with ``$`` , and the resulting string isn't expanded. For example, ``$$(VAR_NAME)`` is passed as ``$(VAR_NAME)`` whether or not the ``VAR_NAME`` environment variable exists. For more information, see `CMD <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/builder/#cmd>`_ in the *Dockerfile reference* and `Define a command and arguments for a pod <https://docs.aws.amazon.com/https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/>`_ in the *Kubernetes documentation* .
            :param command: The entrypoint for the container. This isn't run within a shell. If this isn't specified, the ``ENTRYPOINT`` of the container image is used. Environment variable references are expanded using the container's environment. If the referenced environment variable doesn't exist, the reference in the command isn't changed. For example, if the reference is to " ``$(NAME1)`` " and the ``NAME1`` environment variable doesn't exist, the command string will remain " ``$(NAME1)`` ." ``$$`` is replaced with ``$`` and the resulting string isn't expanded. For example, ``$$(VAR_NAME)`` will be passed as ``$(VAR_NAME)`` whether or not the ``VAR_NAME`` environment variable exists. The entrypoint can't be updated. For more information, see `ENTRYPOINT <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/builder/#entrypoint>`_ in the *Dockerfile reference* and `Define a command and arguments for a container <https://docs.aws.amazon.com/https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/>`_ and `Entrypoint <https://docs.aws.amazon.com/https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint>`_ in the *Kubernetes documentation* .
            :param env: The environment variables to pass to a container. .. epigraph:: Environment variables cannot start with " ``AWS_BATCH`` ". This naming convention is reserved for variables that AWS Batch sets.
            :param image_pull_policy: The image pull policy for the container. Supported values are ``Always`` , ``IfNotPresent`` , and ``Never`` . This parameter defaults to ``IfNotPresent`` . However, if the ``:latest`` tag is specified, it defaults to ``Always`` . For more information, see `Updating images <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/containers/images/#updating-images>`_ in the *Kubernetes documentation* .
            :param name: The name of the container. If the name isn't specified, the default name " ``Default`` " is used. Each container in a pod must have a unique name.
            :param resources: The type and amount of resources to assign to a container. The supported resources include ``memory`` , ``cpu`` , and ``nvidia.com/gpu`` . For more information, see `Resource management for pods and containers <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>`_ in the *Kubernetes documentation* .
            :param security_context: 
            :param volume_mounts: The volume mounts for the container. AWS Batch supports ``emptyDir`` , ``hostPath`` , and ``secret`` volume types. For more information about volumes and volume mounts in Kubernetes, see `Volumes <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # limits: Any
                # requests: Any
                
                eks_container_property = batch.CfnJobDefinition.EksContainerProperty(
                    image="image",
                
                    # the properties below are optional
                    args=["args"],
                    command=["command"],
                    env=[batch.CfnJobDefinition.EksContainerEnvironmentVariableProperty(
                        name="name",
                
                        # the properties below are optional
                        value="value"
                    )],
                    image_pull_policy="imagePullPolicy",
                    name="name",
                    resources=batch.CfnJobDefinition.ResourcesProperty(
                        limits=limits,
                        requests=requests
                    ),
                    security_context=batch.CfnJobDefinition.SecurityContextProperty(
                        privileged=False,
                        read_only_root_filesystem=False,
                        run_as_group=123,
                        run_as_non_root=False,
                        run_as_user=123
                    ),
                    volume_mounts=[batch.CfnJobDefinition.EksContainerVolumeMountProperty(
                        mount_path="mountPath",
                        name="name",
                        read_only=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a9ece3a6d2417f8d913bdfc7bdf646d1de352c65903e333939133c3e81b1f4f3)
                check_type(argname="argument image", value=image, expected_type=type_hints["image"])
                check_type(argname="argument args", value=args, expected_type=type_hints["args"])
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument env", value=env, expected_type=type_hints["env"])
                check_type(argname="argument image_pull_policy", value=image_pull_policy, expected_type=type_hints["image_pull_policy"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
                check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
                check_type(argname="argument volume_mounts", value=volume_mounts, expected_type=type_hints["volume_mounts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "image": image,
            }
            if args is not None:
                self._values["args"] = args
            if command is not None:
                self._values["command"] = command
            if env is not None:
                self._values["env"] = env
            if image_pull_policy is not None:
                self._values["image_pull_policy"] = image_pull_policy
            if name is not None:
                self._values["name"] = name
            if resources is not None:
                self._values["resources"] = resources
            if security_context is not None:
                self._values["security_context"] = security_context
            if volume_mounts is not None:
                self._values["volume_mounts"] = volume_mounts

        @builtins.property
        def image(self) -> builtins.str:
            '''The Docker image used to start the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-image
            '''
            result = self._values.get("image")
            assert result is not None, "Required property 'image' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of arguments to the entrypoint.

            If this isn't specified, the ``CMD`` of the container image is used. This corresponds to the ``args`` member in the `Entrypoint <https://docs.aws.amazon.com/https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint>`_ portion of the `Pod <https://docs.aws.amazon.com/https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/>`_ in Kubernetes. Environment variable references are expanded using the container's environment.

            If the referenced environment variable doesn't exist, the reference in the command isn't changed. For example, if the reference is to " ``$(NAME1)`` " and the ``NAME1`` environment variable doesn't exist, the command string will remain " ``$(NAME1)`` ." ``$$`` is replaced with ``$`` , and the resulting string isn't expanded. For example, ``$$(VAR_NAME)`` is passed as ``$(VAR_NAME)`` whether or not the ``VAR_NAME`` environment variable exists. For more information, see `CMD <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/builder/#cmd>`_ in the *Dockerfile reference* and `Define a command and arguments for a pod <https://docs.aws.amazon.com/https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The entrypoint for the container.

            This isn't run within a shell. If this isn't specified, the ``ENTRYPOINT`` of the container image is used. Environment variable references are expanded using the container's environment.

            If the referenced environment variable doesn't exist, the reference in the command isn't changed. For example, if the reference is to " ``$(NAME1)`` " and the ``NAME1`` environment variable doesn't exist, the command string will remain " ``$(NAME1)`` ." ``$$`` is replaced with ``$`` and the resulting string isn't expanded. For example, ``$$(VAR_NAME)`` will be passed as ``$(VAR_NAME)`` whether or not the ``VAR_NAME`` environment variable exists. The entrypoint can't be updated. For more information, see `ENTRYPOINT <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/builder/#entrypoint>`_ in the *Dockerfile reference* and `Define a command and arguments for a container <https://docs.aws.amazon.com/https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/>`_ and `Entrypoint <https://docs.aws.amazon.com/https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-command
            '''
            result = self._values.get("command")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def env(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksContainerEnvironmentVariableProperty"]]]]:
            '''The environment variables to pass to a container.

            .. epigraph::

               Environment variables cannot start with " ``AWS_BATCH`` ". This naming convention is reserved for variables that AWS Batch sets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-env
            '''
            result = self._values.get("env")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksContainerEnvironmentVariableProperty"]]]], result)

        @builtins.property
        def image_pull_policy(self) -> typing.Optional[builtins.str]:
            '''The image pull policy for the container.

            Supported values are ``Always`` , ``IfNotPresent`` , and ``Never`` . This parameter defaults to ``IfNotPresent`` . However, if the ``:latest`` tag is specified, it defaults to ``Always`` . For more information, see `Updating images <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/containers/images/#updating-images>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-imagepullpolicy
            '''
            result = self._values.get("image_pull_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the container.

            If the name isn't specified, the default name " ``Default`` " is used. Each container in a pod must have a unique name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resources(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ResourcesProperty"]]:
            '''The type and amount of resources to assign to a container.

            The supported resources include ``memory`` , ``cpu`` , and ``nvidia.com/gpu`` . For more information, see `Resource management for pods and containers <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ResourcesProperty"]], result)

        @builtins.property
        def security_context(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.SecurityContextProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-securitycontext
            '''
            result = self._values.get("security_context")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.SecurityContextProperty"]], result)

        @builtins.property
        def volume_mounts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksContainerVolumeMountProperty"]]]]:
            '''The volume mounts for the container.

            AWS Batch supports ``emptyDir`` , ``hostPath`` , and ``secret`` volume types. For more information about volumes and volume mounts in Kubernetes, see `Volumes <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-volumemounts
            '''
            result = self._values.get("volume_mounts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksContainerVolumeMountProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksContainerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EksContainerVolumeMountProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mount_path": "mountPath",
            "name": "name",
            "read_only": "readOnly",
        },
    )
    class EksContainerVolumeMountProperty:
        def __init__(
            self,
            *,
            mount_path: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The volume mounts for a container for an Amazon EKS job.

            For more information about volumes and volume mounts in Kubernetes, see `Volumes <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/>`_ in the *Kubernetes documentation* .

            :param mount_path: The path on the container where the volume is mounted.
            :param name: The name the volume mount. This must match the name of one of the volumes in the pod.
            :param read_only: If this value is ``true`` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                eks_container_volume_mount_property = batch.CfnJobDefinition.EksContainerVolumeMountProperty(
                    mount_path="mountPath",
                    name="name",
                    read_only=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__855f1c6efd210a25d73922fc636cbbe8c4e08f7e49a5b9582f0ac1759eab5147)
                check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if mount_path is not None:
                self._values["mount_path"] = mount_path
            if name is not None:
                self._values["name"] = name
            if read_only is not None:
                self._values["read_only"] = read_only

        @builtins.property
        def mount_path(self) -> typing.Optional[builtins.str]:
            '''The path on the container where the volume is mounted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html#cfn-batch-jobdefinition-ekscontainervolumemount-mountpath
            '''
            result = self._values.get("mount_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name the volume mount.

            This must match the name of one of the volumes in the pod.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html#cfn-batch-jobdefinition-ekscontainervolumemount-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def read_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If this value is ``true`` , the container has read-only access to the volume.

            Otherwise, the container can write to the volume. The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html#cfn-batch-jobdefinition-ekscontainervolumemount-readonly
            '''
            result = self._values.get("read_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksContainerVolumeMountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EksPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"pod_properties": "podProperties"},
    )
    class EksPropertiesProperty:
        def __init__(
            self,
            *,
            pod_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.PodPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object that contains the properties for the Kubernetes resources of a job.

            :param pod_properties: The properties for the Kubernetes pod resources of a job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # labels: Any
                # limits: Any
                # requests: Any
                
                eks_properties_property = batch.CfnJobDefinition.EksPropertiesProperty(
                    pod_properties=batch.CfnJobDefinition.PodPropertiesProperty(
                        containers=[batch.CfnJobDefinition.EksContainerProperty(
                            image="image",
                
                            # the properties below are optional
                            args=["args"],
                            command=["command"],
                            env=[batch.CfnJobDefinition.EksContainerEnvironmentVariableProperty(
                                name="name",
                
                                # the properties below are optional
                                value="value"
                            )],
                            image_pull_policy="imagePullPolicy",
                            name="name",
                            resources=batch.CfnJobDefinition.ResourcesProperty(
                                limits=limits,
                                requests=requests
                            ),
                            security_context=batch.CfnJobDefinition.SecurityContextProperty(
                                privileged=False,
                                read_only_root_filesystem=False,
                                run_as_group=123,
                                run_as_non_root=False,
                                run_as_user=123
                            ),
                            volume_mounts=[batch.CfnJobDefinition.EksContainerVolumeMountProperty(
                                mount_path="mountPath",
                                name="name",
                                read_only=False
                            )]
                        )],
                        dns_policy="dnsPolicy",
                        host_network=False,
                        metadata=batch.CfnJobDefinition.MetadataProperty(
                            labels=labels
                        ),
                        service_account_name="serviceAccountName",
                        volumes=[batch.CfnJobDefinition.EksVolumeProperty(
                            name="name",
                
                            # the properties below are optional
                            empty_dir=batch.CfnJobDefinition.EmptyDirProperty(
                                medium="medium",
                                size_limit="sizeLimit"
                            ),
                            host_path=batch.CfnJobDefinition.HostPathProperty(
                                path="path"
                            ),
                            secret=batch.CfnJobDefinition.EksSecretProperty(
                                secret_name="secretName",
                
                                # the properties below are optional
                                optional=False
                            )
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab4acc4a05a00897faf964911a9c5d642ebccbae43237575ad3b0b27ecb3ee74)
                check_type(argname="argument pod_properties", value=pod_properties, expected_type=type_hints["pod_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pod_properties is not None:
                self._values["pod_properties"] = pod_properties

        @builtins.property
        def pod_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.PodPropertiesProperty"]]:
            '''The properties for the Kubernetes pod resources of a job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksproperties.html#cfn-batch-jobdefinition-eksproperties-podproperties
            '''
            result = self._values.get("pod_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.PodPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EksSecretProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_name": "secretName", "optional": "optional"},
    )
    class EksSecretProperty:
        def __init__(
            self,
            *,
            secret_name: builtins.str,
            optional: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies the configuration of a Kubernetes ``secret`` volume.

            For more information, see `secret <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/#secret>`_ in the *Kubernetes documentation* .

            :param secret_name: The name of the secret. The name must be allowed as a DNS subdomain name. For more information, see `DNS subdomain names <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names>`_ in the *Kubernetes documentation* .
            :param optional: Specifies whether the secret or the secret's keys must be defined.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekssecret.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                eks_secret_property = batch.CfnJobDefinition.EksSecretProperty(
                    secret_name="secretName",
                
                    # the properties below are optional
                    optional=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__285ba8b233801a3c8377d3b178bafde5c49a98f09f3e37c53c663ac43e11a41c)
                check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
                check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_name": secret_name,
            }
            if optional is not None:
                self._values["optional"] = optional

        @builtins.property
        def secret_name(self) -> builtins.str:
            '''The name of the secret.

            The name must be allowed as a DNS subdomain name. For more information, see `DNS subdomain names <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekssecret.html#cfn-batch-jobdefinition-ekssecret-secretname
            '''
            result = self._values.get("secret_name")
            assert result is not None, "Required property 'secret_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def optional(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the secret or the secret's keys must be defined.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekssecret.html#cfn-batch-jobdefinition-ekssecret-optional
            '''
            result = self._values.get("optional")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksSecretProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EksVolumeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "empty_dir": "emptyDir",
            "host_path": "hostPath",
            "secret": "secret",
        },
    )
    class EksVolumeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            empty_dir: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EmptyDirProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            host_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.HostPathProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            secret: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EksSecretProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies an Amazon EKS volume for a job definition.

            :param name: The name of the volume. The name must be allowed as a DNS subdomain name. For more information, see `DNS subdomain names <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names>`_ in the *Kubernetes documentation* .
            :param empty_dir: Specifies the configuration of a Kubernetes ``emptyDir`` volume. For more information, see `emptyDir <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/#emptydir>`_ in the *Kubernetes documentation* .
            :param host_path: Specifies the configuration of a Kubernetes ``hostPath`` volume. For more information, see `hostPath <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/#hostpath>`_ in the *Kubernetes documentation* .
            :param secret: Specifies the configuration of a Kubernetes ``secret`` volume. For more information, see `secret <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/#secret>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                eks_volume_property = batch.CfnJobDefinition.EksVolumeProperty(
                    name="name",
                
                    # the properties below are optional
                    empty_dir=batch.CfnJobDefinition.EmptyDirProperty(
                        medium="medium",
                        size_limit="sizeLimit"
                    ),
                    host_path=batch.CfnJobDefinition.HostPathProperty(
                        path="path"
                    ),
                    secret=batch.CfnJobDefinition.EksSecretProperty(
                        secret_name="secretName",
                
                        # the properties below are optional
                        optional=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71bf085e500a34c552f178e2df09efdf138a2c99fb19667f0b4cf9e398ca47eb)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument empty_dir", value=empty_dir, expected_type=type_hints["empty_dir"])
                check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
                check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if empty_dir is not None:
                self._values["empty_dir"] = empty_dir
            if host_path is not None:
                self._values["host_path"] = host_path
            if secret is not None:
                self._values["secret"] = secret

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the volume.

            The name must be allowed as a DNS subdomain name. For more information, see `DNS subdomain names <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html#cfn-batch-jobdefinition-eksvolume-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def empty_dir(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EmptyDirProperty"]]:
            '''Specifies the configuration of a Kubernetes ``emptyDir`` volume.

            For more information, see `emptyDir <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/#emptydir>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html#cfn-batch-jobdefinition-eksvolume-emptydir
            '''
            result = self._values.get("empty_dir")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EmptyDirProperty"]], result)

        @builtins.property
        def host_path(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.HostPathProperty"]]:
            '''Specifies the configuration of a Kubernetes ``hostPath`` volume.

            For more information, see `hostPath <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/#hostpath>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html#cfn-batch-jobdefinition-eksvolume-hostpath
            '''
            result = self._values.get("host_path")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.HostPathProperty"]], result)

        @builtins.property
        def secret(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksSecretProperty"]]:
            '''Specifies the configuration of a Kubernetes ``secret`` volume.

            For more information, see `secret <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/storage/volumes/#secret>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html#cfn-batch-jobdefinition-eksvolume-secret
            '''
            result = self._values.get("secret")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksSecretProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksVolumeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EmptyDirProperty",
        jsii_struct_bases=[],
        name_mapping={"medium": "medium", "size_limit": "sizeLimit"},
    )
    class EmptyDirProperty:
        def __init__(
            self,
            *,
            medium: typing.Optional[builtins.str] = None,
            size_limit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param medium: 
            :param size_limit: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-emptydir.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                empty_dir_property = batch.CfnJobDefinition.EmptyDirProperty(
                    medium="medium",
                    size_limit="sizeLimit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bdef2f5e1ccd021a3913efc6e9f67cc3f3972961e97a491b8a739c8033fa20a3)
                check_type(argname="argument medium", value=medium, expected_type=type_hints["medium"])
                check_type(argname="argument size_limit", value=size_limit, expected_type=type_hints["size_limit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if medium is not None:
                self._values["medium"] = medium
            if size_limit is not None:
                self._values["size_limit"] = size_limit

        @builtins.property
        def medium(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-emptydir.html#cfn-batch-jobdefinition-emptydir-medium
            '''
            result = self._values.get("medium")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def size_limit(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-emptydir.html#cfn-batch-jobdefinition-emptydir-sizelimit
            '''
            result = self._values.get("size_limit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmptyDirProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Environment property type specifies environment variables to use in a job definition.

            :param name: The name of the environment variable.
            :param value: The value of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                environment_property = batch.CfnJobDefinition.EnvironmentProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1410eef4fad9b82401792bfb3c1c9342d946ef2f57199de602a1d63db8df8b41)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html#cfn-batch-jobdefinition-environment-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html#cfn-batch-jobdefinition-environment-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EphemeralStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"size_in_gib": "sizeInGiB"},
    )
    class EphemeralStorageProperty:
        def __init__(self, *, size_in_gib: jsii.Number) -> None:
            '''The amount of ephemeral storage to allocate for the task.

            This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate .

            :param size_in_gib: The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is ``21`` GiB and the maximum supported value is ``200`` GiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ephemeralstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                ephemeral_storage_property = batch.CfnJobDefinition.EphemeralStorageProperty(
                    size_in_gi_b=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c8e501c23ca082963ca4e3f697be654dd2053f8a6f062fcd801a10d61dd916cf)
                check_type(argname="argument size_in_gib", value=size_in_gib, expected_type=type_hints["size_in_gib"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "size_in_gib": size_in_gib,
            }

        @builtins.property
        def size_in_gib(self) -> jsii.Number:
            '''The total amount, in GiB, of ephemeral storage to set for the task.

            The minimum supported value is ``21`` GiB and the maximum supported value is ``200`` GiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ephemeralstorage.html#cfn-batch-jobdefinition-ephemeralstorage-sizeingib
            '''
            result = self._values.get("size_in_gib")
            assert result is not None, "Required property 'size_in_gib' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EphemeralStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.EvaluateOnExitProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "on_exit_code": "onExitCode",
            "on_reason": "onReason",
            "on_status_reason": "onStatusReason",
        },
    )
    class EvaluateOnExitProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            on_exit_code: typing.Optional[builtins.str] = None,
            on_reason: typing.Optional[builtins.str] = None,
            on_status_reason: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies an array of up to 5 conditions to be met, and an action to take ( ``RETRY`` or ``EXIT`` ) if all conditions are met.

            If none of the ``EvaluateOnExit`` conditions in a ``RetryStrategy`` match, then the job is retried.

            :param action: Specifies the action to take if all of the specified conditions ( ``onStatusReason`` , ``onReason`` , and ``onExitCode`` ) are met. The values aren't case sensitive.
            :param on_exit_code: Contains a glob pattern to match against the decimal representation of the ``ExitCode`` returned for a job. The pattern can be up to 512 characters long. It can contain only numbers, and can end with an asterisk (*) so that only the start of the string needs to be an exact match. The string can contain up to 512 characters.
            :param on_reason: Contains a glob pattern to match against the ``Reason`` returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces and tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.
            :param on_status_reason: Contains a glob pattern to match against the ``StatusReason`` returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white spaces (including spaces or tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                evaluate_on_exit_property = batch.CfnJobDefinition.EvaluateOnExitProperty(
                    action="action",
                
                    # the properties below are optional
                    on_exit_code="onExitCode",
                    on_reason="onReason",
                    on_status_reason="onStatusReason"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__662f88de3d4a2c44e67c0a3c3ee43319e3b3ee88c557f7669e584f52665e667e)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument on_exit_code", value=on_exit_code, expected_type=type_hints["on_exit_code"])
                check_type(argname="argument on_reason", value=on_reason, expected_type=type_hints["on_reason"])
                check_type(argname="argument on_status_reason", value=on_status_reason, expected_type=type_hints["on_status_reason"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
            }
            if on_exit_code is not None:
                self._values["on_exit_code"] = on_exit_code
            if on_reason is not None:
                self._values["on_reason"] = on_reason
            if on_status_reason is not None:
                self._values["on_status_reason"] = on_status_reason

        @builtins.property
        def action(self) -> builtins.str:
            '''Specifies the action to take if all of the specified conditions ( ``onStatusReason`` , ``onReason`` , and ``onExitCode`` ) are met.

            The values aren't case sensitive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def on_exit_code(self) -> typing.Optional[builtins.str]:
            '''Contains a glob pattern to match against the decimal representation of the ``ExitCode`` returned for a job.

            The pattern can be up to 512 characters long. It can contain only numbers, and can end with an asterisk (*) so that only the start of the string needs to be an exact match.

            The string can contain up to 512 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onexitcode
            '''
            result = self._values.get("on_exit_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def on_reason(self) -> typing.Optional[builtins.str]:
            '''Contains a glob pattern to match against the ``Reason`` returned for a job.

            The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces and tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onreason
            '''
            result = self._values.get("on_reason")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def on_status_reason(self) -> typing.Optional[builtins.str]:
            '''Contains a glob pattern to match against the ``StatusReason`` returned for a job.

            The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white spaces (including spaces or tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onstatusreason
            '''
            result = self._values.get("on_status_reason")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluateOnExitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.FargatePlatformConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"platform_version": "platformVersion"},
    )
    class FargatePlatformConfigurationProperty:
        def __init__(
            self,
            *,
            platform_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The platform configuration for jobs that are running on Fargate resources.

            Jobs that run on EC2 resources must not specify this parameter.

            :param platform_version: The AWS Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the ``LATEST`` platform version is used by default. This uses a recent, approved version of the AWS Fargate platform for compute resources. For more information, see `AWS Fargate platform versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-fargateplatformconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                fargate_platform_configuration_property = batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                    platform_version="platformVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b088f865053d4cfdc2700de70d732a768d630a892a20da6fda19303df04e9b4)
                check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if platform_version is not None:
                self._values["platform_version"] = platform_version

        @builtins.property
        def platform_version(self) -> typing.Optional[builtins.str]:
            '''The AWS Fargate platform version where the jobs are running.

            A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the ``LATEST`` platform version is used by default. This uses a recent, approved version of the AWS Fargate platform for compute resources. For more information, see `AWS Fargate platform versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-fargateplatformconfiguration.html#cfn-batch-jobdefinition-fargateplatformconfiguration-platformversion
            '''
            result = self._values.get("platform_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FargatePlatformConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.HostPathProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path"},
    )
    class HostPathProperty:
        def __init__(self, *, path: typing.Optional[builtins.str] = None) -> None:
            '''
            :param path: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-hostpath.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                host_path_property = batch.CfnJobDefinition.HostPathProperty(
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2bf55e035d36507c507c0ff620eda0a3096496a2cd5226656fc5e4af46e1b9ac)
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-hostpath.html#cfn-batch-jobdefinition-hostpath-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HostPathProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.LinuxParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "devices": "devices",
            "init_process_enabled": "initProcessEnabled",
            "max_swap": "maxSwap",
            "shared_memory_size": "sharedMemorySize",
            "swappiness": "swappiness",
            "tmpfs": "tmpfs",
        },
    )
    class LinuxParametersProperty:
        def __init__(
            self,
            *,
            devices: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.DeviceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            init_process_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_swap: typing.Optional[jsii.Number] = None,
            shared_memory_size: typing.Optional[jsii.Number] = None,
            swappiness: typing.Optional[jsii.Number] = None,
            tmpfs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.TmpfsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Linux-specific modifications that are applied to the container, such as details for device mappings.

            :param devices: Any of the host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--device`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.
            :param init_process_enabled: If true, run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``
            :param max_swap: The total amount of swap memory (in MiB) a container can use. This parameter is translated to the ``--memory-swap`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ where the value is the sum of the container memory plus the ``maxSwap`` value. For more information, see ```--memory-swap`` details <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details>`_ in the Docker documentation. If a ``maxSwap`` value of ``0`` is specified, the container doesn't use swap. Accepted values are ``0`` or any positive integer. If the ``maxSwap`` parameter is omitted, the container doesn't use the swap configuration for the container instance that it's running on. A ``maxSwap`` value must be set for the ``swappiness`` parameter to be used. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.
            :param shared_memory_size: The value for the size (in MiB) of the ``/dev/shm`` volume. This parameter maps to the ``--shm-size`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.
            :param swappiness: You can use this parameter to tune a container's memory swappiness behavior. A ``swappiness`` value of ``0`` causes swapping to not occur unless absolutely necessary. A ``swappiness`` value of ``100`` causes pages to be swapped aggressively. Valid values are whole numbers between ``0`` and ``100`` . If the ``swappiness`` parameter isn't specified, a default value of ``60`` is used. If a value isn't specified for ``maxSwap`` , then this parameter is ignored. If ``maxSwap`` is set to 0, the container doesn't use swap. This parameter maps to the ``--memory-swappiness`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . Consider the following when you use a per-container swap configuration. - Swap space must be enabled and allocated on the container instance for the containers to use. .. epigraph:: By default, the Amazon ECS optimized AMIs don't have swap enabled. You must enable swap on the instance to use this feature. For more information, see `Instance store swap volumes <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html>`_ in the *Amazon EC2 User Guide for Linux Instances* or `How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file? <https://docs.aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/>`_ - The swap space parameters are only supported for job definitions using EC2 resources. - If the ``maxSwap`` and ``swappiness`` parameters are omitted from a job definition, each container has a default ``swappiness`` value of 60. Moreover, the total swap usage is limited to two times the memory reservation of the container. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.
            :param tmpfs: The container path, mount options, and size (in MiB) of the ``tmpfs`` mount. This parameter maps to the ``--tmpfs`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide this parameter for this resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-linuxparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                linux_parameters_property = batch.CfnJobDefinition.LinuxParametersProperty(
                    devices=[batch.CfnJobDefinition.DeviceProperty(
                        container_path="containerPath",
                        host_path="hostPath",
                        permissions=["permissions"]
                    )],
                    init_process_enabled=False,
                    max_swap=123,
                    shared_memory_size=123,
                    swappiness=123,
                    tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                        container_path="containerPath",
                        size=123,
                
                        # the properties below are optional
                        mount_options=["mountOptions"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46c01503a14b135de04e03e8a183177fbaa4f728ed5853b4de848d62c1f248ae)
                check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
                check_type(argname="argument init_process_enabled", value=init_process_enabled, expected_type=type_hints["init_process_enabled"])
                check_type(argname="argument max_swap", value=max_swap, expected_type=type_hints["max_swap"])
                check_type(argname="argument shared_memory_size", value=shared_memory_size, expected_type=type_hints["shared_memory_size"])
                check_type(argname="argument swappiness", value=swappiness, expected_type=type_hints["swappiness"])
                check_type(argname="argument tmpfs", value=tmpfs, expected_type=type_hints["tmpfs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if devices is not None:
                self._values["devices"] = devices
            if init_process_enabled is not None:
                self._values["init_process_enabled"] = init_process_enabled
            if max_swap is not None:
                self._values["max_swap"] = max_swap
            if shared_memory_size is not None:
                self._values["shared_memory_size"] = shared_memory_size
            if swappiness is not None:
                self._values["swappiness"] = swappiness
            if tmpfs is not None:
                self._values["tmpfs"] = tmpfs

        @builtins.property
        def devices(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.DeviceProperty"]]]]:
            '''Any of the host devices to expose to the container.

            This parameter maps to ``Devices`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--device`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-linuxparameters.html#cfn-batch-jobdefinition-linuxparameters-devices
            '''
            result = self._values.get("devices")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.DeviceProperty"]]]], result)

        @builtins.property
        def init_process_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, run an ``init`` process inside the container that forwards signals and reaps processes.

            This parameter maps to the ``--init`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-linuxparameters.html#cfn-batch-jobdefinition-linuxparameters-initprocessenabled
            '''
            result = self._values.get("init_process_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_swap(self) -> typing.Optional[jsii.Number]:
            '''The total amount of swap memory (in MiB) a container can use.

            This parameter is translated to the ``--memory-swap`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ where the value is the sum of the container memory plus the ``maxSwap`` value. For more information, see ```--memory-swap`` details <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details>`_ in the Docker documentation.

            If a ``maxSwap`` value of ``0`` is specified, the container doesn't use swap. Accepted values are ``0`` or any positive integer. If the ``maxSwap`` parameter is omitted, the container doesn't use the swap configuration for the container instance that it's running on. A ``maxSwap`` value must be set for the ``swappiness`` parameter to be used.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-linuxparameters.html#cfn-batch-jobdefinition-linuxparameters-maxswap
            '''
            result = self._values.get("max_swap")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shared_memory_size(self) -> typing.Optional[jsii.Number]:
            '''The value for the size (in MiB) of the ``/dev/shm`` volume.

            This parameter maps to the ``--shm-size`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-linuxparameters.html#cfn-batch-jobdefinition-linuxparameters-sharedmemorysize
            '''
            result = self._values.get("shared_memory_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def swappiness(self) -> typing.Optional[jsii.Number]:
            '''You can use this parameter to tune a container's memory swappiness behavior.

            A ``swappiness`` value of ``0`` causes swapping to not occur unless absolutely necessary. A ``swappiness`` value of ``100`` causes pages to be swapped aggressively. Valid values are whole numbers between ``0`` and ``100`` . If the ``swappiness`` parameter isn't specified, a default value of ``60`` is used. If a value isn't specified for ``maxSwap`` , then this parameter is ignored. If ``maxSwap`` is set to 0, the container doesn't use swap. This parameter maps to the ``--memory-swappiness`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            Consider the following when you use a per-container swap configuration.

            - Swap space must be enabled and allocated on the container instance for the containers to use.

            .. epigraph::

               By default, the Amazon ECS optimized AMIs don't have swap enabled. You must enable swap on the instance to use this feature. For more information, see `Instance store swap volumes <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html>`_ in the *Amazon EC2 User Guide for Linux Instances* or `How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file? <https://docs.aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/>`_

            - The swap space parameters are only supported for job definitions using EC2 resources.
            - If the ``maxSwap`` and ``swappiness`` parameters are omitted from a job definition, each container has a default ``swappiness`` value of 60. Moreover, the total swap usage is limited to two times the memory reservation of the container.

            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-linuxparameters.html#cfn-batch-jobdefinition-linuxparameters-swappiness
            '''
            result = self._values.get("swappiness")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def tmpfs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.TmpfsProperty"]]]]:
            '''The container path, mount options, and size (in MiB) of the ``tmpfs`` mount.

            This parameter maps to the ``--tmpfs`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide this parameter for this resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-linuxparameters.html#cfn-batch-jobdefinition-linuxparameters-tmpfs
            '''
            result = self._values.get("tmpfs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.TmpfsProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinuxParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_driver": "logDriver",
            "options": "options",
            "secret_options": "secretOptions",
        },
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            log_driver: builtins.str,
            options: typing.Any = None,
            secret_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.SecretProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Log configuration options to send to a custom log driver for the container.

            :param log_driver: The log driver to use for the container. The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default. The supported log drivers are ``awslogs`` , ``fluentd`` , ``gelf`` , ``json-file`` , ``journald`` , ``logentries`` , ``syslog`` , and ``splunk`` . .. epigraph:: Jobs that are running on Fargate resources are restricted to the ``awslogs`` and ``splunk`` log drivers. - **awslogs** - Specifies the Amazon CloudWatch Logs logging driver. For more information, see `Using the awslogs log driver <https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html>`_ in the *AWS Batch User Guide* and `Amazon CloudWatch Logs logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/awslogs/>`_ in the Docker documentation. - **fluentd** - Specifies the Fluentd logging driver. For more information including usage and options, see `Fluentd logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/fluentd/>`_ in the *Docker documentation* . - **gelf** - Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see `Graylog Extended Format logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/gelf/>`_ in the *Docker documentation* . - **journald** - Specifies the journald logging driver. For more information including usage and options, see `Journald logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/journald/>`_ in the *Docker documentation* . - **json-file** - Specifies the JSON file logging driver. For more information including usage and options, see `JSON File logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/json-file/>`_ in the *Docker documentation* . - **splunk** - Specifies the Splunk logging driver. For more information including usage and options, see `Splunk logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/splunk/>`_ in the *Docker documentation* . - **syslog** - Specifies the syslog logging driver. For more information including usage and options, see `Syslog logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/syslog/>`_ in the *Docker documentation* . .. epigraph:: If you have a custom driver that's not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that's `available on GitHub <https://docs.aws.amazon.com/https://github.com/aws/amazon-ecs-agent>`_ and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesn't currently support running modified copies of this software. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``
            :param options: The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``
            :param secret_options: The secrets to pass to the log configuration. For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-logconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # options: Any
                
                log_configuration_property = batch.CfnJobDefinition.LogConfigurationProperty(
                    log_driver="logDriver",
                
                    # the properties below are optional
                    options=options,
                    secret_options=[batch.CfnJobDefinition.SecretProperty(
                        name="name",
                        value_from="valueFrom"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76e3055acf404e0b579b27c323b043bfb9f33e586341d48d4c5a17760f100e72)
                check_type(argname="argument log_driver", value=log_driver, expected_type=type_hints["log_driver"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
                check_type(argname="argument secret_options", value=secret_options, expected_type=type_hints["secret_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_driver": log_driver,
            }
            if options is not None:
                self._values["options"] = options
            if secret_options is not None:
                self._values["secret_options"] = secret_options

        @builtins.property
        def log_driver(self) -> builtins.str:
            '''The log driver to use for the container.

            The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.

            The supported log drivers are ``awslogs`` , ``fluentd`` , ``gelf`` , ``json-file`` , ``journald`` , ``logentries`` , ``syslog`` , and ``splunk`` .
            .. epigraph::

               Jobs that are running on Fargate resources are restricted to the ``awslogs`` and ``splunk`` log drivers.

            - **awslogs** - Specifies the Amazon CloudWatch Logs logging driver. For more information, see `Using the awslogs log driver <https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html>`_ in the *AWS Batch User Guide* and `Amazon CloudWatch Logs logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/awslogs/>`_ in the Docker documentation.
            - **fluentd** - Specifies the Fluentd logging driver. For more information including usage and options, see `Fluentd logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/fluentd/>`_ in the *Docker documentation* .
            - **gelf** - Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see `Graylog Extended Format logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/gelf/>`_ in the *Docker documentation* .
            - **journald** - Specifies the journald logging driver. For more information including usage and options, see `Journald logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/journald/>`_ in the *Docker documentation* .
            - **json-file** - Specifies the JSON file logging driver. For more information including usage and options, see `JSON File logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/json-file/>`_ in the *Docker documentation* .
            - **splunk** - Specifies the Splunk logging driver. For more information including usage and options, see `Splunk logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/splunk/>`_ in the *Docker documentation* .
            - **syslog** - Specifies the syslog logging driver. For more information including usage and options, see `Syslog logging driver <https://docs.aws.amazon.com/https://docs.docker.com/config/containers/logging/syslog/>`_ in the *Docker documentation* .

            .. epigraph::

               If you have a custom driver that's not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that's `available on GitHub <https://docs.aws.amazon.com/https://github.com/aws/amazon-ecs-agent>`_ and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesn't currently support running modified copies of this software.

            This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-logconfiguration.html#cfn-batch-jobdefinition-logconfiguration-logdriver
            '''
            result = self._values.get("log_driver")
            assert result is not None, "Required property 'log_driver' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def options(self) -> typing.Any:
            '''The configuration options to send to the log driver.

            This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version | grep "Server API version"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-logconfiguration.html#cfn-batch-jobdefinition-logconfiguration-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Any, result)

        @builtins.property
        def secret_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.SecretProperty"]]]]:
            '''The secrets to pass to the log configuration.

            For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-logconfiguration.html#cfn-batch-jobdefinition-logconfiguration-secretoptions
            '''
            result = self._values.get("secret_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.SecretProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.MetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"labels": "labels"},
    )
    class MetadataProperty:
        def __init__(self, *, labels: typing.Any = None) -> None:
            '''
            :param labels: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-metadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # labels: Any
                
                metadata_property = batch.CfnJobDefinition.MetadataProperty(
                    labels=labels
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a991ab55d6c85b732418b9a39402702cdf7043f946aaf69c13b36a4ccdd84cc)
                check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if labels is not None:
                self._values["labels"] = labels

        @builtins.property
        def labels(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-metadata.html#cfn-batch-jobdefinition-metadata-labels
            '''
            result = self._values.get("labels")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.MountPointsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_path": "containerPath",
            "read_only": "readOnly",
            "source_volume": "sourceVolume",
        },
    )
    class MountPointsProperty:
        def __init__(
            self,
            *,
            container_path: typing.Optional[builtins.str] = None,
            read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            source_volume: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details for a Docker volume mount point that's used in a job's container properties.

            This parameter maps to ``Volumes`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`_ section of the *Docker Remote API* and the ``--volume`` option to docker run.

            :param container_path: The path on the container where the host volume is mounted.
            :param read_only: If this value is ``true`` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is ``false`` .
            :param source_volume: The name of the volume to mount.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                mount_points_property = batch.CfnJobDefinition.MountPointsProperty(
                    container_path="containerPath",
                    read_only=False,
                    source_volume="sourceVolume"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47aa253c2fbb1ab8f90425d412e691e807d1454f21b10bb59eee6c2b63cf29b5)
                check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
                check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
                check_type(argname="argument source_volume", value=source_volume, expected_type=type_hints["source_volume"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_path is not None:
                self._values["container_path"] = container_path
            if read_only is not None:
                self._values["read_only"] = read_only
            if source_volume is not None:
                self._values["source_volume"] = source_volume

        @builtins.property
        def container_path(self) -> typing.Optional[builtins.str]:
            '''The path on the container where the host volume is mounted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-containerpath
            '''
            result = self._values.get("container_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def read_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If this value is ``true`` , the container has read-only access to the volume.

            Otherwise, the container can write to the volume. The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-readonly
            '''
            result = self._values.get("read_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def source_volume(self) -> typing.Optional[builtins.str]:
            '''The name of the volume to mount.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-sourcevolume
            '''
            result = self._values.get("source_volume")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MountPointsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"assign_public_ip": "assignPublicIp"},
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            assign_public_ip: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The network configuration for jobs that are running on Fargate resources.

            Jobs that are running on EC2 resources must not specify this parameter.

            :param assign_public_ip: Indicates whether the job has a public IP address. For a job that's running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see `Amazon ECS task networking <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`_ in the *Amazon Elastic Container Service Developer Guide* . The default value is " ``DISABLED`` ".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                network_configuration_property = batch.CfnJobDefinition.NetworkConfigurationProperty(
                    assign_public_ip="assignPublicIp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__681e5c00b804be1ae6d3076ea32a17483eee30db6c96e73768c520d652064300)
                check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if assign_public_ip is not None:
                self._values["assign_public_ip"] = assign_public_ip

        @builtins.property
        def assign_public_ip(self) -> typing.Optional[builtins.str]:
            '''Indicates whether the job has a public IP address.

            For a job that's running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see `Amazon ECS task networking <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`_ in the *Amazon Elastic Container Service Developer Guide* . The default value is " ``DISABLED`` ".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-networkconfiguration.html#cfn-batch-jobdefinition-networkconfiguration-assignpublicip
            '''
            result = self._values.get("assign_public_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.NodePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "main_node": "mainNode",
            "node_range_properties": "nodeRangeProperties",
            "num_nodes": "numNodes",
        },
    )
    class NodePropertiesProperty:
        def __init__(
            self,
            *,
            main_node: jsii.Number,
            node_range_properties: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.NodeRangePropertyProperty", typing.Dict[builtins.str, typing.Any]]]]],
            num_nodes: jsii.Number,
        ) -> None:
            '''An object that represents the node properties of a multi-node parallel job.

            .. epigraph::

               Node properties can't be specified for Amazon EKS based job definitions.

            :param main_node: Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.
            :param node_range_properties: A list of node ranges and their properties that are associated with a multi-node parallel job.
            :param num_nodes: The number of nodes that are associated with a multi-node parallel job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # options: Any
                
                node_properties_property = batch.CfnJobDefinition.NodePropertiesProperty(
                    main_node=123,
                    node_range_properties=[batch.CfnJobDefinition.NodeRangePropertyProperty(
                        target_nodes="targetNodes",
                
                        # the properties below are optional
                        container=batch.CfnJobDefinition.ContainerPropertiesProperty(
                            image="image",
                
                            # the properties below are optional
                            command=["command"],
                            environment=[batch.CfnJobDefinition.EnvironmentProperty(
                                name="name",
                                value="value"
                            )],
                            ephemeral_storage=batch.CfnJobDefinition.EphemeralStorageProperty(
                                size_in_gi_b=123
                            ),
                            execution_role_arn="executionRoleArn",
                            fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                                platform_version="platformVersion"
                            ),
                            instance_type="instanceType",
                            job_role_arn="jobRoleArn",
                            linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                                devices=[batch.CfnJobDefinition.DeviceProperty(
                                    container_path="containerPath",
                                    host_path="hostPath",
                                    permissions=["permissions"]
                                )],
                                init_process_enabled=False,
                                max_swap=123,
                                shared_memory_size=123,
                                swappiness=123,
                                tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                                    container_path="containerPath",
                                    size=123,
                
                                    # the properties below are optional
                                    mount_options=["mountOptions"]
                                )]
                            ),
                            log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                                log_driver="logDriver",
                
                                # the properties below are optional
                                options=options,
                                secret_options=[batch.CfnJobDefinition.SecretProperty(
                                    name="name",
                                    value_from="valueFrom"
                                )]
                            ),
                            memory=123,
                            mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                                container_path="containerPath",
                                read_only=False,
                                source_volume="sourceVolume"
                            )],
                            network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                                assign_public_ip="assignPublicIp"
                            ),
                            privileged=False,
                            readonly_root_filesystem=False,
                            resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                                type="type",
                                value="value"
                            )],
                            runtime_platform=batch.CfnJobDefinition.RuntimePlatformProperty(
                                cpu_architecture="cpuArchitecture",
                                operating_system_family="operatingSystemFamily"
                            ),
                            secrets=[batch.CfnJobDefinition.SecretProperty(
                                name="name",
                                value_from="valueFrom"
                            )],
                            ulimits=[batch.CfnJobDefinition.UlimitProperty(
                                hard_limit=123,
                                name="name",
                                soft_limit=123
                            )],
                            user="user",
                            vcpus=123,
                            volumes=[batch.CfnJobDefinition.VolumesProperty(
                                efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                                    file_system_id="fileSystemId",
                
                                    # the properties below are optional
                                    authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                        access_point_id="accessPointId",
                                        iam="iam"
                                    ),
                                    root_directory="rootDirectory",
                                    transit_encryption="transitEncryption",
                                    transit_encryption_port=123
                                ),
                                host=batch.CfnJobDefinition.VolumesHostProperty(
                                    source_path="sourcePath"
                                ),
                                name="name"
                            )]
                        )
                    )],
                    num_nodes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b765fef4e53f81f8c1a37eea0ea015533bd4621e0f00e5e86923931469f2fbd1)
                check_type(argname="argument main_node", value=main_node, expected_type=type_hints["main_node"])
                check_type(argname="argument node_range_properties", value=node_range_properties, expected_type=type_hints["node_range_properties"])
                check_type(argname="argument num_nodes", value=num_nodes, expected_type=type_hints["num_nodes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "main_node": main_node,
                "node_range_properties": node_range_properties,
                "num_nodes": num_nodes,
            }

        @builtins.property
        def main_node(self) -> jsii.Number:
            '''Specifies the node index for the main node of a multi-node parallel job.

            This node index value must be fewer than the number of nodes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-mainnode
            '''
            result = self._values.get("main_node")
            assert result is not None, "Required property 'main_node' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def node_range_properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.NodeRangePropertyProperty"]]]:
            '''A list of node ranges and their properties that are associated with a multi-node parallel job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-noderangeproperties
            '''
            result = self._values.get("node_range_properties")
            assert result is not None, "Required property 'node_range_properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.NodeRangePropertyProperty"]]], result)

        @builtins.property
        def num_nodes(self) -> jsii.Number:
            '''The number of nodes that are associated with a multi-node parallel job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-numnodes
            '''
            result = self._values.get("num_nodes")
            assert result is not None, "Required property 'num_nodes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.NodeRangePropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"target_nodes": "targetNodes", "container": "container"},
    )
    class NodeRangePropertyProperty:
        def __init__(
            self,
            *,
            target_nodes: builtins.str,
            container: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.ContainerPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object that represents the properties of the node range for a multi-node parallel job.

            :param target_nodes: The range of nodes, using node index values. A range of ``0:3`` indicates nodes with index values of ``0`` through ``3`` . If the starting range value is omitted ( ``:n`` ), then ``0`` is used to start the range. If the ending range value is omitted ( ``n:`` ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes ( ``0:n`` ). You can nest node ranges (for example, ``0:10`` and ``4:5`` ). In this case, the ``4:5`` range properties override the ``0:10`` properties.
            :param container: The container details for the node range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # options: Any
                
                node_range_property_property = batch.CfnJobDefinition.NodeRangePropertyProperty(
                    target_nodes="targetNodes",
                
                    # the properties below are optional
                    container=batch.CfnJobDefinition.ContainerPropertiesProperty(
                        image="image",
                
                        # the properties below are optional
                        command=["command"],
                        environment=[batch.CfnJobDefinition.EnvironmentProperty(
                            name="name",
                            value="value"
                        )],
                        ephemeral_storage=batch.CfnJobDefinition.EphemeralStorageProperty(
                            size_in_gi_b=123
                        ),
                        execution_role_arn="executionRoleArn",
                        fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                            platform_version="platformVersion"
                        ),
                        instance_type="instanceType",
                        job_role_arn="jobRoleArn",
                        linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                            devices=[batch.CfnJobDefinition.DeviceProperty(
                                container_path="containerPath",
                                host_path="hostPath",
                                permissions=["permissions"]
                            )],
                            init_process_enabled=False,
                            max_swap=123,
                            shared_memory_size=123,
                            swappiness=123,
                            tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                                container_path="containerPath",
                                size=123,
                
                                # the properties below are optional
                                mount_options=["mountOptions"]
                            )]
                        ),
                        log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                            log_driver="logDriver",
                
                            # the properties below are optional
                            options=options,
                            secret_options=[batch.CfnJobDefinition.SecretProperty(
                                name="name",
                                value_from="valueFrom"
                            )]
                        ),
                        memory=123,
                        mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                            container_path="containerPath",
                            read_only=False,
                            source_volume="sourceVolume"
                        )],
                        network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                            assign_public_ip="assignPublicIp"
                        ),
                        privileged=False,
                        readonly_root_filesystem=False,
                        resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                            type="type",
                            value="value"
                        )],
                        runtime_platform=batch.CfnJobDefinition.RuntimePlatformProperty(
                            cpu_architecture="cpuArchitecture",
                            operating_system_family="operatingSystemFamily"
                        ),
                        secrets=[batch.CfnJobDefinition.SecretProperty(
                            name="name",
                            value_from="valueFrom"
                        )],
                        ulimits=[batch.CfnJobDefinition.UlimitProperty(
                            hard_limit=123,
                            name="name",
                            soft_limit=123
                        )],
                        user="user",
                        vcpus=123,
                        volumes=[batch.CfnJobDefinition.VolumesProperty(
                            efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                                file_system_id="fileSystemId",
                
                                # the properties below are optional
                                authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                    access_point_id="accessPointId",
                                    iam="iam"
                                ),
                                root_directory="rootDirectory",
                                transit_encryption="transitEncryption",
                                transit_encryption_port=123
                            ),
                            host=batch.CfnJobDefinition.VolumesHostProperty(
                                source_path="sourcePath"
                            ),
                            name="name"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__005c21025a81827c3f5ed456b171eb7ffdf652583c7da0ff6ff67186436afeee)
                check_type(argname="argument target_nodes", value=target_nodes, expected_type=type_hints["target_nodes"])
                check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_nodes": target_nodes,
            }
            if container is not None:
                self._values["container"] = container

        @builtins.property
        def target_nodes(self) -> builtins.str:
            '''The range of nodes, using node index values.

            A range of ``0:3`` indicates nodes with index values of ``0`` through ``3`` . If the starting range value is omitted ( ``:n`` ), then ``0`` is used to start the range. If the ending range value is omitted ( ``n:`` ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes ( ``0:n`` ). You can nest node ranges (for example, ``0:10`` and ``4:5`` ). In this case, the ``4:5`` range properties override the ``0:10`` properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html#cfn-batch-jobdefinition-noderangeproperty-targetnodes
            '''
            result = self._values.get("target_nodes")
            assert result is not None, "Required property 'target_nodes' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ContainerPropertiesProperty"]]:
            '''The container details for the node range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html#cfn-batch-jobdefinition-noderangeproperty-container
            '''
            result = self._values.get("container")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.ContainerPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeRangePropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.PodPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "containers": "containers",
            "dns_policy": "dnsPolicy",
            "host_network": "hostNetwork",
            "metadata": "metadata",
            "service_account_name": "serviceAccountName",
            "volumes": "volumes",
        },
    )
    class PodPropertiesProperty:
        def __init__(
            self,
            *,
            containers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EksContainerProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            dns_policy: typing.Optional[builtins.str] = None,
            host_network: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.MetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_account_name: typing.Optional[builtins.str] = None,
            volumes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EksVolumeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The properties for the pod.

            :param containers: The properties of the container that's used on the Amazon EKS pod.
            :param dns_policy: The DNS policy for the pod. The default value is ``ClusterFirst`` . If the ``hostNetwork`` parameter is not specified, the default is ``ClusterFirstWithHostNet`` . ``ClusterFirst`` indicates that any DNS query that does not match the configured cluster domain suffix is forwarded to the upstream nameserver inherited from the node. If no value was specified for ``dnsPolicy`` in the `RegisterJobDefinition <https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html>`_ API operation, then no value will be returned for ``dnsPolicy`` by either of `DescribeJobDefinitions <https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobDefinitions.html>`_ or `DescribeJobs <https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobs.html>`_ API operations. The pod spec setting will contain either ``ClusterFirst`` or ``ClusterFirstWithHostNet`` , depending on the value of the ``hostNetwork`` parameter. For more information, see `Pod's DNS policy <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy>`_ in the *Kubernetes documentation* . Valid values: ``Default`` | ``ClusterFirst`` | ``ClusterFirstWithHostNet``
            :param host_network: Indicates if the pod uses the hosts' network IP address. The default value is ``true`` . Setting this to ``false`` enables the Kubernetes pod networking model. Most AWS Batch workloads are egress-only and don't require the overhead of IP allocation for each pod for incoming connections. For more information, see `Host namespaces <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/security/pod-security-policy/#host-namespaces>`_ and `Pod networking <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking>`_ in the *Kubernetes documentation* .
            :param metadata: 
            :param service_account_name: The name of the service account that's used to run the pod. For more information, see `Kubernetes service accounts <https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html>`_ and `Configure a Kubernetes service account to assume an IAM role <https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html>`_ in the *Amazon EKS User Guide* and `Configure service accounts for pods <https://docs.aws.amazon.com/https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/>`_ in the *Kubernetes documentation* .
            :param volumes: Specifies the volumes for a job definition that uses Amazon EKS resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # labels: Any
                # limits: Any
                # requests: Any
                
                pod_properties_property = batch.CfnJobDefinition.PodPropertiesProperty(
                    containers=[batch.CfnJobDefinition.EksContainerProperty(
                        image="image",
                
                        # the properties below are optional
                        args=["args"],
                        command=["command"],
                        env=[batch.CfnJobDefinition.EksContainerEnvironmentVariableProperty(
                            name="name",
                
                            # the properties below are optional
                            value="value"
                        )],
                        image_pull_policy="imagePullPolicy",
                        name="name",
                        resources=batch.CfnJobDefinition.ResourcesProperty(
                            limits=limits,
                            requests=requests
                        ),
                        security_context=batch.CfnJobDefinition.SecurityContextProperty(
                            privileged=False,
                            read_only_root_filesystem=False,
                            run_as_group=123,
                            run_as_non_root=False,
                            run_as_user=123
                        ),
                        volume_mounts=[batch.CfnJobDefinition.EksContainerVolumeMountProperty(
                            mount_path="mountPath",
                            name="name",
                            read_only=False
                        )]
                    )],
                    dns_policy="dnsPolicy",
                    host_network=False,
                    metadata=batch.CfnJobDefinition.MetadataProperty(
                        labels=labels
                    ),
                    service_account_name="serviceAccountName",
                    volumes=[batch.CfnJobDefinition.EksVolumeProperty(
                        name="name",
                
                        # the properties below are optional
                        empty_dir=batch.CfnJobDefinition.EmptyDirProperty(
                            medium="medium",
                            size_limit="sizeLimit"
                        ),
                        host_path=batch.CfnJobDefinition.HostPathProperty(
                            path="path"
                        ),
                        secret=batch.CfnJobDefinition.EksSecretProperty(
                            secret_name="secretName",
                
                            # the properties below are optional
                            optional=False
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__75127ae5a1697c34be5f24dcb69fa5c36a3498e1b2c284babc814c444bc47b1c)
                check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
                check_type(argname="argument dns_policy", value=dns_policy, expected_type=type_hints["dns_policy"])
                check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
                check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
                check_type(argname="argument service_account_name", value=service_account_name, expected_type=type_hints["service_account_name"])
                check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if containers is not None:
                self._values["containers"] = containers
            if dns_policy is not None:
                self._values["dns_policy"] = dns_policy
            if host_network is not None:
                self._values["host_network"] = host_network
            if metadata is not None:
                self._values["metadata"] = metadata
            if service_account_name is not None:
                self._values["service_account_name"] = service_account_name
            if volumes is not None:
                self._values["volumes"] = volumes

        @builtins.property
        def containers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksContainerProperty"]]]]:
            '''The properties of the container that's used on the Amazon EKS pod.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-containers
            '''
            result = self._values.get("containers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksContainerProperty"]]]], result)

        @builtins.property
        def dns_policy(self) -> typing.Optional[builtins.str]:
            '''The DNS policy for the pod.

            The default value is ``ClusterFirst`` . If the ``hostNetwork`` parameter is not specified, the default is ``ClusterFirstWithHostNet`` . ``ClusterFirst`` indicates that any DNS query that does not match the configured cluster domain suffix is forwarded to the upstream nameserver inherited from the node. If no value was specified for ``dnsPolicy`` in the `RegisterJobDefinition <https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html>`_ API operation, then no value will be returned for ``dnsPolicy`` by either of `DescribeJobDefinitions <https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobDefinitions.html>`_ or `DescribeJobs <https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobs.html>`_ API operations. The pod spec setting will contain either ``ClusterFirst`` or ``ClusterFirstWithHostNet`` , depending on the value of the ``hostNetwork`` parameter. For more information, see `Pod's DNS policy <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy>`_ in the *Kubernetes documentation* .

            Valid values: ``Default`` | ``ClusterFirst`` | ``ClusterFirstWithHostNet``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-dnspolicy
            '''
            result = self._values.get("dns_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def host_network(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates if the pod uses the hosts' network IP address.

            The default value is ``true`` . Setting this to ``false`` enables the Kubernetes pod networking model. Most AWS Batch workloads are egress-only and don't require the overhead of IP allocation for each pod for incoming connections. For more information, see `Host namespaces <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/security/pod-security-policy/#host-namespaces>`_ and `Pod networking <https://docs.aws.amazon.com/https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-hostnetwork
            '''
            result = self._values.get("host_network")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def metadata(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.MetadataProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-metadata
            '''
            result = self._values.get("metadata")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.MetadataProperty"]], result)

        @builtins.property
        def service_account_name(self) -> typing.Optional[builtins.str]:
            '''The name of the service account that's used to run the pod.

            For more information, see `Kubernetes service accounts <https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html>`_ and `Configure a Kubernetes service account to assume an IAM role <https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html>`_ in the *Amazon EKS User Guide* and `Configure service accounts for pods <https://docs.aws.amazon.com/https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/>`_ in the *Kubernetes documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-serviceaccountname
            '''
            result = self._values.get("service_account_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volumes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksVolumeProperty"]]]]:
            '''Specifies the volumes for a job definition that uses Amazon EKS resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-volumes
            '''
            result = self._values.get("volumes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EksVolumeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PodPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.ResourceRequirementProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class ResourceRequirementProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The type and amount of a resource to assign to a container.

            The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :param type: The type of resource to assign to a container. The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .
            :param value: The quantity of the specified resource to reserve for the container. The values vary based on the ``type`` specified. - **type="GPU"** - The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesn't exceed the number of available GPUs on the compute resource that the job is launched on. .. epigraph:: GPUs aren't available for jobs that are running on Fargate resources. - **type="MEMORY"** - The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: If you're trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory management <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`_ in the *AWS Batch User Guide* . For jobs that are running on Fargate resources, then ``value`` is the hard limit (in MiB), and must match one of the supported values and the ``VCPU`` values must be one of the values supported for that memory value. - **value = 512** - ``VCPU`` = 0.25 - **value = 1024** - ``VCPU`` = 0.25 or 0.5 - **value = 2048** - ``VCPU`` = 0.25, 0.5, or 1 - **value = 3072** - ``VCPU`` = 0.5, or 1 - **value = 4096** - ``VCPU`` = 0.5, 1, or 2 - **value = 5120, 6144, or 7168** - ``VCPU`` = 1 or 2 - **value = 8192** - ``VCPU`` = 1, 2, or 4 - **value = 9216, 10240, 11264, 12288, 13312, 14336, or 15360** - ``VCPU`` = 2 or 4 - **value = 16384** - ``VCPU`` = 2, 4, or 8 - **value = 17408, 18432, 19456, 21504, 22528, 23552, 25600, 26624, 27648, 29696, or 30720** - ``VCPU`` = 4 - **value = 20480, 24576, or 28672** - ``VCPU`` = 4 or 8 - **value = 36864, 45056, 53248, or 61440** - ``VCPU`` = 8 - **value = 32768, 40960, 49152, or 57344** - ``VCPU`` = 8 or 16 - **value = 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880** - ``VCPU`` = 16 - **type="VCPU"** - The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . Each vCPU is equivalent to 1,024 CPU shares. For EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once. The default for the Fargate On-Demand vCPU resource count quota is 6 vCPUs. For more information about Fargate quotas, see `AWS Fargate quotas <https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#service-quotas-fargate>`_ in the *AWS General Reference* . For jobs that are running on Fargate resources, then ``value`` must match one of the supported values and the ``MEMORY`` values must be one of the values supported for that ``VCPU`` value. The supported values are 0.25, 0.5, 1, 2, 4, 8, and 16 - **value = 0.25** - ``MEMORY`` = 512, 1024, or 2048 - **value = 0.5** - ``MEMORY`` = 1024, 2048, 3072, or 4096 - **value = 1** - ``MEMORY`` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192 - **value = 2** - ``MEMORY`` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384 - **value = 4** - ``MEMORY`` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720 - **value = 8** - ``MEMORY`` = 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, or 61440 - **value = 16** - ``MEMORY`` = 32768, 40960, 49152, 57344, 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                resource_requirement_property = batch.CfnJobDefinition.ResourceRequirementProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7384d4b3b97f8aebbaa3dfe7ec74991276f6b53d6e1885662f675369f1d0166c)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of resource to assign to a container.

            The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html#cfn-batch-jobdefinition-resourcerequirement-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The quantity of the specified resource to reserve for the container. The values vary based on the ``type`` specified.

            - **type="GPU"** - The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesn't exceed the number of available GPUs on the compute resource that the job is launched on.

            .. epigraph::

               GPUs aren't available for jobs that are running on Fargate resources.

            - **type="MEMORY"** - The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            .. epigraph::

               If you're trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory management <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`_ in the *AWS Batch User Guide* .

            For jobs that are running on Fargate resources, then ``value`` is the hard limit (in MiB), and must match one of the supported values and the ``VCPU`` values must be one of the values supported for that memory value.

            - **value = 512** - ``VCPU`` = 0.25
            - **value = 1024** - ``VCPU`` = 0.25 or 0.5
            - **value = 2048** - ``VCPU`` = 0.25, 0.5, or 1
            - **value = 3072** - ``VCPU`` = 0.5, or 1
            - **value = 4096** - ``VCPU`` = 0.5, 1, or 2
            - **value = 5120, 6144, or 7168** - ``VCPU`` = 1 or 2
            - **value = 8192** - ``VCPU`` = 1, 2, or 4
            - **value = 9216, 10240, 11264, 12288, 13312, 14336, or 15360** - ``VCPU`` = 2 or 4
            - **value = 16384** - ``VCPU`` = 2, 4, or 8
            - **value = 17408, 18432, 19456, 21504, 22528, 23552, 25600, 26624, 27648, 29696, or 30720** - ``VCPU`` = 4
            - **value = 20480, 24576, or 28672** - ``VCPU`` = 4 or 8
            - **value = 36864, 45056, 53248, or 61440** - ``VCPU`` = 8
            - **value = 32768, 40960, 49152, or 57344** - ``VCPU`` = 8 or 16
            - **value = 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880** - ``VCPU`` = 16
            - **type="VCPU"** - The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . Each vCPU is equivalent to 1,024 CPU shares. For EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once.

            The default for the Fargate On-Demand vCPU resource count quota is 6 vCPUs. For more information about Fargate quotas, see `AWS Fargate quotas <https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#service-quotas-fargate>`_ in the *AWS General Reference* .

            For jobs that are running on Fargate resources, then ``value`` must match one of the supported values and the ``MEMORY`` values must be one of the values supported for that ``VCPU`` value. The supported values are 0.25, 0.5, 1, 2, 4, 8, and 16

            - **value = 0.25** - ``MEMORY`` = 512, 1024, or 2048
            - **value = 0.5** - ``MEMORY`` = 1024, 2048, 3072, or 4096
            - **value = 1** - ``MEMORY`` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192
            - **value = 2** - ``MEMORY`` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384
            - **value = 4** - ``MEMORY`` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720
            - **value = 8** - ``MEMORY`` = 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, or 61440
            - **value = 16** - ``MEMORY`` = 32768, 40960, 49152, 57344, 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html#cfn-batch-jobdefinition-resourcerequirement-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceRequirementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.ResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"limits": "limits", "requests": "requests"},
    )
    class ResourcesProperty:
        def __init__(
            self,
            *,
            limits: typing.Any = None,
            requests: typing.Any = None,
        ) -> None:
            '''
            :param limits: 
            :param requests: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                # limits: Any
                # requests: Any
                
                resources_property = batch.CfnJobDefinition.ResourcesProperty(
                    limits=limits,
                    requests=requests
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__634ef7ff057388be2736fb45bfab10d038183951137f893e49e433ed83008f6a)
                check_type(argname="argument limits", value=limits, expected_type=type_hints["limits"])
                check_type(argname="argument requests", value=requests, expected_type=type_hints["requests"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if limits is not None:
                self._values["limits"] = limits
            if requests is not None:
                self._values["requests"] = requests

        @builtins.property
        def limits(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resources.html#cfn-batch-jobdefinition-resources-limits
            '''
            result = self._values.get("limits")
            return typing.cast(typing.Any, result)

        @builtins.property
        def requests(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resources.html#cfn-batch-jobdefinition-resources-requests
            '''
            result = self._values.get("requests")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.RetryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"attempts": "attempts", "evaluate_on_exit": "evaluateOnExit"},
    )
    class RetryStrategyProperty:
        def __init__(
            self,
            *,
            attempts: typing.Optional[jsii.Number] = None,
            evaluate_on_exit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EvaluateOnExitProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The retry strategy that's associated with a job.

            For more information, see `Automated job retries <https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html>`_ in the *AWS Batch User Guide* .

            :param attempts: The number of times to move a job to the ``RUNNABLE`` status. You can specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the same number of attempts as the value.
            :param evaluate_on_exit: Array of up to 5 objects that specify the conditions where jobs are retried or failed. If this parameter is specified, then the ``attempts`` parameter must also be specified. If none of the listed conditions match, then the job is retried.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                retry_strategy_property = batch.CfnJobDefinition.RetryStrategyProperty(
                    attempts=123,
                    evaluate_on_exit=[batch.CfnJobDefinition.EvaluateOnExitProperty(
                        action="action",
                
                        # the properties below are optional
                        on_exit_code="onExitCode",
                        on_reason="onReason",
                        on_status_reason="onStatusReason"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__800b22bca4d215e51bdb19588f0ed454bc972b986dd5a03f640fe8681acd52be)
                check_type(argname="argument attempts", value=attempts, expected_type=type_hints["attempts"])
                check_type(argname="argument evaluate_on_exit", value=evaluate_on_exit, expected_type=type_hints["evaluate_on_exit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attempts is not None:
                self._values["attempts"] = attempts
            if evaluate_on_exit is not None:
                self._values["evaluate_on_exit"] = evaluate_on_exit

        @builtins.property
        def attempts(self) -> typing.Optional[jsii.Number]:
            '''The number of times to move a job to the ``RUNNABLE`` status.

            You can specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the same number of attempts as the value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html#cfn-batch-jobdefinition-retrystrategy-attempts
            '''
            result = self._values.get("attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def evaluate_on_exit(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EvaluateOnExitProperty"]]]]:
            '''Array of up to 5 objects that specify the conditions where jobs are retried or failed.

            If this parameter is specified, then the ``attempts`` parameter must also be specified. If none of the listed conditions match, then the job is retried.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html#cfn-batch-jobdefinition-retrystrategy-evaluateonexit
            '''
            result = self._values.get("evaluate_on_exit")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EvaluateOnExitProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.RuntimePlatformProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu_architecture": "cpuArchitecture",
            "operating_system_family": "operatingSystemFamily",
        },
    )
    class RuntimePlatformProperty:
        def __init__(
            self,
            *,
            cpu_architecture: typing.Optional[builtins.str] = None,
            operating_system_family: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param cpu_architecture: 
            :param operating_system_family: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-runtimeplatform.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                runtime_platform_property = batch.CfnJobDefinition.RuntimePlatformProperty(
                    cpu_architecture="cpuArchitecture",
                    operating_system_family="operatingSystemFamily"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbdffb76b27dbbdbbc0d2ebc2229966bd04e50d9dbe061567a0dba94004d9e3e)
                check_type(argname="argument cpu_architecture", value=cpu_architecture, expected_type=type_hints["cpu_architecture"])
                check_type(argname="argument operating_system_family", value=operating_system_family, expected_type=type_hints["operating_system_family"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cpu_architecture is not None:
                self._values["cpu_architecture"] = cpu_architecture
            if operating_system_family is not None:
                self._values["operating_system_family"] = operating_system_family

        @builtins.property
        def cpu_architecture(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-runtimeplatform.html#cfn-batch-jobdefinition-runtimeplatform-cpuarchitecture
            '''
            result = self._values.get("cpu_architecture")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operating_system_family(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-runtimeplatform.html#cfn-batch-jobdefinition-runtimeplatform-operatingsystemfamily
            '''
            result = self._values.get("operating_system_family")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuntimePlatformProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.SecretProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value_from": "valueFrom"},
    )
    class SecretProperty:
        def __init__(self, *, name: builtins.str, value_from: builtins.str) -> None:
            '''An object that represents the secret to expose to your container.

            Secrets can be exposed to a container in the following ways:

            - To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter.
            - To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter.

            For more information, see `Specifying sensitive data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`_ in the *AWS Batch User Guide* .

            :param name: The name of the secret.
            :param value_from: The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store. .. epigraph:: If the AWS Systems Manager Parameter Store parameter exists in the same Region as the job you're launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                secret_property = batch.CfnJobDefinition.SecretProperty(
                    name="name",
                    value_from="valueFrom"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__627c25c89399f4c648455cf23b1833f2f5961be5393bea72498980b6dd1b8fac)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value_from", value=value_from, expected_type=type_hints["value_from"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value_from": value_from,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html#cfn-batch-jobdefinition-secret-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_from(self) -> builtins.str:
            '''The secret to expose to the container.

            The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
            .. epigraph::

               If the AWS Systems Manager Parameter Store parameter exists in the same Region as the job you're launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html#cfn-batch-jobdefinition-secret-valuefrom
            '''
            result = self._values.get("value_from")
            assert result is not None, "Required property 'value_from' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.SecurityContextProperty",
        jsii_struct_bases=[],
        name_mapping={
            "privileged": "privileged",
            "read_only_root_filesystem": "readOnlyRootFilesystem",
            "run_as_group": "runAsGroup",
            "run_as_non_root": "runAsNonRoot",
            "run_as_user": "runAsUser",
        },
    )
    class SecurityContextProperty:
        def __init__(
            self,
            *,
            privileged: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            run_as_group: typing.Optional[jsii.Number] = None,
            run_as_non_root: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            run_as_user: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param privileged: 
            :param read_only_root_filesystem: 
            :param run_as_group: 
            :param run_as_non_root: 
            :param run_as_user: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-securitycontext.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                security_context_property = batch.CfnJobDefinition.SecurityContextProperty(
                    privileged=False,
                    read_only_root_filesystem=False,
                    run_as_group=123,
                    run_as_non_root=False,
                    run_as_user=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ecf4bfd8ece80e1bc3ee0536353fc145f3c5b08f62a604a53b62e7d2526f9d0e)
                check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
                check_type(argname="argument read_only_root_filesystem", value=read_only_root_filesystem, expected_type=type_hints["read_only_root_filesystem"])
                check_type(argname="argument run_as_group", value=run_as_group, expected_type=type_hints["run_as_group"])
                check_type(argname="argument run_as_non_root", value=run_as_non_root, expected_type=type_hints["run_as_non_root"])
                check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if privileged is not None:
                self._values["privileged"] = privileged
            if read_only_root_filesystem is not None:
                self._values["read_only_root_filesystem"] = read_only_root_filesystem
            if run_as_group is not None:
                self._values["run_as_group"] = run_as_group
            if run_as_non_root is not None:
                self._values["run_as_non_root"] = run_as_non_root
            if run_as_user is not None:
                self._values["run_as_user"] = run_as_user

        @builtins.property
        def privileged(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-securitycontext.html#cfn-batch-jobdefinition-securitycontext-privileged
            '''
            result = self._values.get("privileged")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def read_only_root_filesystem(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-securitycontext.html#cfn-batch-jobdefinition-securitycontext-readonlyrootfilesystem
            '''
            result = self._values.get("read_only_root_filesystem")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def run_as_group(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-securitycontext.html#cfn-batch-jobdefinition-securitycontext-runasgroup
            '''
            result = self._values.get("run_as_group")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def run_as_non_root(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-securitycontext.html#cfn-batch-jobdefinition-securitycontext-runasnonroot
            '''
            result = self._values.get("run_as_non_root")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def run_as_user(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-securitycontext.html#cfn-batch-jobdefinition-securitycontext-runasuser
            '''
            result = self._values.get("run_as_user")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecurityContextProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.TimeoutProperty",
        jsii_struct_bases=[],
        name_mapping={"attempt_duration_seconds": "attemptDurationSeconds"},
    )
    class TimeoutProperty:
        def __init__(
            self,
            *,
            attempt_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An object that represents a job timeout configuration.

            :param attempt_duration_seconds: The job timeout time (in seconds) that's measured from the job attempt's ``startedAt`` timestamp. After this time passes, AWS Batch terminates your jobs if they aren't finished. The minimum value for the timeout is 60 seconds. For array jobs, the timeout applies to the child jobs, not to the parent array job. For multi-node parallel (MNP) jobs, the timeout applies to the whole job, not to the individual nodes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                timeout_property = batch.CfnJobDefinition.TimeoutProperty(
                    attempt_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b035a85f593ff8b58d3fbc57a8614a7bc0d733c70f8504eab630022b6186187)
                check_type(argname="argument attempt_duration_seconds", value=attempt_duration_seconds, expected_type=type_hints["attempt_duration_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attempt_duration_seconds is not None:
                self._values["attempt_duration_seconds"] = attempt_duration_seconds

        @builtins.property
        def attempt_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The job timeout time (in seconds) that's measured from the job attempt's ``startedAt`` timestamp.

            After this time passes, AWS Batch terminates your jobs if they aren't finished. The minimum value for the timeout is 60 seconds.

            For array jobs, the timeout applies to the child jobs, not to the parent array job.

            For multi-node parallel (MNP) jobs, the timeout applies to the whole job, not to the individual nodes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html#cfn-batch-jobdefinition-timeout-attemptdurationseconds
            '''
            result = self._values.get("attempt_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.TmpfsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_path": "containerPath",
            "size": "size",
            "mount_options": "mountOptions",
        },
    )
    class TmpfsProperty:
        def __init__(
            self,
            *,
            container_path: builtins.str,
            size: jsii.Number,
            mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The container path, mount options, and size of the ``tmpfs`` mount.

            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources.

            :param container_path: The absolute file path in the container where the ``tmpfs`` volume is mounted.
            :param size: The size (in MiB) of the ``tmpfs`` volume.
            :param mount_options: The list of ``tmpfs`` volume mount options. Valid values: " ``defaults`` " | " ``ro`` " | " ``rw`` " | " ``suid`` " | " ``nosuid`` " | " ``dev`` " | " ``nodev`` " | " ``exec`` " | " ``noexec`` " | " ``sync`` " | " ``async`` " | " ``dirsync`` " | " ``remount`` " | " ``mand`` " | " ``nomand`` " | " ``atime`` " | " ``noatime`` " | " ``diratime`` " | " ``nodiratime`` " | " ``bind`` " | " ``rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime`` " | " ``norelatime`` " | " ``strictatime`` " | " ``nostrictatime`` " | " ``mode`` " | " ``uid`` " | " ``gid`` " | " ``nr_inodes`` " | " ``nr_blocks`` " | " ``mpol`` "

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                tmpfs_property = batch.CfnJobDefinition.TmpfsProperty(
                    container_path="containerPath",
                    size=123,
                
                    # the properties below are optional
                    mount_options=["mountOptions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c16bfb0295986db06cd649d9ca6994f1d86d2d884185ad1eda92e6da68041e0)
                check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
                check_type(argname="argument size", value=size, expected_type=type_hints["size"])
                check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_path": container_path,
                "size": size,
            }
            if mount_options is not None:
                self._values["mount_options"] = mount_options

        @builtins.property
        def container_path(self) -> builtins.str:
            '''The absolute file path in the container where the ``tmpfs`` volume is mounted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-containerpath
            '''
            result = self._values.get("container_path")
            assert result is not None, "Required property 'container_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def size(self) -> jsii.Number:
            '''The size (in MiB) of the ``tmpfs`` volume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-size
            '''
            result = self._values.get("size")
            assert result is not None, "Required property 'size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of ``tmpfs`` volume mount options.

            Valid values: " ``defaults`` " | " ``ro`` " | " ``rw`` " | " ``suid`` " | " ``nosuid`` " | " ``dev`` " | " ``nodev`` " | " ``exec`` " | " ``noexec`` " | " ``sync`` " | " ``async`` " | " ``dirsync`` " | " ``remount`` " | " ``mand`` " | " ``nomand`` " | " ``atime`` " | " ``noatime`` " | " ``diratime`` " | " ``nodiratime`` " | " ``bind`` " | " ``rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime`` " | " ``norelatime`` " | " ``strictatime`` " | " ``nostrictatime`` " | " ``mode`` " | " ``uid`` " | " ``gid`` " | " ``nr_inodes`` " | " ``nr_blocks`` " | " ``mpol`` "

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-mountoptions
            '''
            result = self._values.get("mount_options")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TmpfsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.UlimitProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hard_limit": "hardLimit",
            "name": "name",
            "soft_limit": "softLimit",
        },
    )
    class UlimitProperty:
        def __init__(
            self,
            *,
            hard_limit: jsii.Number,
            name: builtins.str,
            soft_limit: jsii.Number,
        ) -> None:
            '''The ``ulimit`` settings to pass to the container.

            .. epigraph::

               This object isn't applicable to jobs that are running on Fargate resources.

            :param hard_limit: The hard limit for the ``ulimit`` type.
            :param name: The ``type`` of the ``ulimit`` .
            :param soft_limit: The soft limit for the ``ulimit`` type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                ulimit_property = batch.CfnJobDefinition.UlimitProperty(
                    hard_limit=123,
                    name="name",
                    soft_limit=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9422053e6f2d5b223ad6edca9c1d424075ea7f34d3f55f01ed34ea8f4b51e8d4)
                check_type(argname="argument hard_limit", value=hard_limit, expected_type=type_hints["hard_limit"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument soft_limit", value=soft_limit, expected_type=type_hints["soft_limit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hard_limit": hard_limit,
                "name": name,
                "soft_limit": soft_limit,
            }

        @builtins.property
        def hard_limit(self) -> jsii.Number:
            '''The hard limit for the ``ulimit`` type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-hardlimit
            '''
            result = self._values.get("hard_limit")
            assert result is not None, "Required property 'hard_limit' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The ``type`` of the ``ulimit`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def soft_limit(self) -> jsii.Number:
            '''The soft limit for the ``ulimit`` type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-softlimit
            '''
            result = self._values.get("soft_limit")
            assert result is not None, "Required property 'soft_limit' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UlimitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.VolumesHostProperty",
        jsii_struct_bases=[],
        name_mapping={"source_path": "sourcePath"},
    )
    class VolumesHostProperty:
        def __init__(
            self,
            *,
            source_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Determine whether your data volume persists on the host container instance and where it's stored.

            If this parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.

            :param source_path: The path on the host container instance that's presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported. .. epigraph:: This parameter isn't applicable to jobs that run on Fargate resources. Don't provide this for these jobs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                volumes_host_property = batch.CfnJobDefinition.VolumesHostProperty(
                    source_path="sourcePath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1af85cd0eadb4e77501a8751a1c3fc18ec19311f49db5d0f921588460010456a)
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source_path is not None:
                self._values["source_path"] = source_path

        @builtins.property
        def source_path(self) -> typing.Optional[builtins.str]:
            '''The path on the host container instance that's presented to the container.

            If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
            .. epigraph::

               This parameter isn't applicable to jobs that run on Fargate resources. Don't provide this for these jobs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html#cfn-batch-jobdefinition-volumeshost-sourcepath
            '''
            result = self._values.get("source_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumesHostProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinition.VolumesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "efs_volume_configuration": "efsVolumeConfiguration",
            "host": "host",
            "name": "name",
        },
    )
    class VolumesProperty:
        def __init__(
            self,
            *,
            efs_volume_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.EfsVolumeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            host: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobDefinition.VolumesHostProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A list of volumes that are associated with the job.

            :param efs_volume_configuration: This is used when you're using an Amazon Elastic File System file system for job storage. For more information, see `Amazon EFS Volumes <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html>`_ in the *AWS Batch User Guide* .
            :param host: The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it's stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running. .. epigraph:: This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
            :param name: The name of the volume. It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                volumes_property = batch.CfnJobDefinition.VolumesProperty(
                    efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                        file_system_id="fileSystemId",
                
                        # the properties below are optional
                        authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                            access_point_id="accessPointId",
                            iam="iam"
                        ),
                        root_directory="rootDirectory",
                        transit_encryption="transitEncryption",
                        transit_encryption_port=123
                    ),
                    host=batch.CfnJobDefinition.VolumesHostProperty(
                        source_path="sourcePath"
                    ),
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4a9d90db8477ca586c3c89fb2ce5a548e9a3bb699ae625a80a8a105b02a362e)
                check_type(argname="argument efs_volume_configuration", value=efs_volume_configuration, expected_type=type_hints["efs_volume_configuration"])
                check_type(argname="argument host", value=host, expected_type=type_hints["host"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if efs_volume_configuration is not None:
                self._values["efs_volume_configuration"] = efs_volume_configuration
            if host is not None:
                self._values["host"] = host
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def efs_volume_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EfsVolumeConfigurationProperty"]]:
            '''This is used when you're using an Amazon Elastic File System file system for job storage.

            For more information, see `Amazon EFS Volumes <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html>`_ in the *AWS Batch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-efsvolumeconfiguration
            '''
            result = self._values.get("efs_volume_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.EfsVolumeConfigurationProperty"]], result)

        @builtins.property
        def host(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.VolumesHostProperty"]]:
            '''The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it's stored.

            If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.
            .. epigraph::

               This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-host
            '''
            result = self._values.get("host")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobDefinition.VolumesHostProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the volume.

            It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_batch.CfnJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "container_properties": "containerProperties",
        "eks_properties": "eksProperties",
        "job_definition_name": "jobDefinitionName",
        "node_properties": "nodeProperties",
        "parameters": "parameters",
        "platform_capabilities": "platformCapabilities",
        "propagate_tags": "propagateTags",
        "retry_strategy": "retryStrategy",
        "scheduling_priority": "schedulingPriority",
        "tags": "tags",
        "timeout": "timeout",
    },
)
class CfnJobDefinitionProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        container_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.ContainerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        eks_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EksPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        job_definition_name: typing.Optional[builtins.str] = None,
        node_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.NodePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        parameters: typing.Any = None,
        platform_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        propagate_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        retry_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.RetryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        scheduling_priority: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        timeout: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.TimeoutProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnJobDefinition``.

        :param type: The type of job definition. For more information about multi-node parallel jobs, see `Creating a multi-node parallel job definition <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html>`_ in the *AWS Batch User Guide* . .. epigraph:: If the job is run on Fargate resources, then ``multinode`` isn't supported.
        :param container_properties: An object with various properties specific to Amazon ECS based jobs. Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified.
        :param eks_properties: An object with various properties that are specific to Amazon EKS based jobs. Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified.
        :param job_definition_name: The name of the job definition.
        :param node_properties: An object with various properties that are specific to multi-node parallel jobs. Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified. .. epigraph:: If the job runs on Fargate resources, don't specify ``nodeProperties`` . Use ``containerProperties`` instead.
        :param parameters: Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see `Job definition parameters <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`_ in the *AWS Batch User Guide* .
        :param platform_capabilities: The platform capabilities required by the job definition. If no value is specified, it defaults to ``EC2`` . Jobs run on Fargate resources specify ``FARGATE`` .
        :param propagate_tags: Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the ``FAILED`` state.
        :param retry_strategy: The retry strategy to use for failed jobs that are submitted with this job definition.
        :param scheduling_priority: The scheduling priority of the job definition. This only affects jobs in job queues with a fair share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.
        :param tags: The tags that are applied to the job definition.
        :param timeout: The timeout time for jobs that are submitted with this job definition. After the amount of time you specify passes, AWS Batch terminates your jobs if they aren't finished.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_batch as batch
            
            # labels: Any
            # limits: Any
            # options: Any
            # parameters: Any
            # requests: Any
            # tags: Any
            
            cfn_job_definition_props = batch.CfnJobDefinitionProps(
                type="type",
            
                # the properties below are optional
                container_properties=batch.CfnJobDefinition.ContainerPropertiesProperty(
                    image="image",
            
                    # the properties below are optional
                    command=["command"],
                    environment=[batch.CfnJobDefinition.EnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    ephemeral_storage=batch.CfnJobDefinition.EphemeralStorageProperty(
                        size_in_gi_b=123
                    ),
                    execution_role_arn="executionRoleArn",
                    fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                        platform_version="platformVersion"
                    ),
                    instance_type="instanceType",
                    job_role_arn="jobRoleArn",
                    linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                        devices=[batch.CfnJobDefinition.DeviceProperty(
                            container_path="containerPath",
                            host_path="hostPath",
                            permissions=["permissions"]
                        )],
                        init_process_enabled=False,
                        max_swap=123,
                        shared_memory_size=123,
                        swappiness=123,
                        tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                            container_path="containerPath",
                            size=123,
            
                            # the properties below are optional
                            mount_options=["mountOptions"]
                        )]
                    ),
                    log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                        log_driver="logDriver",
            
                        # the properties below are optional
                        options=options,
                        secret_options=[batch.CfnJobDefinition.SecretProperty(
                            name="name",
                            value_from="valueFrom"
                        )]
                    ),
                    memory=123,
                    mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                        container_path="containerPath",
                        read_only=False,
                        source_volume="sourceVolume"
                    )],
                    network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                        assign_public_ip="assignPublicIp"
                    ),
                    privileged=False,
                    readonly_root_filesystem=False,
                    resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                        type="type",
                        value="value"
                    )],
                    runtime_platform=batch.CfnJobDefinition.RuntimePlatformProperty(
                        cpu_architecture="cpuArchitecture",
                        operating_system_family="operatingSystemFamily"
                    ),
                    secrets=[batch.CfnJobDefinition.SecretProperty(
                        name="name",
                        value_from="valueFrom"
                    )],
                    ulimits=[batch.CfnJobDefinition.UlimitProperty(
                        hard_limit=123,
                        name="name",
                        soft_limit=123
                    )],
                    user="user",
                    vcpus=123,
                    volumes=[batch.CfnJobDefinition.VolumesProperty(
                        efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                            file_system_id="fileSystemId",
            
                            # the properties below are optional
                            authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                access_point_id="accessPointId",
                                iam="iam"
                            ),
                            root_directory="rootDirectory",
                            transit_encryption="transitEncryption",
                            transit_encryption_port=123
                        ),
                        host=batch.CfnJobDefinition.VolumesHostProperty(
                            source_path="sourcePath"
                        ),
                        name="name"
                    )]
                ),
                eks_properties=batch.CfnJobDefinition.EksPropertiesProperty(
                    pod_properties=batch.CfnJobDefinition.PodPropertiesProperty(
                        containers=[batch.CfnJobDefinition.EksContainerProperty(
                            image="image",
            
                            # the properties below are optional
                            args=["args"],
                            command=["command"],
                            env=[batch.CfnJobDefinition.EksContainerEnvironmentVariableProperty(
                                name="name",
            
                                # the properties below are optional
                                value="value"
                            )],
                            image_pull_policy="imagePullPolicy",
                            name="name",
                            resources=batch.CfnJobDefinition.ResourcesProperty(
                                limits=limits,
                                requests=requests
                            ),
                            security_context=batch.CfnJobDefinition.SecurityContextProperty(
                                privileged=False,
                                read_only_root_filesystem=False,
                                run_as_group=123,
                                run_as_non_root=False,
                                run_as_user=123
                            ),
                            volume_mounts=[batch.CfnJobDefinition.EksContainerVolumeMountProperty(
                                mount_path="mountPath",
                                name="name",
                                read_only=False
                            )]
                        )],
                        dns_policy="dnsPolicy",
                        host_network=False,
                        metadata=batch.CfnJobDefinition.MetadataProperty(
                            labels=labels
                        ),
                        service_account_name="serviceAccountName",
                        volumes=[batch.CfnJobDefinition.EksVolumeProperty(
                            name="name",
            
                            # the properties below are optional
                            empty_dir=batch.CfnJobDefinition.EmptyDirProperty(
                                medium="medium",
                                size_limit="sizeLimit"
                            ),
                            host_path=batch.CfnJobDefinition.HostPathProperty(
                                path="path"
                            ),
                            secret=batch.CfnJobDefinition.EksSecretProperty(
                                secret_name="secretName",
            
                                # the properties below are optional
                                optional=False
                            )
                        )]
                    )
                ),
                job_definition_name="jobDefinitionName",
                node_properties=batch.CfnJobDefinition.NodePropertiesProperty(
                    main_node=123,
                    node_range_properties=[batch.CfnJobDefinition.NodeRangePropertyProperty(
                        target_nodes="targetNodes",
            
                        # the properties below are optional
                        container=batch.CfnJobDefinition.ContainerPropertiesProperty(
                            image="image",
            
                            # the properties below are optional
                            command=["command"],
                            environment=[batch.CfnJobDefinition.EnvironmentProperty(
                                name="name",
                                value="value"
                            )],
                            ephemeral_storage=batch.CfnJobDefinition.EphemeralStorageProperty(
                                size_in_gi_b=123
                            ),
                            execution_role_arn="executionRoleArn",
                            fargate_platform_configuration=batch.CfnJobDefinition.FargatePlatformConfigurationProperty(
                                platform_version="platformVersion"
                            ),
                            instance_type="instanceType",
                            job_role_arn="jobRoleArn",
                            linux_parameters=batch.CfnJobDefinition.LinuxParametersProperty(
                                devices=[batch.CfnJobDefinition.DeviceProperty(
                                    container_path="containerPath",
                                    host_path="hostPath",
                                    permissions=["permissions"]
                                )],
                                init_process_enabled=False,
                                max_swap=123,
                                shared_memory_size=123,
                                swappiness=123,
                                tmpfs=[batch.CfnJobDefinition.TmpfsProperty(
                                    container_path="containerPath",
                                    size=123,
            
                                    # the properties below are optional
                                    mount_options=["mountOptions"]
                                )]
                            ),
                            log_configuration=batch.CfnJobDefinition.LogConfigurationProperty(
                                log_driver="logDriver",
            
                                # the properties below are optional
                                options=options,
                                secret_options=[batch.CfnJobDefinition.SecretProperty(
                                    name="name",
                                    value_from="valueFrom"
                                )]
                            ),
                            memory=123,
                            mount_points=[batch.CfnJobDefinition.MountPointsProperty(
                                container_path="containerPath",
                                read_only=False,
                                source_volume="sourceVolume"
                            )],
                            network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                                assign_public_ip="assignPublicIp"
                            ),
                            privileged=False,
                            readonly_root_filesystem=False,
                            resource_requirements=[batch.CfnJobDefinition.ResourceRequirementProperty(
                                type="type",
                                value="value"
                            )],
                            runtime_platform=batch.CfnJobDefinition.RuntimePlatformProperty(
                                cpu_architecture="cpuArchitecture",
                                operating_system_family="operatingSystemFamily"
                            ),
                            secrets=[batch.CfnJobDefinition.SecretProperty(
                                name="name",
                                value_from="valueFrom"
                            )],
                            ulimits=[batch.CfnJobDefinition.UlimitProperty(
                                hard_limit=123,
                                name="name",
                                soft_limit=123
                            )],
                            user="user",
                            vcpus=123,
                            volumes=[batch.CfnJobDefinition.VolumesProperty(
                                efs_volume_configuration=batch.CfnJobDefinition.EfsVolumeConfigurationProperty(
                                    file_system_id="fileSystemId",
            
                                    # the properties below are optional
                                    authorization_config=batch.CfnJobDefinition.AuthorizationConfigProperty(
                                        access_point_id="accessPointId",
                                        iam="iam"
                                    ),
                                    root_directory="rootDirectory",
                                    transit_encryption="transitEncryption",
                                    transit_encryption_port=123
                                ),
                                host=batch.CfnJobDefinition.VolumesHostProperty(
                                    source_path="sourcePath"
                                ),
                                name="name"
                            )]
                        )
                    )],
                    num_nodes=123
                ),
                parameters=parameters,
                platform_capabilities=["platformCapabilities"],
                propagate_tags=False,
                retry_strategy=batch.CfnJobDefinition.RetryStrategyProperty(
                    attempts=123,
                    evaluate_on_exit=[batch.CfnJobDefinition.EvaluateOnExitProperty(
                        action="action",
            
                        # the properties below are optional
                        on_exit_code="onExitCode",
                        on_reason="onReason",
                        on_status_reason="onStatusReason"
                    )]
                ),
                scheduling_priority=123,
                tags=tags,
                timeout=batch.CfnJobDefinition.TimeoutProperty(
                    attempt_duration_seconds=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed150d027b29486332c3fd2205a51f3c6f64c25946114fb86a6eba38434e87c9)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument container_properties", value=container_properties, expected_type=type_hints["container_properties"])
            check_type(argname="argument eks_properties", value=eks_properties, expected_type=type_hints["eks_properties"])
            check_type(argname="argument job_definition_name", value=job_definition_name, expected_type=type_hints["job_definition_name"])
            check_type(argname="argument node_properties", value=node_properties, expected_type=type_hints["node_properties"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument platform_capabilities", value=platform_capabilities, expected_type=type_hints["platform_capabilities"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument retry_strategy", value=retry_strategy, expected_type=type_hints["retry_strategy"])
            check_type(argname="argument scheduling_priority", value=scheduling_priority, expected_type=type_hints["scheduling_priority"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if container_properties is not None:
            self._values["container_properties"] = container_properties
        if eks_properties is not None:
            self._values["eks_properties"] = eks_properties
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if node_properties is not None:
            self._values["node_properties"] = node_properties
        if parameters is not None:
            self._values["parameters"] = parameters
        if platform_capabilities is not None:
            self._values["platform_capabilities"] = platform_capabilities
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if retry_strategy is not None:
            self._values["retry_strategy"] = retry_strategy
        if scheduling_priority is not None:
            self._values["scheduling_priority"] = scheduling_priority
        if tags is not None:
            self._values["tags"] = tags
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of job definition.

        For more information about multi-node parallel jobs, see `Creating a multi-node parallel job definition <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html>`_ in the *AWS Batch User Guide* .
        .. epigraph::

           If the job is run on Fargate resources, then ``multinode`` isn't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.ContainerPropertiesProperty]]:
        '''An object with various properties specific to Amazon ECS based jobs.

        Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-containerproperties
        '''
        result = self._values.get("container_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.ContainerPropertiesProperty]], result)

    @builtins.property
    def eks_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.EksPropertiesProperty]]:
        '''An object with various properties that are specific to Amazon EKS based jobs.

        Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-eksproperties
        '''
        result = self._values.get("eks_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.EksPropertiesProperty]], result)

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.NodePropertiesProperty]]:
        '''An object with various properties that are specific to multi-node parallel jobs.

        Valid values are ``containerProperties`` , ``eksProperties`` , and ``nodeProperties`` . Only one can be specified.
        .. epigraph::

           If the job runs on Fargate resources, don't specify ``nodeProperties`` . Use ``containerProperties`` instead.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-nodeproperties
        '''
        result = self._values.get("node_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.NodePropertiesProperty]], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''Default parameters or parameter substitution placeholders that are set in the job definition.

        Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see `Job definition parameters <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`_ in the *AWS Batch User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def platform_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The platform capabilities required by the job definition.

        If no value is specified, it defaults to ``EC2`` . Jobs run on Fargate resources specify ``FARGATE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-platformcapabilities
        '''
        result = self._values.get("platform_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def propagate_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task.

        If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the ``FAILED`` state.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-propagatetags
        '''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def retry_strategy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.RetryStrategyProperty]]:
        '''The retry strategy to use for failed jobs that are submitted with this job definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-retrystrategy
        '''
        result = self._values.get("retry_strategy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.RetryStrategyProperty]], result)

    @builtins.property
    def scheduling_priority(self) -> typing.Optional[jsii.Number]:
        '''The scheduling priority of the job definition.

        This only affects jobs in job queues with a fair share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-schedulingpriority
        '''
        result = self._values.get("scheduling_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The tags that are applied to the job definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def timeout(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.TimeoutProperty]]:
        '''The timeout time for jobs that are submitted with this job definition.

        After the amount of time you specify passes, AWS Batch terminates your jobs if they aren't finished.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.TimeoutProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnJobQueue(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_batch.CfnJobQueue",
):
    '''The ``AWS::Batch::JobQueue`` resource specifies the parameters for an AWS Batch job queue definition.

    For more information, see `Job Queues <https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html>`_ in the ** .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_batch as batch
        
        cfn_job_queue = batch.CfnJobQueue(self, "MyCfnJobQueue",
            compute_environment_order=[batch.CfnJobQueue.ComputeEnvironmentOrderProperty(
                compute_environment="computeEnvironment",
                order=123
            )],
            priority=123,
        
            # the properties below are optional
            job_queue_name="jobQueueName",
            scheduling_policy_arn="schedulingPolicyArn",
            state="state",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        compute_environment_order: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobQueue.ComputeEnvironmentOrderProperty", typing.Dict[builtins.str, typing.Any]]]]],
        priority: jsii.Number,
        job_queue_name: typing.Optional[builtins.str] = None,
        scheduling_policy_arn: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param compute_environment_order: The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed. .. epigraph:: All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.
        :param priority: The priority of the job queue. Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` . All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
        :param job_queue_name: The name of the job queue. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param scheduling_policy_arn: The Amazon Resource Name (ARN) of the scheduling policy. The format is ``aws: *Partition* :batch: *Region* : *Account* :scheduling-policy/ *Name*`` . For example, ``aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy`` .
        :param state: The state of the job queue. If the job queue state is ``ENABLED`` , it is able to accept jobs. If the job queue state is ``DISABLED`` , new jobs can't be added to the queue, but jobs already in the queue can finish.
        :param tags: The tags that are applied to the job queue. For more information, see `Tagging your AWS Batch resources <https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html>`_ in *AWS Batch User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6480ab252bc515b2cdb6dc0c833877438fd473fd39eadf6b8a064969a5fc051d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobQueueProps(
            compute_environment_order=compute_environment_order,
            priority=priority,
            job_queue_name=job_queue_name,
            scheduling_policy_arn=scheduling_policy_arn,
            state=state,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0501823e805eabb76b2d16d277e0e42dcf4e0873c3adb0898fab52f723baa571)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce1fe922d9589f26998c2113a8a19530d98bfc01fe2462a8639a3593512e2368)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrJobQueueArn")
    def attr_job_queue_arn(self) -> builtins.str:
        '''Returns the job queue ARN, such as ``batch: *us-east-1* : *111122223333* :job-queue/ *JobQueueName*`` .

        :cloudformationAttribute: JobQueueArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobQueueArn"))

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
    @jsii.member(jsii_name="computeEnvironmentOrder")
    def compute_environment_order(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobQueue.ComputeEnvironmentOrderProperty"]]]:
        '''The set of compute environments mapped to a job queue and their order relative to each other.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobQueue.ComputeEnvironmentOrderProperty"]]], jsii.get(self, "computeEnvironmentOrder"))

    @compute_environment_order.setter
    def compute_environment_order(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobQueue.ComputeEnvironmentOrderProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa1c2f3f42165309672c3fdf8c286ff9dc5e99756ec1a5b3ffca9e719d4c7036)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeEnvironmentOrder", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''The priority of the job queue.'''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__620331f74c116d31a6d43627e1a45e7041bc3c110194265f30dc193863c8ed94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="jobQueueName")
    def job_queue_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobQueueName"))

    @job_queue_name.setter
    def job_queue_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b88e27e62b46f1049263a61bb14f62674a8121083de64c2db32d585651e1c30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobQueueName", value)

    @builtins.property
    @jsii.member(jsii_name="schedulingPolicyArn")
    def scheduling_policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the scheduling policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulingPolicyArn"))

    @scheduling_policy_arn.setter
    def scheduling_policy_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48a6952b4a8d4426554895a52085bf8c88701735f3f94a3426e81e56ab8a5761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingPolicyArn", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the job queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e97106b05367d04f8f618f0b8edf4f7fdc4b88436890062ac6e344ede4e180b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags that are applied to the job queue.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e658491e12e1806302783cf972183ab89bf0d8d1d3abe7164fad544d18b91367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnJobQueue.ComputeEnvironmentOrderProperty",
        jsii_struct_bases=[],
        name_mapping={"compute_environment": "computeEnvironment", "order": "order"},
    )
    class ComputeEnvironmentOrderProperty:
        def __init__(
            self,
            *,
            compute_environment: builtins.str,
            order: jsii.Number,
        ) -> None:
            '''The order that compute environments are tried in for job placement within a queue.

            Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
            .. epigraph::

               All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.

            :param compute_environment: The Amazon Resource Name (ARN) of the compute environment.
            :param order: The order of the compute environment. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower ``order`` integer value is tried for job placement first.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                compute_environment_order_property = batch.CfnJobQueue.ComputeEnvironmentOrderProperty(
                    compute_environment="computeEnvironment",
                    order=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__939623842116ecc366f7e36591fb2bdd35bd47aacc55c0a794ff81ec2a026c43)
                check_type(argname="argument compute_environment", value=compute_environment, expected_type=type_hints["compute_environment"])
                check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "compute_environment": compute_environment,
                "order": order,
            }

        @builtins.property
        def compute_environment(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the compute environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html#cfn-batch-jobqueue-computeenvironmentorder-computeenvironment
            '''
            result = self._values.get("compute_environment")
            assert result is not None, "Required property 'compute_environment' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def order(self) -> jsii.Number:
            '''The order of the compute environment.

            Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower ``order`` integer value is tried for job placement first.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html#cfn-batch-jobqueue-computeenvironmentorder-order
            '''
            result = self._values.get("order")
            assert result is not None, "Required property 'order' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeEnvironmentOrderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_batch.CfnJobQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "compute_environment_order": "computeEnvironmentOrder",
        "priority": "priority",
        "job_queue_name": "jobQueueName",
        "scheduling_policy_arn": "schedulingPolicyArn",
        "state": "state",
        "tags": "tags",
    },
)
class CfnJobQueueProps:
    def __init__(
        self,
        *,
        compute_environment_order: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobQueue.ComputeEnvironmentOrderProperty, typing.Dict[builtins.str, typing.Any]]]]],
        priority: jsii.Number,
        job_queue_name: typing.Optional[builtins.str] = None,
        scheduling_policy_arn: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnJobQueue``.

        :param compute_environment_order: The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed. .. epigraph:: All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.
        :param priority: The priority of the job queue. Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` . All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
        :param job_queue_name: The name of the job queue. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param scheduling_policy_arn: The Amazon Resource Name (ARN) of the scheduling policy. The format is ``aws: *Partition* :batch: *Region* : *Account* :scheduling-policy/ *Name*`` . For example, ``aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy`` .
        :param state: The state of the job queue. If the job queue state is ``ENABLED`` , it is able to accept jobs. If the job queue state is ``DISABLED`` , new jobs can't be added to the queue, but jobs already in the queue can finish.
        :param tags: The tags that are applied to the job queue. For more information, see `Tagging your AWS Batch resources <https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html>`_ in *AWS Batch User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_batch as batch
            
            cfn_job_queue_props = batch.CfnJobQueueProps(
                compute_environment_order=[batch.CfnJobQueue.ComputeEnvironmentOrderProperty(
                    compute_environment="computeEnvironment",
                    order=123
                )],
                priority=123,
            
                # the properties below are optional
                job_queue_name="jobQueueName",
                scheduling_policy_arn="schedulingPolicyArn",
                state="state",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__009d6d384b1b723169e64875095e05fe852ae3931adf5ba2004d22475a76caa9)
            check_type(argname="argument compute_environment_order", value=compute_environment_order, expected_type=type_hints["compute_environment_order"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument job_queue_name", value=job_queue_name, expected_type=type_hints["job_queue_name"])
            check_type(argname="argument scheduling_policy_arn", value=scheduling_policy_arn, expected_type=type_hints["scheduling_policy_arn"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "compute_environment_order": compute_environment_order,
            "priority": priority,
        }
        if job_queue_name is not None:
            self._values["job_queue_name"] = job_queue_name
        if scheduling_policy_arn is not None:
            self._values["scheduling_policy_arn"] = scheduling_policy_arn
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def compute_environment_order(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnJobQueue.ComputeEnvironmentOrderProperty]]]:
        '''The set of compute environments mapped to a job queue and their order relative to each other.

        The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.
        .. epigraph::

           All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-computeenvironmentorder
        '''
        result = self._values.get("compute_environment_order")
        assert result is not None, "Required property 'compute_environment_order' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnJobQueue.ComputeEnvironmentOrderProperty]]], result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The priority of the job queue.

        Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` . All of the compute environments must be either EC2 ( ``EC2`` or ``SPOT`` ) or Fargate ( ``FARGATE`` or ``FARGATE_SPOT`` ); EC2 and Fargate compute environments can't be mixed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def job_queue_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job queue.

        It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-jobqueuename
        '''
        result = self._values.get("job_queue_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduling_policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the scheduling policy.

        The format is ``aws: *Partition* :batch: *Region* : *Account* :scheduling-policy/ *Name*`` . For example, ``aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-schedulingpolicyarn
        '''
        result = self._values.get("scheduling_policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the job queue.

        If the job queue state is ``ENABLED`` , it is able to accept jobs. If the job queue state is ``DISABLED`` , new jobs can't be added to the queue, but jobs already in the queue can finish.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags that are applied to the job queue.

        For more information, see `Tagging your AWS Batch resources <https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html>`_ in *AWS Batch User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSchedulingPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_batch.CfnSchedulingPolicy",
):
    '''The ``AWS::Batch::SchedulingPolicy`` resource specifies the parameters for an AWS Batch scheduling policy.

    For more information, see `Scheduling Policies <https://docs.aws.amazon.com/batch/latest/userguide/scheduling_policies.html>`_ in the ** .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_batch as batch
        
        cfn_scheduling_policy = batch.CfnSchedulingPolicy(self, "MyCfnSchedulingPolicy",
            fairshare_policy=batch.CfnSchedulingPolicy.FairsharePolicyProperty(
                compute_reservation=123,
                share_decay_seconds=123,
                share_distribution=[batch.CfnSchedulingPolicy.ShareAttributesProperty(
                    share_identifier="shareIdentifier",
                    weight_factor=123
                )]
            ),
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        fairshare_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedulingPolicy.FairsharePolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param fairshare_policy: The fair share policy of the scheduling policy.
        :param name: The name of the scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param tags: The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in *AWS General Reference* . These tags can be updated or removed using the `TagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html>`_ and `UntagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html>`_ API operations.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31a21a4a6536b3efab619619ed719e6b0662b5c83fe7a1dc489b27f0b3ea56db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchedulingPolicyProps(
            fairshare_policy=fairshare_policy, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df36e53e7605cc7837477592dff920fd2c974ea55bea2f8469f2e732ec9524ca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aefdc709a6b9ffad7303fb907694b285dd6ed2a9795b2c93a5ab983d1fc0ab2e)
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
        '''Returns the scheduling policy ARN, such as ``batch: *us-east-1* : *111122223333* :scheduling-policy/ *HighPriority*`` .

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
    @jsii.member(jsii_name="fairsharePolicy")
    def fairshare_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedulingPolicy.FairsharePolicyProperty"]]:
        '''The fair share policy of the scheduling policy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedulingPolicy.FairsharePolicyProperty"]], jsii.get(self, "fairsharePolicy"))

    @fairshare_policy.setter
    def fairshare_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedulingPolicy.FairsharePolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc1fdc7b365c326e80f94bc6ce2c1ba05c54c3d0dc4caaecec7e9eb7ec315b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fairsharePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the scheduling policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__411bf4b677626f26ae0d797bd4706cc6d8b5dbd45471422cf971b438d0f43ee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags that you apply to the scheduling policy to help you categorize and organize your resources.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f828d01fc7085728330a84e961df84cb35664d5a94e9bbf3bcfe93f7b3c7d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnSchedulingPolicy.FairsharePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compute_reservation": "computeReservation",
            "share_decay_seconds": "shareDecaySeconds",
            "share_distribution": "shareDistribution",
        },
    )
    class FairsharePolicyProperty:
        def __init__(
            self,
            *,
            compute_reservation: typing.Optional[jsii.Number] = None,
            share_decay_seconds: typing.Optional[jsii.Number] = None,
            share_distribution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedulingPolicy.ShareAttributesProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The fair share policy for a scheduling policy.

            :param compute_reservation: A value used to reserve some of the available maximum vCPU for fair share identifiers that aren't already used. The reserved ratio is ``( *computeReservation* /100)^ *ActiveFairShares*`` where ``*ActiveFairShares*`` is the number of active fair share identifiers. For example, a ``computeReservation`` value of 50 indicates that AWS Batch reserves 50% of the maximum available vCPU if there's only one fair share identifier. It reserves 25% if there are two fair share identifiers. It reserves 12.5% if there are three fair share identifiers. A ``computeReservation`` value of 25 indicates that AWS Batch should reserve 25% of the maximum available vCPU if there's only one fair share identifier, 6.25% if there are two fair share identifiers, and 1.56% if there are three fair share identifiers. The minimum value is 0 and the maximum value is 99.
            :param share_decay_seconds: The amount of time (in seconds) to use to calculate a fair share percentage for each fair share identifier in use. A value of zero (0) indicates that only current usage is measured. The decay allows for more recently run jobs to have more weight than jobs that ran earlier. The maximum supported value is 604800 (1 week).
            :param share_distribution: An array of ``SharedIdentifier`` objects that contain the weights for the fair share identifiers for the fair share policy. Fair share identifiers that aren't included have a default weight of ``1.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                fairshare_policy_property = batch.CfnSchedulingPolicy.FairsharePolicyProperty(
                    compute_reservation=123,
                    share_decay_seconds=123,
                    share_distribution=[batch.CfnSchedulingPolicy.ShareAttributesProperty(
                        share_identifier="shareIdentifier",
                        weight_factor=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d584604e0200cce08bb1571b600a67b89e1eafdfce088d1cbe150d7b12935adc)
                check_type(argname="argument compute_reservation", value=compute_reservation, expected_type=type_hints["compute_reservation"])
                check_type(argname="argument share_decay_seconds", value=share_decay_seconds, expected_type=type_hints["share_decay_seconds"])
                check_type(argname="argument share_distribution", value=share_distribution, expected_type=type_hints["share_distribution"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compute_reservation is not None:
                self._values["compute_reservation"] = compute_reservation
            if share_decay_seconds is not None:
                self._values["share_decay_seconds"] = share_decay_seconds
            if share_distribution is not None:
                self._values["share_distribution"] = share_distribution

        @builtins.property
        def compute_reservation(self) -> typing.Optional[jsii.Number]:
            '''A value used to reserve some of the available maximum vCPU for fair share identifiers that aren't already used.

            The reserved ratio is ``( *computeReservation* /100)^ *ActiveFairShares*`` where ``*ActiveFairShares*`` is the number of active fair share identifiers.

            For example, a ``computeReservation`` value of 50 indicates that AWS Batch reserves 50% of the maximum available vCPU if there's only one fair share identifier. It reserves 25% if there are two fair share identifiers. It reserves 12.5% if there are three fair share identifiers. A ``computeReservation`` value of 25 indicates that AWS Batch should reserve 25% of the maximum available vCPU if there's only one fair share identifier, 6.25% if there are two fair share identifiers, and 1.56% if there are three fair share identifiers.

            The minimum value is 0 and the maximum value is 99.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-computereservation
            '''
            result = self._values.get("compute_reservation")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def share_decay_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time (in seconds) to use to calculate a fair share percentage for each fair share identifier in use.

            A value of zero (0) indicates that only current usage is measured. The decay allows for more recently run jobs to have more weight than jobs that ran earlier. The maximum supported value is 604800 (1 week).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-sharedecayseconds
            '''
            result = self._values.get("share_decay_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def share_distribution(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedulingPolicy.ShareAttributesProperty"]]]]:
            '''An array of ``SharedIdentifier`` objects that contain the weights for the fair share identifiers for the fair share policy.

            Fair share identifiers that aren't included have a default weight of ``1.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-sharedistribution
            '''
            result = self._values.get("share_distribution")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedulingPolicy.ShareAttributesProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FairsharePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_batch.CfnSchedulingPolicy.ShareAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "share_identifier": "shareIdentifier",
            "weight_factor": "weightFactor",
        },
    )
    class ShareAttributesProperty:
        def __init__(
            self,
            *,
            share_identifier: typing.Optional[builtins.str] = None,
            weight_factor: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the weights for the fair share identifiers for the fair share policy.

            Fair share identifiers that aren't included have a default weight of ``1.0`` .

            :param share_identifier: A fair share identifier or fair share identifier prefix. If the string ends with an asterisk (*), this entry specifies the weight factor to use for fair share identifiers that start with that prefix. The list of fair share identifiers in a fair share policy can't overlap. For example, you can't have one that specifies a ``shareIdentifier`` of ``UserA*`` and another that specifies a ``shareIdentifier`` of ``UserA-1`` . There can be no more than 500 fair share identifiers active in a job queue. The string is limited to 255 alphanumeric characters, and can be followed by an asterisk (*).
            :param weight_factor: The weight factor for the fair share identifier. The default value is 1.0. A lower value has a higher priority for compute resources. For example, jobs that use a share identifier with a weight factor of 0.125 (1/8) get 8 times the compute resources of jobs that use a share identifier with a weight factor of 1. The smallest supported value is 0.0001, and the largest supported value is 999.9999.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_batch as batch
                
                share_attributes_property = batch.CfnSchedulingPolicy.ShareAttributesProperty(
                    share_identifier="shareIdentifier",
                    weight_factor=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a48599c650ce1ded6e5309cc09389c78237f12aa2328bbfe0d3335052f05da70)
                check_type(argname="argument share_identifier", value=share_identifier, expected_type=type_hints["share_identifier"])
                check_type(argname="argument weight_factor", value=weight_factor, expected_type=type_hints["weight_factor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if share_identifier is not None:
                self._values["share_identifier"] = share_identifier
            if weight_factor is not None:
                self._values["weight_factor"] = weight_factor

        @builtins.property
        def share_identifier(self) -> typing.Optional[builtins.str]:
            '''A fair share identifier or fair share identifier prefix.

            If the string ends with an asterisk (*), this entry specifies the weight factor to use for fair share identifiers that start with that prefix. The list of fair share identifiers in a fair share policy can't overlap. For example, you can't have one that specifies a ``shareIdentifier`` of ``UserA*`` and another that specifies a ``shareIdentifier`` of ``UserA-1`` .

            There can be no more than 500 fair share identifiers active in a job queue.

            The string is limited to 255 alphanumeric characters, and can be followed by an asterisk (*).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html#cfn-batch-schedulingpolicy-shareattributes-shareidentifier
            '''
            result = self._values.get("share_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def weight_factor(self) -> typing.Optional[jsii.Number]:
            '''The weight factor for the fair share identifier.

            The default value is 1.0. A lower value has a higher priority for compute resources. For example, jobs that use a share identifier with a weight factor of 0.125 (1/8) get 8 times the compute resources of jobs that use a share identifier with a weight factor of 1.

            The smallest supported value is 0.0001, and the largest supported value is 999.9999.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html#cfn-batch-schedulingpolicy-shareattributes-weightfactor
            '''
            result = self._values.get("weight_factor")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ShareAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_batch.CfnSchedulingPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "fairshare_policy": "fairsharePolicy",
        "name": "name",
        "tags": "tags",
    },
)
class CfnSchedulingPolicyProps:
    def __init__(
        self,
        *,
        fairshare_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedulingPolicy.FairsharePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchedulingPolicy``.

        :param fairshare_policy: The fair share policy of the scheduling policy.
        :param name: The name of the scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
        :param tags: The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in *AWS General Reference* . These tags can be updated or removed using the `TagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html>`_ and `UntagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html>`_ API operations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_batch as batch
            
            cfn_scheduling_policy_props = batch.CfnSchedulingPolicyProps(
                fairshare_policy=batch.CfnSchedulingPolicy.FairsharePolicyProperty(
                    compute_reservation=123,
                    share_decay_seconds=123,
                    share_distribution=[batch.CfnSchedulingPolicy.ShareAttributesProperty(
                        share_identifier="shareIdentifier",
                        weight_factor=123
                    )]
                ),
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa72ee437297b58169f0020ba3178c321d8f72981fcd34857611be31a96093d)
            check_type(argname="argument fairshare_policy", value=fairshare_policy, expected_type=type_hints["fairshare_policy"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fairshare_policy is not None:
            self._values["fairshare_policy"] = fairshare_policy
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def fairshare_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchedulingPolicy.FairsharePolicyProperty]]:
        '''The fair share policy of the scheduling policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy
        '''
        result = self._values.get("fairshare_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchedulingPolicy.FairsharePolicyProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the scheduling policy.

        It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags that you apply to the scheduling policy to help you categorize and organize your resources.

        Each tag consists of a key and an optional value. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in *AWS General Reference* .

        These tags can be updated or removed using the `TagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html>`_ and `UntagResource <https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html>`_ API operations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchedulingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComputeEnvironment",
    "CfnComputeEnvironmentProps",
    "CfnJobDefinition",
    "CfnJobDefinitionProps",
    "CfnJobQueue",
    "CfnJobQueueProps",
    "CfnSchedulingPolicy",
    "CfnSchedulingPolicyProps",
]

publication.publish()

def _typecheckingstub__b3892141757a3fffc40366f3b0a3472c965c97710a96f3bb61a3618dd43af76e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    type: builtins.str,
    compute_environment_name: typing.Optional[builtins.str] = None,
    compute_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.ComputeResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    eks_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.EksConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    replace_compute_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    service_role: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    unmanagedv_cpus: typing.Optional[jsii.Number] = None,
    update_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.UpdatePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__181dea136575948e2334f9ffce96122ded2c4edc304f6835d519b8a40e411e4e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d72cf2605a93f743b750e273ccea4c1be6e5210af9e44b94c6722180f03040d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af58b33143bf1d8d98a3c10df145b0898751e739fa8cabe1763160d50bc3d730(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703e5e791be63f407384e398bda6c05261d86a114fb52955ac953213dc086558(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa0f8cbb024617b335ccf7af8884568ad91340203512578a8d682adfdfce5cd9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.ComputeResourcesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__896771848c9977e1ce30b550c3e02c1b1e7e047a645b3eb92c3d6d3bcf2ef1cf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.EksConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7a9dd96ed6e9e51373fc67bf7c1cfa4f89dea1d9ec4216da0ee3a471c21879(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682bb80f66d8c5016b985338436d49dc6155bd7a11dc1567d1a6478eddb9fc94(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30039c901207ae322b43ee9582a8efa812de586638692e722a62baa18097a10d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd461eb02586f268eaf0fc0a27581016dd596744fdebffc9a80af4b63a998bd3(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e874461559bd593606ec74eed9b2200a045433519c0ec8ec8d62a53f967da17a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39e9319d6ed789d3e7f527a145e7be0671311d4703680199b29ca8aef5635e60(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeEnvironment.UpdatePolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e554c6eb00e2d197fa806c35d70007a7590c1c363259e3e48971f0671e0e85f(
    *,
    maxv_cpus: jsii.Number,
    subnets: typing.Sequence[builtins.str],
    type: builtins.str,
    allocation_strategy: typing.Optional[builtins.str] = None,
    bid_percentage: typing.Optional[jsii.Number] = None,
    desiredv_cpus: typing.Optional[jsii.Number] = None,
    ec2_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.Ec2ConfigurationObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_key_pair: typing.Optional[builtins.str] = None,
    image_id: typing.Optional[builtins.str] = None,
    instance_role: typing.Optional[builtins.str] = None,
    instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.LaunchTemplateSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    minv_cpus: typing.Optional[jsii.Number] = None,
    placement_group: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    spot_iam_fleet_role: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    update_to_latest_image_version: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3b98c061a5de7793f276c675aa6c48c626a13d8debc8bf1a12f74113040fcb(
    *,
    image_type: builtins.str,
    image_id_override: typing.Optional[builtins.str] = None,
    image_kubernetes_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d01293eced89171b858aec2adc4c3362e7bc583fff04c8572350b492d38c641(
    *,
    eks_cluster_arn: builtins.str,
    kubernetes_namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a48b24f0297afff0df36a352af2f9856ad8fac713d1ecbc2161d0b968651da(
    *,
    launch_template_id: typing.Optional[builtins.str] = None,
    launch_template_name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f01f930e5e22d80ed490169089dfdbf2f416fdeb6b3ae57212518ae0b70b5e3(
    *,
    job_execution_timeout_minutes: typing.Optional[jsii.Number] = None,
    terminate_jobs_on_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a81ed1de03c840384ae49a0a4dbeb244507d2327c304fc093af8d720954eb257(
    *,
    type: builtins.str,
    compute_environment_name: typing.Optional[builtins.str] = None,
    compute_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.ComputeResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    eks_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.EksConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    replace_compute_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    service_role: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    unmanagedv_cpus: typing.Optional[jsii.Number] = None,
    update_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeEnvironment.UpdatePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37959c68856ab28ea1a57515db976bc2215806d52c75f6166834df6ae651417f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    type: builtins.str,
    container_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.ContainerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    eks_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EksPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_definition_name: typing.Optional[builtins.str] = None,
    node_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.NodePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parameters: typing.Any = None,
    platform_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    propagate_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retry_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.RetryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scheduling_priority: typing.Optional[jsii.Number] = None,
    tags: typing.Any = None,
    timeout: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.TimeoutProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84b6af858f7642dbc10029a34c2ed90c61a840b3c9d8a639fbe0690b4aa593d9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__710ae17567654ca123f279efb5ee033134bde1c49217d5abca4db2e98435f076(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96b92c09c064b55548b6669735edc8ffa8187ffae08746200ea2113f36cdcc6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69a394e899a3c712c6499f6fcffa98702eb3ab7de5e4489e6e69fb85ae55491(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.ContainerPropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca04be0ba694eb2f262cad48402ba7bf94953530d02c650e2679b1f91498c346(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.EksPropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f628b65bca30d37b13950af18cab324471321abe3a2e97c363552c0adbe924(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9d18dd3dda5e5761ec3a8f3c7af96598c179ac9f1bca0af0078b6aee12c880b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.NodePropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dfa67937c5c5c585d3dedec8653cb0633c802b99afaa23545e8fcc71bf4ef88(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df387fd03e7b9707eac2330bd1c2776f56a71ead17f60e9cc8606c21591b2cca(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__269e7fe24ddc93928c4ed8726528871fc789de7275942860c547acd761f99025(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac615dba37cd2b5a6e9d6f8cdd4b6beef51ff826d65fe0b5cdc31685de03def(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.RetryStrategyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba2bfccdff2acf2f90d4e7a4965d8dcb1ae572e2c9cbd92260bf928e42d7e01(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e523eed1bbd28b55b217e2df4a08d397d7fea1eab9961fca2a86f1f43fb0631f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa7b04ecd9d9f8e9c609d704cda9a2176a378049913a70b741c06702f6586c79(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobDefinition.TimeoutProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a944ff69de809bc564eb18b81b5fe5aaf841b525a61c70b907da2a96bd8d9b10(
    *,
    access_point_id: typing.Optional[builtins.str] = None,
    iam: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09b3c38642739790560033cae597f009c106d353ddc5faf85f6a7bf4891ac4d1(
    *,
    image: builtins.str,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ephemeral_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EphemeralStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    fargate_platform_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.FargatePlatformConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_type: typing.Optional[builtins.str] = None,
    job_role_arn: typing.Optional[builtins.str] = None,
    linux_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.LinuxParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    memory: typing.Optional[jsii.Number] = None,
    mount_points: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.MountPointsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    privileged: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    readonly_root_filesystem: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    resource_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.ResourceRequirementProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    runtime_platform: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.RuntimePlatformProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    secrets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.SecretProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ulimits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.UlimitProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    user: typing.Optional[builtins.str] = None,
    vcpus: typing.Optional[jsii.Number] = None,
    volumes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.VolumesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbf78805f7f3d50af2c331ead7e1f53e092ea7a76782151236bad4f3bfc77b0(
    *,
    container_path: typing.Optional[builtins.str] = None,
    host_path: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f673b085b46133477cd372799511104e89e28bf34ac0f6255020b20ef8b7e3e0(
    *,
    file_system_id: builtins.str,
    authorization_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.AuthorizationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    root_directory: typing.Optional[builtins.str] = None,
    transit_encryption: typing.Optional[builtins.str] = None,
    transit_encryption_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daaaeed078e13c29ac34da5a79bab4c04e8767edaf6d6a60877918a94797c218(
    *,
    name: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ece3a6d2417f8d913bdfc7bdf646d1de352c65903e333939133c3e81b1f4f3(
    *,
    image: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    env: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EksContainerEnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    image_pull_policy: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.ResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.SecurityContextProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    volume_mounts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EksContainerVolumeMountProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__855f1c6efd210a25d73922fc636cbbe8c4e08f7e49a5b9582f0ac1759eab5147(
    *,
    mount_path: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab4acc4a05a00897faf964911a9c5d642ebccbae43237575ad3b0b27ecb3ee74(
    *,
    pod_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.PodPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__285ba8b233801a3c8377d3b178bafde5c49a98f09f3e37c53c663ac43e11a41c(
    *,
    secret_name: builtins.str,
    optional: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71bf085e500a34c552f178e2df09efdf138a2c99fb19667f0b4cf9e398ca47eb(
    *,
    name: builtins.str,
    empty_dir: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EmptyDirProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    host_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.HostPathProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    secret: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EksSecretProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdef2f5e1ccd021a3913efc6e9f67cc3f3972961e97a491b8a739c8033fa20a3(
    *,
    medium: typing.Optional[builtins.str] = None,
    size_limit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1410eef4fad9b82401792bfb3c1c9342d946ef2f57199de602a1d63db8df8b41(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e501c23ca082963ca4e3f697be654dd2053f8a6f062fcd801a10d61dd916cf(
    *,
    size_in_gib: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662f88de3d4a2c44e67c0a3c3ee43319e3b3ee88c557f7669e584f52665e667e(
    *,
    action: builtins.str,
    on_exit_code: typing.Optional[builtins.str] = None,
    on_reason: typing.Optional[builtins.str] = None,
    on_status_reason: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b088f865053d4cfdc2700de70d732a768d630a892a20da6fda19303df04e9b4(
    *,
    platform_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf55e035d36507c507c0ff620eda0a3096496a2cd5226656fc5e4af46e1b9ac(
    *,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c01503a14b135de04e03e8a183177fbaa4f728ed5853b4de848d62c1f248ae(
    *,
    devices: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.DeviceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    init_process_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_swap: typing.Optional[jsii.Number] = None,
    shared_memory_size: typing.Optional[jsii.Number] = None,
    swappiness: typing.Optional[jsii.Number] = None,
    tmpfs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.TmpfsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e3055acf404e0b579b27c323b043bfb9f33e586341d48d4c5a17760f100e72(
    *,
    log_driver: builtins.str,
    options: typing.Any = None,
    secret_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.SecretProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a991ab55d6c85b732418b9a39402702cdf7043f946aaf69c13b36a4ccdd84cc(
    *,
    labels: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47aa253c2fbb1ab8f90425d412e691e807d1454f21b10bb59eee6c2b63cf29b5(
    *,
    container_path: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    source_volume: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681e5c00b804be1ae6d3076ea32a17483eee30db6c96e73768c520d652064300(
    *,
    assign_public_ip: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b765fef4e53f81f8c1a37eea0ea015533bd4621e0f00e5e86923931469f2fbd1(
    *,
    main_node: jsii.Number,
    node_range_properties: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.NodeRangePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]],
    num_nodes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__005c21025a81827c3f5ed456b171eb7ffdf652583c7da0ff6ff67186436afeee(
    *,
    target_nodes: builtins.str,
    container: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.ContainerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75127ae5a1697c34be5f24dcb69fa5c36a3498e1b2c284babc814c444bc47b1c(
    *,
    containers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EksContainerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    dns_policy: typing.Optional[builtins.str] = None,
    host_network: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.MetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_account_name: typing.Optional[builtins.str] = None,
    volumes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EksVolumeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7384d4b3b97f8aebbaa3dfe7ec74991276f6b53d6e1885662f675369f1d0166c(
    *,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__634ef7ff057388be2736fb45bfab10d038183951137f893e49e433ed83008f6a(
    *,
    limits: typing.Any = None,
    requests: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__800b22bca4d215e51bdb19588f0ed454bc972b986dd5a03f640fe8681acd52be(
    *,
    attempts: typing.Optional[jsii.Number] = None,
    evaluate_on_exit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EvaluateOnExitProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbdffb76b27dbbdbbc0d2ebc2229966bd04e50d9dbe061567a0dba94004d9e3e(
    *,
    cpu_architecture: typing.Optional[builtins.str] = None,
    operating_system_family: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627c25c89399f4c648455cf23b1833f2f5961be5393bea72498980b6dd1b8fac(
    *,
    name: builtins.str,
    value_from: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf4bfd8ece80e1bc3ee0536353fc145f3c5b08f62a604a53b62e7d2526f9d0e(
    *,
    privileged: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    run_as_group: typing.Optional[jsii.Number] = None,
    run_as_non_root: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    run_as_user: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b035a85f593ff8b58d3fbc57a8614a7bc0d733c70f8504eab630022b6186187(
    *,
    attempt_duration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c16bfb0295986db06cd649d9ca6994f1d86d2d884185ad1eda92e6da68041e0(
    *,
    container_path: builtins.str,
    size: jsii.Number,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9422053e6f2d5b223ad6edca9c1d424075ea7f34d3f55f01ed34ea8f4b51e8d4(
    *,
    hard_limit: jsii.Number,
    name: builtins.str,
    soft_limit: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af85cd0eadb4e77501a8751a1c3fc18ec19311f49db5d0f921588460010456a(
    *,
    source_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4a9d90db8477ca586c3c89fb2ce5a548e9a3bb699ae625a80a8a105b02a362e(
    *,
    efs_volume_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EfsVolumeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    host: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.VolumesHostProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed150d027b29486332c3fd2205a51f3c6f64c25946114fb86a6eba38434e87c9(
    *,
    type: builtins.str,
    container_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.ContainerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    eks_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.EksPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_definition_name: typing.Optional[builtins.str] = None,
    node_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.NodePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parameters: typing.Any = None,
    platform_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    propagate_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retry_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.RetryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scheduling_priority: typing.Optional[jsii.Number] = None,
    tags: typing.Any = None,
    timeout: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobDefinition.TimeoutProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6480ab252bc515b2cdb6dc0c833877438fd473fd39eadf6b8a064969a5fc051d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    compute_environment_order: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobQueue.ComputeEnvironmentOrderProperty, typing.Dict[builtins.str, typing.Any]]]]],
    priority: jsii.Number,
    job_queue_name: typing.Optional[builtins.str] = None,
    scheduling_policy_arn: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0501823e805eabb76b2d16d277e0e42dcf4e0873c3adb0898fab52f723baa571(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1fe922d9589f26998c2113a8a19530d98bfc01fe2462a8639a3593512e2368(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa1c2f3f42165309672c3fdf8c286ff9dc5e99756ec1a5b3ffca9e719d4c7036(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnJobQueue.ComputeEnvironmentOrderProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__620331f74c116d31a6d43627e1a45e7041bc3c110194265f30dc193863c8ed94(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b88e27e62b46f1049263a61bb14f62674a8121083de64c2db32d585651e1c30(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48a6952b4a8d4426554895a52085bf8c88701735f3f94a3426e81e56ab8a5761(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e97106b05367d04f8f618f0b8edf4f7fdc4b88436890062ac6e344ede4e180b0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e658491e12e1806302783cf972183ab89bf0d8d1d3abe7164fad544d18b91367(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939623842116ecc366f7e36591fb2bdd35bd47aacc55c0a794ff81ec2a026c43(
    *,
    compute_environment: builtins.str,
    order: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009d6d384b1b723169e64875095e05fe852ae3931adf5ba2004d22475a76caa9(
    *,
    compute_environment_order: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobQueue.ComputeEnvironmentOrderProperty, typing.Dict[builtins.str, typing.Any]]]]],
    priority: jsii.Number,
    job_queue_name: typing.Optional[builtins.str] = None,
    scheduling_policy_arn: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a21a4a6536b3efab619619ed719e6b0662b5c83fe7a1dc489b27f0b3ea56db(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    fairshare_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedulingPolicy.FairsharePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df36e53e7605cc7837477592dff920fd2c974ea55bea2f8469f2e732ec9524ca(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aefdc709a6b9ffad7303fb907694b285dd6ed2a9795b2c93a5ab983d1fc0ab2e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc1fdc7b365c326e80f94bc6ce2c1ba05c54c3d0dc4caaecec7e9eb7ec315b3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchedulingPolicy.FairsharePolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__411bf4b677626f26ae0d797bd4706cc6d8b5dbd45471422cf971b438d0f43ee0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f828d01fc7085728330a84e961df84cb35664d5a94e9bbf3bcfe93f7b3c7d5(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d584604e0200cce08bb1571b600a67b89e1eafdfce088d1cbe150d7b12935adc(
    *,
    compute_reservation: typing.Optional[jsii.Number] = None,
    share_decay_seconds: typing.Optional[jsii.Number] = None,
    share_distribution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedulingPolicy.ShareAttributesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a48599c650ce1ded6e5309cc09389c78237f12aa2328bbfe0d3335052f05da70(
    *,
    share_identifier: typing.Optional[builtins.str] = None,
    weight_factor: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa72ee437297b58169f0020ba3178c321d8f72981fcd34857611be31a96093d(
    *,
    fairshare_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedulingPolicy.FairsharePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
