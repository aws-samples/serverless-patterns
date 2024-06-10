'''
# AWS::ResilienceHub Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_resiliencehub as resiliencehub
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ResilienceHub construct libraries](https://constructs.dev/search?q=resiliencehub)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ResilienceHub resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResilienceHub.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ResilienceHub](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResilienceHub.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnApp(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_resiliencehub.CfnApp",
):
    '''Creates an AWS Resilience Hub application.

    An AWS Resilience Hub application is a collection of AWS resources structured to prevent and recover AWS application disruptions. To describe a AWS Resilience Hub application, you provide an application name, resources from one or more AWS CloudFormation stacks, AWS Resource Groups , Terraform state files, AppRegistry applications, and an appropriate resiliency policy. In addition, you can also add resources that are located on Amazon Elastic Kubernetes Service (Amazon EKS) clusters as optional resources. For more information about the number of resources supported per application, see `Service quotas <https://docs.aws.amazon.com/general/latest/gr/resiliencehub.html#limits_resiliencehub>`_ .

    After you create an AWS Resilience Hub application, you publish it so that you can run a resiliency assessment on it. You can then use recommendations from the assessment to improve resiliency by running another assessment, comparing results, and then iterating the process until you achieve your goals for recovery time objective (RTO) and recovery point objective (RPO).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html
    :cloudformationResource: AWS::ResilienceHub::App
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_resiliencehub as resiliencehub
        
        cfn_app = resiliencehub.CfnApp(self, "MyCfnApp",
            app_template_body="appTemplateBody",
            name="name",
            resource_mappings=[resiliencehub.CfnApp.ResourceMappingProperty(
                mapping_type="mappingType",
                physical_resource_id=resiliencehub.CfnApp.PhysicalResourceIdProperty(
                    identifier="identifier",
                    type="type",
        
                    # the properties below are optional
                    aws_account_id="awsAccountId",
                    aws_region="awsRegion"
                ),
        
                # the properties below are optional
                eks_source_name="eksSourceName",
                logical_stack_name="logicalStackName",
                resource_name="resourceName",
                terraform_source_name="terraformSourceName"
            )],
        
            # the properties below are optional
            app_assessment_schedule="appAssessmentSchedule",
            description="description",
            event_subscriptions=[resiliencehub.CfnApp.EventSubscriptionProperty(
                event_type="eventType",
                name="name",
        
                # the properties below are optional
                sns_topic_arn="snsTopicArn"
            )],
            permission_model=resiliencehub.CfnApp.PermissionModelProperty(
                type="type",
        
                # the properties below are optional
                cross_account_role_arns=["crossAccountRoleArns"],
                invoker_role_name="invokerRoleName"
            ),
            resiliency_policy_arn="resiliencyPolicyArn",
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
        app_template_body: builtins.str,
        name: builtins.str,
        resource_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.ResourceMappingProperty", typing.Dict[builtins.str, typing.Any]]]]],
        app_assessment_schedule: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        event_subscriptions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.EventSubscriptionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        permission_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.PermissionModelProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        resiliency_policy_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_template_body: A JSON string that provides information about your application structure. To learn more about the ``appTemplateBody`` template, see the sample template in `Sample appTemplateBody template <https://docs.aws.amazon.com//resilience-hub/latest/APIReference/API_PutDraftAppVersionTemplate.html#API_PutDraftAppVersionTemplate_Examples>`_ . The ``appTemplateBody`` JSON string has the following structure: - *``resources``* The list of logical resources that needs to be included in the AWS Resilience Hub application. Type: Array .. epigraph:: Don't add the resources that you want to exclude. Each ``resources`` array item includes the following fields: - *``logicalResourceId``* The logical identifier of the resource. Type: Object Each ``logicalResourceId`` object includes the following fields: - ``identifier`` Identifier of the resource. Type: String - ``logicalStackName`` Name of the AWS CloudFormation stack this resource belongs to. Type: String - ``resourceGroupName`` Name of the resource group this resource belongs to. Type: String - ``terraformSourceName`` Name of the Terraform S3 state file this resource belongs to. Type: String - ``eksSourceName`` Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to. .. epigraph:: This parameter accepts values in "eks-cluster/namespace" format. Type: String - *``type``* The type of resource. Type: string - *``name``* Name of the resource. Type: String - ``additionalInfo`` Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ . .. epigraph:: Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: ``"failover-regions"`` Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`` - *``appComponents``* The list of Application Components (AppComponent) that this resource belongs to. If an AppComponent is not part of the AWS Resilience Hub application, it will be added. Type: Array Each ``appComponents`` array item includes the following fields: - ``name`` Name of the AppComponent. Type: String - ``type`` The type of AppComponent. For more information about the types of AppComponent, see `Grouping resources in an AppComponent <https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html>`_ . Type: String - ``resourceNames`` The list of included resources that are assigned to the AppComponent. Type: Array of strings - ``additionalInfo`` Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ . .. epigraph:: Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: ``"failover-regions"`` Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`` - *``excludedResources``* The list of logical resource identifiers to be excluded from the application. Type: Array .. epigraph:: Don't add the resources that you want to include. Each ``excludedResources`` array item includes the following fields: - *``logicalResourceIds``* The logical identifier of the resource. Type: Object .. epigraph:: You can configure only one of the following fields: - ``logicalStackName`` - ``resourceGroupName`` - ``terraformSourceName`` - ``eksSourceName`` Each ``logicalResourceIds`` object includes the following fields: - ``identifier`` The identifier of the resource. Type: String - ``logicalStackName`` Name of the AWS CloudFormation stack this resource belongs to. Type: String - ``resourceGroupName`` Name of the resource group this resource belongs to. Type: String - ``terraformSourceName`` Name of the Terraform S3 state file this resource belongs to. Type: String - ``eksSourceName`` Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to. .. epigraph:: This parameter accepts values in "eks-cluster/namespace" format. Type: String - *``version``* The AWS Resilience Hub application version. - ``additionalInfo`` Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ . .. epigraph:: Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: ``"failover-regions"`` Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"``
        :param name: Name for the application.
        :param resource_mappings: An array of ``ResourceMapping`` objects.
        :param app_assessment_schedule: Assessment execution schedule with 'Daily' or 'Disabled' values.
        :param description: Optional description for an application.
        :param event_subscriptions: The list of events you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for *Drift detected* and *Scheduled assessment failure* events.
        :param permission_model: Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.
        :param resiliency_policy_arn: The Amazon Resource Name (ARN) of the resiliency policy.
        :param tags: Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__303e76fc3650422653be00dea7484c071f68688b86b0b136d647cee7306c7958)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppProps(
            app_template_body=app_template_body,
            name=name,
            resource_mappings=resource_mappings,
            app_assessment_schedule=app_assessment_schedule,
            description=description,
            event_subscriptions=event_subscriptions,
            permission_model=permission_model,
            resiliency_policy_arn=resiliency_policy_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59fba2f0cf5aadd1fd75ba32c9b4bfb1c0d6e43acd0002173024ce9e85ed285e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__39b1746c5aaa0b06207855cbb349cb99ee17a1df8cdfc71812db83d0b9680219)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAppArn")
    def attr_app_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the applcation.

        :cloudformationAttribute: AppArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDriftStatus")
    def attr_drift_status(self) -> builtins.str:
        '''Indicates if compliance drifts (deviations) were detected while running an assessment for your application.

        :cloudformationAttribute: DriftStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDriftStatus"))

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
    @jsii.member(jsii_name="appTemplateBody")
    def app_template_body(self) -> builtins.str:
        '''A JSON string that provides information about your application structure.'''
        return typing.cast(builtins.str, jsii.get(self, "appTemplateBody"))

    @app_template_body.setter
    def app_template_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c2df1cafeabd95579e76b6448abd4bc8191ed805fa79934e5a2ba2863d8a4a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appTemplateBody", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name for the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ec5f12ec50861e776ad80e27c62359d36bca636f0adbf44ed2618963e02c64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceMappings")
    def resource_mappings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.ResourceMappingProperty"]]]:
        '''An array of ``ResourceMapping`` objects.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.ResourceMappingProperty"]]], jsii.get(self, "resourceMappings"))

    @resource_mappings.setter
    def resource_mappings(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.ResourceMappingProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7be56e25078fc8e2aedbbef7b1762fc9e3fdb0096405151631ffaeb94832cc34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceMappings", value)

    @builtins.property
    @jsii.member(jsii_name="appAssessmentSchedule")
    def app_assessment_schedule(self) -> typing.Optional[builtins.str]:
        '''Assessment execution schedule with 'Daily' or 'Disabled' values.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appAssessmentSchedule"))

    @app_assessment_schedule.setter
    def app_assessment_schedule(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1219dae6dd0d44c29343fb98a2d5c76c2a24c08981364a9635db5d542b60665d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appAssessmentSchedule", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional description for an application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef5b0a7209d4ed93ddc4b9b03b30dfaf9f4e659b9ac9551bd3e4332a348c0c36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="eventSubscriptions")
    def event_subscriptions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EventSubscriptionProperty"]]]]:
        '''The list of events you would like to subscribe and get notification for.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EventSubscriptionProperty"]]]], jsii.get(self, "eventSubscriptions"))

    @event_subscriptions.setter
    def event_subscriptions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EventSubscriptionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d302607b7a1dfbffee8d2ab82e294e1d08c27584331ec9bea2e75add9db5b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSubscriptions", value)

    @builtins.property
    @jsii.member(jsii_name="permissionModel")
    def permission_model(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.PermissionModelProperty"]]:
        '''Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.PermissionModelProperty"]], jsii.get(self, "permissionModel"))

    @permission_model.setter
    def permission_model(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.PermissionModelProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e15df41e400e8a9cff1ec67cfe4cdb6224b7e0faa1f84a7164a3aff0b0462f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionModel", value)

    @builtins.property
    @jsii.member(jsii_name="resiliencyPolicyArn")
    def resiliency_policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resiliency policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resiliencyPolicyArn"))

    @resiliency_policy_arn.setter
    def resiliency_policy_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce4ee431bd44e41d23a7b0df5a1d235166dfde2dcb98cb013d61da840d20b025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resiliencyPolicyArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags assigned to the resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d13896f18fa79328cd19410a666196ad5f076947628b86a3d2d74479248cc5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resiliencehub.CfnApp.EventSubscriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_type": "eventType",
            "name": "name",
            "sns_topic_arn": "snsTopicArn",
        },
    )
    class EventSubscriptionProperty:
        def __init__(
            self,
            *,
            event_type: builtins.str,
            name: builtins.str,
            sns_topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Indicates an event you would like to subscribe and get notification for.

            Currently, AWS Resilience Hub supports notifications only for *Drift detected* and *Scheduled assessment failure* events.

            :param event_type: The type of event you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for *Drift detected* ( ``DriftDetected`` ) and *Scheduled assessment failure* ( ``ScheduledAssessmentFailure`` ) events.
            :param name: Unique name to identify an event subscription.
            :param sns_topic_arn: Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic. The format for this ARN is: ``arn:partition:sns:region:account:topic-name`` . For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resiliencehub as resiliencehub
                
                event_subscription_property = resiliencehub.CfnApp.EventSubscriptionProperty(
                    event_type="eventType",
                    name="name",
                
                    # the properties below are optional
                    sns_topic_arn="snsTopicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24e5de7bc5abc5f46b1e0bcc9b765adaa418f9f436edcfd31c40a13a5740d617)
                check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_type": event_type,
                "name": name,
            }
            if sns_topic_arn is not None:
                self._values["sns_topic_arn"] = sns_topic_arn

        @builtins.property
        def event_type(self) -> builtins.str:
            '''The type of event you would like to subscribe and get notification for.

            Currently, AWS Resilience Hub supports notifications only for *Drift detected* ( ``DriftDetected`` ) and *Scheduled assessment failure* ( ``ScheduledAssessmentFailure`` ) events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html#cfn-resiliencehub-app-eventsubscription-eventtype
            '''
            result = self._values.get("event_type")
            assert result is not None, "Required property 'event_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''Unique name to identify an event subscription.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html#cfn-resiliencehub-app-eventsubscription-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sns_topic_arn(self) -> typing.Optional[builtins.str]:
            '''Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic.

            The format for this ARN is: ``arn:partition:sns:region:account:topic-name`` . For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html#cfn-resiliencehub-app-eventsubscription-snstopicarn
            '''
            result = self._values.get("sns_topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSubscriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resiliencehub.CfnApp.PermissionModelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "cross_account_role_arns": "crossAccountRoleArns",
            "invoker_role_name": "invokerRoleName",
        },
    )
    class PermissionModelProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            cross_account_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            invoker_role_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.

            :param type: Defines how AWS Resilience Hub scans your resources. It can scan for the resources by using a pre-existing role in your AWS account, or by using the credentials of the current IAM user.
            :param cross_account_role_arns: Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts. These ARNs are used for querying purposes while importing resources and assessing your application. .. epigraph:: - These ARNs are required only when your resources are in other accounts and you have different role name in these accounts. Else, the invoker role name will be used in the other accounts. - These roles must have a trust policy with ``iam:AssumeRole`` permission to the invoker role in the primary account.
            :param invoker_role_name: Existing AWS IAM role name in the primary AWS account that will be assumed by AWS Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment. .. epigraph:: - You must have ``iam:passRole`` permission for this role while creating or updating the application. - Currently, ``invokerRoleName`` accepts only ``[A-Za-z0-9_+=,.@-]`` characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resiliencehub as resiliencehub
                
                permission_model_property = resiliencehub.CfnApp.PermissionModelProperty(
                    type="type",
                
                    # the properties below are optional
                    cross_account_role_arns=["crossAccountRoleArns"],
                    invoker_role_name="invokerRoleName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a8107f5f0a79085bc51c1ccd12ec056fa14fa89fbad641ef5065c416f4ae281)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument cross_account_role_arns", value=cross_account_role_arns, expected_type=type_hints["cross_account_role_arns"])
                check_type(argname="argument invoker_role_name", value=invoker_role_name, expected_type=type_hints["invoker_role_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if cross_account_role_arns is not None:
                self._values["cross_account_role_arns"] = cross_account_role_arns
            if invoker_role_name is not None:
                self._values["invoker_role_name"] = invoker_role_name

        @builtins.property
        def type(self) -> builtins.str:
            '''Defines how AWS Resilience Hub scans your resources.

            It can scan for the resources by using a pre-existing role in your AWS account, or by using the credentials of the current IAM user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html#cfn-resiliencehub-app-permissionmodel-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cross_account_role_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts.

            These ARNs are used for querying purposes while importing resources and assessing your application.
            .. epigraph::

               - These ARNs are required only when your resources are in other accounts and you have different role name in these accounts. Else, the invoker role name will be used in the other accounts.
               - These roles must have a trust policy with ``iam:AssumeRole`` permission to the invoker role in the primary account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html#cfn-resiliencehub-app-permissionmodel-crossaccountrolearns
            '''
            result = self._values.get("cross_account_role_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def invoker_role_name(self) -> typing.Optional[builtins.str]:
            '''Existing AWS IAM role name in the primary AWS account that will be assumed by AWS Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment.

            .. epigraph::

               - You must have ``iam:passRole`` permission for this role while creating or updating the application.
               - Currently, ``invokerRoleName`` accepts only ``[A-Za-z0-9_+=,.@-]`` characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html#cfn-resiliencehub-app-permissionmodel-invokerrolename
            '''
            result = self._values.get("invoker_role_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PermissionModelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resiliencehub.CfnApp.PhysicalResourceIdProperty",
        jsii_struct_bases=[],
        name_mapping={
            "identifier": "identifier",
            "type": "type",
            "aws_account_id": "awsAccountId",
            "aws_region": "awsRegion",
        },
    )
    class PhysicalResourceIdProperty:
        def __init__(
            self,
            *,
            identifier: builtins.str,
            type: builtins.str,
            aws_account_id: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a physical resource identifier.

            :param identifier: Identifier of the physical resource.
            :param type: Specifies the type of physical resource identifier. - **Arn** - The resource identifier is an Amazon Resource Name (ARN) and it can identify the following list of resources: - ``AWS::ECS::Service`` - ``AWS::EFS::FileSystem`` - ``AWS::ElasticLoadBalancingV2::LoadBalancer`` - ``AWS::Lambda::Function`` - ``AWS::SNS::Topic`` - **Native** - The resource identifier is an AWS Resilience Hub -native identifier and it can identify the following list of resources: - ``AWS::ApiGateway::RestApi`` - ``AWS::ApiGatewayV2::Api`` - ``AWS::AutoScaling::AutoScalingGroup`` - ``AWS::DocDB::DBCluster`` - ``AWS::DocDB::DBGlobalCluster`` - ``AWS::DocDB::DBInstance`` - ``AWS::DynamoDB::GlobalTable`` - ``AWS::DynamoDB::Table`` - ``AWS::EC2::EC2Fleet`` - ``AWS::EC2::Instance`` - ``AWS::EC2::NatGateway`` - ``AWS::EC2::Volume`` - ``AWS::ElasticLoadBalancing::LoadBalancer`` - ``AWS::RDS::DBCluster`` - ``AWS::RDS::DBInstance`` - ``AWS::RDS::GlobalCluster`` - ``AWS::Route53::RecordSet`` - ``AWS::S3::Bucket`` - ``AWS::SQS::Queue``
            :param aws_account_id: The AWS account that owns the physical resource.
            :param aws_region: The AWS Region that the physical resource is located in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resiliencehub as resiliencehub
                
                physical_resource_id_property = resiliencehub.CfnApp.PhysicalResourceIdProperty(
                    identifier="identifier",
                    type="type",
                
                    # the properties below are optional
                    aws_account_id="awsAccountId",
                    aws_region="awsRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3eacd68e84c228cdd21e0474784bb6561272f2528af8dda91c1eb8fc45207812)
                check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "identifier": identifier,
                "type": type,
            }
            if aws_account_id is not None:
                self._values["aws_account_id"] = aws_account_id
            if aws_region is not None:
                self._values["aws_region"] = aws_region

        @builtins.property
        def identifier(self) -> builtins.str:
            '''Identifier of the physical resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-identifier
            '''
            result = self._values.get("identifier")
            assert result is not None, "Required property 'identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''Specifies the type of physical resource identifier.

            - **Arn** - The resource identifier is an Amazon Resource Name (ARN) and it can identify the following list of resources:
            - ``AWS::ECS::Service``
            - ``AWS::EFS::FileSystem``
            - ``AWS::ElasticLoadBalancingV2::LoadBalancer``
            - ``AWS::Lambda::Function``
            - ``AWS::SNS::Topic``
            - **Native** - The resource identifier is an AWS Resilience Hub -native identifier and it can identify the following list of resources:
            - ``AWS::ApiGateway::RestApi``
            - ``AWS::ApiGatewayV2::Api``
            - ``AWS::AutoScaling::AutoScalingGroup``
            - ``AWS::DocDB::DBCluster``
            - ``AWS::DocDB::DBGlobalCluster``
            - ``AWS::DocDB::DBInstance``
            - ``AWS::DynamoDB::GlobalTable``
            - ``AWS::DynamoDB::Table``
            - ``AWS::EC2::EC2Fleet``
            - ``AWS::EC2::Instance``
            - ``AWS::EC2::NatGateway``
            - ``AWS::EC2::Volume``
            - ``AWS::ElasticLoadBalancing::LoadBalancer``
            - ``AWS::RDS::DBCluster``
            - ``AWS::RDS::DBInstance``
            - ``AWS::RDS::GlobalCluster``
            - ``AWS::Route53::RecordSet``
            - ``AWS::S3::Bucket``
            - ``AWS::SQS::Queue``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_account_id(self) -> typing.Optional[builtins.str]:
            '''The AWS account that owns the physical resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-awsaccountid
            '''
            result = self._values.get("aws_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the physical resource is located in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhysicalResourceIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resiliencehub.CfnApp.ResourceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mapping_type": "mappingType",
            "physical_resource_id": "physicalResourceId",
            "eks_source_name": "eksSourceName",
            "logical_stack_name": "logicalStackName",
            "resource_name": "resourceName",
            "terraform_source_name": "terraformSourceName",
        },
    )
    class ResourceMappingProperty:
        def __init__(
            self,
            *,
            mapping_type: builtins.str,
            physical_resource_id: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.PhysicalResourceIdProperty", typing.Dict[builtins.str, typing.Any]]],
            eks_source_name: typing.Optional[builtins.str] = None,
            logical_stack_name: typing.Optional[builtins.str] = None,
            resource_name: typing.Optional[builtins.str] = None,
            terraform_source_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a resource mapping.

            :param mapping_type: Specifies the type of resource mapping.
            :param physical_resource_id: Identifier of the physical resource.
            :param eks_source_name: Name of the Amazon Elastic Kubernetes Service cluster and namespace that this resource is mapped to when the ``mappingType`` is ``EKS`` . .. epigraph:: This parameter accepts values in "eks-cluster/namespace" format.
            :param logical_stack_name: Name of the AWS CloudFormation stack this resource is mapped to when the ``mappingType`` is ``CfnStack`` .
            :param resource_name: Name of the resource that this resource is mapped to when the ``mappingType`` is ``Resource`` .
            :param terraform_source_name: Name of the Terraform source that this resource is mapped to when the ``mappingType`` is ``Terraform`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resiliencehub as resiliencehub
                
                resource_mapping_property = resiliencehub.CfnApp.ResourceMappingProperty(
                    mapping_type="mappingType",
                    physical_resource_id=resiliencehub.CfnApp.PhysicalResourceIdProperty(
                        identifier="identifier",
                        type="type",
                
                        # the properties below are optional
                        aws_account_id="awsAccountId",
                        aws_region="awsRegion"
                    ),
                
                    # the properties below are optional
                    eks_source_name="eksSourceName",
                    logical_stack_name="logicalStackName",
                    resource_name="resourceName",
                    terraform_source_name="terraformSourceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__73ce15c2c4786e2990c8cd30f8becbb71d99cd69d3c1b4c44211c8e6baaf1027)
                check_type(argname="argument mapping_type", value=mapping_type, expected_type=type_hints["mapping_type"])
                check_type(argname="argument physical_resource_id", value=physical_resource_id, expected_type=type_hints["physical_resource_id"])
                check_type(argname="argument eks_source_name", value=eks_source_name, expected_type=type_hints["eks_source_name"])
                check_type(argname="argument logical_stack_name", value=logical_stack_name, expected_type=type_hints["logical_stack_name"])
                check_type(argname="argument resource_name", value=resource_name, expected_type=type_hints["resource_name"])
                check_type(argname="argument terraform_source_name", value=terraform_source_name, expected_type=type_hints["terraform_source_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mapping_type": mapping_type,
                "physical_resource_id": physical_resource_id,
            }
            if eks_source_name is not None:
                self._values["eks_source_name"] = eks_source_name
            if logical_stack_name is not None:
                self._values["logical_stack_name"] = logical_stack_name
            if resource_name is not None:
                self._values["resource_name"] = resource_name
            if terraform_source_name is not None:
                self._values["terraform_source_name"] = terraform_source_name

        @builtins.property
        def mapping_type(self) -> builtins.str:
            '''Specifies the type of resource mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-mappingtype
            '''
            result = self._values.get("mapping_type")
            assert result is not None, "Required property 'mapping_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def physical_resource_id(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnApp.PhysicalResourceIdProperty"]:
            '''Identifier of the physical resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-physicalresourceid
            '''
            result = self._values.get("physical_resource_id")
            assert result is not None, "Required property 'physical_resource_id' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApp.PhysicalResourceIdProperty"], result)

        @builtins.property
        def eks_source_name(self) -> typing.Optional[builtins.str]:
            '''Name of the Amazon Elastic Kubernetes Service cluster and namespace that this resource is mapped to when the ``mappingType`` is ``EKS`` .

            .. epigraph::

               This parameter accepts values in "eks-cluster/namespace" format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-ekssourcename
            '''
            result = self._values.get("eks_source_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def logical_stack_name(self) -> typing.Optional[builtins.str]:
            '''Name of the AWS CloudFormation stack this resource is mapped to when the ``mappingType`` is ``CfnStack`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-logicalstackname
            '''
            result = self._values.get("logical_stack_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_name(self) -> typing.Optional[builtins.str]:
            '''Name of the resource that this resource is mapped to when the ``mappingType`` is ``Resource`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-resourcename
            '''
            result = self._values.get("resource_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def terraform_source_name(self) -> typing.Optional[builtins.str]:
            '''Name of the Terraform source that this resource is mapped to when the ``mappingType`` is ``Terraform`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-terraformsourcename
            '''
            result = self._values.get("terraform_source_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_resiliencehub.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_template_body": "appTemplateBody",
        "name": "name",
        "resource_mappings": "resourceMappings",
        "app_assessment_schedule": "appAssessmentSchedule",
        "description": "description",
        "event_subscriptions": "eventSubscriptions",
        "permission_model": "permissionModel",
        "resiliency_policy_arn": "resiliencyPolicyArn",
        "tags": "tags",
    },
)
class CfnAppProps:
    def __init__(
        self,
        *,
        app_template_body: builtins.str,
        name: builtins.str,
        resource_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.ResourceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]],
        app_assessment_schedule: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        event_subscriptions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EventSubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        permission_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.PermissionModelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        resiliency_policy_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApp``.

        :param app_template_body: A JSON string that provides information about your application structure. To learn more about the ``appTemplateBody`` template, see the sample template in `Sample appTemplateBody template <https://docs.aws.amazon.com//resilience-hub/latest/APIReference/API_PutDraftAppVersionTemplate.html#API_PutDraftAppVersionTemplate_Examples>`_ . The ``appTemplateBody`` JSON string has the following structure: - *``resources``* The list of logical resources that needs to be included in the AWS Resilience Hub application. Type: Array .. epigraph:: Don't add the resources that you want to exclude. Each ``resources`` array item includes the following fields: - *``logicalResourceId``* The logical identifier of the resource. Type: Object Each ``logicalResourceId`` object includes the following fields: - ``identifier`` Identifier of the resource. Type: String - ``logicalStackName`` Name of the AWS CloudFormation stack this resource belongs to. Type: String - ``resourceGroupName`` Name of the resource group this resource belongs to. Type: String - ``terraformSourceName`` Name of the Terraform S3 state file this resource belongs to. Type: String - ``eksSourceName`` Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to. .. epigraph:: This parameter accepts values in "eks-cluster/namespace" format. Type: String - *``type``* The type of resource. Type: string - *``name``* Name of the resource. Type: String - ``additionalInfo`` Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ . .. epigraph:: Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: ``"failover-regions"`` Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`` - *``appComponents``* The list of Application Components (AppComponent) that this resource belongs to. If an AppComponent is not part of the AWS Resilience Hub application, it will be added. Type: Array Each ``appComponents`` array item includes the following fields: - ``name`` Name of the AppComponent. Type: String - ``type`` The type of AppComponent. For more information about the types of AppComponent, see `Grouping resources in an AppComponent <https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html>`_ . Type: String - ``resourceNames`` The list of included resources that are assigned to the AppComponent. Type: Array of strings - ``additionalInfo`` Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ . .. epigraph:: Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: ``"failover-regions"`` Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`` - *``excludedResources``* The list of logical resource identifiers to be excluded from the application. Type: Array .. epigraph:: Don't add the resources that you want to include. Each ``excludedResources`` array item includes the following fields: - *``logicalResourceIds``* The logical identifier of the resource. Type: Object .. epigraph:: You can configure only one of the following fields: - ``logicalStackName`` - ``resourceGroupName`` - ``terraformSourceName`` - ``eksSourceName`` Each ``logicalResourceIds`` object includes the following fields: - ``identifier`` The identifier of the resource. Type: String - ``logicalStackName`` Name of the AWS CloudFormation stack this resource belongs to. Type: String - ``resourceGroupName`` Name of the resource group this resource belongs to. Type: String - ``terraformSourceName`` Name of the Terraform S3 state file this resource belongs to. Type: String - ``eksSourceName`` Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to. .. epigraph:: This parameter accepts values in "eks-cluster/namespace" format. Type: String - *``version``* The AWS Resilience Hub application version. - ``additionalInfo`` Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ . .. epigraph:: Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: ``"failover-regions"`` Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"``
        :param name: Name for the application.
        :param resource_mappings: An array of ``ResourceMapping`` objects.
        :param app_assessment_schedule: Assessment execution schedule with 'Daily' or 'Disabled' values.
        :param description: Optional description for an application.
        :param event_subscriptions: The list of events you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for *Drift detected* and *Scheduled assessment failure* events.
        :param permission_model: Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.
        :param resiliency_policy_arn: The Amazon Resource Name (ARN) of the resiliency policy.
        :param tags: Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_resiliencehub as resiliencehub
            
            cfn_app_props = resiliencehub.CfnAppProps(
                app_template_body="appTemplateBody",
                name="name",
                resource_mappings=[resiliencehub.CfnApp.ResourceMappingProperty(
                    mapping_type="mappingType",
                    physical_resource_id=resiliencehub.CfnApp.PhysicalResourceIdProperty(
                        identifier="identifier",
                        type="type",
            
                        # the properties below are optional
                        aws_account_id="awsAccountId",
                        aws_region="awsRegion"
                    ),
            
                    # the properties below are optional
                    eks_source_name="eksSourceName",
                    logical_stack_name="logicalStackName",
                    resource_name="resourceName",
                    terraform_source_name="terraformSourceName"
                )],
            
                # the properties below are optional
                app_assessment_schedule="appAssessmentSchedule",
                description="description",
                event_subscriptions=[resiliencehub.CfnApp.EventSubscriptionProperty(
                    event_type="eventType",
                    name="name",
            
                    # the properties below are optional
                    sns_topic_arn="snsTopicArn"
                )],
                permission_model=resiliencehub.CfnApp.PermissionModelProperty(
                    type="type",
            
                    # the properties below are optional
                    cross_account_role_arns=["crossAccountRoleArns"],
                    invoker_role_name="invokerRoleName"
                ),
                resiliency_policy_arn="resiliencyPolicyArn",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4cbfaccc19fec8c2bd3f0ad17cdc9d5c9a66dbdcc7077312163442e737af125)
            check_type(argname="argument app_template_body", value=app_template_body, expected_type=type_hints["app_template_body"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_mappings", value=resource_mappings, expected_type=type_hints["resource_mappings"])
            check_type(argname="argument app_assessment_schedule", value=app_assessment_schedule, expected_type=type_hints["app_assessment_schedule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_subscriptions", value=event_subscriptions, expected_type=type_hints["event_subscriptions"])
            check_type(argname="argument permission_model", value=permission_model, expected_type=type_hints["permission_model"])
            check_type(argname="argument resiliency_policy_arn", value=resiliency_policy_arn, expected_type=type_hints["resiliency_policy_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_template_body": app_template_body,
            "name": name,
            "resource_mappings": resource_mappings,
        }
        if app_assessment_schedule is not None:
            self._values["app_assessment_schedule"] = app_assessment_schedule
        if description is not None:
            self._values["description"] = description
        if event_subscriptions is not None:
            self._values["event_subscriptions"] = event_subscriptions
        if permission_model is not None:
            self._values["permission_model"] = permission_model
        if resiliency_policy_arn is not None:
            self._values["resiliency_policy_arn"] = resiliency_policy_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_template_body(self) -> builtins.str:
        '''A JSON string that provides information about your application structure.

        To learn more about the ``appTemplateBody`` template, see the sample template in `Sample appTemplateBody template <https://docs.aws.amazon.com//resilience-hub/latest/APIReference/API_PutDraftAppVersionTemplate.html#API_PutDraftAppVersionTemplate_Examples>`_ .

        The ``appTemplateBody`` JSON string has the following structure:

        - *``resources``*

        The list of logical resources that needs to be included in the AWS Resilience Hub application.

        Type: Array
        .. epigraph::

           Don't add the resources that you want to exclude.

        Each ``resources`` array item includes the following fields:

        - *``logicalResourceId``*

        The logical identifier of the resource.

        Type: Object

        Each ``logicalResourceId`` object includes the following fields:

        - ``identifier``

        Identifier of the resource.

        Type: String

        - ``logicalStackName``

        Name of the AWS CloudFormation stack this resource belongs to.

        Type: String

        - ``resourceGroupName``

        Name of the resource group this resource belongs to.

        Type: String

        - ``terraformSourceName``

        Name of the Terraform S3 state file this resource belongs to.

        Type: String

        - ``eksSourceName``

        Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.
        .. epigraph::

           This parameter accepts values in "eks-cluster/namespace" format.

        Type: String

        - *``type``*

        The type of resource.

        Type: string

        - *``name``*

        Name of the resource.

        Type: String

        - ``additionalInfo``

        Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ .
        .. epigraph::

           Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.

           Key: ``"failover-regions"``

           Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"``

        - *``appComponents``*

        The list of Application Components (AppComponent) that this resource belongs to. If an AppComponent is not part of the AWS Resilience Hub application, it will be added.

        Type: Array

        Each ``appComponents`` array item includes the following fields:

        - ``name``

        Name of the AppComponent.

        Type: String

        - ``type``

        The type of AppComponent. For more information about the types of AppComponent, see `Grouping resources in an AppComponent <https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html>`_ .

        Type: String

        - ``resourceNames``

        The list of included resources that are assigned to the AppComponent.

        Type: Array of strings

        - ``additionalInfo``

        Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ .
        .. epigraph::

           Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.

           Key: ``"failover-regions"``

           Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"``

        - *``excludedResources``*

        The list of logical resource identifiers to be excluded from the application.

        Type: Array
        .. epigraph::

           Don't add the resources that you want to include.

        Each ``excludedResources`` array item includes the following fields:

        - *``logicalResourceIds``*

        The logical identifier of the resource.

        Type: Object
        .. epigraph::

           You can configure only one of the following fields:

           - ``logicalStackName``
           - ``resourceGroupName``
           - ``terraformSourceName``
           - ``eksSourceName``

        Each ``logicalResourceIds`` object includes the following fields:

        - ``identifier``

        The identifier of the resource.

        Type: String

        - ``logicalStackName``

        Name of the AWS CloudFormation stack this resource belongs to.

        Type: String

        - ``resourceGroupName``

        Name of the resource group this resource belongs to.

        Type: String

        - ``terraformSourceName``

        Name of the Terraform S3 state file this resource belongs to.

        Type: String

        - ``eksSourceName``

        Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.
        .. epigraph::

           This parameter accepts values in "eks-cluster/namespace" format.

        Type: String

        - *``version``*

        The AWS Resilience Hub application version.

        - ``additionalInfo``

        Additional configuration parameters for an AWS Resilience Hub application. If you want to implement ``additionalInfo`` through the AWS Resilience Hub console rather than using an API call, see `Configure the application configuration parameters <https://docs.aws.amazon.com//resilience-hub/latest/userguide/app-config-param.html>`_ .
        .. epigraph::

           Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.

           Key: ``"failover-regions"``

           Value: ``"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-apptemplatebody
        '''
        result = self._values.get("app_template_body")
        assert result is not None, "Required property 'app_template_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_mappings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.ResourceMappingProperty]]]:
        '''An array of ``ResourceMapping`` objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-resourcemappings
        '''
        result = self._values.get("resource_mappings")
        assert result is not None, "Required property 'resource_mappings' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.ResourceMappingProperty]]], result)

    @builtins.property
    def app_assessment_schedule(self) -> typing.Optional[builtins.str]:
        '''Assessment execution schedule with 'Daily' or 'Disabled' values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-appassessmentschedule
        '''
        result = self._values.get("app_assessment_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional description for an application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_subscriptions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EventSubscriptionProperty]]]]:
        '''The list of events you would like to subscribe and get notification for.

        Currently, AWS Resilience Hub supports notifications only for *Drift detected* and *Scheduled assessment failure* events.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-eventsubscriptions
        '''
        result = self._values.get("event_subscriptions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EventSubscriptionProperty]]]], result)

    @builtins.property
    def permission_model(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.PermissionModelProperty]]:
        '''Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-permissionmodel
        '''
        result = self._values.get("permission_model")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.PermissionModelProperty]], result)

    @builtins.property
    def resiliency_policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resiliency policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-resiliencypolicyarn
        '''
        result = self._values.get("resiliency_policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags assigned to the resource.

        A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnResiliencyPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_resiliencehub.CfnResiliencyPolicy",
):
    '''Defines a resiliency policy.

    .. epigraph::

       AWS Resilience Hub allows you to provide a value of zero for ``rtoInSecs`` and ``rpoInSecs`` of your resiliency policy. But, while assessing your application, the lowest possible assessment result is near zero. Hence, if you provide value zero for ``rtoInSecs`` and ``rpoInSecs`` , the estimated workload RTO and estimated workload RPO result will be near zero and the *Compliance status* for your application will be set to *Policy breached* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html
    :cloudformationResource: AWS::ResilienceHub::ResiliencyPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_resiliencehub as resiliencehub
        
        cfn_resiliency_policy = resiliencehub.CfnResiliencyPolicy(self, "MyCfnResiliencyPolicy",
            policy={
                "policy_key": resiliencehub.CfnResiliencyPolicy.FailurePolicyProperty(
                    rpo_in_secs=123,
                    rto_in_secs=123
                )
            },
            policy_name="policyName",
            tier="tier",
        
            # the properties below are optional
            data_location_constraint="dataLocationConstraint",
            policy_description="policyDescription",
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
        policy: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnResiliencyPolicy.FailurePolicyProperty", typing.Dict[builtins.str, typing.Any]]]]],
        policy_name: builtins.str,
        tier: builtins.str,
        data_location_constraint: typing.Optional[builtins.str] = None,
        policy_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy: The resiliency policy.
        :param policy_name: The name of the policy.
        :param tier: The tier for this resiliency policy, ranging from the highest severity ( ``MissionCritical`` ) to lowest ( ``NonCritical`` ).
        :param data_location_constraint: Specifies a high-level geographical location constraint for where your resilience policy data can be stored.
        :param policy_description: The description for the policy.
        :param tags: Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ca523154c6ed6b81a708c52b134ad763abb59cc66e6b7fc33cf2c8de8bda28b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResiliencyPolicyProps(
            policy=policy,
            policy_name=policy_name,
            tier=tier,
            data_location_constraint=data_location_constraint,
            policy_description=policy_description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23ae03f6bfefa00273e55de0b4ee8ebbb10095bb3e49cce571cda4bef8a8494)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70914fc8c6bf4533b705a29f3317230532469314340e9789128d3b37814b1543)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyArn")
    def attr_policy_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the resiliency policy.

        :cloudformationAttribute: PolicyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyArn"))

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
    @jsii.member(jsii_name="policy")
    def policy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnResiliencyPolicy.FailurePolicyProperty"]]]:
        '''The resiliency policy.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnResiliencyPolicy.FailurePolicyProperty"]]], jsii.get(self, "policy"))

    @policy.setter
    def policy(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnResiliencyPolicy.FailurePolicyProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c81f492b83bee694a01e4aa4ae84bc7903a84252105f01380996bcf77119a83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34fd04d0312f7348f68c9a137c175637ed8986ee6668d212f9ccb5f63df73cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        '''The tier for this resiliency policy, ranging from the highest severity ( ``MissionCritical`` ) to lowest ( ``NonCritical`` ).'''
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63aa6d63d9a2e5c5908fb449583a66f8f0ca1b9d0299917bf1c9aa1018efbe8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="dataLocationConstraint")
    def data_location_constraint(self) -> typing.Optional[builtins.str]:
        '''Specifies a high-level geographical location constraint for where your resilience policy data can be stored.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataLocationConstraint"))

    @data_location_constraint.setter
    def data_location_constraint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ce3251c4d65d121ac1dfd3d81f2cc55a1e4f5d27dd6107aec2662ccd9f9da1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLocationConstraint", value)

    @builtins.property
    @jsii.member(jsii_name="policyDescription")
    def policy_description(self) -> typing.Optional[builtins.str]:
        '''The description for the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyDescription"))

    @policy_description.setter
    def policy_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33c98d88b8f5dc4d978a76d3d8062b3b9ed0b9dbd8a11666125cf03bdb240c25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDescription", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags assigned to the resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e570922a4c9e088d785778e4bf4377e5e745c3948e4b4c61b64f0cbbefee0ce9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resiliencehub.CfnResiliencyPolicy.FailurePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"rpo_in_secs": "rpoInSecs", "rto_in_secs": "rtoInSecs"},
    )
    class FailurePolicyProperty:
        def __init__(
            self,
            *,
            rpo_in_secs: jsii.Number,
            rto_in_secs: jsii.Number,
        ) -> None:
            '''Defines a failure policy.

            :param rpo_in_secs: Recovery Point Objective (RPO) in seconds.
            :param rto_in_secs: Recovery Time Objective (RTO) in seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resiliencehub as resiliencehub
                
                failure_policy_property = resiliencehub.CfnResiliencyPolicy.FailurePolicyProperty(
                    rpo_in_secs=123,
                    rto_in_secs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b31c880d8724506ba4025d50fede62d462b847c02406fe66ed0c1b34e12bd23)
                check_type(argname="argument rpo_in_secs", value=rpo_in_secs, expected_type=type_hints["rpo_in_secs"])
                check_type(argname="argument rto_in_secs", value=rto_in_secs, expected_type=type_hints["rto_in_secs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rpo_in_secs": rpo_in_secs,
                "rto_in_secs": rto_in_secs,
            }

        @builtins.property
        def rpo_in_secs(self) -> jsii.Number:
            '''Recovery Point Objective (RPO) in seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html#cfn-resiliencehub-resiliencypolicy-failurepolicy-rpoinsecs
            '''
            result = self._values.get("rpo_in_secs")
            assert result is not None, "Required property 'rpo_in_secs' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rto_in_secs(self) -> jsii.Number:
            '''Recovery Time Objective (RTO) in seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html#cfn-resiliencehub-resiliencypolicy-failurepolicy-rtoinsecs
            '''
            result = self._values.get("rto_in_secs")
            assert result is not None, "Required property 'rto_in_secs' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailurePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_resiliencehub.CfnResiliencyPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "policy_name": "policyName",
        "tier": "tier",
        "data_location_constraint": "dataLocationConstraint",
        "policy_description": "policyDescription",
        "tags": "tags",
    },
)
class CfnResiliencyPolicyProps:
    def __init__(
        self,
        *,
        policy: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnResiliencyPolicy.FailurePolicyProperty, typing.Dict[builtins.str, typing.Any]]]]],
        policy_name: builtins.str,
        tier: builtins.str,
        data_location_constraint: typing.Optional[builtins.str] = None,
        policy_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResiliencyPolicy``.

        :param policy: The resiliency policy.
        :param policy_name: The name of the policy.
        :param tier: The tier for this resiliency policy, ranging from the highest severity ( ``MissionCritical`` ) to lowest ( ``NonCritical`` ).
        :param data_location_constraint: Specifies a high-level geographical location constraint for where your resilience policy data can be stored.
        :param policy_description: The description for the policy.
        :param tags: Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_resiliencehub as resiliencehub
            
            cfn_resiliency_policy_props = resiliencehub.CfnResiliencyPolicyProps(
                policy={
                    "policy_key": resiliencehub.CfnResiliencyPolicy.FailurePolicyProperty(
                        rpo_in_secs=123,
                        rto_in_secs=123
                    )
                },
                policy_name="policyName",
                tier="tier",
            
                # the properties below are optional
                data_location_constraint="dataLocationConstraint",
                policy_description="policyDescription",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b51a30718bd8977a8288b1d2934e1722c7b034c5064ff893bb6b2bbb6feb7ba7)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument data_location_constraint", value=data_location_constraint, expected_type=type_hints["data_location_constraint"])
            check_type(argname="argument policy_description", value=policy_description, expected_type=type_hints["policy_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
            "policy_name": policy_name,
            "tier": tier,
        }
        if data_location_constraint is not None:
            self._values["data_location_constraint"] = data_location_constraint
        if policy_description is not None:
            self._values["policy_description"] = policy_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def policy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnResiliencyPolicy.FailurePolicyProperty]]]:
        '''The resiliency policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnResiliencyPolicy.FailurePolicyProperty]]], result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''The tier for this resiliency policy, ranging from the highest severity ( ``MissionCritical`` ) to lowest ( ``NonCritical`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-tier
        '''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_location_constraint(self) -> typing.Optional[builtins.str]:
        '''Specifies a high-level geographical location constraint for where your resilience policy data can be stored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-datalocationconstraint
        '''
        result = self._values.get("data_location_constraint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_description(self) -> typing.Optional[builtins.str]:
        '''The description for the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policydescription
        '''
        result = self._values.get("policy_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags assigned to the resource.

        A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResiliencyPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApp",
    "CfnAppProps",
    "CfnResiliencyPolicy",
    "CfnResiliencyPolicyProps",
]

publication.publish()

def _typecheckingstub__303e76fc3650422653be00dea7484c071f68688b86b0b136d647cee7306c7958(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_template_body: builtins.str,
    name: builtins.str,
    resource_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.ResourceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]],
    app_assessment_schedule: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    event_subscriptions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EventSubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    permission_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.PermissionModelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resiliency_policy_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59fba2f0cf5aadd1fd75ba32c9b4bfb1c0d6e43acd0002173024ce9e85ed285e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39b1746c5aaa0b06207855cbb349cb99ee17a1df8cdfc71812db83d0b9680219(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c2df1cafeabd95579e76b6448abd4bc8191ed805fa79934e5a2ba2863d8a4a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ec5f12ec50861e776ad80e27c62359d36bca636f0adbf44ed2618963e02c64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7be56e25078fc8e2aedbbef7b1762fc9e3fdb0096405151631ffaeb94832cc34(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.ResourceMappingProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1219dae6dd0d44c29343fb98a2d5c76c2a24c08981364a9635db5d542b60665d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef5b0a7209d4ed93ddc4b9b03b30dfaf9f4e659b9ac9551bd3e4332a348c0c36(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d302607b7a1dfbffee8d2ab82e294e1d08c27584331ec9bea2e75add9db5b6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EventSubscriptionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e15df41e400e8a9cff1ec67cfe4cdb6224b7e0faa1f84a7164a3aff0b0462f9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.PermissionModelProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce4ee431bd44e41d23a7b0df5a1d235166dfde2dcb98cb013d61da840d20b025(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d13896f18fa79328cd19410a666196ad5f076947628b86a3d2d74479248cc5b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24e5de7bc5abc5f46b1e0bcc9b765adaa418f9f436edcfd31c40a13a5740d617(
    *,
    event_type: builtins.str,
    name: builtins.str,
    sns_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8107f5f0a79085bc51c1ccd12ec056fa14fa89fbad641ef5065c416f4ae281(
    *,
    type: builtins.str,
    cross_account_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    invoker_role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eacd68e84c228cdd21e0474784bb6561272f2528af8dda91c1eb8fc45207812(
    *,
    identifier: builtins.str,
    type: builtins.str,
    aws_account_id: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ce15c2c4786e2990c8cd30f8becbb71d99cd69d3c1b4c44211c8e6baaf1027(
    *,
    mapping_type: builtins.str,
    physical_resource_id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.PhysicalResourceIdProperty, typing.Dict[builtins.str, typing.Any]]],
    eks_source_name: typing.Optional[builtins.str] = None,
    logical_stack_name: typing.Optional[builtins.str] = None,
    resource_name: typing.Optional[builtins.str] = None,
    terraform_source_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4cbfaccc19fec8c2bd3f0ad17cdc9d5c9a66dbdcc7077312163442e737af125(
    *,
    app_template_body: builtins.str,
    name: builtins.str,
    resource_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.ResourceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]],
    app_assessment_schedule: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    event_subscriptions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EventSubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    permission_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.PermissionModelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resiliency_policy_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca523154c6ed6b81a708c52b134ad763abb59cc66e6b7fc33cf2c8de8bda28b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnResiliencyPolicy.FailurePolicyProperty, typing.Dict[builtins.str, typing.Any]]]]],
    policy_name: builtins.str,
    tier: builtins.str,
    data_location_constraint: typing.Optional[builtins.str] = None,
    policy_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23ae03f6bfefa00273e55de0b4ee8ebbb10095bb3e49cce571cda4bef8a8494(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70914fc8c6bf4533b705a29f3317230532469314340e9789128d3b37814b1543(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c81f492b83bee694a01e4aa4ae84bc7903a84252105f01380996bcf77119a83(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnResiliencyPolicy.FailurePolicyProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34fd04d0312f7348f68c9a137c175637ed8986ee6668d212f9ccb5f63df73cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63aa6d63d9a2e5c5908fb449583a66f8f0ca1b9d0299917bf1c9aa1018efbe8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ce3251c4d65d121ac1dfd3d81f2cc55a1e4f5d27dd6107aec2662ccd9f9da1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33c98d88b8f5dc4d978a76d3d8062b3b9ed0b9dbd8a11666125cf03bdb240c25(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e570922a4c9e088d785778e4bf4377e5e745c3948e4b4c61b64f0cbbefee0ce9(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b31c880d8724506ba4025d50fede62d462b847c02406fe66ed0c1b34e12bd23(
    *,
    rpo_in_secs: jsii.Number,
    rto_in_secs: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51a30718bd8977a8288b1d2934e1722c7b034c5064ff893bb6b2bbb6feb7ba7(
    *,
    policy: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnResiliencyPolicy.FailurePolicyProperty, typing.Dict[builtins.str, typing.Any]]]]],
    policy_name: builtins.str,
    tier: builtins.str,
    data_location_constraint: typing.Optional[builtins.str] = None,
    policy_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
