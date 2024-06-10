'''
# AWS Region-Specific Information Directory

## Usage

Some information used in CDK Applications differs from one AWS region to
another, such as service principals used in IAM policies, S3 static website
endpoints, ...

### The `RegionInfo` class

The library offers a simple interface to obtain region specific information in
the form of the `RegionInfo` class. This is the preferred way to interact with
the regional information database:

```python
# Get the information for "eu-west-1":
region = region_info.RegionInfo.get("eu-west-1")

# Access attributes:
region.s3_static_website_endpoint # s3-website-eu-west-1.amazonaws.com
region.service_principal("logs.amazonaws.com")
```

The `RegionInfo` layer is built on top of the Low-Level API, which is described
below and can be used to register additional data, including user-defined facts
that are not available through the `RegionInfo` interface.

### Low-Level API

This library offers a primitive database of such information so that CDK
constructs can easily access regional information. The `FactName` class provides
a list of known fact names, which can then be used with the `RegionInfo` to
retrieve a particular value:

```python
code_deploy_principal = region_info.Fact.find("us-east-1", region_info.FactName.service_principal("codedeploy.amazonaws.com"))
# => codedeploy.us-east-1.amazonaws.com

static_website = region_info.Fact.find("ap-northeast-1", region_info.FactName.S3_STATIC_WEBSITE_ENDPOINT)
```

## Supplying new or missing information

As new regions are released, it might happen that a particular fact you need is
missing from the library. In such cases, the `Fact.register` method can be used
to inject FactName into the database:

```python
@jsii.implements(region_info.IFact)
class MyFact:

region_info.Fact.register(MyFact())
```

## Overriding incorrect information

In the event information provided by the library is incorrect, it can be
overridden using the same `Fact.register` method demonstrated above, simply
adding an extra boolean argument:

```python
@jsii.implements(region_info.IFact)
class MyFact:

region_info.Fact.register(MyFact(), True)
```

If you happen to have stumbled upon incorrect data built into this library, it
is always a good idea to report your findings in a [GitHub issue](https://github.com/aws/aws-cdk/issues), so we can fix
it for everyone else!

---


This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
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


class Default(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.region_info.Default"):
    '''Provides default values for certain regional information points.'''

    @jsii.member(jsii_name="servicePrincipal")
    @builtins.classmethod
    def service_principal(
        cls,
        service_fqn: builtins.str,
        region: builtins.str,
        url_suffix: builtins.str,
    ) -> builtins.str:
        '''Computes a "standard" AWS Service principal for a given service, region and suffix.

        This is useful for example when
        you need to compute a service principal name, but you do not have a synthesize-time region literal available (so
        all you have is ``{ "Ref": "AWS::Region" }``). This way you get the same defaulting behavior that is normally used
        for built-in data.

        :param service_fqn: the name of the service (s3, s3.amazonaws.com, ...).
        :param region: the region in which the service principal is needed.
        :param url_suffix: deprecated and ignored.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ed580ab93fc60dd8fa1b87d26acd7858752bf9581325d9fdde38b224ee5da52)
            check_type(argname="argument service_fqn", value=service_fqn, expected_type=type_hints["service_fqn"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument url_suffix", value=url_suffix, expected_type=type_hints["url_suffix"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "servicePrincipal", [service_fqn, region, url_suffix]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_ENDPOINT_SERVICE_NAME_PREFIX")
    def VPC_ENDPOINT_SERVICE_NAME_PREFIX(cls) -> builtins.str:
        '''The default value for a VPC Endpoint Service name prefix, useful if you do not have a synthesize-time region literal available (all you have is ``{ "Ref": "AWS::Region" }``).'''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_ENDPOINT_SERVICE_NAME_PREFIX"))


class Fact(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.region_info.Fact"):
    '''A database of regional information.

    :exampleMetadata: infused

    Example::

        @jsii.implements(region_info.IFact)
        class MyFact:
        
        region_info.Fact.register(MyFact())
    '''

    @jsii.member(jsii_name="definedFacts")
    @builtins.classmethod
    def defined_facts(cls) -> typing.List[typing.List[builtins.str]]:
        '''Return all pairs of (region, factName) that are defined.'''
        return typing.cast(typing.List[typing.List[builtins.str]], jsii.sinvoke(cls, "definedFacts", []))

    @jsii.member(jsii_name="find")
    @builtins.classmethod
    def find(
        cls,
        region: builtins.str,
        name: builtins.str,
    ) -> typing.Optional[builtins.str]:
        '''Retrieves a fact from this Fact database.

        :param region: the name of the region (e.g: ``us-east-1``).
        :param name: the name of the fact being looked up (see the ``FactName`` class for details).

        :return: the fact value if it is known, and ``undefined`` otherwise.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__727f44dd49d6697508adfcf85a0821cd604a47806af06bd93d5e794210343c72)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(typing.Optional[builtins.str], jsii.sinvoke(cls, "find", [region, name]))

    @jsii.member(jsii_name="register")
    @builtins.classmethod
    def register(
        cls,
        fact: "IFact",
        allow_replacing: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Registers a new fact in this Fact database.

        :param fact: the new fact to be registered.
        :param allow_replacing: whether new facts can replace existing facts or not.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6f49f7af106ebb8acd267cdbe85794fb8b4878040de2bb98cd0ea6f31e0221)
            check_type(argname="argument fact", value=fact, expected_type=type_hints["fact"])
            check_type(argname="argument allow_replacing", value=allow_replacing, expected_type=type_hints["allow_replacing"])
        return typing.cast(None, jsii.sinvoke(cls, "register", [fact, allow_replacing]))

    @jsii.member(jsii_name="requireFact")
    @builtins.classmethod
    def require_fact(cls, region: builtins.str, name: builtins.str) -> builtins.str:
        '''Retrieve a fact from the Fact database.

        (retrieval will fail if the specified region or
        fact name does not exist.)

        :param region: the name of the region (e.g: ``us-east-1``).
        :param name: the name of the fact being looked up (see the ``FactName`` class for details).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78d53652aae6f4162a51705eb1c8ed6aecce155647a56c7011f21a51f1889066)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "requireFact", [region, name]))

    @jsii.member(jsii_name="unregister")
    @builtins.classmethod
    def unregister(
        cls,
        region: builtins.str,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Removes a fact from the database.

        :param region: the region for which the fact is to be removed.
        :param name: the name of the fact to remove.
        :param value: the value that should be removed (removal will fail if the value is specified, but does not match the current stored value).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1830bd6c4b0fa66fd9e45dca1b8ce4bd4848b5ab28831c793956707d5857952e)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.sinvoke(cls, "unregister", [region, name, value]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="names")
    def names(cls) -> typing.List[builtins.str]:
        '''Returns the list of names of registered facts.

        All facts will be present in at least one region.
        '''
        return typing.cast(typing.List[builtins.str], jsii.sget(cls, "names"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="regions")
    def regions(cls) -> typing.List[builtins.str]:
        '''
        :return:

        the list of names of AWS Regions for which there is at least one registered fact. This
        includes Regions defined in AWS_REGIONS plus custom defined regions.
        '''
        return typing.cast(typing.List[builtins.str], jsii.sget(cls, "regions"))


class FactName(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.region_info.FactName"):
    '''All standardized fact names.

    :exampleMetadata: infused

    Example::

        @jsii.implements(region_info.IFact)
        class MyFact:
        
        region_info.Fact.register(MyFact())
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="adotLambdaLayer")
    @builtins.classmethod
    def adot_lambda_layer(
        cls,
        type: builtins.str,
        version: builtins.str,
        architecture: builtins.str,
    ) -> builtins.str:
        '''The ARN of Amazon Distro for OpenTelemetry (ADOT) Lambda layer for a given lambda type, version and architecture.

        :param type: the type of the ADOT lambda layer.
        :param version: the layer version.
        :param architecture: the Lambda Function architecture (e.g. 'x86_64' or 'arm64').
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a52ea8b2faec71331553359ca14bac1a12036119dce3c5e6e3022ebea5734934)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "adotLambdaLayer", [type, version, architecture]))

    @jsii.member(jsii_name="appConfigLambdaLayerVersion")
    @builtins.classmethod
    def app_config_lambda_layer_version(
        cls,
        version: builtins.str,
        arch: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''The ARN of AppConfig Lambda Layer for a given version (e.g. 2.0.181).

        :param version: The layer version.
        :param arch: The architecture (optional), defaults to x86_64.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f54bb938ce691bf38d46828de52e9e8afaacfd2ae36e0187c737382ecb3f0fd8)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument arch", value=arch, expected_type=type_hints["arch"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "appConfigLambdaLayerVersion", [version, arch]))

    @jsii.member(jsii_name="cloudwatchLambdaInsightsVersion")
    @builtins.classmethod
    def cloudwatch_lambda_insights_version(
        cls,
        version: builtins.str,
        arch: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''The ARN of CloudWatch Lambda Insights for a version (e.g. 1.0.98.0).

        :param version: -
        :param arch: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43e6018c25205623b05e3dea383d535db52915f6e910faa0b43bd987f1d9f466)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument arch", value=arch, expected_type=type_hints["arch"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "cloudwatchLambdaInsightsVersion", [version, arch]))

    @jsii.member(jsii_name="paramsAndSecretsLambdaLayer")
    @builtins.classmethod
    def params_and_secrets_lambda_layer(
        cls,
        version: builtins.str,
        architecture: builtins.str,
    ) -> builtins.str:
        '''The ARN of Parameters and Secrets Lambda layer for a given lambda architecture.

        :param version: the layer version.
        :param architecture: the Lambda Function architecture (e.g. 'x86_64' or 'arm64').
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e85af17141cb06d78caf690b404140a60da484702dae653fb870c38266e1cb)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "paramsAndSecretsLambdaLayer", [version, architecture]))

    @jsii.member(jsii_name="servicePrincipal")
    @builtins.classmethod
    def service_principal(cls, service: builtins.str) -> builtins.str:
        '''The name of the regional service principal for a given service.

        :param service: the service name, either simple (e.g: ``s3``, ``codedeploy``) or qualified (e.g: ``s3.amazonaws.com``). The ``.amazonaws.com`` and ``.amazonaws.com.cn`` domains are stripped from service names, so they are canonicalized in that respect.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b14fde076501b6bbe3459fe473f8a85eda6046b48c735804859dd2c381a5566f)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "servicePrincipal", [service]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPMESH_ECR_ACCOUNT")
    def APPMESH_ECR_ACCOUNT(cls) -> builtins.str:
        '''The ID of the AWS account that owns the public ECR repository that contains the AWS App Mesh Envoy Proxy images in a given region.'''
        return typing.cast(builtins.str, jsii.sget(cls, "APPMESH_ECR_ACCOUNT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CDK_METADATA_RESOURCE_AVAILABLE")
    def CDK_METADATA_RESOURCE_AVAILABLE(cls) -> builtins.str:
        '''Whether the AWS::CDK::Metadata CloudFormation Resource is available in-region or not.

        The value is a boolean
        modelled as ``YES`` or ``NO``.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CDK_METADATA_RESOURCE_AVAILABLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DLC_REPOSITORY_ACCOUNT")
    def DLC_REPOSITORY_ACCOUNT(cls) -> builtins.str:
        '''The ID of the AWS account that owns the public ECR repository that contains the AWS Deep Learning Containers images in a given region.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DLC_REPOSITORY_ACCOUNT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DOMAIN_SUFFIX")
    def DOMAIN_SUFFIX(cls) -> builtins.str:
        '''The domain suffix for a region (e.g: 'amazonaws.com`).'''
        return typing.cast(builtins.str, jsii.sget(cls, "DOMAIN_SUFFIX"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_ENV_ENDPOINT_HOSTED_ZONE_ID")
    def EBS_ENV_ENDPOINT_HOSTED_ZONE_ID(cls) -> builtins.str:
        '''The hosted zone ID used by Route 53 to alias a EBS environment endpoint in this region (e.g: Z2O1EMRO9K5GLX).'''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_ENV_ENDPOINT_HOSTED_ZONE_ID"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELBV2_ACCOUNT")
    def ELBV2_ACCOUNT(cls) -> builtins.str:
        '''The account for ELBv2 in this region.'''
        return typing.cast(builtins.str, jsii.sget(cls, "ELBV2_ACCOUNT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FIREHOSE_CIDR_BLOCK")
    def FIREHOSE_CIDR_BLOCK(cls) -> builtins.str:
        '''The CIDR block used by Kinesis Data Firehose servers.'''
        return typing.cast(builtins.str, jsii.sget(cls, "FIREHOSE_CIDR_BLOCK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IS_OPT_IN_REGION")
    def IS_OPT_IN_REGION(cls) -> builtins.str:
        '''Whether the given region is an opt-in region or not.

        The value is a boolean
        modelled as ``YES`` or ``NO``.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IS_OPT_IN_REGION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PARTITION")
    def PARTITION(cls) -> builtins.str:
        '''The name of the partition for a region (e.g: 'aws', 'aws-cn', ...).'''
        return typing.cast(builtins.str, jsii.sget(cls, "PARTITION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_STATIC_WEBSITE_ENDPOINT")
    def S3_STATIC_WEBSITE_ENDPOINT(cls) -> builtins.str:
        '''The endpoint used for hosting S3 static websites.'''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_STATIC_WEBSITE_ENDPOINT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_STATIC_WEBSITE_ZONE_53_HOSTED_ZONE_ID")
    def S3_STATIC_WEBSITE_ZONE_53_HOSTED_ZONE_ID(cls) -> builtins.str:
        '''The endpoint used for aliasing S3 static websites in Route 53.'''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_STATIC_WEBSITE_ZONE_53_HOSTED_ZONE_ID"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAML_SIGN_ON_URL")
    def SAML_SIGN_ON_URL(cls) -> builtins.str:
        '''The SAML Sign On URL for partition used by IAM SAML Principal.'''
        return typing.cast(builtins.str, jsii.sget(cls, "SAML_SIGN_ON_URL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_ENDPOINT_SERVICE_NAME_PREFIX")
    def VPC_ENDPOINT_SERVICE_NAME_PREFIX(cls) -> builtins.str:
        '''The prefix for VPC Endpoint Service names, cn.com.amazonaws.vpce for China regions, com.amazonaws.vpce otherwise.'''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_ENDPOINT_SERVICE_NAME_PREFIX"))


@jsii.interface(jsii_type="aws-cdk-lib.region_info.IFact")
class IFact(typing_extensions.Protocol):
    '''A fact that can be registered about a particular region.'''

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this fact.

        Standardized values are provided by the ``Facts`` class.
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        '''The region for which this fact applies.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of this fact.'''
        ...


class _IFactProxy:
    '''A fact that can be registered about a particular region.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.region_info.IFact"

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this fact.

        Standardized values are provided by the ``Facts`` class.
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        '''The region for which this fact applies.'''
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of this fact.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "value"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFact).__jsii_proxy_class__ = lambda : _IFactProxy


class RegionInfo(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.region_info.RegionInfo",
):
    '''Information pertaining to an AWS region.

    :exampleMetadata: infused

    Example::

        # Get the information for "eu-west-1":
        region = region_info.RegionInfo.get("eu-west-1")
        
        # Access attributes:
        region.s3_static_website_endpoint # s3-website-eu-west-1.amazonaws.com
        region.service_principal("logs.amazonaws.com")
    '''

    @jsii.member(jsii_name="get")
    @builtins.classmethod
    def get(cls, name: builtins.str) -> "RegionInfo":
        '''Obtain region info for a given region name.

        :param name: the name of the region (e.g: us-east-1).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3466db588ebe6149482deac8597b3a55aa41380440489271daf6e7c39d285b1)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast("RegionInfo", jsii.sinvoke(cls, "get", [name]))

    @jsii.member(jsii_name="limitedRegionMap")
    @builtins.classmethod
    def limited_region_map(
        cls,
        fact_name: builtins.str,
        partitions: typing.Sequence[builtins.str],
    ) -> typing.Mapping[builtins.str, builtins.str]:
        '''Retrieves a collection of all fact values for all regions, limited to some partitions.

        :param fact_name: the name of the fact to retrieve values for. For a list of common fact names, see the FactName class
        :param partitions: list of partitions to retrieve facts for. Defaults to ``['aws', 'aws-cn']``.

        :return:

        a mapping with AWS region codes as the keys,
        and the fact in the given region as the value for that key
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21ecc25c666c6163e89638fdcf818b27ace4d211f59a3393eb7436c93a122a14)
            check_type(argname="argument fact_name", value=fact_name, expected_type=type_hints["fact_name"])
            check_type(argname="argument partitions", value=partitions, expected_type=type_hints["partitions"])
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.sinvoke(cls, "limitedRegionMap", [fact_name, partitions]))

    @jsii.member(jsii_name="regionMap")
    @builtins.classmethod
    def region_map(
        cls,
        fact_name: builtins.str,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        '''Retrieves a collection of all fact values for all regions that fact is defined in.

        :param fact_name: the name of the fact to retrieve values for. For a list of common fact names, see the FactName class

        :return:

        a mapping with AWS region codes as the keys,
        and the fact in the given region as the value for that key
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c43c4d000f66cab277e05819376eedd79a9c37e4474478c78d7a58e8e8df1f1a)
            check_type(argname="argument fact_name", value=fact_name, expected_type=type_hints["fact_name"])
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.sinvoke(cls, "regionMap", [fact_name]))

    @jsii.member(jsii_name="adotLambdaLayerArn")
    def adot_lambda_layer_arn(
        self,
        type: builtins.str,
        version: builtins.str,
        architecture: builtins.str,
    ) -> typing.Optional[builtins.str]:
        '''The ARN of the ADOT Lambda layer, for the given layer type, version and architecture.

        :param type: the type of the ADOT lambda layer.
        :param version: the layer version.
        :param architecture: the Lambda Function architecture (e.g. 'x86_64' or 'arm64').
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c84a70b89ec85497195301e831f21749101789f92f60eb738af9aee6e5feeb)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "adotLambdaLayerArn", [type, version, architecture]))

    @jsii.member(jsii_name="appConfigLambdaArn")
    def app_config_lambda_arn(
        self,
        layer_version: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
    ) -> typing.Optional[builtins.str]:
        '''The ARN of the AppConfig Lambda Layer, for the given version.

        :param layer_version: The layer version (e.g. 2.0.181).
        :param architecture: The Lambda Function architecture (e.g. 'x86_64' or 'arm64'), defaults to x86_64.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb80d3b2e5be7b9dec6c393e9eb0977edf5031aec2a80cc490438c4c300932b)
            check_type(argname="argument layer_version", value=layer_version, expected_type=type_hints["layer_version"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "appConfigLambdaArn", [layer_version, architecture]))

    @jsii.member(jsii_name="cloudwatchLambdaInsightsArn")
    def cloudwatch_lambda_insights_arn(
        self,
        insights_version: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
    ) -> typing.Optional[builtins.str]:
        '''The ARN of the CloudWatch Lambda Insights extension, for the given version.

        :param insights_version: the version (e.g. 1.0.98.0).
        :param architecture: the Lambda Function architecture (e.g. 'x86_64' or 'arm64').
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cce016d7f88a7bd5b91741d5a6afd2c644bef86b54f2533ad6dc772d87d599f5)
            check_type(argname="argument insights_version", value=insights_version, expected_type=type_hints["insights_version"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "cloudwatchLambdaInsightsArn", [insights_version, architecture]))

    @jsii.member(jsii_name="paramsAndSecretsLambdaLayerArn")
    def params_and_secrets_lambda_layer_arn(
        self,
        version: builtins.str,
        architecture: builtins.str,
    ) -> typing.Optional[builtins.str]:
        '''The ARN of the Parameters and Secrets Lambda layer for the given lambda architecture.

        :param version: the layer version.
        :param architecture: the Lambda Function architecture (e.g. 'x86_64' or 'arm64').
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b956146d487195c3acb1779c0146a94aee85876962f555b1e971c8ce90ec930)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "paramsAndSecretsLambdaLayerArn", [version, architecture]))

    @jsii.member(jsii_name="servicePrincipal")
    def service_principal(self, service: builtins.str) -> typing.Optional[builtins.str]:
        '''The name of the service principal for a given service in this region.

        :param service: the service name (e.g: s3.amazonaws.com).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7fa00c6eee8344d2d7dec9a9b3e5aabd291377b56af4261818a521770e400cf)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "servicePrincipal", [service]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="regions")
    def regions(cls) -> typing.List["RegionInfo"]:
        '''
        :return:

        the list of names of AWS regions for which there is at least one registered fact. This
        may not be an exaustive list of all available AWS regions.
        '''
        return typing.cast(typing.List["RegionInfo"], jsii.sget(cls, "regions"))

    @builtins.property
    @jsii.member(jsii_name="cdkMetadataResourceAvailable")
    def cdk_metadata_resource_available(self) -> builtins.bool:
        '''Whether the ``AWS::CDK::Metadata`` CloudFormation Resource is available in this region or not.'''
        return typing.cast(builtins.bool, jsii.get(self, "cdkMetadataResourceAvailable"))

    @builtins.property
    @jsii.member(jsii_name="isOptInRegion")
    def is_opt_in_region(self) -> builtins.bool:
        '''Whether the given region is an opt-in region.'''
        return typing.cast(builtins.bool, jsii.get(self, "isOptInRegion"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="appMeshRepositoryAccount")
    def app_mesh_repository_account(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS account that owns the public ECR repository that contains the AWS App Mesh Envoy Proxy images in a given region.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appMeshRepositoryAccount"))

    @builtins.property
    @jsii.member(jsii_name="dlcRepositoryAccount")
    def dlc_repository_account(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS account that owns the public ECR repository containing the AWS Deep Learning Containers images in this region.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dlcRepositoryAccount"))

    @builtins.property
    @jsii.member(jsii_name="domainSuffix")
    def domain_suffix(self) -> typing.Optional[builtins.str]:
        '''The domain name suffix (e.g: amazonaws.com) for this region.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainSuffix"))

    @builtins.property
    @jsii.member(jsii_name="ebsEnvEndpointHostedZoneId")
    def ebs_env_endpoint_hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''The hosted zone ID used by Route 53 to alias a EBS environment endpoint in this region (e.g: Z2O1EMRO9K5GLX).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ebsEnvEndpointHostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="elbv2Account")
    def elbv2_account(self) -> typing.Optional[builtins.str]:
        '''The account ID for ELBv2 in this region.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elbv2Account"))

    @builtins.property
    @jsii.member(jsii_name="firehoseCidrBlock")
    def firehose_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The CIDR block used by Kinesis Data Firehose servers.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firehoseCidrBlock"))

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> typing.Optional[builtins.str]:
        '''The name of the ARN partition for this region (e.g: aws).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partition"))

    @builtins.property
    @jsii.member(jsii_name="s3StaticWebsiteEndpoint")
    def s3_static_website_endpoint(self) -> typing.Optional[builtins.str]:
        '''The endpoint used by S3 static website hosting in this region (e.g: s3-static-website-us-east-1.amazonaws.com).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3StaticWebsiteEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="s3StaticWebsiteHostedZoneId")
    def s3_static_website_hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''The hosted zone ID used by Route 53 to alias a S3 static website in this region (e.g: Z2O1EMRO9K5GLX).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3StaticWebsiteHostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="samlSignOnUrl")
    def saml_sign_on_url(self) -> typing.Optional[builtins.str]:
        '''SAML Sign On URL used by IAM SAML Principals.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "samlSignOnUrl"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointServiceNamePrefix")
    def vpc_endpoint_service_name_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for VPC Endpoint Service names, cn.com.amazonaws.vpce for China regions, com.amazonaws.vpce otherwise.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcEndpointServiceNamePrefix"))


__all__ = [
    "Default",
    "Fact",
    "FactName",
    "IFact",
    "RegionInfo",
]

publication.publish()

def _typecheckingstub__6ed580ab93fc60dd8fa1b87d26acd7858752bf9581325d9fdde38b224ee5da52(
    service_fqn: builtins.str,
    region: builtins.str,
    url_suffix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__727f44dd49d6697508adfcf85a0821cd604a47806af06bd93d5e794210343c72(
    region: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6f49f7af106ebb8acd267cdbe85794fb8b4878040de2bb98cd0ea6f31e0221(
    fact: IFact,
    allow_replacing: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d53652aae6f4162a51705eb1c8ed6aecce155647a56c7011f21a51f1889066(
    region: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1830bd6c4b0fa66fd9e45dca1b8ce4bd4848b5ab28831c793956707d5857952e(
    region: builtins.str,
    name: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a52ea8b2faec71331553359ca14bac1a12036119dce3c5e6e3022ebea5734934(
    type: builtins.str,
    version: builtins.str,
    architecture: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f54bb938ce691bf38d46828de52e9e8afaacfd2ae36e0187c737382ecb3f0fd8(
    version: builtins.str,
    arch: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43e6018c25205623b05e3dea383d535db52915f6e910faa0b43bd987f1d9f466(
    version: builtins.str,
    arch: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e85af17141cb06d78caf690b404140a60da484702dae653fb870c38266e1cb(
    version: builtins.str,
    architecture: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b14fde076501b6bbe3459fe473f8a85eda6046b48c735804859dd2c381a5566f(
    service: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3466db588ebe6149482deac8597b3a55aa41380440489271daf6e7c39d285b1(
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ecc25c666c6163e89638fdcf818b27ace4d211f59a3393eb7436c93a122a14(
    fact_name: builtins.str,
    partitions: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c43c4d000f66cab277e05819376eedd79a9c37e4474478c78d7a58e8e8df1f1a(
    fact_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c84a70b89ec85497195301e831f21749101789f92f60eb738af9aee6e5feeb(
    type: builtins.str,
    version: builtins.str,
    architecture: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb80d3b2e5be7b9dec6c393e9eb0977edf5031aec2a80cc490438c4c300932b(
    layer_version: builtins.str,
    architecture: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce016d7f88a7bd5b91741d5a6afd2c644bef86b54f2533ad6dc772d87d599f5(
    insights_version: builtins.str,
    architecture: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b956146d487195c3acb1779c0146a94aee85876962f555b1e971c8ce90ec930(
    version: builtins.str,
    architecture: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7fa00c6eee8344d2d7dec9a9b3e5aabd291377b56af4261818a521770e400cf(
    service: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
