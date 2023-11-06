'''
# AWS Elastic Beanstalk Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_elasticbeanstalk as elasticbeanstalk
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ElasticBeanstalk construct libraries](https://constructs.dev/search?q=elasticbeanstalk)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ElasticBeanstalk resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElasticBeanstalk.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ElasticBeanstalk](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElasticBeanstalk.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplication",
):
    '''Specify an AWS Elastic Beanstalk application by using the AWS::ElasticBeanstalk::Application resource in an AWS CloudFormation template.

    The AWS::ElasticBeanstalk::Application resource is an AWS Elastic Beanstalk Beanstalk resource type that specifies an Elastic Beanstalk application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
        
        cfn_application = elasticbeanstalk.CfnApplication(self, "MyCfnApplication",
            application_name="applicationName",
            description="description",
            resource_lifecycle_config=elasticbeanstalk.CfnApplication.ApplicationResourceLifecycleConfigProperty(
                service_role="serviceRole",
                version_lifecycle_config=elasticbeanstalk.CfnApplication.ApplicationVersionLifecycleConfigProperty(
                    max_age_rule=elasticbeanstalk.CfnApplication.MaxAgeRuleProperty(
                        delete_source_from_s3=False,
                        enabled=False,
                        max_age_in_days=123
                    ),
                    max_count_rule=elasticbeanstalk.CfnApplication.MaxCountRuleProperty(
                        delete_source_from_s3=False,
                        enabled=False,
                        max_count=123
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
        application_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        resource_lifecycle_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.ApplicationResourceLifecycleConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_name: A name for the Elastic Beanstalk application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param description: Your description of the application.
        :param resource_lifecycle_config: Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2037a8b39c672f9e224a0d55f87a787c8f06cc34801647c616c1d3544fc61b01)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            application_name=application_name,
            description=description,
            resource_lifecycle_config=resource_lifecycle_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67008ad4d98231202ed96bd8356ff5d52d6ab2ac0b949ec39dee9c2e5b28516c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94e3218203e8d26f754fc4833f6d89df4a7aed57f2b40ba41097383e596f90ec)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[builtins.str]:
        '''A name for the Elastic Beanstalk application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6bf36c756c98eefc03fcfa7fc47b01fa9a2e1bbbcdea2614f2cbbe19f2ac5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Your description of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c92d2b49bcac99b2f1f38ca944c407acf1d8ac8d05cf0061b761bacef80edaeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLifecycleConfig")
    def resource_lifecycle_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ApplicationResourceLifecycleConfigProperty"]]:
        '''Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ApplicationResourceLifecycleConfigProperty"]], jsii.get(self, "resourceLifecycleConfig"))

    @resource_lifecycle_config.setter
    def resource_lifecycle_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ApplicationResourceLifecycleConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a75fb3cf2d34861537e2d37fd676dbea69752fd913fa7086637904894d1654f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLifecycleConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplication.ApplicationResourceLifecycleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "service_role": "serviceRole",
            "version_lifecycle_config": "versionLifecycleConfig",
        },
    )
    class ApplicationResourceLifecycleConfigProperty:
        def __init__(
            self,
            *,
            service_role: typing.Optional[builtins.str] = None,
            version_lifecycle_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.ApplicationVersionLifecycleConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Use the ``ApplicationResourceLifecycleConfig`` property type to specify lifecycle settings for resources that belong to an AWS Elastic Beanstalk application when defining an AWS::ElasticBeanstalk::Application resource in an AWS CloudFormation template.

            The resource lifecycle configuration for an application. Defines lifecycle settings for resources that belong to the application, and the service role that Elastic Beanstalk assumes in order to apply lifecycle settings. The version lifecycle configuration defines lifecycle settings for application versions.

            ``ApplicationResourceLifecycleConfig`` is a property of the `AWS::ElasticBeanstalk::Application <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html>`_ resource.

            :param service_role: The ARN of an IAM service role that Elastic Beanstalk has permission to assume. The ``ServiceRole`` property is required the first time that you provide a ``ResourceLifecycleConfig`` for the application. After you provide it once, Elastic Beanstalk persists the Service Role with the application, and you don't need to specify it again. You can, however, specify it in subsequent updates to change the Service Role to another value.
            :param version_lifecycle_config: Defines lifecycle settings for application versions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                application_resource_lifecycle_config_property = elasticbeanstalk.CfnApplication.ApplicationResourceLifecycleConfigProperty(
                    service_role="serviceRole",
                    version_lifecycle_config=elasticbeanstalk.CfnApplication.ApplicationVersionLifecycleConfigProperty(
                        max_age_rule=elasticbeanstalk.CfnApplication.MaxAgeRuleProperty(
                            delete_source_from_s3=False,
                            enabled=False,
                            max_age_in_days=123
                        ),
                        max_count_rule=elasticbeanstalk.CfnApplication.MaxCountRuleProperty(
                            delete_source_from_s3=False,
                            enabled=False,
                            max_count=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cab1602adff55377880de5336c8a2e9ecfcfe203ea299cbb9dec79dc27168b2c)
                check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
                check_type(argname="argument version_lifecycle_config", value=version_lifecycle_config, expected_type=type_hints["version_lifecycle_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if service_role is not None:
                self._values["service_role"] = service_role
            if version_lifecycle_config is not None:
                self._values["version_lifecycle_config"] = version_lifecycle_config

        @builtins.property
        def service_role(self) -> typing.Optional[builtins.str]:
            '''The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

            The ``ServiceRole`` property is required the first time that you provide a ``ResourceLifecycleConfig`` for the application. After you provide it once, Elastic Beanstalk persists the Service Role with the application, and you don't need to specify it again. You can, however, specify it in subsequent updates to change the Service Role to another value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-servicerole
            '''
            result = self._values.get("service_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version_lifecycle_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ApplicationVersionLifecycleConfigProperty"]]:
            '''Defines lifecycle settings for application versions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-versionlifecycleconfig
            '''
            result = self._values.get("version_lifecycle_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ApplicationVersionLifecycleConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationResourceLifecycleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplication.ApplicationVersionLifecycleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"max_age_rule": "maxAgeRule", "max_count_rule": "maxCountRule"},
    )
    class ApplicationVersionLifecycleConfigProperty:
        def __init__(
            self,
            *,
            max_age_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.MaxAgeRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            max_count_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.MaxCountRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Use the ``ApplicationVersionLifecycleConfig`` property type to specify application version lifecycle settings for an AWS Elastic Beanstalk application when defining an AWS::ElasticBeanstalk::Application resource in an AWS CloudFormation template.

            The application version lifecycle settings for an application. Defines the rules that Elastic Beanstalk applies to an application's versions in order to avoid hitting the per-region limit for application versions.

            When Elastic Beanstalk deletes an application version from its database, you can no longer deploy that version to an environment. The source bundle remains in S3 unless you configure the rule to delete it.

            ``ApplicationVersionLifecycleConfig`` is a property of the `ApplicationResourceLifecycleConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html>`_ property type.

            :param max_age_rule: Specify a max age rule to restrict the length of time that application versions are retained for an application.
            :param max_count_rule: Specify a max count rule to restrict the number of application versions that are retained for an application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                application_version_lifecycle_config_property = elasticbeanstalk.CfnApplication.ApplicationVersionLifecycleConfigProperty(
                    max_age_rule=elasticbeanstalk.CfnApplication.MaxAgeRuleProperty(
                        delete_source_from_s3=False,
                        enabled=False,
                        max_age_in_days=123
                    ),
                    max_count_rule=elasticbeanstalk.CfnApplication.MaxCountRuleProperty(
                        delete_source_from_s3=False,
                        enabled=False,
                        max_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57d77f447c2f85e748e224d6919c6b28bd509c15cb6d45958762ec3dddfd0a31)
                check_type(argname="argument max_age_rule", value=max_age_rule, expected_type=type_hints["max_age_rule"])
                check_type(argname="argument max_count_rule", value=max_count_rule, expected_type=type_hints["max_count_rule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_age_rule is not None:
                self._values["max_age_rule"] = max_age_rule
            if max_count_rule is not None:
                self._values["max_count_rule"] = max_count_rule

        @builtins.property
        def max_age_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MaxAgeRuleProperty"]]:
            '''Specify a max age rule to restrict the length of time that application versions are retained for an application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxagerule
            '''
            result = self._values.get("max_age_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MaxAgeRuleProperty"]], result)

        @builtins.property
        def max_count_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MaxCountRuleProperty"]]:
            '''Specify a max count rule to restrict the number of application versions that are retained for an application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxcountrule
            '''
            result = self._values.get("max_count_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.MaxCountRuleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationVersionLifecycleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplication.MaxAgeRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_source_from_s3": "deleteSourceFromS3",
            "enabled": "enabled",
            "max_age_in_days": "maxAgeInDays",
        },
    )
    class MaxAgeRuleProperty:
        def __init__(
            self,
            *,
            delete_source_from_s3: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_age_in_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Use the ``MaxAgeRule`` property type to specify a max age rule to restrict the length of time that application versions are retained for an AWS Elastic Beanstalk application when defining an AWS::ElasticBeanstalk::Application resource in an AWS CloudFormation template.

            A lifecycle rule that deletes application versions after the specified number of days.

            ``MaxAgeRule`` is a property of the `ApplicationVersionLifecycleConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html>`_ property type.

            :param delete_source_from_s3: Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.
            :param enabled: Specify ``true`` to apply the rule, or ``false`` to disable it.
            :param max_age_in_days: Specify the number of days to retain an application versions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                max_age_rule_property = elasticbeanstalk.CfnApplication.MaxAgeRuleProperty(
                    delete_source_from_s3=False,
                    enabled=False,
                    max_age_in_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__85ed97d29f0279d47ee3340de9177215f38b5a970ec931a1b64762af5da76bfd)
                check_type(argname="argument delete_source_from_s3", value=delete_source_from_s3, expected_type=type_hints["delete_source_from_s3"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument max_age_in_days", value=max_age_in_days, expected_type=type_hints["max_age_in_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_source_from_s3 is not None:
                self._values["delete_source_from_s3"] = delete_source_from_s3
            if enabled is not None:
                self._values["enabled"] = enabled
            if max_age_in_days is not None:
                self._values["max_age_in_days"] = max_age_in_days

        @builtins.property
        def delete_source_from_s3(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-deletesourcefroms3
            '''
            result = self._values.get("delete_source_from_s3")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify ``true`` to apply the rule, or ``false`` to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_age_in_days(self) -> typing.Optional[jsii.Number]:
            '''Specify the number of days to retain an application versions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-maxageindays
            '''
            result = self._values.get("max_age_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaxAgeRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplication.MaxCountRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_source_from_s3": "deleteSourceFromS3",
            "enabled": "enabled",
            "max_count": "maxCount",
        },
    )
    class MaxCountRuleProperty:
        def __init__(
            self,
            *,
            delete_source_from_s3: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Use the ``MaxAgeRule`` property type to specify a max count rule to restrict the number of application versions that are retained for an AWS Elastic Beanstalk application when defining an AWS::ElasticBeanstalk::Application resource in an AWS CloudFormation template.

            A lifecycle rule that deletes the oldest application version when the maximum count is exceeded.

            ``MaxCountRule`` is a property of the `ApplicationVersionLifecycleConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html>`_ property type.

            :param delete_source_from_s3: Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.
            :param enabled: Specify ``true`` to apply the rule, or ``false`` to disable it.
            :param max_count: Specify the maximum number of application versions to retain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                max_count_rule_property = elasticbeanstalk.CfnApplication.MaxCountRuleProperty(
                    delete_source_from_s3=False,
                    enabled=False,
                    max_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a27816fed8fa85ae75502cf6691d26ee691b6c71d47f8b4fab4ea659dbf0d13d)
                check_type(argname="argument delete_source_from_s3", value=delete_source_from_s3, expected_type=type_hints["delete_source_from_s3"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument max_count", value=max_count, expected_type=type_hints["max_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_source_from_s3 is not None:
                self._values["delete_source_from_s3"] = delete_source_from_s3
            if enabled is not None:
                self._values["enabled"] = enabled
            if max_count is not None:
                self._values["max_count"] = max_count

        @builtins.property
        def delete_source_from_s3(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-deletesourcefroms3
            '''
            result = self._values.get("delete_source_from_s3")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify ``true`` to apply the rule, or ``false`` to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_count(self) -> typing.Optional[jsii.Number]:
            '''Specify the maximum number of application versions to retain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-maxcount
            '''
            result = self._values.get("max_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaxCountRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "description": "description",
        "resource_lifecycle_config": "resourceLifecycleConfig",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        resource_lifecycle_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationResourceLifecycleConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param application_name: A name for the Elastic Beanstalk application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param description: Your description of the application.
        :param resource_lifecycle_config: Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
            
            cfn_application_props = elasticbeanstalk.CfnApplicationProps(
                application_name="applicationName",
                description="description",
                resource_lifecycle_config=elasticbeanstalk.CfnApplication.ApplicationResourceLifecycleConfigProperty(
                    service_role="serviceRole",
                    version_lifecycle_config=elasticbeanstalk.CfnApplication.ApplicationVersionLifecycleConfigProperty(
                        max_age_rule=elasticbeanstalk.CfnApplication.MaxAgeRuleProperty(
                            delete_source_from_s3=False,
                            enabled=False,
                            max_age_in_days=123
                        ),
                        max_count_rule=elasticbeanstalk.CfnApplication.MaxCountRuleProperty(
                            delete_source_from_s3=False,
                            enabled=False,
                            max_count=123
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31c1735cd136eec2821ea76e53787fc49838698c06b9830e11f3e4a61ecceab7)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument resource_lifecycle_config", value=resource_lifecycle_config, expected_type=type_hints["resource_lifecycle_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name
        if description is not None:
            self._values["description"] = description
        if resource_lifecycle_config is not None:
            self._values["resource_lifecycle_config"] = resource_lifecycle_config

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''A name for the Elastic Beanstalk application.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html#cfn-elasticbeanstalk-application-applicationname
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Your description of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html#cfn-elasticbeanstalk-application-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_lifecycle_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ApplicationResourceLifecycleConfigProperty]]:
        '''Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html#cfn-elasticbeanstalk-application-resourcelifecycleconfig
        '''
        result = self._values.get("resource_lifecycle_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ApplicationResourceLifecycleConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnApplicationVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplicationVersion",
):
    '''Specify an AWS Elastic Beanstalk application version by using the AWS::ElasticBeanstalk::ApplicationVersion resource in an AWS CloudFormation template.

    The AWS::ElasticBeanstalk::ApplicationVersion resource is an AWS Elastic Beanstalk resource type that specifies an application version, an iteration of deployable code, for an Elastic Beanstalk application.
    .. epigraph::

       After you create an application version with a specified Amazon S3 bucket and key location, you can't change that Amazon S3 location. If you change the Amazon S3 location, an attempt to launch an environment from the application version will fail.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
        
        cfn_application_version = elasticbeanstalk.CfnApplicationVersion(self, "MyCfnApplicationVersion",
            application_name="applicationName",
            source_bundle=elasticbeanstalk.CfnApplicationVersion.SourceBundleProperty(
                s3_bucket="s3Bucket",
                s3_key="s3Key"
            ),
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        source_bundle: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplicationVersion.SourceBundleProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_name: The name of the Elastic Beanstalk application that is associated with this application version.
        :param source_bundle: The Amazon S3 bucket and key that identify the location of the source bundle for this version. .. epigraph:: The Amazon S3 bucket must be in the same region as the environment.
        :param description: A description of this application version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1516c528cdf5646f1fbc2db47de8d7888e64c08ccc28b6b1ea3f1c451b19a4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationVersionProps(
            application_name=application_name,
            source_bundle=source_bundle,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__904e752e1e1668e8c5324ea8047fd950cbc7d9bd4e2add9803c8f86204e1bc54)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97d5a82ad81553feb3520c025f9dc451708bd07df2be9394343ed645575835b5)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the Elastic Beanstalk application that is associated with this application version.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27168377f8f2dcb4108fbfe1e434ca0369c6eb4b5fde30de3223efb36d74fc6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceBundle")
    def source_bundle(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnApplicationVersion.SourceBundleProperty"]:
        '''The Amazon S3 bucket and key that identify the location of the source bundle for this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApplicationVersion.SourceBundleProperty"], jsii.get(self, "sourceBundle"))

    @source_bundle.setter
    def source_bundle(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnApplicationVersion.SourceBundleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e851d2ec17de05de650c602ffaa2d9d6d18f2cb17466abca441fe30ac1b50d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceBundle", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this application version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2990bd41c8492714f738e92c7d46621588e6d2d20631de262c28b3b7bad07ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplicationVersion.SourceBundleProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_bucket": "s3Bucket", "s3_key": "s3Key"},
    )
    class SourceBundleProperty:
        def __init__(self, *, s3_bucket: builtins.str, s3_key: builtins.str) -> None:
            '''Use the ``SourceBundle`` property type to specify the Amazon S3 location of the source bundle for an AWS Elastic Beanstalk application version when defining an AWS::ElasticBeanstalk::ApplicationVersion resource in an AWS CloudFormation template.

            The ``SourceBundle`` property is an embedded property of the `AWS::ElasticBeanstalk::ApplicationVersion <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html>`_ resource. It specifies the Amazon S3 location of the source bundle for an AWS Elastic Beanstalk application version.

            :param s3_bucket: The Amazon S3 bucket where the data is located.
            :param s3_key: The Amazon S3 key where the data is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-applicationversion-sourcebundle.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                source_bundle_property = elasticbeanstalk.CfnApplicationVersion.SourceBundleProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bab0ce5312d0bfddca943d9bb19c1093f2bc6756b952bafc260c4c84b3c3d7b3)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The Amazon S3 bucket where the data is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-applicationversion-sourcebundle.html#cfn-elasticbeanstalk-applicationversion-sourcebundle-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''The Amazon S3 key where the data is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-applicationversion-sourcebundle.html#cfn-elasticbeanstalk-applicationversion-sourcebundle-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceBundleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnApplicationVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "source_bundle": "sourceBundle",
        "description": "description",
    },
)
class CfnApplicationVersionProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        source_bundle: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationVersion.SourceBundleProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplicationVersion``.

        :param application_name: The name of the Elastic Beanstalk application that is associated with this application version.
        :param source_bundle: The Amazon S3 bucket and key that identify the location of the source bundle for this version. .. epigraph:: The Amazon S3 bucket must be in the same region as the environment.
        :param description: A description of this application version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
            
            cfn_application_version_props = elasticbeanstalk.CfnApplicationVersionProps(
                application_name="applicationName",
                source_bundle=elasticbeanstalk.CfnApplicationVersion.SourceBundleProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                ),
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d59bfde6ef9919e591cebecf28041cd2684a7628953d69fbe6a460205d95f96)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument source_bundle", value=source_bundle, expected_type=type_hints["source_bundle"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "source_bundle": source_bundle,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the Elastic Beanstalk application that is associated with this application version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html#cfn-elasticbeanstalk-applicationversion-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_bundle(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnApplicationVersion.SourceBundleProperty]:
        '''The Amazon S3 bucket and key that identify the location of the source bundle for this version.

        .. epigraph::

           The Amazon S3 bucket must be in the same region as the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html#cfn-elasticbeanstalk-applicationversion-sourcebundle
        '''
        result = self._values.get("source_bundle")
        assert result is not None, "Required property 'source_bundle' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnApplicationVersion.SourceBundleProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this application version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html#cfn-elasticbeanstalk-applicationversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnConfigurationTemplate",
):
    '''Specify an AWS Elastic Beanstalk configuration template by using the AWS::ElasticBeanstalk::ConfigurationTemplate resource in an AWS CloudFormation template.

    The AWS::ElasticBeanstalk::ConfigurationTemplate resource is an AWS Elastic Beanstalk resource type that specifies an Elastic Beanstalk configuration template, associated with a specific Elastic Beanstalk application. You define application configuration settings in a configuration template. You can then use the configuration template to deploy different versions of the application with the same configuration settings.
    .. epigraph::

       The Elastic Beanstalk console and documentation often refer to configuration templates as *saved configurations* . When you set configuration options in a saved configuration (configuration template), Elastic Beanstalk applies them with a particular precedence as part of applying options from multiple sources. For more information, see `Configuration Options <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
        
        cfn_configuration_template = elasticbeanstalk.CfnConfigurationTemplate(self, "MyCfnConfigurationTemplate",
            application_name="applicationName",
        
            # the properties below are optional
            description="description",
            environment_id="environmentId",
            option_settings=[elasticbeanstalk.CfnConfigurationTemplate.ConfigurationOptionSettingProperty(
                namespace="namespace",
                option_name="optionName",
        
                # the properties below are optional
                resource_name="resourceName",
                value="value"
            )],
            platform_arn="platformArn",
            solution_stack_name="solutionStackName",
            source_configuration=elasticbeanstalk.CfnConfigurationTemplate.SourceConfigurationProperty(
                application_name="applicationName",
                template_name="templateName"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        environment_id: typing.Optional[builtins.str] = None,
        option_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationTemplate.ConfigurationOptionSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        platform_arn: typing.Optional[builtins.str] = None,
        solution_stack_name: typing.Optional[builtins.str] = None,
        source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationTemplate.SourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_name: The name of the Elastic Beanstalk application to associate with this configuration template.
        :param description: An optional description for this configuration.
        :param environment_id: The ID of an environment whose settings you want to use to create the configuration template. You must specify ``EnvironmentId`` if you don't specify ``PlatformArn`` , ``SolutionStackName`` , or ``SourceConfiguration`` .
        :param option_settings: Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see `Option Values <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .
        :param platform_arn: The Amazon Resource Name (ARN) of the custom platform. For more information, see `Custom Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* . .. epigraph:: If you specify ``PlatformArn`` , then don't specify ``SolutionStackName`` .
        :param solution_stack_name: The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, ``64bit Amazon Linux 2013.09 running Tomcat 7 Java 7`` . A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see `Supported Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* . You must specify ``SolutionStackName`` if you don't specify ``PlatformArn`` , ``EnvironmentId`` , or ``SourceConfiguration`` . Use the ```ListAvailableSolutionStacks`` <https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html>`_ API to obtain a list of available solution stacks.
        :param source_configuration: An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration. Values specified in ``OptionSettings`` override any values obtained from the ``SourceConfiguration`` . You must specify ``SourceConfiguration`` if you don't specify ``PlatformArn`` , ``EnvironmentId`` , or ``SolutionStackName`` . Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e16e4991a410c838f73cd94150f707bdc9d297ed64ed0f67e1bf183266f36923)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationTemplateProps(
            application_name=application_name,
            description=description,
            environment_id=environment_id,
            option_settings=option_settings,
            platform_arn=platform_arn,
            solution_stack_name=solution_stack_name,
            source_configuration=source_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c0e1a86d4ecaebaf21d17747fcb42a178fa22e102cd23a7b784ccca109c059c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c92b475285789cb6d89f2fa870fd45e9ca74a42e5089d6f75084cd5428c92930)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTemplateName")
    def attr_template_name(self) -> builtins.str:
        '''The name of the configuration template.

        :cloudformationAttribute: TemplateName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTemplateName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the Elastic Beanstalk application to associate with this configuration template.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7233e1b2fdf96b0719aad84afaf67d4e80b80e2216d53813200ab4083cd3d79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for this configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92814ce35605efc126107dacc2f3dd1e0a4a00bd47ea4d45b2b5e1a28fa51e7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of an environment whose settings you want to use to create the configuration template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentId"))

    @environment_id.setter
    def environment_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cce6105908a7c7d064a4708e87b39cc1ad0c08a1f6c23ef07b254920062b2b51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentId", value)

    @builtins.property
    @jsii.member(jsii_name="optionSettings")
    def option_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationTemplate.ConfigurationOptionSettingProperty"]]]]:
        '''Option values for the Elastic Beanstalk configuration, such as the instance type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationTemplate.ConfigurationOptionSettingProperty"]]]], jsii.get(self, "optionSettings"))

    @option_settings.setter
    def option_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationTemplate.ConfigurationOptionSettingProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d3d231a3a5e4ac5f74ffd51d127adf4d05bd0317b35ba4f5efa5c5b5d9d444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionSettings", value)

    @builtins.property
    @jsii.member(jsii_name="platformArn")
    def platform_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the custom platform.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformArn"))

    @platform_arn.setter
    def platform_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7cf33f9354e06bb7ba16714da3f9d8c5f45b8651992b1d188c273c9567b78b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformArn", value)

    @builtins.property
    @jsii.member(jsii_name="solutionStackName")
    def solution_stack_name(self) -> typing.Optional[builtins.str]:
        '''The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "solutionStackName"))

    @solution_stack_name.setter
    def solution_stack_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fda6098fc28e550f397aa00d810b4be6508b89d4f6c126a3f27b03001c3e7698)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "solutionStackName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationTemplate.SourceConfigurationProperty"]]:
        '''An Elastic Beanstalk configuration template to base this one on.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationTemplate.SourceConfigurationProperty"]], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationTemplate.SourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7ef0aa6a6895a3055a35a82ea9af1c29b76ca8fa807de3e85b831b17f7da10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnConfigurationTemplate.ConfigurationOptionSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "namespace": "namespace",
            "option_name": "optionName",
            "resource_name": "resourceName",
            "value": "value",
        },
    )
    class ConfigurationOptionSettingProperty:
        def __init__(
            self,
            *,
            namespace: builtins.str,
            option_name: builtins.str,
            resource_name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the ``ConfigurationOptionSetting`` property type to specify an option for an AWS Elastic Beanstalk configuration template when defining an AWS::ElasticBeanstalk::ConfigurationTemplate resource in an AWS CloudFormation template.

            The ``ConfigurationOptionSetting`` property type specifies an option for an AWS Elastic Beanstalk configuration template.

            The ``OptionSettings`` property of the `AWS::ElasticBeanstalk::ConfigurationTemplate <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-beanstalk-configurationtemplate.html>`_ resource contains a list of ``ConfigurationOptionSetting`` property types.

            For a list of possible namespaces and option values, see `Option Values <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .

            :param namespace: A unique namespace that identifies the option's associated AWS resource.
            :param option_name: The name of the configuration option.
            :param resource_name: A unique resource name for the option setting. Use it for a time–based scaling configuration option.
            :param value: The current value for the configuration option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                configuration_option_setting_property = elasticbeanstalk.CfnConfigurationTemplate.ConfigurationOptionSettingProperty(
                    namespace="namespace",
                    option_name="optionName",
                
                    # the properties below are optional
                    resource_name="resourceName",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__abed0b599f8199ae57be09e0e454fc0b760f0f0c57a3bf88601a9c9b318f29ae)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument option_name", value=option_name, expected_type=type_hints["option_name"])
                check_type(argname="argument resource_name", value=resource_name, expected_type=type_hints["resource_name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "namespace": namespace,
                "option_name": option_name,
            }
            if resource_name is not None:
                self._values["resource_name"] = resource_name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def namespace(self) -> builtins.str:
            '''A unique namespace that identifies the option's associated AWS resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def option_name(self) -> builtins.str:
            '''The name of the configuration option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-optionname
            '''
            result = self._values.get("option_name")
            assert result is not None, "Required property 'option_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_name(self) -> typing.Optional[builtins.str]:
            '''A unique resource name for the option setting.

            Use it for a time–based scaling configuration option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-resourcename
            '''
            result = self._values.get("resource_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The current value for the configuration option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationOptionSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnConfigurationTemplate.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_name": "applicationName",
            "template_name": "templateName",
        },
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            application_name: builtins.str,
            template_name: builtins.str,
        ) -> None:
            '''Use the ``SourceConfiguration`` property type to specify another AWS Elastic Beanstalk configuration template as the base to creating a new AWS::ElasticBeanstalk::ConfigurationTemplate resource in an AWS CloudFormation template.

            An AWS Elastic Beanstalk configuration template to base a new one on. You can use it to define a `AWS::ElasticBeanstalk::ConfigurationTemplate <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-beanstalk-configurationtemplate.html>`_ resource.

            :param application_name: The name of the application associated with the configuration.
            :param template_name: The name of the configuration template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                source_configuration_property = elasticbeanstalk.CfnConfigurationTemplate.SourceConfigurationProperty(
                    application_name="applicationName",
                    template_name="templateName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3fd0a38fbd1739c9c00badb2a396cea51ea99ab2d5bec33851b4206c1a8bfbf)
                check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
                check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_name": application_name,
                "template_name": template_name,
            }

        @builtins.property
        def application_name(self) -> builtins.str:
            '''The name of the application associated with the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-applicationname
            '''
            result = self._values.get("application_name")
            assert result is not None, "Required property 'application_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def template_name(self) -> builtins.str:
            '''The name of the configuration template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-templatename
            '''
            result = self._values.get("template_name")
            assert result is not None, "Required property 'template_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnConfigurationTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "description": "description",
        "environment_id": "environmentId",
        "option_settings": "optionSettings",
        "platform_arn": "platformArn",
        "solution_stack_name": "solutionStackName",
        "source_configuration": "sourceConfiguration",
    },
)
class CfnConfigurationTemplateProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        environment_id: typing.Optional[builtins.str] = None,
        option_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationTemplate.ConfigurationOptionSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        platform_arn: typing.Optional[builtins.str] = None,
        solution_stack_name: typing.Optional[builtins.str] = None,
        source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationTemplate.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationTemplate``.

        :param application_name: The name of the Elastic Beanstalk application to associate with this configuration template.
        :param description: An optional description for this configuration.
        :param environment_id: The ID of an environment whose settings you want to use to create the configuration template. You must specify ``EnvironmentId`` if you don't specify ``PlatformArn`` , ``SolutionStackName`` , or ``SourceConfiguration`` .
        :param option_settings: Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see `Option Values <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .
        :param platform_arn: The Amazon Resource Name (ARN) of the custom platform. For more information, see `Custom Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* . .. epigraph:: If you specify ``PlatformArn`` , then don't specify ``SolutionStackName`` .
        :param solution_stack_name: The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, ``64bit Amazon Linux 2013.09 running Tomcat 7 Java 7`` . A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see `Supported Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* . You must specify ``SolutionStackName`` if you don't specify ``PlatformArn`` , ``EnvironmentId`` , or ``SourceConfiguration`` . Use the ```ListAvailableSolutionStacks`` <https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html>`_ API to obtain a list of available solution stacks.
        :param source_configuration: An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration. Values specified in ``OptionSettings`` override any values obtained from the ``SourceConfiguration`` . You must specify ``SourceConfiguration`` if you don't specify ``PlatformArn`` , ``EnvironmentId`` , or ``SolutionStackName`` . Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
            
            cfn_configuration_template_props = elasticbeanstalk.CfnConfigurationTemplateProps(
                application_name="applicationName",
            
                # the properties below are optional
                description="description",
                environment_id="environmentId",
                option_settings=[elasticbeanstalk.CfnConfigurationTemplate.ConfigurationOptionSettingProperty(
                    namespace="namespace",
                    option_name="optionName",
            
                    # the properties below are optional
                    resource_name="resourceName",
                    value="value"
                )],
                platform_arn="platformArn",
                solution_stack_name="solutionStackName",
                source_configuration=elasticbeanstalk.CfnConfigurationTemplate.SourceConfigurationProperty(
                    application_name="applicationName",
                    template_name="templateName"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796fd0fbbd75363f93a84b4414ff29f987c772572666882bfec89de9a1ec0553)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
            check_type(argname="argument option_settings", value=option_settings, expected_type=type_hints["option_settings"])
            check_type(argname="argument platform_arn", value=platform_arn, expected_type=type_hints["platform_arn"])
            check_type(argname="argument solution_stack_name", value=solution_stack_name, expected_type=type_hints["solution_stack_name"])
            check_type(argname="argument source_configuration", value=source_configuration, expected_type=type_hints["source_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
        }
        if description is not None:
            self._values["description"] = description
        if environment_id is not None:
            self._values["environment_id"] = environment_id
        if option_settings is not None:
            self._values["option_settings"] = option_settings
        if platform_arn is not None:
            self._values["platform_arn"] = platform_arn
        if solution_stack_name is not None:
            self._values["solution_stack_name"] = solution_stack_name
        if source_configuration is not None:
            self._values["source_configuration"] = source_configuration

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the Elastic Beanstalk application to associate with this configuration template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for this configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of an environment whose settings you want to use to create the configuration template.

        You must specify ``EnvironmentId`` if you don't specify ``PlatformArn`` , ``SolutionStackName`` , or ``SourceConfiguration`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-environmentid
        '''
        result = self._values.get("environment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def option_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationTemplate.ConfigurationOptionSettingProperty]]]]:
        '''Option values for the Elastic Beanstalk configuration, such as the instance type.

        If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see `Option Values <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-optionsettings
        '''
        result = self._values.get("option_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationTemplate.ConfigurationOptionSettingProperty]]]], result)

    @builtins.property
    def platform_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the custom platform.

        For more information, see `Custom Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .
        .. epigraph::

           If you specify ``PlatformArn`` , then don't specify ``SolutionStackName`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-platformarn
        '''
        result = self._values.get("platform_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def solution_stack_name(self) -> typing.Optional[builtins.str]:
        '''The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses.

        For example, ``64bit Amazon Linux 2013.09 running Tomcat 7 Java 7`` . A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see `Supported Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .

        You must specify ``SolutionStackName`` if you don't specify ``PlatformArn`` , ``EnvironmentId`` , or ``SourceConfiguration`` .

        Use the ```ListAvailableSolutionStacks`` <https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html>`_ API to obtain a list of available solution stacks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-solutionstackname
        '''
        result = self._values.get("solution_stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationTemplate.SourceConfigurationProperty]]:
        '''An Elastic Beanstalk configuration template to base this one on.

        If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.

        Values specified in ``OptionSettings`` override any values obtained from the ``SourceConfiguration`` .

        You must specify ``SourceConfiguration`` if you don't specify ``PlatformArn`` , ``EnvironmentId`` , or ``SolutionStackName`` .

        Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationTemplate.SourceConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnEnvironment",
):
    '''Specify an AWS Elastic Beanstalk environment by using the AWS::ElasticBeanstalk::Environment resource in an AWS CloudFormation template.

    The AWS::ElasticBeanstalk::Environment resource is an AWS Elastic Beanstalk resource type that specifies an Elastic Beanstalk environment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
        
        cfn_environment = elasticbeanstalk.CfnEnvironment(self, "MyCfnEnvironment",
            application_name="applicationName",
        
            # the properties below are optional
            cname_prefix="cnamePrefix",
            description="description",
            environment_name="environmentName",
            operations_role="operationsRole",
            option_settings=[elasticbeanstalk.CfnEnvironment.OptionSettingProperty(
                namespace="namespace",
                option_name="optionName",
        
                # the properties below are optional
                resource_name="resourceName",
                value="value"
            )],
            platform_arn="platformArn",
            solution_stack_name="solutionStackName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            template_name="templateName",
            tier=elasticbeanstalk.CfnEnvironment.TierProperty(
                name="name",
                type="type",
                version="version"
            ),
            version_label="versionLabel"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        cname_prefix: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        operations_role: typing.Optional[builtins.str] = None,
        option_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.OptionSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        platform_arn: typing.Optional[builtins.str] = None,
        solution_stack_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_name: typing.Optional[builtins.str] = None,
        tier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.TierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_name: The name of the application that is associated with this environment.
        :param cname_prefix: If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
        :param description: Your description for this environment.
        :param environment_name: A unique name for the environment. Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It can't start or end with a hyphen. This name must be unique within a region in your account. If you don't specify the ``CNAMEPrefix`` parameter, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application. If you don't specify an environment name, AWS CloudFormation generates a unique physical ID and uses that ID for the environment name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param operations_role: .. epigraph:: The operations role feature of AWS Elastic Beanstalk is in beta release and is subject to change. The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role. If specified, Elastic Beanstalk uses the operations role for permissions to downstream services during this call and during subsequent calls acting on this environment. To specify an operations role, you must have the ``iam:PassRole`` permission for the role.
        :param option_settings: Key-value pairs defining configuration options for this environment, such as the instance type. These options override the values that are defined in the solution stack or the `configuration template <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-beanstalk-configurationtemplate.html>`_ . If you remove any options during a stack update, the removed options retain their current values.
        :param platform_arn: The Amazon Resource Name (ARN) of the custom platform to use with the environment. For more information, see `Custom Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* . .. epigraph:: If you specify ``PlatformArn`` , don't specify ``SolutionStackName`` .
        :param solution_stack_name: The name of an Elastic Beanstalk solution stack (platform version) to use with the environment. If specified, Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack. For a list of current solution stacks, see `Elastic Beanstalk Supported Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html>`_ in the *AWS Elastic Beanstalk Platforms* guide. .. epigraph:: If you specify ``SolutionStackName`` , don't specify ``PlatformArn`` or ``TemplateName`` .
        :param tags: Specifies the tags applied to resources in the environment.
        :param template_name: The name of the Elastic Beanstalk configuration template to use with the environment. .. epigraph:: If you specify ``TemplateName`` , then don't specify ``SolutionStackName`` .
        :param tier: Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
        :param version_label: The name of the application version to deploy. Default: If not specified, Elastic Beanstalk attempts to deploy the sample application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cf0ef6beb55fa53b1a8e411b9c9453f886af4235facc3424c0cc16848847d3a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            application_name=application_name,
            cname_prefix=cname_prefix,
            description=description,
            environment_name=environment_name,
            operations_role=operations_role,
            option_settings=option_settings,
            platform_arn=platform_arn,
            solution_stack_name=solution_stack_name,
            tags=tags,
            template_name=template_name,
            tier=tier,
            version_label=version_label,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f908a9308749ec4a33168b2903edb82ec8ed4841e37ed9ba1dfe6091de9685e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3da19e1ff38a1265567069741f44271966512d401d0eace8a7e37b023d970a7f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointUrl")
    def attr_endpoint_url(self) -> builtins.str:
        '''For load-balanced, autoscaling environments, the URL to the load balancer. For single-instance environments, the IP address of the instance.

        Example load balancer URL:

        Example instance IP address:

        ``192.0.2.0``

        :cloudformationAttribute: EndpointURL
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointUrl"))

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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the application that is associated with this environment.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a45ace37048e9ed59e71bb25b723ec8e19cb618d626dd3e45b82ae0be3c1a1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="cnamePrefix")
    def cname_prefix(self) -> typing.Optional[builtins.str]:
        '''If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnamePrefix"))

    @cname_prefix.setter
    def cname_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4a848622bc7849c93a76b3ce531317d0b65e71ca7f45f3f4c6bb71bf02704af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cnamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Your description for this environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d912447b9dfd21801fb7018e9c876e5889549ddcead426ed6181fafac2800f43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''A unique name for the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentName"))

    @environment_name.setter
    def environment_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8570fa0d0170bf11b81e2e5bb73eea06bcb0906511770ab3190a4aadd321a460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentName", value)

    @builtins.property
    @jsii.member(jsii_name="operationsRole")
    def operations_role(self) -> typing.Optional[builtins.str]:
        '''.. epigraph::

   The operations role feature of AWS Elastic Beanstalk is in beta release and is subject to change.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationsRole"))

    @operations_role.setter
    def operations_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ab2a8e99c451a7186ae155a62df68dd122517978bbff7d1b5fea612e861fbe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationsRole", value)

    @builtins.property
    @jsii.member(jsii_name="optionSettings")
    def option_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.OptionSettingProperty"]]]]:
        '''Key-value pairs defining configuration options for this environment, such as the instance type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.OptionSettingProperty"]]]], jsii.get(self, "optionSettings"))

    @option_settings.setter
    def option_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.OptionSettingProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7600abd455a41ff1c834927848b4c43cc4b499702ee8a19f3bf0da07cd3e84ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionSettings", value)

    @builtins.property
    @jsii.member(jsii_name="platformArn")
    def platform_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the custom platform to use with the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformArn"))

    @platform_arn.setter
    def platform_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e777d1f2e6e595d291870c01857be4a5dc53abaa344194d85981a18cf8523888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformArn", value)

    @builtins.property
    @jsii.member(jsii_name="solutionStackName")
    def solution_stack_name(self) -> typing.Optional[builtins.str]:
        '''The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "solutionStackName"))

    @solution_stack_name.setter
    def solution_stack_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8029b6097c363f3346be36b46ec75d014ac0966650ff35f2642004f338105f14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "solutionStackName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the tags applied to resources in the environment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89946348997537ce6938ca9985772322b3f46254f3b2d8a8534f716f9e584ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Elastic Beanstalk configuration template to use with the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d4829c7f624610b49115f71e4c1ed85bd516768d254abe493a830af6ce25984)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateName", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.TierProperty"]]:
        '''Specifies the tier to use in creating this environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.TierProperty"]], jsii.get(self, "tier"))

    @tier.setter
    def tier(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.TierProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26b98f48829b19de15f9b899e224ed744dacdd8304b8d311e0612315637bb776)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="versionLabel")
    def version_label(self) -> typing.Optional[builtins.str]:
        '''The name of the application version to deploy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionLabel"))

    @version_label.setter
    def version_label(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c344a581fa209e3cb4fa7fcaf9e00fce4f848081c5402400e27d997f5f940676)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionLabel", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnEnvironment.OptionSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "namespace": "namespace",
            "option_name": "optionName",
            "resource_name": "resourceName",
            "value": "value",
        },
    )
    class OptionSettingProperty:
        def __init__(
            self,
            *,
            namespace: builtins.str,
            option_name: builtins.str,
            resource_name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the ``OptionSetting`` property type to specify an option for an AWS Elastic Beanstalk environment when defining an AWS::ElasticBeanstalk::Environment resource in an AWS CloudFormation template.

            The ``OptionSetting`` property type specifies an option for an AWS Elastic Beanstalk environment.

            The ``OptionSettings`` property of the `AWS::ElasticBeanstalk::Environment <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html>`_ resource contains a list of ``OptionSetting`` property types.

            For a list of possible namespaces and option values, see `Option Values <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .

            :param namespace: A unique namespace that identifies the option's associated AWS resource.
            :param option_name: The name of the configuration option.
            :param resource_name: A unique resource name for the option setting. Use it for a time–based scaling configuration option.
            :param value: The current value for the configuration option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                option_setting_property = elasticbeanstalk.CfnEnvironment.OptionSettingProperty(
                    namespace="namespace",
                    option_name="optionName",
                
                    # the properties below are optional
                    resource_name="resourceName",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c70d2deeb69902e04b3f8946afd2b8f293993a66df8b69d9703d3a352743c3af)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument option_name", value=option_name, expected_type=type_hints["option_name"])
                check_type(argname="argument resource_name", value=resource_name, expected_type=type_hints["resource_name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "namespace": namespace,
                "option_name": option_name,
            }
            if resource_name is not None:
                self._values["resource_name"] = resource_name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def namespace(self) -> builtins.str:
            '''A unique namespace that identifies the option's associated AWS resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html#cfn-elasticbeanstalk-environment-optionsetting-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def option_name(self) -> builtins.str:
            '''The name of the configuration option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html#cfn-elasticbeanstalk-environment-optionsetting-optionname
            '''
            result = self._values.get("option_name")
            assert result is not None, "Required property 'option_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_name(self) -> typing.Optional[builtins.str]:
            '''A unique resource name for the option setting.

            Use it for a time–based scaling configuration option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html#cfn-elasticbeanstalk-environment-optionsetting-resourcename
            '''
            result = self._values.get("resource_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The current value for the configuration option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html#cfn-elasticbeanstalk-environment-optionsetting-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OptionSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnEnvironment.TierProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type", "version": "version"},
    )
    class TierProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the ``Tier`` property type to specify the environment tier for an AWS Elastic Beanstalk environment when defining an AWS::ElasticBeanstalk::Environment resource in an AWS CloudFormation template.

            Describes the environment tier for an `AWS::ElasticBeanstalk::Environment <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html>`_ resource. For more information, see `Environment Tiers <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-tiers.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .

            :param name: The name of this environment tier. Valid values: - For *Web server tier* – ``WebServer`` - For *Worker tier* – ``Worker``
            :param type: The type of this environment tier. Valid values: - For *Web server tier* – ``Standard`` - For *Worker tier* – ``SQS/HTTP``
            :param version: The version of this environment tier. When you don't set a value to it, Elastic Beanstalk uses the latest compatible worker tier version. .. epigraph:: This member is deprecated. Any specific version that you set may become out of date. We recommend leaving it unspecified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-tier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
                
                tier_property = elasticbeanstalk.CfnEnvironment.TierProperty(
                    name="name",
                    type="type",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__20ebf44ad0b64564e5b4154c6f5b2e8a52f2ed1b20db6288a5f6c827817256e0)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if type is not None:
                self._values["type"] = type
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of this environment tier.

            Valid values:

            - For *Web server tier* – ``WebServer``
            - For *Worker tier* – ``Worker``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-tier.html#cfn-elasticbeanstalk-environment-tier-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of this environment tier.

            Valid values:

            - For *Web server tier* – ``Standard``
            - For *Worker tier* – ``SQS/HTTP``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-tier.html#cfn-elasticbeanstalk-environment-tier-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of this environment tier.

            When you don't set a value to it, Elastic Beanstalk uses the latest compatible worker tier version.
            .. epigraph::

               This member is deprecated. Any specific version that you set may become out of date. We recommend leaving it unspecified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-tier.html#cfn-elasticbeanstalk-environment-tier-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticbeanstalk.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "cname_prefix": "cnamePrefix",
        "description": "description",
        "environment_name": "environmentName",
        "operations_role": "operationsRole",
        "option_settings": "optionSettings",
        "platform_arn": "platformArn",
        "solution_stack_name": "solutionStackName",
        "tags": "tags",
        "template_name": "templateName",
        "tier": "tier",
        "version_label": "versionLabel",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        cname_prefix: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        operations_role: typing.Optional[builtins.str] = None,
        option_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.OptionSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        platform_arn: typing.Optional[builtins.str] = None,
        solution_stack_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_name: typing.Optional[builtins.str] = None,
        tier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.TierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param application_name: The name of the application that is associated with this environment.
        :param cname_prefix: If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
        :param description: Your description for this environment.
        :param environment_name: A unique name for the environment. Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It can't start or end with a hyphen. This name must be unique within a region in your account. If you don't specify the ``CNAMEPrefix`` parameter, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application. If you don't specify an environment name, AWS CloudFormation generates a unique physical ID and uses that ID for the environment name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param operations_role: .. epigraph:: The operations role feature of AWS Elastic Beanstalk is in beta release and is subject to change. The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role. If specified, Elastic Beanstalk uses the operations role for permissions to downstream services during this call and during subsequent calls acting on this environment. To specify an operations role, you must have the ``iam:PassRole`` permission for the role.
        :param option_settings: Key-value pairs defining configuration options for this environment, such as the instance type. These options override the values that are defined in the solution stack or the `configuration template <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-beanstalk-configurationtemplate.html>`_ . If you remove any options during a stack update, the removed options retain their current values.
        :param platform_arn: The Amazon Resource Name (ARN) of the custom platform to use with the environment. For more information, see `Custom Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* . .. epigraph:: If you specify ``PlatformArn`` , don't specify ``SolutionStackName`` .
        :param solution_stack_name: The name of an Elastic Beanstalk solution stack (platform version) to use with the environment. If specified, Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack. For a list of current solution stacks, see `Elastic Beanstalk Supported Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html>`_ in the *AWS Elastic Beanstalk Platforms* guide. .. epigraph:: If you specify ``SolutionStackName`` , don't specify ``PlatformArn`` or ``TemplateName`` .
        :param tags: Specifies the tags applied to resources in the environment.
        :param template_name: The name of the Elastic Beanstalk configuration template to use with the environment. .. epigraph:: If you specify ``TemplateName`` , then don't specify ``SolutionStackName`` .
        :param tier: Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
        :param version_label: The name of the application version to deploy. Default: If not specified, Elastic Beanstalk attempts to deploy the sample application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticbeanstalk as elasticbeanstalk
            
            cfn_environment_props = elasticbeanstalk.CfnEnvironmentProps(
                application_name="applicationName",
            
                # the properties below are optional
                cname_prefix="cnamePrefix",
                description="description",
                environment_name="environmentName",
                operations_role="operationsRole",
                option_settings=[elasticbeanstalk.CfnEnvironment.OptionSettingProperty(
                    namespace="namespace",
                    option_name="optionName",
            
                    # the properties below are optional
                    resource_name="resourceName",
                    value="value"
                )],
                platform_arn="platformArn",
                solution_stack_name="solutionStackName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                template_name="templateName",
                tier=elasticbeanstalk.CfnEnvironment.TierProperty(
                    name="name",
                    type="type",
                    version="version"
                ),
                version_label="versionLabel"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9bf8840bb336097f9a8ab8a2978d262cc75efab262110246ba9ccd4885b1eb0)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument cname_prefix", value=cname_prefix, expected_type=type_hints["cname_prefix"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
            check_type(argname="argument operations_role", value=operations_role, expected_type=type_hints["operations_role"])
            check_type(argname="argument option_settings", value=option_settings, expected_type=type_hints["option_settings"])
            check_type(argname="argument platform_arn", value=platform_arn, expected_type=type_hints["platform_arn"])
            check_type(argname="argument solution_stack_name", value=solution_stack_name, expected_type=type_hints["solution_stack_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument version_label", value=version_label, expected_type=type_hints["version_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
        }
        if cname_prefix is not None:
            self._values["cname_prefix"] = cname_prefix
        if description is not None:
            self._values["description"] = description
        if environment_name is not None:
            self._values["environment_name"] = environment_name
        if operations_role is not None:
            self._values["operations_role"] = operations_role
        if option_settings is not None:
            self._values["option_settings"] = option_settings
        if platform_arn is not None:
            self._values["platform_arn"] = platform_arn
        if solution_stack_name is not None:
            self._values["solution_stack_name"] = solution_stack_name
        if tags is not None:
            self._values["tags"] = tags
        if template_name is not None:
            self._values["template_name"] = template_name
        if tier is not None:
            self._values["tier"] = tier
        if version_label is not None:
            self._values["version_label"] = version_label

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the application that is associated with this environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cname_prefix(self) -> typing.Optional[builtins.str]:
        '''If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL.

        If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-cnameprefix
        '''
        result = self._values.get("cname_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Your description for this environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''A unique name for the environment.

        Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It can't start or end with a hyphen. This name must be unique within a region in your account.

        If you don't specify the ``CNAMEPrefix`` parameter, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application.

        If you don't specify an environment name, AWS CloudFormation generates a unique physical ID and uses that ID for the environment name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-environmentname
        '''
        result = self._values.get("environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operations_role(self) -> typing.Optional[builtins.str]:
        '''.. epigraph::

   The operations role feature of AWS Elastic Beanstalk is in beta release and is subject to change.

        The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role. If specified, Elastic Beanstalk uses the operations role for permissions to downstream services during this call and during subsequent calls acting on this environment. To specify an operations role, you must have the ``iam:PassRole`` permission for the role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-operationsrole
        '''
        result = self._values.get("operations_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def option_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.OptionSettingProperty]]]]:
        '''Key-value pairs defining configuration options for this environment, such as the instance type.

        These options override the values that are defined in the solution stack or the `configuration template <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-beanstalk-configurationtemplate.html>`_ . If you remove any options during a stack update, the removed options retain their current values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-optionsettings
        '''
        result = self._values.get("option_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.OptionSettingProperty]]]], result)

    @builtins.property
    def platform_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the custom platform to use with the environment.

        For more information, see `Custom Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .
        .. epigraph::

           If you specify ``PlatformArn`` , don't specify ``SolutionStackName`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-platformarn
        '''
        result = self._values.get("platform_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def solution_stack_name(self) -> typing.Optional[builtins.str]:
        '''The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.

        If specified, Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack. For a list of current solution stacks, see `Elastic Beanstalk Supported Platforms <https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html>`_ in the *AWS Elastic Beanstalk Platforms* guide.
        .. epigraph::

           If you specify ``SolutionStackName`` , don't specify ``PlatformArn`` or ``TemplateName`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-solutionstackname
        '''
        result = self._values.get("solution_stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the tags applied to resources in the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def template_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Elastic Beanstalk configuration template to use with the environment.

        .. epigraph::

           If you specify ``TemplateName`` , then don't specify ``SolutionStackName`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-templatename
        '''
        result = self._values.get("template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.TierProperty]]:
        '''Specifies the tier to use in creating this environment.

        The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-tier
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.TierProperty]], result)

    @builtins.property
    def version_label(self) -> typing.Optional[builtins.str]:
        '''The name of the application version to deploy.

        Default: If not specified, Elastic Beanstalk attempts to deploy the sample application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-versionlabel
        '''
        result = self._values.get("version_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnApplicationVersion",
    "CfnApplicationVersionProps",
    "CfnConfigurationTemplate",
    "CfnConfigurationTemplateProps",
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()

def _typecheckingstub__2037a8b39c672f9e224a0d55f87a787c8f06cc34801647c616c1d3544fc61b01(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    resource_lifecycle_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationResourceLifecycleConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67008ad4d98231202ed96bd8356ff5d52d6ab2ac0b949ec39dee9c2e5b28516c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e3218203e8d26f754fc4833f6d89df4a7aed57f2b40ba41097383e596f90ec(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6bf36c756c98eefc03fcfa7fc47b01fa9a2e1bbbcdea2614f2cbbe19f2ac5e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92d2b49bcac99b2f1f38ca944c407acf1d8ac8d05cf0061b761bacef80edaeb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a75fb3cf2d34861537e2d37fd676dbea69752fd913fa7086637904894d1654f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ApplicationResourceLifecycleConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cab1602adff55377880de5336c8a2e9ecfcfe203ea299cbb9dec79dc27168b2c(
    *,
    service_role: typing.Optional[builtins.str] = None,
    version_lifecycle_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationVersionLifecycleConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d77f447c2f85e748e224d6919c6b28bd509c15cb6d45958762ec3dddfd0a31(
    *,
    max_age_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.MaxAgeRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_count_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.MaxCountRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ed97d29f0279d47ee3340de9177215f38b5a970ec931a1b64762af5da76bfd(
    *,
    delete_source_from_s3: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_age_in_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a27816fed8fa85ae75502cf6691d26ee691b6c71d47f8b4fab4ea659dbf0d13d(
    *,
    delete_source_from_s3: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31c1735cd136eec2821ea76e53787fc49838698c06b9830e11f3e4a61ecceab7(
    *,
    application_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    resource_lifecycle_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationResourceLifecycleConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1516c528cdf5646f1fbc2db47de8d7888e64c08ccc28b6b1ea3f1c451b19a4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    source_bundle: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationVersion.SourceBundleProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__904e752e1e1668e8c5324ea8047fd950cbc7d9bd4e2add9803c8f86204e1bc54(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d5a82ad81553feb3520c025f9dc451708bd07df2be9394343ed645575835b5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27168377f8f2dcb4108fbfe1e434ca0369c6eb4b5fde30de3223efb36d74fc6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e851d2ec17de05de650c602ffaa2d9d6d18f2cb17466abca441fe30ac1b50d80(
    value: typing.Union[_IResolvable_da3f097b, CfnApplicationVersion.SourceBundleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2990bd41c8492714f738e92c7d46621588e6d2d20631de262c28b3b7bad07ce2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab0ce5312d0bfddca943d9bb19c1093f2bc6756b952bafc260c4c84b3c3d7b3(
    *,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d59bfde6ef9919e591cebecf28041cd2684a7628953d69fbe6a460205d95f96(
    *,
    application_name: builtins.str,
    source_bundle: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationVersion.SourceBundleProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e16e4991a410c838f73cd94150f707bdc9d297ed64ed0f67e1bf183266f36923(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    environment_id: typing.Optional[builtins.str] = None,
    option_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationTemplate.ConfigurationOptionSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    platform_arn: typing.Optional[builtins.str] = None,
    solution_stack_name: typing.Optional[builtins.str] = None,
    source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationTemplate.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c0e1a86d4ecaebaf21d17747fcb42a178fa22e102cd23a7b784ccca109c059c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92b475285789cb6d89f2fa870fd45e9ca74a42e5089d6f75084cd5428c92930(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7233e1b2fdf96b0719aad84afaf67d4e80b80e2216d53813200ab4083cd3d79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92814ce35605efc126107dacc2f3dd1e0a4a00bd47ea4d45b2b5e1a28fa51e7d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce6105908a7c7d064a4708e87b39cc1ad0c08a1f6c23ef07b254920062b2b51(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d3d231a3a5e4ac5f74ffd51d127adf4d05bd0317b35ba4f5efa5c5b5d9d444(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationTemplate.ConfigurationOptionSettingProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7cf33f9354e06bb7ba16714da3f9d8c5f45b8651992b1d188c273c9567b78b4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda6098fc28e550f397aa00d810b4be6508b89d4f6c126a3f27b03001c3e7698(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7ef0aa6a6895a3055a35a82ea9af1c29b76ca8fa807de3e85b831b17f7da10(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationTemplate.SourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abed0b599f8199ae57be09e0e454fc0b760f0f0c57a3bf88601a9c9b318f29ae(
    *,
    namespace: builtins.str,
    option_name: builtins.str,
    resource_name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3fd0a38fbd1739c9c00badb2a396cea51ea99ab2d5bec33851b4206c1a8bfbf(
    *,
    application_name: builtins.str,
    template_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796fd0fbbd75363f93a84b4414ff29f987c772572666882bfec89de9a1ec0553(
    *,
    application_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    environment_id: typing.Optional[builtins.str] = None,
    option_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationTemplate.ConfigurationOptionSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    platform_arn: typing.Optional[builtins.str] = None,
    solution_stack_name: typing.Optional[builtins.str] = None,
    source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationTemplate.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cf0ef6beb55fa53b1a8e411b9c9453f886af4235facc3424c0cc16848847d3a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    cname_prefix: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    operations_role: typing.Optional[builtins.str] = None,
    option_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.OptionSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    platform_arn: typing.Optional[builtins.str] = None,
    solution_stack_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_name: typing.Optional[builtins.str] = None,
    tier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.TierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    version_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f908a9308749ec4a33168b2903edb82ec8ed4841e37ed9ba1dfe6091de9685e4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da19e1ff38a1265567069741f44271966512d401d0eace8a7e37b023d970a7f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a45ace37048e9ed59e71bb25b723ec8e19cb618d626dd3e45b82ae0be3c1a1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a848622bc7849c93a76b3ce531317d0b65e71ca7f45f3f4c6bb71bf02704af(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d912447b9dfd21801fb7018e9c876e5889549ddcead426ed6181fafac2800f43(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8570fa0d0170bf11b81e2e5bb73eea06bcb0906511770ab3190a4aadd321a460(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ab2a8e99c451a7186ae155a62df68dd122517978bbff7d1b5fea612e861fbe8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7600abd455a41ff1c834927848b4c43cc4b499702ee8a19f3bf0da07cd3e84ee(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.OptionSettingProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e777d1f2e6e595d291870c01857be4a5dc53abaa344194d85981a18cf8523888(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8029b6097c363f3346be36b46ec75d014ac0966650ff35f2642004f338105f14(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89946348997537ce6938ca9985772322b3f46254f3b2d8a8534f716f9e584ac(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d4829c7f624610b49115f71e4c1ed85bd516768d254abe493a830af6ce25984(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b98f48829b19de15f9b899e224ed744dacdd8304b8d311e0612315637bb776(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.TierProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c344a581fa209e3cb4fa7fcaf9e00fce4f848081c5402400e27d997f5f940676(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70d2deeb69902e04b3f8946afd2b8f293993a66df8b69d9703d3a352743c3af(
    *,
    namespace: builtins.str,
    option_name: builtins.str,
    resource_name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20ebf44ad0b64564e5b4154c6f5b2e8a52f2ed1b20db6288a5f6c827817256e0(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9bf8840bb336097f9a8ab8a2978d262cc75efab262110246ba9ccd4885b1eb0(
    *,
    application_name: builtins.str,
    cname_prefix: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    operations_role: typing.Optional[builtins.str] = None,
    option_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.OptionSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    platform_arn: typing.Optional[builtins.str] = None,
    solution_stack_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_name: typing.Optional[builtins.str] = None,
    tier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.TierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    version_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
