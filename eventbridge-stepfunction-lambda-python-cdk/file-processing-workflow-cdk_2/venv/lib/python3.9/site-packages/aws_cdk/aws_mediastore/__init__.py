'''
# AWS Elemental MediaStore Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mediastore as mediastore
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MediaStore construct libraries](https://constructs.dev/search?q=mediastore)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MediaStore resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaStore.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MediaStore](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaStore.html).

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
class CfnContainer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediastore.CfnContainer",
):
    '''The AWS::MediaStore::Container resource specifies a storage container to hold objects.

    A container is similar to a bucket in Amazon S3.

    When you create a container using AWS CloudFormation , the template manages data for five API actions: creating a container, setting access logging, updating the default container policy, adding a cross-origin resource sharing (CORS) policy, and adding an object lifecycle policy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediastore as mediastore
        
        cfn_container = mediastore.CfnContainer(self, "MyCfnContainer",
            container_name="containerName",
        
            # the properties below are optional
            access_logging_enabled=False,
            cors_policy=[mediastore.CfnContainer.CorsRuleProperty(
                allowed_headers=["allowedHeaders"],
                allowed_methods=["allowedMethods"],
                allowed_origins=["allowedOrigins"],
                expose_headers=["exposeHeaders"],
                max_age_seconds=123
            )],
            lifecycle_policy="lifecyclePolicy",
            metric_policy=mediastore.CfnContainer.MetricPolicyProperty(
                container_level_metrics="containerLevelMetrics",
        
                # the properties below are optional
                metric_policy_rules=[mediastore.CfnContainer.MetricPolicyRuleProperty(
                    object_group="objectGroup",
                    object_group_name="objectGroupName"
                )]
            ),
            policy="policy",
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
        container_name: builtins.str,
        access_logging_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cors_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.CorsRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        lifecycle_policy: typing.Optional[builtins.str] = None,
        metric_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.MetricPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        policy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param container_name: The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named ``movies`` in every region, as long as you don’t have an existing container with that name.
        :param access_logging_enabled: The state of access logging on the container. This value is ``false`` by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to ``true`` , indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.
        :param cors_policy: Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser's XMLHttpRequest capability. To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed. To learn more about CORS, see `Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore <https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html>`_ .
        :param lifecycle_policy: Writes an object lifecycle policy to a container. If the container already has an object lifecycle policy, the service replaces the existing policy with the new policy. It takes up to 20 minutes for the change to take effect. For information about how to construct an object lifecycle policy, see `Components of an Object Lifecycle Policy <https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-components.html>`_ .
        :param metric_policy: 
        :param policy: Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the `AWS Identity and Access Management User Guide <https://docs.aws.amazon.com/iam/>`_ . For this release of the REST API, you can create only one policy for a container. If you enter ``PutContainerPolicy`` twice, the second command modifies the existing policy.
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd8b42cebeb5c28f65fdaf7cdf3151c7003f34b222c43c9272971e72f3d1b79c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContainerProps(
            container_name=container_name,
            access_logging_enabled=access_logging_enabled,
            cors_policy=cors_policy,
            lifecycle_policy=lifecycle_policy,
            metric_policy=metric_policy,
            policy=policy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__380b07056d31d913a855d2b963be5ca4c914bbfd1062eaa3de145c2afc5223a4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__28a52ed6094516b25916bea3e0dc8ac921b3e094e1fb4b74d06cdef76224005b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''The DNS endpoint of the container.

        Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

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
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        '''The name for the container.'''
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10e7e81e71aa4b865a53dcff4b11dbf9fde09b2d2b25f839e982ab92110fe012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="accessLoggingEnabled")
    def access_logging_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The state of access logging on the container.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "accessLoggingEnabled"))

    @access_logging_enabled.setter
    def access_logging_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa774c7c5a8092f174195c7b605a1516571a888f5be6c2df2f5a2584d8b581c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLoggingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="corsPolicy")
    def cors_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.CorsRuleProperty"]]]]:
        '''Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.CorsRuleProperty"]]]], jsii.get(self, "corsPolicy"))

    @cors_policy.setter
    def cors_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.CorsRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__467426d7f4bad0107abaee763e8b698f349eb6f7e80bec30278bb48af442d70e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "corsPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicy")
    def lifecycle_policy(self) -> typing.Optional[builtins.str]:
        '''Writes an object lifecycle policy to a container.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecyclePolicy"))

    @lifecycle_policy.setter
    def lifecycle_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__283671ecfc000621a4145f391f01564d103579132b4dba5c58a8d37a6469fb7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecyclePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="metricPolicy")
    def metric_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.MetricPolicyProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.MetricPolicyProperty"]], jsii.get(self, "metricPolicy"))

    @metric_policy.setter
    def metric_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.MetricPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fbe17101e1cbabe4ada35b516bf8c1866a67969c1a431e3e00e64089669ff87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Optional[builtins.str]:
        '''Creates an access policy for the specified container to restrict the users and clients that can access it.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb4bb02f97dcf212717074795ec241aa23847808700630f07392cee599cd3553)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af8f09217c9fcffb59ad0a4b95e405df0ad5d481e0b17745a0feaf4d46e6c880)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediastore.CfnContainer.CorsRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_headers": "allowedHeaders",
            "allowed_methods": "allowedMethods",
            "allowed_origins": "allowedOrigins",
            "expose_headers": "exposeHeaders",
            "max_age_seconds": "maxAgeSeconds",
        },
    )
    class CorsRuleProperty:
        def __init__(
            self,
            *,
            allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
            expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
            max_age_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A rule for a CORS policy.

            You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.

            :param allowed_headers: Specifies which headers are allowed in a preflight ``OPTIONS`` request through the ``Access-Control-Request-Headers`` header. Each header name that is specified in ``Access-Control-Request-Headers`` must have a corresponding entry in the rule. Only the headers that were requested are sent back. This element can contain only one wildcard character (*).
            :param allowed_methods: Identifies an HTTP method that the origin that is specified in the rule is allowed to execute. Each CORS rule must contain at least one ``AllowedMethods`` and one ``AllowedOrigins`` element.
            :param allowed_origins: One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object). Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.
            :param expose_headers: One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object). This element is optional for each rule.
            :param max_age_seconds: The time in seconds that your browser caches the preflight response for the specified resource. A CORS rule can have only one ``MaxAgeSeconds`` element.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediastore as mediastore
                
                cors_rule_property = mediastore.CfnContainer.CorsRuleProperty(
                    allowed_headers=["allowedHeaders"],
                    allowed_methods=["allowedMethods"],
                    allowed_origins=["allowedOrigins"],
                    expose_headers=["exposeHeaders"],
                    max_age_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c96ae41746996533cc51915a7e7299af261c338fe33c4d4d1748fd37490f0787)
                check_type(argname="argument allowed_headers", value=allowed_headers, expected_type=type_hints["allowed_headers"])
                check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
                check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
                check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
                check_type(argname="argument max_age_seconds", value=max_age_seconds, expected_type=type_hints["max_age_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_headers is not None:
                self._values["allowed_headers"] = allowed_headers
            if allowed_methods is not None:
                self._values["allowed_methods"] = allowed_methods
            if allowed_origins is not None:
                self._values["allowed_origins"] = allowed_origins
            if expose_headers is not None:
                self._values["expose_headers"] = expose_headers
            if max_age_seconds is not None:
                self._values["max_age_seconds"] = max_age_seconds

        @builtins.property
        def allowed_headers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies which headers are allowed in a preflight ``OPTIONS`` request through the ``Access-Control-Request-Headers`` header.

            Each header name that is specified in ``Access-Control-Request-Headers`` must have a corresponding entry in the rule. Only the headers that were requested are sent back.

            This element can contain only one wildcard character (*).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedheaders
            '''
            result = self._values.get("allowed_headers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_methods(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.

            Each CORS rule must contain at least one ``AllowedMethods`` and one ``AllowedOrigins`` element.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedmethods
            '''
            result = self._values.get("allowed_methods")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_origins(self) -> typing.Optional[typing.List[builtins.str]]:
            '''One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object).

            Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedorigins
            '''
            result = self._values.get("allowed_origins")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object).

            This element is optional for each rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-exposeheaders
            '''
            result = self._values.get("expose_headers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def max_age_seconds(self) -> typing.Optional[jsii.Number]:
            '''The time in seconds that your browser caches the preflight response for the specified resource.

            A CORS rule can have only one ``MaxAgeSeconds`` element.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-maxageseconds
            '''
            result = self._values.get("max_age_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CorsRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediastore.CfnContainer.MetricPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_level_metrics": "containerLevelMetrics",
            "metric_policy_rules": "metricPolicyRules",
        },
    )
    class MetricPolicyProperty:
        def __init__(
            self,
            *,
            container_level_metrics: builtins.str,
            metric_policy_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.MetricPolicyRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The metric policy that is associated with the container.

            A metric policy allows AWS Elemental MediaStore to send metrics to Amazon CloudWatch. In the policy, you must indicate whether you want MediaStore to send container-level metrics. You can also include rules to define groups of objects that you want MediaStore to send object-level metrics for.

            To view examples of how to construct a metric policy for your use case, see `Example Metric Policies <https://docs.aws.amazon.com/mediastore/latest/ug/policies-metric-examples.html>`_ .

            :param container_level_metrics: A setting to enable or disable metrics at the container level.
            :param metric_policy_rules: A parameter that holds an array of rules that enable metrics at the object level. This parameter is optional, but if you choose to include it, you must also include at least one rule. By default, you can include up to five rules. You can also `request a quota increase <https://docs.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediastore/quotas>`_ to allow up to 300 rules per policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediastore as mediastore
                
                metric_policy_property = mediastore.CfnContainer.MetricPolicyProperty(
                    container_level_metrics="containerLevelMetrics",
                
                    # the properties below are optional
                    metric_policy_rules=[mediastore.CfnContainer.MetricPolicyRuleProperty(
                        object_group="objectGroup",
                        object_group_name="objectGroupName"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d42dc359c0fbb40ceaf4fe27382dfec6a8e02bc42efc869d89ff1688c7cedd56)
                check_type(argname="argument container_level_metrics", value=container_level_metrics, expected_type=type_hints["container_level_metrics"])
                check_type(argname="argument metric_policy_rules", value=metric_policy_rules, expected_type=type_hints["metric_policy_rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_level_metrics": container_level_metrics,
            }
            if metric_policy_rules is not None:
                self._values["metric_policy_rules"] = metric_policy_rules

        @builtins.property
        def container_level_metrics(self) -> builtins.str:
            '''A setting to enable or disable metrics at the container level.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicy.html#cfn-mediastore-container-metricpolicy-containerlevelmetrics
            '''
            result = self._values.get("container_level_metrics")
            assert result is not None, "Required property 'container_level_metrics' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_policy_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.MetricPolicyRuleProperty"]]]]:
            '''A parameter that holds an array of rules that enable metrics at the object level.

            This parameter is optional, but if you choose to include it, you must also include at least one rule. By default, you can include up to five rules. You can also `request a quota increase <https://docs.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediastore/quotas>`_ to allow up to 300 rules per policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicy.html#cfn-mediastore-container-metricpolicy-metricpolicyrules
            '''
            result = self._values.get("metric_policy_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.MetricPolicyRuleProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediastore.CfnContainer.MetricPolicyRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object_group": "objectGroup",
            "object_group_name": "objectGroupName",
        },
    )
    class MetricPolicyRuleProperty:
        def __init__(
            self,
            *,
            object_group: builtins.str,
            object_group_name: builtins.str,
        ) -> None:
            '''A setting that enables metrics at the object level.

            Each rule contains an object group and an object group name. If the policy includes the MetricPolicyRules parameter, you must include at least one rule. Each metric policy can include up to five rules by default. You can also `request a quota increase <https://docs.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediastore/quotas>`_ to allow up to 300 rules per policy.

            :param object_group: A path or file name that defines which objects to include in the group. Wildcards (*) are acceptable.
            :param object_group_name: A name that allows you to refer to the object group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicyrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediastore as mediastore
                
                metric_policy_rule_property = mediastore.CfnContainer.MetricPolicyRuleProperty(
                    object_group="objectGroup",
                    object_group_name="objectGroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63f217ee2499d5b4f967ce2813a4594f4eb7d56cce030a41aaf5c31552f0475b)
                check_type(argname="argument object_group", value=object_group, expected_type=type_hints["object_group"])
                check_type(argname="argument object_group_name", value=object_group_name, expected_type=type_hints["object_group_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object_group": object_group,
                "object_group_name": object_group_name,
            }

        @builtins.property
        def object_group(self) -> builtins.str:
            '''A path or file name that defines which objects to include in the group.

            Wildcards (*) are acceptable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicyrule.html#cfn-mediastore-container-metricpolicyrule-objectgroup
            '''
            result = self._values.get("object_group")
            assert result is not None, "Required property 'object_group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_group_name(self) -> builtins.str:
            '''A name that allows you to refer to the object group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicyrule.html#cfn-mediastore-container-metricpolicyrule-objectgroupname
            '''
            result = self._values.get("object_group_name")
            assert result is not None, "Required property 'object_group_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricPolicyRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediastore.CfnContainerProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "access_logging_enabled": "accessLoggingEnabled",
        "cors_policy": "corsPolicy",
        "lifecycle_policy": "lifecyclePolicy",
        "metric_policy": "metricPolicy",
        "policy": "policy",
        "tags": "tags",
    },
)
class CfnContainerProps:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        access_logging_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cors_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.CorsRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        lifecycle_policy: typing.Optional[builtins.str] = None,
        metric_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.MetricPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        policy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContainer``.

        :param container_name: The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named ``movies`` in every region, as long as you don’t have an existing container with that name.
        :param access_logging_enabled: The state of access logging on the container. This value is ``false`` by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to ``true`` , indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.
        :param cors_policy: Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser's XMLHttpRequest capability. To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed. To learn more about CORS, see `Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore <https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html>`_ .
        :param lifecycle_policy: Writes an object lifecycle policy to a container. If the container already has an object lifecycle policy, the service replaces the existing policy with the new policy. It takes up to 20 minutes for the change to take effect. For information about how to construct an object lifecycle policy, see `Components of an Object Lifecycle Policy <https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-components.html>`_ .
        :param metric_policy: 
        :param policy: Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the `AWS Identity and Access Management User Guide <https://docs.aws.amazon.com/iam/>`_ . For this release of the REST API, you can create only one policy for a container. If you enter ``PutContainerPolicy`` twice, the second command modifies the existing policy.
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediastore as mediastore
            
            cfn_container_props = mediastore.CfnContainerProps(
                container_name="containerName",
            
                # the properties below are optional
                access_logging_enabled=False,
                cors_policy=[mediastore.CfnContainer.CorsRuleProperty(
                    allowed_headers=["allowedHeaders"],
                    allowed_methods=["allowedMethods"],
                    allowed_origins=["allowedOrigins"],
                    expose_headers=["exposeHeaders"],
                    max_age_seconds=123
                )],
                lifecycle_policy="lifecyclePolicy",
                metric_policy=mediastore.CfnContainer.MetricPolicyProperty(
                    container_level_metrics="containerLevelMetrics",
            
                    # the properties below are optional
                    metric_policy_rules=[mediastore.CfnContainer.MetricPolicyRuleProperty(
                        object_group="objectGroup",
                        object_group_name="objectGroupName"
                    )]
                ),
                policy="policy",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40306af5b770854abc9e3f568c4ca2d80a5a5886a6f698d75584f726b0f11f7e)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument access_logging_enabled", value=access_logging_enabled, expected_type=type_hints["access_logging_enabled"])
            check_type(argname="argument cors_policy", value=cors_policy, expected_type=type_hints["cors_policy"])
            check_type(argname="argument lifecycle_policy", value=lifecycle_policy, expected_type=type_hints["lifecycle_policy"])
            check_type(argname="argument metric_policy", value=metric_policy, expected_type=type_hints["metric_policy"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_name": container_name,
        }
        if access_logging_enabled is not None:
            self._values["access_logging_enabled"] = access_logging_enabled
        if cors_policy is not None:
            self._values["cors_policy"] = cors_policy
        if lifecycle_policy is not None:
            self._values["lifecycle_policy"] = lifecycle_policy
        if metric_policy is not None:
            self._values["metric_policy"] = metric_policy
        if policy is not None:
            self._values["policy"] = policy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def container_name(self) -> builtins.str:
        '''The name for the container.

        The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named ``movies`` in every region, as long as you don’t have an existing container with that name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-containername
        '''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_logging_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The state of access logging on the container.

        This value is ``false`` by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to ``true`` , indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-accessloggingenabled
        '''
        result = self._values.get("access_logging_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def cors_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainer.CorsRuleProperty]]]]:
        '''Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests.

        For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser's XMLHttpRequest capability.

        To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.

        To learn more about CORS, see `Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore <https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-corspolicy
        '''
        result = self._values.get("cors_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainer.CorsRuleProperty]]]], result)

    @builtins.property
    def lifecycle_policy(self) -> typing.Optional[builtins.str]:
        '''Writes an object lifecycle policy to a container.

        If the container already has an object lifecycle policy, the service replaces the existing policy with the new policy. It takes up to 20 minutes for the change to take effect.

        For information about how to construct an object lifecycle policy, see `Components of an Object Lifecycle Policy <https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-components.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-lifecyclepolicy
        '''
        result = self._values.get("lifecycle_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainer.MetricPolicyProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-metricpolicy
        '''
        result = self._values.get("metric_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainer.MetricPolicyProperty]], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''Creates an access policy for the specified container to restrict the users and clients that can access it.

        For information about the data that is included in an access policy, see the `AWS Identity and Access Management User Guide <https://docs.aws.amazon.com/iam/>`_ .

        For this release of the REST API, you can create only one policy for a container. If you enter ``PutContainerPolicy`` twice, the second command modifies the existing policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-policy
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContainerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnContainer",
    "CfnContainerProps",
]

publication.publish()

def _typecheckingstub__cd8b42cebeb5c28f65fdaf7cdf3151c7003f34b222c43c9272971e72f3d1b79c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    container_name: builtins.str,
    access_logging_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cors_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.CorsRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lifecycle_policy: typing.Optional[builtins.str] = None,
    metric_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.MetricPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    policy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__380b07056d31d913a855d2b963be5ca4c914bbfd1062eaa3de145c2afc5223a4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28a52ed6094516b25916bea3e0dc8ac921b3e094e1fb4b74d06cdef76224005b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e7e81e71aa4b865a53dcff4b11dbf9fde09b2d2b25f839e982ab92110fe012(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa774c7c5a8092f174195c7b605a1516571a888f5be6c2df2f5a2584d8b581c1(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__467426d7f4bad0107abaee763e8b698f349eb6f7e80bec30278bb48af442d70e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainer.CorsRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__283671ecfc000621a4145f391f01564d103579132b4dba5c58a8d37a6469fb7c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fbe17101e1cbabe4ada35b516bf8c1866a67969c1a431e3e00e64089669ff87(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainer.MetricPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb4bb02f97dcf212717074795ec241aa23847808700630f07392cee599cd3553(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8f09217c9fcffb59ad0a4b95e405df0ad5d481e0b17745a0feaf4d46e6c880(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96ae41746996533cc51915a7e7299af261c338fe33c4d4d1748fd37490f0787(
    *,
    allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
    expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_age_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d42dc359c0fbb40ceaf4fe27382dfec6a8e02bc42efc869d89ff1688c7cedd56(
    *,
    container_level_metrics: builtins.str,
    metric_policy_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.MetricPolicyRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f217ee2499d5b4f967ce2813a4594f4eb7d56cce030a41aaf5c31552f0475b(
    *,
    object_group: builtins.str,
    object_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40306af5b770854abc9e3f568c4ca2d80a5a5886a6f698d75584f726b0f11f7e(
    *,
    container_name: builtins.str,
    access_logging_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cors_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.CorsRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lifecycle_policy: typing.Optional[builtins.str] = None,
    metric_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.MetricPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    policy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
