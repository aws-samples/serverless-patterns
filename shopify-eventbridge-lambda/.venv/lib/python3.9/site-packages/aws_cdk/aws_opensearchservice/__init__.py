'''
# Amazon OpenSearch Service Construct Library

See [Migrating to OpenSearch](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-elasticsearch-readme.html#migrating-to-opensearch) for migration instructions from `aws-cdk-lib/aws-elasticsearch` to this module, `aws-cdk-lib/aws-opensearchservice`.

## Quick start

Create a development cluster by simply specifying the version:

```python
dev_domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0
)
```

To perform version upgrades without replacing the entire domain, specify the `enableVersionUpgrade` property.

```python
dev_domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    enable_version_upgrade=True
)
```

Create a cluster with GP3 volumes:

```python
gp3_domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_2_5,
    ebs=EbsOptions(
        volume_size=30,
        volume_type=ec2.EbsDeviceVolumeType.GP3,
        throughput=125,
        iops=3000
    )
)
```

Create a production grade cluster by also specifying things like capacity and az distribution

```python
prod_domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    capacity=CapacityConfig(
        master_nodes=5,
        data_nodes=20
    ),
    ebs=EbsOptions(
        volume_size=20
    ),
    zone_awareness=ZoneAwarenessConfig(
        availability_zone_count=3
    ),
    logging=LoggingOptions(
        slow_search_log_enabled=True,
        app_log_enabled=True,
        slow_index_log_enabled=True
    )
)
```

This creates an Amazon OpenSearch Service cluster and automatically sets up log groups for
logging the domain logs and slow search logs.

## A note about SLR

Some cluster configurations (e.g VPC access) require the existence of the [`AWSServiceRoleForAmazonElasticsearchService`](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html) Service-Linked Role.

When performing such operations via the AWS Console, this SLR is created automatically when needed. However, this is not the behavior when using CloudFormation. If an SLR is needed, but doesn't exist, you will encounter a failure message similar to:

```console
Before you can proceed, you must enable a service-linked role to give Amazon OpenSearch Service...
```

To resolve this, you need to [create](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) the SLR. We recommend using the AWS CLI:

```console
aws iam create-service-linked-role --aws-service-name es.amazonaws.com
```

You can also create it using the CDK, **but note that only the first application deploying this will succeed**:

```python
slr = iam.CfnServiceLinkedRole(self, "Service Linked Role",
    aws_service_name="es.amazonaws.com"
)
```

## Importing existing domains

### Using a known domain endpoint

To import an existing domain into your CDK application, use the `Domain.fromDomainEndpoint` factory method.
This method accepts a domain endpoint of an already existing domain:

```python
domain_endpoint = "https://my-domain-jcjotrt6f7otem4sqcwbch3c4u.us-east-1.es.amazonaws.com"
domain = Domain.from_domain_endpoint(self, "ImportedDomain", domain_endpoint)
```

### Using the output of another CloudFormation stack

To import an existing domain with the help of an exported value from another CloudFormation stack,
use the `Domain.fromDomainAttributes` factory method. This will accept tokens.

```python
domain_arn = Fn.import_value("another-cf-stack-export-domain-arn")
domain_endpoint = Fn.import_value("another-cf-stack-export-domain-endpoint")
domain = Domain.from_domain_attributes(self, "ImportedDomain",
    domain_arn=domain_arn,
    domain_endpoint=domain_endpoint
)
```

## Permissions

### IAM

Helper methods also exist for managing access to the domain.

```python
# fn: lambda.Function
# domain: Domain


# Grant write access to the app-search index
domain.grant_index_write("app-search", fn)

# Grant read access to the 'app-search/_search' path
domain.grant_path_read("app-search/_search", fn)
```

## Encryption

The domain can also be created with encryption enabled:

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    ebs=EbsOptions(
        volume_size=100,
        volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
    ),
    node_to_node_encryption=True,
    encryption_at_rest=EncryptionAtRestOptions(
        enabled=True
    )
)
```

This sets up the domain with node to node encryption and encryption at
rest. You can also choose to supply your own KMS key to use for encryption at
rest.

## VPC Support

Domains can be placed inside a VPC, providing a secure communication between Amazon OpenSearch Service and other services within the VPC without the need for an internet gateway, NAT device, or VPN connection.

> Visit [VPC Support for Amazon OpenSearch Service Domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html) for more details.

```python
vpc = ec2.Vpc(self, "Vpc")
domain_props = DomainProps(
    version=EngineVersion.OPENSEARCH_1_0,
    removal_policy=RemovalPolicy.DESTROY,
    vpc=vpc,
    # must be enabled since our VPC contains multiple private subnets.
    zone_awareness=ZoneAwarenessConfig(
        enabled=True
    ),
    capacity=CapacityConfig(
        # must be an even number since the default az count is 2.
        data_nodes=2
    )
)
Domain(self, "Domain", domain_props)
```

In addition, you can use the `vpcSubnets` property to control which specific subnets will be used, and the `securityGroups` property to control
which security groups will be attached to the domain. By default, CDK will select all *private* subnets in the VPC, and create one dedicated security group.

## Metrics

Helper methods exist to access common domain metrics for example:

```python
# domain: Domain

free_storage_space = domain.metric_free_storage_space()
master_sys_memory_utilization = domain.metric("MasterSysMemoryUtilization")
```

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Fine grained access control

The domain can also be created with a master user configured. The password can
be supplied or dynamically created if not supplied.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    enforce_https=True,
    node_to_node_encryption=True,
    encryption_at_rest=EncryptionAtRestOptions(
        enabled=True
    ),
    fine_grained_access_control=AdvancedSecurityOptions(
        master_user_name="master-user"
    )
)

master_user_password = domain.master_user_password
```

## SAML authentication

You can enable SAML authentication to use your existing identity provider
to offer single sign-on (SSO) for dashboards on Amazon OpenSearch Service domains
running OpenSearch or Elasticsearch 6.7 or later.
To use SAML authentication, fine-grained access control must be enabled.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    enforce_https=True,
    node_to_node_encryption=True,
    encryption_at_rest=EncryptionAtRestOptions(
        enabled=True
    ),
    fine_grained_access_control=AdvancedSecurityOptions(
        master_user_name="master-user",
        saml_authentication_enabled=True,
        saml_authentication_options=SAMLOptionsProperty(
            idp_entity_id="entity-id",
            idp_metadata_content="metadata-content-with-quotes-escaped"
        )
    )
)
```

## Using unsigned basic auth

For convenience, the domain can be configured to allow unsigned HTTP requests
that use basic auth. Unless the domain is configured to be part of a VPC this
means anyone can access the domain using the configured master username and
password.

To enable unsigned basic auth access the domain is configured with an access
policy that allows anonymous requests, HTTPS required, node to node encryption,
encryption at rest and fine grained access control.

If the above settings are not set they will be configured as part of enabling
unsigned basic auth. If they are set with conflicting values, an error will be
thrown.

If no master user is configured a default master user is created with the
username `admin`.

If no password is configured a default master user password is created and
stored in the AWS Secrets Manager as secret. The secret has the prefix
`<domain id>MasterUser`.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    use_unsigned_basic_auth=True
)

master_user_password = domain.master_user_password
```

## Custom access policies

If the domain requires custom access control it can be configured either as a
constructor property, or later by means of a helper method.

For simple permissions the `accessPolicies` constructor may be sufficient:

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    access_policies=[
        iam.PolicyStatement(
            actions=["es:*ESHttpPost", "es:ESHttpPut*"],
            effect=iam.Effect.ALLOW,
            principals=[iam.AccountPrincipal("123456789012")],
            resources=["*"]
        )
    ]
)
```

For more complex use-cases, for example, to set the domain up to receive data from a
[cross-account Kinesis Firehose](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-firehose-cross-account-streaming/) the `addAccessPolicies` helper method
allows for policies that include the explicit domain ARN.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0
)
domain.add_access_policies(
    iam.PolicyStatement(
        actions=["es:ESHttpPost", "es:ESHttpPut"],
        effect=iam.Effect.ALLOW,
        principals=[iam.AccountPrincipal("123456789012")],
        resources=[domain.domain_arn, f"{domain.domainArn}/*"]
    ),
    iam.PolicyStatement(
        actions=["es:ESHttpGet"],
        effect=iam.Effect.ALLOW,
        principals=[iam.AccountPrincipal("123456789012")],
        resources=[f"{domain.domainArn}/_all/_settings", f"{domain.domainArn}/_cluster/stats", f"{domain.domainArn}/index-name*/_mapping/type-name", f"{domain.domainArn}/roletest*/_mapping/roletest", f"{domain.domainArn}/_nodes", f"{domain.domainArn}/_nodes/stats", f"{domain.domainArn}/_nodes/*/stats", f"{domain.domainArn}/_stats", f"{domain.domainArn}/index-name*/_stats", f"{domain.domainArn}/roletest*/_stat"
        ]
    ))
```

## Audit logs

Audit logs can be enabled for a domain, but only when fine grained access control is enabled.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    enforce_https=True,
    node_to_node_encryption=True,
    encryption_at_rest=EncryptionAtRestOptions(
        enabled=True
    ),
    fine_grained_access_control=AdvancedSecurityOptions(
        master_user_name="master-user"
    ),
    logging=LoggingOptions(
        audit_log_enabled=True,
        slow_search_log_enabled=True,
        app_log_enabled=True,
        slow_index_log_enabled=True
    )
)
```

## Suppress creating CloudWatch Logs resource policy

When logging is enabled for the domain, the CloudWatch Logs resource policy is created by default.
This resource policy is necessary for logging, but since only a maximum of 10 resource policies can be created per region,
the maximum number of resource policies may be a problem when enabling logging for several domains.
By setting the `suppressLogsResourcePolicy` option to true, you can suppress the creation of a CloudWatch Logs resource policy.

If you set the `suppressLogsResourcePolicy` option to true, you must create a resource policy before deployment.
Also, to avoid reaching this limit, consider reusing a broader policy that includes multiple log groups.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    enforce_https=True,
    node_to_node_encryption=True,
    encryption_at_rest=EncryptionAtRestOptions(
        enabled=True
    ),
    fine_grained_access_control=AdvancedSecurityOptions(
        master_user_name="master-user"
    ),
    logging=LoggingOptions(
        audit_log_enabled=True,
        slow_search_log_enabled=True,
        app_log_enabled=True,
        slow_index_log_enabled=True
    ),
    suppress_logs_resource_policy=True
)
```

> Visit [Monitoring OpenSearch logs with Amazon CloudWatch Logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html) for more details.

## UltraWarm

UltraWarm nodes can be enabled to provide a cost-effective way to store large amounts of read-only data.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    capacity=CapacityConfig(
        master_nodes=2,
        warm_nodes=2,
        warm_instance_type="ultrawarm1.medium.search"
    )
)
```

## Cold storage

Cold storage can be enabled on the domain. You must enable UltraWarm storage to enable cold storage.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    capacity=CapacityConfig(
        master_nodes=2,
        warm_nodes=2,
        warm_instance_type="ultrawarm1.medium.search"
    ),
    cold_storage_enabled=True
)
```

## Custom endpoint

Custom endpoints can be configured to reach the domain under a custom domain name.

```python
Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    custom_endpoint=CustomEndpointOptions(
        domain_name="search.example.com"
    )
)
```

It is also possible to specify a custom certificate instead of the auto-generated one.

Additionally, an automatic CNAME-Record is created if a hosted zone is provided for the custom endpoint

## Advanced options

[Advanced options](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options) can used to configure additional options.

```python
Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    advanced_options={
        "rest.action.multi.allow_explicit_index": "false",
        "indices.fielddata.cache.size": "25",
        "indices.query.bool.max_clause_count": "2048"
    }
)
```

## Amazon Cognito authentication for OpenSearch Dashboards

The domain can be configured to use Amazon Cognito authentication for OpenSearch Dashboards.

> Visit [Configuring Amazon Cognito authentication for OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html) for more details.

```python
# cognito_configuration_role: iam.Role


domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_0,
    cognito_dashboards_auth=CognitoOptions(
        role=cognito_configuration_role,
        identity_pool_id="example-identity-pool-id",
        user_pool_id="example-user-pool-id"
    )
)
```

## Enable support for Multi-AZ with Standby deployment

The domain can be configured to use [multi-AZ with standby](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html#managedomains-za-standby).

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_3,
    ebs=EbsOptions(
        volume_size=10,
        volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD_GP3
    ),
    zone_awareness=ZoneAwarenessConfig(
        enabled=True,
        availability_zone_count=3
    ),
    capacity=CapacityConfig(
        multi_az_with_standby_enabled=True,
        master_nodes=3,
        data_nodes=3
    )
)
```

## Define off-peak windows

The domain can be configured to use a daily 10-hour window considered as off-peak hours.

Off-peak windows were introduced on February 16, 2023.
All domains created before this date have the off-peak window disabled by default.
You must manually enable and configure the off-peak window for these domains.
All domains created after this date will have the off-peak window enabled by default.
You can't disable the off-peak window for a domain after it's enabled.

> Visit [Defining off-peak windows for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html) for more details.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_3,
    off_peak_window_enabled=True,  # can be omitted if offPeakWindowStart is set
    off_peak_window_start=WindowStartTime(
        hours=20,
        minutes=0
    )
)
```

## Configuring service software updates

The domain can be configured to use service software updates.

> Visit [Service software updates in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html) for more details.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_3,
    enable_auto_software_update=True
)
```

## IP address type

You can specify either dual stack or IPv4 as your IP address type.

```python
domain = Domain(self, "Domain",
    version=EngineVersion.OPENSEARCH_1_3,
    ip_address_type=IpAddressType.DUAL_STACK
)
```
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
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    SecretValue as _SecretValue_3dd0ddae,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_certificatemanager import ICertificate as _ICertificate_c194c70b
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_ec2 import (
    Connections as _Connections_0f31fce8,
    EbsDeviceVolumeType as _EbsDeviceVolumeType_6792555b,
    IConnectable as _IConnectable_10015a05,
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IRole as _IRole_235f5d8e,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_logs import ILogGroup as _ILogGroup_3c4fa718
from ..aws_route53 import IHostedZone as _IHostedZone_9a6907ad


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.AdvancedSecurityOptions",
    jsii_struct_bases=[],
    name_mapping={
        "master_user_arn": "masterUserArn",
        "master_user_name": "masterUserName",
        "master_user_password": "masterUserPassword",
        "saml_authentication_enabled": "samlAuthenticationEnabled",
        "saml_authentication_options": "samlAuthenticationOptions",
    },
)
class AdvancedSecurityOptions:
    def __init__(
        self,
        *,
        master_user_arn: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[_SecretValue_3dd0ddae] = None,
        saml_authentication_enabled: typing.Optional[builtins.bool] = None,
        saml_authentication_options: typing.Optional[typing.Union["SAMLOptionsProperty", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Specifies options for fine-grained access control.

        :param master_user_arn: ARN for the master user. Only specify this or masterUserName, but not both. Default: - fine-grained access control is disabled
        :param master_user_name: Username for the master user. Only specify this or masterUserArn, but not both. Default: - fine-grained access control is disabled
        :param master_user_password: Password for the master user. You can use ``SecretValue.unsafePlainText`` to specify a password in plain text or use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in Secrets Manager. Default: - A Secrets Manager generated password
        :param saml_authentication_enabled: True to enable SAML authentication for a domain. Default: - SAML authentication is disabled. Enabled if ``samlAuthenticationOptions`` is set.
        :param saml_authentication_options: Container for information about the SAML configuration for OpenSearch Dashboards. If set, ``samlAuthenticationEnabled`` will be enabled. Default: - no SAML authentication options

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_0,
                enforce_https=True,
                node_to_node_encryption=True,
                encryption_at_rest=EncryptionAtRestOptions(
                    enabled=True
                ),
                fine_grained_access_control=AdvancedSecurityOptions(
                    master_user_name="master-user",
                    saml_authentication_enabled=True,
                    saml_authentication_options=SAMLOptionsProperty(
                        idp_entity_id="entity-id",
                        idp_metadata_content="metadata-content-with-quotes-escaped"
                    )
                )
            )
        '''
        if isinstance(saml_authentication_options, dict):
            saml_authentication_options = SAMLOptionsProperty(**saml_authentication_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1e95392d4761126042f2d6d6160889a80c269d2f13c21476fe92febdb7f04e3)
            check_type(argname="argument master_user_arn", value=master_user_arn, expected_type=type_hints["master_user_arn"])
            check_type(argname="argument master_user_name", value=master_user_name, expected_type=type_hints["master_user_name"])
            check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
            check_type(argname="argument saml_authentication_enabled", value=saml_authentication_enabled, expected_type=type_hints["saml_authentication_enabled"])
            check_type(argname="argument saml_authentication_options", value=saml_authentication_options, expected_type=type_hints["saml_authentication_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if master_user_arn is not None:
            self._values["master_user_arn"] = master_user_arn
        if master_user_name is not None:
            self._values["master_user_name"] = master_user_name
        if master_user_password is not None:
            self._values["master_user_password"] = master_user_password
        if saml_authentication_enabled is not None:
            self._values["saml_authentication_enabled"] = saml_authentication_enabled
        if saml_authentication_options is not None:
            self._values["saml_authentication_options"] = saml_authentication_options

    @builtins.property
    def master_user_arn(self) -> typing.Optional[builtins.str]:
        '''ARN for the master user.

        Only specify this or masterUserName, but not both.

        :default: - fine-grained access control is disabled
        '''
        result = self._values.get("master_user_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_name(self) -> typing.Optional[builtins.str]:
        '''Username for the master user.

        Only specify this or masterUserArn, but not both.

        :default: - fine-grained access control is disabled
        '''
        result = self._values.get("master_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[_SecretValue_3dd0ddae]:
        '''Password for the master user.

        You can use ``SecretValue.unsafePlainText`` to specify a password in plain text or
        use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in
        Secrets Manager.

        :default: - A Secrets Manager generated password
        '''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[_SecretValue_3dd0ddae], result)

    @builtins.property
    def saml_authentication_enabled(self) -> typing.Optional[builtins.bool]:
        '''True to enable SAML authentication for a domain.

        :default: - SAML authentication is disabled. Enabled if ``samlAuthenticationOptions`` is set.

        :see: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/saml.html
        '''
        result = self._values.get("saml_authentication_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def saml_authentication_options(self) -> typing.Optional["SAMLOptionsProperty"]:
        '''Container for information about the SAML configuration for OpenSearch Dashboards.

        If set, ``samlAuthenticationEnabled`` will be enabled.

        :default: - no SAML authentication options
        '''
        result = self._values.get("saml_authentication_options")
        return typing.cast(typing.Optional["SAMLOptionsProperty"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdvancedSecurityOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.CapacityConfig",
    jsii_struct_bases=[],
    name_mapping={
        "data_node_instance_type": "dataNodeInstanceType",
        "data_nodes": "dataNodes",
        "master_node_instance_type": "masterNodeInstanceType",
        "master_nodes": "masterNodes",
        "multi_az_with_standby_enabled": "multiAzWithStandbyEnabled",
        "warm_instance_type": "warmInstanceType",
        "warm_nodes": "warmNodes",
    },
)
class CapacityConfig:
    def __init__(
        self,
        *,
        data_node_instance_type: typing.Optional[builtins.str] = None,
        data_nodes: typing.Optional[jsii.Number] = None,
        master_node_instance_type: typing.Optional[builtins.str] = None,
        master_nodes: typing.Optional[jsii.Number] = None,
        multi_az_with_standby_enabled: typing.Optional[builtins.bool] = None,
        warm_instance_type: typing.Optional[builtins.str] = None,
        warm_nodes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Configures the capacity of the cluster such as the instance type and the number of instances.

        :param data_node_instance_type: The instance type for your data nodes, such as ``m3.medium.search``. For valid values, see `Supported Instance Types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ in the Amazon OpenSearch Service Developer Guide. Default: - r5.large.search
        :param data_nodes: The number of data nodes (instances) to use in the Amazon OpenSearch Service domain. Default: - 1
        :param master_node_instance_type: The hardware configuration of the computer that hosts the dedicated master node, such as ``m3.medium.search``. For valid values, see `Supported Instance Types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ in the Amazon OpenSearch Service Developer Guide. Default: - r5.large.search
        :param master_nodes: The number of instances to use for the master node. Default: - no dedicated master nodes
        :param multi_az_with_standby_enabled: Indicates whether Multi-AZ with Standby deployment option is enabled. For more information, see `Multi-AZ with Standby <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html#managedomains-za-standby>`_ Default: - multi-az with standby if the feature flag ``ENABLE_OPENSEARCH_MULTIAZ_WITH_STANDBY`` is true, no multi-az with standby otherwise
        :param warm_instance_type: The instance type for your UltraWarm node, such as ``ultrawarm1.medium.search``. For valid values, see `UltraWarm Storage Limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#limits-ultrawarm>`_ in the Amazon OpenSearch Service Developer Guide. Default: - ultrawarm1.medium.search
        :param warm_nodes: The number of UltraWarm nodes (instances) to use in the Amazon OpenSearch Service domain. Default: - no UltraWarm nodes

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_0,
                capacity=CapacityConfig(
                    master_nodes=2,
                    warm_nodes=2,
                    warm_instance_type="ultrawarm1.medium.search"
                ),
                cold_storage_enabled=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48cdec23c4ecd3d168ddd937e9295b924cdea583f9951d98aacce1c1c90cad71)
            check_type(argname="argument data_node_instance_type", value=data_node_instance_type, expected_type=type_hints["data_node_instance_type"])
            check_type(argname="argument data_nodes", value=data_nodes, expected_type=type_hints["data_nodes"])
            check_type(argname="argument master_node_instance_type", value=master_node_instance_type, expected_type=type_hints["master_node_instance_type"])
            check_type(argname="argument master_nodes", value=master_nodes, expected_type=type_hints["master_nodes"])
            check_type(argname="argument multi_az_with_standby_enabled", value=multi_az_with_standby_enabled, expected_type=type_hints["multi_az_with_standby_enabled"])
            check_type(argname="argument warm_instance_type", value=warm_instance_type, expected_type=type_hints["warm_instance_type"])
            check_type(argname="argument warm_nodes", value=warm_nodes, expected_type=type_hints["warm_nodes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_node_instance_type is not None:
            self._values["data_node_instance_type"] = data_node_instance_type
        if data_nodes is not None:
            self._values["data_nodes"] = data_nodes
        if master_node_instance_type is not None:
            self._values["master_node_instance_type"] = master_node_instance_type
        if master_nodes is not None:
            self._values["master_nodes"] = master_nodes
        if multi_az_with_standby_enabled is not None:
            self._values["multi_az_with_standby_enabled"] = multi_az_with_standby_enabled
        if warm_instance_type is not None:
            self._values["warm_instance_type"] = warm_instance_type
        if warm_nodes is not None:
            self._values["warm_nodes"] = warm_nodes

    @builtins.property
    def data_node_instance_type(self) -> typing.Optional[builtins.str]:
        '''The instance type for your data nodes, such as ``m3.medium.search``. For valid values, see `Supported Instance Types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ in the Amazon OpenSearch Service Developer Guide.

        :default: - r5.large.search
        '''
        result = self._values.get("data_node_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of data nodes (instances) to use in the Amazon OpenSearch Service domain.

        :default: - 1
        '''
        result = self._values.get("data_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def master_node_instance_type(self) -> typing.Optional[builtins.str]:
        '''The hardware configuration of the computer that hosts the dedicated master node, such as ``m3.medium.search``. For valid values, see `Supported Instance Types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ in the Amazon OpenSearch Service Developer Guide.

        :default: - r5.large.search
        '''
        result = self._values.get("master_node_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of instances to use for the master node.

        :default: - no dedicated master nodes
        '''
        result = self._values.get("master_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def multi_az_with_standby_enabled(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether Multi-AZ with Standby deployment option is enabled.

        For more information, see `Multi-AZ with
        Standby <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html#managedomains-za-standby>`_

        :default:

        - multi-az with standby if the feature flag ``ENABLE_OPENSEARCH_MULTIAZ_WITH_STANDBY``
        is true, no multi-az with standby otherwise
        '''
        result = self._values.get("multi_az_with_standby_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def warm_instance_type(self) -> typing.Optional[builtins.str]:
        '''The instance type for your UltraWarm node, such as ``ultrawarm1.medium.search``. For valid values, see `UltraWarm Storage Limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#limits-ultrawarm>`_ in the Amazon OpenSearch Service Developer Guide.

        :default: - ultrawarm1.medium.search
        '''
        result = self._values.get("warm_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warm_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of UltraWarm nodes (instances) to use in the Amazon OpenSearch Service domain.

        :default: - no UltraWarm nodes
        '''
        result = self._values.get("warm_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapacityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain",
):
    '''The AWS::OpenSearchService::Domain resource creates an Amazon OpenSearch Service domain.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html
    :cloudformationResource: AWS::OpenSearchService::Domain
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearchservice as opensearchservice
        
        # access_policies: Any
        
        cfn_domain = opensearchservice.CfnDomain(self, "MyCfnDomain",
            access_policies=access_policies,
            advanced_options={
                "advanced_options_key": "advancedOptions"
            },
            advanced_security_options=opensearchservice.CfnDomain.AdvancedSecurityOptionsInputProperty(
                anonymous_auth_disable_date="anonymousAuthDisableDate",
                anonymous_auth_enabled=False,
                enabled=False,
                internal_user_database_enabled=False,
                master_user_options=opensearchservice.CfnDomain.MasterUserOptionsProperty(
                    master_user_arn="masterUserArn",
                    master_user_name="masterUserName",
                    master_user_password="masterUserPassword"
                ),
                saml_options=opensearchservice.CfnDomain.SAMLOptionsProperty(
                    enabled=False,
                    idp=opensearchservice.CfnDomain.IdpProperty(
                        entity_id="entityId",
                        metadata_content="metadataContent"
                    ),
                    master_backend_role="masterBackendRole",
                    master_user_name="masterUserName",
                    roles_key="rolesKey",
                    session_timeout_minutes=123,
                    subject_key="subjectKey"
                )
            ),
            cluster_config=opensearchservice.CfnDomain.ClusterConfigProperty(
                cold_storage_options=opensearchservice.CfnDomain.ColdStorageOptionsProperty(
                    enabled=False
                ),
                dedicated_master_count=123,
                dedicated_master_enabled=False,
                dedicated_master_type="dedicatedMasterType",
                instance_count=123,
                instance_type="instanceType",
                multi_az_with_standby_enabled=False,
                warm_count=123,
                warm_enabled=False,
                warm_type="warmType",
                zone_awareness_config=opensearchservice.CfnDomain.ZoneAwarenessConfigProperty(
                    availability_zone_count=123
                ),
                zone_awareness_enabled=False
            ),
            cognito_options=opensearchservice.CfnDomain.CognitoOptionsProperty(
                enabled=False,
                identity_pool_id="identityPoolId",
                role_arn="roleArn",
                user_pool_id="userPoolId"
            ),
            domain_arn="domainArn",
            domain_endpoint_options=opensearchservice.CfnDomain.DomainEndpointOptionsProperty(
                custom_endpoint="customEndpoint",
                custom_endpoint_certificate_arn="customEndpointCertificateArn",
                custom_endpoint_enabled=False,
                enforce_https=False,
                tls_security_policy="tlsSecurityPolicy"
            ),
            domain_name="domainName",
            ebs_options=opensearchservice.CfnDomain.EBSOptionsProperty(
                ebs_enabled=False,
                iops=123,
                throughput=123,
                volume_size=123,
                volume_type="volumeType"
            ),
            encryption_at_rest_options=opensearchservice.CfnDomain.EncryptionAtRestOptionsProperty(
                enabled=False,
                kms_key_id="kmsKeyId"
            ),
            engine_version="engineVersion",
            ip_address_type="ipAddressType",
            log_publishing_options={
                "log_publishing_options_key": opensearchservice.CfnDomain.LogPublishingOptionProperty(
                    cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn",
                    enabled=False
                )
            },
            node_to_node_encryption_options=opensearchservice.CfnDomain.NodeToNodeEncryptionOptionsProperty(
                enabled=False
            ),
            off_peak_window_options=opensearchservice.CfnDomain.OffPeakWindowOptionsProperty(
                enabled=False,
                off_peak_window=opensearchservice.CfnDomain.OffPeakWindowProperty(
                    window_start_time=opensearchservice.CfnDomain.WindowStartTimeProperty(
                        hours=123,
                        minutes=123
                    )
                )
            ),
            snapshot_options=opensearchservice.CfnDomain.SnapshotOptionsProperty(
                automated_snapshot_start_hour=123
            ),
            software_update_options=opensearchservice.CfnDomain.SoftwareUpdateOptionsProperty(
                auto_software_update_enabled=False
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_options=opensearchservice.CfnDomain.VPCOptionsProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_policies: typing.Any = None,
        advanced_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        advanced_security_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.AdvancedSecurityOptionsInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cluster_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ClusterConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cognito_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.CognitoOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        domain_arn: typing.Optional[builtins.str] = None,
        domain_endpoint_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.DomainEndpointOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        ebs_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.EBSOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        encryption_at_rest_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.EncryptionAtRestOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.LogPublishingOptionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        node_to_node_encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.NodeToNodeEncryptionOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        off_peak_window_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.OffPeakWindowOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        snapshot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.SnapshotOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        software_update_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.SoftwareUpdateOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.VPCOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_policies: An AWS Identity and Access Management ( IAM ) policy document that specifies who can access the OpenSearch Service domain and their permissions. For more information, see `Configuring access policies <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-creating>`_ in the *Amazon OpenSearch Service Developer Guide* .
        :param advanced_options: Additional options to specify for the OpenSearch Service domain. For more information, see `AdvancedOptions <https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateDomain.html#API_CreateDomain_RequestBody>`_ in the OpenSearch Service API reference.
        :param advanced_security_options: Specifies options for fine-grained access control and SAML authentication. If you specify advanced security options, you must also enable node-to-node encryption ( `NodeToNodeEncryptionOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html>`_ ) and encryption at rest ( `EncryptionAtRestOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html>`_ ). You must also enable ``EnforceHTTPS`` within `DomainEndpointOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html>`_ , which requires HTTPS for all traffic to the domain.
        :param cluster_config: Container for the cluster configuration of a domain.
        :param cognito_options: Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.
        :param domain_arn: 
        :param domain_endpoint_options: Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.
        :param domain_name: A name for the OpenSearch Service domain. The name must have a minimum length of 3 and a maximum length of 28. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the domain name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . Required when creating a new domain. .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param ebs_options: The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain. For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .
        :param encryption_at_rest_options: Whether the domain should encrypt data at rest, and if so, the AWS KMS key to use. See `Encryption of data at rest for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html>`_ . If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.
        :param engine_version: The version of OpenSearch to use. The value must be in the format ``OpenSearch_X.Y`` or ``Elasticsearch_X.Y`` . If not specified, the latest version of OpenSearch is used. For information about the versions that OpenSearch Service supports, see `Supported versions of OpenSearch and Elasticsearch <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#choosing-version>`_ in the *Amazon OpenSearch Service Developer Guide* . If you set the `EnableVersionUpgrade <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-upgradeopensearchdomain>`_ update policy to ``true`` , you can update ``EngineVersion`` without interruption. When ``EnableVersionUpgrade`` is set to ``false`` , or is not specified, updating ``EngineVersion`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param ip_address_type: Choose either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.
        :param log_publishing_options: An object with one or more of the following keys: ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , ``AUDIT_LOGS`` , depending on the types of logs you want to publish. Each key needs a valid ``LogPublishingOption`` value. For the full syntax, see the `examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain--examples>`_ .
        :param node_to_node_encryption_options: Specifies whether node-to-node encryption is enabled. See `Node-to-node encryption for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html>`_ .
        :param off_peak_window_options: Options for a domain's off-peak window, during which OpenSearch Service can perform mandatory configuration changes on the domain.
        :param snapshot_options: *DEPRECATED* . The automated snapshot configuration for the OpenSearch Service domain indexes.
        :param software_update_options: Service software update options for the domain.
        :param tags: An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Service domain.
        :param vpc_options: The virtual private cloud (VPC) configuration for the OpenSearch Service domain. For more information, see `Launching your Amazon OpenSearch Service domains within a VPC <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html>`_ in the *Amazon OpenSearch Service Developer Guide* . If you remove this entity altogether, along with its associated properties, it causes a replacement. You might encounter this scenario if you're updating your security configuration from a VPC to a public endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fcd2545392b3f48f314c640881e38e167b5936f1165d2eb1ce21766d3db5770)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(
            access_policies=access_policies,
            advanced_options=advanced_options,
            advanced_security_options=advanced_security_options,
            cluster_config=cluster_config,
            cognito_options=cognito_options,
            domain_arn=domain_arn,
            domain_endpoint_options=domain_endpoint_options,
            domain_name=domain_name,
            ebs_options=ebs_options,
            encryption_at_rest_options=encryption_at_rest_options,
            engine_version=engine_version,
            ip_address_type=ip_address_type,
            log_publishing_options=log_publishing_options,
            node_to_node_encryption_options=node_to_node_encryption_options,
            off_peak_window_options=off_peak_window_options,
            snapshot_options=snapshot_options,
            software_update_options=software_update_options,
            tags=tags,
            vpc_options=vpc_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36055c1f3a4932ba1e8f0542c29f5149d636738c30a3d9d1bdafb864d00f2e64)
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
            type_hints = typing.get_type_hints(_typecheckingstub__82c494c700f6860a942b3abd6b86cf929f307e898357419f56692f0b4084c2a5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAdvancedSecurityOptionsAnonymousAuthDisableDate")
    def attr_advanced_security_options_anonymous_auth_disable_date(
        self,
    ) -> builtins.str:
        '''Date and time when the migration period will be disabled.

        Only necessary when `enabling fine-grained access control on an existing domain <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing>`_ .

        :cloudformationAttribute: AdvancedSecurityOptions.AnonymousAuthDisableDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAdvancedSecurityOptionsAnonymousAuthDisableDate"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the CloudFormation stack.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainEndpoint")
    def attr_domain_endpoint(self) -> builtins.str:
        '''The domain-specific endpoint used for requests to the OpenSearch APIs, such as ``search-mystack-1ab2cdefghij-ab1c2deckoyb3hofw7wpqa3cm.us-west-1.es.amazonaws.com`` .

        :cloudformationAttribute: DomainEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainEndpoints")
    def attr_domain_endpoints(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: DomainEndpoints
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDomainEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainEndpointV2")
    def attr_domain_endpoint_v2(self) -> builtins.str:
        '''If ``IPAddressType`` to set to ``dualstack`` , a version 2 domain endpoint is provisioned.

        This endpoint functions like a normal endpoint, except that it works with both IPv4 and IPv6 IP addresses. Normal endpoints work only with IPv4 IP addresses.

        :cloudformationAttribute: DomainEndpointV2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainEndpointV2"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The resource ID.

        For example, ``123456789012/my-domain`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptions")
    def attr_service_software_options(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrServiceSoftwareOptions"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptionsAutomatedUpdateDate")
    def attr_service_software_options_automated_update_date(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions.AutomatedUpdateDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceSoftwareOptionsAutomatedUpdateDate"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptionsCancellable")
    def attr_service_software_options_cancellable(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions.Cancellable
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrServiceSoftwareOptionsCancellable"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptionsCurrentVersion")
    def attr_service_software_options_current_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions.CurrentVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceSoftwareOptionsCurrentVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptionsDescription")
    def attr_service_software_options_description(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions.Description
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceSoftwareOptionsDescription"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptionsNewVersion")
    def attr_service_software_options_new_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions.NewVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceSoftwareOptionsNewVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptionsOptionalDeployment")
    def attr_service_software_options_optional_deployment(
        self,
    ) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions.OptionalDeployment
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrServiceSoftwareOptionsOptionalDeployment"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptionsUpdateAvailable")
    def attr_service_software_options_update_available(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions.UpdateAvailable
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrServiceSoftwareOptionsUpdateAvailable"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceSoftwareOptionsUpdateStatus")
    def attr_service_software_options_update_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceSoftwareOptions.UpdateStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceSoftwareOptionsUpdateStatus"))

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
    @jsii.member(jsii_name="accessPolicies")
    def access_policies(self) -> typing.Any:
        '''An AWS Identity and Access Management ( IAM ) policy document that specifies who can access the OpenSearch Service domain and their permissions.'''
        return typing.cast(typing.Any, jsii.get(self, "accessPolicies"))

    @access_policies.setter
    def access_policies(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5300173c129717cc6b181e91e5685dc6f63810f40281dca8b4c3a64113df8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="advancedOptions")
    def advanced_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional options to specify for the OpenSearch Service domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "advancedOptions"))

    @advanced_options.setter
    def advanced_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a8bbf96e0583433dd9f44c7bc58405687275c5e3102497c3de8597470024609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedOptions", value)

    @builtins.property
    @jsii.member(jsii_name="advancedSecurityOptions")
    def advanced_security_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AdvancedSecurityOptionsInputProperty"]]:
        '''Specifies options for fine-grained access control and SAML authentication.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AdvancedSecurityOptionsInputProperty"]], jsii.get(self, "advancedSecurityOptions"))

    @advanced_security_options.setter
    def advanced_security_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AdvancedSecurityOptionsInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__228f471e13ce4e3daa56e3913f7b610971afccf6ec06adc08af42a85ad0abde9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedSecurityOptions", value)

    @builtins.property
    @jsii.member(jsii_name="clusterConfig")
    def cluster_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ClusterConfigProperty"]]:
        '''Container for the cluster configuration of a domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ClusterConfigProperty"]], jsii.get(self, "clusterConfig"))

    @cluster_config.setter
    def cluster_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ClusterConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa86e4bef09a3455a33af8fe1a0310646154d89f5113370b517cfbe529c69080)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterConfig", value)

    @builtins.property
    @jsii.member(jsii_name="cognitoOptions")
    def cognito_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.CognitoOptionsProperty"]]:
        '''Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.CognitoOptionsProperty"]], jsii.get(self, "cognitoOptions"))

    @cognito_options.setter
    def cognito_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.CognitoOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba3653fa5c99276b72d7f6127ab8c7a58e79d65fa1bb3870a642aae948411169)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cognitoOptions", value)

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainArn"))

    @domain_arn.setter
    def domain_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3136cec5fb1c8bfbc63aa354d269746af30bf8ace2a1386b3c54154aef71642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainArn", value)

    @builtins.property
    @jsii.member(jsii_name="domainEndpointOptions")
    def domain_endpoint_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.DomainEndpointOptionsProperty"]]:
        '''Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.DomainEndpointOptionsProperty"]], jsii.get(self, "domainEndpointOptions"))

    @domain_endpoint_options.setter
    def domain_endpoint_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.DomainEndpointOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af44788b6e909cca8e8e5c9cb554dda8dc1f217fe434e42fd8738b0f0636804e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainEndpointOptions", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''A name for the OpenSearch Service domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fbf0bdf5087e279e6006801d40e67891ae239f2249b16c7c14ce58bd2d0e85e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="ebsOptions")
    def ebs_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EBSOptionsProperty"]]:
        '''The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EBSOptionsProperty"]], jsii.get(self, "ebsOptions"))

    @ebs_options.setter
    def ebs_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EBSOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c4377e2450f1c3438e90e2429bf9650c6490320abe0c622e2a80734761fec52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptions", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionAtRestOptions")
    def encryption_at_rest_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EncryptionAtRestOptionsProperty"]]:
        '''Whether the domain should encrypt data at rest, and if so, the AWS KMS key to use.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EncryptionAtRestOptionsProperty"]], jsii.get(self, "encryptionAtRestOptions"))

    @encryption_at_rest_options.setter
    def encryption_at_rest_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EncryptionAtRestOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a2b92e6c487faf5299f3c6d1f31ea619c1b1d93925b6634dfc0b81cde67cf89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtRestOptions", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version of OpenSearch to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88301df742e18b9ab560ac04b99b966a761eeee663731308b40ab8ca4cd509f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''Choose either dual stack or IPv4 as your IP address type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15de3b6bee67c94e6a9ff942356ecb4f67771482ab0d1655f673b885868135c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value)

    @builtins.property
    @jsii.member(jsii_name="logPublishingOptions")
    def log_publishing_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnDomain.LogPublishingOptionProperty"]]]]:
        '''An object with one or more of the following keys: ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , ``AUDIT_LOGS`` , depending on the types of logs you want to publish.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnDomain.LogPublishingOptionProperty"]]]], jsii.get(self, "logPublishingOptions"))

    @log_publishing_options.setter
    def log_publishing_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnDomain.LogPublishingOptionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ad842d30b972e4535042c97d9a43923a473c809de18faef95c075764d365933)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logPublishingOptions", value)

    @builtins.property
    @jsii.member(jsii_name="nodeToNodeEncryptionOptions")
    def node_to_node_encryption_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.NodeToNodeEncryptionOptionsProperty"]]:
        '''Specifies whether node-to-node encryption is enabled.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.NodeToNodeEncryptionOptionsProperty"]], jsii.get(self, "nodeToNodeEncryptionOptions"))

    @node_to_node_encryption_options.setter
    def node_to_node_encryption_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.NodeToNodeEncryptionOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd0a25ab3a544c4d8cceb480a502adf178ccdbe1d5fdc2273557e28bb2a3b65a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeToNodeEncryptionOptions", value)

    @builtins.property
    @jsii.member(jsii_name="offPeakWindowOptions")
    def off_peak_window_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.OffPeakWindowOptionsProperty"]]:
        '''Options for a domain's off-peak window, during which OpenSearch Service can perform mandatory configuration changes on the domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.OffPeakWindowOptionsProperty"]], jsii.get(self, "offPeakWindowOptions"))

    @off_peak_window_options.setter
    def off_peak_window_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.OffPeakWindowOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a3a2b200397209bed0a90cb39485a3ccb08bcbb3d56bbecc1ef0b66b5d0e9c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offPeakWindowOptions", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotOptions")
    def snapshot_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SnapshotOptionsProperty"]]:
        '''*DEPRECATED* .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SnapshotOptionsProperty"]], jsii.get(self, "snapshotOptions"))

    @snapshot_options.setter
    def snapshot_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SnapshotOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4355f39393b86da5d9d2bb3c03113864e6a1293ce3a4a9b21ccbc2f55009520a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotOptions", value)

    @builtins.property
    @jsii.member(jsii_name="softwareUpdateOptions")
    def software_update_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SoftwareUpdateOptionsProperty"]]:
        '''Service software update options for the domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SoftwareUpdateOptionsProperty"]], jsii.get(self, "softwareUpdateOptions"))

    @software_update_options.setter
    def software_update_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SoftwareUpdateOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8acae61e3be2830b5d0094ea6fec133fbcd21857779bf3d47fd39615ad0e27eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "softwareUpdateOptions", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Service domain.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__492b192acd9acaa788b5501251071046e08d3e3cb47dc8fe653c58c5857dbc08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcOptions")
    def vpc_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.VPCOptionsProperty"]]:
        '''The virtual private cloud (VPC) configuration for the OpenSearch Service domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.VPCOptionsProperty"]], jsii.get(self, "vpcOptions"))

    @vpc_options.setter
    def vpc_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.VPCOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b93b8c5b5730096cbd511fb71c9b9508cb307bcbfee46f7a0c11da785c33d2e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcOptions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.AdvancedSecurityOptionsInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "anonymous_auth_disable_date": "anonymousAuthDisableDate",
            "anonymous_auth_enabled": "anonymousAuthEnabled",
            "enabled": "enabled",
            "internal_user_database_enabled": "internalUserDatabaseEnabled",
            "master_user_options": "masterUserOptions",
            "saml_options": "samlOptions",
        },
    )
    class AdvancedSecurityOptionsInputProperty:
        def __init__(
            self,
            *,
            anonymous_auth_disable_date: typing.Optional[builtins.str] = None,
            anonymous_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            master_user_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.MasterUserOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            saml_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.SAMLOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies options for fine-grained access control.

            If you specify advanced security options, you must also enable node-to-node encryption ( `NodeToNodeEncryptionOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html>`_ ) and encryption at rest ( `EncryptionAtRestOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html>`_ ). You must also enable ``EnforceHTTPS`` within `DomainEndpointOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html>`_ , which requires HTTPS for all traffic to the domain.

            :param anonymous_auth_disable_date: Date and time when the migration period will be disabled. Only necessary when `enabling fine-grained access control on an existing domain <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing>`_ .
            :param anonymous_auth_enabled: True to enable a 30-day migration period during which administrators can create role mappings. Only necessary when `enabling fine-grained access control on an existing domain <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing>`_ .
            :param enabled: True to enable fine-grained access control. You must also enable encryption of data at rest and node-to-node encryption. See `Fine-grained access control in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html>`_ .
            :param internal_user_database_enabled: True to enable the internal user database.
            :param master_user_options: Specifies information about the master user.
            :param saml_options: Container for information about the SAML configuration for OpenSearch Dashboards.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                advanced_security_options_input_property = opensearchservice.CfnDomain.AdvancedSecurityOptionsInputProperty(
                    anonymous_auth_disable_date="anonymousAuthDisableDate",
                    anonymous_auth_enabled=False,
                    enabled=False,
                    internal_user_database_enabled=False,
                    master_user_options=opensearchservice.CfnDomain.MasterUserOptionsProperty(
                        master_user_arn="masterUserArn",
                        master_user_name="masterUserName",
                        master_user_password="masterUserPassword"
                    ),
                    saml_options=opensearchservice.CfnDomain.SAMLOptionsProperty(
                        enabled=False,
                        idp=opensearchservice.CfnDomain.IdpProperty(
                            entity_id="entityId",
                            metadata_content="metadataContent"
                        ),
                        master_backend_role="masterBackendRole",
                        master_user_name="masterUserName",
                        roles_key="rolesKey",
                        session_timeout_minutes=123,
                        subject_key="subjectKey"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd5c3c68239a044600ab387ec52e22ed8852c6e213d5626aa4396b28aab3af9e)
                check_type(argname="argument anonymous_auth_disable_date", value=anonymous_auth_disable_date, expected_type=type_hints["anonymous_auth_disable_date"])
                check_type(argname="argument anonymous_auth_enabled", value=anonymous_auth_enabled, expected_type=type_hints["anonymous_auth_enabled"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument internal_user_database_enabled", value=internal_user_database_enabled, expected_type=type_hints["internal_user_database_enabled"])
                check_type(argname="argument master_user_options", value=master_user_options, expected_type=type_hints["master_user_options"])
                check_type(argname="argument saml_options", value=saml_options, expected_type=type_hints["saml_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if anonymous_auth_disable_date is not None:
                self._values["anonymous_auth_disable_date"] = anonymous_auth_disable_date
            if anonymous_auth_enabled is not None:
                self._values["anonymous_auth_enabled"] = anonymous_auth_enabled
            if enabled is not None:
                self._values["enabled"] = enabled
            if internal_user_database_enabled is not None:
                self._values["internal_user_database_enabled"] = internal_user_database_enabled
            if master_user_options is not None:
                self._values["master_user_options"] = master_user_options
            if saml_options is not None:
                self._values["saml_options"] = saml_options

        @builtins.property
        def anonymous_auth_disable_date(self) -> typing.Optional[builtins.str]:
            '''Date and time when the migration period will be disabled.

            Only necessary when `enabling fine-grained access control on an existing domain <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-anonymousauthdisabledate
            '''
            result = self._values.get("anonymous_auth_disable_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def anonymous_auth_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to enable a 30-day migration period during which administrators can create role mappings.

            Only necessary when `enabling fine-grained access control on an existing domain <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-anonymousauthenabled
            '''
            result = self._values.get("anonymous_auth_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to enable fine-grained access control.

            You must also enable encryption of data at rest and node-to-node encryption. See `Fine-grained access control in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def internal_user_database_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to enable the internal user database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled
            '''
            result = self._values.get("internal_user_database_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def master_user_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.MasterUserOptionsProperty"]]:
            '''Specifies information about the master user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-masteruseroptions
            '''
            result = self._values.get("master_user_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.MasterUserOptionsProperty"]], result)

        @builtins.property
        def saml_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SAMLOptionsProperty"]]:
            '''Container for information about the SAML configuration for OpenSearch Dashboards.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-samloptions
            '''
            result = self._values.get("saml_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SAMLOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedSecurityOptionsInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cold_storage_options": "coldStorageOptions",
            "dedicated_master_count": "dedicatedMasterCount",
            "dedicated_master_enabled": "dedicatedMasterEnabled",
            "dedicated_master_type": "dedicatedMasterType",
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "multi_az_with_standby_enabled": "multiAzWithStandbyEnabled",
            "warm_count": "warmCount",
            "warm_enabled": "warmEnabled",
            "warm_type": "warmType",
            "zone_awareness_config": "zoneAwarenessConfig",
            "zone_awareness_enabled": "zoneAwarenessEnabled",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            cold_storage_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ColdStorageOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dedicated_master_count: typing.Optional[jsii.Number] = None,
            dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            dedicated_master_type: typing.Optional[builtins.str] = None,
            instance_count: typing.Optional[jsii.Number] = None,
            instance_type: typing.Optional[builtins.str] = None,
            multi_az_with_standby_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            warm_count: typing.Optional[jsii.Number] = None,
            warm_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            warm_type: typing.Optional[builtins.str] = None,
            zone_awareness_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ZoneAwarenessConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The cluster configuration for the OpenSearch Service domain.

            You can specify options such as the instance type and the number of instances. For more information, see `Creating and managing Amazon OpenSearch Service domains <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param cold_storage_options: Container for cold storage configuration options.
            :param dedicated_master_count: The number of instances to use for the master node. If you specify this property, you must specify ``true`` for the ``DedicatedMasterEnabled`` property.
            :param dedicated_master_enabled: Indicates whether to use a dedicated master node for the OpenSearch Service domain. A dedicated master node is a cluster node that performs cluster management tasks, but doesn't hold data or respond to data upload requests. Dedicated master nodes offload cluster management tasks to increase the stability of your search clusters. See `Dedicated master nodes in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html>`_ .
            :param dedicated_master_type: The hardware configuration of the computer that hosts the dedicated master node, such as ``m3.medium.search`` . If you specify this property, you must specify ``true`` for the ``DedicatedMasterEnabled`` property. For valid values, see `Supported instance types in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ .
            :param instance_count: The number of data nodes (instances) to use in the OpenSearch Service domain.
            :param instance_type: The instance type for your data nodes, such as ``m3.medium.search`` . For valid values, see `Supported instance types in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ .
            :param multi_az_with_standby_enabled: Indicates whether Multi-AZ with Standby deployment option is enabled. For more information, see `Multi-AZ with Standby <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html#managedomains-za-standby>`_ .
            :param warm_count: The number of warm nodes in the cluster.
            :param warm_enabled: Whether to enable UltraWarm storage for the cluster. See `UltraWarm storage for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ultrawarm.html>`_ .
            :param warm_type: The instance type for the cluster's warm nodes.
            :param zone_awareness_config: Specifies zone awareness configuration options. Only use if ``ZoneAwarenessEnabled`` is ``true`` .
            :param zone_awareness_enabled: Indicates whether to enable zone awareness for the OpenSearch Service domain. When you enable zone awareness, OpenSearch Service allocates the nodes and replica index shards that belong to a cluster across two Availability Zones (AZs) in the same region to prevent data loss and minimize downtime in the event of node or data center failure. Don't enable zone awareness if your cluster has no replica index shards or is a single-node cluster. For more information, see `Configuring a multi-AZ domain in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                cluster_config_property = opensearchservice.CfnDomain.ClusterConfigProperty(
                    cold_storage_options=opensearchservice.CfnDomain.ColdStorageOptionsProperty(
                        enabled=False
                    ),
                    dedicated_master_count=123,
                    dedicated_master_enabled=False,
                    dedicated_master_type="dedicatedMasterType",
                    instance_count=123,
                    instance_type="instanceType",
                    multi_az_with_standby_enabled=False,
                    warm_count=123,
                    warm_enabled=False,
                    warm_type="warmType",
                    zone_awareness_config=opensearchservice.CfnDomain.ZoneAwarenessConfigProperty(
                        availability_zone_count=123
                    ),
                    zone_awareness_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3aeae3d5b66cfdff675e691ae3d90b2e82990d0dc2a13a8fbab733bba4e26eda)
                check_type(argname="argument cold_storage_options", value=cold_storage_options, expected_type=type_hints["cold_storage_options"])
                check_type(argname="argument dedicated_master_count", value=dedicated_master_count, expected_type=type_hints["dedicated_master_count"])
                check_type(argname="argument dedicated_master_enabled", value=dedicated_master_enabled, expected_type=type_hints["dedicated_master_enabled"])
                check_type(argname="argument dedicated_master_type", value=dedicated_master_type, expected_type=type_hints["dedicated_master_type"])
                check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument multi_az_with_standby_enabled", value=multi_az_with_standby_enabled, expected_type=type_hints["multi_az_with_standby_enabled"])
                check_type(argname="argument warm_count", value=warm_count, expected_type=type_hints["warm_count"])
                check_type(argname="argument warm_enabled", value=warm_enabled, expected_type=type_hints["warm_enabled"])
                check_type(argname="argument warm_type", value=warm_type, expected_type=type_hints["warm_type"])
                check_type(argname="argument zone_awareness_config", value=zone_awareness_config, expected_type=type_hints["zone_awareness_config"])
                check_type(argname="argument zone_awareness_enabled", value=zone_awareness_enabled, expected_type=type_hints["zone_awareness_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cold_storage_options is not None:
                self._values["cold_storage_options"] = cold_storage_options
            if dedicated_master_count is not None:
                self._values["dedicated_master_count"] = dedicated_master_count
            if dedicated_master_enabled is not None:
                self._values["dedicated_master_enabled"] = dedicated_master_enabled
            if dedicated_master_type is not None:
                self._values["dedicated_master_type"] = dedicated_master_type
            if instance_count is not None:
                self._values["instance_count"] = instance_count
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if multi_az_with_standby_enabled is not None:
                self._values["multi_az_with_standby_enabled"] = multi_az_with_standby_enabled
            if warm_count is not None:
                self._values["warm_count"] = warm_count
            if warm_enabled is not None:
                self._values["warm_enabled"] = warm_enabled
            if warm_type is not None:
                self._values["warm_type"] = warm_type
            if zone_awareness_config is not None:
                self._values["zone_awareness_config"] = zone_awareness_config
            if zone_awareness_enabled is not None:
                self._values["zone_awareness_enabled"] = zone_awareness_enabled

        @builtins.property
        def cold_storage_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ColdStorageOptionsProperty"]]:
            '''Container for cold storage configuration options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-coldstorageoptions
            '''
            result = self._values.get("cold_storage_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ColdStorageOptionsProperty"]], result)

        @builtins.property
        def dedicated_master_count(self) -> typing.Optional[jsii.Number]:
            '''The number of instances to use for the master node.

            If you specify this property, you must specify ``true`` for the ``DedicatedMasterEnabled`` property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmastercount
            '''
            result = self._values.get("dedicated_master_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dedicated_master_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to use a dedicated master node for the OpenSearch Service domain.

            A dedicated master node is a cluster node that performs cluster management tasks, but doesn't hold data or respond to data upload requests. Dedicated master nodes offload cluster management tasks to increase the stability of your search clusters. See `Dedicated master nodes in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmasterenabled
            '''
            result = self._values.get("dedicated_master_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def dedicated_master_type(self) -> typing.Optional[builtins.str]:
            '''The hardware configuration of the computer that hosts the dedicated master node, such as ``m3.medium.search`` . If you specify this property, you must specify ``true`` for the ``DedicatedMasterEnabled`` property. For valid values, see `Supported instance types in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmastertype
            '''
            result = self._values.get("dedicated_master_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_count(self) -> typing.Optional[jsii.Number]:
            '''The number of data nodes (instances) to use in the OpenSearch Service domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''The instance type for your data nodes, such as ``m3.medium.search`` . For valid values, see `Supported instance types in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def multi_az_with_standby_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether Multi-AZ with Standby deployment option is enabled.

            For more information, see `Multi-AZ with Standby <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html#managedomains-za-standby>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-multiazwithstandbyenabled
            '''
            result = self._values.get("multi_az_with_standby_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def warm_count(self) -> typing.Optional[jsii.Number]:
            '''The number of warm nodes in the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmcount
            '''
            result = self._values.get("warm_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def warm_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to enable UltraWarm storage for the cluster.

            See `UltraWarm storage for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ultrawarm.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmenabled
            '''
            result = self._values.get("warm_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def warm_type(self) -> typing.Optional[builtins.str]:
            '''The instance type for the cluster's warm nodes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmtype
            '''
            result = self._values.get("warm_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zone_awareness_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ZoneAwarenessConfigProperty"]]:
            '''Specifies zone awareness configuration options.

            Only use if ``ZoneAwarenessEnabled`` is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-zoneawarenessconfig
            '''
            result = self._values.get("zone_awareness_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ZoneAwarenessConfigProperty"]], result)

        @builtins.property
        def zone_awareness_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to enable zone awareness for the OpenSearch Service domain.

            When you enable zone awareness, OpenSearch Service allocates the nodes and replica index shards that belong to a cluster across two Availability Zones (AZs) in the same region to prevent data loss and minimize downtime in the event of node or data center failure. Don't enable zone awareness if your cluster has no replica index shards or is a single-node cluster. For more information, see `Configuring a multi-AZ domain in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-zoneawarenessenabled
            '''
            result = self._values.get("zone_awareness_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.CognitoOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "identity_pool_id": "identityPoolId",
            "role_arn": "roleArn",
            "user_pool_id": "userPoolId",
        },
    )
    class CognitoOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            identity_pool_id: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
            user_pool_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.

            :param enabled: Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards. See `Amazon Cognito authentication for OpenSearch Dashboards <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html>`_ .
            :param identity_pool_id: The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication. Required if you enabled Cognito Authentication for OpenSearch Dashboards.
            :param role_arn: The ``AmazonOpenSearchServiceCognitoAccess`` role that allows OpenSearch Service to configure your user pool and identity pool. Required if you enabled Cognito Authentication for OpenSearch Dashboards.
            :param user_pool_id: The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication. Required if you enabled Cognito Authentication for OpenSearch Dashboards.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                cognito_options_property = opensearchservice.CfnDomain.CognitoOptionsProperty(
                    enabled=False,
                    identity_pool_id="identityPoolId",
                    role_arn="roleArn",
                    user_pool_id="userPoolId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e167c0d00635fad84f1646761ab6a47124b645d9a98a38bc74beb3d2ecbca1c2)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if identity_pool_id is not None:
                self._values["identity_pool_id"] = identity_pool_id
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards.

            See `Amazon Cognito authentication for OpenSearch Dashboards <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def identity_pool_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

            Required if you enabled Cognito Authentication for OpenSearch Dashboards.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-identitypoolid
            '''
            result = self._values.get("identity_pool_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ``AmazonOpenSearchServiceCognitoAccess`` role that allows OpenSearch Service to configure your user pool and identity pool.

            Required if you enabled Cognito Authentication for OpenSearch Dashboards.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_pool_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

            Required if you enabled Cognito Authentication for OpenSearch Dashboards.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-userpoolid
            '''
            result = self._values.get("user_pool_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.ColdStorageOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class ColdStorageOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Container for the parameters required to enable cold storage for an OpenSearch Service domain.

            For more information, see `Cold storage for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cold-storage.html>`_ .

            :param enabled: Whether to enable or disable cold storage on the domain. You must enable UltraWarm storage to enable cold storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-coldstorageoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                cold_storage_options_property = opensearchservice.CfnDomain.ColdStorageOptionsProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c3864a36f4132782987b173c24fdcbec6040683b2f632146b11bb53578fc274f)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to enable or disable cold storage on the domain.

            You must enable UltraWarm storage to enable cold storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-coldstorageoptions.html#cfn-opensearchservice-domain-coldstorageoptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColdStorageOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.DomainEndpointOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_endpoint": "customEndpoint",
            "custom_endpoint_certificate_arn": "customEndpointCertificateArn",
            "custom_endpoint_enabled": "customEndpointEnabled",
            "enforce_https": "enforceHttps",
            "tls_security_policy": "tlsSecurityPolicy",
        },
    )
    class DomainEndpointOptionsProperty:
        def __init__(
            self,
            *,
            custom_endpoint: typing.Optional[builtins.str] = None,
            custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
            custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enforce_https: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            tls_security_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.

            :param custom_endpoint: The fully qualified URL for your custom endpoint. Required if you enabled a custom endpoint for the domain.
            :param custom_endpoint_certificate_arn: The AWS Certificate Manager ARN for your domain's SSL/TLS certificate. Required if you enabled a custom endpoint for the domain.
            :param custom_endpoint_enabled: True to enable a custom endpoint for the domain. If enabled, you must also provide values for ``CustomEndpoint`` and ``CustomEndpointCertificateArn`` .
            :param enforce_https: True to require that all traffic to the domain arrive over HTTPS. Required if you enable fine-grained access control in `AdvancedSecurityOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .
            :param tls_security_policy: The minimum TLS version required for traffic to the domain. Valid values are TLS 1.3 (recommended) or 1.2:. - ``Policy-Min-TLS-1-0-2019-07`` - ``Policy-Min-TLS-1-2-2019-07``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                domain_endpoint_options_property = opensearchservice.CfnDomain.DomainEndpointOptionsProperty(
                    custom_endpoint="customEndpoint",
                    custom_endpoint_certificate_arn="customEndpointCertificateArn",
                    custom_endpoint_enabled=False,
                    enforce_https=False,
                    tls_security_policy="tlsSecurityPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e1afb3f072b83950253cff17b0d6c2d24505ec14925f8f1b645dd5c539c2ca4d)
                check_type(argname="argument custom_endpoint", value=custom_endpoint, expected_type=type_hints["custom_endpoint"])
                check_type(argname="argument custom_endpoint_certificate_arn", value=custom_endpoint_certificate_arn, expected_type=type_hints["custom_endpoint_certificate_arn"])
                check_type(argname="argument custom_endpoint_enabled", value=custom_endpoint_enabled, expected_type=type_hints["custom_endpoint_enabled"])
                check_type(argname="argument enforce_https", value=enforce_https, expected_type=type_hints["enforce_https"])
                check_type(argname="argument tls_security_policy", value=tls_security_policy, expected_type=type_hints["tls_security_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_endpoint is not None:
                self._values["custom_endpoint"] = custom_endpoint
            if custom_endpoint_certificate_arn is not None:
                self._values["custom_endpoint_certificate_arn"] = custom_endpoint_certificate_arn
            if custom_endpoint_enabled is not None:
                self._values["custom_endpoint_enabled"] = custom_endpoint_enabled
            if enforce_https is not None:
                self._values["enforce_https"] = enforce_https
            if tls_security_policy is not None:
                self._values["tls_security_policy"] = tls_security_policy

        @builtins.property
        def custom_endpoint(self) -> typing.Optional[builtins.str]:
            '''The fully qualified URL for your custom endpoint.

            Required if you enabled a custom endpoint for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpoint
            '''
            result = self._values.get("custom_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_endpoint_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The AWS Certificate Manager ARN for your domain's SSL/TLS certificate.

            Required if you enabled a custom endpoint for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpointcertificatearn
            '''
            result = self._values.get("custom_endpoint_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_endpoint_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to enable a custom endpoint for the domain.

            If enabled, you must also provide values for ``CustomEndpoint`` and ``CustomEndpointCertificateArn`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpointenabled
            '''
            result = self._values.get("custom_endpoint_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enforce_https(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to require that all traffic to the domain arrive over HTTPS.

            Required if you enable fine-grained access control in `AdvancedSecurityOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-enforcehttps
            '''
            result = self._values.get("enforce_https")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def tls_security_policy(self) -> typing.Optional[builtins.str]:
            '''The minimum TLS version required for traffic to the domain. Valid values are TLS 1.3 (recommended) or 1.2:.

            - ``Policy-Min-TLS-1-0-2019-07``
            - ``Policy-Min-TLS-1-2-2019-07``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-tlssecuritypolicy
            '''
            result = self._values.get("tls_security_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainEndpointOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.EBSOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_enabled": "ebsEnabled",
            "iops": "iops",
            "throughput": "throughput",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EBSOptionsProperty:
        def __init__(
            self,
            *,
            ebs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            iops: typing.Optional[jsii.Number] = None,
            throughput: typing.Optional[jsii.Number] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain.

            For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param ebs_enabled: Specifies whether Amazon EBS volumes are attached to data nodes in the OpenSearch Service domain.
            :param iops: The number of I/O operations per second (IOPS) that the volume supports. This property applies only to the ``gp3`` and provisioned IOPS EBS volume types.
            :param throughput: The throughput (in MiB/s) of the EBS volumes attached to data nodes. Applies only to the ``gp3`` volume type.
            :param volume_size: The size (in GiB) of the EBS volume for each data node. The minimum and maximum size of an EBS volume depends on the EBS volume type and the instance type to which it is attached. For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .
            :param volume_type: The EBS volume type to use with the OpenSearch Service domain. If you choose ``gp3`` , you must also specify values for ``Iops`` and ``Throughput`` . For more information about each type, see `Amazon EBS volume types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`_ in the *Amazon EC2 User Guide for Linux Instances* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                e_bSOptions_property = opensearchservice.CfnDomain.EBSOptionsProperty(
                    ebs_enabled=False,
                    iops=123,
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0edcf62ab77376e080d4b111ffdeee55bda3d1ea1c392a1acb86f78ce234e31b)
                check_type(argname="argument ebs_enabled", value=ebs_enabled, expected_type=type_hints["ebs_enabled"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ebs_enabled is not None:
                self._values["ebs_enabled"] = ebs_enabled
            if iops is not None:
                self._values["iops"] = iops
            if throughput is not None:
                self._values["throughput"] = throughput
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def ebs_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether Amazon EBS volumes are attached to data nodes in the OpenSearch Service domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-ebsenabled
            '''
            result = self._values.get("ebs_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The number of I/O operations per second (IOPS) that the volume supports.

            This property applies only to the ``gp3`` and provisioned IOPS EBS volume types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''The throughput (in MiB/s) of the EBS volumes attached to data nodes.

            Applies only to the ``gp3`` volume type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''The size (in GiB) of the EBS volume for each data node.

            The minimum and maximum size of an EBS volume depends on the EBS volume type and the instance type to which it is attached. For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''The EBS volume type to use with the OpenSearch Service domain.

            If you choose ``gp3`` , you must also specify values for ``Iops`` and ``Throughput`` . For more information about each type, see `Amazon EBS volume types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`_ in the *Amazon EC2 User Guide for Linux Instances* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EBSOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.EncryptionAtRestOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "kms_key_id": "kmsKeyId"},
    )
    class EncryptionAtRestOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Whether the domain should encrypt data at rest, and if so, the AWS Key Management Service key to use.

            :param enabled: Specify ``true`` to enable encryption at rest. Required if you enable fine-grained access control in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ . If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.
            :param kms_key_id: The KMS key ID. Takes the form ``1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a`` . Required if you enable encryption at rest. You can also use ``keyAlias`` as a value. If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                encryption_at_rest_options_property = opensearchservice.CfnDomain.EncryptionAtRestOptionsProperty(
                    enabled=False,
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8045e71bf2b9389f7b778b391167aea3cf2ff9b7ccd6b9462c26cc1dcd4f9cbc)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify ``true`` to enable encryption at rest. Required if you enable fine-grained access control in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .

            If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html#cfn-opensearchservice-domain-encryptionatrestoptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS key ID. Takes the form ``1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a`` . Required if you enable encryption at rest.

            You can also use ``keyAlias`` as a value.

            If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html#cfn-opensearchservice-domain-encryptionatrestoptions-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionAtRestOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.IdpProperty",
        jsii_struct_bases=[],
        name_mapping={"entity_id": "entityId", "metadata_content": "metadataContent"},
    )
    class IdpProperty:
        def __init__(
            self,
            *,
            entity_id: builtins.str,
            metadata_content: builtins.str,
        ) -> None:
            '''The SAML Identity Provider's information.

            :param entity_id: The unique entity ID of the application in the SAML identity provider.
            :param metadata_content: The metadata of the SAML application, in XML format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-idp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                idp_property = opensearchservice.CfnDomain.IdpProperty(
                    entity_id="entityId",
                    metadata_content="metadataContent"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df207d57c5bf0c99afe86b2563e40142d554f359eddff25bfecdf22c97a3ed72)
                check_type(argname="argument entity_id", value=entity_id, expected_type=type_hints["entity_id"])
                check_type(argname="argument metadata_content", value=metadata_content, expected_type=type_hints["metadata_content"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entity_id": entity_id,
                "metadata_content": metadata_content,
            }

        @builtins.property
        def entity_id(self) -> builtins.str:
            '''The unique entity ID of the application in the SAML identity provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-idp.html#cfn-opensearchservice-domain-idp-entityid
            '''
            result = self._values.get("entity_id")
            assert result is not None, "Required property 'entity_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metadata_content(self) -> builtins.str:
            '''The metadata of the SAML application, in XML format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-idp.html#cfn-opensearchservice-domain-idp-metadatacontent
            '''
            result = self._values.get("metadata_content")
            assert result is not None, "Required property 'metadata_content' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdpProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.LogPublishingOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_log_group_arn": "cloudWatchLogsLogGroupArn",
            "enabled": "enabled",
        },
    )
    class LogPublishingOptionProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies whether the OpenSearch Service domain publishes application, search slow logs, or index slow logs to Amazon CloudWatch.

            Each option must be an object of name ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , or ``AUDIT_LOGS`` depending on the type of logs you want to publish. For the full syntax, see the `examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain--examples>`_ .

            Before you enable log publishing, you need to create a CloudWatch log group and provide OpenSearch Service the correct permissions to write to it. To learn more, see `Enabling log publishing ( AWS CloudFormation) <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html#createdomain-configure-slow-logs-cfn>`_ .

            :param cloud_watch_logs_log_group_arn: Specifies the CloudWatch log group to publish to. Required if you enable log publishing.
            :param enabled: If ``true`` , enables the publishing of logs to CloudWatch. Default: ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                log_publishing_option_property = opensearchservice.CfnDomain.LogPublishingOptionProperty(
                    cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn",
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f619e98a16faa2be95396251f0c046225b41dc39039c1064a235021c6127a509)
                check_type(argname="argument cloud_watch_logs_log_group_arn", value=cloud_watch_logs_log_group_arn, expected_type=type_hints["cloud_watch_logs_log_group_arn"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs_log_group_arn is not None:
                self._values["cloud_watch_logs_log_group_arn"] = cloud_watch_logs_log_group_arn
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def cloud_watch_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
            '''Specifies the CloudWatch log group to publish to.

            Required if you enable log publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html#cfn-opensearchservice-domain-logpublishingoption-cloudwatchlogsloggrouparn
            '''
            result = self._values.get("cloud_watch_logs_log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , enables the publishing of logs to CloudWatch.

            Default: ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html#cfn-opensearchservice-domain-logpublishingoption-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogPublishingOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.MasterUserOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "master_user_arn": "masterUserArn",
            "master_user_name": "masterUserName",
            "master_user_password": "masterUserPassword",
        },
    )
    class MasterUserOptionsProperty:
        def __init__(
            self,
            *,
            master_user_arn: typing.Optional[builtins.str] = None,
            master_user_name: typing.Optional[builtins.str] = None,
            master_user_password: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies information about the master user.

            Required if ``InternalUserDatabaseEnabled`` is true in `AdvancedSecurityOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .

            :param master_user_arn: Amazon Resource Name (ARN) for the master user. The ARN can point to an IAM user or role. This property is required for Amazon Cognito to work, and it must match the role configured for Cognito. Only specify if ``InternalUserDatabaseEnabled`` is false in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .
            :param master_user_name: Username for the master user. Only specify if ``InternalUserDatabaseEnabled`` is true in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ . If you don't want to specify this value directly within the template, you can use a `dynamic reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html>`_ instead.
            :param master_user_password: Password for the master user. Only specify if ``InternalUserDatabaseEnabled`` is true in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ . If you don't want to specify this value directly within the template, you can use a `dynamic reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html>`_ instead.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                master_user_options_property = opensearchservice.CfnDomain.MasterUserOptionsProperty(
                    master_user_arn="masterUserArn",
                    master_user_name="masterUserName",
                    master_user_password="masterUserPassword"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d898e88f61289087d3cdae775ccfc96a5810d38fd1a901ddd469c8377d40e163)
                check_type(argname="argument master_user_arn", value=master_user_arn, expected_type=type_hints["master_user_arn"])
                check_type(argname="argument master_user_name", value=master_user_name, expected_type=type_hints["master_user_name"])
                check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if master_user_arn is not None:
                self._values["master_user_arn"] = master_user_arn
            if master_user_name is not None:
                self._values["master_user_name"] = master_user_name
            if master_user_password is not None:
                self._values["master_user_password"] = master_user_password

        @builtins.property
        def master_user_arn(self) -> typing.Optional[builtins.str]:
            '''Amazon Resource Name (ARN) for the master user.

            The ARN can point to an IAM user or role. This property is required for Amazon Cognito to work, and it must match the role configured for Cognito. Only specify if ``InternalUserDatabaseEnabled`` is false in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masteruserarn
            '''
            result = self._values.get("master_user_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def master_user_name(self) -> typing.Optional[builtins.str]:
            '''Username for the master user. Only specify if ``InternalUserDatabaseEnabled`` is true in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .

            If you don't want to specify this value directly within the template, you can use a `dynamic reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html>`_ instead.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masterusername
            '''
            result = self._values.get("master_user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def master_user_password(self) -> typing.Optional[builtins.str]:
            '''Password for the master user. Only specify if ``InternalUserDatabaseEnabled`` is true in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .

            If you don't want to specify this value directly within the template, you can use a `dynamic reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html>`_ instead.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masteruserpassword
            '''
            result = self._values.get("master_user_password")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MasterUserOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.NodeToNodeEncryptionOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class NodeToNodeEncryptionOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies options for node-to-node encryption.

            :param enabled: Specifies to enable or disable node-to-node encryption on the domain. Required if you enable fine-grained access control in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                node_to_node_encryption_options_property = opensearchservice.CfnDomain.NodeToNodeEncryptionOptionsProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbea990af8e11f12ced7e27d027040c8ec8f64ffa1f9d71f254282114946ea92)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies to enable or disable node-to-node encryption on the domain.

            Required if you enable fine-grained access control in `AdvancedSecurityOptionsInput <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html#cfn-opensearchservice-domain-nodetonodeencryptionoptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeToNodeEncryptionOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.OffPeakWindowOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "off_peak_window": "offPeakWindow"},
    )
    class OffPeakWindowOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            off_peak_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.OffPeakWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Off-peak window settings for the domain.

            :param enabled: Specifies whether off-peak window settings are enabled for the domain.
            :param off_peak_window: Off-peak window settings for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindowoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                off_peak_window_options_property = opensearchservice.CfnDomain.OffPeakWindowOptionsProperty(
                    enabled=False,
                    off_peak_window=opensearchservice.CfnDomain.OffPeakWindowProperty(
                        window_start_time=opensearchservice.CfnDomain.WindowStartTimeProperty(
                            hours=123,
                            minutes=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__60d60226ff032c6e6c2d237e050aa8d3a58b6a67c4b5e0bdb59300620e1b4ad6)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument off_peak_window", value=off_peak_window, expected_type=type_hints["off_peak_window"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if off_peak_window is not None:
                self._values["off_peak_window"] = off_peak_window

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether off-peak window settings are enabled for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindowoptions.html#cfn-opensearchservice-domain-offpeakwindowoptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def off_peak_window(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.OffPeakWindowProperty"]]:
            '''Off-peak window settings for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindowoptions.html#cfn-opensearchservice-domain-offpeakwindowoptions-offpeakwindow
            '''
            result = self._values.get("off_peak_window")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.OffPeakWindowProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OffPeakWindowOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.OffPeakWindowProperty",
        jsii_struct_bases=[],
        name_mapping={"window_start_time": "windowStartTime"},
    )
    class OffPeakWindowProperty:
        def __init__(
            self,
            *,
            window_start_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.WindowStartTimeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A custom 10-hour, low-traffic window during which OpenSearch Service can perform mandatory configuration changes on the domain.

            These actions can include scheduled service software updates and blue/green Auto-Tune enhancements. OpenSearch Service will schedule these actions during the window that you specify. If you don't specify a window start time, it defaults to 10:00 P.M. local time.

            :param window_start_time: The desired start time for an off-peak maintenance window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                off_peak_window_property = opensearchservice.CfnDomain.OffPeakWindowProperty(
                    window_start_time=opensearchservice.CfnDomain.WindowStartTimeProperty(
                        hours=123,
                        minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30d779e62b9e7bc4d33e575c2c20d7da26b34d1299cff8c0f1810cd484dc86e3)
                check_type(argname="argument window_start_time", value=window_start_time, expected_type=type_hints["window_start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if window_start_time is not None:
                self._values["window_start_time"] = window_start_time

        @builtins.property
        def window_start_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.WindowStartTimeProperty"]]:
            '''The desired start time for an off-peak maintenance window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindow.html#cfn-opensearchservice-domain-offpeakwindow-windowstarttime
            '''
            result = self._values.get("window_start_time")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.WindowStartTimeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OffPeakWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.SAMLOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "idp": "idp",
            "master_backend_role": "masterBackendRole",
            "master_user_name": "masterUserName",
            "roles_key": "rolesKey",
            "session_timeout_minutes": "sessionTimeoutMinutes",
            "subject_key": "subjectKey",
        },
    )
    class SAMLOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            idp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.IdpProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            master_backend_role: typing.Optional[builtins.str] = None,
            master_user_name: typing.Optional[builtins.str] = None,
            roles_key: typing.Optional[builtins.str] = None,
            session_timeout_minutes: typing.Optional[jsii.Number] = None,
            subject_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Container for information about the SAML configuration for OpenSearch Dashboards.

            :param enabled: True to enable SAML authentication for a domain.
            :param idp: The SAML Identity Provider's information.
            :param master_backend_role: The backend role that the SAML master user is mapped to.
            :param master_user_name: The SAML master user name, which is stored in the domain's internal user database.
            :param roles_key: Element of the SAML assertion to use for backend roles. Default is ``roles`` .
            :param session_timeout_minutes: The duration, in minutes, after which a user session becomes inactive. Acceptable values are between 1 and 1440, and the default value is 60.
            :param subject_key: Element of the SAML assertion to use for the user name. Default is ``NameID`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                s_aMLOptions_property = opensearchservice.CfnDomain.SAMLOptionsProperty(
                    enabled=False,
                    idp=opensearchservice.CfnDomain.IdpProperty(
                        entity_id="entityId",
                        metadata_content="metadataContent"
                    ),
                    master_backend_role="masterBackendRole",
                    master_user_name="masterUserName",
                    roles_key="rolesKey",
                    session_timeout_minutes=123,
                    subject_key="subjectKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b5e21e3867bc5223d95d43002facac59aeb4bf08a5eb92c2adf7498d4b99a166)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument idp", value=idp, expected_type=type_hints["idp"])
                check_type(argname="argument master_backend_role", value=master_backend_role, expected_type=type_hints["master_backend_role"])
                check_type(argname="argument master_user_name", value=master_user_name, expected_type=type_hints["master_user_name"])
                check_type(argname="argument roles_key", value=roles_key, expected_type=type_hints["roles_key"])
                check_type(argname="argument session_timeout_minutes", value=session_timeout_minutes, expected_type=type_hints["session_timeout_minutes"])
                check_type(argname="argument subject_key", value=subject_key, expected_type=type_hints["subject_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if idp is not None:
                self._values["idp"] = idp
            if master_backend_role is not None:
                self._values["master_backend_role"] = master_backend_role
            if master_user_name is not None:
                self._values["master_user_name"] = master_user_name
            if roles_key is not None:
                self._values["roles_key"] = roles_key
            if session_timeout_minutes is not None:
                self._values["session_timeout_minutes"] = session_timeout_minutes
            if subject_key is not None:
                self._values["subject_key"] = subject_key

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to enable SAML authentication for a domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def idp(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.IdpProperty"]]:
            '''The SAML Identity Provider's information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-idp
            '''
            result = self._values.get("idp")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.IdpProperty"]], result)

        @builtins.property
        def master_backend_role(self) -> typing.Optional[builtins.str]:
            '''The backend role that the SAML master user is mapped to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-masterbackendrole
            '''
            result = self._values.get("master_backend_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def master_user_name(self) -> typing.Optional[builtins.str]:
            '''The SAML master user name, which is stored in the domain's internal user database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-masterusername
            '''
            result = self._values.get("master_user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def roles_key(self) -> typing.Optional[builtins.str]:
            '''Element of the SAML assertion to use for backend roles.

            Default is ``roles`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-roleskey
            '''
            result = self._values.get("roles_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def session_timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The duration, in minutes, after which a user session becomes inactive.

            Acceptable values are between 1 and 1440, and the default value is 60.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-sessiontimeoutminutes
            '''
            result = self._values.get("session_timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def subject_key(self) -> typing.Optional[builtins.str]:
            '''Element of the SAML assertion to use for the user name.

            Default is ``NameID`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-subjectkey
            '''
            result = self._values.get("subject_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAMLOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.ServiceSoftwareOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "automated_update_date": "automatedUpdateDate",
            "cancellable": "cancellable",
            "current_version": "currentVersion",
            "description": "description",
            "new_version": "newVersion",
            "optional_deployment": "optionalDeployment",
            "update_available": "updateAvailable",
            "update_status": "updateStatus",
        },
    )
    class ServiceSoftwareOptionsProperty:
        def __init__(
            self,
            *,
            automated_update_date: typing.Optional[builtins.str] = None,
            cancellable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            current_version: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            new_version: typing.Optional[builtins.str] = None,
            optional_deployment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            update_available: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            update_status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The current status of the service software for an Amazon OpenSearch Service domain.

            For more information, see `Service software updates in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html>`_ .

            :param automated_update_date: The timestamp, in Epoch time, until which you can manually request a service software update. After this date, we automatically update your service software.
            :param cancellable: True if you're able to cancel your service software version update. False if you can't cancel your service software update.
            :param current_version: The current service software version present on the domain.
            :param description: A description of the service software update status.
            :param new_version: The new service software version, if one is available.
            :param optional_deployment: True if a service software is never automatically updated. False if a service software is automatically updated after the automated update date.
            :param update_available: True if you're able to update your service software version. False if you can't update your service software version.
            :param update_status: The status of your service software update.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                service_software_options_property = opensearchservice.CfnDomain.ServiceSoftwareOptionsProperty(
                    automated_update_date="automatedUpdateDate",
                    cancellable=False,
                    current_version="currentVersion",
                    description="description",
                    new_version="newVersion",
                    optional_deployment=False,
                    update_available=False,
                    update_status="updateStatus"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__17b60fc8205546d1616e28c359a0065b932fe65e39fe26c0c36bf78a39640570)
                check_type(argname="argument automated_update_date", value=automated_update_date, expected_type=type_hints["automated_update_date"])
                check_type(argname="argument cancellable", value=cancellable, expected_type=type_hints["cancellable"])
                check_type(argname="argument current_version", value=current_version, expected_type=type_hints["current_version"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument new_version", value=new_version, expected_type=type_hints["new_version"])
                check_type(argname="argument optional_deployment", value=optional_deployment, expected_type=type_hints["optional_deployment"])
                check_type(argname="argument update_available", value=update_available, expected_type=type_hints["update_available"])
                check_type(argname="argument update_status", value=update_status, expected_type=type_hints["update_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automated_update_date is not None:
                self._values["automated_update_date"] = automated_update_date
            if cancellable is not None:
                self._values["cancellable"] = cancellable
            if current_version is not None:
                self._values["current_version"] = current_version
            if description is not None:
                self._values["description"] = description
            if new_version is not None:
                self._values["new_version"] = new_version
            if optional_deployment is not None:
                self._values["optional_deployment"] = optional_deployment
            if update_available is not None:
                self._values["update_available"] = update_available
            if update_status is not None:
                self._values["update_status"] = update_status

        @builtins.property
        def automated_update_date(self) -> typing.Optional[builtins.str]:
            '''The timestamp, in Epoch time, until which you can manually request a service software update.

            After this date, we automatically update your service software.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-automatedupdatedate
            '''
            result = self._values.get("automated_update_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cancellable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True if you're able to cancel your service software version update.

            False if you can't cancel your service software update.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-cancellable
            '''
            result = self._values.get("cancellable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def current_version(self) -> typing.Optional[builtins.str]:
            '''The current service software version present on the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-currentversion
            '''
            result = self._values.get("current_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the service software update status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def new_version(self) -> typing.Optional[builtins.str]:
            '''The new service software version, if one is available.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-newversion
            '''
            result = self._values.get("new_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def optional_deployment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True if a service software is never automatically updated.

            False if a service software is automatically updated after the automated update date.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-optionaldeployment
            '''
            result = self._values.get("optional_deployment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def update_available(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True if you're able to update your service software version.

            False if you can't update your service software version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-updateavailable
            '''
            result = self._values.get("update_available")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def update_status(self) -> typing.Optional[builtins.str]:
            '''The status of your service software update.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-updatestatus
            '''
            result = self._values.get("update_status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceSoftwareOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.SnapshotOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"automated_snapshot_start_hour": "automatedSnapshotStartHour"},
    )
    class SnapshotOptionsProperty:
        def __init__(
            self,
            *,
            automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''*DEPRECATED* .

            This setting is only relevant to domains running legacy Elasticsearch OSS versions earlier than 5.3. It does not apply to OpenSearch domains.

            The automated snapshot configuration for the OpenSearch Service domain indexes.

            :param automated_snapshot_start_hour: The hour in UTC during which the service takes an automated daily snapshot of the indexes in the OpenSearch Service domain. For example, if you specify 0, OpenSearch Service takes an automated snapshot everyday between midnight and 1 am. You can specify a value between 0 and 23.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                snapshot_options_property = opensearchservice.CfnDomain.SnapshotOptionsProperty(
                    automated_snapshot_start_hour=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36321f8809b3e46d31ad2079d9c9a47da5cdee345f411bb1e57bf166897c2d1c)
                check_type(argname="argument automated_snapshot_start_hour", value=automated_snapshot_start_hour, expected_type=type_hints["automated_snapshot_start_hour"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automated_snapshot_start_hour is not None:
                self._values["automated_snapshot_start_hour"] = automated_snapshot_start_hour

        @builtins.property
        def automated_snapshot_start_hour(self) -> typing.Optional[jsii.Number]:
            '''The hour in UTC during which the service takes an automated daily snapshot of the indexes in the OpenSearch Service domain.

            For example, if you specify 0, OpenSearch Service takes an automated snapshot everyday between midnight and 1 am. You can specify a value between 0 and 23.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html#cfn-opensearchservice-domain-snapshotoptions-automatedsnapshotstarthour
            '''
            result = self._values.get("automated_snapshot_start_hour")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnapshotOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.SoftwareUpdateOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"auto_software_update_enabled": "autoSoftwareUpdateEnabled"},
    )
    class SoftwareUpdateOptionsProperty:
        def __init__(
            self,
            *,
            auto_software_update_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Options for configuring service software updates for a domain.

            :param auto_software_update_enabled: Specifies whether automatic service software updates are enabled for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-softwareupdateoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                software_update_options_property = opensearchservice.CfnDomain.SoftwareUpdateOptionsProperty(
                    auto_software_update_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3f5b07fb34bad0710947f07e46bcb56c9b4dde81217ab11372e2037cc7ecc912)
                check_type(argname="argument auto_software_update_enabled", value=auto_software_update_enabled, expected_type=type_hints["auto_software_update_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_software_update_enabled is not None:
                self._values["auto_software_update_enabled"] = auto_software_update_enabled

        @builtins.property
        def auto_software_update_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether automatic service software updates are enabled for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-softwareupdateoptions.html#cfn-opensearchservice-domain-softwareupdateoptions-autosoftwareupdateenabled
            '''
            result = self._values.get("auto_software_update_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SoftwareUpdateOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.VPCOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VPCOptionsProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The virtual private cloud (VPC) configuration for the OpenSearch Service domain.

            For more information, see `Launching your Amazon OpenSearch Service domains using a VPC <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param security_group_ids: The list of security group IDs that are associated with the VPC endpoints for the domain. If you don't provide a security group ID, OpenSearch Service uses the default security group for the VPC. To learn more, see `Security groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon VPC User Guide* .
            :param subnet_ids: Provide one subnet ID for each Availability Zone that your domain uses. For example, you must specify three subnet IDs for a three-AZ domain. To learn more, see `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon VPC User Guide* . If you specify more than one subnet, you must also configure ``ZoneAwarenessEnabled`` and ``ZoneAwarenessConfig`` within `ClusterConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html>`_ , otherwise you'll see the error "You must specify exactly one subnet" during template creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                v_pCOptions_property = opensearchservice.CfnDomain.VPCOptionsProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b5e509f3eeacdd0fd9d933797c926acbd5e00cdfca76bc715ee89c0ba33d541)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of security group IDs that are associated with the VPC endpoints for the domain.

            If you don't provide a security group ID, OpenSearch Service uses the default security group for the VPC. To learn more, see `Security groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon VPC User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html#cfn-opensearchservice-domain-vpcoptions-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Provide one subnet ID for each Availability Zone that your domain uses.

            For example, you must specify three subnet IDs for a three-AZ domain. To learn more, see `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon VPC User Guide* .

            If you specify more than one subnet, you must also configure ``ZoneAwarenessEnabled`` and ``ZoneAwarenessConfig`` within `ClusterConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html>`_ , otherwise you'll see the error "You must specify exactly one subnet" during template creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html#cfn-opensearchservice-domain-vpcoptions-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.WindowStartTimeProperty",
        jsii_struct_bases=[],
        name_mapping={"hours": "hours", "minutes": "minutes"},
    )
    class WindowStartTimeProperty:
        def __init__(self, *, hours: jsii.Number, minutes: jsii.Number) -> None:
            '''A custom start time for the off-peak window, in Coordinated Universal Time (UTC).

            The window length will always be 10 hours, so you can't specify an end time. For example, if you specify 11:00 P.M. UTC as a start time, the end time will automatically be set to 9:00 A.M.

            :param hours: The start hour of the window in Coordinated Universal Time (UTC), using 24-hour time. For example, 17 refers to 5:00 P.M. UTC. The minimum value is 0 and the maximum value is 23.
            :param minutes: The start minute of the window, in UTC. The minimum value is 0 and the maximum value is 59.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-windowstarttime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                window_start_time_property = opensearchservice.CfnDomain.WindowStartTimeProperty(
                    hours=123,
                    minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6090d0f7ef0a5ff38223c37e3fded0a822e4e3052cd46ba0b2430b408bd5f698)
                check_type(argname="argument hours", value=hours, expected_type=type_hints["hours"])
                check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hours": hours,
                "minutes": minutes,
            }

        @builtins.property
        def hours(self) -> jsii.Number:
            '''The start hour of the window in Coordinated Universal Time (UTC), using 24-hour time.

            For example, 17 refers to 5:00 P.M. UTC. The minimum value is 0 and the maximum value is 23.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-windowstarttime.html#cfn-opensearchservice-domain-windowstarttime-hours
            '''
            result = self._values.get("hours")
            assert result is not None, "Required property 'hours' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def minutes(self) -> jsii.Number:
            '''The start minute of the window, in UTC.

            The minimum value is 0 and the maximum value is 59.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-windowstarttime.html#cfn-opensearchservice-domain-windowstarttime-minutes
            '''
            result = self._values.get("minutes")
            assert result is not None, "Required property 'minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WindowStartTimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomain.ZoneAwarenessConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"availability_zone_count": "availabilityZoneCount"},
    )
    class ZoneAwarenessConfigProperty:
        def __init__(
            self,
            *,
            availability_zone_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies zone awareness configuration options.

            Only use if ``ZoneAwarenessEnabled`` is ``true`` .

            :param availability_zone_count: If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use. Valid values are ``2`` and ``3`` . Default is 2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchservice as opensearchservice
                
                zone_awareness_config_property = opensearchservice.CfnDomain.ZoneAwarenessConfigProperty(
                    availability_zone_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__256b4aabbc2391aa4f2b7e2d1c28804fdc91f3e9c7c213de20cc38a33dc255b2)
                check_type(argname="argument availability_zone_count", value=availability_zone_count, expected_type=type_hints["availability_zone_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone_count is not None:
                self._values["availability_zone_count"] = availability_zone_count

        @builtins.property
        def availability_zone_count(self) -> typing.Optional[jsii.Number]:
            '''If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use.

            Valid values are ``2`` and ``3`` . Default is 2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html#cfn-opensearchservice-domain-zoneawarenessconfig-availabilityzonecount
            '''
            result = self._values.get("availability_zone_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZoneAwarenessConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_policies": "accessPolicies",
        "advanced_options": "advancedOptions",
        "advanced_security_options": "advancedSecurityOptions",
        "cluster_config": "clusterConfig",
        "cognito_options": "cognitoOptions",
        "domain_arn": "domainArn",
        "domain_endpoint_options": "domainEndpointOptions",
        "domain_name": "domainName",
        "ebs_options": "ebsOptions",
        "encryption_at_rest_options": "encryptionAtRestOptions",
        "engine_version": "engineVersion",
        "ip_address_type": "ipAddressType",
        "log_publishing_options": "logPublishingOptions",
        "node_to_node_encryption_options": "nodeToNodeEncryptionOptions",
        "off_peak_window_options": "offPeakWindowOptions",
        "snapshot_options": "snapshotOptions",
        "software_update_options": "softwareUpdateOptions",
        "tags": "tags",
        "vpc_options": "vpcOptions",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        access_policies: typing.Any = None,
        advanced_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        advanced_security_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.AdvancedSecurityOptionsInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        cluster_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ClusterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        cognito_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.CognitoOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        domain_arn: typing.Optional[builtins.str] = None,
        domain_endpoint_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.DomainEndpointOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        ebs_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EBSOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        encryption_at_rest_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EncryptionAtRestOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.LogPublishingOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        node_to_node_encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.NodeToNodeEncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        off_peak_window_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.OffPeakWindowOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        snapshot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SnapshotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        software_update_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SoftwareUpdateOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.VPCOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param access_policies: An AWS Identity and Access Management ( IAM ) policy document that specifies who can access the OpenSearch Service domain and their permissions. For more information, see `Configuring access policies <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-creating>`_ in the *Amazon OpenSearch Service Developer Guide* .
        :param advanced_options: Additional options to specify for the OpenSearch Service domain. For more information, see `AdvancedOptions <https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateDomain.html#API_CreateDomain_RequestBody>`_ in the OpenSearch Service API reference.
        :param advanced_security_options: Specifies options for fine-grained access control and SAML authentication. If you specify advanced security options, you must also enable node-to-node encryption ( `NodeToNodeEncryptionOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html>`_ ) and encryption at rest ( `EncryptionAtRestOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html>`_ ). You must also enable ``EnforceHTTPS`` within `DomainEndpointOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html>`_ , which requires HTTPS for all traffic to the domain.
        :param cluster_config: Container for the cluster configuration of a domain.
        :param cognito_options: Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.
        :param domain_arn: 
        :param domain_endpoint_options: Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.
        :param domain_name: A name for the OpenSearch Service domain. The name must have a minimum length of 3 and a maximum length of 28. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the domain name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . Required when creating a new domain. .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param ebs_options: The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain. For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .
        :param encryption_at_rest_options: Whether the domain should encrypt data at rest, and if so, the AWS KMS key to use. See `Encryption of data at rest for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html>`_ . If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.
        :param engine_version: The version of OpenSearch to use. The value must be in the format ``OpenSearch_X.Y`` or ``Elasticsearch_X.Y`` . If not specified, the latest version of OpenSearch is used. For information about the versions that OpenSearch Service supports, see `Supported versions of OpenSearch and Elasticsearch <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#choosing-version>`_ in the *Amazon OpenSearch Service Developer Guide* . If you set the `EnableVersionUpgrade <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-upgradeopensearchdomain>`_ update policy to ``true`` , you can update ``EngineVersion`` without interruption. When ``EnableVersionUpgrade`` is set to ``false`` , or is not specified, updating ``EngineVersion`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param ip_address_type: Choose either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.
        :param log_publishing_options: An object with one or more of the following keys: ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , ``AUDIT_LOGS`` , depending on the types of logs you want to publish. Each key needs a valid ``LogPublishingOption`` value. For the full syntax, see the `examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain--examples>`_ .
        :param node_to_node_encryption_options: Specifies whether node-to-node encryption is enabled. See `Node-to-node encryption for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html>`_ .
        :param off_peak_window_options: Options for a domain's off-peak window, during which OpenSearch Service can perform mandatory configuration changes on the domain.
        :param snapshot_options: *DEPRECATED* . The automated snapshot configuration for the OpenSearch Service domain indexes.
        :param software_update_options: Service software update options for the domain.
        :param tags: An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Service domain.
        :param vpc_options: The virtual private cloud (VPC) configuration for the OpenSearch Service domain. For more information, see `Launching your Amazon OpenSearch Service domains within a VPC <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html>`_ in the *Amazon OpenSearch Service Developer Guide* . If you remove this entity altogether, along with its associated properties, it causes a replacement. You might encounter this scenario if you're updating your security configuration from a VPC to a public endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearchservice as opensearchservice
            
            # access_policies: Any
            
            cfn_domain_props = opensearchservice.CfnDomainProps(
                access_policies=access_policies,
                advanced_options={
                    "advanced_options_key": "advancedOptions"
                },
                advanced_security_options=opensearchservice.CfnDomain.AdvancedSecurityOptionsInputProperty(
                    anonymous_auth_disable_date="anonymousAuthDisableDate",
                    anonymous_auth_enabled=False,
                    enabled=False,
                    internal_user_database_enabled=False,
                    master_user_options=opensearchservice.CfnDomain.MasterUserOptionsProperty(
                        master_user_arn="masterUserArn",
                        master_user_name="masterUserName",
                        master_user_password="masterUserPassword"
                    ),
                    saml_options=opensearchservice.CfnDomain.SAMLOptionsProperty(
                        enabled=False,
                        idp=opensearchservice.CfnDomain.IdpProperty(
                            entity_id="entityId",
                            metadata_content="metadataContent"
                        ),
                        master_backend_role="masterBackendRole",
                        master_user_name="masterUserName",
                        roles_key="rolesKey",
                        session_timeout_minutes=123,
                        subject_key="subjectKey"
                    )
                ),
                cluster_config=opensearchservice.CfnDomain.ClusterConfigProperty(
                    cold_storage_options=opensearchservice.CfnDomain.ColdStorageOptionsProperty(
                        enabled=False
                    ),
                    dedicated_master_count=123,
                    dedicated_master_enabled=False,
                    dedicated_master_type="dedicatedMasterType",
                    instance_count=123,
                    instance_type="instanceType",
                    multi_az_with_standby_enabled=False,
                    warm_count=123,
                    warm_enabled=False,
                    warm_type="warmType",
                    zone_awareness_config=opensearchservice.CfnDomain.ZoneAwarenessConfigProperty(
                        availability_zone_count=123
                    ),
                    zone_awareness_enabled=False
                ),
                cognito_options=opensearchservice.CfnDomain.CognitoOptionsProperty(
                    enabled=False,
                    identity_pool_id="identityPoolId",
                    role_arn="roleArn",
                    user_pool_id="userPoolId"
                ),
                domain_arn="domainArn",
                domain_endpoint_options=opensearchservice.CfnDomain.DomainEndpointOptionsProperty(
                    custom_endpoint="customEndpoint",
                    custom_endpoint_certificate_arn="customEndpointCertificateArn",
                    custom_endpoint_enabled=False,
                    enforce_https=False,
                    tls_security_policy="tlsSecurityPolicy"
                ),
                domain_name="domainName",
                ebs_options=opensearchservice.CfnDomain.EBSOptionsProperty(
                    ebs_enabled=False,
                    iops=123,
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                ),
                encryption_at_rest_options=opensearchservice.CfnDomain.EncryptionAtRestOptionsProperty(
                    enabled=False,
                    kms_key_id="kmsKeyId"
                ),
                engine_version="engineVersion",
                ip_address_type="ipAddressType",
                log_publishing_options={
                    "log_publishing_options_key": opensearchservice.CfnDomain.LogPublishingOptionProperty(
                        cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn",
                        enabled=False
                    )
                },
                node_to_node_encryption_options=opensearchservice.CfnDomain.NodeToNodeEncryptionOptionsProperty(
                    enabled=False
                ),
                off_peak_window_options=opensearchservice.CfnDomain.OffPeakWindowOptionsProperty(
                    enabled=False,
                    off_peak_window=opensearchservice.CfnDomain.OffPeakWindowProperty(
                        window_start_time=opensearchservice.CfnDomain.WindowStartTimeProperty(
                            hours=123,
                            minutes=123
                        )
                    )
                ),
                snapshot_options=opensearchservice.CfnDomain.SnapshotOptionsProperty(
                    automated_snapshot_start_hour=123
                ),
                software_update_options=opensearchservice.CfnDomain.SoftwareUpdateOptionsProperty(
                    auto_software_update_enabled=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_options=opensearchservice.CfnDomain.VPCOptionsProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a3bbf8db74762f8d49d2ee572e0b31eef8650964dd0e8a168a5fe2d67607c52)
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
            check_type(argname="argument advanced_options", value=advanced_options, expected_type=type_hints["advanced_options"])
            check_type(argname="argument advanced_security_options", value=advanced_security_options, expected_type=type_hints["advanced_security_options"])
            check_type(argname="argument cluster_config", value=cluster_config, expected_type=type_hints["cluster_config"])
            check_type(argname="argument cognito_options", value=cognito_options, expected_type=type_hints["cognito_options"])
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument domain_endpoint_options", value=domain_endpoint_options, expected_type=type_hints["domain_endpoint_options"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument ebs_options", value=ebs_options, expected_type=type_hints["ebs_options"])
            check_type(argname="argument encryption_at_rest_options", value=encryption_at_rest_options, expected_type=type_hints["encryption_at_rest_options"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument log_publishing_options", value=log_publishing_options, expected_type=type_hints["log_publishing_options"])
            check_type(argname="argument node_to_node_encryption_options", value=node_to_node_encryption_options, expected_type=type_hints["node_to_node_encryption_options"])
            check_type(argname="argument off_peak_window_options", value=off_peak_window_options, expected_type=type_hints["off_peak_window_options"])
            check_type(argname="argument snapshot_options", value=snapshot_options, expected_type=type_hints["snapshot_options"])
            check_type(argname="argument software_update_options", value=software_update_options, expected_type=type_hints["software_update_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_options", value=vpc_options, expected_type=type_hints["vpc_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_policies is not None:
            self._values["access_policies"] = access_policies
        if advanced_options is not None:
            self._values["advanced_options"] = advanced_options
        if advanced_security_options is not None:
            self._values["advanced_security_options"] = advanced_security_options
        if cluster_config is not None:
            self._values["cluster_config"] = cluster_config
        if cognito_options is not None:
            self._values["cognito_options"] = cognito_options
        if domain_arn is not None:
            self._values["domain_arn"] = domain_arn
        if domain_endpoint_options is not None:
            self._values["domain_endpoint_options"] = domain_endpoint_options
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if ebs_options is not None:
            self._values["ebs_options"] = ebs_options
        if encryption_at_rest_options is not None:
            self._values["encryption_at_rest_options"] = encryption_at_rest_options
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if log_publishing_options is not None:
            self._values["log_publishing_options"] = log_publishing_options
        if node_to_node_encryption_options is not None:
            self._values["node_to_node_encryption_options"] = node_to_node_encryption_options
        if off_peak_window_options is not None:
            self._values["off_peak_window_options"] = off_peak_window_options
        if snapshot_options is not None:
            self._values["snapshot_options"] = snapshot_options
        if software_update_options is not None:
            self._values["software_update_options"] = software_update_options
        if tags is not None:
            self._values["tags"] = tags
        if vpc_options is not None:
            self._values["vpc_options"] = vpc_options

    @builtins.property
    def access_policies(self) -> typing.Any:
        '''An AWS Identity and Access Management ( IAM ) policy document that specifies who can access the OpenSearch Service domain and their permissions.

        For more information, see `Configuring access policies <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-creating>`_ in the *Amazon OpenSearch Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-accesspolicies
        '''
        result = self._values.get("access_policies")
        return typing.cast(typing.Any, result)

    @builtins.property
    def advanced_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional options to specify for the OpenSearch Service domain.

        For more information, see `AdvancedOptions <https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateDomain.html#API_CreateDomain_RequestBody>`_ in the OpenSearch Service API reference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-advancedoptions
        '''
        result = self._values.get("advanced_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def advanced_security_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.AdvancedSecurityOptionsInputProperty]]:
        '''Specifies options for fine-grained access control and SAML authentication.

        If you specify advanced security options, you must also enable node-to-node encryption ( `NodeToNodeEncryptionOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html>`_ ) and encryption at rest ( `EncryptionAtRestOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html>`_ ). You must also enable ``EnforceHTTPS`` within `DomainEndpointOptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html>`_ , which requires HTTPS for all traffic to the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-advancedsecurityoptions
        '''
        result = self._values.get("advanced_security_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.AdvancedSecurityOptionsInputProperty]], result)

    @builtins.property
    def cluster_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.ClusterConfigProperty]]:
        '''Container for the cluster configuration of a domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-clusterconfig
        '''
        result = self._values.get("cluster_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.ClusterConfigProperty]], result)

    @builtins.property
    def cognito_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.CognitoOptionsProperty]]:
        '''Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-cognitooptions
        '''
        result = self._values.get("cognito_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.CognitoOptionsProperty]], result)

    @builtins.property
    def domain_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainarn
        '''
        result = self._values.get("domain_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_endpoint_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.DomainEndpointOptionsProperty]]:
        '''Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainendpointoptions
        '''
        result = self._values.get("domain_endpoint_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.DomainEndpointOptionsProperty]], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''A name for the OpenSearch Service domain.

        The name must have a minimum length of 3 and a maximum length of 28. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the domain name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        Required when creating a new domain.
        .. epigraph::

           If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainname
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EBSOptionsProperty]]:
        '''The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain.

        For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-ebsoptions
        '''
        result = self._values.get("ebs_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EBSOptionsProperty]], result)

    @builtins.property
    def encryption_at_rest_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EncryptionAtRestOptionsProperty]]:
        '''Whether the domain should encrypt data at rest, and if so, the AWS KMS key to use.

        See `Encryption of data at rest for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html>`_ .

        If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-encryptionatrestoptions
        '''
        result = self._values.get("encryption_at_rest_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EncryptionAtRestOptionsProperty]], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version of OpenSearch to use.

        The value must be in the format ``OpenSearch_X.Y`` or ``Elasticsearch_X.Y`` . If not specified, the latest version of OpenSearch is used. For information about the versions that OpenSearch Service supports, see `Supported versions of OpenSearch and Elasticsearch <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#choosing-version>`_ in the *Amazon OpenSearch Service Developer Guide* .

        If you set the `EnableVersionUpgrade <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-upgradeopensearchdomain>`_ update policy to ``true`` , you can update ``EngineVersion`` without interruption. When ``EnableVersionUpgrade`` is set to ``false`` , or is not specified, updating ``EngineVersion`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''Choose either dual stack or IPv4 as your IP address type.

        Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-ipaddresstype
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_publishing_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDomain.LogPublishingOptionProperty]]]]:
        '''An object with one or more of the following keys: ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , ``AUDIT_LOGS`` , depending on the types of logs you want to publish.

        Each key needs a valid ``LogPublishingOption`` value. For the full syntax, see the `examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain--examples>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-logpublishingoptions
        '''
        result = self._values.get("log_publishing_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDomain.LogPublishingOptionProperty]]]], result)

    @builtins.property
    def node_to_node_encryption_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.NodeToNodeEncryptionOptionsProperty]]:
        '''Specifies whether node-to-node encryption is enabled.

        See `Node-to-node encryption for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-nodetonodeencryptionoptions
        '''
        result = self._values.get("node_to_node_encryption_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.NodeToNodeEncryptionOptionsProperty]], result)

    @builtins.property
    def off_peak_window_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.OffPeakWindowOptionsProperty]]:
        '''Options for a domain's off-peak window, during which OpenSearch Service can perform mandatory configuration changes on the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-offpeakwindowoptions
        '''
        result = self._values.get("off_peak_window_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.OffPeakWindowOptionsProperty]], result)

    @builtins.property
    def snapshot_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SnapshotOptionsProperty]]:
        '''*DEPRECATED* .

        The automated snapshot configuration for the OpenSearch Service domain indexes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-snapshotoptions
        '''
        result = self._values.get("snapshot_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SnapshotOptionsProperty]], result)

    @builtins.property
    def software_update_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SoftwareUpdateOptionsProperty]]:
        '''Service software update options for the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-softwareupdateoptions
        '''
        result = self._values.get("software_update_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SoftwareUpdateOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Service domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.VPCOptionsProperty]]:
        '''The virtual private cloud (VPC) configuration for the OpenSearch Service domain.

        For more information, see `Launching your Amazon OpenSearch Service domains within a VPC <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html>`_ in the *Amazon OpenSearch Service Developer Guide* .

        If you remove this entity altogether, along with its associated properties, it causes a replacement. You might encounter this scenario if you're updating your security configuration from a VPC to a public endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-vpcoptions
        '''
        result = self._values.get("vpc_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.VPCOptionsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.CognitoOptions",
    jsii_struct_bases=[],
    name_mapping={
        "identity_pool_id": "identityPoolId",
        "role": "role",
        "user_pool_id": "userPoolId",
    },
)
class CognitoOptions:
    def __init__(
        self,
        *,
        identity_pool_id: builtins.str,
        role: _IRole_235f5d8e,
        user_pool_id: builtins.str,
    ) -> None:
        '''Configures Amazon OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.

        :param identity_pool_id: The Amazon Cognito identity pool ID that you want Amazon OpenSearch Service to use for OpenSearch Dashboards authentication.
        :param role: A role that allows Amazon OpenSearch Service to configure your user pool and identity pool. It must have the ``AmazonESCognitoAccess`` policy attached to it.
        :param user_pool_id: The Amazon Cognito user pool ID that you want Amazon OpenSearch Service to use for OpenSearch Dashboards authentication.

        :see: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html
        :exampleMetadata: fixture=migrate-opensearch infused

        Example::

            opensearch.Domain(self, "Domain",
                cognito_dashboards_auth=opensearch.CognitoOptions(
                    identity_pool_id="test-identity-pool-id",
                    user_pool_id="test-user-pool-id",
                    role=role
                ),
                version=open_search_version
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ac57cf9250cdb4adb2c04b922ca15a9a5d18b8e118cff3f08ab7d1171f1fcd9)
            check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_pool_id": identity_pool_id,
            "role": role,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def identity_pool_id(self) -> builtins.str:
        '''The Amazon Cognito identity pool ID that you want Amazon OpenSearch Service to use for OpenSearch Dashboards authentication.'''
        result = self._values.get("identity_pool_id")
        assert result is not None, "Required property 'identity_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> _IRole_235f5d8e:
        '''A role that allows Amazon OpenSearch Service to configure your user pool and identity pool.

        It must have the ``AmazonESCognitoAccess`` policy attached to it.

        :see: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html#cognito-auth-prereq
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The Amazon Cognito user pool ID that you want Amazon OpenSearch Service to use for OpenSearch Dashboards authentication.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.CustomEndpointOptions",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "certificate": "certificate",
        "hosted_zone": "hostedZone",
    },
)
class CustomEndpointOptions:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        certificate: typing.Optional[_ICertificate_c194c70b] = None,
        hosted_zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> None:
        '''Configures a custom domain endpoint for the Amazon OpenSearch Service domain.

        :param domain_name: The custom domain name to assign.
        :param certificate: The certificate to use. Default: - create a new one
        :param hosted_zone: The hosted zone in Route53 to create the CNAME record in. Default: - do not create a CNAME

        :exampleMetadata: infused

        Example::

            Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_0,
                custom_endpoint=CustomEndpointOptions(
                    domain_name="search.example.com"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bfcfb0c951977f30c9119dd53a7307c78b4a3185828104fe4e4d17628ef7d24)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if hosted_zone is not None:
            self._values["hosted_zone"] = hosted_zone

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The custom domain name to assign.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[_ICertificate_c194c70b]:
        '''The certificate to use.

        :default: - create a new one
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[_ICertificate_c194c70b], result)

    @builtins.property
    def hosted_zone(self) -> typing.Optional[_IHostedZone_9a6907ad]:
        '''The hosted zone in Route53 to create the CNAME record in.

        :default: - do not create a CNAME
        '''
        result = self._values.get("hosted_zone")
        return typing.cast(typing.Optional[_IHostedZone_9a6907ad], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomEndpointOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.DomainAttributes",
    jsii_struct_bases=[],
    name_mapping={"domain_arn": "domainArn", "domain_endpoint": "domainEndpoint"},
)
class DomainAttributes:
    def __init__(
        self,
        *,
        domain_arn: builtins.str,
        domain_endpoint: builtins.str,
    ) -> None:
        '''Reference to an Amazon OpenSearch Service domain.

        :param domain_arn: The ARN of the Amazon OpenSearch Service domain.
        :param domain_endpoint: The domain endpoint of the Amazon OpenSearch Service domain.

        :exampleMetadata: infused

        Example::

            domain_arn = Fn.import_value("another-cf-stack-export-domain-arn")
            domain_endpoint = Fn.import_value("another-cf-stack-export-domain-endpoint")
            domain = Domain.from_domain_attributes(self, "ImportedDomain",
                domain_arn=domain_arn,
                domain_endpoint=domain_endpoint
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b64144592f37187baf13886dda52519ca86792e6e902692955529605957265b3)
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument domain_endpoint", value=domain_endpoint, expected_type=type_hints["domain_endpoint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_arn": domain_arn,
            "domain_endpoint": domain_endpoint,
        }

    @builtins.property
    def domain_arn(self) -> builtins.str:
        '''The ARN of the Amazon OpenSearch Service domain.'''
        result = self._values.get("domain_arn")
        assert result is not None, "Required property 'domain_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_endpoint(self) -> builtins.str:
        '''The domain endpoint of the Amazon OpenSearch Service domain.'''
        result = self._values.get("domain_endpoint")
        assert result is not None, "Required property 'domain_endpoint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.DomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "version": "version",
        "access_policies": "accessPolicies",
        "advanced_options": "advancedOptions",
        "automated_snapshot_start_hour": "automatedSnapshotStartHour",
        "capacity": "capacity",
        "cognito_dashboards_auth": "cognitoDashboardsAuth",
        "cold_storage_enabled": "coldStorageEnabled",
        "custom_endpoint": "customEndpoint",
        "domain_name": "domainName",
        "ebs": "ebs",
        "enable_auto_software_update": "enableAutoSoftwareUpdate",
        "enable_version_upgrade": "enableVersionUpgrade",
        "encryption_at_rest": "encryptionAtRest",
        "enforce_https": "enforceHttps",
        "fine_grained_access_control": "fineGrainedAccessControl",
        "ip_address_type": "ipAddressType",
        "logging": "logging",
        "node_to_node_encryption": "nodeToNodeEncryption",
        "off_peak_window_enabled": "offPeakWindowEnabled",
        "off_peak_window_start": "offPeakWindowStart",
        "removal_policy": "removalPolicy",
        "security_groups": "securityGroups",
        "suppress_logs_resource_policy": "suppressLogsResourcePolicy",
        "tls_security_policy": "tlsSecurityPolicy",
        "use_unsigned_basic_auth": "useUnsignedBasicAuth",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "zone_awareness": "zoneAwareness",
    },
)
class DomainProps:
    def __init__(
        self,
        *,
        version: "EngineVersion",
        access_policies: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
        capacity: typing.Optional[typing.Union[CapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        cognito_dashboards_auth: typing.Optional[typing.Union[CognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cold_storage_enabled: typing.Optional[builtins.bool] = None,
        custom_endpoint: typing.Optional[typing.Union[CustomEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        ebs: typing.Optional[typing.Union["EbsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_auto_software_update: typing.Optional[builtins.bool] = None,
        enable_version_upgrade: typing.Optional[builtins.bool] = None,
        encryption_at_rest: typing.Optional[typing.Union["EncryptionAtRestOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        enforce_https: typing.Optional[builtins.bool] = None,
        fine_grained_access_control: typing.Optional[typing.Union[AdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        ip_address_type: typing.Optional["IpAddressType"] = None,
        logging: typing.Optional[typing.Union["LoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        node_to_node_encryption: typing.Optional[builtins.bool] = None,
        off_peak_window_enabled: typing.Optional[builtins.bool] = None,
        off_peak_window_start: typing.Optional[typing.Union["WindowStartTime", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        suppress_logs_resource_policy: typing.Optional[builtins.bool] = None,
        tls_security_policy: typing.Optional["TLSSecurityPolicy"] = None,
        use_unsigned_basic_auth: typing.Optional[builtins.bool] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
        zone_awareness: typing.Optional[typing.Union["ZoneAwarenessConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for an Amazon OpenSearch Service domain.

        :param version: The Elasticsearch/OpenSearch version that your domain will leverage.
        :param access_policies: Domain access policies. Default: - No access policies.
        :param advanced_options: Additional options to specify for the Amazon OpenSearch Service domain. Default: - no advanced options are specified
        :param automated_snapshot_start_hour: The hour in UTC during which the service takes an automated daily snapshot of the indices in the Amazon OpenSearch Service domain. Only applies for Elasticsearch versions below 5.3. Default: - Hourly automated snapshots not used
        :param capacity: The cluster capacity configuration for the Amazon OpenSearch Service domain. Default: - 1 r5.large.search data node; no dedicated master nodes.
        :param cognito_dashboards_auth: Configures Amazon OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards. Default: - Cognito not used for authentication to OpenSearch Dashboards.
        :param cold_storage_enabled: Whether to enable or disable cold storage on the domain. You must enable UltraWarm storage to enable cold storage. Default: - undefined
        :param custom_endpoint: To configure a custom domain configure these options. If you specify a Route53 hosted zone it will create a CNAME record and use DNS validation for the certificate Default: - no custom domain endpoint will be configured
        :param domain_name: Enforces a particular physical domain name. Default: - A name will be auto-generated.
        :param ebs: The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the Amazon OpenSearch Service domain. Default: - 10 GiB General Purpose (SSD) volumes per node.
        :param enable_auto_software_update: Specifies whether automatic service software updates are enabled for the domain. Default: - false
        :param enable_version_upgrade: To upgrade an Amazon OpenSearch Service domain to a new version, rather than replacing the entire domain resource, use the EnableVersionUpgrade update policy. Default: - false
        :param encryption_at_rest: Encryption at rest options for the cluster. Default: - No encryption at rest
        :param enforce_https: True to require that all traffic to the domain arrive over HTTPS. Default: - false
        :param fine_grained_access_control: Specifies options for fine-grained access control. Requires Elasticsearch version 6.7 or later or OpenSearch version 1.0 or later. Enabling fine-grained access control also requires encryption of data at rest and node-to-node encryption, along with enforced HTTPS. Default: - fine-grained access control is disabled
        :param ip_address_type: Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later. Default: - IpAddressType.IPV4
        :param logging: Configuration log publishing configuration options. Default: - No logs are published
        :param node_to_node_encryption: Specify true to enable node to node encryption. Requires Elasticsearch version 6.0 or later or OpenSearch version 1.0 or later. Default: - Node to node encryption is not enabled.
        :param off_peak_window_enabled: Options for enabling a domain's off-peak window, during which OpenSearch Service can perform mandatory configuration changes on the domain. Off-peak windows were introduced on February 16, 2023. All domains created before this date have the off-peak window disabled by default. You must manually enable and configure the off-peak window for these domains. All domains created after this date will have the off-peak window enabled by default. You can't disable the off-peak window for a domain after it's enabled. Default: - Disabled for domains created before February 16, 2023. Enabled for domains created after. Enabled if ``offPeakWindowStart`` is set.
        :param off_peak_window_start: Start time for the off-peak window, in Coordinated Universal Time (UTC). The window length will always be 10 hours, so you can't specify an end time. For example, if you specify 11:00 P.M. UTC as a start time, the end time will automatically be set to 9:00 A.M. Default: - 10:00 P.M. local time
        :param removal_policy: Policy to apply when the domain is removed from the stack. Default: RemovalPolicy.RETAIN
        :param security_groups: The list of security groups that are associated with the VPC endpoints for the domain. Only used if ``vpc`` is specified. Default: - One new security group is created.
        :param suppress_logs_resource_policy: Specify whether to create a CloudWatch Logs resource policy or not. When logging is enabled for the domain, a CloudWatch Logs resource policy is created by default. However, CloudWatch Logs supports only 10 resource policies per region. If you enable logging for several domains, it may hit the quota and cause an error. By setting this property to true, creating a resource policy is suppressed, allowing you to avoid this problem. If you set this option to true, you must create a resource policy before deployment. Default: - false
        :param tls_security_policy: The minimum TLS version required for traffic to the domain. Default: - TLSSecurityPolicy.TLS_1_0
        :param use_unsigned_basic_auth: Configures the domain so that unsigned basic auth is enabled. If no master user is provided a default master user with username ``admin`` and a dynamically generated password stored in KMS is created. The password can be retrieved by getting ``masterUserPassword`` from the domain instance. Setting this to true will also add an access policy that allows unsigned access, enable node to node encryption, encryption at rest. If conflicting settings are encountered (like disabling encryption at rest) enabling this setting will cause a failure. Default: - false
        :param vpc: Place the domain inside this VPC. Default: - Domain is not placed in a VPC.
        :param vpc_subnets: The specific vpc subnets the domain will be placed in. You must provide one subnet for each Availability Zone that your domain uses. For example, you must specify three subnet IDs for a three Availability Zone domain. Only used if ``vpc`` is specified. Default: - All private subnets.
        :param zone_awareness: The cluster zone awareness configuration for the Amazon OpenSearch Service domain. Default: - no zone awareness (1 AZ)

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_0,
                ebs=EbsOptions(
                    volume_size=100,
                    volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
                ),
                node_to_node_encryption=True,
                encryption_at_rest=EncryptionAtRestOptions(
                    enabled=True
                )
            )
        '''
        if isinstance(capacity, dict):
            capacity = CapacityConfig(**capacity)
        if isinstance(cognito_dashboards_auth, dict):
            cognito_dashboards_auth = CognitoOptions(**cognito_dashboards_auth)
        if isinstance(custom_endpoint, dict):
            custom_endpoint = CustomEndpointOptions(**custom_endpoint)
        if isinstance(ebs, dict):
            ebs = EbsOptions(**ebs)
        if isinstance(encryption_at_rest, dict):
            encryption_at_rest = EncryptionAtRestOptions(**encryption_at_rest)
        if isinstance(fine_grained_access_control, dict):
            fine_grained_access_control = AdvancedSecurityOptions(**fine_grained_access_control)
        if isinstance(logging, dict):
            logging = LoggingOptions(**logging)
        if isinstance(off_peak_window_start, dict):
            off_peak_window_start = WindowStartTime(**off_peak_window_start)
        if isinstance(zone_awareness, dict):
            zone_awareness = ZoneAwarenessConfig(**zone_awareness)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0435b5d94950ff07269642dd229e13535b70e6b92e19fbea5906bff08927fa74)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
            check_type(argname="argument advanced_options", value=advanced_options, expected_type=type_hints["advanced_options"])
            check_type(argname="argument automated_snapshot_start_hour", value=automated_snapshot_start_hour, expected_type=type_hints["automated_snapshot_start_hour"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument cognito_dashboards_auth", value=cognito_dashboards_auth, expected_type=type_hints["cognito_dashboards_auth"])
            check_type(argname="argument cold_storage_enabled", value=cold_storage_enabled, expected_type=type_hints["cold_storage_enabled"])
            check_type(argname="argument custom_endpoint", value=custom_endpoint, expected_type=type_hints["custom_endpoint"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
            check_type(argname="argument enable_auto_software_update", value=enable_auto_software_update, expected_type=type_hints["enable_auto_software_update"])
            check_type(argname="argument enable_version_upgrade", value=enable_version_upgrade, expected_type=type_hints["enable_version_upgrade"])
            check_type(argname="argument encryption_at_rest", value=encryption_at_rest, expected_type=type_hints["encryption_at_rest"])
            check_type(argname="argument enforce_https", value=enforce_https, expected_type=type_hints["enforce_https"])
            check_type(argname="argument fine_grained_access_control", value=fine_grained_access_control, expected_type=type_hints["fine_grained_access_control"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument node_to_node_encryption", value=node_to_node_encryption, expected_type=type_hints["node_to_node_encryption"])
            check_type(argname="argument off_peak_window_enabled", value=off_peak_window_enabled, expected_type=type_hints["off_peak_window_enabled"])
            check_type(argname="argument off_peak_window_start", value=off_peak_window_start, expected_type=type_hints["off_peak_window_start"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument suppress_logs_resource_policy", value=suppress_logs_resource_policy, expected_type=type_hints["suppress_logs_resource_policy"])
            check_type(argname="argument tls_security_policy", value=tls_security_policy, expected_type=type_hints["tls_security_policy"])
            check_type(argname="argument use_unsigned_basic_auth", value=use_unsigned_basic_auth, expected_type=type_hints["use_unsigned_basic_auth"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument zone_awareness", value=zone_awareness, expected_type=type_hints["zone_awareness"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
        }
        if access_policies is not None:
            self._values["access_policies"] = access_policies
        if advanced_options is not None:
            self._values["advanced_options"] = advanced_options
        if automated_snapshot_start_hour is not None:
            self._values["automated_snapshot_start_hour"] = automated_snapshot_start_hour
        if capacity is not None:
            self._values["capacity"] = capacity
        if cognito_dashboards_auth is not None:
            self._values["cognito_dashboards_auth"] = cognito_dashboards_auth
        if cold_storage_enabled is not None:
            self._values["cold_storage_enabled"] = cold_storage_enabled
        if custom_endpoint is not None:
            self._values["custom_endpoint"] = custom_endpoint
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if ebs is not None:
            self._values["ebs"] = ebs
        if enable_auto_software_update is not None:
            self._values["enable_auto_software_update"] = enable_auto_software_update
        if enable_version_upgrade is not None:
            self._values["enable_version_upgrade"] = enable_version_upgrade
        if encryption_at_rest is not None:
            self._values["encryption_at_rest"] = encryption_at_rest
        if enforce_https is not None:
            self._values["enforce_https"] = enforce_https
        if fine_grained_access_control is not None:
            self._values["fine_grained_access_control"] = fine_grained_access_control
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if logging is not None:
            self._values["logging"] = logging
        if node_to_node_encryption is not None:
            self._values["node_to_node_encryption"] = node_to_node_encryption
        if off_peak_window_enabled is not None:
            self._values["off_peak_window_enabled"] = off_peak_window_enabled
        if off_peak_window_start is not None:
            self._values["off_peak_window_start"] = off_peak_window_start
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if suppress_logs_resource_policy is not None:
            self._values["suppress_logs_resource_policy"] = suppress_logs_resource_policy
        if tls_security_policy is not None:
            self._values["tls_security_policy"] = tls_security_policy
        if use_unsigned_basic_auth is not None:
            self._values["use_unsigned_basic_auth"] = use_unsigned_basic_auth
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if zone_awareness is not None:
            self._values["zone_awareness"] = zone_awareness

    @builtins.property
    def version(self) -> "EngineVersion":
        '''The Elasticsearch/OpenSearch version that your domain will leverage.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast("EngineVersion", result)

    @builtins.property
    def access_policies(
        self,
    ) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''Domain access policies.

        :default: - No access policies.
        '''
        result = self._values.get("access_policies")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    @builtins.property
    def advanced_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional options to specify for the Amazon OpenSearch Service domain.

        :default: - no advanced options are specified

        :see: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options
        '''
        result = self._values.get("advanced_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def automated_snapshot_start_hour(self) -> typing.Optional[jsii.Number]:
        '''The hour in UTC during which the service takes an automated daily snapshot of the indices in the Amazon OpenSearch Service domain.

        Only applies for Elasticsearch versions
        below 5.3.

        :default: - Hourly automated snapshots not used
        '''
        result = self._values.get("automated_snapshot_start_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def capacity(self) -> typing.Optional[CapacityConfig]:
        '''The cluster capacity configuration for the Amazon OpenSearch Service domain.

        :default: - 1 r5.large.search data node; no dedicated master nodes.
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[CapacityConfig], result)

    @builtins.property
    def cognito_dashboards_auth(self) -> typing.Optional[CognitoOptions]:
        '''Configures Amazon OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.

        :default: - Cognito not used for authentication to OpenSearch Dashboards.
        '''
        result = self._values.get("cognito_dashboards_auth")
        return typing.cast(typing.Optional[CognitoOptions], result)

    @builtins.property
    def cold_storage_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable or disable cold storage on the domain.

        You must enable UltraWarm storage to enable cold storage.

        :default: - undefined

        :see: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cold-storage.html
        '''
        result = self._values.get("cold_storage_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def custom_endpoint(self) -> typing.Optional[CustomEndpointOptions]:
        '''To configure a custom domain configure these options.

        If you specify a Route53 hosted zone it will create a CNAME record and use DNS validation for the certificate

        :default: - no custom domain endpoint will be configured
        '''
        result = self._values.get("custom_endpoint")
        return typing.cast(typing.Optional[CustomEndpointOptions], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''Enforces a particular physical domain name.

        :default: - A name will be auto-generated.
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs(self) -> typing.Optional["EbsOptions"]:
        '''The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the Amazon OpenSearch Service domain.

        :default: - 10 GiB General Purpose (SSD) volumes per node.
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["EbsOptions"], result)

    @builtins.property
    def enable_auto_software_update(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether automatic service software updates are enabled for the domain.

        :default: - false

        :see: https://docs.aws.amazon.com/it_it/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-softwareupdateoptions.html
        '''
        result = self._values.get("enable_auto_software_update")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_version_upgrade(self) -> typing.Optional[builtins.bool]:
        '''To upgrade an Amazon OpenSearch Service domain to a new version, rather than replacing the entire domain resource, use the EnableVersionUpgrade update policy.

        :default: - false

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-upgradeopensearchdomain
        '''
        result = self._values.get("enable_version_upgrade")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_at_rest(self) -> typing.Optional["EncryptionAtRestOptions"]:
        '''Encryption at rest options for the cluster.

        :default: - No encryption at rest
        '''
        result = self._values.get("encryption_at_rest")
        return typing.cast(typing.Optional["EncryptionAtRestOptions"], result)

    @builtins.property
    def enforce_https(self) -> typing.Optional[builtins.bool]:
        '''True to require that all traffic to the domain arrive over HTTPS.

        :default: - false
        '''
        result = self._values.get("enforce_https")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def fine_grained_access_control(self) -> typing.Optional[AdvancedSecurityOptions]:
        '''Specifies options for fine-grained access control.

        Requires Elasticsearch version 6.7 or later or OpenSearch version 1.0 or later. Enabling fine-grained access control
        also requires encryption of data at rest and node-to-node encryption, along with
        enforced HTTPS.

        :default: - fine-grained access control is disabled
        '''
        result = self._values.get("fine_grained_access_control")
        return typing.cast(typing.Optional[AdvancedSecurityOptions], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional["IpAddressType"]:
        '''Specify either dual stack or IPv4 as your IP address type.

        Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option.

        If you set your IP address type to dual stack, you can't change your address type later.

        :default: - IpAddressType.IPV4
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional["IpAddressType"], result)

    @builtins.property
    def logging(self) -> typing.Optional["LoggingOptions"]:
        '''Configuration log publishing configuration options.

        :default: - No logs are published
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["LoggingOptions"], result)

    @builtins.property
    def node_to_node_encryption(self) -> typing.Optional[builtins.bool]:
        '''Specify true to enable node to node encryption.

        Requires Elasticsearch version 6.0 or later or OpenSearch version 1.0 or later.

        :default: - Node to node encryption is not enabled.
        '''
        result = self._values.get("node_to_node_encryption")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def off_peak_window_enabled(self) -> typing.Optional[builtins.bool]:
        '''Options for enabling a domain's off-peak window, during which OpenSearch Service can perform mandatory configuration changes on the domain.

        Off-peak windows were introduced on February 16, 2023.
        All domains created before this date have the off-peak window disabled by default.
        You must manually enable and configure the off-peak window for these domains.
        All domains created after this date will have the off-peak window enabled by default.
        You can't disable the off-peak window for a domain after it's enabled.

        :default: - Disabled for domains created before February 16, 2023. Enabled for domains created after. Enabled if ``offPeakWindowStart`` is set.

        :see: https://docs.aws.amazon.com/it_it/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindow.html
        '''
        result = self._values.get("off_peak_window_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def off_peak_window_start(self) -> typing.Optional["WindowStartTime"]:
        '''Start time for the off-peak window, in Coordinated Universal Time (UTC).

        The window length will always be 10 hours, so you can't specify an end time.
        For example, if you specify 11:00 P.M. UTC as a start time, the end time will automatically be set to 9:00 A.M.

        :default: - 10:00 P.M. local time
        '''
        result = self._values.get("off_peak_window_start")
        return typing.cast(typing.Optional["WindowStartTime"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Policy to apply when the domain is removed from the stack.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''The list of security groups that are associated with the VPC endpoints for the domain.

        Only used if ``vpc`` is specified.

        :default: - One new security group is created.

        :see: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def suppress_logs_resource_policy(self) -> typing.Optional[builtins.bool]:
        '''Specify whether to create a CloudWatch Logs resource policy or not.

        When logging is enabled for the domain, a CloudWatch Logs resource policy is created by default.
        However, CloudWatch Logs supports only 10 resource policies per region.
        If you enable logging for several domains, it may hit the quota and cause an error.
        By setting this property to true, creating a resource policy is suppressed, allowing you to avoid this problem.

        If you set this option to true, you must create a resource policy before deployment.

        :default: - false

        :see: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html
        '''
        result = self._values.get("suppress_logs_resource_policy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_security_policy(self) -> typing.Optional["TLSSecurityPolicy"]:
        '''The minimum TLS version required for traffic to the domain.

        :default: - TLSSecurityPolicy.TLS_1_0
        '''
        result = self._values.get("tls_security_policy")
        return typing.cast(typing.Optional["TLSSecurityPolicy"], result)

    @builtins.property
    def use_unsigned_basic_auth(self) -> typing.Optional[builtins.bool]:
        '''Configures the domain so that unsigned basic auth is enabled.

        If no master user is provided a default master user
        with username ``admin`` and a dynamically generated password stored in KMS is created. The password can be retrieved
        by getting ``masterUserPassword`` from the domain instance.

        Setting this to true will also add an access policy that allows unsigned
        access, enable node to node encryption, encryption at rest. If conflicting
        settings are encountered (like disabling encryption at rest) enabling this
        setting will cause a failure.

        :default: - false
        '''
        result = self._values.get("use_unsigned_basic_auth")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''Place the domain inside this VPC.

        :default: - Domain is not placed in a VPC.

        :see: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[typing.List[_SubnetSelection_e57d76df]]:
        '''The specific vpc subnets the domain will be placed in.

        You must provide one subnet for each Availability Zone
        that your domain uses. For example, you must specify three subnet IDs for a three Availability Zone
        domain.

        Only used if ``vpc`` is specified.

        :default: - All private subnets.

        :see: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[typing.List[_SubnetSelection_e57d76df]], result)

    @builtins.property
    def zone_awareness(self) -> typing.Optional["ZoneAwarenessConfig"]:
        '''The cluster zone awareness configuration for the Amazon OpenSearch Service domain.

        :default: - no zone awareness (1 AZ)
        '''
        result = self._values.get("zone_awareness")
        return typing.cast(typing.Optional["ZoneAwarenessConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.EbsOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "iops": "iops",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class EbsOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[_EbsDeviceVolumeType_6792555b] = None,
    ) -> None:
        '''The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the Amazon OpenSearch Service domain.

        For more information, see
        `Amazon EBS <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html>`_
        in the Amazon Elastic Compute Cloud Developer Guide.

        :param enabled: Specifies whether Amazon EBS volumes are attached to data nodes in the Amazon OpenSearch Service domain. Default: - true
        :param iops: The number of I/O operations per second (IOPS) that the volume supports. This property applies only to the gp3 and Provisioned IOPS (SSD) EBS volume type. Default: - iops are not set.
        :param throughput: The throughput (in MiB/s) of the EBS volumes attached to data nodes. This property applies only to the gp3 volume type. Default: - throughput is not set.
        :param volume_size: The size (in GiB) of the EBS volume for each data node. The minimum and maximum size of an EBS volume depends on the EBS volume type and the instance type to which it is attached. For valid values, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the Amazon OpenSearch Service Developer Guide. Default: 10
        :param volume_type: The EBS volume type to use with the Amazon OpenSearch Service domain, such as standard, gp2, io1. Default: gp2

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_0,
                ebs=EbsOptions(
                    volume_size=100,
                    volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
                ),
                node_to_node_encryption=True,
                encryption_at_rest=EncryptionAtRestOptions(
                    enabled=True
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__388b3ff533950547aa29493d027ac01b8d3d4139dc5061e4f70a2cf8e0912d38)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether Amazon EBS volumes are attached to data nodes in the Amazon OpenSearch Service domain.

        :default: - true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''The number of I/O operations per second (IOPS) that the volume supports.

        This property applies only to the gp3 and Provisioned IOPS (SSD) EBS
        volume type.

        :default: - iops are not set.
        '''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''The throughput (in MiB/s) of the EBS volumes attached to data nodes.

        This property applies only to the gp3 volume type.

        :default: - throughput is not set.
        '''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''The size (in GiB) of the EBS volume for each data node.

        The minimum and
        maximum size of an EBS volume depends on the EBS volume type and the
        instance type to which it is attached.  For  valid values, see
        `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_
        in the Amazon OpenSearch Service Developer Guide.

        :default: 10
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[_EbsDeviceVolumeType_6792555b]:
        '''The EBS volume type to use with the Amazon OpenSearch Service domain, such as standard, gp2, io1.

        :default: gp2
        '''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[_EbsDeviceVolumeType_6792555b], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EbsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.EncryptionAtRestOptions",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "kms_key": "kmsKey"},
)
class EncryptionAtRestOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
    ) -> None:
        '''Whether the domain should encrypt data at rest, and if so, the AWS Key Management Service (KMS) key to use.

        Can only be used to create a new domain,
        not update an existing one. Requires Elasticsearch version 5.1 or later or OpenSearch version 1.0 or later.

        :param enabled: Specify true to enable encryption at rest. Default: - encryption at rest is disabled.
        :param kms_key: Supply if using KMS key for encryption at rest. Default: - uses default aws/es KMS key.

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_0,
                enforce_https=True,
                node_to_node_encryption=True,
                encryption_at_rest=EncryptionAtRestOptions(
                    enabled=True
                ),
                fine_grained_access_control=AdvancedSecurityOptions(
                    master_user_name="master-user",
                    saml_authentication_enabled=True,
                    saml_authentication_options=SAMLOptionsProperty(
                        idp_entity_id="entity-id",
                        idp_metadata_content="metadata-content-with-quotes-escaped"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5973f04ac98b9a2d9bddce35a01a16416d58b7f8a10bd553cfabe3909eb2523)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if kms_key is not None:
            self._values["kms_key"] = kms_key

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Specify true to enable encryption at rest.

        :default: - encryption at rest is disabled.
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''Supply if using KMS key for encryption at rest.

        :default: - uses default aws/es KMS key.
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncryptionAtRestOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EngineVersion(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchservice.EngineVersion",
):
    '''OpenSearch version.

    :exampleMetadata: infused

    Example::

        domain = Domain(self, "Domain",
            version=EngineVersion.OPENSEARCH_1_0,
            ebs=EbsOptions(
                volume_size=100,
                volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
            ),
            node_to_node_encryption=True,
            encryption_at_rest=EncryptionAtRestOptions(
                enabled=True
            )
        )
    '''

    @jsii.member(jsii_name="elasticsearch")
    @builtins.classmethod
    def elasticsearch(cls, version: builtins.str) -> "EngineVersion":
        '''Custom ElasticSearch version.

        :param version: custom version number.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e9ff089c138ae673bd34470711323158868e600ef582eaf1138c7dbfabe659d)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast("EngineVersion", jsii.sinvoke(cls, "elasticsearch", [version]))

    @jsii.member(jsii_name="openSearch")
    @builtins.classmethod
    def open_search(cls, version: builtins.str) -> "EngineVersion":
        '''Custom OpenSearch version.

        :param version: custom version number.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4e60eeb3f3de1852dda34e9fc12006c90072b2af1169917137b26002e7ca6b)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast("EngineVersion", jsii.sinvoke(cls, "openSearch", [version]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_1_5")
    def ELASTICSEARCH_1_5(cls) -> "EngineVersion":
        '''AWS Elasticsearch 1.5.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_1_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_2_3")
    def ELASTICSEARCH_2_3(cls) -> "EngineVersion":
        '''AWS Elasticsearch 2.3.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_2_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_5_1")
    def ELASTICSEARCH_5_1(cls) -> "EngineVersion":
        '''AWS Elasticsearch 5.1.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_5_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_5_3")
    def ELASTICSEARCH_5_3(cls) -> "EngineVersion":
        '''AWS Elasticsearch 5.3.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_5_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_5_5")
    def ELASTICSEARCH_5_5(cls) -> "EngineVersion":
        '''AWS Elasticsearch 5.5.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_5_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_5_6")
    def ELASTICSEARCH_5_6(cls) -> "EngineVersion":
        '''AWS Elasticsearch 5.6.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_5_6"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_6_0")
    def ELASTICSEARCH_6_0(cls) -> "EngineVersion":
        '''AWS Elasticsearch 6.0.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_6_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_6_2")
    def ELASTICSEARCH_6_2(cls) -> "EngineVersion":
        '''AWS Elasticsearch 6.2.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_6_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_6_3")
    def ELASTICSEARCH_6_3(cls) -> "EngineVersion":
        '''AWS Elasticsearch 6.3.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_6_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_6_4")
    def ELASTICSEARCH_6_4(cls) -> "EngineVersion":
        '''AWS Elasticsearch 6.4.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_6_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_6_5")
    def ELASTICSEARCH_6_5(cls) -> "EngineVersion":
        '''AWS Elasticsearch 6.5.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_6_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_6_7")
    def ELASTICSEARCH_6_7(cls) -> "EngineVersion":
        '''AWS Elasticsearch 6.7.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_6_7"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_6_8")
    def ELASTICSEARCH_6_8(cls) -> "EngineVersion":
        '''AWS Elasticsearch 6.8.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_6_8"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_7_1")
    def ELASTICSEARCH_7_1(cls) -> "EngineVersion":
        '''AWS Elasticsearch 7.1.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_7_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_7_10")
    def ELASTICSEARCH_7_10(cls) -> "EngineVersion":
        '''AWS Elasticsearch 7.10.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_7_10"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_7_4")
    def ELASTICSEARCH_7_4(cls) -> "EngineVersion":
        '''AWS Elasticsearch 7.4.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_7_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_7_7")
    def ELASTICSEARCH_7_7(cls) -> "EngineVersion":
        '''AWS Elasticsearch 7.7.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_7_7"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_7_8")
    def ELASTICSEARCH_7_8(cls) -> "EngineVersion":
        '''AWS Elasticsearch 7.8.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_7_8"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_7_9")
    def ELASTICSEARCH_7_9(cls) -> "EngineVersion":
        '''AWS Elasticsearch 7.9.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "ELASTICSEARCH_7_9"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_1_0")
    def OPENSEARCH_1_0(cls) -> "EngineVersion":
        '''AWS OpenSearch 1.0.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_1_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_1_1")
    def OPENSEARCH_1_1(cls) -> "EngineVersion":
        '''AWS OpenSearch 1.1.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_1_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_1_2")
    def OPENSEARCH_1_2(cls) -> "EngineVersion":
        '''AWS OpenSearch 1.2.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_1_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_1_3")
    def OPENSEARCH_1_3(cls) -> "EngineVersion":
        '''AWS OpenSearch 1.3.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_1_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_2_10")
    def OPENSEARCH_2_10(cls) -> "EngineVersion":
        '''(deprecated) AWS OpenSearch 2.10.

        :deprecated: use latest version of the OpenSearch engine

        :stability: deprecated
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_2_10"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_2_11")
    def OPENSEARCH_2_11(cls) -> "EngineVersion":
        '''AWS OpenSearch 2.11.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_2_11"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_2_3")
    def OPENSEARCH_2_3(cls) -> "EngineVersion":
        '''AWS OpenSearch 2.3.

        OpenSearch 2.3 is now available on Amazon OpenSearch Service across 26
        regions globally. Please refer to the AWS Region Table for more
        information about Amazon OpenSearch Service availability:
        https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_2_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_2_5")
    def OPENSEARCH_2_5(cls) -> "EngineVersion":
        '''AWS OpenSearch 2.5.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_2_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_2_7")
    def OPENSEARCH_2_7(cls) -> "EngineVersion":
        '''AWS OpenSearch 2.7.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_2_7"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_2_9")
    def OPENSEARCH_2_9(cls) -> "EngineVersion":
        '''AWS OpenSearch 2.9.'''
        return typing.cast("EngineVersion", jsii.sget(cls, "OPENSEARCH_2_9"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''engine version identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.interface(jsii_type="aws-cdk-lib.aws_opensearchservice.IDomain")
class IDomain(_IResource_c80c4260, typing_extensions.Protocol):
    '''An interface that represents an Amazon OpenSearch Service domain - either created with the CDK, or an existing one.'''

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> builtins.str:
        '''Arn of the Amazon OpenSearch Service domain.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="domainEndpoint")
    def domain_endpoint(self) -> builtins.str:
        '''Endpoint of the Amazon OpenSearch Service domain.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        '''Identifier of the Amazon OpenSearch Service domain.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''Domain name of the Amazon OpenSearch Service domain.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantIndexRead")
    def grant_index_read(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantIndexReadWrite")
    def grant_index_read_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantIndexWrite")
    def grant_index_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantPathRead")
    def grant_path_read(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantPathReadWrite")
    def grant_path_read_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantPathWrite")
    def grant_path_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this domain.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricAutomatedSnapshotFailure")
    def metric_automated_snapshot_failure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for automated snapshot failures.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricClusterIndexWritesBlocked")
    def metric_cluster_index_writes_blocked(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the cluster blocking index writes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 1 minute
        '''
        ...

    @jsii.member(jsii_name="metricClusterStatusRed")
    def metric_cluster_status_red(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the time the cluster status is red.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricClusterStatusYellow")
    def metric_cluster_status_yellow(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the time the cluster status is yellow.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricCPUUtilization")
    def metric_cpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricFreeStorageSpace")
    def metric_free_storage_space(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the storage space of nodes in the cluster.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricIndexingLatency")
    def metric_indexing_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for indexing latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricJVMMemoryPressure")
    def metric_jvm_memory_pressure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricKMSKeyError")
    def metric_kms_key_error(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for KMS key errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricKMSKeyInaccessible")
    def metric_kms_key_inaccessible(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for KMS key being inaccessible.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricMasterCPUUtilization")
    def metric_master_cpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for master CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricMasterJVMMemoryPressure")
    def metric_master_jvm_memory_pressure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for master JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricNodes")
    def metric_nodes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of nodes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 1 hour
        '''
        ...

    @jsii.member(jsii_name="metricSearchableDocuments")
    def metric_searchable_documents(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for number of searchable documents.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricSearchLatency")
    def metric_search_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for search latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes
        '''
        ...


class _IDomainProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''An interface that represents an Amazon OpenSearch Service domain - either created with the CDK, or an existing one.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_opensearchservice.IDomain"

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> builtins.str:
        '''Arn of the Amazon OpenSearch Service domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainArn"))

    @builtins.property
    @jsii.member(jsii_name="domainEndpoint")
    def domain_endpoint(self) -> builtins.str:
        '''Endpoint of the Amazon OpenSearch Service domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        '''Identifier of the Amazon OpenSearch Service domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''Domain name of the Amazon OpenSearch Service domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @jsii.member(jsii_name="grantIndexRead")
    def grant_index_read(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a94e154ecf4f9073f5d7c9e1ea7e03f69da172094fa85d76ced59ad241b1fb2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexRead", [index, identity]))

    @jsii.member(jsii_name="grantIndexReadWrite")
    def grant_index_read_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e57d957edccc649ee25aa5e026d1e4a380aefa1fca47ac85fb2332017684c2d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexReadWrite", [index, identity]))

    @jsii.member(jsii_name="grantIndexWrite")
    def grant_index_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e11c5bfffab0ceb5f6e6d11d8c2422feb5ca967394bcd5e0f9cf0f2979cfac0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexWrite", [index, identity]))

    @jsii.member(jsii_name="grantPathRead")
    def grant_path_read(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__023ad84c0e882f65c76fb064e82ff3cd67cfa07f593f45818a1a2c9c03688dbb)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathRead", [path, identity]))

    @jsii.member(jsii_name="grantPathReadWrite")
    def grant_path_read_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bc2ab50330adaac8ffebc655effda16c72446686a9b26d8c09644e3cde524f5)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathReadWrite", [path, identity]))

    @jsii.member(jsii_name="grantPathWrite")
    def grant_path_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__402463dfcfddcd6aaa36a0ec13a1628f29914c911b19e66e17d3cc38b5661762)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathWrite", [path, identity]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d29656876fe4553e567e59a1a0cbb6942145d5715c6aec2bdba4c0524ce284f)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [identity]))

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99698755eef9bf19abbfc958ee11633e093e93f46c5c5f99f45308fa7212f08b)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantReadWrite", [identity]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__599ff214d878684eadaa975bf3d8bf19930fc28a8788cab7625b3a913e0975e1)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [identity]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this domain.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed477ecf16b0f23884f9eb3a0a90df530d2486e08c8dd662432a14ff4837bd08)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricAutomatedSnapshotFailure")
    def metric_automated_snapshot_failure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for automated snapshot failures.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricAutomatedSnapshotFailure", [props]))

    @jsii.member(jsii_name="metricClusterIndexWritesBlocked")
    def metric_cluster_index_writes_blocked(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the cluster blocking index writes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 1 minute
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricClusterIndexWritesBlocked", [props]))

    @jsii.member(jsii_name="metricClusterStatusRed")
    def metric_cluster_status_red(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the time the cluster status is red.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricClusterStatusRed", [props]))

    @jsii.member(jsii_name="metricClusterStatusYellow")
    def metric_cluster_status_yellow(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the time the cluster status is yellow.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricClusterStatusYellow", [props]))

    @jsii.member(jsii_name="metricCPUUtilization")
    def metric_cpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricCPUUtilization", [props]))

    @jsii.member(jsii_name="metricFreeStorageSpace")
    def metric_free_storage_space(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the storage space of nodes in the cluster.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFreeStorageSpace", [props]))

    @jsii.member(jsii_name="metricIndexingLatency")
    def metric_indexing_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for indexing latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricIndexingLatency", [props]))

    @jsii.member(jsii_name="metricJVMMemoryPressure")
    def metric_jvm_memory_pressure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricJVMMemoryPressure", [props]))

    @jsii.member(jsii_name="metricKMSKeyError")
    def metric_kms_key_error(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for KMS key errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricKMSKeyError", [props]))

    @jsii.member(jsii_name="metricKMSKeyInaccessible")
    def metric_kms_key_inaccessible(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for KMS key being inaccessible.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricKMSKeyInaccessible", [props]))

    @jsii.member(jsii_name="metricMasterCPUUtilization")
    def metric_master_cpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for master CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricMasterCPUUtilization", [props]))

    @jsii.member(jsii_name="metricMasterJVMMemoryPressure")
    def metric_master_jvm_memory_pressure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for master JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricMasterJVMMemoryPressure", [props]))

    @jsii.member(jsii_name="metricNodes")
    def metric_nodes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of nodes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 1 hour
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNodes", [props]))

    @jsii.member(jsii_name="metricSearchableDocuments")
    def metric_searchable_documents(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for number of searchable documents.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSearchableDocuments", [props]))

    @jsii.member(jsii_name="metricSearchLatency")
    def metric_search_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for search latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSearchLatency", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomain).__jsii_proxy_class__ = lambda : _IDomainProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_opensearchservice.IpAddressType")
class IpAddressType(enum.Enum):
    '''The IP address type for the domain.

    :exampleMetadata: infused

    Example::

        domain = Domain(self, "Domain",
            version=EngineVersion.OPENSEARCH_1_3,
            ip_address_type=IpAddressType.DUAL_STACK
        )
    '''

    IPV4 = "IPV4"
    '''IPv4 addresses only.'''
    DUAL_STACK = "DUAL_STACK"
    '''IPv4 and IPv6 addresses.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.LoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "app_log_enabled": "appLogEnabled",
        "app_log_group": "appLogGroup",
        "audit_log_enabled": "auditLogEnabled",
        "audit_log_group": "auditLogGroup",
        "slow_index_log_enabled": "slowIndexLogEnabled",
        "slow_index_log_group": "slowIndexLogGroup",
        "slow_search_log_enabled": "slowSearchLogEnabled",
        "slow_search_log_group": "slowSearchLogGroup",
    },
)
class LoggingOptions:
    def __init__(
        self,
        *,
        app_log_enabled: typing.Optional[builtins.bool] = None,
        app_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        audit_log_enabled: typing.Optional[builtins.bool] = None,
        audit_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        slow_index_log_enabled: typing.Optional[builtins.bool] = None,
        slow_index_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        slow_search_log_enabled: typing.Optional[builtins.bool] = None,
        slow_search_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    ) -> None:
        '''Configures log settings for the domain.

        :param app_log_enabled: Specify if Amazon OpenSearch Service application logging should be set up. Requires Elasticsearch version 5.1 or later or OpenSearch version 1.0 or later. An explicit ``false`` is required when disabling it from ``true``. Default: - false
        :param app_log_group: Log Amazon OpenSearch Service application logs to this log group. Default: - a new log group is created if app logging is enabled
        :param audit_log_enabled: Specify if Amazon OpenSearch Service audit logging should be set up. Requires Elasticsearch version 6.7 or later or OpenSearch version 1.0 or later and fine grained access control to be enabled. Default: - false
        :param audit_log_group: Log Amazon OpenSearch Service audit logs to this log group. Default: - a new log group is created if audit logging is enabled
        :param slow_index_log_enabled: Specify if slow index logging should be set up. Requires Elasticsearch version 5.1 or later or OpenSearch version 1.0 or later. An explicit ``false`` is required when disabling it from ``true``. Default: - false
        :param slow_index_log_group: Log slow indices to this log group. Default: - a new log group is created if slow index logging is enabled
        :param slow_search_log_enabled: Specify if slow search logging should be set up. Requires Elasticsearch version 5.1 or later or OpenSearch version 1.0 or later. An explicit ``false`` is required when disabling it from ``true``. Default: - false
        :param slow_search_log_group: Log slow searches to this log group. Default: - a new log group is created if slow search logging is enabled

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_0,
                enforce_https=True,
                node_to_node_encryption=True,
                encryption_at_rest=EncryptionAtRestOptions(
                    enabled=True
                ),
                fine_grained_access_control=AdvancedSecurityOptions(
                    master_user_name="master-user"
                ),
                logging=LoggingOptions(
                    audit_log_enabled=True,
                    slow_search_log_enabled=True,
                    app_log_enabled=True,
                    slow_index_log_enabled=True
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f2efbcf1fc757504a748851740a44deb59ed98ee9c1d8c213d60960f900a593)
            check_type(argname="argument app_log_enabled", value=app_log_enabled, expected_type=type_hints["app_log_enabled"])
            check_type(argname="argument app_log_group", value=app_log_group, expected_type=type_hints["app_log_group"])
            check_type(argname="argument audit_log_enabled", value=audit_log_enabled, expected_type=type_hints["audit_log_enabled"])
            check_type(argname="argument audit_log_group", value=audit_log_group, expected_type=type_hints["audit_log_group"])
            check_type(argname="argument slow_index_log_enabled", value=slow_index_log_enabled, expected_type=type_hints["slow_index_log_enabled"])
            check_type(argname="argument slow_index_log_group", value=slow_index_log_group, expected_type=type_hints["slow_index_log_group"])
            check_type(argname="argument slow_search_log_enabled", value=slow_search_log_enabled, expected_type=type_hints["slow_search_log_enabled"])
            check_type(argname="argument slow_search_log_group", value=slow_search_log_group, expected_type=type_hints["slow_search_log_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if app_log_enabled is not None:
            self._values["app_log_enabled"] = app_log_enabled
        if app_log_group is not None:
            self._values["app_log_group"] = app_log_group
        if audit_log_enabled is not None:
            self._values["audit_log_enabled"] = audit_log_enabled
        if audit_log_group is not None:
            self._values["audit_log_group"] = audit_log_group
        if slow_index_log_enabled is not None:
            self._values["slow_index_log_enabled"] = slow_index_log_enabled
        if slow_index_log_group is not None:
            self._values["slow_index_log_group"] = slow_index_log_group
        if slow_search_log_enabled is not None:
            self._values["slow_search_log_enabled"] = slow_search_log_enabled
        if slow_search_log_group is not None:
            self._values["slow_search_log_group"] = slow_search_log_group

    @builtins.property
    def app_log_enabled(self) -> typing.Optional[builtins.bool]:
        '''Specify if Amazon OpenSearch Service application logging should be set up.

        Requires Elasticsearch version 5.1 or later or OpenSearch version 1.0 or later.
        An explicit ``false`` is required when disabling it from ``true``.

        :default: - false
        '''
        result = self._values.get("app_log_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def app_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log Amazon OpenSearch Service application logs to this log group.

        :default: - a new log group is created if app logging is enabled
        '''
        result = self._values.get("app_log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def audit_log_enabled(self) -> typing.Optional[builtins.bool]:
        '''Specify if Amazon OpenSearch Service audit logging should be set up.

        Requires Elasticsearch version 6.7 or later or OpenSearch version 1.0 or later and fine grained access control to be enabled.

        :default: - false
        '''
        result = self._values.get("audit_log_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def audit_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log Amazon OpenSearch Service audit logs to this log group.

        :default: - a new log group is created if audit logging is enabled
        '''
        result = self._values.get("audit_log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def slow_index_log_enabled(self) -> typing.Optional[builtins.bool]:
        '''Specify if slow index logging should be set up.

        Requires Elasticsearch version 5.1 or later or OpenSearch version 1.0 or later.
        An explicit ``false`` is required when disabling it from ``true``.

        :default: - false
        '''
        result = self._values.get("slow_index_log_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def slow_index_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log slow indices to this log group.

        :default: - a new log group is created if slow index logging is enabled
        '''
        result = self._values.get("slow_index_log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def slow_search_log_enabled(self) -> typing.Optional[builtins.bool]:
        '''Specify if slow search logging should be set up.

        Requires Elasticsearch version 5.1 or later or OpenSearch version 1.0 or later.
        An explicit ``false`` is required when disabling it from ``true``.

        :default: - false
        '''
        result = self._values.get("slow_search_log_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def slow_search_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log slow searches to this log group.

        :default: - a new log group is created if slow search logging is enabled
        '''
        result = self._values.get("slow_search_log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.SAMLOptionsProperty",
    jsii_struct_bases=[],
    name_mapping={
        "idp_entity_id": "idpEntityId",
        "idp_metadata_content": "idpMetadataContent",
        "master_backend_role": "masterBackendRole",
        "master_user_name": "masterUserName",
        "roles_key": "rolesKey",
        "session_timeout_minutes": "sessionTimeoutMinutes",
        "subject_key": "subjectKey",
    },
)
class SAMLOptionsProperty:
    def __init__(
        self,
        *,
        idp_entity_id: builtins.str,
        idp_metadata_content: builtins.str,
        master_backend_role: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        roles_key: typing.Optional[builtins.str] = None,
        session_timeout_minutes: typing.Optional[jsii.Number] = None,
        subject_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Container for information about the SAML configuration for OpenSearch Dashboards.

        :param idp_entity_id: The unique entity ID of the application in the SAML identity provider.
        :param idp_metadata_content: The metadata of the SAML application, in XML format.
        :param master_backend_role: The backend role that the SAML master user is mapped to. Any users with this backend role receives full permission in OpenSearch Dashboards/Kibana. To use a SAML master backend role, configure the ``rolesKey`` property. Default: - The master user is not mapped to a backend role
        :param master_user_name: The SAML master username, which is stored in the domain's internal user database. This SAML user receives full permission in OpenSearch Dashboards/Kibana. Creating a new master username does not delete any existing master usernames. Default: - No master user name is configured
        :param roles_key: Element of the SAML assertion to use for backend roles. Default: - roles
        :param session_timeout_minutes: The duration, in minutes, after which a user session becomes inactive. Default: - 60
        :param subject_key: Element of the SAML assertion to use for the user name. Default: - NameID element of the SAML assertion fot the user name

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_0,
                enforce_https=True,
                node_to_node_encryption=True,
                encryption_at_rest=EncryptionAtRestOptions(
                    enabled=True
                ),
                fine_grained_access_control=AdvancedSecurityOptions(
                    master_user_name="master-user",
                    saml_authentication_enabled=True,
                    saml_authentication_options=SAMLOptionsProperty(
                        idp_entity_id="entity-id",
                        idp_metadata_content="metadata-content-with-quotes-escaped"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3971b3c73627d57587c667b1ede64fbba4de4fd4a086af959dc2d0f812f8e36b)
            check_type(argname="argument idp_entity_id", value=idp_entity_id, expected_type=type_hints["idp_entity_id"])
            check_type(argname="argument idp_metadata_content", value=idp_metadata_content, expected_type=type_hints["idp_metadata_content"])
            check_type(argname="argument master_backend_role", value=master_backend_role, expected_type=type_hints["master_backend_role"])
            check_type(argname="argument master_user_name", value=master_user_name, expected_type=type_hints["master_user_name"])
            check_type(argname="argument roles_key", value=roles_key, expected_type=type_hints["roles_key"])
            check_type(argname="argument session_timeout_minutes", value=session_timeout_minutes, expected_type=type_hints["session_timeout_minutes"])
            check_type(argname="argument subject_key", value=subject_key, expected_type=type_hints["subject_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "idp_entity_id": idp_entity_id,
            "idp_metadata_content": idp_metadata_content,
        }
        if master_backend_role is not None:
            self._values["master_backend_role"] = master_backend_role
        if master_user_name is not None:
            self._values["master_user_name"] = master_user_name
        if roles_key is not None:
            self._values["roles_key"] = roles_key
        if session_timeout_minutes is not None:
            self._values["session_timeout_minutes"] = session_timeout_minutes
        if subject_key is not None:
            self._values["subject_key"] = subject_key

    @builtins.property
    def idp_entity_id(self) -> builtins.str:
        '''The unique entity ID of the application in the SAML identity provider.'''
        result = self._values.get("idp_entity_id")
        assert result is not None, "Required property 'idp_entity_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def idp_metadata_content(self) -> builtins.str:
        '''The metadata of the SAML application, in XML format.'''
        result = self._values.get("idp_metadata_content")
        assert result is not None, "Required property 'idp_metadata_content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_backend_role(self) -> typing.Optional[builtins.str]:
        '''The backend role that the SAML master user is mapped to.

        Any users with this backend role receives full permission in OpenSearch Dashboards/Kibana.
        To use a SAML master backend role, configure the ``rolesKey`` property.

        :default: - The master user is not mapped to a backend role
        '''
        result = self._values.get("master_backend_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_name(self) -> typing.Optional[builtins.str]:
        '''The SAML master username, which is stored in the domain's internal user database.

        This SAML user receives full permission in OpenSearch Dashboards/Kibana.
        Creating a new master username does not delete any existing master usernames.

        :default: - No master user name is configured
        '''
        result = self._values.get("master_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles_key(self) -> typing.Optional[builtins.str]:
        '''Element of the SAML assertion to use for backend roles.

        :default: - roles
        '''
        result = self._values.get("roles_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''The duration, in minutes, after which a user session becomes inactive.

        :default: - 60
        '''
        result = self._values.get("session_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subject_key(self) -> typing.Optional[builtins.str]:
        '''Element of the SAML assertion to use for the user name.

        :default: - NameID element of the SAML assertion fot the user name
        '''
        result = self._values.get("subject_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SAMLOptionsProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_opensearchservice.TLSSecurityPolicy")
class TLSSecurityPolicy(enum.Enum):
    '''The minimum TLS version required for traffic to the domain.'''

    TLS_1_0 = "TLS_1_0"
    '''Cipher suite TLS 1.0.'''
    TLS_1_2 = "TLS_1_2"
    '''Cipher suite TLS 1.2.'''
    TLS_1_2_PFS = "TLS_1_2_PFS"
    '''Cipher suite TLS 1.2 to 1.3 with perfect forward secrecy (PFS).'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.WindowStartTime",
    jsii_struct_bases=[],
    name_mapping={"hours": "hours", "minutes": "minutes"},
)
class WindowStartTime:
    def __init__(self, *, hours: jsii.Number, minutes: jsii.Number) -> None:
        '''
        :param hours: The start hour of the window in Coordinated Universal Time (UTC), using 24-hour time. For example, 17 refers to 5:00 P.M. UTC. Default: - 22
        :param minutes: The start minute of the window, in UTC. Default: - 0

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_3,
                off_peak_window_enabled=True,  # can be omitted if offPeakWindowStart is set
                off_peak_window_start=WindowStartTime(
                    hours=20,
                    minutes=0
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa10c95f5a58e650c77a0c42630f2fa77e6475974ad59138caebb586e5fad2c)
            check_type(argname="argument hours", value=hours, expected_type=type_hints["hours"])
            check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hours": hours,
            "minutes": minutes,
        }

    @builtins.property
    def hours(self) -> jsii.Number:
        '''The start hour of the window in Coordinated Universal Time (UTC), using 24-hour time.

        For example, 17 refers to 5:00 P.M. UTC.

        :default: - 22
        '''
        result = self._values.get("hours")
        assert result is not None, "Required property 'hours' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minutes(self) -> jsii.Number:
        '''The start minute of the window, in UTC.

        :default: - 0
        '''
        result = self._values.get("minutes")
        assert result is not None, "Required property 'minutes' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowStartTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchservice.ZoneAwarenessConfig",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone_count": "availabilityZoneCount",
        "enabled": "enabled",
    },
)
class ZoneAwarenessConfig:
    def __init__(
        self,
        *,
        availability_zone_count: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Specifies zone awareness configuration options.

        :param availability_zone_count: If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use. Valid values are 2 and 3. Default: - 2 if zone awareness is enabled.
        :param enabled: Indicates whether to enable zone awareness for the Amazon OpenSearch Service domain. When you enable zone awareness, Amazon OpenSearch Service allocates the nodes and replica index shards that belong to a cluster across two Availability Zones (AZs) in the same region to prevent data loss and minimize downtime in the event of node or data center failure. Don't enable zone awareness if your cluster has no replica index shards or is a single-node cluster. For more information, see `Configuring a Multi-AZ Domain <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html>`_ in the Amazon OpenSearch Service Developer Guide. Default: - false

        :exampleMetadata: infused

        Example::

            domain = Domain(self, "Domain",
                version=EngineVersion.OPENSEARCH_1_3,
                ebs=EbsOptions(
                    volume_size=10,
                    volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD_GP3
                ),
                zone_awareness=ZoneAwarenessConfig(
                    enabled=True,
                    availability_zone_count=3
                ),
                capacity=CapacityConfig(
                    multi_az_with_standby_enabled=True,
                    master_nodes=3,
                    data_nodes=3
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d25db0248db5c13d8d8371728510a20f1632b4180af6f40e9838b4d28d6a375d)
            check_type(argname="argument availability_zone_count", value=availability_zone_count, expected_type=type_hints["availability_zone_count"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zone_count is not None:
            self._values["availability_zone_count"] = availability_zone_count
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def availability_zone_count(self) -> typing.Optional[jsii.Number]:
        '''If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use.

        Valid values are 2 and 3.

        :default: - 2 if zone awareness is enabled.
        '''
        result = self._values.get("availability_zone_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to enable zone awareness for the Amazon OpenSearch Service domain.

        When you enable zone awareness, Amazon OpenSearch Service allocates the nodes and replica
        index shards that belong to a cluster across two Availability Zones (AZs)
        in the same region to prevent data loss and minimize downtime in the event
        of node or data center failure. Don't enable zone awareness if your cluster
        has no replica index shards or is a single-node cluster. For more information,
        see `Configuring a Multi-AZ Domain <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html>`_
        in the Amazon OpenSearch Service Developer Guide.

        :default: - false
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneAwarenessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IDomain, _IConnectable_10015a05)
class Domain(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchservice.Domain",
):
    '''Provides an Amazon OpenSearch Service domain.

    :exampleMetadata: infused

    Example::

        domain = Domain(self, "Domain",
            version=EngineVersion.OPENSEARCH_1_0,
            ebs=EbsOptions(
                volume_size=100,
                volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
            ),
            node_to_node_encryption=True,
            encryption_at_rest=EncryptionAtRestOptions(
                enabled=True
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        version: EngineVersion,
        access_policies: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
        capacity: typing.Optional[typing.Union[CapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        cognito_dashboards_auth: typing.Optional[typing.Union[CognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cold_storage_enabled: typing.Optional[builtins.bool] = None,
        custom_endpoint: typing.Optional[typing.Union[CustomEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        ebs: typing.Optional[typing.Union[EbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        enable_auto_software_update: typing.Optional[builtins.bool] = None,
        enable_version_upgrade: typing.Optional[builtins.bool] = None,
        encryption_at_rest: typing.Optional[typing.Union[EncryptionAtRestOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        enforce_https: typing.Optional[builtins.bool] = None,
        fine_grained_access_control: typing.Optional[typing.Union[AdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        ip_address_type: typing.Optional[IpAddressType] = None,
        logging: typing.Optional[typing.Union[LoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        node_to_node_encryption: typing.Optional[builtins.bool] = None,
        off_peak_window_enabled: typing.Optional[builtins.bool] = None,
        off_peak_window_start: typing.Optional[typing.Union[WindowStartTime, typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        suppress_logs_resource_policy: typing.Optional[builtins.bool] = None,
        tls_security_policy: typing.Optional[TLSSecurityPolicy] = None,
        use_unsigned_basic_auth: typing.Optional[builtins.bool] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
        zone_awareness: typing.Optional[typing.Union[ZoneAwarenessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param version: The Elasticsearch/OpenSearch version that your domain will leverage.
        :param access_policies: Domain access policies. Default: - No access policies.
        :param advanced_options: Additional options to specify for the Amazon OpenSearch Service domain. Default: - no advanced options are specified
        :param automated_snapshot_start_hour: The hour in UTC during which the service takes an automated daily snapshot of the indices in the Amazon OpenSearch Service domain. Only applies for Elasticsearch versions below 5.3. Default: - Hourly automated snapshots not used
        :param capacity: The cluster capacity configuration for the Amazon OpenSearch Service domain. Default: - 1 r5.large.search data node; no dedicated master nodes.
        :param cognito_dashboards_auth: Configures Amazon OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards. Default: - Cognito not used for authentication to OpenSearch Dashboards.
        :param cold_storage_enabled: Whether to enable or disable cold storage on the domain. You must enable UltraWarm storage to enable cold storage. Default: - undefined
        :param custom_endpoint: To configure a custom domain configure these options. If you specify a Route53 hosted zone it will create a CNAME record and use DNS validation for the certificate Default: - no custom domain endpoint will be configured
        :param domain_name: Enforces a particular physical domain name. Default: - A name will be auto-generated.
        :param ebs: The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the Amazon OpenSearch Service domain. Default: - 10 GiB General Purpose (SSD) volumes per node.
        :param enable_auto_software_update: Specifies whether automatic service software updates are enabled for the domain. Default: - false
        :param enable_version_upgrade: To upgrade an Amazon OpenSearch Service domain to a new version, rather than replacing the entire domain resource, use the EnableVersionUpgrade update policy. Default: - false
        :param encryption_at_rest: Encryption at rest options for the cluster. Default: - No encryption at rest
        :param enforce_https: True to require that all traffic to the domain arrive over HTTPS. Default: - false
        :param fine_grained_access_control: Specifies options for fine-grained access control. Requires Elasticsearch version 6.7 or later or OpenSearch version 1.0 or later. Enabling fine-grained access control also requires encryption of data at rest and node-to-node encryption, along with enforced HTTPS. Default: - fine-grained access control is disabled
        :param ip_address_type: Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later. Default: - IpAddressType.IPV4
        :param logging: Configuration log publishing configuration options. Default: - No logs are published
        :param node_to_node_encryption: Specify true to enable node to node encryption. Requires Elasticsearch version 6.0 or later or OpenSearch version 1.0 or later. Default: - Node to node encryption is not enabled.
        :param off_peak_window_enabled: Options for enabling a domain's off-peak window, during which OpenSearch Service can perform mandatory configuration changes on the domain. Off-peak windows were introduced on February 16, 2023. All domains created before this date have the off-peak window disabled by default. You must manually enable and configure the off-peak window for these domains. All domains created after this date will have the off-peak window enabled by default. You can't disable the off-peak window for a domain after it's enabled. Default: - Disabled for domains created before February 16, 2023. Enabled for domains created after. Enabled if ``offPeakWindowStart`` is set.
        :param off_peak_window_start: Start time for the off-peak window, in Coordinated Universal Time (UTC). The window length will always be 10 hours, so you can't specify an end time. For example, if you specify 11:00 P.M. UTC as a start time, the end time will automatically be set to 9:00 A.M. Default: - 10:00 P.M. local time
        :param removal_policy: Policy to apply when the domain is removed from the stack. Default: RemovalPolicy.RETAIN
        :param security_groups: The list of security groups that are associated with the VPC endpoints for the domain. Only used if ``vpc`` is specified. Default: - One new security group is created.
        :param suppress_logs_resource_policy: Specify whether to create a CloudWatch Logs resource policy or not. When logging is enabled for the domain, a CloudWatch Logs resource policy is created by default. However, CloudWatch Logs supports only 10 resource policies per region. If you enable logging for several domains, it may hit the quota and cause an error. By setting this property to true, creating a resource policy is suppressed, allowing you to avoid this problem. If you set this option to true, you must create a resource policy before deployment. Default: - false
        :param tls_security_policy: The minimum TLS version required for traffic to the domain. Default: - TLSSecurityPolicy.TLS_1_0
        :param use_unsigned_basic_auth: Configures the domain so that unsigned basic auth is enabled. If no master user is provided a default master user with username ``admin`` and a dynamically generated password stored in KMS is created. The password can be retrieved by getting ``masterUserPassword`` from the domain instance. Setting this to true will also add an access policy that allows unsigned access, enable node to node encryption, encryption at rest. If conflicting settings are encountered (like disabling encryption at rest) enabling this setting will cause a failure. Default: - false
        :param vpc: Place the domain inside this VPC. Default: - Domain is not placed in a VPC.
        :param vpc_subnets: The specific vpc subnets the domain will be placed in. You must provide one subnet for each Availability Zone that your domain uses. For example, you must specify three subnet IDs for a three Availability Zone domain. Only used if ``vpc`` is specified. Default: - All private subnets.
        :param zone_awareness: The cluster zone awareness configuration for the Amazon OpenSearch Service domain. Default: - no zone awareness (1 AZ)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b55c263a445ddb2a2f58a555600f616a7f051ea1adc2ff24d3c1b949f77adea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DomainProps(
            version=version,
            access_policies=access_policies,
            advanced_options=advanced_options,
            automated_snapshot_start_hour=automated_snapshot_start_hour,
            capacity=capacity,
            cognito_dashboards_auth=cognito_dashboards_auth,
            cold_storage_enabled=cold_storage_enabled,
            custom_endpoint=custom_endpoint,
            domain_name=domain_name,
            ebs=ebs,
            enable_auto_software_update=enable_auto_software_update,
            enable_version_upgrade=enable_version_upgrade,
            encryption_at_rest=encryption_at_rest,
            enforce_https=enforce_https,
            fine_grained_access_control=fine_grained_access_control,
            ip_address_type=ip_address_type,
            logging=logging,
            node_to_node_encryption=node_to_node_encryption,
            off_peak_window_enabled=off_peak_window_enabled,
            off_peak_window_start=off_peak_window_start,
            removal_policy=removal_policy,
            security_groups=security_groups,
            suppress_logs_resource_policy=suppress_logs_resource_policy,
            tls_security_policy=tls_security_policy,
            use_unsigned_basic_auth=use_unsigned_basic_auth,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            zone_awareness=zone_awareness,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDomainAttributes")
    @builtins.classmethod
    def from_domain_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_arn: builtins.str,
        domain_endpoint: builtins.str,
    ) -> IDomain:
        '''Creates a domain construct that represents an external domain.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param domain_arn: The ARN of the Amazon OpenSearch Service domain.
        :param domain_endpoint: The domain endpoint of the Amazon OpenSearch Service domain.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6ffa71310423abeed383c9f52ba32bb0fa317ad14f132816245815b3e940310)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = DomainAttributes(
            domain_arn=domain_arn, domain_endpoint=domain_endpoint
        )

        return typing.cast(IDomain, jsii.sinvoke(cls, "fromDomainAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromDomainEndpoint")
    @builtins.classmethod
    def from_domain_endpoint(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        domain_endpoint: builtins.str,
    ) -> IDomain:
        '''Creates a domain construct that represents an external domain via domain endpoint.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param domain_endpoint: The domain's endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4120385867c55130a3cf133cb8085f5cefe334d66a5d6e70d3e9e9418245d08)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain_endpoint", value=domain_endpoint, expected_type=type_hints["domain_endpoint"])
        return typing.cast(IDomain, jsii.sinvoke(cls, "fromDomainEndpoint", [scope, id, domain_endpoint]))

    @jsii.member(jsii_name="addAccessPolicies")
    def add_access_policies(
        self,
        *access_policy_statements: _PolicyStatement_0fe33853,
    ) -> None:
        '''Add policy statements to the domain access policy.

        :param access_policy_statements: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b574b4a514e3bb203cffb9ddd5209b2b2a01ce79dc36360161e899511707241)
            check_type(argname="argument access_policy_statements", value=access_policy_statements, expected_type=typing.Tuple[type_hints["access_policy_statements"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addAccessPolicies", [*access_policy_statements]))

    @jsii.member(jsii_name="grantIndexRead")
    def grant_index_read(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c17a1b5f2df8ec5a2fbde2e82d834e9e1b50beea702cbb05d271229424738353)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexRead", [index, identity]))

    @jsii.member(jsii_name="grantIndexReadWrite")
    def grant_index_read_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e5c489ad7012b9bc81a711bc734d7e0782fc54f9027a928d5dcecc0f5f9a5cd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexReadWrite", [index, identity]))

    @jsii.member(jsii_name="grantIndexWrite")
    def grant_index_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12e3d51a1fcb874e85363acb5e8f0dbd4d4cfaf3ecab7e205a09b56b62f5cfb9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexWrite", [index, identity]))

    @jsii.member(jsii_name="grantPathRead")
    def grant_path_read(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b65bb1298d94b6f4088f13d08e6ce44ee6510750e19ada7afcdc19f34d811c3)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathRead", [path, identity]))

    @jsii.member(jsii_name="grantPathReadWrite")
    def grant_path_read_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c1b795776f466d929f266cb75cc2986ee3561aab1dd23fb27d4d8804261a3e1)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathReadWrite", [path, identity]))

    @jsii.member(jsii_name="grantPathWrite")
    def grant_path_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fe8266b2ff4c33565a7997602913043cc928b6eea646853e875600e42a903d)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathWrite", [path, identity]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b96664d302cdbc2c0ca76918ba82604a1ae24a6a91a3c254fbb0bfcbe9cdf81)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [identity]))

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read/write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92539b4ce708945aca7b9c15b640902718548cbad21caf4c3c3a9fd778873d8b)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantReadWrite", [identity]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6f47f51e3eed25d674651e29b33fb23e5edd9d7efd2f0b81fc604ddaaa7a711)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [identity]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this domain.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6380e234537911c13695e16580579ea3144cdf17f001286bfce646a753cc3d3)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricAutomatedSnapshotFailure")
    def metric_automated_snapshot_failure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for automated snapshot failures.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricAutomatedSnapshotFailure", [props]))

    @jsii.member(jsii_name="metricClusterIndexWritesBlocked")
    def metric_cluster_index_writes_blocked(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the cluster blocking index writes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 1 minute
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricClusterIndexWritesBlocked", [props]))

    @jsii.member(jsii_name="metricClusterStatusRed")
    def metric_cluster_status_red(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the time the cluster status is red.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricClusterStatusRed", [props]))

    @jsii.member(jsii_name="metricClusterStatusYellow")
    def metric_cluster_status_yellow(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the time the cluster status is yellow.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricClusterStatusYellow", [props]))

    @jsii.member(jsii_name="metricCPUUtilization")
    def metric_cpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricCPUUtilization", [props]))

    @jsii.member(jsii_name="metricFreeStorageSpace")
    def metric_free_storage_space(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the storage space of nodes in the cluster.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFreeStorageSpace", [props]))

    @jsii.member(jsii_name="metricIndexingLatency")
    def metric_indexing_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for indexing latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricIndexingLatency", [props]))

    @jsii.member(jsii_name="metricJVMMemoryPressure")
    def metric_jvm_memory_pressure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricJVMMemoryPressure", [props]))

    @jsii.member(jsii_name="metricKMSKeyError")
    def metric_kms_key_error(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for KMS key errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricKMSKeyError", [props]))

    @jsii.member(jsii_name="metricKMSKeyInaccessible")
    def metric_kms_key_inaccessible(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for KMS key being inaccessible.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricKMSKeyInaccessible", [props]))

    @jsii.member(jsii_name="metricMasterCPUUtilization")
    def metric_master_cpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for master CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricMasterCPUUtilization", [props]))

    @jsii.member(jsii_name="metricMasterJVMMemoryPressure")
    def metric_master_jvm_memory_pressure(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for master JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricMasterJVMMemoryPressure", [props]))

    @jsii.member(jsii_name="metricNodes")
    def metric_nodes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of nodes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 1 hour
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNodes", [props]))

    @jsii.member(jsii_name="metricSearchableDocuments")
    def metric_searchable_documents(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for number of searchable documents.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSearchableDocuments", [props]))

    @jsii.member(jsii_name="metricSearchLatency")
    def metric_search_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for search latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSearchLatency", [props]))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_0f31fce8:
        '''Manages network connections to the domain.

        This will throw an error in case the domain
        is not placed inside a VPC.
        '''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> builtins.str:
        '''Arn of the Amazon OpenSearch Service domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainArn"))

    @builtins.property
    @jsii.member(jsii_name="domainEndpoint")
    def domain_endpoint(self) -> builtins.str:
        '''Endpoint of the Amazon OpenSearch Service domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        '''Identifier of the Amazon OpenSearch Service domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''Domain name of the Amazon OpenSearch Service domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @builtins.property
    @jsii.member(jsii_name="appLogGroup")
    def app_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log group that application logs are logged to.

        :attribute: true
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "appLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="auditLogGroup")
    def audit_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log group that audit logs are logged to.

        :attribute: true
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "auditLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> typing.Optional[_SecretValue_3dd0ddae]:
        '''Master user password if fine grained access control is configured.'''
        return typing.cast(typing.Optional[_SecretValue_3dd0ddae], jsii.get(self, "masterUserPassword"))

    @builtins.property
    @jsii.member(jsii_name="slowIndexLogGroup")
    def slow_index_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log group that slow indices are logged to.

        :attribute: true
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "slowIndexLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="slowSearchLogGroup")
    def slow_search_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log group that slow searches are logged to.

        :attribute: true
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "slowSearchLogGroup"))


__all__ = [
    "AdvancedSecurityOptions",
    "CapacityConfig",
    "CfnDomain",
    "CfnDomainProps",
    "CognitoOptions",
    "CustomEndpointOptions",
    "Domain",
    "DomainAttributes",
    "DomainProps",
    "EbsOptions",
    "EncryptionAtRestOptions",
    "EngineVersion",
    "IDomain",
    "IpAddressType",
    "LoggingOptions",
    "SAMLOptionsProperty",
    "TLSSecurityPolicy",
    "WindowStartTime",
    "ZoneAwarenessConfig",
]

publication.publish()

def _typecheckingstub__c1e95392d4761126042f2d6d6160889a80c269d2f13c21476fe92febdb7f04e3(
    *,
    master_user_arn: typing.Optional[builtins.str] = None,
    master_user_name: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[_SecretValue_3dd0ddae] = None,
    saml_authentication_enabled: typing.Optional[builtins.bool] = None,
    saml_authentication_options: typing.Optional[typing.Union[SAMLOptionsProperty, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48cdec23c4ecd3d168ddd937e9295b924cdea583f9951d98aacce1c1c90cad71(
    *,
    data_node_instance_type: typing.Optional[builtins.str] = None,
    data_nodes: typing.Optional[jsii.Number] = None,
    master_node_instance_type: typing.Optional[builtins.str] = None,
    master_nodes: typing.Optional[jsii.Number] = None,
    multi_az_with_standby_enabled: typing.Optional[builtins.bool] = None,
    warm_instance_type: typing.Optional[builtins.str] = None,
    warm_nodes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fcd2545392b3f48f314c640881e38e167b5936f1165d2eb1ce21766d3db5770(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_policies: typing.Any = None,
    advanced_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    advanced_security_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.AdvancedSecurityOptionsInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cluster_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ClusterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cognito_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.CognitoOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    domain_endpoint_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.DomainEndpointOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_name: typing.Optional[builtins.str] = None,
    ebs_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EBSOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_at_rest_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EncryptionAtRestOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    engine_version: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.LogPublishingOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    node_to_node_encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.NodeToNodeEncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    off_peak_window_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.OffPeakWindowOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snapshot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SnapshotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    software_update_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SoftwareUpdateOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.VPCOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36055c1f3a4932ba1e8f0542c29f5149d636738c30a3d9d1bdafb864d00f2e64(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82c494c700f6860a942b3abd6b86cf929f307e898357419f56692f0b4084c2a5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5300173c129717cc6b181e91e5685dc6f63810f40281dca8b4c3a64113df8f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a8bbf96e0583433dd9f44c7bc58405687275c5e3102497c3de8597470024609(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__228f471e13ce4e3daa56e3913f7b610971afccf6ec06adc08af42a85ad0abde9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.AdvancedSecurityOptionsInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa86e4bef09a3455a33af8fe1a0310646154d89f5113370b517cfbe529c69080(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.ClusterConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3653fa5c99276b72d7f6127ab8c7a58e79d65fa1bb3870a642aae948411169(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.CognitoOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3136cec5fb1c8bfbc63aa354d269746af30bf8ace2a1386b3c54154aef71642(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af44788b6e909cca8e8e5c9cb554dda8dc1f217fe434e42fd8738b0f0636804e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.DomainEndpointOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fbf0bdf5087e279e6006801d40e67891ae239f2249b16c7c14ce58bd2d0e85e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c4377e2450f1c3438e90e2429bf9650c6490320abe0c622e2a80734761fec52(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EBSOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2b92e6c487faf5299f3c6d1f31ea619c1b1d93925b6634dfc0b81cde67cf89(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EncryptionAtRestOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88301df742e18b9ab560ac04b99b966a761eeee663731308b40ab8ca4cd509f1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15de3b6bee67c94e6a9ff942356ecb4f67771482ab0d1655f673b885868135c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad842d30b972e4535042c97d9a43923a473c809de18faef95c075764d365933(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDomain.LogPublishingOptionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0a25ab3a544c4d8cceb480a502adf178ccdbe1d5fdc2273557e28bb2a3b65a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.NodeToNodeEncryptionOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a3a2b200397209bed0a90cb39485a3ccb08bcbb3d56bbecc1ef0b66b5d0e9c4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.OffPeakWindowOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4355f39393b86da5d9d2bb3c03113864e6a1293ce3a4a9b21ccbc2f55009520a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SnapshotOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8acae61e3be2830b5d0094ea6fec133fbcd21857779bf3d47fd39615ad0e27eb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SoftwareUpdateOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__492b192acd9acaa788b5501251071046e08d3e3cb47dc8fe653c58c5857dbc08(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b93b8c5b5730096cbd511fb71c9b9508cb307bcbfee46f7a0c11da785c33d2e8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.VPCOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd5c3c68239a044600ab387ec52e22ed8852c6e213d5626aa4396b28aab3af9e(
    *,
    anonymous_auth_disable_date: typing.Optional[builtins.str] = None,
    anonymous_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    master_user_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.MasterUserOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    saml_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SAMLOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aeae3d5b66cfdff675e691ae3d90b2e82990d0dc2a13a8fbab733bba4e26eda(
    *,
    cold_storage_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ColdStorageOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dedicated_master_count: typing.Optional[jsii.Number] = None,
    dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    dedicated_master_type: typing.Optional[builtins.str] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    instance_type: typing.Optional[builtins.str] = None,
    multi_az_with_standby_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    warm_count: typing.Optional[jsii.Number] = None,
    warm_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    warm_type: typing.Optional[builtins.str] = None,
    zone_awareness_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ZoneAwarenessConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e167c0d00635fad84f1646761ab6a47124b645d9a98a38bc74beb3d2ecbca1c2(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    identity_pool_id: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    user_pool_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3864a36f4132782987b173c24fdcbec6040683b2f632146b11bb53578fc274f(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1afb3f072b83950253cff17b0d6c2d24505ec14925f8f1b645dd5c539c2ca4d(
    *,
    custom_endpoint: typing.Optional[builtins.str] = None,
    custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
    custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enforce_https: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tls_security_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0edcf62ab77376e080d4b111ffdeee55bda3d1ea1c392a1acb86f78ce234e31b(
    *,
    ebs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8045e71bf2b9389f7b778b391167aea3cf2ff9b7ccd6b9462c26cc1dcd4f9cbc(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df207d57c5bf0c99afe86b2563e40142d554f359eddff25bfecdf22c97a3ed72(
    *,
    entity_id: builtins.str,
    metadata_content: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f619e98a16faa2be95396251f0c046225b41dc39039c1064a235021c6127a509(
    *,
    cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d898e88f61289087d3cdae775ccfc96a5810d38fd1a901ddd469c8377d40e163(
    *,
    master_user_arn: typing.Optional[builtins.str] = None,
    master_user_name: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbea990af8e11f12ced7e27d027040c8ec8f64ffa1f9d71f254282114946ea92(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d60226ff032c6e6c2d237e050aa8d3a58b6a67c4b5e0bdb59300620e1b4ad6(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    off_peak_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.OffPeakWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d779e62b9e7bc4d33e575c2c20d7da26b34d1299cff8c0f1810cd484dc86e3(
    *,
    window_start_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.WindowStartTimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5e21e3867bc5223d95d43002facac59aeb4bf08a5eb92c2adf7498d4b99a166(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    idp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.IdpProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    master_backend_role: typing.Optional[builtins.str] = None,
    master_user_name: typing.Optional[builtins.str] = None,
    roles_key: typing.Optional[builtins.str] = None,
    session_timeout_minutes: typing.Optional[jsii.Number] = None,
    subject_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17b60fc8205546d1616e28c359a0065b932fe65e39fe26c0c36bf78a39640570(
    *,
    automated_update_date: typing.Optional[builtins.str] = None,
    cancellable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    current_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    new_version: typing.Optional[builtins.str] = None,
    optional_deployment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    update_available: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    update_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36321f8809b3e46d31ad2079d9c9a47da5cdee345f411bb1e57bf166897c2d1c(
    *,
    automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5b07fb34bad0710947f07e46bcb56c9b4dde81217ab11372e2037cc7ecc912(
    *,
    auto_software_update_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b5e509f3eeacdd0fd9d933797c926acbd5e00cdfca76bc715ee89c0ba33d541(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6090d0f7ef0a5ff38223c37e3fded0a822e4e3052cd46ba0b2430b408bd5f698(
    *,
    hours: jsii.Number,
    minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__256b4aabbc2391aa4f2b7e2d1c28804fdc91f3e9c7c213de20cc38a33dc255b2(
    *,
    availability_zone_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a3bbf8db74762f8d49d2ee572e0b31eef8650964dd0e8a168a5fe2d67607c52(
    *,
    access_policies: typing.Any = None,
    advanced_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    advanced_security_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.AdvancedSecurityOptionsInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cluster_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ClusterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cognito_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.CognitoOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    domain_endpoint_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.DomainEndpointOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_name: typing.Optional[builtins.str] = None,
    ebs_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EBSOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_at_rest_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EncryptionAtRestOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    engine_version: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.LogPublishingOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    node_to_node_encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.NodeToNodeEncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    off_peak_window_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.OffPeakWindowOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snapshot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SnapshotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    software_update_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SoftwareUpdateOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.VPCOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac57cf9250cdb4adb2c04b922ca15a9a5d18b8e118cff3f08ab7d1171f1fcd9(
    *,
    identity_pool_id: builtins.str,
    role: _IRole_235f5d8e,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bfcfb0c951977f30c9119dd53a7307c78b4a3185828104fe4e4d17628ef7d24(
    *,
    domain_name: builtins.str,
    certificate: typing.Optional[_ICertificate_c194c70b] = None,
    hosted_zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b64144592f37187baf13886dda52519ca86792e6e902692955529605957265b3(
    *,
    domain_arn: builtins.str,
    domain_endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0435b5d94950ff07269642dd229e13535b70e6b92e19fbea5906bff08927fa74(
    *,
    version: EngineVersion,
    access_policies: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
    capacity: typing.Optional[typing.Union[CapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    cognito_dashboards_auth: typing.Optional[typing.Union[CognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cold_storage_enabled: typing.Optional[builtins.bool] = None,
    custom_endpoint: typing.Optional[typing.Union[CustomEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[EbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_auto_software_update: typing.Optional[builtins.bool] = None,
    enable_version_upgrade: typing.Optional[builtins.bool] = None,
    encryption_at_rest: typing.Optional[typing.Union[EncryptionAtRestOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enforce_https: typing.Optional[builtins.bool] = None,
    fine_grained_access_control: typing.Optional[typing.Union[AdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ip_address_type: typing.Optional[IpAddressType] = None,
    logging: typing.Optional[typing.Union[LoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    node_to_node_encryption: typing.Optional[builtins.bool] = None,
    off_peak_window_enabled: typing.Optional[builtins.bool] = None,
    off_peak_window_start: typing.Optional[typing.Union[WindowStartTime, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    suppress_logs_resource_policy: typing.Optional[builtins.bool] = None,
    tls_security_policy: typing.Optional[TLSSecurityPolicy] = None,
    use_unsigned_basic_auth: typing.Optional[builtins.bool] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
    zone_awareness: typing.Optional[typing.Union[ZoneAwarenessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__388b3ff533950547aa29493d027ac01b8d3d4139dc5061e4f70a2cf8e0912d38(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[_EbsDeviceVolumeType_6792555b] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5973f04ac98b9a2d9bddce35a01a16416d58b7f8a10bd553cfabe3909eb2523(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    kms_key: typing.Optional[_IKey_5f11635f] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9ff089c138ae673bd34470711323158868e600ef582eaf1138c7dbfabe659d(
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e4e60eeb3f3de1852dda34e9fc12006c90072b2af1169917137b26002e7ca6b(
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a94e154ecf4f9073f5d7c9e1ea7e03f69da172094fa85d76ced59ad241b1fb2(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e57d957edccc649ee25aa5e026d1e4a380aefa1fca47ac85fb2332017684c2d(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e11c5bfffab0ceb5f6e6d11d8c2422feb5ca967394bcd5e0f9cf0f2979cfac0(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__023ad84c0e882f65c76fb064e82ff3cd67cfa07f593f45818a1a2c9c03688dbb(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bc2ab50330adaac8ffebc655effda16c72446686a9b26d8c09644e3cde524f5(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__402463dfcfddcd6aaa36a0ec13a1628f29914c911b19e66e17d3cc38b5661762(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d29656876fe4553e567e59a1a0cbb6942145d5715c6aec2bdba4c0524ce284f(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99698755eef9bf19abbfc958ee11633e093e93f46c5c5f99f45308fa7212f08b(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599ff214d878684eadaa975bf3d8bf19930fc28a8788cab7625b3a913e0975e1(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed477ecf16b0f23884f9eb3a0a90df530d2486e08c8dd662432a14ff4837bd08(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f2efbcf1fc757504a748851740a44deb59ed98ee9c1d8c213d60960f900a593(
    *,
    app_log_enabled: typing.Optional[builtins.bool] = None,
    app_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    audit_log_enabled: typing.Optional[builtins.bool] = None,
    audit_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    slow_index_log_enabled: typing.Optional[builtins.bool] = None,
    slow_index_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    slow_search_log_enabled: typing.Optional[builtins.bool] = None,
    slow_search_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3971b3c73627d57587c667b1ede64fbba4de4fd4a086af959dc2d0f812f8e36b(
    *,
    idp_entity_id: builtins.str,
    idp_metadata_content: builtins.str,
    master_backend_role: typing.Optional[builtins.str] = None,
    master_user_name: typing.Optional[builtins.str] = None,
    roles_key: typing.Optional[builtins.str] = None,
    session_timeout_minutes: typing.Optional[jsii.Number] = None,
    subject_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa10c95f5a58e650c77a0c42630f2fa77e6475974ad59138caebb586e5fad2c(
    *,
    hours: jsii.Number,
    minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d25db0248db5c13d8d8371728510a20f1632b4180af6f40e9838b4d28d6a375d(
    *,
    availability_zone_count: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b55c263a445ddb2a2f58a555600f616a7f051ea1adc2ff24d3c1b949f77adea(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    version: EngineVersion,
    access_policies: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
    capacity: typing.Optional[typing.Union[CapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    cognito_dashboards_auth: typing.Optional[typing.Union[CognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cold_storage_enabled: typing.Optional[builtins.bool] = None,
    custom_endpoint: typing.Optional[typing.Union[CustomEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[EbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_auto_software_update: typing.Optional[builtins.bool] = None,
    enable_version_upgrade: typing.Optional[builtins.bool] = None,
    encryption_at_rest: typing.Optional[typing.Union[EncryptionAtRestOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enforce_https: typing.Optional[builtins.bool] = None,
    fine_grained_access_control: typing.Optional[typing.Union[AdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ip_address_type: typing.Optional[IpAddressType] = None,
    logging: typing.Optional[typing.Union[LoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    node_to_node_encryption: typing.Optional[builtins.bool] = None,
    off_peak_window_enabled: typing.Optional[builtins.bool] = None,
    off_peak_window_start: typing.Optional[typing.Union[WindowStartTime, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    suppress_logs_resource_policy: typing.Optional[builtins.bool] = None,
    tls_security_policy: typing.Optional[TLSSecurityPolicy] = None,
    use_unsigned_basic_auth: typing.Optional[builtins.bool] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
    zone_awareness: typing.Optional[typing.Union[ZoneAwarenessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ffa71310423abeed383c9f52ba32bb0fa317ad14f132816245815b3e940310(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_arn: builtins.str,
    domain_endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4120385867c55130a3cf133cb8085f5cefe334d66a5d6e70d3e9e9418245d08(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    domain_endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b574b4a514e3bb203cffb9ddd5209b2b2a01ce79dc36360161e899511707241(
    *access_policy_statements: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c17a1b5f2df8ec5a2fbde2e82d834e9e1b50beea702cbb05d271229424738353(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e5c489ad7012b9bc81a711bc734d7e0782fc54f9027a928d5dcecc0f5f9a5cd(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12e3d51a1fcb874e85363acb5e8f0dbd4d4cfaf3ecab7e205a09b56b62f5cfb9(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b65bb1298d94b6f4088f13d08e6ce44ee6510750e19ada7afcdc19f34d811c3(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c1b795776f466d929f266cb75cc2986ee3561aab1dd23fb27d4d8804261a3e1(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fe8266b2ff4c33565a7997602913043cc928b6eea646853e875600e42a903d(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b96664d302cdbc2c0ca76918ba82604a1ae24a6a91a3c254fbb0bfcbe9cdf81(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92539b4ce708945aca7b9c15b640902718548cbad21caf4c3c3a9fd778873d8b(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6f47f51e3eed25d674651e29b33fb23e5edd9d7efd2f0b81fc604ddaaa7a711(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6380e234537911c13695e16580579ea3144cdf17f001286bfce646a753cc3d3(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass
