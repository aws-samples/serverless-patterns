'''
# AWS Systems Manager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Using existing SSM Parameters in your CDK app

You can reference existing SSM Parameter Store values that you want to use in
your CDK app by using `ssm.StringParameter.fromStringParameterAttributes`:

```python
parameter_version = Token.as_number({"Ref": "MyParameter"})

# Retrieve the latest value of the non-secret parameter
# with name "/My/String/Parameter".
string_value = ssm.StringParameter.from_string_parameter_attributes(self, "MyValue",
    parameter_name="/My/Public/Parameter"
).string_value
string_value_version_from_token = ssm.StringParameter.from_string_parameter_attributes(self, "MyValueVersionFromToken",
    parameter_name="/My/Public/Parameter",
    # parameter version from token
    version=parameter_version
).string_value

# Retrieve a specific version of the secret (SecureString) parameter.
# 'version' is always required.
secret_value = ssm.StringParameter.from_secure_string_parameter_attributes(self, "MySecureValue",
    parameter_name="/My/Secret/Parameter",
    version=5
)
secret_value_version_from_token = ssm.StringParameter.from_secure_string_parameter_attributes(self, "MySecureValueVersionFromToken",
    parameter_name="/My/Secret/Parameter",
    # parameter version from token
    version=parameter_version
)
```

You can also reference an existing SSM Parameter Store value that matches an
[AWS specific parameter type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-specific-parameter-types):

```python
ssm.StringParameter.value_for_typed_string_parameter_v2(self, "/My/Public/Parameter", ssm.ParameterValueType.AWS_EC2_IMAGE_ID)
```

To do the same for a SSM Parameter Store value that is stored as a list:

```python
ssm.StringListParameter.value_for_typed_list_parameter(self, "/My/Public/Parameter", ssm.ParameterValueType.AWS_EC2_IMAGE_ID)
```

### Lookup existing parameters

You can also use an existing parameter by looking up the parameter from the AWS environment.
This method uses AWS API calls to lookup the value from SSM during synthesis.

```python
string_value = ssm.StringParameter.value_from_lookup(self, "/My/Public/Parameter")
```

When using `valueFromLookup` an initial value of 'dummy-value-for-${parameterName}'
(`dummy-value-for-/My/Public/Parameter` in the above example)
is returned prior to the lookup being performed. This can lead to errors if you are using this
value in places that require a certain format. For example if you have stored the ARN for a SNS
topic in a SSM Parameter which you want to lookup and provide to `Topic.fromTopicArn()`

```python
arn_lookup = ssm.StringParameter.value_from_lookup(self, "/my/topic/arn")
sns.Topic.from_topic_arn(self, "Topic", arn_lookup)
```

Initially `arnLookup` will be equal to `dummy-value-for-/my/topic/arn` which will cause
`Topic.fromTopicArn` to throw an error indicating that the value is not in `arn` format.

For these use cases you need to handle the `dummy-value` in your code. For example:

```python
arn_lookup = ssm.StringParameter.value_from_lookup(self, "/my/topic/arn")
# arn_lookup_value: str
if arn_lookup.includes("dummy-value"):
    arn_lookup_value = self.format_arn(
        service="sns",
        resource="topic",
        resource_name=arn_lookup
    )
else:
    arn_lookup_value = arn_lookup

sns.Topic.from_topic_arn(self, "Topic", arn_lookup_value)
```

Alternatively, if the property supports tokens you can convert the parameter value into a token
to be resolved *after* the lookup has been completed.

```python
arn_lookup = ssm.StringParameter.value_from_lookup(self, "/my/role/arn")
iam.Role.from_role_arn(self, "role", Lazy.string({"produce": () => arnLookup}))
```

## Creating new SSM Parameters in your CDK app

You can create either `ssm.StringParameter` or `ssm.StringListParameter`s in
a CDK app. These are public (not secret) values. Parameters of type
*SecureString* cannot be created directly from a CDK application; if you want
to provision secrets automatically, use Secrets Manager Secrets (see the
`aws-cdk-lib/aws-secretsmanager` package).

```python
ssm.StringParameter(self, "Parameter",
    allowed_pattern=".*",
    description="The value Foo",
    parameter_name="FooParameter",
    string_value="Foo",
    tier=ssm.ParameterTier.ADVANCED
)
```

```python
# Grant read access to some Role
# role: iam.IRole
# Create a new SSM Parameter holding a String
param = ssm.StringParameter(self, "StringParameter",
    # description: 'Some user-friendly description',
    # name: 'ParameterName',
    string_value="Initial parameter value"
)
param.grant_read(role)

# Create a new SSM Parameter holding a StringList
list_parameter = ssm.StringListParameter(self, "StringListParameter",
    # description: 'Some user-friendly description',
    # name: 'ParameterName',
    string_list_value=["Initial parameter value A", "Initial parameter value B"]
)
```

When specifying an `allowedPattern`, the values provided as string literals
are validated against the pattern and an exception is raised if a value
provided does not comply.
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
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_iam import Grant as _Grant_a7ae64f8, IGrantable as _IGrantable_71c4f5de
from ..aws_kms import IKey as _IKey_5f11635f


@jsii.implements(_IInspectable_c2943556)
class CfnAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation",
):
    '''The ``AWS::SSM::Association`` resource creates a State Manager association for your managed instances.

    A State Manager association defines the state that you want to maintain on your instances. For example, an association can specify that anti-virus software must be installed and running on your instances, or that certain ports must be closed. For static targets, the association specifies a schedule for when the configuration is reapplied. For dynamic targets, such as an AWS Resource Groups or an AWS Auto Scaling Group, State Manager applies the configuration when new instances are added to the group. The association also specifies actions to take when applying the configuration. For example, an association for anti-virus software might run once a day. If the software is not installed, then State Manager installs it. If the software is installed, but the service is not running, then the association might instruct State Manager to start the service.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
    :cloudformationResource: AWS::SSM::Association
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        # parameters: Any
        
        cfn_association = ssm.CfnAssociation(self, "MyCfnAssociation",
            name="name",
        
            # the properties below are optional
            apply_only_at_cron_interval=False,
            association_name="associationName",
            automation_target_parameter_name="automationTargetParameterName",
            calendar_names=["calendarNames"],
            compliance_severity="complianceSeverity",
            document_version="documentVersion",
            instance_id="instanceId",
            max_concurrency="maxConcurrency",
            max_errors="maxErrors",
            output_location=ssm.CfnAssociation.InstanceAssociationOutputLocationProperty(
                s3_location=ssm.CfnAssociation.S3OutputLocationProperty(
                    output_s3_bucket_name="outputS3BucketName",
                    output_s3_key_prefix="outputS3KeyPrefix",
                    output_s3_region="outputS3Region"
                )
            ),
            parameters=parameters,
            schedule_expression="scheduleExpression",
            schedule_offset=123,
            sync_compliance="syncCompliance",
            targets=[ssm.CfnAssociation.TargetProperty(
                key="key",
                values=["values"]
            )],
            wait_for_success_timeout_seconds=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        association_name: typing.Optional[builtins.str] = None,
        automation_target_parameter_name: typing.Optional[builtins.str] = None,
        calendar_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        compliance_severity: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        parameters: typing.Any = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        sync_compliance: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssociation.TargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the SSM document that contains the configuration information for the instance. You can specify ``Command`` or ``Automation`` documents. The documents can be AWS -predefined documents, documents you created, or a document that is shared with you from another account. For SSM documents that are shared with you from other AWS accounts , you must specify the complete SSM document ARN, in the following format: ``arn:partition:ssm:region:account-id:document/document-name`` For example: ``arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document`` For AWS -predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, ``AWS -ApplyPatchBaseline`` or ``My-Document`` .
        :param apply_only_at_cron_interval: By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you don't want an association to run immediately after you create it. This parameter is not supported for rate expressions.
        :param association_name: Specify a descriptive name for the association.
        :param automation_target_parameter_name: Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a capability of AWS Systems Manager .
        :param calendar_names: The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations only run when that Change Calendar is open. For more information, see `AWS Systems Manager Change Calendar <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar>`_ .
        :param compliance_severity: The severity level that is assigned to the association.
        :param document_version: The version of the SSM document to associate with the target. .. epigraph:: Note the following important information. - State Manager doesn't support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the ``default`` version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to ``default`` . - ``DocumentVersion`` is not valid for documents owned by AWS , such as ``AWS-RunPatchBaseline`` or ``AWS-UpdateSSMAgent`` . If you specify ``DocumentVersion`` for an AWS document, the system returns the following error: "Error occurred during operation 'CreateAssociation'." (RequestToken: , HandlerErrorCode: GeneralServiceException).
        :param instance_id: The ID of the instance that the SSM document is associated with. You must specify the ``InstanceId`` or ``Targets`` property. .. epigraph:: ``InstanceId`` has been deprecated. To specify an instance ID for an association, use the ``Targets`` parameter. If you use the parameter ``InstanceId`` , you cannot use the parameters ``AssociationName`` , ``DocumentVersion`` , ``MaxErrors`` , ``MaxConcurrency`` , ``OutputLocation`` , or ``ScheduleExpression`` . To use these parameters, you must use the ``Targets`` parameter.
        :param max_concurrency: The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time. If a new managed node starts and attempts to run an association while Systems Manager is running ``MaxConcurrency`` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for ``MaxConcurrency`` .
        :param max_errors: The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set ``MaxError`` to 10%, then the system stops sending the request when the sixth error is received. Executions that are already running an association when ``MaxErrors`` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set ``MaxConcurrency`` to 1 so that executions proceed one at a time.
        :param output_location: An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.
        :param parameters: The parameters for the runtime configuration of the document.
        :param schedule_expression: A cron expression that specifies a schedule when the association runs. The schedule runs in Coordinated Universal Time (UTC).
        :param schedule_offset: Number of days to wait after the scheduled day to run an association.
        :param sync_compliance: The mode for generating association compliance. You can specify ``AUTO`` or ``MANUAL`` . In ``AUTO`` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is ``COMPLIANT`` . If the association execution doesn't run successfully, the association is ``NON-COMPLIANT`` . In ``MANUAL`` mode, you must specify the ``AssociationId`` as a parameter for the ``PutComplianceItems`` API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the ``PutComplianceItems`` API action. By default, all associations use ``AUTO`` mode.
        :param targets: The targets for the association. You must specify the ``InstanceId`` or ``Targets`` property. You can target all instances in an AWS account by specifying t he ``InstanceIds`` key with a value of ``*`` . Supported formats include the following. - ``Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>,<instance-id-3>`` - ``Key=tag-key,Values=<my-tag-key-1>,<my-tag-key-2>`` To view a JSON and a YAML example that targets all instances, see "Create an association for all managed instances in an AWS account " on the Examples page.
        :param wait_for_success_timeout_seconds: The number of seconds the service should wait for the association status to show "Success" before proceeding with the stack execution. If the association status doesn't show "Success" after the specified number of seconds, then stack creation fails. .. epigraph:: When you specify a value for the ``WaitForSuccessTimeoutSeconds`` , `drift detection <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`_ for your AWS CloudFormation stack’s configuration might yield inaccurate results. If drift detection is important in your scenario, we recommend that you don’t include ``WaitForSuccessTimeoutSeconds`` in your template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92579425f735301e17a993e7df464a283a7d42ba685c2d4205cf945db662d245)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssociationProps(
            name=name,
            apply_only_at_cron_interval=apply_only_at_cron_interval,
            association_name=association_name,
            automation_target_parameter_name=automation_target_parameter_name,
            calendar_names=calendar_names,
            compliance_severity=compliance_severity,
            document_version=document_version,
            instance_id=instance_id,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            output_location=output_location,
            parameters=parameters,
            schedule_expression=schedule_expression,
            schedule_offset=schedule_offset,
            sync_compliance=sync_compliance,
            targets=targets,
            wait_for_success_timeout_seconds=wait_for_success_timeout_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04dced959ace7c06e46713696a2e0111696820a92076dddbfb0d4e73ef74ff78)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1a0993d5c26d39b2f098659a8dbf1c928697492ab3d066975eff6b1a5799d2b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> builtins.str:
        '''The association ID.

        :cloudformationAttribute: AssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the SSM document that contains the configuration information for the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e92bf5492040a0299998b0a9b059a356249d33ec61a41eeee594e093a7d0fb93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="applyOnlyAtCronInterval")
    def apply_only_at_cron_interval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "applyOnlyAtCronInterval"))

    @apply_only_at_cron_interval.setter
    def apply_only_at_cron_interval(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9023084f7868b14116f97ca76b80fe2c8428bca0dc340c9e250534372a8882b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyOnlyAtCronInterval", value)

    @builtins.property
    @jsii.member(jsii_name="associationName")
    def association_name(self) -> typing.Optional[builtins.str]:
        '''Specify a descriptive name for the association.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associationName"))

    @association_name.setter
    def association_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb049dd8f3d81baa9ccd163bb3c0e0c5f10114fd3a4d9ed4a1da2dfaa2e7a70c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associationName", value)

    @builtins.property
    @jsii.member(jsii_name="automationTargetParameterName")
    def automation_target_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Choose the parameter that will define how your automation will branch out.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automationTargetParameterName"))

    @automation_target_parameter_name.setter
    def automation_target_parameter_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784e8ad1b8f5f3c269d31598a3121d33ed36eb41074ed3c1c4d612eed6484920)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automationTargetParameterName", value)

    @builtins.property
    @jsii.member(jsii_name="calendarNames")
    def calendar_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "calendarNames"))

    @calendar_names.setter
    def calendar_names(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89f46620766a6cb92f5e7135d5be6128d4d6e6dc8da7d7a49f8216a2bd89ce04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "calendarNames", value)

    @builtins.property
    @jsii.member(jsii_name="complianceSeverity")
    def compliance_severity(self) -> typing.Optional[builtins.str]:
        '''The severity level that is assigned to the association.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceSeverity"))

    @compliance_severity.setter
    def compliance_severity(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e8a1f13b08374e8b174f211647e4f9aee7820e96b01b93747f906958e9aff43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "complianceSeverity", value)

    @builtins.property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> typing.Optional[builtins.str]:
        '''The version of the SSM document to associate with the target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6852a105eba64031e2ab4c7f0f0c2569933f7be795a2d958593d091f277a667)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the instance that the SSM document is associated with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a40e1278e729960017eba97f7aaf904bfa9d528733d2142f2710e6cf17306f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''The maximum number of targets allowed to run the association at the same time.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8a46c913675e9198e679ed1f83d648c1ccd40b2341879145404fd2ebc256093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''The number of errors that are allowed before the system stops sending requests to run the association on additional targets.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97c0c0ebc4e8f350ab107d93e7f4ebce7994eb4e9c23da3d470fbd5a5fd349e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxErrors", value)

    @builtins.property
    @jsii.member(jsii_name="outputLocation")
    def output_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssociation.InstanceAssociationOutputLocationProperty"]]:
        '''An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssociation.InstanceAssociationOutputLocationProperty"]], jsii.get(self, "outputLocation"))

    @output_location.setter
    def output_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssociation.InstanceAssociationOutputLocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7f2d6bae4a2f47caddaa51675bf95100b06b460f639a924aec4c36f3e0dfe13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputLocation", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''The parameters for the runtime configuration of the document.'''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7bc72c1573e12dfc32dfc15c4125adfa3aee907e4c231fb1dc195260483bca5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> typing.Optional[builtins.str]:
        '''A cron expression that specifies a schedule when the association runs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b45e3419b475a4d33fe733aa9418e965aeddb232d631f9b2024913c92d22947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpression", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleOffset")
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''Number of days to wait after the scheduled day to run an association.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scheduleOffset"))

    @schedule_offset.setter
    def schedule_offset(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae92d319670461482db27cc5bf559ad4df2f8df83ba4d88119ce8f83e9169873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleOffset", value)

    @builtins.property
    @jsii.member(jsii_name="syncCompliance")
    def sync_compliance(self) -> typing.Optional[builtins.str]:
        '''The mode for generating association compliance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncCompliance"))

    @sync_compliance.setter
    def sync_compliance(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d7078ea082466fa5a28a7853d4916de9d395e0a7adf5ae826e9a2028bdb9a93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncCompliance", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssociation.TargetProperty"]]]]:
        '''The targets for the association.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssociation.TargetProperty"]]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssociation.TargetProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ce3b93eff1353677d4fb546ad1db9172eecc860870a57f1426f1ff63ce088d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @builtins.property
    @jsii.member(jsii_name="waitForSuccessTimeoutSeconds")
    def wait_for_success_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds the service should wait for the association status to show "Success" before proceeding with the stack execution.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitForSuccessTimeoutSeconds"))

    @wait_for_success_timeout_seconds.setter
    def wait_for_success_timeout_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43bea7a30e23800585f05a151814b8ef7b0f58707fa06c13448e65157d2bac89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForSuccessTimeoutSeconds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.InstanceAssociationOutputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_location": "s3Location"},
    )
    class InstanceAssociationOutputLocationProperty:
        def __init__(
            self,
            *,
            s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssociation.S3OutputLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''``InstanceAssociationOutputLocation`` is a property of the `AWS::SSM::Association <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html>`_ resource that specifies an Amazon S3 bucket where you want to store the results of this association request.

            For the minimal permissions required to enable Amazon S3 output for an association, see `Creating associations <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc.html>`_ in the *Systems Manager User Guide* .

            :param s3_location: ``S3OutputLocation`` is a property of the `InstanceAssociationOutputLocation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html>`_ property that specifies an Amazon S3 bucket where you want to store the results of this request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                instance_association_output_location_property = ssm.CfnAssociation.InstanceAssociationOutputLocationProperty(
                    s3_location=ssm.CfnAssociation.S3OutputLocationProperty(
                        output_s3_bucket_name="outputS3BucketName",
                        output_s3_key_prefix="outputS3KeyPrefix",
                        output_s3_region="outputS3Region"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29c9f5eb48dae8552c932fed2a3854daa4ad977ed9796c37909bff98cd60fc4a)
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def s3_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssociation.S3OutputLocationProperty"]]:
            '''``S3OutputLocation`` is a property of the `InstanceAssociationOutputLocation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html>`_ property that specifies an Amazon S3 bucket where you want to store the results of this request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html#cfn-ssm-association-instanceassociationoutputlocation-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssociation.S3OutputLocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceAssociationOutputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.S3OutputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output_s3_bucket_name": "outputS3BucketName",
            "output_s3_key_prefix": "outputS3KeyPrefix",
            "output_s3_region": "outputS3Region",
        },
    )
    class S3OutputLocationProperty:
        def __init__(
            self,
            *,
            output_s3_bucket_name: typing.Optional[builtins.str] = None,
            output_s3_key_prefix: typing.Optional[builtins.str] = None,
            output_s3_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``S3OutputLocation`` is a property of the `AWS::SSM::Association <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html>`_ resource that specifies an Amazon S3 bucket where you want to store the results of this association request.

            :param output_s3_bucket_name: The name of the S3 bucket.
            :param output_s3_key_prefix: The S3 bucket subfolder.
            :param output_s3_region: The AWS Region of the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                s3_output_location_property = ssm.CfnAssociation.S3OutputLocationProperty(
                    output_s3_bucket_name="outputS3BucketName",
                    output_s3_key_prefix="outputS3KeyPrefix",
                    output_s3_region="outputS3Region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35ca1813f2b90a1f8e54124b2a16a5661e9c22d218461bb08292623a1dd09123)
                check_type(argname="argument output_s3_bucket_name", value=output_s3_bucket_name, expected_type=type_hints["output_s3_bucket_name"])
                check_type(argname="argument output_s3_key_prefix", value=output_s3_key_prefix, expected_type=type_hints["output_s3_key_prefix"])
                check_type(argname="argument output_s3_region", value=output_s3_region, expected_type=type_hints["output_s3_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if output_s3_bucket_name is not None:
                self._values["output_s3_bucket_name"] = output_s3_bucket_name
            if output_s3_key_prefix is not None:
                self._values["output_s3_key_prefix"] = output_s3_key_prefix
            if output_s3_region is not None:
                self._values["output_s3_region"] = output_s3_region

        @builtins.property
        def output_s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3bucketname
            '''
            result = self._values.get("output_s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 bucket subfolder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3keyprefix
            '''
            result = self._values.get("output_s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region of the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3region
            '''
            result = self._values.get("output_s3_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''``Target`` is a property of the `AWS::SSM::Association <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html>`_ resource that specifies the targets for an SSM document in Systems Manager . You can target all instances in an AWS account by specifying the ``InstanceIds`` key with a value of ``*`` . To view a JSON and a YAML example that targets all instances, see the example "Create an association for all managed instances in an AWS account " later in this page.

            :param key: User-defined criteria for sending commands that target managed nodes that meet the criteria.
            :param values: User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include EC2 tags of ``ServerRole,WebServer`` . Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                target_property = ssm.CfnAssociation.TargetProperty(
                    key="key",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e23bdeb61e8b0804a4fde32db838d3743a925dc709401804cd81e355e25bee0d)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''User-defined criteria for sending commands that target managed nodes that meet the criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''User-defined criteria that maps to ``Key`` .

            For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include EC2 tags of ``ServerRole,WebServer`` .

            Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "apply_only_at_cron_interval": "applyOnlyAtCronInterval",
        "association_name": "associationName",
        "automation_target_parameter_name": "automationTargetParameterName",
        "calendar_names": "calendarNames",
        "compliance_severity": "complianceSeverity",
        "document_version": "documentVersion",
        "instance_id": "instanceId",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "output_location": "outputLocation",
        "parameters": "parameters",
        "schedule_expression": "scheduleExpression",
        "schedule_offset": "scheduleOffset",
        "sync_compliance": "syncCompliance",
        "targets": "targets",
        "wait_for_success_timeout_seconds": "waitForSuccessTimeoutSeconds",
    },
)
class CfnAssociationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        association_name: typing.Optional[builtins.str] = None,
        automation_target_parameter_name: typing.Optional[builtins.str] = None,
        calendar_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        compliance_severity: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        parameters: typing.Any = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        sync_compliance: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssociation``.

        :param name: The name of the SSM document that contains the configuration information for the instance. You can specify ``Command`` or ``Automation`` documents. The documents can be AWS -predefined documents, documents you created, or a document that is shared with you from another account. For SSM documents that are shared with you from other AWS accounts , you must specify the complete SSM document ARN, in the following format: ``arn:partition:ssm:region:account-id:document/document-name`` For example: ``arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document`` For AWS -predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, ``AWS -ApplyPatchBaseline`` or ``My-Document`` .
        :param apply_only_at_cron_interval: By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you don't want an association to run immediately after you create it. This parameter is not supported for rate expressions.
        :param association_name: Specify a descriptive name for the association.
        :param automation_target_parameter_name: Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a capability of AWS Systems Manager .
        :param calendar_names: The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations only run when that Change Calendar is open. For more information, see `AWS Systems Manager Change Calendar <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar>`_ .
        :param compliance_severity: The severity level that is assigned to the association.
        :param document_version: The version of the SSM document to associate with the target. .. epigraph:: Note the following important information. - State Manager doesn't support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the ``default`` version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to ``default`` . - ``DocumentVersion`` is not valid for documents owned by AWS , such as ``AWS-RunPatchBaseline`` or ``AWS-UpdateSSMAgent`` . If you specify ``DocumentVersion`` for an AWS document, the system returns the following error: "Error occurred during operation 'CreateAssociation'." (RequestToken: , HandlerErrorCode: GeneralServiceException).
        :param instance_id: The ID of the instance that the SSM document is associated with. You must specify the ``InstanceId`` or ``Targets`` property. .. epigraph:: ``InstanceId`` has been deprecated. To specify an instance ID for an association, use the ``Targets`` parameter. If you use the parameter ``InstanceId`` , you cannot use the parameters ``AssociationName`` , ``DocumentVersion`` , ``MaxErrors`` , ``MaxConcurrency`` , ``OutputLocation`` , or ``ScheduleExpression`` . To use these parameters, you must use the ``Targets`` parameter.
        :param max_concurrency: The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time. If a new managed node starts and attempts to run an association while Systems Manager is running ``MaxConcurrency`` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for ``MaxConcurrency`` .
        :param max_errors: The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set ``MaxError`` to 10%, then the system stops sending the request when the sixth error is received. Executions that are already running an association when ``MaxErrors`` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set ``MaxConcurrency`` to 1 so that executions proceed one at a time.
        :param output_location: An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.
        :param parameters: The parameters for the runtime configuration of the document.
        :param schedule_expression: A cron expression that specifies a schedule when the association runs. The schedule runs in Coordinated Universal Time (UTC).
        :param schedule_offset: Number of days to wait after the scheduled day to run an association.
        :param sync_compliance: The mode for generating association compliance. You can specify ``AUTO`` or ``MANUAL`` . In ``AUTO`` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is ``COMPLIANT`` . If the association execution doesn't run successfully, the association is ``NON-COMPLIANT`` . In ``MANUAL`` mode, you must specify the ``AssociationId`` as a parameter for the ``PutComplianceItems`` API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the ``PutComplianceItems`` API action. By default, all associations use ``AUTO`` mode.
        :param targets: The targets for the association. You must specify the ``InstanceId`` or ``Targets`` property. You can target all instances in an AWS account by specifying t he ``InstanceIds`` key with a value of ``*`` . Supported formats include the following. - ``Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>,<instance-id-3>`` - ``Key=tag-key,Values=<my-tag-key-1>,<my-tag-key-2>`` To view a JSON and a YAML example that targets all instances, see "Create an association for all managed instances in an AWS account " on the Examples page.
        :param wait_for_success_timeout_seconds: The number of seconds the service should wait for the association status to show "Success" before proceeding with the stack execution. If the association status doesn't show "Success" after the specified number of seconds, then stack creation fails. .. epigraph:: When you specify a value for the ``WaitForSuccessTimeoutSeconds`` , `drift detection <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`_ for your AWS CloudFormation stack’s configuration might yield inaccurate results. If drift detection is important in your scenario, we recommend that you don’t include ``WaitForSuccessTimeoutSeconds`` in your template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            # parameters: Any
            
            cfn_association_props = ssm.CfnAssociationProps(
                name="name",
            
                # the properties below are optional
                apply_only_at_cron_interval=False,
                association_name="associationName",
                automation_target_parameter_name="automationTargetParameterName",
                calendar_names=["calendarNames"],
                compliance_severity="complianceSeverity",
                document_version="documentVersion",
                instance_id="instanceId",
                max_concurrency="maxConcurrency",
                max_errors="maxErrors",
                output_location=ssm.CfnAssociation.InstanceAssociationOutputLocationProperty(
                    s3_location=ssm.CfnAssociation.S3OutputLocationProperty(
                        output_s3_bucket_name="outputS3BucketName",
                        output_s3_key_prefix="outputS3KeyPrefix",
                        output_s3_region="outputS3Region"
                    )
                ),
                parameters=parameters,
                schedule_expression="scheduleExpression",
                schedule_offset=123,
                sync_compliance="syncCompliance",
                targets=[ssm.CfnAssociation.TargetProperty(
                    key="key",
                    values=["values"]
                )],
                wait_for_success_timeout_seconds=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb0c608fec68cefb540b911fce04c4316c075989d67e9aa888cb8f01cc7e0dac)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument apply_only_at_cron_interval", value=apply_only_at_cron_interval, expected_type=type_hints["apply_only_at_cron_interval"])
            check_type(argname="argument association_name", value=association_name, expected_type=type_hints["association_name"])
            check_type(argname="argument automation_target_parameter_name", value=automation_target_parameter_name, expected_type=type_hints["automation_target_parameter_name"])
            check_type(argname="argument calendar_names", value=calendar_names, expected_type=type_hints["calendar_names"])
            check_type(argname="argument compliance_severity", value=compliance_severity, expected_type=type_hints["compliance_severity"])
            check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_errors", value=max_errors, expected_type=type_hints["max_errors"])
            check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument schedule_offset", value=schedule_offset, expected_type=type_hints["schedule_offset"])
            check_type(argname="argument sync_compliance", value=sync_compliance, expected_type=type_hints["sync_compliance"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument wait_for_success_timeout_seconds", value=wait_for_success_timeout_seconds, expected_type=type_hints["wait_for_success_timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if apply_only_at_cron_interval is not None:
            self._values["apply_only_at_cron_interval"] = apply_only_at_cron_interval
        if association_name is not None:
            self._values["association_name"] = association_name
        if automation_target_parameter_name is not None:
            self._values["automation_target_parameter_name"] = automation_target_parameter_name
        if calendar_names is not None:
            self._values["calendar_names"] = calendar_names
        if compliance_severity is not None:
            self._values["compliance_severity"] = compliance_severity
        if document_version is not None:
            self._values["document_version"] = document_version
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if output_location is not None:
            self._values["output_location"] = output_location
        if parameters is not None:
            self._values["parameters"] = parameters
        if schedule_expression is not None:
            self._values["schedule_expression"] = schedule_expression
        if schedule_offset is not None:
            self._values["schedule_offset"] = schedule_offset
        if sync_compliance is not None:
            self._values["sync_compliance"] = sync_compliance
        if targets is not None:
            self._values["targets"] = targets
        if wait_for_success_timeout_seconds is not None:
            self._values["wait_for_success_timeout_seconds"] = wait_for_success_timeout_seconds

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the SSM document that contains the configuration information for the instance.

        You can specify ``Command`` or ``Automation`` documents. The documents can be AWS -predefined documents, documents you created, or a document that is shared with you from another account. For SSM documents that are shared with you from other AWS accounts , you must specify the complete SSM document ARN, in the following format:

        ``arn:partition:ssm:region:account-id:document/document-name``

        For example: ``arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document``

        For AWS -predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, ``AWS -ApplyPatchBaseline`` or ``My-Document`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_only_at_cron_interval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified.

        Specify this option if you don't want an association to run immediately after you create it. This parameter is not supported for rate expressions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-applyonlyatcroninterval
        '''
        result = self._values.get("apply_only_at_cron_interval")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def association_name(self) -> typing.Optional[builtins.str]:
        '''Specify a descriptive name for the association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-associationname
        '''
        result = self._values.get("association_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automation_target_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Choose the parameter that will define how your automation will branch out.

        This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a capability of AWS Systems Manager .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-automationtargetparametername
        '''
        result = self._values.get("automation_target_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def calendar_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under.

        The associations only run when that Change Calendar is open. For more information, see `AWS Systems Manager Change Calendar <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-calendarnames
        '''
        result = self._values.get("calendar_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def compliance_severity(self) -> typing.Optional[builtins.str]:
        '''The severity level that is assigned to the association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-complianceseverity
        '''
        result = self._values.get("compliance_severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''The version of the SSM document to associate with the target.

        .. epigraph::

           Note the following important information.

           - State Manager doesn't support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the ``default`` version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to ``default`` .
           - ``DocumentVersion`` is not valid for documents owned by AWS , such as ``AWS-RunPatchBaseline`` or ``AWS-UpdateSSMAgent`` . If you specify ``DocumentVersion`` for an AWS document, the system returns the following error: "Error occurred during operation 'CreateAssociation'." (RequestToken: , HandlerErrorCode: GeneralServiceException).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-documentversion
        '''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the instance that the SSM document is associated with.

        You must specify the ``InstanceId`` or ``Targets`` property.
        .. epigraph::

           ``InstanceId`` has been deprecated. To specify an instance ID for an association, use the ``Targets`` parameter. If you use the parameter ``InstanceId`` , you cannot use the parameters ``AssociationName`` , ``DocumentVersion`` , ``MaxErrors`` , ``MaxConcurrency`` , ``OutputLocation`` , or ``ScheduleExpression`` . To use these parameters, you must use the ``Targets`` parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-instanceid
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''The maximum number of targets allowed to run the association at the same time.

        You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.

        If a new managed node starts and attempts to run an association while Systems Manager is running ``MaxConcurrency`` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for ``MaxConcurrency`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxconcurrency
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''The number of errors that are allowed before the system stops sending requests to run the association on additional targets.

        You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set ``MaxError`` to 10%, then the system stops sending the request when the sixth error is received.

        Executions that are already running an association when ``MaxErrors`` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set ``MaxConcurrency`` to 1 so that executions proceed one at a time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxerrors
        '''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssociation.InstanceAssociationOutputLocationProperty]]:
        '''An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-outputlocation
        '''
        result = self._values.get("output_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssociation.InstanceAssociationOutputLocationProperty]], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''The parameters for the runtime configuration of the document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def schedule_expression(self) -> typing.Optional[builtins.str]:
        '''A cron expression that specifies a schedule when the association runs.

        The schedule runs in Coordinated Universal Time (UTC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleexpression
        '''
        result = self._values.get("schedule_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''Number of days to wait after the scheduled day to run an association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleoffset
        '''
        result = self._values.get("schedule_offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sync_compliance(self) -> typing.Optional[builtins.str]:
        '''The mode for generating association compliance.

        You can specify ``AUTO`` or ``MANUAL`` . In ``AUTO`` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is ``COMPLIANT`` . If the association execution doesn't run successfully, the association is ``NON-COMPLIANT`` .

        In ``MANUAL`` mode, you must specify the ``AssociationId`` as a parameter for the ``PutComplianceItems`` API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the ``PutComplianceItems`` API action.

        By default, all associations use ``AUTO`` mode.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-synccompliance
        '''
        result = self._values.get("sync_compliance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssociation.TargetProperty]]]]:
        '''The targets for the association.

        You must specify the ``InstanceId`` or ``Targets`` property. You can target all instances in an AWS account by specifying t he ``InstanceIds`` key with a value of ``*`` .

        Supported formats include the following.

        - ``Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>,<instance-id-3>``
        - ``Key=tag-key,Values=<my-tag-key-1>,<my-tag-key-2>``

        To view a JSON and a YAML example that targets all instances, see "Create an association for all managed instances in an AWS account " on the Examples page.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-targets
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssociation.TargetProperty]]]], result)

    @builtins.property
    def wait_for_success_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds the service should wait for the association status to show "Success" before proceeding with the stack execution.

        If the association status doesn't show "Success" after the specified number of seconds, then stack creation fails.
        .. epigraph::

           When you specify a value for the ``WaitForSuccessTimeoutSeconds`` , `drift detection <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`_ for your AWS CloudFormation stack’s configuration might yield inaccurate results. If drift detection is important in your scenario, we recommend that you don’t include ``WaitForSuccessTimeoutSeconds`` in your template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-waitforsuccesstimeoutseconds
        '''
        result = self._values.get("wait_for_success_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDocument(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnDocument",
):
    '''The ``AWS::SSM::Document`` resource creates a Systems Manager (SSM) document in AWS Systems Manager .

    This document d efines the actions that Systems Manager performs on your AWS resources.
    .. epigraph::

       This resource does not support AWS CloudFormation drift detection.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
    :cloudformationResource: AWS::SSM::Document
    :exampleMetadata: infused

    Example::

        # application: appconfig.Application
        # document: ssm.CfnDocument
        
        
        appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
            application=application,
            location=appconfig.ConfigurationSource.from_cfn_document(document)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        content: typing.Any,
        attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDocument.AttachmentsSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        document_format: typing.Optional[builtins.str] = None,
        document_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        requires: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDocument.DocumentRequiresProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_type: typing.Optional[builtins.str] = None,
        update_method: typing.Optional[builtins.str] = None,
        version_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content: The content for the new SSM document in JSON or YAML. For more information about the schemas for SSM document content, see `SSM document schema features and examples <https://docs.aws.amazon.com/systems-manager/latest/userguide/document-schemas-features.html>`_ in the *AWS Systems Manager User Guide* . .. epigraph:: This parameter also supports ``String`` data types.
        :param attachments: A list of key-value pairs that describe attachments to a version of a document.
        :param document_format: Specify the document format for the request. ``JSON`` is the default format. Default: - "JSON"
        :param document_type: The type of document to create.
        :param name: A name for the SSM document. .. epigraph:: You can't use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes: - ``aws`` - ``amazon`` - ``amzn`` - ``AWSEC2`` - ``AWSConfigRemediation`` - ``AWSSupport``
        :param requires: A list of SSM documents required by a document. This parameter is used exclusively by AWS AppConfig . When a user creates an AWS AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an ``ApplicationConfiguration`` document requires an ``ApplicationConfigurationSchema`` document for validation purposes. For more information, see `What is AWS AppConfig ? <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .
        :param tags: AWS CloudFormation resource tags to apply to the document. Use tags to help you identify and categorize resources.
        :param target_type: Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: ``/AWS::EC2::Instance`` . If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see `AWS resource and property types reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ in the *AWS CloudFormation User Guide* .
        :param update_method: If the document resource you specify in your template already exists, this parameter determines whether a new version of the existing document is created, or the existing document is replaced. ``Replace`` is the default method. If you specify ``NewVersion`` for the ``UpdateMethod`` parameter, and the ``Name`` of the document does not match an existing resource, a new document is created. When you specify ``NewVersion`` , the default version of the document is changed to the newly created version. Default: - "Replace"
        :param version_name: An optional field specifying the version of the artifact you are creating with the document. For example, ``Release12.1`` . This value is unique across all versions of a document, and can't be changed.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d0587e99b7ec516726ff27f1c34b1714d8645ad06944d59be27a612537ddab2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDocumentProps(
            content=content,
            attachments=attachments,
            document_format=document_format,
            document_type=document_type,
            name=name,
            requires=requires,
            tags=tags,
            target_type=target_type,
            update_method=update_method,
            version_name=version_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e943c2273ff892e2fdd4d583a1890854bb12dbd590854b62347e2fa9562d5a14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2188ce8a82f6b6d9f8be3fad6fa91e030961fe82ccfc50ea9018eb0ca9a5568f)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> typing.Any:
        '''The content for the new SSM document in JSON or YAML.'''
        return typing.cast(typing.Any, jsii.get(self, "content"))

    @content.setter
    def content(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5959ba776c476fbcff87b818558733698ac254ec78c13e966dec8b6d890dba49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="attachments")
    def attachments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDocument.AttachmentsSourceProperty"]]]]:
        '''A list of key-value pairs that describe attachments to a version of a document.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDocument.AttachmentsSourceProperty"]]]], jsii.get(self, "attachments"))

    @attachments.setter
    def attachments(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDocument.AttachmentsSourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__175aeee83820e4c740052899af41bd6da137e36dc8a7c97e1979f2a38dfb8ad5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachments", value)

    @builtins.property
    @jsii.member(jsii_name="documentFormat")
    def document_format(self) -> typing.Optional[builtins.str]:
        '''Specify the document format for the request.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentFormat"))

    @document_format.setter
    def document_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d78f0fc9dc92bbdeda2dcfc1e140d76d56dba997674014f72aaf4c862bf73256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentFormat", value)

    @builtins.property
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> typing.Optional[builtins.str]:
        '''The type of document to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentType"))

    @document_type.setter
    def document_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1470169f5980c3b4dc4cbba07fd16d25490957e1af4df9aaa44a046e8043856f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the SSM document.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b1ce30b81e0af0ed907c214243ea20a6ec6304887e3dd6da9e7f40c535dfd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="requires")
    def requires(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDocument.DocumentRequiresProperty"]]]]:
        '''A list of SSM documents required by a document.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDocument.DocumentRequiresProperty"]]]], jsii.get(self, "requires"))

    @requires.setter
    def requires(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDocument.DocumentRequiresProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f21e2047334ed6671ad1892afe1b670d99e12c8d4d4404c82dc71a489c595d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requires", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''AWS CloudFormation resource tags to apply to the document.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__562d6c2a06cbb316f503d8b64a06c9f80424782257db2c710c729b1f8466d90f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> typing.Optional[builtins.str]:
        '''Specify a target type to define the kinds of resources the document can run on.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05561a31234b57ff868b8ce303562a7ae870c3d8d67ddf5a4937ba4df268d903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)

    @builtins.property
    @jsii.member(jsii_name="updateMethod")
    def update_method(self) -> typing.Optional[builtins.str]:
        '''If the document resource you specify in your template already exists, this parameter determines whether a new version of the existing document is created, or the existing document is replaced.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateMethod"))

    @update_method.setter
    def update_method(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02ecd7f9b655f49b73ab05cdb2e63068bb0cb928f2b663d4563fb23457450917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateMethod", value)

    @builtins.property
    @jsii.member(jsii_name="versionName")
    def version_name(self) -> typing.Optional[builtins.str]:
        '''An optional field specifying the version of the artifact you are creating with the document.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionName"))

    @version_name.setter
    def version_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa50c9cd05e6bdac375dbcdf81332154e8628548ba5da12e0a6064a42b8587d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnDocument.AttachmentsSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "name": "name", "values": "values"},
    )
    class AttachmentsSourceProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Identifying information about a document attachment, including the file name and a key-value pair that identifies the location of an attachment to a document.

            :param key: The key of a key-value pair that identifies the location of an attachment to a document.
            :param name: The name of the document attachment file.
            :param values: The value of a key-value pair that identifies the location of an attachment to a document. The format for *Value* depends on the type of key you specify. - For the key *SourceUrl* , the value is an S3 bucket location. For example: ``"Values": [ "s3://doc-example-bucket/my-folder" ]`` - For the key *S3FileUrl* , the value is a file in an S3 bucket. For example: ``"Values": [ "s3://doc-example-bucket/my-folder/my-file.py" ]`` - For the key *AttachmentReference* , the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example: ``"Values": [ "MyOtherDocument/3/my-other-file.py" ]`` However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example: ``"Values": [ "arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py" ]``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                attachments_source_property = ssm.CfnDocument.AttachmentsSourceProperty(
                    key="key",
                    name="name",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5af3bdb71c8069e4c4385fdecf788d6f19e9cf5a960b1f847f9e68fa3bc0bd8c)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if name is not None:
                self._values["name"] = name
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key of a key-value pair that identifies the location of an attachment to a document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the document attachment file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The value of a key-value pair that identifies the location of an attachment to a document.

            The format for *Value* depends on the type of key you specify.

            - For the key *SourceUrl* , the value is an S3 bucket location. For example:

            ``"Values": [ "s3://doc-example-bucket/my-folder" ]``

            - For the key *S3FileUrl* , the value is a file in an S3 bucket. For example:

            ``"Values": [ "s3://doc-example-bucket/my-folder/my-file.py" ]``

            - For the key *AttachmentReference* , the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example:

            ``"Values": [ "MyOtherDocument/3/my-other-file.py" ]``

            However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example:

            ``"Values": [ "arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py" ]``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttachmentsSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnDocument.DocumentRequiresProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class DocumentRequiresProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An SSM document required by the current document.

            :param name: The name of the required SSM document. The name can be an Amazon Resource Name (ARN).
            :param version: The document version required by the current document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                document_requires_property = ssm.CfnDocument.DocumentRequiresProperty(
                    name="name",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aef1956d3e7560ca3d8bf2295207e843bbdd851217757941ff4d603fe26e3ceb)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the required SSM document.

            The name can be an Amazon Resource Name (ARN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html#cfn-ssm-document-documentrequires-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The document version required by the current document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html#cfn-ssm-document-documentrequires-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentRequiresProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnDocumentProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "attachments": "attachments",
        "document_format": "documentFormat",
        "document_type": "documentType",
        "name": "name",
        "requires": "requires",
        "tags": "tags",
        "target_type": "targetType",
        "update_method": "updateMethod",
        "version_name": "versionName",
    },
)
class CfnDocumentProps:
    def __init__(
        self,
        *,
        content: typing.Any,
        attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocument.AttachmentsSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        document_format: typing.Optional[builtins.str] = None,
        document_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        requires: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocument.DocumentRequiresProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_type: typing.Optional[builtins.str] = None,
        update_method: typing.Optional[builtins.str] = None,
        version_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDocument``.

        :param content: The content for the new SSM document in JSON or YAML. For more information about the schemas for SSM document content, see `SSM document schema features and examples <https://docs.aws.amazon.com/systems-manager/latest/userguide/document-schemas-features.html>`_ in the *AWS Systems Manager User Guide* . .. epigraph:: This parameter also supports ``String`` data types.
        :param attachments: A list of key-value pairs that describe attachments to a version of a document.
        :param document_format: Specify the document format for the request. ``JSON`` is the default format. Default: - "JSON"
        :param document_type: The type of document to create.
        :param name: A name for the SSM document. .. epigraph:: You can't use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes: - ``aws`` - ``amazon`` - ``amzn`` - ``AWSEC2`` - ``AWSConfigRemediation`` - ``AWSSupport``
        :param requires: A list of SSM documents required by a document. This parameter is used exclusively by AWS AppConfig . When a user creates an AWS AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an ``ApplicationConfiguration`` document requires an ``ApplicationConfigurationSchema`` document for validation purposes. For more information, see `What is AWS AppConfig ? <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .
        :param tags: AWS CloudFormation resource tags to apply to the document. Use tags to help you identify and categorize resources.
        :param target_type: Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: ``/AWS::EC2::Instance`` . If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see `AWS resource and property types reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ in the *AWS CloudFormation User Guide* .
        :param update_method: If the document resource you specify in your template already exists, this parameter determines whether a new version of the existing document is created, or the existing document is replaced. ``Replace`` is the default method. If you specify ``NewVersion`` for the ``UpdateMethod`` parameter, and the ``Name`` of the document does not match an existing resource, a new document is created. When you specify ``NewVersion`` , the default version of the document is changed to the newly created version. Default: - "Replace"
        :param version_name: An optional field specifying the version of the artifact you are creating with the document. For example, ``Release12.1`` . This value is unique across all versions of a document, and can't be changed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            # content: Any
            
            cfn_document_props = ssm.CfnDocumentProps(
                content=content,
            
                # the properties below are optional
                attachments=[ssm.CfnDocument.AttachmentsSourceProperty(
                    key="key",
                    name="name",
                    values=["values"]
                )],
                document_format="documentFormat",
                document_type="documentType",
                name="name",
                requires=[ssm.CfnDocument.DocumentRequiresProperty(
                    name="name",
                    version="version"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_type="targetType",
                update_method="updateMethod",
                version_name="versionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25566dec89d0b8b9f0c9ebb93fd7f63988acea14deb943fd94cfe89a3d03a14a)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument attachments", value=attachments, expected_type=type_hints["attachments"])
            check_type(argname="argument document_format", value=document_format, expected_type=type_hints["document_format"])
            check_type(argname="argument document_type", value=document_type, expected_type=type_hints["document_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument requires", value=requires, expected_type=type_hints["requires"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument update_method", value=update_method, expected_type=type_hints["update_method"])
            check_type(argname="argument version_name", value=version_name, expected_type=type_hints["version_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
        }
        if attachments is not None:
            self._values["attachments"] = attachments
        if document_format is not None:
            self._values["document_format"] = document_format
        if document_type is not None:
            self._values["document_type"] = document_type
        if name is not None:
            self._values["name"] = name
        if requires is not None:
            self._values["requires"] = requires
        if tags is not None:
            self._values["tags"] = tags
        if target_type is not None:
            self._values["target_type"] = target_type
        if update_method is not None:
            self._values["update_method"] = update_method
        if version_name is not None:
            self._values["version_name"] = version_name

    @builtins.property
    def content(self) -> typing.Any:
        '''The content for the new SSM document in JSON or YAML.

        For more information about the schemas for SSM document content, see `SSM document schema features and examples <https://docs.aws.amazon.com/systems-manager/latest/userguide/document-schemas-features.html>`_ in the *AWS Systems Manager User Guide* .
        .. epigraph::

           This parameter also supports ``String`` data types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def attachments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDocument.AttachmentsSourceProperty]]]]:
        '''A list of key-value pairs that describe attachments to a version of a document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-attachments
        '''
        result = self._values.get("attachments")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDocument.AttachmentsSourceProperty]]]], result)

    @builtins.property
    def document_format(self) -> typing.Optional[builtins.str]:
        '''Specify the document format for the request.

        ``JSON`` is the default format.

        :default: - "JSON"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documentformat
        '''
        result = self._values.get("document_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_type(self) -> typing.Optional[builtins.str]:
        '''The type of document to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documenttype
        '''
        result = self._values.get("document_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the SSM document.

        .. epigraph::

           You can't use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes:

           - ``aws``
           - ``amazon``
           - ``amzn``
           - ``AWSEC2``
           - ``AWSConfigRemediation``
           - ``AWSSupport``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requires(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDocument.DocumentRequiresProperty]]]]:
        '''A list of SSM documents required by a document.

        This parameter is used exclusively by AWS AppConfig . When a user creates an AWS AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an ``ApplicationConfiguration`` document requires an ``ApplicationConfigurationSchema`` document for validation purposes. For more information, see `What is AWS AppConfig ? <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-requires
        '''
        result = self._values.get("requires")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDocument.DocumentRequiresProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''AWS CloudFormation resource tags to apply to the document.

        Use tags to help you identify and categorize resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def target_type(self) -> typing.Optional[builtins.str]:
        '''Specify a target type to define the kinds of resources the document can run on.

        For example, to run a document on EC2 instances, specify the following value: ``/AWS::EC2::Instance`` . If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see `AWS resource and property types reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ in the *AWS CloudFormation User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-targettype
        '''
        result = self._values.get("target_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_method(self) -> typing.Optional[builtins.str]:
        '''If the document resource you specify in your template already exists, this parameter determines whether a new version of the existing document is created, or the existing document is replaced.

        ``Replace`` is the default method. If you specify ``NewVersion`` for the ``UpdateMethod`` parameter, and the ``Name`` of the document does not match an existing resource, a new document is created. When you specify ``NewVersion`` , the default version of the document is changed to the newly created version.

        :default: - "Replace"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-updatemethod
        '''
        result = self._values.get("update_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_name(self) -> typing.Optional[builtins.str]:
        '''An optional field specifying the version of the artifact you are creating with the document.

        For example, ``Release12.1`` . This value is unique across all versions of a document, and can't be changed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-versionname
        '''
        result = self._values.get("version_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMaintenanceWindow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindow",
):
    '''The ``AWS::SSM::MaintenanceWindow`` resource represents general information about a maintenance window for AWS Systems Manager .

    Maintenance windows let you define a schedule for when to perform potentially disruptive actions on your instances, such as patching an operating system (OS), updating drivers, or installing software. Each maintenance window has a schedule, a duration, a set of registered targets, and a set of registered tasks.

    For more information, see `Systems Manager Maintenance Windows <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html>`_ in the *AWS Systems Manager User Guide* and `CreateMaintenanceWindow <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateMaintenanceWindow.html>`_ in the *AWS Systems Manager API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
    :cloudformationResource: AWS::SSM::MaintenanceWindow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_maintenance_window = ssm.CfnMaintenanceWindow(self, "MyCfnMaintenanceWindow",
            allow_unassociated_targets=False,
            cutoff=123,
            duration=123,
            name="name",
            schedule="schedule",
        
            # the properties below are optional
            description="description",
            end_date="endDate",
            schedule_offset=123,
            schedule_timezone="scheduleTimezone",
            start_date="startDate",
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
        allow_unassociated_targets: typing.Union[builtins.bool, _IResolvable_da3f097b],
        cutoff: jsii.Number,
        duration: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param allow_unassociated_targets: Enables a maintenance window task to run on managed instances, even if you have not registered those instances as targets. If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the maintenance window.
        :param cutoff: The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
        :param duration: The duration of the maintenance window in hours.
        :param name: The name of the maintenance window.
        :param schedule: The schedule of the maintenance window in the form of a cron or rate expression.
        :param description: A description of the maintenance window.
        :param end_date: The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.
        :param schedule_offset: The number of days to wait to run a maintenance window after the scheduled cron expression date and time.
        :param schedule_timezone: The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.
        :param start_date: The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. ``StartDate`` allows you to delay activation of the maintenance window until the specified future date.
        :param tags: Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad1b2a4216045934da690d96bf97784e2924381a651333920a48e8bccaa28bed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMaintenanceWindowProps(
            allow_unassociated_targets=allow_unassociated_targets,
            cutoff=cutoff,
            duration=duration,
            name=name,
            schedule=schedule,
            description=description,
            end_date=end_date,
            schedule_offset=schedule_offset,
            schedule_timezone=schedule_timezone,
            start_date=start_date,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baf2d9bcb608aa3fdea2507f7b28a1b89f11d7986467106d573d646ed1bd6c09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__02e48a97af13ee9ec2b735682801a3c97b65f0385eaa8f17565b7437c7d55503)
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
    @jsii.member(jsii_name="allowUnassociatedTargets")
    def allow_unassociated_targets(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Enables a maintenance window task to run on managed instances, even if you have not registered those instances as targets.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "allowUnassociatedTargets"))

    @allow_unassociated_targets.setter
    def allow_unassociated_targets(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b59de04623e80b94c25e028af2976d77afe2bc536f6dd59cd55cec25843686a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowUnassociatedTargets", value)

    @builtins.property
    @jsii.member(jsii_name="cutoff")
    def cutoff(self) -> jsii.Number:
        '''The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.'''
        return typing.cast(jsii.Number, jsii.get(self, "cutoff"))

    @cutoff.setter
    def cutoff(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d56bec4e39b855ff10336eb33b0d79cd1e1176cf1b7f78e5e405719c4eca1f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cutoff", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        '''The duration of the maintenance window in hours.'''
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b5c28ccb571d4df4caa3b264761f43b63e629207366a74c8d3f485171df3bc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the maintenance window.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__995c29377559e15e0f1c56e36005d64d6364a914f20d79cfc82b5914d73bd876)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        '''The schedule of the maintenance window in the form of a cron or rate expression.'''
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f38a694c05ce44a00d9222454ce9730a88ab55b543178b87550f611fa66317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the maintenance window.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28aeaf50f7690fe17faf3319ac5908dca8bb57fac700b1295b0de46996a76ff3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endDate"))

    @end_date.setter
    def end_date(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96bd2ef248cf8835b029f6a8d83774b266650f228ec191067204d5eef38b6d70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endDate", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleOffset")
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''The number of days to wait to run a maintenance window after the scheduled cron expression date and time.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scheduleOffset"))

    @schedule_offset.setter
    def schedule_offset(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e109a6d18454ed60fdaa5c9f3665397d813614a627e51216d6a6c4c328f703a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleOffset", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleTimezone")
    def schedule_timezone(self) -> typing.Optional[builtins.str]:
        '''The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleTimezone"))

    @schedule_timezone.setter
    def schedule_timezone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8759638f42d7bafe21e1d7ac7c933693408b493eb89b2e82e61fb4407805b0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startDate"))

    @start_date.setter
    def start_date(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a011b6550ec143adc25e489b9d0cd4d88120fed5047ded6ab0b4191dcda41f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startDate", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs).'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff8aedf9ec0e769950717671246b7841aefbc47689520e9925ec90bc7e70a148)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowProps",
    jsii_struct_bases=[],
    name_mapping={
        "allow_unassociated_targets": "allowUnassociatedTargets",
        "cutoff": "cutoff",
        "duration": "duration",
        "name": "name",
        "schedule": "schedule",
        "description": "description",
        "end_date": "endDate",
        "schedule_offset": "scheduleOffset",
        "schedule_timezone": "scheduleTimezone",
        "start_date": "startDate",
        "tags": "tags",
    },
)
class CfnMaintenanceWindowProps:
    def __init__(
        self,
        *,
        allow_unassociated_targets: typing.Union[builtins.bool, _IResolvable_da3f097b],
        cutoff: jsii.Number,
        duration: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMaintenanceWindow``.

        :param allow_unassociated_targets: Enables a maintenance window task to run on managed instances, even if you have not registered those instances as targets. If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the maintenance window.
        :param cutoff: The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
        :param duration: The duration of the maintenance window in hours.
        :param name: The name of the maintenance window.
        :param schedule: The schedule of the maintenance window in the form of a cron or rate expression.
        :param description: A description of the maintenance window.
        :param end_date: The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.
        :param schedule_offset: The number of days to wait to run a maintenance window after the scheduled cron expression date and time.
        :param schedule_timezone: The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.
        :param start_date: The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. ``StartDate`` allows you to delay activation of the maintenance window until the specified future date.
        :param tags: Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_maintenance_window_props = ssm.CfnMaintenanceWindowProps(
                allow_unassociated_targets=False,
                cutoff=123,
                duration=123,
                name="name",
                schedule="schedule",
            
                # the properties below are optional
                description="description",
                end_date="endDate",
                schedule_offset=123,
                schedule_timezone="scheduleTimezone",
                start_date="startDate",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e76d52f884f4303547d94985493397dbda06375d2fb22bef09cd893b8126578e)
            check_type(argname="argument allow_unassociated_targets", value=allow_unassociated_targets, expected_type=type_hints["allow_unassociated_targets"])
            check_type(argname="argument cutoff", value=cutoff, expected_type=type_hints["cutoff"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
            check_type(argname="argument schedule_offset", value=schedule_offset, expected_type=type_hints["schedule_offset"])
            check_type(argname="argument schedule_timezone", value=schedule_timezone, expected_type=type_hints["schedule_timezone"])
            check_type(argname="argument start_date", value=start_date, expected_type=type_hints["start_date"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allow_unassociated_targets": allow_unassociated_targets,
            "cutoff": cutoff,
            "duration": duration,
            "name": name,
            "schedule": schedule,
        }
        if description is not None:
            self._values["description"] = description
        if end_date is not None:
            self._values["end_date"] = end_date
        if schedule_offset is not None:
            self._values["schedule_offset"] = schedule_offset
        if schedule_timezone is not None:
            self._values["schedule_timezone"] = schedule_timezone
        if start_date is not None:
            self._values["start_date"] = start_date
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def allow_unassociated_targets(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Enables a maintenance window task to run on managed instances, even if you have not registered those instances as targets.

        If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-allowunassociatedtargets
        '''
        result = self._values.get("allow_unassociated_targets")
        assert result is not None, "Required property 'allow_unassociated_targets' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def cutoff(self) -> jsii.Number:
        '''The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-cutoff
        '''
        result = self._values.get("cutoff")
        assert result is not None, "Required property 'cutoff' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def duration(self) -> jsii.Number:
        '''The duration of the maintenance window in hours.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-duration
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> builtins.str:
        '''The schedule of the maintenance window in the form of a cron or rate expression.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-enddate
        '''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''The number of days to wait to run a maintenance window after the scheduled cron expression date and time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduleoffset
        '''
        result = self._values.get("schedule_offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schedule_timezone(self) -> typing.Optional[builtins.str]:
        '''The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduletimezone
        '''
        result = self._values.get("schedule_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active.

        ``StartDate`` allows you to delay activation of the maintenance window until the specified future date.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-startdate
        '''
        result = self._values.get("start_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs).

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaintenanceWindowTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTarget",
):
    '''The ``AWS::SSM::MaintenanceWindowTarget`` resource registers a target with a maintenance window for AWS Systems Manager .

    For more information, see `RegisterTargetWithMaintenanceWindow <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterTargetWithMaintenanceWindow.html>`_ in the *AWS Systems Manager API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
    :cloudformationResource: AWS::SSM::MaintenanceWindowTarget
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_maintenance_window_target = ssm.CfnMaintenanceWindowTarget(self, "MyCfnMaintenanceWindowTarget",
            resource_type="resourceType",
            targets=[ssm.CfnMaintenanceWindowTarget.TargetsProperty(
                key="key",
                values=["values"]
            )],
            window_id="windowId",
        
            # the properties below are optional
            description="description",
            name="name",
            owner_information="ownerInformation"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_type: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", typing.Dict[builtins.str, typing.Any]]]]],
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_information: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_type: The type of target that is being registered with the maintenance window.
        :param targets: The targets to register with the maintenance window. In other words, the instances to run commands on when the maintenance window runs. You must specify targets by using the ``WindowTargetIds`` parameter.
        :param window_id: The ID of the maintenance window to register the target with.
        :param description: A description for the target.
        :param name: The name for the maintenance window target.
        :param owner_information: A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2179f5bf9c66eb25232096c54c2b6db2fe7f605be13acfcdbc1bae1e8a27cf5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMaintenanceWindowTargetProps(
            resource_type=resource_type,
            targets=targets,
            window_id=window_id,
            description=description,
            name=name,
            owner_information=owner_information,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f471a86408fc354ec99155aa301b1a033e814a122604764e6b408635b1277b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a50ede4d01d25c69fe012a9b8cbe9ca79f322d9e3381d509a9e366d6e5f8b21f)
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
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The type of target that is being registered with the maintenance window.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a13388269754c40d63f1299c7452e64c78999e96e3c4e045f5b0d2e28a6a50d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTarget.TargetsProperty"]]]:
        '''The targets to register with the maintenance window.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTarget.TargetsProperty"]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTarget.TargetsProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__803208e9f40c4e62295f82d8ba5e2943d3dba56d9a7f29d414b3e56f6b4ffdb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @builtins.property
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        '''The ID of the maintenance window to register the target with.'''
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f880c1d4dc9c35b640f583b5a1eae791d6b9aba785b421257fce0c13f84f94ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd052b26378460dad14d691180cd79953a8b934b32bf7c740b62447530a2480b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the maintenance window target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b12333ebaf74b7018641702cfa3157bc7e93dd94bce92bbf2ba08eb43c2e47c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ownerInformation")
    def owner_information(self) -> typing.Optional[builtins.str]:
        '''A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInformation"))

    @owner_information.setter
    def owner_information(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7edbe00367604f6dbbbf871d14ab1b0b6484dc2ec9985bdff2795cb5d1183d4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerInformation", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTarget.TargetsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetsProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The ``Targets`` property type specifies adding a target to a maintenance window target in AWS Systems Manager .

            ``Targets`` is a property of the `AWS::SSM::MaintenanceWindowTarget <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html>`_ resource.

            :param key: User-defined criteria for sending commands that target managed nodes that meet the criteria.
            :param values: User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include EC2 tags of ``ServerRole,WebServer`` . Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                targets_property = ssm.CfnMaintenanceWindowTarget.TargetsProperty(
                    key="key",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f385d4e9e8ebe3c37486729db165f1ed4064a2d660f424ea0550addace9d949)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''User-defined criteria for sending commands that target managed nodes that meet the criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''User-defined criteria that maps to ``Key`` .

            For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include EC2 tags of ``ServerRole,WebServer`` .

            Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_type": "resourceType",
        "targets": "targets",
        "window_id": "windowId",
        "description": "description",
        "name": "name",
        "owner_information": "ownerInformation",
    },
)
class CfnMaintenanceWindowTargetProps:
    def __init__(
        self,
        *,
        resource_type: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, typing.Dict[builtins.str, typing.Any]]]]],
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_information: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMaintenanceWindowTarget``.

        :param resource_type: The type of target that is being registered with the maintenance window.
        :param targets: The targets to register with the maintenance window. In other words, the instances to run commands on when the maintenance window runs. You must specify targets by using the ``WindowTargetIds`` parameter.
        :param window_id: The ID of the maintenance window to register the target with.
        :param description: A description for the target.
        :param name: The name for the maintenance window target.
        :param owner_information: A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_maintenance_window_target_props = ssm.CfnMaintenanceWindowTargetProps(
                resource_type="resourceType",
                targets=[ssm.CfnMaintenanceWindowTarget.TargetsProperty(
                    key="key",
                    values=["values"]
                )],
                window_id="windowId",
            
                # the properties below are optional
                description="description",
                name="name",
                owner_information="ownerInformation"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f19925b4e71098d1d7c3ce4f156f1dd7af4f0d2c164edb55bdbb1bc8cefb0b22)
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument window_id", value=window_id, expected_type=type_hints["window_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument owner_information", value=owner_information, expected_type=type_hints["owner_information"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_type": resource_type,
            "targets": targets,
            "window_id": window_id,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if owner_information is not None:
            self._values["owner_information"] = owner_information

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The type of target that is being registered with the maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTarget.TargetsProperty]]]:
        '''The targets to register with the maintenance window.

        In other words, the instances to run commands on when the maintenance window runs.

        You must specify targets by using the ``WindowTargetIds`` parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTarget.TargetsProperty]]], result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''The ID of the maintenance window to register the target with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-windowid
        '''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the maintenance window target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_information(self) -> typing.Optional[builtins.str]:
        '''A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-ownerinformation
        '''
        result = self._values.get("owner_information")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaintenanceWindowTask(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask",
):
    '''The ``AWS::SSM::MaintenanceWindowTask`` resource defines information about a task for an AWS Systems Manager maintenance window.

    For more information, see `RegisterTaskWithMaintenanceWindow <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterTaskWithMaintenanceWindow.html>`_ in the *AWS Systems Manager API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
    :cloudformationResource: AWS::SSM::MaintenanceWindowTask
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        # parameters: Any
        # task_parameters: Any
        
        cfn_maintenance_window_task = ssm.CfnMaintenanceWindowTask(self, "MyCfnMaintenanceWindowTask",
            priority=123,
            task_arn="taskArn",
            task_type="taskType",
            window_id="windowId",
        
            # the properties below are optional
            cutoff_behavior="cutoffBehavior",
            description="description",
            logging_info=ssm.CfnMaintenanceWindowTask.LoggingInfoProperty(
                region="region",
                s3_bucket="s3Bucket",
        
                # the properties below are optional
                s3_prefix="s3Prefix"
            ),
            max_concurrency="maxConcurrency",
            max_errors="maxErrors",
            name="name",
            service_role_arn="serviceRoleArn",
            targets=[ssm.CfnMaintenanceWindowTask.TargetProperty(
                key="key",
                values=["values"]
            )],
            task_invocation_parameters=ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty(
                maintenance_window_automation_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty(
                    document_version="documentVersion",
                    parameters=parameters
                ),
                maintenance_window_lambda_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty(
                    client_context="clientContext",
                    payload="payload",
                    qualifier="qualifier"
                ),
                maintenance_window_run_command_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty(
                    cloud_watch_output_config=ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                        cloud_watch_log_group_name="cloudWatchLogGroupName",
                        cloud_watch_output_enabled=False
                    ),
                    comment="comment",
                    document_hash="documentHash",
                    document_hash_type="documentHashType",
                    document_version="documentVersion",
                    notification_config=ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                        notification_arn="notificationArn",
        
                        # the properties below are optional
                        notification_events=["notificationEvents"],
                        notification_type="notificationType"
                    ),
                    output_s3_bucket_name="outputS3BucketName",
                    output_s3_key_prefix="outputS3KeyPrefix",
                    parameters=parameters,
                    service_role_arn="serviceRoleArn",
                    timeout_seconds=123
                ),
                maintenance_window_step_functions_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty(
                    input="input",
                    name="name"
                )
            ),
            task_parameters=task_parameters
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        priority: jsii.Number,
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        cutoff_behavior: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.TargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        task_parameters: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param priority: The priority of the task in the maintenance window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
        :param task_arn: The resource that the task uses during execution. For ``RUN_COMMAND`` and ``AUTOMATION`` task types, ``TaskArn`` is the SSM document name or Amazon Resource Name (ARN). For ``LAMBDA`` tasks, ``TaskArn`` is the function name or ARN. For ``STEP_FUNCTIONS`` tasks, ``TaskArn`` is the state machine ARN.
        :param task_type: The type of task. Valid values: ``RUN_COMMAND`` , ``AUTOMATION`` , ``LAMBDA`` , ``STEP_FUNCTIONS`` .
        :param window_id: The ID of the maintenance window where the task is registered.
        :param cutoff_behavior: The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.
        :param description: A description of the task.
        :param logging_info: Information about an Amazon S3 bucket to write Run Command task-level logs to. .. epigraph:: ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs for Run Command tasks, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS ::SSM::MaintenanceWindowTask MaintenanceWindowRunCommandParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html>`_ .
        :param max_concurrency: The maximum number of targets this task can be run for, in parallel. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases. For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.
        :param max_errors: The maximum number of errors allowed before this task stops being scheduled. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases. For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.
        :param name: The task name.
        :param service_role_arn: The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run ``RegisterTaskWithMaintenanceWindow`` . However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see `Setting up maintenance windows <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html>`_ in the in the *AWS Systems Manager User Guide* .
        :param targets: The targets, either instances or window target IDs. - Specify instances using ``Key=InstanceIds,Values= *instanceid1* , *instanceid2*`` . - Specify window target IDs using ``Key=WindowTargetIds,Values= *window-target-id-1* , *window-target-id-2*`` .
        :param task_invocation_parameters: The parameters to pass to the task when it runs. Populate only the fields that match the task type. All other fields should be empty. .. epigraph:: When you update a maintenance window task that has options specified in ``TaskInvocationParameters`` , you must provide again all the ``TaskInvocationParameters`` values that you want to retain. The values you do not specify again are removed. For example, suppose that when you registered a Run Command task, you specified ``TaskInvocationParameters`` values for ``Comment`` , ``NotificationConfig`` , and ``OutputS3BucketName`` . If you update the maintenance window task and specify only a different ``OutputS3BucketName`` value, the values for ``Comment`` and ``NotificationConfig`` are removed.
        :param task_parameters: The parameters to pass to the task when it runs. .. epigraph:: ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `MaintenanceWindowTaskInvocationParameters <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTaskInvocationParameters.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab957de8d8a36935188de8e7d81d523e1ab1253ec8aab9717d062cb647fc726)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMaintenanceWindowTaskProps(
            priority=priority,
            task_arn=task_arn,
            task_type=task_type,
            window_id=window_id,
            cutoff_behavior=cutoff_behavior,
            description=description,
            logging_info=logging_info,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            name=name,
            service_role_arn=service_role_arn,
            targets=targets,
            task_invocation_parameters=task_invocation_parameters,
            task_parameters=task_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e4d0dade8da18d6c77b051157c365c8b25a5b6997ae831a7a6fc9dc9203061)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eec35f80592307cae2cc9e343334a35f2ed35398df071ffe5e875583ecd86cb3)
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
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''The priority of the task in the maintenance window.'''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0776f1dec28892f4f039655f4bd58dbab218be1a93993a08a46b2b3fee1a05f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="taskArn")
    def task_arn(self) -> builtins.str:
        '''The resource that the task uses during execution.'''
        return typing.cast(builtins.str, jsii.get(self, "taskArn"))

    @task_arn.setter
    def task_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adccf6935c75e32f84ba21008278bed07a786695c2220217c969ece517a13e19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskArn", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        '''The type of task.'''
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e764d7191dd17ad7c6af4e9cf3288e2143c2b9bebf0395428c7823743dc7e4ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        '''The ID of the maintenance window where the task is registered.'''
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4911136cee1564bf01fe47e9aee783650f347033d01719aeec40bbbfa56ab6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowId", value)

    @builtins.property
    @jsii.member(jsii_name="cutoffBehavior")
    def cutoff_behavior(self) -> typing.Optional[builtins.str]:
        '''The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cutoffBehavior"))

    @cutoff_behavior.setter
    def cutoff_behavior(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56747468a672310155a1a7bd35fab9b92e4e9c51a4e0adec7ff48e95da06e65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cutoffBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f65b28dee7cbeaeef25a47438a9bee61026d458be2cbab4f789904d33e0ca84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="loggingInfo")
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.LoggingInfoProperty"]]:
        '''Information about an Amazon S3 bucket to write Run Command task-level logs to.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.LoggingInfoProperty"]], jsii.get(self, "loggingInfo"))

    @logging_info.setter
    def logging_info(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.LoggingInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7420eb69352c5dffbc63903691d96642ddd213905d4bd87088eb40562b6c37b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingInfo", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''The maximum number of targets this task can be run for, in parallel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe2c1e1cc2613320a5ea339c1908852d8fafbd3051c7edda4b2494635526ea55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''The maximum number of errors allowed before this task stops being scheduled.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba4e556931384c4cf77d1adc667d26d5be5fe17ea89e74b7cfd53f51ed9d3d1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxErrors", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The task name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce0290645c39827e48ca0d011a90f954ce1b5035c94f2b2a84769599cd94116a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa12d14b73c4415f857256339d8c9efbbeb6b154b5de888ae2db34a195687f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.TargetProperty"]]]]:
        '''The targets, either instances or window target IDs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.TargetProperty"]]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.TargetProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba1a5fa6e80a94431946dcbb6c59475e65e96ae172de3aac908aa8b1fbbad49c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @builtins.property
    @jsii.member(jsii_name="taskInvocationParameters")
    def task_invocation_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.TaskInvocationParametersProperty"]]:
        '''The parameters to pass to the task when it runs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.TaskInvocationParametersProperty"]], jsii.get(self, "taskInvocationParameters"))

    @task_invocation_parameters.setter
    def task_invocation_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.TaskInvocationParametersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e676346c741943a2f14e79e926c8b5230365f4924b6a9161db3fc3486bab0d22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskInvocationParameters", value)

    @builtins.property
    @jsii.member(jsii_name="taskParameters")
    def task_parameters(self) -> typing.Any:
        '''The parameters to pass to the task when it runs.'''
        return typing.cast(typing.Any, jsii.get(self, "taskParameters"))

    @task_parameters.setter
    def task_parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__308ea737f8a21130dc4ef906e4efbdd26c268158e16c66982b9d8f555370f880)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskParameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_log_group_name": "cloudWatchLogGroupName",
            "cloud_watch_output_enabled": "cloudWatchOutputEnabled",
        },
    )
    class CloudWatchOutputConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_log_group_name: typing.Optional[builtins.str] = None,
            cloud_watch_output_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Configuration options for sending command output to Amazon CloudWatch Logs.

            :param cloud_watch_log_group_name: The name of the CloudWatch Logs log group where you want to send command output. If you don't specify a group name, AWS Systems Manager automatically creates a log group for you. The log group uses the following naming format: ``aws/ssm/ *SystemsManagerDocumentName*``
            :param cloud_watch_output_enabled: Enables Systems Manager to send command output to CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                cloud_watch_output_config_property = ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                    cloud_watch_log_group_name="cloudWatchLogGroupName",
                    cloud_watch_output_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbb39dc4cd39115a407f4e0e21302b4fce66ba760a368fafa0c26eb9621b52ba)
                check_type(argname="argument cloud_watch_log_group_name", value=cloud_watch_log_group_name, expected_type=type_hints["cloud_watch_log_group_name"])
                check_type(argname="argument cloud_watch_output_enabled", value=cloud_watch_output_enabled, expected_type=type_hints["cloud_watch_output_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_log_group_name is not None:
                self._values["cloud_watch_log_group_name"] = cloud_watch_log_group_name
            if cloud_watch_output_enabled is not None:
                self._values["cloud_watch_output_enabled"] = cloud_watch_output_enabled

        @builtins.property
        def cloud_watch_log_group_name(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch Logs log group where you want to send command output.

            If you don't specify a group name, AWS Systems Manager automatically creates a log group for you. The log group uses the following naming format:

            ``aws/ssm/ *SystemsManagerDocumentName*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchloggroupname
            '''
            result = self._values.get("cloud_watch_log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cloud_watch_output_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables Systems Manager to send command output to CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchoutputenabled
            '''
            result = self._values.get("cloud_watch_output_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.LoggingInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "s3_bucket": "s3Bucket",
            "s3_prefix": "s3Prefix",
        },
    )
    class LoggingInfoProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            s3_bucket: builtins.str,
            s3_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LoggingInfo`` property type specifies information about the Amazon S3 bucket to write instance-level logs to.

            ``LoggingInfo`` is a property of the `AWS::SSM::MaintenanceWindowTask <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html>`_ resource.
            .. epigraph::

               ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS ::SSM::MaintenanceWindowTask MaintenanceWindowRunCommandParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html>`_ .

            :param region: The AWS Region where the S3 bucket is located.
            :param s3_bucket: The name of an S3 bucket where execution logs are stored.
            :param s3_prefix: The Amazon S3 bucket subfolder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                logging_info_property = ssm.CfnMaintenanceWindowTask.LoggingInfoProperty(
                    region="region",
                    s3_bucket="s3Bucket",
                
                    # the properties below are optional
                    s3_prefix="s3Prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b0aefccdd3eb793a2d8676899122ea22603064cb2b55d0a5657cc2772cff4aa)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_prefix", value=s3_prefix, expected_type=type_hints["s3_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
                "s3_bucket": s3_bucket,
            }
            if s3_prefix is not None:
                self._values["s3_prefix"] = s3_prefix

        @builtins.property
        def region(self) -> builtins.str:
            '''The AWS Region where the S3 bucket is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The name of an S3 bucket where execution logs are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_prefix(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 bucket subfolder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3prefix
            '''
            result = self._values.get("s3_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_version": "documentVersion",
            "parameters": "parameters",
        },
    )
    class MaintenanceWindowAutomationParametersProperty:
        def __init__(
            self,
            *,
            document_version: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
        ) -> None:
            '''The ``MaintenanceWindowAutomationParameters`` property type specifies the parameters for an ``AUTOMATION`` task type for a maintenance window task in AWS Systems Manager .

            ``MaintenanceWindowAutomationParameters`` is a property of the `TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ property type.

            For information about available parameters in Automation runbooks, you can view the content of the runbook itself in the Systems Manager console. For information, see `View runbook content <https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents-reference-details.html#view-automation-json>`_ in the *AWS Systems Manager User Guide* .

            :param document_version: The version of an Automation runbook to use during task execution.
            :param parameters: The parameters for the ``AUTOMATION`` type task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                # parameters: Any
                
                maintenance_window_automation_parameters_property = ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty(
                    document_version="documentVersion",
                    parameters=parameters
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d47f7c3b4729bc4c5e324a0169340617ced800e35e73c55674ef6d731fbbc0a7)
                check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if document_version is not None:
                self._values["document_version"] = document_version
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''The version of an Automation runbook to use during task execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''The parameters for the ``AUTOMATION`` type task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowAutomationParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_context": "clientContext",
            "payload": "payload",
            "qualifier": "qualifier",
        },
    )
    class MaintenanceWindowLambdaParametersProperty:
        def __init__(
            self,
            *,
            client_context: typing.Optional[builtins.str] = None,
            payload: typing.Optional[builtins.str] = None,
            qualifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``MaintenanceWindowLambdaParameters`` property type specifies the parameters for a ``LAMBDA`` task type for a maintenance window task in AWS Systems Manager .

            ``MaintenanceWindowLambdaParameters`` is a property of the `TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ property type.

            :param client_context: Client-specific information to pass to the AWS Lambda function that you're invoking. You can then use the ``context`` variable to process the client information in your AWS Lambda function.
            :param payload: JSON to provide to your AWS Lambda function as input. .. epigraph:: Although ``Type`` is listed as "String" for this property, the payload content must be formatted as a Base64-encoded binary data object. *Length Constraint:* 4096
            :param qualifier: An AWS Lambda function version or alias name. If you specify a function version, the action uses the qualified function Amazon Resource Name (ARN) to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version that the alias points to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                maintenance_window_lambda_parameters_property = ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty(
                    client_context="clientContext",
                    payload="payload",
                    qualifier="qualifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49f94512f6a22e24e49adf01fdbcf2f071f6443d79613410ed49f6eb9c20b4ea)
                check_type(argname="argument client_context", value=client_context, expected_type=type_hints["client_context"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
                check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if client_context is not None:
                self._values["client_context"] = client_context
            if payload is not None:
                self._values["payload"] = payload
            if qualifier is not None:
                self._values["qualifier"] = qualifier

        @builtins.property
        def client_context(self) -> typing.Optional[builtins.str]:
            '''Client-specific information to pass to the AWS Lambda function that you're invoking.

            You can then use the ``context`` variable to process the client information in your AWS Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-clientcontext
            '''
            result = self._values.get("client_context")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload(self) -> typing.Optional[builtins.str]:
            '''JSON to provide to your AWS Lambda function as input.

            .. epigraph::

               Although ``Type`` is listed as "String" for this property, the payload content must be formatted as a Base64-encoded binary data object.

            *Length Constraint:* 4096

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def qualifier(self) -> typing.Optional[builtins.str]:
            '''An AWS Lambda function version or alias name.

            If you specify a function version, the action uses the qualified function Amazon Resource Name (ARN) to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version that the alias points to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-qualifier
            '''
            result = self._values.get("qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowLambdaParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_output_config": "cloudWatchOutputConfig",
            "comment": "comment",
            "document_hash": "documentHash",
            "document_hash_type": "documentHashType",
            "document_version": "documentVersion",
            "notification_config": "notificationConfig",
            "output_s3_bucket_name": "outputS3BucketName",
            "output_s3_key_prefix": "outputS3KeyPrefix",
            "parameters": "parameters",
            "service_role_arn": "serviceRoleArn",
            "timeout_seconds": "timeoutSeconds",
        },
    )
    class MaintenanceWindowRunCommandParametersProperty:
        def __init__(
            self,
            *,
            cloud_watch_output_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            comment: typing.Optional[builtins.str] = None,
            document_hash: typing.Optional[builtins.str] = None,
            document_hash_type: typing.Optional[builtins.str] = None,
            document_version: typing.Optional[builtins.str] = None,
            notification_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.NotificationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            output_s3_bucket_name: typing.Optional[builtins.str] = None,
            output_s3_key_prefix: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            service_role_arn: typing.Optional[builtins.str] = None,
            timeout_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``MaintenanceWindowRunCommandParameters`` property type specifies the parameters for a ``RUN_COMMAND`` task type for a maintenance window task in AWS Systems Manager .

            This means that these parameters are the same as those for the ``SendCommand`` API call. For more information about ``SendCommand`` parameters, see `SendCommand <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html>`_ in the *AWS Systems Manager API Reference* .

            For information about available parameters in SSM Command documents, you can view the content of the document itself in the Systems Manager console. For information, see `Viewing SSM command document content <https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-ssm-document-content.html>`_ in the *AWS Systems Manager User Guide* .

            ``MaintenanceWindowRunCommandParameters`` is a property of the `TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ property type.

            :param cloud_watch_output_config: Configuration options for sending command output to Amazon CloudWatch Logs.
            :param comment: Information about the command or commands to run.
            :param document_hash: The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
            :param document_hash_type: The SHA-256 or SHA-1 hash type. SHA-1 hashes are deprecated.
            :param document_version: The AWS Systems Manager document (SSM document) version to use in the request. You can specify ``$DEFAULT`` , ``$LATEST`` , or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example: ``--document-version "\\$DEFAULT"`` ``--document-version "\\$LATEST"`` ``--document-version "3"``
            :param notification_config: Configurations for sending notifications about command status changes on a per-managed node basis.
            :param output_s3_bucket_name: The name of the Amazon Simple Storage Service (Amazon S3) bucket.
            :param output_s3_key_prefix: The S3 bucket subfolder.
            :param parameters: The parameters for the ``RUN_COMMAND`` task execution. The supported parameters are the same as those for the ``SendCommand`` API call. For more information, see `SendCommand <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html>`_ in the *AWS Systems Manager API Reference* .
            :param service_role_arn: The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run ``RegisterTaskWithMaintenanceWindow`` . However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see `Setting up maintenance windows <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html>`_ in the in the *AWS Systems Manager User Guide* .
            :param timeout_seconds: If this time is reached and the command hasn't already started running, it doesn't run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                # parameters: Any
                
                maintenance_window_run_command_parameters_property = ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty(
                    cloud_watch_output_config=ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                        cloud_watch_log_group_name="cloudWatchLogGroupName",
                        cloud_watch_output_enabled=False
                    ),
                    comment="comment",
                    document_hash="documentHash",
                    document_hash_type="documentHashType",
                    document_version="documentVersion",
                    notification_config=ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                        notification_arn="notificationArn",
                
                        # the properties below are optional
                        notification_events=["notificationEvents"],
                        notification_type="notificationType"
                    ),
                    output_s3_bucket_name="outputS3BucketName",
                    output_s3_key_prefix="outputS3KeyPrefix",
                    parameters=parameters,
                    service_role_arn="serviceRoleArn",
                    timeout_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4e9c786755609427df5303964986a560cf57e26ca86a0fa4cdb6a67584f7aa01)
                check_type(argname="argument cloud_watch_output_config", value=cloud_watch_output_config, expected_type=type_hints["cloud_watch_output_config"])
                check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
                check_type(argname="argument document_hash", value=document_hash, expected_type=type_hints["document_hash"])
                check_type(argname="argument document_hash_type", value=document_hash_type, expected_type=type_hints["document_hash_type"])
                check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
                check_type(argname="argument notification_config", value=notification_config, expected_type=type_hints["notification_config"])
                check_type(argname="argument output_s3_bucket_name", value=output_s3_bucket_name, expected_type=type_hints["output_s3_bucket_name"])
                check_type(argname="argument output_s3_key_prefix", value=output_s3_key_prefix, expected_type=type_hints["output_s3_key_prefix"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
                check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_output_config is not None:
                self._values["cloud_watch_output_config"] = cloud_watch_output_config
            if comment is not None:
                self._values["comment"] = comment
            if document_hash is not None:
                self._values["document_hash"] = document_hash
            if document_hash_type is not None:
                self._values["document_hash_type"] = document_hash_type
            if document_version is not None:
                self._values["document_version"] = document_version
            if notification_config is not None:
                self._values["notification_config"] = notification_config
            if output_s3_bucket_name is not None:
                self._values["output_s3_bucket_name"] = output_s3_bucket_name
            if output_s3_key_prefix is not None:
                self._values["output_s3_key_prefix"] = output_s3_key_prefix
            if parameters is not None:
                self._values["parameters"] = parameters
            if service_role_arn is not None:
                self._values["service_role_arn"] = service_role_arn
            if timeout_seconds is not None:
                self._values["timeout_seconds"] = timeout_seconds

        @builtins.property
        def cloud_watch_output_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty"]]:
            '''Configuration options for sending command output to Amazon CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-cloudwatchoutputconfig
            '''
            result = self._values.get("cloud_watch_output_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty"]], result)

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            '''Information about the command or commands to run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-comment
            '''
            result = self._values.get("comment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_hash(self) -> typing.Optional[builtins.str]:
            '''The SHA-256 or SHA-1 hash created by the system when the document was created.

            SHA-1 hashes have been deprecated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthash
            '''
            result = self._values.get("document_hash")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_hash_type(self) -> typing.Optional[builtins.str]:
            '''The SHA-256 or SHA-1 hash type.

            SHA-1 hashes are deprecated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthashtype
            '''
            result = self._values.get("document_hash_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''The AWS Systems Manager document (SSM document) version to use in the request.

            You can specify ``$DEFAULT`` , ``$LATEST`` , or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example:

            ``--document-version "\\$DEFAULT"``

            ``--document-version "\\$LATEST"``

            ``--document-version "3"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def notification_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.NotificationConfigProperty"]]:
            '''Configurations for sending notifications about command status changes on a per-managed node basis.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-notificationconfig
            '''
            result = self._values.get("notification_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.NotificationConfigProperty"]], result)

        @builtins.property
        def output_s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon Simple Storage Service (Amazon S3) bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3bucketname
            '''
            result = self._values.get("output_s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 bucket subfolder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3keyprefix
            '''
            result = self._values.get("output_s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''The parameters for the ``RUN_COMMAND`` task execution.

            The supported parameters are the same as those for the ``SendCommand`` API call. For more information, see `SendCommand <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html>`_ in the *AWS Systems Manager API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def service_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task.

            If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run ``RegisterTaskWithMaintenanceWindow`` .

            However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see `Setting up maintenance windows <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html>`_ in the in the *AWS Systems Manager User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-servicerolearn
            '''
            result = self._values.get("service_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_seconds(self) -> typing.Optional[jsii.Number]:
            '''If this time is reached and the command hasn't already started running, it doesn't run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-timeoutseconds
            '''
            result = self._values.get("timeout_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowRunCommandParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"input": "input", "name": "name"},
    )
    class MaintenanceWindowStepFunctionsParametersProperty:
        def __init__(
            self,
            *,
            input: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``MaintenanceWindowStepFunctionsParameters`` property type specifies the parameters for the execution of a ``STEP_FUNCTIONS`` task in a Systems Manager maintenance window.

            ``MaintenanceWindowStepFunctionsParameters`` is a property of the `TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ property type.

            :param input: The inputs for the ``STEP_FUNCTIONS`` task.
            :param name: The name of the ``STEP_FUNCTIONS`` task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                maintenance_window_step_functions_parameters_property = ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty(
                    input="input",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7504990f1dfcd8b7592c3b3b181643afde2c73cc8e80cefa0b86447b9907e340)
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if input is not None:
                self._values["input"] = input
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''The inputs for the ``STEP_FUNCTIONS`` task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the ``STEP_FUNCTIONS`` task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowStepFunctionsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.NotificationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "notification_arn": "notificationArn",
            "notification_events": "notificationEvents",
            "notification_type": "notificationType",
        },
    )
    class NotificationConfigProperty:
        def __init__(
            self,
            *,
            notification_arn: builtins.str,
            notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
            notification_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``NotificationConfig`` property type specifies configurations for sending notifications for a maintenance window task in AWS Systems Manager .

            ``NotificationConfig`` is a property of the `MaintenanceWindowRunCommandParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html>`_ property type.

            :param notification_arn: An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.
            :param notification_events: The different events that you can receive notifications for. These events include the following: ``All`` (events), ``InProgress`` , ``Success`` , ``TimedOut`` , ``Cancelled`` , ``Failed`` . To learn more about these events, see `Configuring Amazon SNS Notifications for AWS Systems Manager <https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html>`_ in the *AWS Systems Manager User Guide* .
            :param notification_type: The notification type. - ``Command`` : Receive notification when the status of a command changes. - ``Invocation`` : For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                notification_config_property = ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                    notification_arn="notificationArn",
                
                    # the properties below are optional
                    notification_events=["notificationEvents"],
                    notification_type="notificationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f52d349a1b5c42894659cd315e4a94c0638dbfb6be76c7ac4ea3af2a1e11f464)
                check_type(argname="argument notification_arn", value=notification_arn, expected_type=type_hints["notification_arn"])
                check_type(argname="argument notification_events", value=notification_events, expected_type=type_hints["notification_events"])
                check_type(argname="argument notification_type", value=notification_type, expected_type=type_hints["notification_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "notification_arn": notification_arn,
            }
            if notification_events is not None:
                self._values["notification_events"] = notification_events
            if notification_type is not None:
                self._values["notification_type"] = notification_type

        @builtins.property
        def notification_arn(self) -> builtins.str:
            '''An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic.

            Run Command pushes notifications about command status changes to this topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationarn
            '''
            result = self._values.get("notification_arn")
            assert result is not None, "Required property 'notification_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def notification_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The different events that you can receive notifications for.

            These events include the following: ``All`` (events), ``InProgress`` , ``Success`` , ``TimedOut`` , ``Cancelled`` , ``Failed`` . To learn more about these events, see `Configuring Amazon SNS Notifications for AWS Systems Manager <https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html>`_ in the *AWS Systems Manager User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationevents
            '''
            result = self._values.get("notification_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def notification_type(self) -> typing.Optional[builtins.str]:
            '''The notification type.

            - ``Command`` : Receive notification when the status of a command changes.
            - ``Invocation`` : For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationtype
            '''
            result = self._values.get("notification_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The ``Target`` property type specifies targets (either instances or window target IDs).

            You specify instances by using ``Key=InstanceIds,Values=< *instanceid1* >,< *instanceid2* >`` . You specify window target IDs using ``Key=WindowTargetIds,Values=< *window-target-id-1* >,< *window-target-id-2* >`` for a maintenance window task in AWS Systems Manager .

            ``Target`` is a property of the `AWS::SSM::MaintenanceWindowTask <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html>`_ property type.
            .. epigraph::

               To use ``resource-groups:Name`` as the key for a maintenance window target, specify the resource group as a ``AWS::SSM::MaintenanceWindowTarget`` type, and use the ``Ref`` function to specify the target for ``AWS::SSM::MaintenanceWindowTask`` . For an example, see *Create a Run Command task that targets instances using a resource group name* in `AWS::SSM::MaintenanceWindowTask Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#aws-resource-ssm-maintenancewindowtask--examples>`_ .

            :param key: User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``InstanceIds`` or ``WindowTargetIds`` . For more information about how to target instances within a maintenance window task, see `About 'register-task-with-maintenance-window' Options and Values <https://docs.aws.amazon.com/systems-manager/latest/userguide/register-tasks-options.html>`_ in the *AWS Systems Manager User Guide* .
            :param values: User-defined criteria that maps to ``Key`` . For example, if you specify ``InstanceIds`` , you can specify ``i-1234567890abcdef0,i-9876543210abcdef0`` to run a command on two EC2 instances. For more information about how to target instances within a maintenance window task, see `About 'register-task-with-maintenance-window' Options and Values <https://docs.aws.amazon.com/systems-manager/latest/userguide/register-tasks-options.html>`_ in the *AWS Systems Manager User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                target_property = ssm.CfnMaintenanceWindowTask.TargetProperty(
                    key="key",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b4f690ce6831bb5a0c842fcfe936ca232781e02d69bf2787636fec601c5bbd4)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''User-defined criteria for sending commands that target instances that meet the criteria.

            ``Key`` can be ``InstanceIds`` or ``WindowTargetIds`` . For more information about how to target instances within a maintenance window task, see `About 'register-task-with-maintenance-window' Options and Values <https://docs.aws.amazon.com/systems-manager/latest/userguide/register-tasks-options.html>`_ in the *AWS Systems Manager User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''User-defined criteria that maps to ``Key`` .

            For example, if you specify ``InstanceIds`` , you can specify ``i-1234567890abcdef0,i-9876543210abcdef0`` to run a command on two EC2 instances. For more information about how to target instances within a maintenance window task, see `About 'register-task-with-maintenance-window' Options and Values <https://docs.aws.amazon.com/systems-manager/latest/userguide/register-tasks-options.html>`_ in the *AWS Systems Manager User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maintenance_window_automation_parameters": "maintenanceWindowAutomationParameters",
            "maintenance_window_lambda_parameters": "maintenanceWindowLambdaParameters",
            "maintenance_window_run_command_parameters": "maintenanceWindowRunCommandParameters",
            "maintenance_window_step_functions_parameters": "maintenanceWindowStepFunctionsParameters",
        },
    )
    class TaskInvocationParametersProperty:
        def __init__(
            self,
            *,
            maintenance_window_automation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maintenance_window_lambda_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maintenance_window_run_command_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maintenance_window_step_functions_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``TaskInvocationParameters`` property type specifies the task execution parameters for a maintenance window task in AWS Systems Manager .

            ``TaskInvocationParameters`` is a property of the `AWS::SSM::MaintenanceWindowTask <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html>`_ property type.

            :param maintenance_window_automation_parameters: The parameters for an ``AUTOMATION`` task type.
            :param maintenance_window_lambda_parameters: The parameters for a ``LAMBDA`` task type.
            :param maintenance_window_run_command_parameters: The parameters for a ``RUN_COMMAND`` task type.
            :param maintenance_window_step_functions_parameters: The parameters for a ``STEP_FUNCTIONS`` task type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                # parameters: Any
                
                task_invocation_parameters_property = ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty(
                    maintenance_window_automation_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty(
                        document_version="documentVersion",
                        parameters=parameters
                    ),
                    maintenance_window_lambda_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty(
                        client_context="clientContext",
                        payload="payload",
                        qualifier="qualifier"
                    ),
                    maintenance_window_run_command_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty(
                        cloud_watch_output_config=ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                            cloud_watch_log_group_name="cloudWatchLogGroupName",
                            cloud_watch_output_enabled=False
                        ),
                        comment="comment",
                        document_hash="documentHash",
                        document_hash_type="documentHashType",
                        document_version="documentVersion",
                        notification_config=ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                            notification_arn="notificationArn",
                
                            # the properties below are optional
                            notification_events=["notificationEvents"],
                            notification_type="notificationType"
                        ),
                        output_s3_bucket_name="outputS3BucketName",
                        output_s3_key_prefix="outputS3KeyPrefix",
                        parameters=parameters,
                        service_role_arn="serviceRoleArn",
                        timeout_seconds=123
                    ),
                    maintenance_window_step_functions_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty(
                        input="input",
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6c4d0f27b97034ab166224c30178c332f8ccc78c97088665138b97e1125dbc23)
                check_type(argname="argument maintenance_window_automation_parameters", value=maintenance_window_automation_parameters, expected_type=type_hints["maintenance_window_automation_parameters"])
                check_type(argname="argument maintenance_window_lambda_parameters", value=maintenance_window_lambda_parameters, expected_type=type_hints["maintenance_window_lambda_parameters"])
                check_type(argname="argument maintenance_window_run_command_parameters", value=maintenance_window_run_command_parameters, expected_type=type_hints["maintenance_window_run_command_parameters"])
                check_type(argname="argument maintenance_window_step_functions_parameters", value=maintenance_window_step_functions_parameters, expected_type=type_hints["maintenance_window_step_functions_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if maintenance_window_automation_parameters is not None:
                self._values["maintenance_window_automation_parameters"] = maintenance_window_automation_parameters
            if maintenance_window_lambda_parameters is not None:
                self._values["maintenance_window_lambda_parameters"] = maintenance_window_lambda_parameters
            if maintenance_window_run_command_parameters is not None:
                self._values["maintenance_window_run_command_parameters"] = maintenance_window_run_command_parameters
            if maintenance_window_step_functions_parameters is not None:
                self._values["maintenance_window_step_functions_parameters"] = maintenance_window_step_functions_parameters

        @builtins.property
        def maintenance_window_automation_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty"]]:
            '''The parameters for an ``AUTOMATION`` task type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowautomationparameters
            '''
            result = self._values.get("maintenance_window_automation_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty"]], result)

        @builtins.property
        def maintenance_window_lambda_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty"]]:
            '''The parameters for a ``LAMBDA`` task type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowlambdaparameters
            '''
            result = self._values.get("maintenance_window_lambda_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty"]], result)

        @builtins.property
        def maintenance_window_run_command_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty"]]:
            '''The parameters for a ``RUN_COMMAND`` task type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowruncommandparameters
            '''
            result = self._values.get("maintenance_window_run_command_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty"]], result)

        @builtins.property
        def maintenance_window_step_functions_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty"]]:
            '''The parameters for a ``STEP_FUNCTIONS`` task type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowstepfunctionsparameters
            '''
            result = self._values.get("maintenance_window_step_functions_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskInvocationParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "priority": "priority",
        "task_arn": "taskArn",
        "task_type": "taskType",
        "window_id": "windowId",
        "cutoff_behavior": "cutoffBehavior",
        "description": "description",
        "logging_info": "loggingInfo",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "name": "name",
        "service_role_arn": "serviceRoleArn",
        "targets": "targets",
        "task_invocation_parameters": "taskInvocationParameters",
        "task_parameters": "taskParameters",
    },
)
class CfnMaintenanceWindowTaskProps:
    def __init__(
        self,
        *,
        priority: jsii.Number,
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        cutoff_behavior: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_parameters: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnMaintenanceWindowTask``.

        :param priority: The priority of the task in the maintenance window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
        :param task_arn: The resource that the task uses during execution. For ``RUN_COMMAND`` and ``AUTOMATION`` task types, ``TaskArn`` is the SSM document name or Amazon Resource Name (ARN). For ``LAMBDA`` tasks, ``TaskArn`` is the function name or ARN. For ``STEP_FUNCTIONS`` tasks, ``TaskArn`` is the state machine ARN.
        :param task_type: The type of task. Valid values: ``RUN_COMMAND`` , ``AUTOMATION`` , ``LAMBDA`` , ``STEP_FUNCTIONS`` .
        :param window_id: The ID of the maintenance window where the task is registered.
        :param cutoff_behavior: The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.
        :param description: A description of the task.
        :param logging_info: Information about an Amazon S3 bucket to write Run Command task-level logs to. .. epigraph:: ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs for Run Command tasks, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS ::SSM::MaintenanceWindowTask MaintenanceWindowRunCommandParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html>`_ .
        :param max_concurrency: The maximum number of targets this task can be run for, in parallel. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases. For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.
        :param max_errors: The maximum number of errors allowed before this task stops being scheduled. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases. For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.
        :param name: The task name.
        :param service_role_arn: The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run ``RegisterTaskWithMaintenanceWindow`` . However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see `Setting up maintenance windows <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html>`_ in the in the *AWS Systems Manager User Guide* .
        :param targets: The targets, either instances or window target IDs. - Specify instances using ``Key=InstanceIds,Values= *instanceid1* , *instanceid2*`` . - Specify window target IDs using ``Key=WindowTargetIds,Values= *window-target-id-1* , *window-target-id-2*`` .
        :param task_invocation_parameters: The parameters to pass to the task when it runs. Populate only the fields that match the task type. All other fields should be empty. .. epigraph:: When you update a maintenance window task that has options specified in ``TaskInvocationParameters`` , you must provide again all the ``TaskInvocationParameters`` values that you want to retain. The values you do not specify again are removed. For example, suppose that when you registered a Run Command task, you specified ``TaskInvocationParameters`` values for ``Comment`` , ``NotificationConfig`` , and ``OutputS3BucketName`` . If you update the maintenance window task and specify only a different ``OutputS3BucketName`` value, the values for ``Comment`` and ``NotificationConfig`` are removed.
        :param task_parameters: The parameters to pass to the task when it runs. .. epigraph:: ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `MaintenanceWindowTaskInvocationParameters <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTaskInvocationParameters.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            # parameters: Any
            # task_parameters: Any
            
            cfn_maintenance_window_task_props = ssm.CfnMaintenanceWindowTaskProps(
                priority=123,
                task_arn="taskArn",
                task_type="taskType",
                window_id="windowId",
            
                # the properties below are optional
                cutoff_behavior="cutoffBehavior",
                description="description",
                logging_info=ssm.CfnMaintenanceWindowTask.LoggingInfoProperty(
                    region="region",
                    s3_bucket="s3Bucket",
            
                    # the properties below are optional
                    s3_prefix="s3Prefix"
                ),
                max_concurrency="maxConcurrency",
                max_errors="maxErrors",
                name="name",
                service_role_arn="serviceRoleArn",
                targets=[ssm.CfnMaintenanceWindowTask.TargetProperty(
                    key="key",
                    values=["values"]
                )],
                task_invocation_parameters=ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty(
                    maintenance_window_automation_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty(
                        document_version="documentVersion",
                        parameters=parameters
                    ),
                    maintenance_window_lambda_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty(
                        client_context="clientContext",
                        payload="payload",
                        qualifier="qualifier"
                    ),
                    maintenance_window_run_command_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty(
                        cloud_watch_output_config=ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                            cloud_watch_log_group_name="cloudWatchLogGroupName",
                            cloud_watch_output_enabled=False
                        ),
                        comment="comment",
                        document_hash="documentHash",
                        document_hash_type="documentHashType",
                        document_version="documentVersion",
                        notification_config=ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                            notification_arn="notificationArn",
            
                            # the properties below are optional
                            notification_events=["notificationEvents"],
                            notification_type="notificationType"
                        ),
                        output_s3_bucket_name="outputS3BucketName",
                        output_s3_key_prefix="outputS3KeyPrefix",
                        parameters=parameters,
                        service_role_arn="serviceRoleArn",
                        timeout_seconds=123
                    ),
                    maintenance_window_step_functions_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty(
                        input="input",
                        name="name"
                    )
                ),
                task_parameters=task_parameters
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a897371c334ec198a4346a790b33c5836646788eb0a73ef18f8c56d7c89a1da3)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument task_arn", value=task_arn, expected_type=type_hints["task_arn"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument window_id", value=window_id, expected_type=type_hints["window_id"])
            check_type(argname="argument cutoff_behavior", value=cutoff_behavior, expected_type=type_hints["cutoff_behavior"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument logging_info", value=logging_info, expected_type=type_hints["logging_info"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_errors", value=max_errors, expected_type=type_hints["max_errors"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument task_invocation_parameters", value=task_invocation_parameters, expected_type=type_hints["task_invocation_parameters"])
            check_type(argname="argument task_parameters", value=task_parameters, expected_type=type_hints["task_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "priority": priority,
            "task_arn": task_arn,
            "task_type": task_type,
            "window_id": window_id,
        }
        if cutoff_behavior is not None:
            self._values["cutoff_behavior"] = cutoff_behavior
        if description is not None:
            self._values["description"] = description
        if logging_info is not None:
            self._values["logging_info"] = logging_info
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if name is not None:
            self._values["name"] = name
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn
        if targets is not None:
            self._values["targets"] = targets
        if task_invocation_parameters is not None:
            self._values["task_invocation_parameters"] = task_invocation_parameters
        if task_parameters is not None:
            self._values["task_parameters"] = task_parameters

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The priority of the task in the maintenance window.

        The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def task_arn(self) -> builtins.str:
        '''The resource that the task uses during execution.

        For ``RUN_COMMAND`` and ``AUTOMATION`` task types, ``TaskArn`` is the SSM document name or Amazon Resource Name (ARN).

        For ``LAMBDA`` tasks, ``TaskArn`` is the function name or ARN.

        For ``STEP_FUNCTIONS`` tasks, ``TaskArn`` is the state machine ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskarn
        '''
        result = self._values.get("task_arn")
        assert result is not None, "Required property 'task_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''The type of task.

        Valid values: ``RUN_COMMAND`` , ``AUTOMATION`` , ``LAMBDA`` , ``STEP_FUNCTIONS`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-tasktype
        '''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''The ID of the maintenance window where the task is registered.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-windowid
        '''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cutoff_behavior(self) -> typing.Optional[builtins.str]:
        '''The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-cutoffbehavior
        '''
        result = self._values.get("cutoff_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.LoggingInfoProperty]]:
        '''Information about an Amazon S3 bucket to write Run Command task-level logs to.

        .. epigraph::

           ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs for Run Command tasks, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS ::SSM::MaintenanceWindowTask MaintenanceWindowRunCommandParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-logginginfo
        '''
        result = self._values.get("logging_info")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.LoggingInfoProperty]], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''The maximum number of targets this task can be run for, in parallel.

        .. epigraph::

           Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases.

           For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxconcurrency
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''The maximum number of errors allowed before this task stops being scheduled.

        .. epigraph::

           Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases.

           For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxerrors
        '''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The task name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM service role for AWS Systems Manager to assume when running a maintenance window task.

        If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run ``RegisterTaskWithMaintenanceWindow`` .

        However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see `Setting up maintenance windows <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html>`_ in the in the *AWS Systems Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.TargetProperty]]]]:
        '''The targets, either instances or window target IDs.

        - Specify instances using ``Key=InstanceIds,Values= *instanceid1* , *instanceid2*`` .
        - Specify window target IDs using ``Key=WindowTargetIds,Values= *window-target-id-1* , *window-target-id-2*`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-targets
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.TargetProperty]]]], result)

    @builtins.property
    def task_invocation_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.TaskInvocationParametersProperty]]:
        '''The parameters to pass to the task when it runs.

        Populate only the fields that match the task type. All other fields should be empty.
        .. epigraph::

           When you update a maintenance window task that has options specified in ``TaskInvocationParameters`` , you must provide again all the ``TaskInvocationParameters`` values that you want to retain. The values you do not specify again are removed. For example, suppose that when you registered a Run Command task, you specified ``TaskInvocationParameters`` values for ``Comment`` , ``NotificationConfig`` , and ``OutputS3BucketName`` . If you update the maintenance window task and specify only a different ``OutputS3BucketName`` value, the values for ``Comment`` and ``NotificationConfig`` are removed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters
        '''
        result = self._values.get("task_invocation_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.TaskInvocationParametersProperty]], result)

    @builtins.property
    def task_parameters(self) -> typing.Any:
        '''The parameters to pass to the task when it runs.

        .. epigraph::

           ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `MaintenanceWindowTaskInvocationParameters <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTaskInvocationParameters.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskparameters
        '''
        result = self._values.get("task_parameters")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnParameter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnParameter",
):
    '''The ``AWS::SSM::Parameter`` resource creates an SSM parameter in AWS Systems Manager Parameter Store.

    .. epigraph::

       To create an SSM parameter, you must have the AWS Identity and Access Management ( IAM ) permissions ``ssm:PutParameter`` and ``ssm:AddTagsToResource`` . On stack creation, AWS CloudFormation adds the following three tags to the parameter: ``aws:cloudformation:stack-name`` , ``aws:cloudformation:logical-id`` , and ``aws:cloudformation:stack-id`` , in addition to any custom tags you specify.

       To add, update, or remove tags during stack update, you must have IAM permissions for both ``ssm:AddTagsToResource`` and ``ssm:RemoveTagsFromResource`` . For more information, see `Managing Access Using Policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam.html#security_iam_access-manage>`_ in the *AWS Systems Manager User Guide* .

    For information about valid values for parameters, see `About requirements and constraints for parameter names <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html#sysman-parameter-name-constraints>`_ in the *AWS Systems Manager User Guide* and `PutParameter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html>`_ in the *AWS Systems Manager API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
    :cloudformationResource: AWS::SSM::Parameter
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_parameter = ssm.CfnParameter(self, "MyCfnParameter",
            type="type",
            value="value",
        
            # the properties below are optional
            allowed_pattern="allowedPattern",
            data_type="dataType",
            description="description",
            name="name",
            policies="policies",
            tags={
                "tags_key": "tags"
            },
            tier="tier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        value: builtins.str,
        allowed_pattern: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        policies: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param type: The type of parameter.
        :param value: The parameter value. .. epigraph:: If type is ``StringList`` , the system returns a comma-separated string with no spaces between commas in the ``Value`` field.
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for ``String`` types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\\d+$``
        :param data_type: The data type of the parameter, such as ``text`` or ``aws:ec2:image`` . The default is ``text`` .
        :param description: Information about the parameter.
        :param name: The name of the parameter. .. epigraph:: The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter Amazon Resource Name (ARN), is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName``
        :param policies: Information about the policies assigned to a parameter. `Assigning parameter policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html>`_ in the *AWS Systems Manager User Guide* .
        :param tags: Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.
        :param tier: The parameter tier.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84f5ae628815b139c6b10b41675bde183ddd347469f32bde65a41e5d61495260)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnParameterProps(
            type=type,
            value=value,
            allowed_pattern=allowed_pattern,
            data_type=data_type,
            description=description,
            name=name,
            policies=policies,
            tags=tags,
            tier=tier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f3bad2b3db06c9a38c47a358cad4cefd9300a72bd8e07b1ef1bc420f4b50672)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea040d39901531e947210b790fd2aefea3474d073cd628aa40d996921aada583)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Returns the type of the parameter.

        Valid values are ``String`` or ``StringList`` .

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="attrValue")
    def attr_value(self) -> builtins.str:
        '''Returns the value of the parameter.

        :cloudformationAttribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrValue"))

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
        '''The type of parameter.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c3c8b1ff99cbeb84d6bfa4ec55c0f338baba344c4f051a0df40febf91e77b57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''The parameter value.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d784f981b1fc2fc2f326f9c00450c9509a7f7f86b9e9c7aa8701327c2cfc389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="allowedPattern")
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedPattern"))

    @allowed_pattern.setter
    def allowed_pattern(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9ffaa1025f846ad6a1c834ac9cdadb606682213a46ea55fc7ef79f038fc126c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedPattern", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The data type of the parameter, such as ``text`` or ``aws:ec2:image`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd34f48cc80688e3dee3c3e867bce351bd1d94df72caf85b542394330a8aeed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7395ed2d127b103cdc493e73e958c2b96d25307408ac9f8056cb7f8c798f4d39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d1b8e4a82c71a91758906c6a03031ca428e2b03893385cf6e7897fedbbacd6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.Optional[builtins.str]:
        '''Information about the policies assigned to a parameter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb1627df3e7fc8ca9be15411b137e27706b40b83c560792cf371422ee8ec910)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs).'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7f4d99885d1dde8bc3c789853e6ea39c5cd0a37d0d287307cad2a15a84707f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> typing.Optional[builtins.str]:
        '''The parameter tier.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb309cb97ef3622d8ccca3962a03b455578863222196e6d48ee076e28591cdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnParameterProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "value": "value",
        "allowed_pattern": "allowedPattern",
        "data_type": "dataType",
        "description": "description",
        "name": "name",
        "policies": "policies",
        "tags": "tags",
        "tier": "tier",
    },
)
class CfnParameterProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
        allowed_pattern: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        policies: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnParameter``.

        :param type: The type of parameter.
        :param value: The parameter value. .. epigraph:: If type is ``StringList`` , the system returns a comma-separated string with no spaces between commas in the ``Value`` field.
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for ``String`` types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\\d+$``
        :param data_type: The data type of the parameter, such as ``text`` or ``aws:ec2:image`` . The default is ``text`` .
        :param description: Information about the parameter.
        :param name: The name of the parameter. .. epigraph:: The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter Amazon Resource Name (ARN), is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName``
        :param policies: Information about the policies assigned to a parameter. `Assigning parameter policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html>`_ in the *AWS Systems Manager User Guide* .
        :param tags: Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.
        :param tier: The parameter tier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_parameter_props = ssm.CfnParameterProps(
                type="type",
                value="value",
            
                # the properties below are optional
                allowed_pattern="allowedPattern",
                data_type="dataType",
                description="description",
                name="name",
                policies="policies",
                tags={
                    "tags_key": "tags"
                },
                tier="tier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f89012f4986143c527853d7179ea46d1a3002d4025caeaa2123f32786cfdef8)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument allowed_pattern", value=allowed_pattern, expected_type=type_hints["allowed_pattern"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
            "value": value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if data_type is not None:
            self._values["data_type"] = data_type
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if policies is not None:
            self._values["policies"] = policies
        if tags is not None:
            self._values["tags"] = tags
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The parameter value.

        .. epigraph::

           If type is ``StringList`` , the system returns a comma-separated string with no spaces between commas in the ``Value`` field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for ``String`` types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\\d+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-allowedpattern
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The data type of the parameter, such as ``text`` or ``aws:ec2:image`` .

        The default is ``text`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-datatype
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        .. epigraph::

           The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter Amazon Resource Name (ARN), is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[builtins.str]:
        '''Information about the policies assigned to a parameter.

        `Assigning parameter policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html>`_ in the *AWS Systems Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs).

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''The parameter tier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tier
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPatchBaseline(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline",
):
    '''The ``AWS::SSM::PatchBaseline`` resource defines the basic information for an AWS Systems Manager patch baseline.

    A patch baseline defines which patches are approved for installation on your instances.

    For more information, see `CreatePatchBaseline <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html>`_ in the *AWS Systems Manager API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
    :cloudformationResource: AWS::SSM::PatchBaseline
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_patch_baseline = ssm.CfnPatchBaseline(self, "MyCfnPatchBaseline",
            name="name",
        
            # the properties below are optional
            approval_rules=ssm.CfnPatchBaseline.RuleGroupProperty(
                patch_rules=[ssm.CfnPatchBaseline.RuleProperty(
                    approve_after_days=123,
                    approve_until_date="approveUntilDate",
                    compliance_level="complianceLevel",
                    enable_non_security=False,
                    patch_filter_group=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                        patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                            key="key",
                            values=["values"]
                        )]
                    )
                )]
            ),
            approved_patches=["approvedPatches"],
            approved_patches_compliance_level="approvedPatchesComplianceLevel",
            approved_patches_enable_non_security=False,
            default_baseline=False,
            description="description",
            global_filters=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                    key="key",
                    values=["values"]
                )]
            ),
            operating_system="operatingSystem",
            patch_groups=["patchGroups"],
            rejected_patches=["rejectedPatches"],
            rejected_patches_action="rejectedPatchesAction",
            sources=[ssm.CfnPatchBaseline.PatchSourceProperty(
                configuration="configuration",
                name="name",
                products=["products"]
            )],
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
        approval_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPatchBaseline.RuleGroupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        default_baseline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        operating_system: typing.Optional[builtins.str] = None,
        patch_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPatchBaseline.PatchSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the patch baseline.
        :param approval_rules: A set of rules used to include patches in the baseline.
        :param approved_patches: A list of explicitly approved patches for the baseline. For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .
        :param approved_patches_compliance_level: Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is ``UNSPECIFIED`` . Default: - "UNSPECIFIED"
        :param approved_patches_enable_non_security: Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is ``false`` . Applies to Linux managed nodes only. Default: - false
        :param default_baseline: Set the baseline as default baseline. Only registering to default patch baseline is allowed. Default: - false
        :param description: A description of the patch baseline.
        :param global_filters: A set of global filters used to include patches in the baseline.
        :param operating_system: Defines the operating system the patch baseline applies to. The default value is ``WINDOWS`` . Default: - "WINDOWS"
        :param patch_groups: The name of the patch group to be registered with the patch baseline.
        :param rejected_patches: A list of explicitly rejected patches for the baseline. For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .
        :param rejected_patches_action: The action for Patch Manager to take on patches included in the ``RejectedPackages`` list. - *``ALLOW_AS_DEPENDENCY``* : A package in the ``Rejected`` patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as ``InstalledOther`` . This is the default action if no option is specified. - *BLOCK* : Packages in the *Rejected patches* list, and packages that include them as dependencies, aren't installed by Patch Manager under any circumstances. If a package was installed before it was added to the *Rejected patches* list, or is installed outside of Patch Manager afterward, it's considered noncompliant with the patch baseline and its status is reported as *InstalledRejected* . Default: - "ALLOW_AS_DEPENDENCY"
        :param sources: Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
        :param tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b87565e6649bbe5a503013adf6ae874b3dc918c05cd6b120b99a77e88b0b389)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPatchBaselineProps(
            name=name,
            approval_rules=approval_rules,
            approved_patches=approved_patches,
            approved_patches_compliance_level=approved_patches_compliance_level,
            approved_patches_enable_non_security=approved_patches_enable_non_security,
            default_baseline=default_baseline,
            description=description,
            global_filters=global_filters,
            operating_system=operating_system,
            patch_groups=patch_groups,
            rejected_patches=rejected_patches,
            rejected_patches_action=rejected_patches_action,
            sources=sources,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92307c615f0f17e5616c309d2fdf068be7a53d7ad171009574d4a7aec995eecb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c378f609536815c9c7b9fbe787c900b25bb0c7b14a2373df0ebb0ebe8b9ac55)
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
        '''The ID of the patch baseline.

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the patch baseline.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0c34df6132dc5024ae19aefdba7302eb801aba72f7c63d23a2977bb99d1ce66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="approvalRules")
    def approval_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.RuleGroupProperty"]]:
        '''A set of rules used to include patches in the baseline.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.RuleGroupProperty"]], jsii.get(self, "approvalRules"))

    @approval_rules.setter
    def approval_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.RuleGroupProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b56dfe31210955c8b1e478e9b12fb384520f16c624a7f1fd4ca7edc6c9d052e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalRules", value)

    @builtins.property
    @jsii.member(jsii_name="approvedPatches")
    def approved_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of explicitly approved patches for the baseline.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "approvedPatches"))

    @approved_patches.setter
    def approved_patches(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb6e3b5beff742671c1a2d820ffcd05e84cefb124894eba054fac867f1c23bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatches", value)

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> typing.Optional[builtins.str]:
        '''Defines the compliance level for approved patches.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approvedPatchesComplianceLevel"))

    @approved_patches_compliance_level.setter
    def approved_patches_compliance_level(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bff7659e5eeaba10646c1802753fc8aa922feac17eee3bc2e16dadf1450be553)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatchesComplianceLevel", value)

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "approvedPatchesEnableNonSecurity"))

    @approved_patches_enable_non_security.setter
    def approved_patches_enable_non_security(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__596ca4adbe9b66ae96ac84884c609e25720aab40b7f9d665e6ea16808f1a16ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatchesEnableNonSecurity", value)

    @builtins.property
    @jsii.member(jsii_name="defaultBaseline")
    def default_baseline(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Set the baseline as default baseline.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "defaultBaseline"))

    @default_baseline.setter
    def default_baseline(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a82f38addd776fccd7d2225bc356d9a6e4dc42b938cbf56c083c34cd4994c239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBaseline", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the patch baseline.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e0764881f21962614874d74c4570aaad8c8757ec8f88735329f4ff151db61a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="globalFilters")
    def global_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchFilterGroupProperty"]]:
        '''A set of global filters used to include patches in the baseline.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchFilterGroupProperty"]], jsii.get(self, "globalFilters"))

    @global_filters.setter
    def global_filters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchFilterGroupProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2179c7d6864a34b00339c58eb461fef37a68a420e457e90e7c0c7a25130bfbdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalFilters", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''Defines the operating system the patch baseline applies to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c5260a35c066fde54beec3890872a19db9827a2ab6171144440289a949dffe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystem", value)

    @builtins.property
    @jsii.member(jsii_name="patchGroups")
    def patch_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the patch group to be registered with the patch baseline.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patchGroups"))

    @patch_groups.setter
    def patch_groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a4ed06dc125b4ee77b4188a5d083535e272de23709a82c49ee2701451adddd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patchGroups", value)

    @builtins.property
    @jsii.member(jsii_name="rejectedPatches")
    def rejected_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of explicitly rejected patches for the baseline.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rejectedPatches"))

    @rejected_patches.setter
    def rejected_patches(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1770686b2069f49c778417afc185314be92ad98da528f69041a98291bbffdf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rejectedPatches", value)

    @builtins.property
    @jsii.member(jsii_name="rejectedPatchesAction")
    def rejected_patches_action(self) -> typing.Optional[builtins.str]:
        '''The action for Patch Manager to take on patches included in the ``RejectedPackages`` list.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rejectedPatchesAction"))

    @rejected_patches_action.setter
    def rejected_patches_action(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f95da053faafa2fab292f8a8670cf900b1d6f8c4edba0b0adb5dc8cb58a805c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rejectedPatchesAction", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchSourceProperty"]]]]:
        '''Information about the patches to use to update the managed nodes, including target operating systems and source repositories.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchSourceProperty"]]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchSourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0b14c56c59457cef6fb23f44714aa782c4d1965f4fe83bb31bf5f3ff58e6d22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional metadata that you assign to a resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc0a5821b51a90338294cb305cbf01102292e653fb3aa3f3b379b34ab3a9d0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchFilterGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"patch_filters": "patchFilters"},
    )
    class PatchFilterGroupProperty:
        def __init__(
            self,
            *,
            patch_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPatchBaseline.PatchFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``PatchFilterGroup`` property type specifies a set of patch filters for an AWS Systems Manager patch baseline, typically used for approval rules for a Systems Manager patch baseline.

            ``PatchFilterGroup`` is the property type for the ``GlobalFilters`` property of the `AWS::SSM::PatchBaseline <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html>`_ resource and the ``PatchFilterGroup`` property of the `Rule <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html>`_ property type.

            :param patch_filters: The set of patch filters that make up the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                patch_filter_group_property = ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                    patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                        key="key",
                        values=["values"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4622cb951de1b8fae6c5273a7cead99726f2ae144454c05b4a4b1393a6da770)
                check_type(argname="argument patch_filters", value=patch_filters, expected_type=type_hints["patch_filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if patch_filters is not None:
                self._values["patch_filters"] = patch_filters

        @builtins.property
        def patch_filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchFilterProperty"]]]]:
            '''The set of patch filters that make up the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html#cfn-ssm-patchbaseline-patchfiltergroup-patchfilters
            '''
            result = self._values.get("patch_filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchFilterGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class PatchFilterProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The ``PatchFilter`` property type defines a patch filter for an AWS Systems Manager patch baseline.

            The ``PatchFilters`` property of the `PatchFilterGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html>`_ property type contains a list of ``PatchFilter`` property types.

            You can view lists of valid values for the patch properties by running the ``DescribePatchProperties`` command. For more information, see `DescribePatchProperties <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchProperties.html>`_ in the *AWS Systems Manager API Reference* .

            :param key: The key for the filter. For information about valid keys, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .
            :param values: The value for the filter key. For information about valid values for each key based on operating system type, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                patch_filter_property = ssm.CfnPatchBaseline.PatchFilterProperty(
                    key="key",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__da7d74139bb37dc7d779767e1fd22b1c75774ef3272087902bdecbc1873f1b1e)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key for the filter.

            For information about valid keys, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The value for the filter key.

            For information about valid values for each key based on operating system type, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration": "configuration",
            "name": "name",
            "products": "products",
        },
    )
    class PatchSourceProperty:
        def __init__(
            self,
            *,
            configuration: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            products: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''``PatchSource`` is the property type for the ``Sources`` resource of the `AWS::SSM::PatchBaseline <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html>`_ resource.

            The AWS CloudFormation ``AWS::SSM::PatchSource`` resource is used to provide information about the patches to use to update target instances, including target operating systems and source repository. Applies to Linux managed nodes only.

            :param configuration: The value of the yum repo configuration. For example:. ``[main]`` ``name=MyCustomRepository`` ``baseurl=https://my-custom-repository`` ``enabled=1`` .. epigraph:: For information about other options available for your yum repository configuration, see `dnf.conf(5) <https://docs.aws.amazon.com/https://man7.org/linux/man-pages/man5/dnf.conf.5.html>`_ .
            :param name: The name specified to identify the patch source.
            :param products: The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                patch_source_property = ssm.CfnPatchBaseline.PatchSourceProperty(
                    configuration="configuration",
                    name="name",
                    products=["products"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec545f14b2e356c189699b3d1d51584fde777d8764ed9d5b8ea53e0419a450c4)
                check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument products", value=products, expected_type=type_hints["products"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if configuration is not None:
                self._values["configuration"] = configuration
            if name is not None:
                self._values["name"] = name
            if products is not None:
                self._values["products"] = products

        @builtins.property
        def configuration(self) -> typing.Optional[builtins.str]:
            '''The value of the yum repo configuration. For example:.

            ``[main]``

            ``name=MyCustomRepository``

            ``baseurl=https://my-custom-repository``

            ``enabled=1``
            .. epigraph::

               For information about other options available for your yum repository configuration, see `dnf.conf(5) <https://docs.aws.amazon.com/https://man7.org/linux/man-pages/man5/dnf.conf.5.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-configuration
            '''
            result = self._values.get("configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name specified to identify the patch source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def products(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-products
            '''
            result = self._values.get("products")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.RuleGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"patch_rules": "patchRules"},
    )
    class RuleGroupProperty:
        def __init__(
            self,
            *,
            patch_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPatchBaseline.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``RuleGroup`` property type specifies a set of rules that define the approval rules for an AWS Systems Manager patch baseline.

            ``RuleGroup`` is the property type for the ``ApprovalRules`` property of the `AWS::SSM::PatchBaseline <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html>`_ resource.

            :param patch_rules: The rules that make up the rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                rule_group_property = ssm.CfnPatchBaseline.RuleGroupProperty(
                    patch_rules=[ssm.CfnPatchBaseline.RuleProperty(
                        approve_after_days=123,
                        approve_until_date="approveUntilDate",
                        compliance_level="complianceLevel",
                        enable_non_security=False,
                        patch_filter_group=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                            patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                                key="key",
                                values=["values"]
                            )]
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb925a5a684e1a98e75f665a82421705d4d1af563c5893a0c6a712180618db72)
                check_type(argname="argument patch_rules", value=patch_rules, expected_type=type_hints["patch_rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if patch_rules is not None:
                self._values["patch_rules"] = patch_rules

        @builtins.property
        def patch_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.RuleProperty"]]]]:
            '''The rules that make up the rule group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html#cfn-ssm-patchbaseline-rulegroup-patchrules
            '''
            result = self._values.get("patch_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.RuleProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "approve_after_days": "approveAfterDays",
            "approve_until_date": "approveUntilDate",
            "compliance_level": "complianceLevel",
            "enable_non_security": "enableNonSecurity",
            "patch_filter_group": "patchFilterGroup",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            approve_after_days: typing.Optional[jsii.Number] = None,
            approve_until_date: typing.Optional[builtins.str] = None,
            compliance_level: typing.Optional[builtins.str] = None,
            enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            patch_filter_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``Rule`` property type specifies an approval rule for a Systems Manager patch baseline.

            The ``PatchRules`` property of the `RuleGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html>`_ property type contains a list of ``Rule`` property types.

            :param approve_after_days: The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of ``7`` means that patches are approved seven days after they are released. You must specify a value for ``ApproveAfterDays`` . Exception: Not supported on Debian Server or Ubuntu Server.
            :param approve_until_date: The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically. Not supported on Debian Server or Ubuntu Server. Enter dates in the format ``YYYY-MM-DD`` . For example, ``2021-12-31`` .
            :param compliance_level: A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: ``UNSPECIFIED`` , ``CRITICAL`` , ``HIGH`` , ``MEDIUM`` , ``LOW`` , and ``INFORMATIONAL`` .
            :param enable_non_security: For managed nodes identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is ``false`` . Applies to Linux managed nodes only. Default: - false
            :param patch_filter_group: The patch filter group that defines the criteria for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                rule_property = ssm.CfnPatchBaseline.RuleProperty(
                    approve_after_days=123,
                    approve_until_date="approveUntilDate",
                    compliance_level="complianceLevel",
                    enable_non_security=False,
                    patch_filter_group=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                        patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                            key="key",
                            values=["values"]
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8cc64444abb423fe6f774ad5b2ff12d0f2a189d9ce78b6c8500268e76f1abdbc)
                check_type(argname="argument approve_after_days", value=approve_after_days, expected_type=type_hints["approve_after_days"])
                check_type(argname="argument approve_until_date", value=approve_until_date, expected_type=type_hints["approve_until_date"])
                check_type(argname="argument compliance_level", value=compliance_level, expected_type=type_hints["compliance_level"])
                check_type(argname="argument enable_non_security", value=enable_non_security, expected_type=type_hints["enable_non_security"])
                check_type(argname="argument patch_filter_group", value=patch_filter_group, expected_type=type_hints["patch_filter_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if approve_after_days is not None:
                self._values["approve_after_days"] = approve_after_days
            if approve_until_date is not None:
                self._values["approve_until_date"] = approve_until_date
            if compliance_level is not None:
                self._values["compliance_level"] = compliance_level
            if enable_non_security is not None:
                self._values["enable_non_security"] = enable_non_security
            if patch_filter_group is not None:
                self._values["patch_filter_group"] = patch_filter_group

        @builtins.property
        def approve_after_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline.

            For example, a value of ``7`` means that patches are approved seven days after they are released.

            You must specify a value for ``ApproveAfterDays`` .

            Exception: Not supported on Debian Server or Ubuntu Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveafterdays
            '''
            result = self._values.get("approve_after_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def approve_until_date(self) -> typing.Optional[builtins.str]:
            '''The cutoff date for auto approval of released patches.

            Any patches released on or before this date are installed automatically. Not supported on Debian Server or Ubuntu Server.

            Enter dates in the format ``YYYY-MM-DD`` . For example, ``2021-12-31`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveuntildate
            '''
            result = self._values.get("approve_until_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compliance_level(self) -> typing.Optional[builtins.str]:
            '''A compliance severity level for all approved patches in a patch baseline.

            Valid compliance severity levels include the following: ``UNSPECIFIED`` , ``CRITICAL`` , ``HIGH`` , ``MEDIUM`` , ``LOW`` , and ``INFORMATIONAL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-compliancelevel
            '''
            result = self._values.get("compliance_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_non_security(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''For managed nodes identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository.

            The default value is ``false`` . Applies to Linux managed nodes only.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-enablenonsecurity
            '''
            result = self._values.get("enable_non_security")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def patch_filter_group(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchFilterGroupProperty"]]:
            '''The patch filter group that defines the criteria for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-patchfiltergroup
            '''
            result = self._values.get("patch_filter_group")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPatchBaseline.PatchFilterGroupProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaselineProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "approval_rules": "approvalRules",
        "approved_patches": "approvedPatches",
        "approved_patches_compliance_level": "approvedPatchesComplianceLevel",
        "approved_patches_enable_non_security": "approvedPatchesEnableNonSecurity",
        "default_baseline": "defaultBaseline",
        "description": "description",
        "global_filters": "globalFilters",
        "operating_system": "operatingSystem",
        "patch_groups": "patchGroups",
        "rejected_patches": "rejectedPatches",
        "rejected_patches_action": "rejectedPatchesAction",
        "sources": "sources",
        "tags": "tags",
    },
)
class CfnPatchBaselineProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        approval_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.RuleGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        default_baseline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        operating_system: typing.Optional[builtins.str] = None,
        patch_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.PatchSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPatchBaseline``.

        :param name: The name of the patch baseline.
        :param approval_rules: A set of rules used to include patches in the baseline.
        :param approved_patches: A list of explicitly approved patches for the baseline. For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .
        :param approved_patches_compliance_level: Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is ``UNSPECIFIED`` . Default: - "UNSPECIFIED"
        :param approved_patches_enable_non_security: Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is ``false`` . Applies to Linux managed nodes only. Default: - false
        :param default_baseline: Set the baseline as default baseline. Only registering to default patch baseline is allowed. Default: - false
        :param description: A description of the patch baseline.
        :param global_filters: A set of global filters used to include patches in the baseline.
        :param operating_system: Defines the operating system the patch baseline applies to. The default value is ``WINDOWS`` . Default: - "WINDOWS"
        :param patch_groups: The name of the patch group to be registered with the patch baseline.
        :param rejected_patches: A list of explicitly rejected patches for the baseline. For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .
        :param rejected_patches_action: The action for Patch Manager to take on patches included in the ``RejectedPackages`` list. - *``ALLOW_AS_DEPENDENCY``* : A package in the ``Rejected`` patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as ``InstalledOther`` . This is the default action if no option is specified. - *BLOCK* : Packages in the *Rejected patches* list, and packages that include them as dependencies, aren't installed by Patch Manager under any circumstances. If a package was installed before it was added to the *Rejected patches* list, or is installed outside of Patch Manager afterward, it's considered noncompliant with the patch baseline and its status is reported as *InstalledRejected* . Default: - "ALLOW_AS_DEPENDENCY"
        :param sources: Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
        :param tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_patch_baseline_props = ssm.CfnPatchBaselineProps(
                name="name",
            
                # the properties below are optional
                approval_rules=ssm.CfnPatchBaseline.RuleGroupProperty(
                    patch_rules=[ssm.CfnPatchBaseline.RuleProperty(
                        approve_after_days=123,
                        approve_until_date="approveUntilDate",
                        compliance_level="complianceLevel",
                        enable_non_security=False,
                        patch_filter_group=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                            patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                                key="key",
                                values=["values"]
                            )]
                        )
                    )]
                ),
                approved_patches=["approvedPatches"],
                approved_patches_compliance_level="approvedPatchesComplianceLevel",
                approved_patches_enable_non_security=False,
                default_baseline=False,
                description="description",
                global_filters=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                    patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                        key="key",
                        values=["values"]
                    )]
                ),
                operating_system="operatingSystem",
                patch_groups=["patchGroups"],
                rejected_patches=["rejectedPatches"],
                rejected_patches_action="rejectedPatchesAction",
                sources=[ssm.CfnPatchBaseline.PatchSourceProperty(
                    configuration="configuration",
                    name="name",
                    products=["products"]
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff6666a30d275f2a85d64de631c940fb83198b8b5a376b87a3a684f4a2dddf80)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument approval_rules", value=approval_rules, expected_type=type_hints["approval_rules"])
            check_type(argname="argument approved_patches", value=approved_patches, expected_type=type_hints["approved_patches"])
            check_type(argname="argument approved_patches_compliance_level", value=approved_patches_compliance_level, expected_type=type_hints["approved_patches_compliance_level"])
            check_type(argname="argument approved_patches_enable_non_security", value=approved_patches_enable_non_security, expected_type=type_hints["approved_patches_enable_non_security"])
            check_type(argname="argument default_baseline", value=default_baseline, expected_type=type_hints["default_baseline"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument global_filters", value=global_filters, expected_type=type_hints["global_filters"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
            check_type(argname="argument patch_groups", value=patch_groups, expected_type=type_hints["patch_groups"])
            check_type(argname="argument rejected_patches", value=rejected_patches, expected_type=type_hints["rejected_patches"])
            check_type(argname="argument rejected_patches_action", value=rejected_patches_action, expected_type=type_hints["rejected_patches_action"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if approval_rules is not None:
            self._values["approval_rules"] = approval_rules
        if approved_patches is not None:
            self._values["approved_patches"] = approved_patches
        if approved_patches_compliance_level is not None:
            self._values["approved_patches_compliance_level"] = approved_patches_compliance_level
        if approved_patches_enable_non_security is not None:
            self._values["approved_patches_enable_non_security"] = approved_patches_enable_non_security
        if default_baseline is not None:
            self._values["default_baseline"] = default_baseline
        if description is not None:
            self._values["description"] = description
        if global_filters is not None:
            self._values["global_filters"] = global_filters
        if operating_system is not None:
            self._values["operating_system"] = operating_system
        if patch_groups is not None:
            self._values["patch_groups"] = patch_groups
        if rejected_patches is not None:
            self._values["rejected_patches"] = rejected_patches
        if rejected_patches_action is not None:
            self._values["rejected_patches_action"] = rejected_patches_action
        if sources is not None:
            self._values["sources"] = sources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the patch baseline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def approval_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.RuleGroupProperty]]:
        '''A set of rules used to include patches in the baseline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvalrules
        '''
        result = self._values.get("approval_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.RuleGroupProperty]], result)

    @builtins.property
    def approved_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of explicitly approved patches for the baseline.

        For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatches
        '''
        result = self._values.get("approved_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def approved_patches_compliance_level(self) -> typing.Optional[builtins.str]:
        '''Defines the compliance level for approved patches.

        When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is ``UNSPECIFIED`` .

        :default: - "UNSPECIFIED"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchescompliancelevel
        '''
        result = self._values.get("approved_patches_compliance_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes.

        The default value is ``false`` . Applies to Linux managed nodes only.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity
        '''
        result = self._values.get("approved_patches_enable_non_security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def default_baseline(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Set the baseline as default baseline.

        Only registering to default patch baseline is allowed.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-defaultbaseline
        '''
        result = self._values.get("default_baseline")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the patch baseline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.PatchFilterGroupProperty]]:
        '''A set of global filters used to include patches in the baseline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-globalfilters
        '''
        result = self._values.get("global_filters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.PatchFilterGroupProperty]], result)

    @builtins.property
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''Defines the operating system the patch baseline applies to.

        The default value is ``WINDOWS`` .

        :default: - "WINDOWS"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-operatingsystem
        '''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def patch_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the patch group to be registered with the patch baseline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-patchgroups
        '''
        result = self._values.get("patch_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejected_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of explicitly rejected patches for the baseline.

        For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatches
        '''
        result = self._values.get("rejected_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejected_patches_action(self) -> typing.Optional[builtins.str]:
        '''The action for Patch Manager to take on patches included in the ``RejectedPackages`` list.

        - *``ALLOW_AS_DEPENDENCY``* : A package in the ``Rejected`` patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as ``InstalledOther`` . This is the default action if no option is specified.
        - *BLOCK* : Packages in the *Rejected patches* list, and packages that include them as dependencies, aren't installed by Patch Manager under any circumstances. If a package was installed before it was added to the *Rejected patches* list, or is installed outside of Patch Manager afterward, it's considered noncompliant with the patch baseline and its status is reported as *InstalledRejected* .

        :default: - "ALLOW_AS_DEPENDENCY"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatchesaction
        '''
        result = self._values.get("rejected_patches_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.PatchSourceProperty]]]]:
        '''Information about the patches to use to update the managed nodes, including target operating systems and source repositories.

        Applies to Linux managed nodes only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-sources
        '''
        result = self._values.get("sources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.PatchSourceProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional metadata that you assign to a resource.

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPatchBaselineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceDataSync(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync",
):
    '''The ``AWS::SSM::ResourceDataSync`` resource creates, updates, or deletes a resource data sync for AWS Systems Manager .

    A resource data sync helps you view data from multiple sources in a single location. Systems Manager offers two types of resource data sync: ``SyncToDestination`` and ``SyncFromSource`` .

    You can configure Systems Manager Inventory to use the ``SyncToDestination`` type to synchronize Inventory data from multiple AWS Regions to a single Amazon S3 bucket.

    You can configure Systems Manager Explorer to use the ``SyncFromSource`` type to synchronize operational work items (OpsItems) and operational data (OpsData) from multiple AWS Regions . This type can synchronize OpsItems and OpsData from multiple AWS accounts and Regions or from an ``EntireOrganization`` by using AWS Organizations .

    A resource data sync is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data.

    By default, data is not encrypted in Amazon S3 . We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy.

    For more information, see `Configuring Inventory Collection <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html#sysman-inventory-datasync>`_ and `Setting Up Systems Manager Explorer to Display Data from Multiple Accounts and Regions <https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html>`_ in the *AWS Systems Manager User Guide* .
    .. epigraph::

       The following *Syntax* section shows all fields that are supported for a resource data sync. The *Examples* section below shows the recommended way to specify configurations for each sync type. Refer to the *Examples* section when you create your resource data sync.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
    :cloudformationResource: AWS::SSM::ResourceDataSync
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_resource_data_sync = ssm.CfnResourceDataSync(self, "MyCfnResourceDataSync",
            sync_name="syncName",
        
            # the properties below are optional
            bucket_name="bucketName",
            bucket_prefix="bucketPrefix",
            bucket_region="bucketRegion",
            kms_key_arn="kmsKeyArn",
            s3_destination=ssm.CfnResourceDataSync.S3DestinationProperty(
                bucket_name="bucketName",
                bucket_region="bucketRegion",
                sync_format="syncFormat",
        
                # the properties below are optional
                bucket_prefix="bucketPrefix",
                kms_key_arn="kmsKeyArn"
            ),
            sync_format="syncFormat",
            sync_source=ssm.CfnResourceDataSync.SyncSourceProperty(
                source_regions=["sourceRegions"],
                source_type="sourceType",
        
                # the properties below are optional
                aws_organizations_source=ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty(
                    organization_source_type="organizationSourceType",
        
                    # the properties below are optional
                    organizational_units=["organizationalUnits"]
                ),
                include_future_regions=False
            ),
            sync_type="syncType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        sync_name: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDataSync.S3DestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sync_format: typing.Optional[builtins.str] = None,
        sync_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDataSync.SyncSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sync_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param sync_name: 
        :param bucket_name: The name of the S3 bucket where the aggregated data is stored.
        :param bucket_prefix: An Amazon S3 prefix for the bucket.
        :param bucket_region: The AWS Region with the S3 bucket targeted by the resource data sync.
        :param kms_key_arn: The Amazon Resource Name (ARN) of an encryption key for a destination in Amazon S3 . You can use a KMS key to encrypt inventory data in Amazon S3 . You must specify a key that exist in the same AWS Region as the destination Amazon S3 bucket.
        :param s3_destination: Configuration information for the target S3 bucket.
        :param sync_format: A supported sync format. The following format is currently supported: JsonSerDe
        :param sync_source: Information about the source where the data was synchronized.
        :param sync_type: The type of resource data sync. If ``SyncType`` is ``SyncToDestination`` , then the resource data sync synchronizes data to an S3 bucket. If the ``SyncType`` is ``SyncFromSource`` then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8a24f4d86cad49691c9635278face17e76a24ad5a69daef9687e1e2d395158c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceDataSyncProps(
            sync_name=sync_name,
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            bucket_region=bucket_region,
            kms_key_arn=kms_key_arn,
            s3_destination=s3_destination,
            sync_format=sync_format,
            sync_source=sync_source,
            sync_type=sync_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f6022ac7efc29929aa079bf79384c8ac5f0ba1718316a5dd4e06c591b9203d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__52d300d9d7ba1380e74c90a6b3b244b38158a194c79ff32598a2bb7a06e0603d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSyncName")
    def attr_sync_name(self) -> builtins.str:
        '''The name of the resource data sync.

        :cloudformationAttribute: SyncName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSyncName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="syncName")
    def sync_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syncName"))

    @sync_name.setter
    def sync_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c904544eb14d61bbdd853398a4e1561df17c1a6dbed2a5cec6fa0c804f538935)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the S3 bucket where the aggregated data is stored.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5fa255fdf6d438f6ead55de15298ce164aeda7ca776148e57fdae84a901f60c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''An Amazon S3 prefix for the bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a924763b3a0b031560d9453176bd0f0f3a33209abc82be03fd9bf29cf6d0d559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="bucketRegion")
    def bucket_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region with the S3 bucket targeted by the resource data sync.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketRegion"))

    @bucket_region.setter
    def bucket_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcb2a87b52c756e5533d55b08fe153a077d0b17d2d12326edf29ea9e3aa883c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketRegion", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an encryption key for a destination in Amazon S3 .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd64605b976fdaf20986b520b1f9002208a35fba878e5874ecbba8eac65dbce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3Destination")
    def s3_destination(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDataSync.S3DestinationProperty"]]:
        '''Configuration information for the target S3 bucket.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDataSync.S3DestinationProperty"]], jsii.get(self, "s3Destination"))

    @s3_destination.setter
    def s3_destination(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDataSync.S3DestinationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b7a3560b2c82654cd5bf6fbf841a21a5f937cad116af54ea4ddd8a8d62231d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Destination", value)

    @builtins.property
    @jsii.member(jsii_name="syncFormat")
    def sync_format(self) -> typing.Optional[builtins.str]:
        '''A supported sync format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncFormat"))

    @sync_format.setter
    def sync_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02ab77fd76bb25d5f48e8e3d49dfc9bc861b987ebca523a2e7fca2a67a78a7f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncFormat", value)

    @builtins.property
    @jsii.member(jsii_name="syncSource")
    def sync_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDataSync.SyncSourceProperty"]]:
        '''Information about the source where the data was synchronized.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDataSync.SyncSourceProperty"]], jsii.get(self, "syncSource"))

    @sync_source.setter
    def sync_source(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDataSync.SyncSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__157e7eb014224199daee91a842f040069c8ada6fa6deb70c8401e5815620c3e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncSource", value)

    @builtins.property
    @jsii.member(jsii_name="syncType")
    def sync_type(self) -> typing.Optional[builtins.str]:
        '''The type of resource data sync.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncType"))

    @sync_type.setter
    def sync_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d63d5c9fe36723e0e44dc178597f64394fe6601f2bea49c310bbb449d99b5c06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "organization_source_type": "organizationSourceType",
            "organizational_units": "organizationalUnits",
        },
    )
    class AwsOrganizationsSourceProperty:
        def __init__(
            self,
            *,
            organization_source_type: builtins.str,
            organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Information about the ``AwsOrganizationsSource`` resource data sync source.

            A sync source of this type can synchronize data from AWS Organizations or, if an AWS organization isn't present, from multiple AWS Regions .

            :param organization_source_type: If an AWS organization is present, this is either ``OrganizationalUnits`` or ``EntireOrganization`` . For ``OrganizationalUnits`` , the data is aggregated from a set of organization units. For ``EntireOrganization`` , the data is aggregated from the entire AWS organization.
            :param organizational_units: The AWS Organizations organization units included in the sync.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                aws_organizations_source_property = ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty(
                    organization_source_type="organizationSourceType",
                
                    # the properties below are optional
                    organizational_units=["organizationalUnits"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be83b6195e85fbee2558cb31697cb6e11f4697ac92613c317e23b837253bc9dd)
                check_type(argname="argument organization_source_type", value=organization_source_type, expected_type=type_hints["organization_source_type"])
                check_type(argname="argument organizational_units", value=organizational_units, expected_type=type_hints["organizational_units"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "organization_source_type": organization_source_type,
            }
            if organizational_units is not None:
                self._values["organizational_units"] = organizational_units

        @builtins.property
        def organization_source_type(self) -> builtins.str:
            '''If an AWS organization is present, this is either ``OrganizationalUnits`` or ``EntireOrganization`` .

            For ``OrganizationalUnits`` , the data is aggregated from a set of organization units. For ``EntireOrganization`` , the data is aggregated from the entire AWS organization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html#cfn-ssm-resourcedatasync-awsorganizationssource-organizationsourcetype
            '''
            result = self._values.get("organization_source_type")
            assert result is not None, "Required property 'organization_source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def organizational_units(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The AWS Organizations organization units included in the sync.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html#cfn-ssm-resourcedatasync-awsorganizationssource-organizationalunits
            '''
            result = self._values.get("organizational_units")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsOrganizationsSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.S3DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_region": "bucketRegion",
            "sync_format": "syncFormat",
            "bucket_prefix": "bucketPrefix",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class S3DestinationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_region: builtins.str,
            sync_format: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the target S3 bucket for the resource data sync.

            :param bucket_name: The name of the S3 bucket where the aggregated data is stored.
            :param bucket_region: The AWS Region with the S3 bucket targeted by the resource data sync.
            :param sync_format: A supported sync format. The following format is currently supported: JsonSerDe
            :param bucket_prefix: An Amazon S3 prefix for the bucket.
            :param kms_key_arn: The ARN of an encryption key for a destination in Amazon S3. Must belong to the same Region as the destination S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                s3_destination_property = ssm.CfnResourceDataSync.S3DestinationProperty(
                    bucket_name="bucketName",
                    bucket_region="bucketRegion",
                    sync_format="syncFormat",
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b78c67544ca2178e6a7855605a8caef43993dcfa332e0612430a58da945d418d)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_region", value=bucket_region, expected_type=type_hints["bucket_region"])
                check_type(argname="argument sync_format", value=sync_format, expected_type=type_hints["sync_format"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "bucket_region": bucket_region,
                "sync_format": sync_format,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the S3 bucket where the aggregated data is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_region(self) -> builtins.str:
            '''The AWS Region with the S3 bucket targeted by the resource data sync.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketregion
            '''
            result = self._values.get("bucket_region")
            assert result is not None, "Required property 'bucket_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sync_format(self) -> builtins.str:
            '''A supported sync format.

            The following format is currently supported: JsonSerDe

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-syncformat
            '''
            result = self._values.get("sync_format")
            assert result is not None, "Required property 'sync_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''An Amazon S3 prefix for the bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of an encryption key for a destination in Amazon S3.

            Must belong to the same Region as the destination S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.SyncSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_regions": "sourceRegions",
            "source_type": "sourceType",
            "aws_organizations_source": "awsOrganizationsSource",
            "include_future_regions": "includeFutureRegions",
        },
    )
    class SyncSourceProperty:
        def __init__(
            self,
            *,
            source_regions: typing.Sequence[builtins.str],
            source_type: builtins.str,
            aws_organizations_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceDataSync.AwsOrganizationsSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_future_regions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Information about the source of the data included in the resource data sync.

            :param source_regions: The ``SyncSource`` AWS Regions included in the resource data sync.
            :param source_type: The type of data source for the resource data sync. ``SourceType`` is either ``AwsOrganizations`` (if an organization is present in AWS Organizations ) or ``SingleAccountMultiRegions`` .
            :param aws_organizations_source: Information about the AwsOrganizationsSource resource data sync source. A sync source of this type can synchronize data from AWS Organizations .
            :param include_future_regions: Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                sync_source_property = ssm.CfnResourceDataSync.SyncSourceProperty(
                    source_regions=["sourceRegions"],
                    source_type="sourceType",
                
                    # the properties below are optional
                    aws_organizations_source=ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty(
                        organization_source_type="organizationSourceType",
                
                        # the properties below are optional
                        organizational_units=["organizationalUnits"]
                    ),
                    include_future_regions=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac8e974fe62ffae098cb7f57d7ea4db9b8d0aafbbba47aa7622d2bdcc0405b8e)
                check_type(argname="argument source_regions", value=source_regions, expected_type=type_hints["source_regions"])
                check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
                check_type(argname="argument aws_organizations_source", value=aws_organizations_source, expected_type=type_hints["aws_organizations_source"])
                check_type(argname="argument include_future_regions", value=include_future_regions, expected_type=type_hints["include_future_regions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_regions": source_regions,
                "source_type": source_type,
            }
            if aws_organizations_source is not None:
                self._values["aws_organizations_source"] = aws_organizations_source
            if include_future_regions is not None:
                self._values["include_future_regions"] = include_future_regions

        @builtins.property
        def source_regions(self) -> typing.List[builtins.str]:
            '''The ``SyncSource`` AWS Regions included in the resource data sync.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-sourceregions
            '''
            result = self._values.get("source_regions")
            assert result is not None, "Required property 'source_regions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def source_type(self) -> builtins.str:
            '''The type of data source for the resource data sync.

            ``SourceType`` is either ``AwsOrganizations`` (if an organization is present in AWS Organizations ) or ``SingleAccountMultiRegions`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-sourcetype
            '''
            result = self._values.get("source_type")
            assert result is not None, "Required property 'source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_organizations_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDataSync.AwsOrganizationsSourceProperty"]]:
            '''Information about the AwsOrganizationsSource resource data sync source.

            A sync source of this type can synchronize data from AWS Organizations .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-awsorganizationssource
            '''
            result = self._values.get("aws_organizations_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceDataSync.AwsOrganizationsSourceProperty"]], result)

        @builtins.property
        def include_future_regions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-includefutureregions
            '''
            result = self._values.get("include_future_regions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSyncProps",
    jsii_struct_bases=[],
    name_mapping={
        "sync_name": "syncName",
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "bucket_region": "bucketRegion",
        "kms_key_arn": "kmsKeyArn",
        "s3_destination": "s3Destination",
        "sync_format": "syncFormat",
        "sync_source": "syncSource",
        "sync_type": "syncType",
    },
)
class CfnResourceDataSyncProps:
    def __init__(
        self,
        *,
        sync_name: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDataSync.S3DestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sync_format: typing.Optional[builtins.str] = None,
        sync_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDataSync.SyncSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sync_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceDataSync``.

        :param sync_name: 
        :param bucket_name: The name of the S3 bucket where the aggregated data is stored.
        :param bucket_prefix: An Amazon S3 prefix for the bucket.
        :param bucket_region: The AWS Region with the S3 bucket targeted by the resource data sync.
        :param kms_key_arn: The Amazon Resource Name (ARN) of an encryption key for a destination in Amazon S3 . You can use a KMS key to encrypt inventory data in Amazon S3 . You must specify a key that exist in the same AWS Region as the destination Amazon S3 bucket.
        :param s3_destination: Configuration information for the target S3 bucket.
        :param sync_format: A supported sync format. The following format is currently supported: JsonSerDe
        :param sync_source: Information about the source where the data was synchronized.
        :param sync_type: The type of resource data sync. If ``SyncType`` is ``SyncToDestination`` , then the resource data sync synchronizes data to an S3 bucket. If the ``SyncType`` is ``SyncFromSource`` then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_resource_data_sync_props = ssm.CfnResourceDataSyncProps(
                sync_name="syncName",
            
                # the properties below are optional
                bucket_name="bucketName",
                bucket_prefix="bucketPrefix",
                bucket_region="bucketRegion",
                kms_key_arn="kmsKeyArn",
                s3_destination=ssm.CfnResourceDataSync.S3DestinationProperty(
                    bucket_name="bucketName",
                    bucket_region="bucketRegion",
                    sync_format="syncFormat",
            
                    # the properties below are optional
                    bucket_prefix="bucketPrefix",
                    kms_key_arn="kmsKeyArn"
                ),
                sync_format="syncFormat",
                sync_source=ssm.CfnResourceDataSync.SyncSourceProperty(
                    source_regions=["sourceRegions"],
                    source_type="sourceType",
            
                    # the properties below are optional
                    aws_organizations_source=ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty(
                        organization_source_type="organizationSourceType",
            
                        # the properties below are optional
                        organizational_units=["organizationalUnits"]
                    ),
                    include_future_regions=False
                ),
                sync_type="syncType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26353d4906971bfc49271a95bc4480dfb3fac99c43391b8a0aa7279209b75bb5)
            check_type(argname="argument sync_name", value=sync_name, expected_type=type_hints["sync_name"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument bucket_region", value=bucket_region, expected_type=type_hints["bucket_region"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument s3_destination", value=s3_destination, expected_type=type_hints["s3_destination"])
            check_type(argname="argument sync_format", value=sync_format, expected_type=type_hints["sync_format"])
            check_type(argname="argument sync_source", value=sync_source, expected_type=type_hints["sync_source"])
            check_type(argname="argument sync_type", value=sync_type, expected_type=type_hints["sync_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sync_name": sync_name,
        }
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if bucket_region is not None:
            self._values["bucket_region"] = bucket_region
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if s3_destination is not None:
            self._values["s3_destination"] = s3_destination
        if sync_format is not None:
            self._values["sync_format"] = sync_format
        if sync_source is not None:
            self._values["sync_source"] = sync_source
        if sync_type is not None:
            self._values["sync_type"] = sync_type

    @builtins.property
    def sync_name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncname
        '''
        result = self._values.get("sync_name")
        assert result is not None, "Required property 'sync_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the S3 bucket where the aggregated data is stored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketname
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''An Amazon S3 prefix for the bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketprefix
        '''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region with the S3 bucket targeted by the resource data sync.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketregion
        '''
        result = self._values.get("bucket_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an encryption key for a destination in Amazon S3 .

        You can use a KMS key to encrypt inventory data in Amazon S3 . You must specify a key that exist in the same AWS Region as the destination Amazon S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_destination(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDataSync.S3DestinationProperty]]:
        '''Configuration information for the target S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-s3destination
        '''
        result = self._values.get("s3_destination")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDataSync.S3DestinationProperty]], result)

    @builtins.property
    def sync_format(self) -> typing.Optional[builtins.str]:
        '''A supported sync format.

        The following format is currently supported: JsonSerDe

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncformat
        '''
        result = self._values.get("sync_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDataSync.SyncSourceProperty]]:
        '''Information about the source where the data was synchronized.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncsource
        '''
        result = self._values.get("sync_source")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDataSync.SyncSourceProperty]], result)

    @builtins.property
    def sync_type(self) -> typing.Optional[builtins.str]:
        '''The type of resource data sync.

        If ``SyncType`` is ``SyncToDestination`` , then the resource data sync synchronizes data to an S3 bucket. If the ``SyncType`` is ``SyncFromSource`` then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-synctype
        '''
        result = self._values.get("sync_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceDataSyncProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnResourcePolicy",
):
    '''Creates or updates a Systems Manager resource policy.

    A resource policy helps you to define the IAM entity (for example, an AWS account ) that can manage your Systems Manager resources. Currently, ``OpsItemGroup`` is the only resource that supports Systems Manager resource policies. The resource policy for ``OpsItemGroup`` enables AWS accounts to view and interact with OpsCenter operational work items (OpsItems). OpsCenter is a capability of Systems Manager .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html
    :cloudformationResource: AWS::SSM::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        # policy: Any
        
        cfn_resource_policy = ssm.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            policy=policy,
            resource_arn="resourceArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy: typing.Any,
        resource_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy: A policy you want to associate with a resource.
        :param resource_arn: The Amazon Resource Name (ARN) of the resource to which you want to attach a policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fde734ca585a99029a54306ff0fc2e0b9d248ae4e5ec6603d9179a5e18853eb2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(policy=policy, resource_arn=resource_arn)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4438689c231c110627ddbc405746a39736b727da60a710b45de0af51827c80b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e11274985c814298f7c85bdcfe1dca0d664c308ed58fd52b21ee54096829327b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyHash")
    def attr_policy_hash(self) -> builtins.str:
        '''ID of the current policy version.

        The hash helps to prevent a situation where multiple users attempt to overwrite a policy. You must provide this hash and the policy ID when updating or deleting a policy.

        :cloudformationAttribute: PolicyHash
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyHash"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyId")
    def attr_policy_id(self) -> builtins.str:
        '''ID of the current policy version.

        :cloudformationAttribute: PolicyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''A policy you want to associate with a resource.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e10ca1482b529c76d3760f3dda887f46d2071ff060e4a0a11d253064701edec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource to which you want to attach a policy.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd166322a09f9cd5b0060ba3a485fb9349539a442b3ae8ec7ee33b0ad035d8f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy": "policy", "resource_arn": "resourceArn"},
)
class CfnResourcePolicyProps:
    def __init__(self, *, policy: typing.Any, resource_arn: builtins.str) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param policy: A policy you want to associate with a resource.
        :param resource_arn: The Amazon Resource Name (ARN) of the resource to which you want to attach a policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            # policy: Any
            
            cfn_resource_policy_props = ssm.CfnResourcePolicyProps(
                policy=policy,
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__641aa0c71c4c89cb2aee737e31b19b3ae0745b8943985fb6855da98262576855)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
            "resource_arn": resource_arn,
        }

    @builtins.property
    def policy(self) -> typing.Any:
        '''A policy you want to associate with a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html#cfn-ssm-resourcepolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource to which you want to attach a policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html#cfn-ssm-resourcepolicy-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CommonStringParameterAttributes",
    jsii_struct_bases=[],
    name_mapping={"parameter_name": "parameterName", "simple_name": "simpleName"},
)
class CommonStringParameterAttributes:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Common attributes for string parameters.

        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            common_string_parameter_attributes = ssm.CommonStringParameterAttributes(
                parameter_name="parameterName",
            
                # the properties below are optional
                simple_name=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f4e05a41320bc1b3f1ba81e5056d43a2052eca526364b7ba62177a7542034f)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument simple_name", value=simple_name, expected_type=type_hints["simple_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates if the parameter name is a simple name (i.e. does not include "/" separators).

        This is required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonStringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IParameter")
class IParameter(_IResource_c80c4260, typing_extensions.Protocol):
    '''An SSM Parameter reference.'''

    @builtins.property
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''The ARN of the SSM Parameter resource.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''The name of the SSM Parameter resource.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''The type of the SSM Parameter resource.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants read (DescribeParameter, GetParameters, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: the role to be granted read-only access to the parameter.
        '''
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: the role to be granted write access to the parameter.
        '''
        ...


class _IParameterProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''An SSM Parameter reference.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IParameter"

    @builtins.property
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''The ARN of the SSM Parameter resource.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''The name of the SSM Parameter resource.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''The type of the SSM Parameter resource.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants read (DescribeParameter, GetParameters, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: the role to be granted read-only access to the parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__893dbe773f4eba8ae68bead053c2684acc5663f3c6568bf7b8860bed6523f05c)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: the role to be granted write access to the parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf6ae2a6ac121e36c84da0bbab30988cb29b98a2a83327833cd5a201ac06b622)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameter).__jsii_proxy_class__ = lambda : _IParameterProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IStringListParameter")
class IStringListParameter(IParameter, typing_extensions.Protocol):
    '''A StringList SSM Parameter.'''

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        :attribute: Value
        '''
        ...


class _IStringListParameterProxy(
    jsii.proxy_for(IParameter), # type: ignore[misc]
):
    '''A StringList SSM Parameter.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IStringListParameter"

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        :attribute: Value
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStringListParameter).__jsii_proxy_class__ = lambda : _IStringListParameterProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IStringParameter")
class IStringParameter(IParameter, typing_extensions.Protocol):
    '''A String SSM Parameter.'''

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        :attribute: Value
        '''
        ...


class _IStringParameterProxy(
    jsii.proxy_for(IParameter), # type: ignore[misc]
):
    '''A String SSM Parameter.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IStringParameter"

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        :attribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStringParameter).__jsii_proxy_class__ = lambda : _IStringParameterProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.ListParameterAttributes",
    jsii_struct_bases=[CommonStringParameterAttributes],
    name_mapping={
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "element_type": "elementType",
        "version": "version",
    },
)
class ListParameterAttributes(CommonStringParameterAttributes):
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
        element_type: typing.Optional["ParameterValueType"] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Attributes for parameters of string list type.

        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param element_type: The type of the string list parameter value. Using specific types can be helpful in catching invalid values at the start of creating or updating a stack. CloudFormation validates the values against existing values in the account. Note - if you want to allow values from different AWS accounts, use ParameterValueType.STRING Default: ParameterValueType.STRING
        :param version: The version number of the value you wish to retrieve. Default: The latest version will be retrieved.

        :see: ParameterType
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            list_parameter_attributes = ssm.ListParameterAttributes(
                parameter_name="parameterName",
            
                # the properties below are optional
                element_type=ssm.ParameterValueType.STRING,
                simple_name=False,
                version=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caa32518e1d362afcbf135bf8697e59bfcd27563570e63250f9b6ad629ce1479)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument simple_name", value=simple_name, expected_type=type_hints["simple_name"])
            check_type(argname="argument element_type", value=element_type, expected_type=type_hints["element_type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if element_type is not None:
            self._values["element_type"] = element_type
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates if the parameter name is a simple name (i.e. does not include "/" separators).

        This is required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def element_type(self) -> typing.Optional["ParameterValueType"]:
        '''The type of the string list parameter value.

        Using specific types can be helpful in catching invalid values
        at the start of creating or updating a stack. CloudFormation validates
        the values against existing values in the account.

        Note - if you want to allow values from different AWS accounts, use
        ParameterValueType.STRING

        :default: ParameterValueType.STRING

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types
        '''
        result = self._values.get("element_type")
        return typing.cast(typing.Optional["ParameterValueType"], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''The version number of the value you wish to retrieve.

        :default: The latest version will be retrieved.
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterDataType")
class ParameterDataType(enum.Enum):
    '''SSM parameter data type.'''

    TEXT = "TEXT"
    '''Text.'''
    AWS_EC2_IMAGE = "AWS_EC2_IMAGE"
    '''Aws Ec2 Image.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.ParameterOptions",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
    },
)
class ParameterOptions:
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional["ParameterTier"] = None,
    ) -> None:
        '''Properties needed to create a new SSM Parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            parameter_options = ssm.ParameterOptions(
                allowed_pattern="allowedPattern",
                description="description",
                parameter_name="parameterName",
                simple_name=False,
                tier=ssm.ParameterTier.ADVANCED
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54be6c6ec55adec6de5f0a4b285882a64b6047fff6c35192fc38b5de44f05ec5)
            check_type(argname="argument allowed_pattern", value=allowed_pattern, expected_type=type_hints["allowed_pattern"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument simple_name", value=simple_name, expected_type=type_hints["simple_name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: no validation is performed
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter that you want to add to the system.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        :default: - a name will be generated by CloudFormation
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates if the parameter name is a simple name (i.e. does not include "/" separators).

        This is required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional["ParameterTier"]:
        '''The tier of the string parameter.

        :default: - undefined
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional["ParameterTier"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParameterOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterTier")
class ParameterTier(enum.Enum):
    '''SSM parameter tier.

    :exampleMetadata: infused

    Example::

        ssm.StringParameter(self, "Parameter",
            allowed_pattern=".*",
            description="The value Foo",
            parameter_name="FooParameter",
            string_value="Foo",
            tier=ssm.ParameterTier.ADVANCED
        )
    '''

    ADVANCED = "ADVANCED"
    '''String.'''
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    '''String.'''
    STANDARD = "STANDARD"
    '''String.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterType")
class ParameterType(enum.Enum):
    '''(deprecated) SSM parameter type.

    :deprecated: these types are no longer used

    :stability: deprecated
    '''

    STRING = "STRING"
    '''(deprecated) String.

    :stability: deprecated
    '''
    SECURE_STRING = "SECURE_STRING"
    '''(deprecated) Secure String.

    Parameter Store uses an AWS Key Management Service (KMS) customer master key (CMK) to encrypt the parameter value.
    Parameters of type SecureString cannot be created directly from a CDK application.

    :stability: deprecated
    '''
    STRING_LIST = "STRING_LIST"
    '''(deprecated) String List.

    :stability: deprecated
    '''
    AWS_EC2_IMAGE_ID = "AWS_EC2_IMAGE_ID"
    '''(deprecated) An Amazon EC2 image ID, such as ami-0ff8a91507f77f867.

    :stability: deprecated
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterValueType")
class ParameterValueType(enum.Enum):
    '''The type of CFN SSM Parameter.

    Using specific types can be helpful in catching invalid values
    at the start of creating or updating a stack. CloudFormation validates
    the values against existing values in the account.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types
    :exampleMetadata: infused

    Example::

        ssm.StringParameter.value_for_typed_string_parameter_v2(self, "/My/Public/Parameter", ssm.ParameterValueType.AWS_EC2_IMAGE_ID)
    '''

    STRING = "STRING"
    '''String.'''
    AWS_EC2_AVAILABILITYZONE_NAME = "AWS_EC2_AVAILABILITYZONE_NAME"
    '''An Availability Zone, such as us-west-2a.'''
    AWS_EC2_IMAGE_ID = "AWS_EC2_IMAGE_ID"
    '''An Amazon EC2 image ID, such as ami-0ff8a91507f77f867.'''
    AWS_EC2_INSTANCE_ID = "AWS_EC2_INSTANCE_ID"
    '''An Amazon EC2 instance ID, such as i-1e731a32.'''
    AWS_EC2_KEYPAIR_KEYNAME = "AWS_EC2_KEYPAIR_KEYNAME"
    '''An Amazon EC2 key pair name.'''
    AWS_EC2_SECURITYGROUP_GROUPNAME = "AWS_EC2_SECURITYGROUP_GROUPNAME"
    '''An EC2-Classic or default VPC security group name, such as my-sg-abc.'''
    AWS_EC2_SECURITYGROUP_ID = "AWS_EC2_SECURITYGROUP_ID"
    '''A security group ID, such as sg-a123fd85.'''
    AWS_EC2_SUBNET_ID = "AWS_EC2_SUBNET_ID"
    '''A subnet ID, such as subnet-123a351e.'''
    AWS_EC2_VOLUME_ID = "AWS_EC2_VOLUME_ID"
    '''An Amazon EBS volume ID, such as vol-3cdd3f56.'''
    AWS_EC2_VPC_ID = "AWS_EC2_VPC_ID"
    '''A VPC ID, such as vpc-a123baa3.'''
    AWS_ROUTE53_HOSTEDZONE_ID = "AWS_ROUTE53_HOSTEDZONE_ID"
    '''An Amazon Route 53 hosted zone ID, such as Z23YXV4OVPL04A.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.SecureStringParameterAttributes",
    jsii_struct_bases=[CommonStringParameterAttributes],
    name_mapping={
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "encryption_key": "encryptionKey",
        "version": "version",
    },
)
class SecureStringParameterAttributes(CommonStringParameterAttributes):
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Attributes for secure string parameters.

        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param encryption_key: The encryption key that is used to encrypt this parameter. Default: - default master key
        :param version: The version number of the value you wish to retrieve. Default: - AWS CloudFormation uses the latest version of the parameter

        :exampleMetadata: infused

        Example::

            parameter_version = Token.as_number({"Ref": "MyParameter"})
            
            # Retrieve the latest value of the non-secret parameter
            # with name "/My/String/Parameter".
            string_value = ssm.StringParameter.from_string_parameter_attributes(self, "MyValue",
                parameter_name="/My/Public/Parameter"
            ).string_value
            string_value_version_from_token = ssm.StringParameter.from_string_parameter_attributes(self, "MyValueVersionFromToken",
                parameter_name="/My/Public/Parameter",
                # parameter version from token
                version=parameter_version
            ).string_value
            
            # Retrieve a specific version of the secret (SecureString) parameter.
            # 'version' is always required.
            secret_value = ssm.StringParameter.from_secure_string_parameter_attributes(self, "MySecureValue",
                parameter_name="/My/Secret/Parameter",
                version=5
            )
            secret_value_version_from_token = ssm.StringParameter.from_secure_string_parameter_attributes(self, "MySecureValueVersionFromToken",
                parameter_name="/My/Secret/Parameter",
                # parameter version from token
                version=parameter_version
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c29a999cdf02428bb99b29e94af353e96064d305daa31ac2e3c9bbd7cff7dee)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument simple_name", value=simple_name, expected_type=type_hints["simple_name"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates if the parameter name is a simple name (i.e. does not include "/" separators).

        This is required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The encryption key that is used to encrypt this parameter.

        :default: - default master key
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''The version number of the value you wish to retrieve.

        :default: - AWS CloudFormation uses the latest version of the parameter
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecureStringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStringListParameter, IParameter)
class StringListParameter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.StringListParameter",
):
    '''Creates a new StringList SSM Parameter.

    :resource: AWS::SSM::Parameter
    :exampleMetadata: infused

    Example::

        ssm.StringListParameter.value_for_typed_list_parameter(self, "/My/Public/Parameter", ssm.ParameterValueType.AWS_EC2_IMAGE_ID)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        string_list_value: typing.Sequence[builtins.str],
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param string_list_value: The values of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94de6d51dda014e2ac4e863b9f9611f97d1e28dc774309241f1b4d807451758f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StringListParameterProps(
            string_list_value=string_list_value,
            allowed_pattern=allowed_pattern,
            description=description,
            parameter_name=parameter_name,
            simple_name=simple_name,
            tier=tier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromListParameterAttributes")
    @builtins.classmethod
    def from_list_parameter_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        element_type: typing.Optional[ParameterValueType] = None,
        version: typing.Optional[jsii.Number] = None,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> IStringListParameter:
        '''Imports an external string list parameter with name and optional version.

        :param scope: -
        :param id: -
        :param element_type: The type of the string list parameter value. Using specific types can be helpful in catching invalid values at the start of creating or updating a stack. CloudFormation validates the values against existing values in the account. Note - if you want to allow values from different AWS accounts, use ParameterValueType.STRING Default: ParameterValueType.STRING
        :param version: The version number of the value you wish to retrieve. Default: The latest version will be retrieved.
        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b477545ed5d53e5b666f41087db25aa6bdc347c4cead18a586bd16678f612801)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = ListParameterAttributes(
            element_type=element_type,
            version=version,
            parameter_name=parameter_name,
            simple_name=simple_name,
        )

        return typing.cast(IStringListParameter, jsii.sinvoke(cls, "fromListParameterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromStringListParameterName")
    @builtins.classmethod
    def from_string_list_parameter_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        string_list_parameter_name: builtins.str,
    ) -> IStringListParameter:
        '''Imports an external parameter of type string list.

        Returns a token and should not be parsed.

        :param scope: -
        :param id: -
        :param string_list_parameter_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ee02d93e11a637ffc18281f9eda840005cd8f1adec7265948e87be3b063fd8b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument string_list_parameter_name", value=string_list_parameter_name, expected_type=type_hints["string_list_parameter_name"])
        return typing.cast(IStringListParameter, jsii.sinvoke(cls, "fromStringListParameterName", [scope, id, string_list_parameter_name]))

    @jsii.member(jsii_name="valueForTypedListParameter")
    @builtins.classmethod
    def value_for_typed_list_parameter(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        parameter_name: builtins.str,
        type: typing.Optional[ParameterValueType] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> typing.List[builtins.str]:
        '''Returns a token that will resolve (during deployment) to the list value of an SSM StringList parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param type: the type of the SSM list parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b9ae745d086e0dea148aea94e9f88d8efd375fa182578d056bcfd3fd08b1771)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "valueForTypedListParameter", [scope, parameter_name, type, version]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants read (DescribeParameter, GetParameters, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__819241aedbf400f619f3bb1dab30b0594eef1072ffeee79fad21356c807bec86)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a6c74a7f6bd369fd4593adcf2cfb417138607dd7b20b5da6ea534219eee0c55)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''The ARN of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''The name of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''The type of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The encryption key that is used to encrypt this parameter.

        :default: - default master key
        '''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "encryptionKey"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringListParameterProps",
    jsii_struct_bases=[ParameterOptions],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
        "string_list_value": "stringListValue",
    },
)
class StringListParameterProps(ParameterOptions):
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
        string_list_value: typing.Sequence[builtins.str],
    ) -> None:
        '''Properties needed to create a StringList SSM Parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined
        :param string_list_value: The values of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.

        :exampleMetadata: infused

        Example::

            # Grant read access to some Role
            # role: iam.IRole
            # Create a new SSM Parameter holding a String
            param = ssm.StringParameter(self, "StringParameter",
                # description: 'Some user-friendly description',
                # name: 'ParameterName',
                string_value="Initial parameter value"
            )
            param.grant_read(role)
            
            # Create a new SSM Parameter holding a StringList
            list_parameter = ssm.StringListParameter(self, "StringListParameter",
                # description: 'Some user-friendly description',
                # name: 'ParameterName',
                string_list_value=["Initial parameter value A", "Initial parameter value B"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fda8a7b3397aad49f6c3720e316364d4df6b092c111c31c5e48e223f7ab4b46)
            check_type(argname="argument allowed_pattern", value=allowed_pattern, expected_type=type_hints["allowed_pattern"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument simple_name", value=simple_name, expected_type=type_hints["simple_name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "string_list_value": string_list_value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: no validation is performed
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter that you want to add to the system.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        :default: - a name will be generated by CloudFormation
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates if the parameter name is a simple name (i.e. does not include "/" separators).

        This is required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional[ParameterTier]:
        '''The tier of the string parameter.

        :default: - undefined
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[ParameterTier], result)

    @builtins.property
    def string_list_value(self) -> typing.List[builtins.str]:
        '''The values of the parameter.

        It may not reference another parameter and ``{{}}`` cannot be used in the value.
        '''
        result = self._values.get("string_list_value")
        assert result is not None, "Required property 'string_list_value' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringListParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStringParameter, IParameter)
class StringParameter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.StringParameter",
):
    '''Creates a new String SSM Parameter.

    :resource: AWS::SSM::Parameter

    Example::

        ssm_parameter = ssm.StringParameter(self, "mySsmParameter",
            parameter_name="mySsmParameter",
            string_value="mySsmParameterValue"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        string_value: builtins.str,
        data_type: typing.Optional[ParameterDataType] = None,
        type: typing.Optional[ParameterType] = None,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param string_value: The value of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param data_type: The data type of the parameter, such as ``text`` or ``aws:ec2:image``. Default: ParameterDataType.TEXT
        :param type: (deprecated) The type of the string parameter. Default: ParameterType.STRING
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2eeba991f657f464e2410cd38fdeecff2bdaa0b51e35cd0e4ca251c97217a46)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StringParameterProps(
            string_value=string_value,
            data_type=data_type,
            type=type,
            allowed_pattern=allowed_pattern,
            description=description,
            parameter_name=parameter_name,
            simple_name=simple_name,
            tier=tier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSecureStringParameterAttributes")
    @builtins.classmethod
    def from_secure_string_parameter_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        version: typing.Optional[jsii.Number] = None,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> IStringParameter:
        '''Imports a secure string parameter from the SSM parameter store.

        :param scope: -
        :param id: -
        :param encryption_key: The encryption key that is used to encrypt this parameter. Default: - default master key
        :param version: The version number of the value you wish to retrieve. Default: - AWS CloudFormation uses the latest version of the parameter
        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef716b2d64b7c95b87119e190e88504880c3f46c45b769e05e9f4f805b08c63d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = SecureStringParameterAttributes(
            encryption_key=encryption_key,
            version=version,
            parameter_name=parameter_name,
            simple_name=simple_name,
        )

        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromSecureStringParameterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromStringParameterAttributes")
    @builtins.classmethod
    def from_string_parameter_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        force_dynamic_reference: typing.Optional[builtins.bool] = None,
        type: typing.Optional[ParameterType] = None,
        value_type: typing.Optional[ParameterValueType] = None,
        version: typing.Optional[jsii.Number] = None,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> IStringParameter:
        '''Imports an external string parameter with name and optional version.

        :param scope: -
        :param id: -
        :param force_dynamic_reference: Use a dynamic reference as the representation in CloudFormation template level. By default, CDK tries to deduce an appropriate representation based on the parameter value (a CfnParameter or a dynamic reference). Use this flag to override the representation when it does not work. Default: false
        :param type: (deprecated) The type of the string parameter. Default: ParameterType.STRING
        :param value_type: The type of the string parameter value. Using specific types can be helpful in catching invalid values at the start of creating or updating a stack. CloudFormation validates the values against existing values in the account. Note - if you want to allow values from different AWS accounts, use ParameterValueType.STRING Default: ParameterValueType.STRING
        :param version: The version number of the value you wish to retrieve. Default: The latest version will be retrieved.
        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e612c2654654e8b8bb7821bcd1e47680b025862a2a411467ffa6334e46371b05)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = StringParameterAttributes(
            force_dynamic_reference=force_dynamic_reference,
            type=type,
            value_type=value_type,
            version=version,
            parameter_name=parameter_name,
            simple_name=simple_name,
        )

        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromStringParameterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromStringParameterName")
    @builtins.classmethod
    def from_string_parameter_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        string_parameter_name: builtins.str,
    ) -> IStringParameter:
        '''Imports an external string parameter by name.

        :param scope: -
        :param id: -
        :param string_parameter_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb0299149e02d9543818343516306f4b32ee1ac5f245ff3c79ee5fd2016ec670)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument string_parameter_name", value=string_parameter_name, expected_type=type_hints["string_parameter_name"])
        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromStringParameterName", [scope, id, string_parameter_name]))

    @jsii.member(jsii_name="valueForSecureStringParameter")
    @builtins.classmethod
    def value_for_secure_string_parameter(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        parameter_name: builtins.str,
        version: jsii.Number,
    ) -> builtins.str:
        '''(deprecated) Returns a token that will resolve (during deployment).

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param version: The parameter version (required for secure strings).

        :deprecated: Use ``SecretValue.ssmSecure()`` instead, it will correctly type the imported value as a ``SecretValue`` and allow importing without version. ``SecretValue`` lives in the core ``aws-cdk-lib`` module.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38dfc6aee7234162b6dfa7fd6d79daf1e5e20fb93a83a884110ee85c9406a842)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForSecureStringParameter", [scope, parameter_name, version]))

    @jsii.member(jsii_name="valueForStringParameter")
    @builtins.classmethod
    def value_for_string_parameter(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        parameter_name: builtins.str,
        version: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__587bcd33299d81a1c2d922ca6d8a6c0dbb1a57b5bf5619f44b25a23071ffcf19)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForStringParameter", [scope, parameter_name, version]))

    @jsii.member(jsii_name="valueForTypedStringParameter")
    @builtins.classmethod
    def value_for_typed_string_parameter(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        parameter_name: builtins.str,
        type: typing.Optional[ParameterType] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''(deprecated) Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param type: The type of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).

        :deprecated: - use valueForTypedStringParameterV2 instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ddd12c8dffbad4b7f599d939f1683184715d90ae73713323484cf1f89d0f99)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForTypedStringParameter", [scope, parameter_name, type, version]))

    @jsii.member(jsii_name="valueForTypedStringParameterV2")
    @builtins.classmethod
    def value_for_typed_string_parameter_v2(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        parameter_name: builtins.str,
        type: typing.Optional[ParameterValueType] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param type: The type of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ec30255f3ac830ba0695e062a34e2012e0542d68a61c236b791945a367b24b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForTypedStringParameterV2", [scope, parameter_name, type, version]))

    @jsii.member(jsii_name="valueFromLookup")
    @builtins.classmethod
    def value_from_lookup(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        parameter_name: builtins.str,
    ) -> builtins.str:
        '''Reads the value of an SSM parameter during synthesis through an environmental context provider.

        Requires that the stack this scope is defined in will have explicit
        account/region information. Otherwise, it will fail during synthesis.

        :param scope: -
        :param parameter_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__352ba5506c7762dcb469028a7b0515dc3daed2b43c5a8ff339ed16372f650250)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueFromLookup", [scope, parameter_name]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants read (DescribeParameter, GetParameters, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2b954516f020047895372042cbf3497906d242b8a2c10008ce8a5c2e1335370)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9601cc05d10fcfadbdc97c8deacf47393567be2f0e90bd28ea11cdfe571976fa)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''The ARN of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''The name of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''The type of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.
        '''
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The encryption key that is used to encrypt this parameter.

        :default: - default master key
        '''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "encryptionKey"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringParameterAttributes",
    jsii_struct_bases=[CommonStringParameterAttributes],
    name_mapping={
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "force_dynamic_reference": "forceDynamicReference",
        "type": "type",
        "value_type": "valueType",
        "version": "version",
    },
)
class StringParameterAttributes(CommonStringParameterAttributes):
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
        force_dynamic_reference: typing.Optional[builtins.bool] = None,
        type: typing.Optional[ParameterType] = None,
        value_type: typing.Optional[ParameterValueType] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Attributes for parameters of various types of string.

        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param force_dynamic_reference: Use a dynamic reference as the representation in CloudFormation template level. By default, CDK tries to deduce an appropriate representation based on the parameter value (a CfnParameter or a dynamic reference). Use this flag to override the representation when it does not work. Default: false
        :param type: (deprecated) The type of the string parameter. Default: ParameterType.STRING
        :param value_type: The type of the string parameter value. Using specific types can be helpful in catching invalid values at the start of creating or updating a stack. CloudFormation validates the values against existing values in the account. Note - if you want to allow values from different AWS accounts, use ParameterValueType.STRING Default: ParameterValueType.STRING
        :param version: The version number of the value you wish to retrieve. Default: The latest version will be retrieved.

        :see: ParameterType
        :exampleMetadata: infused

        Example::

            parameter_version = Token.as_number({"Ref": "MyParameter"})
            
            # Retrieve the latest value of the non-secret parameter
            # with name "/My/String/Parameter".
            string_value = ssm.StringParameter.from_string_parameter_attributes(self, "MyValue",
                parameter_name="/My/Public/Parameter"
            ).string_value
            string_value_version_from_token = ssm.StringParameter.from_string_parameter_attributes(self, "MyValueVersionFromToken",
                parameter_name="/My/Public/Parameter",
                # parameter version from token
                version=parameter_version
            ).string_value
            
            # Retrieve a specific version of the secret (SecureString) parameter.
            # 'version' is always required.
            secret_value = ssm.StringParameter.from_secure_string_parameter_attributes(self, "MySecureValue",
                parameter_name="/My/Secret/Parameter",
                version=5
            )
            secret_value_version_from_token = ssm.StringParameter.from_secure_string_parameter_attributes(self, "MySecureValueVersionFromToken",
                parameter_name="/My/Secret/Parameter",
                # parameter version from token
                version=parameter_version
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045695ee32d353600237b891b14ad138098a0add8ba99199144ee57eff4ad99f)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument simple_name", value=simple_name, expected_type=type_hints["simple_name"])
            check_type(argname="argument force_dynamic_reference", value=force_dynamic_reference, expected_type=type_hints["force_dynamic_reference"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value_type", value=value_type, expected_type=type_hints["value_type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if force_dynamic_reference is not None:
            self._values["force_dynamic_reference"] = force_dynamic_reference
        if type is not None:
            self._values["type"] = type
        if value_type is not None:
            self._values["value_type"] = value_type
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates if the parameter name is a simple name (i.e. does not include "/" separators).

        This is required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def force_dynamic_reference(self) -> typing.Optional[builtins.bool]:
        '''Use a dynamic reference as the representation in CloudFormation template level.

        By default, CDK tries to deduce an appropriate representation based on the parameter value (a CfnParameter or a dynamic reference). Use this flag to override the representation when it does not work.

        :default: false
        '''
        result = self._values.get("force_dynamic_reference")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def type(self) -> typing.Optional[ParameterType]:
        '''(deprecated) The type of the string parameter.

        :default: ParameterType.STRING

        :deprecated: - use valueType instead

        :stability: deprecated
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ParameterType], result)

    @builtins.property
    def value_type(self) -> typing.Optional[ParameterValueType]:
        '''The type of the string parameter value.

        Using specific types can be helpful in catching invalid values
        at the start of creating or updating a stack. CloudFormation validates
        the values against existing values in the account.

        Note - if you want to allow values from different AWS accounts, use
        ParameterValueType.STRING

        :default: ParameterValueType.STRING

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types
        '''
        result = self._values.get("value_type")
        return typing.cast(typing.Optional[ParameterValueType], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''The version number of the value you wish to retrieve.

        :default: The latest version will be retrieved.
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringParameterProps",
    jsii_struct_bases=[ParameterOptions],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
        "string_value": "stringValue",
        "data_type": "dataType",
        "type": "type",
    },
)
class StringParameterProps(ParameterOptions):
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
        string_value: builtins.str,
        data_type: typing.Optional[ParameterDataType] = None,
        type: typing.Optional[ParameterType] = None,
    ) -> None:
        '''Properties needed to create a String SSM parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates if the parameter name is a simple name (i.e. does not include "/" separators). This is required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined
        :param string_value: The value of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param data_type: The data type of the parameter, such as ``text`` or ``aws:ec2:image``. Default: ParameterDataType.TEXT
        :param type: (deprecated) The type of the string parameter. Default: ParameterType.STRING

        :exampleMetadata: infused

        Example::

            # Grant read access to some Role
            # role: iam.IRole
            # Create a new SSM Parameter holding a String
            param = ssm.StringParameter(self, "StringParameter",
                # description: 'Some user-friendly description',
                # name: 'ParameterName',
                string_value="Initial parameter value"
            )
            param.grant_read(role)
            
            # Create a new SSM Parameter holding a StringList
            list_parameter = ssm.StringListParameter(self, "StringListParameter",
                # description: 'Some user-friendly description',
                # name: 'ParameterName',
                string_list_value=["Initial parameter value A", "Initial parameter value B"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a14e5cea1d211f374b7c289d526224c03be1f2e91a2a94cbcdf8f1d251335822)
            check_type(argname="argument allowed_pattern", value=allowed_pattern, expected_type=type_hints["allowed_pattern"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument simple_name", value=simple_name, expected_type=type_hints["simple_name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "string_value": string_value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier
        if data_type is not None:
            self._values["data_type"] = data_type
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: no validation is performed
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter that you want to add to the system.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        :default: - a name will be generated by CloudFormation
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates if the parameter name is a simple name (i.e. does not include "/" separators).

        This is required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional[ParameterTier]:
        '''The tier of the string parameter.

        :default: - undefined
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[ParameterTier], result)

    @builtins.property
    def string_value(self) -> builtins.str:
        '''The value of the parameter.

        It may not reference another parameter and ``{{}}`` cannot be used in the value.
        '''
        result = self._values.get("string_value")
        assert result is not None, "Required property 'string_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_type(self) -> typing.Optional[ParameterDataType]:
        '''The data type of the parameter, such as ``text`` or ``aws:ec2:image``.

        :default: ParameterDataType.TEXT
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[ParameterDataType], result)

    @builtins.property
    def type(self) -> typing.Optional[ParameterType]:
        '''(deprecated) The type of the string parameter.

        :default: ParameterType.STRING

        :deprecated: - type will always be 'String'

        :stability: deprecated
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ParameterType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssociation",
    "CfnAssociationProps",
    "CfnDocument",
    "CfnDocumentProps",
    "CfnMaintenanceWindow",
    "CfnMaintenanceWindowProps",
    "CfnMaintenanceWindowTarget",
    "CfnMaintenanceWindowTargetProps",
    "CfnMaintenanceWindowTask",
    "CfnMaintenanceWindowTaskProps",
    "CfnParameter",
    "CfnParameterProps",
    "CfnPatchBaseline",
    "CfnPatchBaselineProps",
    "CfnResourceDataSync",
    "CfnResourceDataSyncProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CommonStringParameterAttributes",
    "IParameter",
    "IStringListParameter",
    "IStringParameter",
    "ListParameterAttributes",
    "ParameterDataType",
    "ParameterOptions",
    "ParameterTier",
    "ParameterType",
    "ParameterValueType",
    "SecureStringParameterAttributes",
    "StringListParameter",
    "StringListParameterProps",
    "StringParameter",
    "StringParameterAttributes",
    "StringParameterProps",
]

publication.publish()

def _typecheckingstub__92579425f735301e17a993e7df464a283a7d42ba685c2d4205cf945db662d245(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    association_name: typing.Optional[builtins.str] = None,
    automation_target_parameter_name: typing.Optional[builtins.str] = None,
    calendar_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    compliance_severity: typing.Optional[builtins.str] = None,
    document_version: typing.Optional[builtins.str] = None,
    instance_id: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[builtins.str] = None,
    max_errors: typing.Optional[builtins.str] = None,
    output_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parameters: typing.Any = None,
    schedule_expression: typing.Optional[builtins.str] = None,
    schedule_offset: typing.Optional[jsii.Number] = None,
    sync_compliance: typing.Optional[builtins.str] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04dced959ace7c06e46713696a2e0111696820a92076dddbfb0d4e73ef74ff78(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1a0993d5c26d39b2f098659a8dbf1c928697492ab3d066975eff6b1a5799d2b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e92bf5492040a0299998b0a9b059a356249d33ec61a41eeee594e093a7d0fb93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9023084f7868b14116f97ca76b80fe2c8428bca0dc340c9e250534372a8882b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb049dd8f3d81baa9ccd163bb3c0e0c5f10114fd3a4d9ed4a1da2dfaa2e7a70c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784e8ad1b8f5f3c269d31598a3121d33ed36eb41074ed3c1c4d612eed6484920(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f46620766a6cb92f5e7135d5be6128d4d6e6dc8da7d7a49f8216a2bd89ce04(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e8a1f13b08374e8b174f211647e4f9aee7820e96b01b93747f906958e9aff43(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6852a105eba64031e2ab4c7f0f0c2569933f7be795a2d958593d091f277a667(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a40e1278e729960017eba97f7aaf904bfa9d528733d2142f2710e6cf17306f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a46c913675e9198e679ed1f83d648c1ccd40b2341879145404fd2ebc256093(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c0c0ebc4e8f350ab107d93e7f4ebce7994eb4e9c23da3d470fbd5a5fd349e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f2d6bae4a2f47caddaa51675bf95100b06b460f639a924aec4c36f3e0dfe13(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssociation.InstanceAssociationOutputLocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7bc72c1573e12dfc32dfc15c4125adfa3aee907e4c231fb1dc195260483bca5(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b45e3419b475a4d33fe733aa9418e965aeddb232d631f9b2024913c92d22947(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae92d319670461482db27cc5bf559ad4df2f8df83ba4d88119ce8f83e9169873(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d7078ea082466fa5a28a7853d4916de9d395e0a7adf5ae826e9a2028bdb9a93(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ce3b93eff1353677d4fb546ad1db9172eecc860870a57f1426f1ff63ce088d4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssociation.TargetProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43bea7a30e23800585f05a151814b8ef7b0f58707fa06c13448e65157d2bac89(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c9f5eb48dae8552c932fed2a3854daa4ad977ed9796c37909bff98cd60fc4a(
    *,
    s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.S3OutputLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ca1813f2b90a1f8e54124b2a16a5661e9c22d218461bb08292623a1dd09123(
    *,
    output_s3_bucket_name: typing.Optional[builtins.str] = None,
    output_s3_key_prefix: typing.Optional[builtins.str] = None,
    output_s3_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e23bdeb61e8b0804a4fde32db838d3743a925dc709401804cd81e355e25bee0d(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb0c608fec68cefb540b911fce04c4316c075989d67e9aa888cb8f01cc7e0dac(
    *,
    name: builtins.str,
    apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    association_name: typing.Optional[builtins.str] = None,
    automation_target_parameter_name: typing.Optional[builtins.str] = None,
    calendar_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    compliance_severity: typing.Optional[builtins.str] = None,
    document_version: typing.Optional[builtins.str] = None,
    instance_id: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[builtins.str] = None,
    max_errors: typing.Optional[builtins.str] = None,
    output_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parameters: typing.Any = None,
    schedule_expression: typing.Optional[builtins.str] = None,
    schedule_offset: typing.Optional[jsii.Number] = None,
    sync_compliance: typing.Optional[builtins.str] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0587e99b7ec516726ff27f1c34b1714d8645ad06944d59be27a612537ddab2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: typing.Any,
    attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocument.AttachmentsSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    document_format: typing.Optional[builtins.str] = None,
    document_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    requires: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocument.DocumentRequiresProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_type: typing.Optional[builtins.str] = None,
    update_method: typing.Optional[builtins.str] = None,
    version_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e943c2273ff892e2fdd4d583a1890854bb12dbd590854b62347e2fa9562d5a14(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2188ce8a82f6b6d9f8be3fad6fa91e030961fe82ccfc50ea9018eb0ca9a5568f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5959ba776c476fbcff87b818558733698ac254ec78c13e966dec8b6d890dba49(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__175aeee83820e4c740052899af41bd6da137e36dc8a7c97e1979f2a38dfb8ad5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDocument.AttachmentsSourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78f0fc9dc92bbdeda2dcfc1e140d76d56dba997674014f72aaf4c862bf73256(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1470169f5980c3b4dc4cbba07fd16d25490957e1af4df9aaa44a046e8043856f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b1ce30b81e0af0ed907c214243ea20a6ec6304887e3dd6da9e7f40c535dfd3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f21e2047334ed6671ad1892afe1b670d99e12c8d4d4404c82dc71a489c595d3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDocument.DocumentRequiresProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__562d6c2a06cbb316f503d8b64a06c9f80424782257db2c710c729b1f8466d90f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05561a31234b57ff868b8ce303562a7ae870c3d8d67ddf5a4937ba4df268d903(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ecd7f9b655f49b73ab05cdb2e63068bb0cb928f2b663d4563fb23457450917(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa50c9cd05e6bdac375dbcdf81332154e8628548ba5da12e0a6064a42b8587d7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af3bdb71c8069e4c4385fdecf788d6f19e9cf5a960b1f847f9e68fa3bc0bd8c(
    *,
    key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef1956d3e7560ca3d8bf2295207e843bbdd851217757941ff4d603fe26e3ceb(
    *,
    name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25566dec89d0b8b9f0c9ebb93fd7f63988acea14deb943fd94cfe89a3d03a14a(
    *,
    content: typing.Any,
    attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocument.AttachmentsSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    document_format: typing.Optional[builtins.str] = None,
    document_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    requires: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocument.DocumentRequiresProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_type: typing.Optional[builtins.str] = None,
    update_method: typing.Optional[builtins.str] = None,
    version_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad1b2a4216045934da690d96bf97784e2924381a651333920a48e8bccaa28bed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allow_unassociated_targets: typing.Union[builtins.bool, _IResolvable_da3f097b],
    cutoff: jsii.Number,
    duration: jsii.Number,
    name: builtins.str,
    schedule: builtins.str,
    description: typing.Optional[builtins.str] = None,
    end_date: typing.Optional[builtins.str] = None,
    schedule_offset: typing.Optional[jsii.Number] = None,
    schedule_timezone: typing.Optional[builtins.str] = None,
    start_date: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf2d9bcb608aa3fdea2507f7b28a1b89f11d7986467106d573d646ed1bd6c09(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e48a97af13ee9ec2b735682801a3c97b65f0385eaa8f17565b7437c7d55503(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b59de04623e80b94c25e028af2976d77afe2bc536f6dd59cd55cec25843686a(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d56bec4e39b855ff10336eb33b0d79cd1e1176cf1b7f78e5e405719c4eca1f2d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5c28ccb571d4df4caa3b264761f43b63e629207366a74c8d3f485171df3bc4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__995c29377559e15e0f1c56e36005d64d6364a914f20d79cfc82b5914d73bd876(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f38a694c05ce44a00d9222454ce9730a88ab55b543178b87550f611fa66317(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28aeaf50f7690fe17faf3319ac5908dca8bb57fac700b1295b0de46996a76ff3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96bd2ef248cf8835b029f6a8d83774b266650f228ec191067204d5eef38b6d70(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e109a6d18454ed60fdaa5c9f3665397d813614a627e51216d6a6c4c328f703a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8759638f42d7bafe21e1d7ac7c933693408b493eb89b2e82e61fb4407805b0e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a011b6550ec143adc25e489b9d0cd4d88120fed5047ded6ab0b4191dcda41f59(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff8aedf9ec0e769950717671246b7841aefbc47689520e9925ec90bc7e70a148(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e76d52f884f4303547d94985493397dbda06375d2fb22bef09cd893b8126578e(
    *,
    allow_unassociated_targets: typing.Union[builtins.bool, _IResolvable_da3f097b],
    cutoff: jsii.Number,
    duration: jsii.Number,
    name: builtins.str,
    schedule: builtins.str,
    description: typing.Optional[builtins.str] = None,
    end_date: typing.Optional[builtins.str] = None,
    schedule_offset: typing.Optional[jsii.Number] = None,
    schedule_timezone: typing.Optional[builtins.str] = None,
    start_date: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2179f5bf9c66eb25232096c54c2b6db2fe7f605be13acfcdbc1bae1e8a27cf5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_type: builtins.str,
    targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, typing.Dict[builtins.str, typing.Any]]]]],
    window_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    owner_information: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f471a86408fc354ec99155aa301b1a033e814a122604764e6b408635b1277b2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a50ede4d01d25c69fe012a9b8cbe9ca79f322d9e3381d509a9e366d6e5f8b21f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a13388269754c40d63f1299c7452e64c78999e96e3c4e045f5b0d2e28a6a50d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__803208e9f40c4e62295f82d8ba5e2943d3dba56d9a7f29d414b3e56f6b4ffdb3(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTarget.TargetsProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f880c1d4dc9c35b640f583b5a1eae791d6b9aba785b421257fce0c13f84f94ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd052b26378460dad14d691180cd79953a8b934b32bf7c740b62447530a2480b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12333ebaf74b7018641702cfa3157bc7e93dd94bce92bbf2ba08eb43c2e47c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7edbe00367604f6dbbbf871d14ab1b0b6484dc2ec9985bdff2795cb5d1183d4e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f385d4e9e8ebe3c37486729db165f1ed4064a2d660f424ea0550addace9d949(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19925b4e71098d1d7c3ce4f156f1dd7af4f0d2c164edb55bdbb1bc8cefb0b22(
    *,
    resource_type: builtins.str,
    targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, typing.Dict[builtins.str, typing.Any]]]]],
    window_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    owner_information: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab957de8d8a36935188de8e7d81d523e1ab1253ec8aab9717d062cb647fc726(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    priority: jsii.Number,
    task_arn: builtins.str,
    task_type: builtins.str,
    window_id: builtins.str,
    cutoff_behavior: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    logging_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_concurrency: typing.Optional[builtins.str] = None,
    max_errors: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    task_invocation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_parameters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e4d0dade8da18d6c77b051157c365c8b25a5b6997ae831a7a6fc9dc9203061(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec35f80592307cae2cc9e343334a35f2ed35398df071ffe5e875583ecd86cb3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0776f1dec28892f4f039655f4bd58dbab218be1a93993a08a46b2b3fee1a05f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adccf6935c75e32f84ba21008278bed07a786695c2220217c969ece517a13e19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e764d7191dd17ad7c6af4e9cf3288e2143c2b9bebf0395428c7823743dc7e4ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4911136cee1564bf01fe47e9aee783650f347033d01719aeec40bbbfa56ab6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56747468a672310155a1a7bd35fab9b92e4e9c51a4e0adec7ff48e95da06e65(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f65b28dee7cbeaeef25a47438a9bee61026d458be2cbab4f789904d33e0ca84(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7420eb69352c5dffbc63903691d96642ddd213905d4bd87088eb40562b6c37b7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.LoggingInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2c1e1cc2613320a5ea339c1908852d8fafbd3051c7edda4b2494635526ea55(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba4e556931384c4cf77d1adc667d26d5be5fe17ea89e74b7cfd53f51ed9d3d1c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce0290645c39827e48ca0d011a90f954ce1b5035c94f2b2a84769599cd94116a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa12d14b73c4415f857256339d8c9efbbeb6b154b5de888ae2db34a195687f34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba1a5fa6e80a94431946dcbb6c59475e65e96ae172de3aac908aa8b1fbbad49c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.TargetProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e676346c741943a2f14e79e926c8b5230365f4924b6a9161db3fc3486bab0d22(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMaintenanceWindowTask.TaskInvocationParametersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308ea737f8a21130dc4ef906e4efbdd26c268158e16c66982b9d8f555370f880(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbb39dc4cd39115a407f4e0e21302b4fce66ba760a368fafa0c26eb9621b52ba(
    *,
    cloud_watch_log_group_name: typing.Optional[builtins.str] = None,
    cloud_watch_output_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b0aefccdd3eb793a2d8676899122ea22603064cb2b55d0a5657cc2772cff4aa(
    *,
    region: builtins.str,
    s3_bucket: builtins.str,
    s3_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d47f7c3b4729bc4c5e324a0169340617ced800e35e73c55674ef6d731fbbc0a7(
    *,
    document_version: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49f94512f6a22e24e49adf01fdbcf2f071f6443d79613410ed49f6eb9c20b4ea(
    *,
    client_context: typing.Optional[builtins.str] = None,
    payload: typing.Optional[builtins.str] = None,
    qualifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e9c786755609427df5303964986a560cf57e26ca86a0fa4cdb6a67584f7aa01(
    *,
    cloud_watch_output_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    comment: typing.Optional[builtins.str] = None,
    document_hash: typing.Optional[builtins.str] = None,
    document_hash_type: typing.Optional[builtins.str] = None,
    document_version: typing.Optional[builtins.str] = None,
    notification_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.NotificationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    output_s3_bucket_name: typing.Optional[builtins.str] = None,
    output_s3_key_prefix: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    service_role_arn: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7504990f1dfcd8b7592c3b3b181643afde2c73cc8e80cefa0b86447b9907e340(
    *,
    input: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52d349a1b5c42894659cd315e4a94c0638dbfb6be76c7ac4ea3af2a1e11f464(
    *,
    notification_arn: builtins.str,
    notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    notification_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b4f690ce6831bb5a0c842fcfe936ca232781e02d69bf2787636fec601c5bbd4(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c4d0f27b97034ab166224c30178c332f8ccc78c97088665138b97e1125dbc23(
    *,
    maintenance_window_automation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maintenance_window_lambda_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maintenance_window_run_command_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maintenance_window_step_functions_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a897371c334ec198a4346a790b33c5836646788eb0a73ef18f8c56d7c89a1da3(
    *,
    priority: jsii.Number,
    task_arn: builtins.str,
    task_type: builtins.str,
    window_id: builtins.str,
    cutoff_behavior: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    logging_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_concurrency: typing.Optional[builtins.str] = None,
    max_errors: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    task_invocation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_parameters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84f5ae628815b139c6b10b41675bde183ddd347469f32bde65a41e5d61495260(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    type: builtins.str,
    value: builtins.str,
    allowed_pattern: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    policies: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f3bad2b3db06c9a38c47a358cad4cefd9300a72bd8e07b1ef1bc420f4b50672(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea040d39901531e947210b790fd2aefea3474d073cd628aa40d996921aada583(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3c8b1ff99cbeb84d6bfa4ec55c0f338baba344c4f051a0df40febf91e77b57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d784f981b1fc2fc2f326f9c00450c9509a7f7f86b9e9c7aa8701327c2cfc389(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ffaa1025f846ad6a1c834ac9cdadb606682213a46ea55fc7ef79f038fc126c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd34f48cc80688e3dee3c3e867bce351bd1d94df72caf85b542394330a8aeed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7395ed2d127b103cdc493e73e958c2b96d25307408ac9f8056cb7f8c798f4d39(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d1b8e4a82c71a91758906c6a03031ca428e2b03893385cf6e7897fedbbacd6b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb1627df3e7fc8ca9be15411b137e27706b40b83c560792cf371422ee8ec910(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f4d99885d1dde8bc3c789853e6ea39c5cd0a37d0d287307cad2a15a84707f4(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb309cb97ef3622d8ccca3962a03b455578863222196e6d48ee076e28591cdc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f89012f4986143c527853d7179ea46d1a3002d4025caeaa2123f32786cfdef8(
    *,
    type: builtins.str,
    value: builtins.str,
    allowed_pattern: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    policies: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b87565e6649bbe5a503013adf6ae874b3dc918c05cd6b120b99a77e88b0b389(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    approval_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.RuleGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    approved_patches_compliance_level: typing.Optional[builtins.str] = None,
    approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    default_baseline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    global_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    operating_system: typing.Optional[builtins.str] = None,
    patch_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    rejected_patches_action: typing.Optional[builtins.str] = None,
    sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.PatchSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92307c615f0f17e5616c309d2fdf068be7a53d7ad171009574d4a7aec995eecb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c378f609536815c9c7b9fbe787c900b25bb0c7b14a2373df0ebb0ebe8b9ac55(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0c34df6132dc5024ae19aefdba7302eb801aba72f7c63d23a2977bb99d1ce66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b56dfe31210955c8b1e478e9b12fb384520f16c624a7f1fd4ca7edc6c9d052e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.RuleGroupProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb6e3b5beff742671c1a2d820ffcd05e84cefb124894eba054fac867f1c23bc(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff7659e5eeaba10646c1802753fc8aa922feac17eee3bc2e16dadf1450be553(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__596ca4adbe9b66ae96ac84884c609e25720aab40b7f9d665e6ea16808f1a16ca(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82f38addd776fccd7d2225bc356d9a6e4dc42b938cbf56c083c34cd4994c239(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e0764881f21962614874d74c4570aaad8c8757ec8f88735329f4ff151db61a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2179c7d6864a34b00339c58eb461fef37a68a420e457e90e7c0c7a25130bfbdf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.PatchFilterGroupProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c5260a35c066fde54beec3890872a19db9827a2ab6171144440289a949dffe9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26a4ed06dc125b4ee77b4188a5d083535e272de23709a82c49ee2701451adddd(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1770686b2069f49c778417afc185314be92ad98da528f69041a98291bbffdf6(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f95da053faafa2fab292f8a8670cf900b1d6f8c4edba0b0adb5dc8cb58a805c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0b14c56c59457cef6fb23f44714aa782c4d1965f4fe83bb31bf5f3ff58e6d22(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPatchBaseline.PatchSourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc0a5821b51a90338294cb305cbf01102292e653fb3aa3f3b379b34ab3a9d0b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4622cb951de1b8fae6c5273a7cead99726f2ae144454c05b4a4b1393a6da770(
    *,
    patch_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.PatchFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da7d74139bb37dc7d779767e1fd22b1c75774ef3272087902bdecbc1873f1b1e(
    *,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec545f14b2e356c189699b3d1d51584fde777d8764ed9d5b8ea53e0419a450c4(
    *,
    configuration: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    products: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb925a5a684e1a98e75f665a82421705d4d1af563c5893a0c6a712180618db72(
    *,
    patch_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc64444abb423fe6f774ad5b2ff12d0f2a189d9ce78b6c8500268e76f1abdbc(
    *,
    approve_after_days: typing.Optional[jsii.Number] = None,
    approve_until_date: typing.Optional[builtins.str] = None,
    compliance_level: typing.Optional[builtins.str] = None,
    enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    patch_filter_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff6666a30d275f2a85d64de631c940fb83198b8b5a376b87a3a684f4a2dddf80(
    *,
    name: builtins.str,
    approval_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.RuleGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    approved_patches_compliance_level: typing.Optional[builtins.str] = None,
    approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    default_baseline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    global_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    operating_system: typing.Optional[builtins.str] = None,
    patch_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    rejected_patches_action: typing.Optional[builtins.str] = None,
    sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPatchBaseline.PatchSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8a24f4d86cad49691c9635278face17e76a24ad5a69daef9687e1e2d395158c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    sync_name: builtins.str,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    bucket_region: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    s3_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDataSync.S3DestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sync_format: typing.Optional[builtins.str] = None,
    sync_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDataSync.SyncSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sync_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f6022ac7efc29929aa079bf79384c8ac5f0ba1718316a5dd4e06c591b9203d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52d300d9d7ba1380e74c90a6b3b244b38158a194c79ff32598a2bb7a06e0603d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c904544eb14d61bbdd853398a4e1561df17c1a6dbed2a5cec6fa0c804f538935(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5fa255fdf6d438f6ead55de15298ce164aeda7ca776148e57fdae84a901f60c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a924763b3a0b031560d9453176bd0f0f3a33209abc82be03fd9bf29cf6d0d559(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb2a87b52c756e5533d55b08fe153a077d0b17d2d12326edf29ea9e3aa883c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd64605b976fdaf20986b520b1f9002208a35fba878e5874ecbba8eac65dbce3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b7a3560b2c82654cd5bf6fbf841a21a5f937cad116af54ea4ddd8a8d62231d8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDataSync.S3DestinationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ab77fd76bb25d5f48e8e3d49dfc9bc861b987ebca523a2e7fca2a67a78a7f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__157e7eb014224199daee91a842f040069c8ada6fa6deb70c8401e5815620c3e5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceDataSync.SyncSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d63d5c9fe36723e0e44dc178597f64394fe6601f2bea49c310bbb449d99b5c06(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be83b6195e85fbee2558cb31697cb6e11f4697ac92613c317e23b837253bc9dd(
    *,
    organization_source_type: builtins.str,
    organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b78c67544ca2178e6a7855605a8caef43993dcfa332e0612430a58da945d418d(
    *,
    bucket_name: builtins.str,
    bucket_region: builtins.str,
    sync_format: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8e974fe62ffae098cb7f57d7ea4db9b8d0aafbbba47aa7622d2bdcc0405b8e(
    *,
    source_regions: typing.Sequence[builtins.str],
    source_type: builtins.str,
    aws_organizations_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDataSync.AwsOrganizationsSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_future_regions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26353d4906971bfc49271a95bc4480dfb3fac99c43391b8a0aa7279209b75bb5(
    *,
    sync_name: builtins.str,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    bucket_region: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    s3_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDataSync.S3DestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sync_format: typing.Optional[builtins.str] = None,
    sync_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceDataSync.SyncSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sync_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fde734ca585a99029a54306ff0fc2e0b9d248ae4e5ec6603d9179a5e18853eb2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy: typing.Any,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4438689c231c110627ddbc405746a39736b727da60a710b45de0af51827c80b1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e11274985c814298f7c85bdcfe1dca0d664c308ed58fd52b21ee54096829327b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e10ca1482b529c76d3760f3dda887f46d2071ff060e4a0a11d253064701edec(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd166322a09f9cd5b0060ba3a485fb9349539a442b3ae8ec7ee33b0ad035d8f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__641aa0c71c4c89cb2aee737e31b19b3ae0745b8943985fb6855da98262576855(
    *,
    policy: typing.Any,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f4e05a41320bc1b3f1ba81e5056d43a2052eca526364b7ba62177a7542034f(
    *,
    parameter_name: builtins.str,
    simple_name: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__893dbe773f4eba8ae68bead053c2684acc5663f3c6568bf7b8860bed6523f05c(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6ae2a6ac121e36c84da0bbab30988cb29b98a2a83327833cd5a201ac06b622(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa32518e1d362afcbf135bf8697e59bfcd27563570e63250f9b6ad629ce1479(
    *,
    parameter_name: builtins.str,
    simple_name: typing.Optional[builtins.bool] = None,
    element_type: typing.Optional[ParameterValueType] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54be6c6ec55adec6de5f0a4b285882a64b6047fff6c35192fc38b5de44f05ec5(
    *,
    allowed_pattern: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    simple_name: typing.Optional[builtins.bool] = None,
    tier: typing.Optional[ParameterTier] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c29a999cdf02428bb99b29e94af353e96064d305daa31ac2e3c9bbd7cff7dee(
    *,
    parameter_name: builtins.str,
    simple_name: typing.Optional[builtins.bool] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94de6d51dda014e2ac4e863b9f9611f97d1e28dc774309241f1b4d807451758f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    string_list_value: typing.Sequence[builtins.str],
    allowed_pattern: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    simple_name: typing.Optional[builtins.bool] = None,
    tier: typing.Optional[ParameterTier] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b477545ed5d53e5b666f41087db25aa6bdc347c4cead18a586bd16678f612801(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    element_type: typing.Optional[ParameterValueType] = None,
    version: typing.Optional[jsii.Number] = None,
    parameter_name: builtins.str,
    simple_name: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee02d93e11a637ffc18281f9eda840005cd8f1adec7265948e87be3b063fd8b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    string_list_parameter_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b9ae745d086e0dea148aea94e9f88d8efd375fa182578d056bcfd3fd08b1771(
    scope: _constructs_77d1e7e8.Construct,
    parameter_name: builtins.str,
    type: typing.Optional[ParameterValueType] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__819241aedbf400f619f3bb1dab30b0594eef1072ffeee79fad21356c807bec86(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6c74a7f6bd369fd4593adcf2cfb417138607dd7b20b5da6ea534219eee0c55(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fda8a7b3397aad49f6c3720e316364d4df6b092c111c31c5e48e223f7ab4b46(
    *,
    allowed_pattern: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    simple_name: typing.Optional[builtins.bool] = None,
    tier: typing.Optional[ParameterTier] = None,
    string_list_value: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2eeba991f657f464e2410cd38fdeecff2bdaa0b51e35cd0e4ca251c97217a46(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    string_value: builtins.str,
    data_type: typing.Optional[ParameterDataType] = None,
    type: typing.Optional[ParameterType] = None,
    allowed_pattern: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    simple_name: typing.Optional[builtins.bool] = None,
    tier: typing.Optional[ParameterTier] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef716b2d64b7c95b87119e190e88504880c3f46c45b769e05e9f4f805b08c63d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    version: typing.Optional[jsii.Number] = None,
    parameter_name: builtins.str,
    simple_name: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e612c2654654e8b8bb7821bcd1e47680b025862a2a411467ffa6334e46371b05(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    force_dynamic_reference: typing.Optional[builtins.bool] = None,
    type: typing.Optional[ParameterType] = None,
    value_type: typing.Optional[ParameterValueType] = None,
    version: typing.Optional[jsii.Number] = None,
    parameter_name: builtins.str,
    simple_name: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb0299149e02d9543818343516306f4b32ee1ac5f245ff3c79ee5fd2016ec670(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    string_parameter_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38dfc6aee7234162b6dfa7fd6d79daf1e5e20fb93a83a884110ee85c9406a842(
    scope: _constructs_77d1e7e8.Construct,
    parameter_name: builtins.str,
    version: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__587bcd33299d81a1c2d922ca6d8a6c0dbb1a57b5bf5619f44b25a23071ffcf19(
    scope: _constructs_77d1e7e8.Construct,
    parameter_name: builtins.str,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ddd12c8dffbad4b7f599d939f1683184715d90ae73713323484cf1f89d0f99(
    scope: _constructs_77d1e7e8.Construct,
    parameter_name: builtins.str,
    type: typing.Optional[ParameterType] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ec30255f3ac830ba0695e062a34e2012e0542d68a61c236b791945a367b24b(
    scope: _constructs_77d1e7e8.Construct,
    parameter_name: builtins.str,
    type: typing.Optional[ParameterValueType] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__352ba5506c7762dcb469028a7b0515dc3daed2b43c5a8ff339ed16372f650250(
    scope: _constructs_77d1e7e8.Construct,
    parameter_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2b954516f020047895372042cbf3497906d242b8a2c10008ce8a5c2e1335370(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9601cc05d10fcfadbdc97c8deacf47393567be2f0e90bd28ea11cdfe571976fa(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045695ee32d353600237b891b14ad138098a0add8ba99199144ee57eff4ad99f(
    *,
    parameter_name: builtins.str,
    simple_name: typing.Optional[builtins.bool] = None,
    force_dynamic_reference: typing.Optional[builtins.bool] = None,
    type: typing.Optional[ParameterType] = None,
    value_type: typing.Optional[ParameterValueType] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a14e5cea1d211f374b7c289d526224c03be1f2e91a2a94cbcdf8f1d251335822(
    *,
    allowed_pattern: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    simple_name: typing.Optional[builtins.bool] = None,
    tier: typing.Optional[ParameterTier] = None,
    string_value: builtins.str,
    data_type: typing.Optional[ParameterDataType] = None,
    type: typing.Optional[ParameterType] = None,
) -> None:
    """Type checking stubs"""
    pass
