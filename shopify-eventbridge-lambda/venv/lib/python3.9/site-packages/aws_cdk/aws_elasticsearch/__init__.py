'''
# Amazon OpenSearch Service Construct Library

> Instead of this module, we recommend using the [aws-cdk-lib/aws-opensearchservice](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_opensearchservice-readme.html) module. See [Amazon OpenSearch Service FAQs](https://aws.amazon.com/opensearch-service/faqs/#Name_change) for details. See [Migrating to OpenSearch](#migrating-to-opensearch) for migration instructions.

## Quick start

Create a development cluster by simply specifying the version:

```python
dev_domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_1
)
```

To perform version upgrades without replacing the entire domain, specify the `enableVersionUpgrade` property.

```python
dev_domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_10,
    enable_version_upgrade=True
)
```

Create a production grade cluster by also specifying things like capacity and az distribution

```python
prod_domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_1,
    capacity=es.CapacityConfig(
        master_nodes=5,
        data_nodes=20
    ),
    ebs=es.EbsOptions(
        volume_size=20
    ),
    zone_awareness=es.ZoneAwarenessConfig(
        availability_zone_count=3
    ),
    logging=es.LoggingOptions(
        slow_search_log_enabled=True,
        app_log_enabled=True,
        slow_index_log_enabled=True
    )
)
```

This creates an Elasticsearch cluster and automatically sets up log groups for
logging the domain logs and slow search logs.

## A note about SLR

Some cluster configurations (e.g VPC access) require the existence of the [`AWSServiceRoleForAmazonElasticsearchService`](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html) service-linked role.

When performing such operations via the AWS Console, this SLR is created automatically when needed. However, this is not the behavior when using CloudFormation. If an SLR is needed, but doesn't exist, you will encounter a failure message similar to:

```console
Before you can proceed, you must enable a service-linked role to give Amazon ES...
```

To resolve this, you need to [create](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) the SLR. We recommend using the AWS CLI:

```console
aws iam create-service-linked-role --aws-service-name es.amazonaws.com
```

You can also create it using the CDK, **but note that only the first application deploying this will succeed**:

```python
slr = iam.CfnServiceLinkedRole(self, "ElasticSLR",
    aws_service_name="es.amazonaws.com"
)
```

## Importing existing domains

To import an existing domain into your CDK application, use the `Domain.fromDomainEndpoint` factory method.
This method accepts a domain endpoint of an already existing domain:

```python
domain_endpoint = "https://my-domain-jcjotrt6f7otem4sqcwbch3c4u.us-east-1.es.amazonaws.com"
domain = es.Domain.from_domain_endpoint(self, "ImportedDomain", domain_endpoint)
```

## Permissions

### IAM

Helper methods also exist for managing access to the domain.

```python
# fn: lambda.Function
# domain: es.Domain


# Grant write access to the app-search index
domain.grant_index_write("app-search", fn)

# Grant read access to the 'app-search/_search' path
domain.grant_path_read("app-search/_search", fn)
```

## Encryption

The domain can also be created with encryption enabled:

```python
domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_4,
    ebs=es.EbsOptions(
        volume_size=100,
        volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
    ),
    node_to_node_encryption=True,
    encryption_at_rest=es.EncryptionAtRestOptions(
        enabled=True
    )
)
```

This sets up the domain with node to node encryption and encryption at
rest. You can also choose to supply your own KMS key to use for encryption at
rest.

## VPC Support

Elasticsearch domains can be placed inside a VPC, providing a secure communication between Amazon ES and other services within the VPC without the need for an internet gateway, NAT device, or VPN connection.

> See [Launching your Amazon OpenSearch Service domains within a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html) for more details.

```python
vpc = ec2.Vpc(self, "Vpc")
domain_props = es.DomainProps(
    version=es.ElasticsearchVersion.V7_1,
    removal_policy=RemovalPolicy.DESTROY,
    vpc=vpc,
    # must be enabled since our VPC contains multiple private subnets.
    zone_awareness=es.ZoneAwarenessConfig(
        enabled=True
    ),
    capacity=es.CapacityConfig(
        # must be an even number since the default az count is 2.
        data_nodes=2
    )
)
es.Domain(self, "Domain", domain_props)
```

In addition, you can use the `vpcSubnets` property to control which specific subnets will be used, and the `securityGroups` property to control
which security groups will be attached to the domain. By default, CDK will select all *private* subnets in the VPC, and create one dedicated security group.

## Metrics

Helper methods exist to access common domain metrics for example:

```python
# domain: es.Domain

free_storage_space = domain.metric_free_storage_space()
master_sys_memory_utilization = domain.metric("MasterSysMemoryUtilization")
```

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Fine grained access control

The domain can also be created with a master user configured. The password can
be supplied or dynamically created if not supplied.

```python
domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_1,
    enforce_https=True,
    node_to_node_encryption=True,
    encryption_at_rest=es.EncryptionAtRestOptions(
        enabled=True
    ),
    fine_grained_access_control=es.AdvancedSecurityOptions(
        master_user_name="master-user"
    )
)

master_user_password = domain.master_user_password
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
domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_1,
    use_unsigned_basic_auth=True
)

master_user_password = domain.master_user_password
```

## Custom access policies

If the domain requires custom access control it can be configured either as a
constructor property, or later by means of a helper method.

For simple permissions the `accessPolicies` constructor may be sufficient:

```python
domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_1,
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
domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_1
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

Audit logs can be enabled for a domain, but only when fine-grained access control is enabled.

```python
domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_1,
    enforce_https=True,
    node_to_node_encryption=True,
    encryption_at_rest=es.EncryptionAtRestOptions(
        enabled=True
    ),
    fine_grained_access_control=es.AdvancedSecurityOptions(
        master_user_name="master-user"
    ),
    logging=es.LoggingOptions(
        audit_log_enabled=True,
        slow_search_log_enabled=True,
        app_log_enabled=True,
        slow_index_log_enabled=True
    )
)
```

## UltraWarm

UltraWarm nodes can be enabled to provide a cost-effective way to store large amounts of read-only data.

```python
domain = es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_10,
    capacity=es.CapacityConfig(
        master_nodes=2,
        warm_nodes=2,
        warm_instance_type="ultrawarm1.medium.elasticsearch"
    )
)
```

## Custom endpoint

Custom endpoints can be configured to reach the ES domain under a custom domain name.

```python
es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_7,
    custom_endpoint=es.CustomEndpointOptions(
        domain_name="search.example.com"
    )
)
```

It is also possible to specify a custom certificate instead of the auto-generated one.

Additionally, an automatic CNAME-Record is created if a hosted zone is provided for the custom endpoint

## Advanced options

[Advanced cluster settings](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options) can used to configure additional options.

```python
es.Domain(self, "Domain",
    version=es.ElasticsearchVersion.V7_7,
    advanced_options={
        "rest.action.multi.allow_explicit_index": "false",
        "indices.fielddata.cache.size": "25",
        "indices.query.bool.max_clause_count": "2048"
    }
)
```

## Migrating to OpenSearch

To migrate from this module (`aws-cdk-lib/aws-elasticsearch`) to the new `aws-cdk-lib/aws-opensearchservice` module, you must modify your CDK application to refer to the new module (including some associated changes) and then perform a CloudFormation resource deletion/import.

### Necessary CDK Modifications

Make the following modifications to your CDK application to migrate to the `aws-cdk-lib/aws-opensearchservice` module.

* Rewrite module imports to use `'aws-cdk-lib/aws-opensearchservice` to `'aws-cdk-lib/aws-elasticsearch`.
  For example:

  ```python
  import aws_cdk.aws_elasticsearch as es
  from aws_cdk.aws_elasticsearch import Domain
  ```

  ...becomes...

  ```python
  import aws_cdk.aws_opensearchservice as opensearch
  from aws_cdk.aws_opensearchservice import Domain
  ```
* Replace instances of `es.ElasticsearchVersion` with `opensearch.EngineVersion`.
  For example:

  ```python
  version = es.ElasticsearchVersion.V7_1
  ```

  ...becomes...

  ```python
  version = opensearch.EngineVersion.ELASTICSEARCH_7_1
  ```
* Replace the `cognitoKibanaAuth` property of `DomainProps` with `cognitoDashboardsAuth`.
  For example:

  ```python
  es.Domain(self, "Domain",
      cognito_kibana_auth=es.CognitoOptions(
          identity_pool_id="test-identity-pool-id",
          user_pool_id="test-user-pool-id",
          role=role
      ),
      version=elasticsearch_version
  )
  ```

  ...becomes...

  ```python
  opensearch.Domain(self, "Domain",
      cognito_dashboards_auth=opensearch.CognitoOptions(
          identity_pool_id="test-identity-pool-id",
          user_pool_id="test-user-pool-id",
          role=role
      ),
      version=open_search_version
  )
  ```
* Rewrite instance type suffixes from `.elasticsearch` to `.search`.
  For example:

  ```python
  es.Domain(self, "Domain",
      capacity=es.CapacityConfig(
          master_node_instance_type="r5.large.elasticsearch"
      ),
      version=elasticsearch_version
  )
  ```

  ...becomes...

  ```python
  opensearch.Domain(self, "Domain",
      capacity=opensearch.CapacityConfig(
          master_node_instance_type="r5.large.search"
      ),
      version=open_search_version
  )
  ```
* Any `CfnInclude`'d domains will need to be re-written in their original template in
  order to be successfully included as a `opensearch.CfnDomain`

### CloudFormation Migration

Follow these steps to migrate your application without data loss:

* Ensure that the [removal policy](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_core.RemovalPolicy.html) on your domains are set to `RemovalPolicy.RETAIN`. This is the default for the domain construct, so nothing is required unless you have specifically set the removal policy to some other value.
* Remove the domain resource from your CloudFormation stacks by manually modifying the synthesized templates used to create the CloudFormation stacks. This may also involve modifying or deleting dependent resources, such as the custom resources that CDK creates to manage the domain's access policy or any other resource you have connected to the domain. You will need to search for references to each domain's logical ID to determine which other resources refer to it and replace or delete those references. Do not remove resources that are dependencies of the domain or you will have to recreate or import them before importing the domain. After modification, deploy the stacks through the AWS Management Console or using the AWS CLI.
* Migrate your CDK application to use the new `aws-cdk-lib/aws-opensearchservice` module by applying the necessary modifications listed above. Synthesize your application and obtain the resulting stack templates.
* Copy just the definition of the domain from the "migrated" templates to the corresponding "stripped" templates that you deployed above. [Import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-existing-stack.html) the orphaned domains into your CloudFormation stacks using these templates.
* Synthesize and deploy your CDK application to reconfigure/recreate the modified dependent resources. The CloudFormation stacks should now contain the same resources as existed prior to migration.
* Proceed with development as normal!
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.AdvancedSecurityOptions",
    jsii_struct_bases=[],
    name_mapping={
        "master_user_arn": "masterUserArn",
        "master_user_name": "masterUserName",
        "master_user_password": "masterUserPassword",
    },
)
class AdvancedSecurityOptions:
    def __init__(
        self,
        *,
        master_user_arn: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[_SecretValue_3dd0ddae] = None,
    ) -> None:
        '''(deprecated) Specifies options for fine-grained access control.

        :param master_user_arn: (deprecated) ARN for the master user. Only specify this or masterUserName, but not both. Default: - fine-grained access control is disabled
        :param master_user_name: (deprecated) Username for the master user. Only specify this or masterUserArn, but not both. Default: - fine-grained access control is disabled
        :param master_user_password: (deprecated) Password for the master user. You can use ``SecretValue.unsafePlainText`` to specify a password in plain text or use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in Secrets Manager. Default: - A Secrets Manager generated password

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            domain = es.Domain(self, "Domain",
                version=es.ElasticsearchVersion.V7_1,
                enforce_https=True,
                node_to_node_encryption=True,
                encryption_at_rest=es.EncryptionAtRestOptions(
                    enabled=True
                ),
                fine_grained_access_control=es.AdvancedSecurityOptions(
                    master_user_name="master-user"
                )
            )
            
            master_user_password = domain.master_user_password
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc9b40ba6fb43b768fc771b2453634a195e8312344879b8f85c37c34d026712)
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
        '''(deprecated) ARN for the master user.

        Only specify this or masterUserName, but not both.

        :default: - fine-grained access control is disabled

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("master_user_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Username for the master user.

        Only specify this or masterUserArn, but not both.

        :default: - fine-grained access control is disabled

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("master_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[_SecretValue_3dd0ddae]:
        '''(deprecated) Password for the master user.

        You can use ``SecretValue.unsafePlainText`` to specify a password in plain text or
        use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in
        Secrets Manager.

        :default: - A Secrets Manager generated password

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[_SecretValue_3dd0ddae], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdvancedSecurityOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticsearch.CapacityConfig",
    jsii_struct_bases=[],
    name_mapping={
        "data_node_instance_type": "dataNodeInstanceType",
        "data_nodes": "dataNodes",
        "master_node_instance_type": "masterNodeInstanceType",
        "master_nodes": "masterNodes",
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
        warm_instance_type: typing.Optional[builtins.str] = None,
        warm_nodes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(deprecated) Configures the capacity of the cluster such as the instance type and the number of instances.

        :param data_node_instance_type: (deprecated) The instance type for your data nodes, such as ``m3.medium.elasticsearch``. For valid values, see `Supported Instance Types <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html>`_ in the Amazon Elasticsearch Service Developer Guide. Default: - r5.large.elasticsearch
        :param data_nodes: (deprecated) The number of data nodes (instances) to use in the Amazon ES domain. Default: - 1
        :param master_node_instance_type: (deprecated) The hardware configuration of the computer that hosts the dedicated master node, such as ``m3.medium.elasticsearch``. For valid values, see [Supported Instance Types] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html) in the Amazon Elasticsearch Service Developer Guide. Default: - r5.large.elasticsearch
        :param master_nodes: (deprecated) The number of instances to use for the master node. Default: - no dedicated master nodes
        :param warm_instance_type: (deprecated) The instance type for your UltraWarm node, such as ``ultrawarm1.medium.elasticsearch``. For valid values, see [UltraWarm Storage Limits] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-limits.html#limits-ultrawarm) in the Amazon Elasticsearch Service Developer Guide. Default: - ultrawarm1.medium.elasticsearch
        :param warm_nodes: (deprecated) The number of UltraWarm nodes (instances) to use in the Amazon ES domain. Default: - no UltraWarm nodes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            domain = es.Domain(self, "Domain",
                version=es.ElasticsearchVersion.V7_10,
                capacity=es.CapacityConfig(
                    master_nodes=2,
                    warm_nodes=2,
                    warm_instance_type="ultrawarm1.medium.elasticsearch"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d904c51cccabe441d3da72a1444303ff901ccd33acf1e26faf7fc107055a594a)
            check_type(argname="argument data_node_instance_type", value=data_node_instance_type, expected_type=type_hints["data_node_instance_type"])
            check_type(argname="argument data_nodes", value=data_nodes, expected_type=type_hints["data_nodes"])
            check_type(argname="argument master_node_instance_type", value=master_node_instance_type, expected_type=type_hints["master_node_instance_type"])
            check_type(argname="argument master_nodes", value=master_nodes, expected_type=type_hints["master_nodes"])
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
        if warm_instance_type is not None:
            self._values["warm_instance_type"] = warm_instance_type
        if warm_nodes is not None:
            self._values["warm_nodes"] = warm_nodes

    @builtins.property
    def data_node_instance_type(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The instance type for your data nodes, such as ``m3.medium.elasticsearch``. For valid values, see `Supported Instance Types <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html>`_ in the Amazon Elasticsearch Service Developer Guide.

        :default: - r5.large.elasticsearch

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("data_node_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_nodes(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) The number of data nodes (instances) to use in the Amazon ES domain.

        :default: - 1

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("data_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def master_node_instance_type(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The hardware configuration of the computer that hosts the dedicated master node, such as ``m3.medium.elasticsearch``. For valid values, see [Supported Instance Types] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html) in the Amazon Elasticsearch Service Developer Guide.

        :default: - r5.large.elasticsearch

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("master_node_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_nodes(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) The number of instances to use for the master node.

        :default: - no dedicated master nodes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("master_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warm_instance_type(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The instance type for your UltraWarm node, such as ``ultrawarm1.medium.elasticsearch``. For valid values, see [UltraWarm Storage Limits] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-limits.html#limits-ultrawarm) in the Amazon Elasticsearch Service Developer Guide.

        :default: - ultrawarm1.medium.elasticsearch

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("warm_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warm_nodes(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) The number of UltraWarm nodes (instances) to use in the Amazon ES domain.

        :default: - no UltraWarm nodes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain",
):
    '''The AWS::Elasticsearch::Domain resource creates an Amazon OpenSearch Service domain.

    .. epigraph::

       The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and legacy Elasticsearch. For instructions to upgrade domains defined within CloudFormation from Elasticsearch to OpenSearch, see `Remarks <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain--remarks>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html
    :cloudformationResource: AWS::Elasticsearch::Domain
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticsearch as elasticsearch
        
        # access_policies: Any
        
        cfn_domain = elasticsearch.CfnDomain(self, "MyCfnDomain",
            access_policies=access_policies,
            advanced_options={
                "advanced_options_key": "advancedOptions"
            },
            advanced_security_options=elasticsearch.CfnDomain.AdvancedSecurityOptionsInputProperty(
                anonymous_auth_enabled=False,
                enabled=False,
                internal_user_database_enabled=False,
                master_user_options=elasticsearch.CfnDomain.MasterUserOptionsProperty(
                    master_user_arn="masterUserArn",
                    master_user_name="masterUserName",
                    master_user_password="masterUserPassword"
                )
            ),
            cognito_options=elasticsearch.CfnDomain.CognitoOptionsProperty(
                enabled=False,
                identity_pool_id="identityPoolId",
                role_arn="roleArn",
                user_pool_id="userPoolId"
            ),
            domain_arn="domainArn",
            domain_endpoint_options=elasticsearch.CfnDomain.DomainEndpointOptionsProperty(
                custom_endpoint="customEndpoint",
                custom_endpoint_certificate_arn="customEndpointCertificateArn",
                custom_endpoint_enabled=False,
                enforce_https=False,
                tls_security_policy="tlsSecurityPolicy"
            ),
            domain_name="domainName",
            ebs_options=elasticsearch.CfnDomain.EBSOptionsProperty(
                ebs_enabled=False,
                iops=123,
                volume_size=123,
                volume_type="volumeType"
            ),
            elasticsearch_cluster_config=elasticsearch.CfnDomain.ElasticsearchClusterConfigProperty(
                cold_storage_options=elasticsearch.CfnDomain.ColdStorageOptionsProperty(
                    enabled=False
                ),
                dedicated_master_count=123,
                dedicated_master_enabled=False,
                dedicated_master_type="dedicatedMasterType",
                instance_count=123,
                instance_type="instanceType",
                warm_count=123,
                warm_enabled=False,
                warm_type="warmType",
                zone_awareness_config=elasticsearch.CfnDomain.ZoneAwarenessConfigProperty(
                    availability_zone_count=123
                ),
                zone_awareness_enabled=False
            ),
            elasticsearch_version="elasticsearchVersion",
            encryption_at_rest_options=elasticsearch.CfnDomain.EncryptionAtRestOptionsProperty(
                enabled=False,
                kms_key_id="kmsKeyId"
            ),
            log_publishing_options={
                "log_publishing_options_key": elasticsearch.CfnDomain.LogPublishingOptionProperty(
                    cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn",
                    enabled=False
                )
            },
            node_to_node_encryption_options=elasticsearch.CfnDomain.NodeToNodeEncryptionOptionsProperty(
                enabled=False
            ),
            snapshot_options=elasticsearch.CfnDomain.SnapshotOptionsProperty(
                automated_snapshot_start_hour=123
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_options=elasticsearch.CfnDomain.VPCOptionsProperty(
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
        cognito_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.CognitoOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        domain_arn: typing.Optional[builtins.str] = None,
        domain_endpoint_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.DomainEndpointOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        ebs_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.EBSOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_cluster_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ElasticsearchClusterConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_version: typing.Optional[builtins.str] = None,
        encryption_at_rest_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.EncryptionAtRestOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.LogPublishingOptionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        node_to_node_encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.NodeToNodeEncryptionOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        snapshot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.SnapshotOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.VPCOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_policies: An AWS Identity and Access Management ( IAM ) policy document that specifies who can access the OpenSearch Service domain and their permissions. For more information, see `Configuring access policies <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-creating>`_ in the *Amazon OpenSearch Service Developer Guid* e.
        :param advanced_options: Additional options to specify for the OpenSearch Service domain. For more information, see `Advanced cluster parameters <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options>`_ in the *Amazon OpenSearch Service Developer Guide* .
        :param advanced_security_options: Specifies options for fine-grained access control.
        :param cognito_options: Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.
        :param domain_arn: 
        :param domain_endpoint_options: Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.
        :param domain_name: A name for the OpenSearch Service domain. For valid values, see the `DomainName <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configuration-api.html#configuration-api-datatypes-domainname>`_ data type in the *Amazon OpenSearch Service Developer Guide* . If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the domain name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param ebs_options: The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain. For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .
        :param elasticsearch_cluster_config: ElasticsearchClusterConfig is a property of the AWS::Elasticsearch::Domain resource that configures the cluster of an Amazon OpenSearch Service domain.
        :param elasticsearch_version: The version of Elasticsearch to use, such as 2.3. If not specified, 1.5 is used as the default. For information about the versions that OpenSearch Service supports, see `Supported versions of OpenSearch and Elasticsearch <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#choosing-version>`_ in the *Amazon OpenSearch Service Developer Guide* . If you set the `EnableVersionUpgrade <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-upgradeopensearchdomain>`_ update policy to ``true`` , you can update ``ElasticsearchVersion`` without interruption. When ``EnableVersionUpgrade`` is set to ``false`` , or is not specified, updating ``ElasticsearchVersion`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param encryption_at_rest_options: Whether the domain should encrypt data at rest, and if so, the AWS Key Management Service key to use. See `Encryption of data at rest for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html>`_ .
        :param log_publishing_options: An object with one or more of the following keys: ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , ``AUDIT_LOGS`` , depending on the types of logs you want to publish. Each key needs a valid ``LogPublishingOption`` value.
        :param node_to_node_encryption_options: Specifies whether node-to-node encryption is enabled. See `Node-to-node encryption for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html>`_ .
        :param snapshot_options: *DEPRECATED* . The automated snapshot configuration for the OpenSearch Service domain indices.
        :param tags: An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Service domain.
        :param vpc_options: The virtual private cloud (VPC) configuration for the OpenSearch Service domain. For more information, see `Launching your Amazon OpenSearch Service domains within a VPC <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html>`_ in the *Amazon OpenSearch Service Developer Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63b7f3680a648547d6da1f542a01684f9c4d84033f4c9aee8eaecae81537b8f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(
            access_policies=access_policies,
            advanced_options=advanced_options,
            advanced_security_options=advanced_security_options,
            cognito_options=cognito_options,
            domain_arn=domain_arn,
            domain_endpoint_options=domain_endpoint_options,
            domain_name=domain_name,
            ebs_options=ebs_options,
            elasticsearch_cluster_config=elasticsearch_cluster_config,
            elasticsearch_version=elasticsearch_version,
            encryption_at_rest_options=encryption_at_rest_options,
            log_publishing_options=log_publishing_options,
            node_to_node_encryption_options=node_to_node_encryption_options,
            snapshot_options=snapshot_options,
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd2d18eaac7c83ff0634d3cb6e2c71e76889773e8b7a399c0dd5aa637bd6ae89)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f966c6cd4c4c0e8fc1b00589d54a432ec5b02208b1097ed5e485a3deaa1a3737)
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
        '''The Amazon Resource Name (ARN) of the domain, such as ``arn:aws:es:us-west-2:123456789012:domain/mystack-elasti-1ab2cdefghij`` .

        This returned value is the same as the one returned by ``AWS::Elasticsearch::Domain.DomainArn`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainEndpoint")
    def attr_domain_endpoint(self) -> builtins.str:
        '''The domain-specific endpoint that's used for requests to the OpenSearch APIs, such as ``search-mystack-elasti-1ab2cdefghij-ab1c2deckoyb3hofw7wpqa3cm.us-west-1.es.amazonaws.com`` .

        :cloudformationAttribute: DomainEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainEndpoint"))

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
    @jsii.member(jsii_name="accessPolicies")
    def access_policies(self) -> typing.Any:
        '''An AWS Identity and Access Management ( IAM ) policy document that specifies who can access the OpenSearch Service domain and their permissions.'''
        return typing.cast(typing.Any, jsii.get(self, "accessPolicies"))

    @access_policies.setter
    def access_policies(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e88303355599d25861730b061f1bc223b85a3768dad89b9fe895dcb0acbb018)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eccb4465105fe2d68c634cb9897defc7a979b09c5873770bdb861cc3cf9f6050)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedOptions", value)

    @builtins.property
    @jsii.member(jsii_name="advancedSecurityOptions")
    def advanced_security_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AdvancedSecurityOptionsInputProperty"]]:
        '''Specifies options for fine-grained access control.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AdvancedSecurityOptionsInputProperty"]], jsii.get(self, "advancedSecurityOptions"))

    @advanced_security_options.setter
    def advanced_security_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AdvancedSecurityOptionsInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9970ee48d4d95c4a50fba27f7ecf5d29a7799901a417a50d5ea2d80bb2a7da73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedSecurityOptions", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__ee253fc130f6145a5f54d7b09ff1166a449bd9ecc8b1142d2cd799fd8c3e8122)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cognitoOptions", value)

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainArn"))

    @domain_arn.setter
    def domain_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8adbdde3df8afce52a188616c8a9ed40b29c6c6ea3a14493572b5169a4bbcaaf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff33eeb03219f470f43d7c038ac4ad48acfa3561168de4acd90068625c223f8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__547819c192aff9b477504559c5f7c768a4e9c9606b6bcb8fed954fa8a2f967c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b92aff95c5a4b46939639f06cb47d5cb23bc8cce780233b7fed861d0a33b21b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptions", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchClusterConfig")
    def elasticsearch_cluster_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ElasticsearchClusterConfigProperty"]]:
        '''ElasticsearchClusterConfig is a property of the AWS::Elasticsearch::Domain resource that configures the cluster of an Amazon OpenSearch Service domain.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ElasticsearchClusterConfigProperty"]], jsii.get(self, "elasticsearchClusterConfig"))

    @elasticsearch_cluster_config.setter
    def elasticsearch_cluster_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ElasticsearchClusterConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02e4164981f0950c083faf5427ec43d8fa41b58062af5ea5e2be947066d05721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchClusterConfig", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchVersion")
    def elasticsearch_version(self) -> typing.Optional[builtins.str]:
        '''The version of Elasticsearch to use, such as 2.3. If not specified, 1.5 is used as the default. For information about the versions that OpenSearch Service supports, see `Supported versions of OpenSearch and Elasticsearch <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#choosing-version>`_ in the *Amazon OpenSearch Service Developer Guide* .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticsearchVersion"))

    @elasticsearch_version.setter
    def elasticsearch_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e2effedbe60ffc2fb8fe65b2cdddd9a29cfdcb61eef184721846e6b028414da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchVersion", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionAtRestOptions")
    def encryption_at_rest_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EncryptionAtRestOptionsProperty"]]:
        '''Whether the domain should encrypt data at rest, and if so, the AWS Key Management Service key to use.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EncryptionAtRestOptionsProperty"]], jsii.get(self, "encryptionAtRestOptions"))

    @encryption_at_rest_options.setter
    def encryption_at_rest_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.EncryptionAtRestOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c2f6f3e7bbcfd1c4ed35e1ea39cf14fc7af68d4b175db0fd18d69c66b89ad9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtRestOptions", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__b68ea5f4731e0bc02f7a196cd4b14d0ac22f6e22a661283031c3be761ff5c610)
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
            type_hints = typing.get_type_hints(_typecheckingstub__20a665cc917a112af2348ce54c28aa2743e93ef9dabf60cfbee200092f3bb7c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeToNodeEncryptionOptions", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__1ceb39ec0c3dca28571cbfbe9689bd6457a60fd17d054c9abf0a2c09165aef74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotOptions", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Service domain.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9076d2462cf49a948d9ea5d30b6392387174b389efc4e1dda4e4789f95edc66)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dff64c1f5c7bb8053ed4408ea633c0472baa0e83f0f43be1e87eb569f30f6739)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcOptions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.AdvancedSecurityOptionsInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "anonymous_auth_enabled": "anonymousAuthEnabled",
            "enabled": "enabled",
            "internal_user_database_enabled": "internalUserDatabaseEnabled",
            "master_user_options": "masterUserOptions",
        },
    )
    class AdvancedSecurityOptionsInputProperty:
        def __init__(
            self,
            *,
            anonymous_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            master_user_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.MasterUserOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies options for fine-grained access control.

            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param anonymous_auth_enabled: 
            :param enabled: True to enable fine-grained access control. You must also enable encryption of data at rest and node-to-node encryption.
            :param internal_user_database_enabled: True to enable the internal user database.
            :param master_user_options: Specifies information about the master user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                advanced_security_options_input_property = elasticsearch.CfnDomain.AdvancedSecurityOptionsInputProperty(
                    anonymous_auth_enabled=False,
                    enabled=False,
                    internal_user_database_enabled=False,
                    master_user_options=elasticsearch.CfnDomain.MasterUserOptionsProperty(
                        master_user_arn="masterUserArn",
                        master_user_name="masterUserName",
                        master_user_password="masterUserPassword"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__20207c85ae0a336344b4986652cfbfc4af27b1a56d54ba31ff6505ea1db70a1b)
                check_type(argname="argument anonymous_auth_enabled", value=anonymous_auth_enabled, expected_type=type_hints["anonymous_auth_enabled"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument internal_user_database_enabled", value=internal_user_database_enabled, expected_type=type_hints["internal_user_database_enabled"])
                check_type(argname="argument master_user_options", value=master_user_options, expected_type=type_hints["master_user_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if anonymous_auth_enabled is not None:
                self._values["anonymous_auth_enabled"] = anonymous_auth_enabled
            if enabled is not None:
                self._values["enabled"] = enabled
            if internal_user_database_enabled is not None:
                self._values["internal_user_database_enabled"] = internal_user_database_enabled
            if master_user_options is not None:
                self._values["master_user_options"] = master_user_options

        @builtins.property
        def anonymous_auth_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-anonymousauthenabled
            '''
            result = self._values.get("anonymous_auth_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to enable fine-grained access control.

            You must also enable encryption of data at rest and node-to-node encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def internal_user_database_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to enable the internal user database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled
            '''
            result = self._values.get("internal_user_database_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def master_user_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.MasterUserOptionsProperty"]]:
            '''Specifies information about the master user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-masteruseroptions
            '''
            result = self._values.get("master_user_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.MasterUserOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedSecurityOptionsInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.CognitoOptionsProperty",
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

            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param enabled: Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards. See `Amazon Cognito authentication for OpenSearch Dashboards <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html>`_ .
            :param identity_pool_id: The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication. Required if you enable Cognito authentication.
            :param role_arn: The ``AmazonESCognitoAccess`` role that allows OpenSearch Service to configure your user pool and identity pool. Required if you enable Cognito authentication.
            :param user_pool_id: The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication. Required if you enable Cognito authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                cognito_options_property = elasticsearch.CfnDomain.CognitoOptionsProperty(
                    enabled=False,
                    identity_pool_id="identityPoolId",
                    role_arn="roleArn",
                    user_pool_id="userPoolId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__595a6b3cdf3d5b32c86feb7dca3af8642c7eda687b4fb444faedfa8415028e7d)
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def identity_pool_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

            Required if you enable Cognito authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-identitypoolid
            '''
            result = self._values.get("identity_pool_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ``AmazonESCognitoAccess`` role that allows OpenSearch Service to configure your user pool and identity pool.

            Required if you enable Cognito authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_pool_id(self) -> typing.Optional[builtins.str]:
            '''The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.

            Required if you enable Cognito authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-userpoolid
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.ColdStorageOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class ColdStorageOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies options for cold storage. For more information, see `Cold storage for Amazon Elasticsearch Service <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/cold-storage.html>`_ .

            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param enabled: Whether to enable or disable cold storage on the domain. You must enable UltraWarm storage in order to enable cold storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                cold_storage_options_property = elasticsearch.CfnDomain.ColdStorageOptionsProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b29fbd709c231836e96b61f6b1dd17e4b87fdbcd26d4ec292f768b17478c922f)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to enable or disable cold storage on the domain.

            You must enable UltraWarm storage in order to enable cold storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html#cfn-elasticsearch-domain-coldstorageoptions-enabled
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.DomainEndpointOptionsProperty",
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

            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param custom_endpoint: The fully qualified URL for your custom endpoint. Required if you enabled a custom endpoint for the domain.
            :param custom_endpoint_certificate_arn: The AWS Certificate Manager ARN for your domain's SSL/TLS certificate. Required if you enabled a custom endpoint for the domain.
            :param custom_endpoint_enabled: True to enable a custom endpoint for the domain. If enabled, you must also provide values for ``CustomEndpoint`` and ``CustomEndpointCertificateArn`` .
            :param enforce_https: True to require that all traffic to the domain arrive over HTTPS.
            :param tls_security_policy: The minimum TLS version required for traffic to the domain. Valid values are TLS 1.3 (recommended) or 1.2:. - ``Policy-Min-TLS-1-0-2019-07`` - ``Policy-Min-TLS-1-2-2019-07``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                domain_endpoint_options_property = elasticsearch.CfnDomain.DomainEndpointOptionsProperty(
                    custom_endpoint="customEndpoint",
                    custom_endpoint_certificate_arn="customEndpointCertificateArn",
                    custom_endpoint_enabled=False,
                    enforce_https=False,
                    tls_security_policy="tlsSecurityPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a315182feb03d4b11e7632eea35a2f35d8b19b801ecb799c3744b2ed0bc11a76)
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpoint
            '''
            result = self._values.get("custom_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_endpoint_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The AWS Certificate Manager ARN for your domain's SSL/TLS certificate.

            Required if you enabled a custom endpoint for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpointcertificatearn
            '''
            result = self._values.get("custom_endpoint_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_endpoint_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to enable a custom endpoint for the domain.

            If enabled, you must also provide values for ``CustomEndpoint`` and ``CustomEndpointCertificateArn`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpointenabled
            '''
            result = self._values.get("custom_endpoint_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enforce_https(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True to require that all traffic to the domain arrive over HTTPS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-enforcehttps
            '''
            result = self._values.get("enforce_https")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def tls_security_policy(self) -> typing.Optional[builtins.str]:
            '''The minimum TLS version required for traffic to the domain. Valid values are TLS 1.3 (recommended) or 1.2:.

            - ``Policy-Min-TLS-1-0-2019-07``
            - ``Policy-Min-TLS-1-2-2019-07``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-tlssecuritypolicy
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.EBSOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_enabled": "ebsEnabled",
            "iops": "iops",
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
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain.

            For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .
            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param ebs_enabled: Specifies whether Amazon EBS volumes are attached to data nodes in the OpenSearch Service domain.
            :param iops: The number of I/O operations per second (IOPS) that the volume supports. This property applies only to provisioned IOPS EBS volume types.
            :param volume_size: The size (in GiB) of the EBS volume for each data node. The minimum and maximum size of an EBS volume depends on the EBS volume type and the instance type to which it is attached. For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .
            :param volume_type: The EBS volume type to use with the OpenSearch Service domain, such as standard, gp2, or io1. For more information about each type, see `Amazon EBS volume types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`_ in the *Amazon EC2 User Guide for Linux Instances* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                e_bSOptions_property = elasticsearch.CfnDomain.EBSOptionsProperty(
                    ebs_enabled=False,
                    iops=123,
                    volume_size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0a4bb0d03dd89e8279b9e57e4a68e7f2fce71595722dbad5fada43cc1b15616)
                check_type(argname="argument ebs_enabled", value=ebs_enabled, expected_type=type_hints["ebs_enabled"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ebs_enabled is not None:
                self._values["ebs_enabled"] = ebs_enabled
            if iops is not None:
                self._values["iops"] = iops
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def ebs_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether Amazon EBS volumes are attached to data nodes in the OpenSearch Service domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-ebsenabled
            '''
            result = self._values.get("ebs_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The number of I/O operations per second (IOPS) that the volume supports.

            This property applies only to provisioned IOPS EBS volume types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''The size (in GiB) of the EBS volume for each data node.

            The minimum and maximum size of an EBS volume depends on the EBS volume type and the instance type to which it is attached. For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''The EBS volume type to use with the OpenSearch Service domain, such as standard, gp2, or io1.

            For more information about each type, see `Amazon EBS volume types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`_ in the *Amazon EC2 User Guide for Linux Instances* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumetype
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.ElasticsearchClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cold_storage_options": "coldStorageOptions",
            "dedicated_master_count": "dedicatedMasterCount",
            "dedicated_master_enabled": "dedicatedMasterEnabled",
            "dedicated_master_type": "dedicatedMasterType",
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "warm_count": "warmCount",
            "warm_enabled": "warmEnabled",
            "warm_type": "warmType",
            "zone_awareness_config": "zoneAwarenessConfig",
            "zone_awareness_enabled": "zoneAwarenessEnabled",
        },
    )
    class ElasticsearchClusterConfigProperty:
        def __init__(
            self,
            *,
            cold_storage_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ColdStorageOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dedicated_master_count: typing.Optional[jsii.Number] = None,
            dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            dedicated_master_type: typing.Optional[builtins.str] = None,
            instance_count: typing.Optional[jsii.Number] = None,
            instance_type: typing.Optional[builtins.str] = None,
            warm_count: typing.Optional[jsii.Number] = None,
            warm_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            warm_type: typing.Optional[builtins.str] = None,
            zone_awareness_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ZoneAwarenessConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The cluster configuration for the OpenSearch Service domain.

            You can specify options such as the instance type and the number of instances. For more information, see `Creating and managing Amazon OpenSearch Service domains <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html>`_ in the *Amazon OpenSearch Service Developer Guide* .
            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param cold_storage_options: Specifies cold storage options for the domain.
            :param dedicated_master_count: The number of instances to use for the master node. If you specify this property, you must specify true for the DedicatedMasterEnabled property.
            :param dedicated_master_enabled: Indicates whether to use a dedicated master node for the OpenSearch Service domain. A dedicated master node is a cluster node that performs cluster management tasks, but doesn't hold data or respond to data upload requests. Dedicated master nodes offload cluster management tasks to increase the stability of your search clusters. See `Dedicated master nodes in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html>`_ .
            :param dedicated_master_type: The hardware configuration of the computer that hosts the dedicated master node, such as ``m3.medium.elasticsearch`` . If you specify this property, you must specify true for the ``DedicatedMasterEnabled`` property. For valid values, see `Supported instance types in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ .
            :param instance_count: The number of data nodes (instances) to use in the OpenSearch Service domain.
            :param instance_type: The instance type for your data nodes, such as ``m3.medium.elasticsearch`` . For valid values, see `Supported instance types in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ .
            :param warm_count: The number of warm nodes in the cluster. Required if you enable warm storage.
            :param warm_enabled: Whether to enable warm storage for the cluster.
            :param warm_type: The instance type for the cluster's warm nodes. Required if you enable warm storage.
            :param zone_awareness_config: Specifies zone awareness configuration options. Only use if ``ZoneAwarenessEnabled`` is ``true`` .
            :param zone_awareness_enabled: Indicates whether to enable zone awareness for the OpenSearch Service domain. When you enable zone awareness, OpenSearch Service allocates the nodes and replica index shards that belong to a cluster across two Availability Zones (AZs) in the same region to prevent data loss and minimize downtime in the event of node or data center failure. Don't enable zone awareness if your cluster has no replica index shards or is a single-node cluster. For more information, see `Configuring a multi-AZ domain in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                elasticsearch_cluster_config_property = elasticsearch.CfnDomain.ElasticsearchClusterConfigProperty(
                    cold_storage_options=elasticsearch.CfnDomain.ColdStorageOptionsProperty(
                        enabled=False
                    ),
                    dedicated_master_count=123,
                    dedicated_master_enabled=False,
                    dedicated_master_type="dedicatedMasterType",
                    instance_count=123,
                    instance_type="instanceType",
                    warm_count=123,
                    warm_enabled=False,
                    warm_type="warmType",
                    zone_awareness_config=elasticsearch.CfnDomain.ZoneAwarenessConfigProperty(
                        availability_zone_count=123
                    ),
                    zone_awareness_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36ac2eb43dd2dc644b88b3f9db0f58ead2dbb47ffc23f3d8fc546f53bfcefb4a)
                check_type(argname="argument cold_storage_options", value=cold_storage_options, expected_type=type_hints["cold_storage_options"])
                check_type(argname="argument dedicated_master_count", value=dedicated_master_count, expected_type=type_hints["dedicated_master_count"])
                check_type(argname="argument dedicated_master_enabled", value=dedicated_master_enabled, expected_type=type_hints["dedicated_master_enabled"])
                check_type(argname="argument dedicated_master_type", value=dedicated_master_type, expected_type=type_hints["dedicated_master_type"])
                check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
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
            '''Specifies cold storage options for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-coldstorageoptions
            '''
            result = self._values.get("cold_storage_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ColdStorageOptionsProperty"]], result)

        @builtins.property
        def dedicated_master_count(self) -> typing.Optional[jsii.Number]:
            '''The number of instances to use for the master node.

            If you specify this property, you must specify true for the DedicatedMasterEnabled property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-dedicatedmastercount
            '''
            result = self._values.get("dedicated_master_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dedicated_master_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to use a dedicated master node for the OpenSearch Service domain.

            A dedicated master node is a cluster node that performs cluster management tasks, but doesn't hold data or respond to data upload requests. Dedicated master nodes offload cluster management tasks to increase the stability of your search clusters. See `Dedicated master nodes in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-dedicatedmasterenabled
            '''
            result = self._values.get("dedicated_master_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def dedicated_master_type(self) -> typing.Optional[builtins.str]:
            '''The hardware configuration of the computer that hosts the dedicated master node, such as ``m3.medium.elasticsearch`` . If you specify this property, you must specify true for the ``DedicatedMasterEnabled`` property. For valid values, see `Supported instance types in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-dedicatedmastertype
            '''
            result = self._values.get("dedicated_master_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_count(self) -> typing.Optional[jsii.Number]:
            '''The number of data nodes (instances) to use in the OpenSearch Service domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''The instance type for your data nodes, such as ``m3.medium.elasticsearch`` . For valid values, see `Supported instance types in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def warm_count(self) -> typing.Optional[jsii.Number]:
            '''The number of warm nodes in the cluster.

            Required if you enable warm storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmcount
            '''
            result = self._values.get("warm_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def warm_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to enable warm storage for the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmenabled
            '''
            result = self._values.get("warm_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def warm_type(self) -> typing.Optional[builtins.str]:
            '''The instance type for the cluster's warm nodes.

            Required if you enable warm storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmtype
            '''
            result = self._values.get("warm_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zone_awareness_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ZoneAwarenessConfigProperty"]]:
            '''Specifies zone awareness configuration options.

            Only use if ``ZoneAwarenessEnabled`` is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-zoneawarenessconfig
            '''
            result = self._values.get("zone_awareness_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ZoneAwarenessConfigProperty"]], result)

        @builtins.property
        def zone_awareness_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to enable zone awareness for the OpenSearch Service domain.

            When you enable zone awareness, OpenSearch Service allocates the nodes and replica index shards that belong to a cluster across two Availability Zones (AZs) in the same region to prevent data loss and minimize downtime in the event of node or data center failure. Don't enable zone awareness if your cluster has no replica index shards or is a single-node cluster. For more information, see `Configuring a multi-AZ domain in Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-zoneawarenessenabled
            '''
            result = self._values.get("zone_awareness_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.EncryptionAtRestOptionsProperty",
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

            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param enabled: Specify ``true`` to enable encryption at rest.
            :param kms_key_id: The KMS key ID. Takes the form ``1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a`` . Required if you enable encryption at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                encryption_at_rest_options_property = elasticsearch.CfnDomain.EncryptionAtRestOptionsProperty(
                    enabled=False,
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ee9f0aff26691f651a27c328864208a5480af26681c2baa3afdcc6b1f8cb27b)
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
            '''Specify ``true`` to enable encryption at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html#cfn-elasticsearch-domain-encryptionatrestoptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS key ID.

            Takes the form ``1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a`` . Required if you enable encryption at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html#cfn-elasticsearch-domain-encryptionatrestoptions-kmskeyid
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.LogPublishingOptionProperty",
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
            '''.. epigraph::

   The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            Specifies whether the OpenSearch Service domain publishes the Elasticsearch application, search slow logs, or index slow logs to Amazon CloudWatch. Each option must be an object of name ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , or ``AUDIT_LOGS`` depending on the type of logs you want to publish.

            If you enable a slow log, you still have to enable the *collection* of slow logs using the Configuration API. To learn more, see `Enabling log publishing ( AWS CLI) <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html#createdomain-configure-slow-logs-cli>`_ .

            :param cloud_watch_logs_log_group_arn: Specifies the CloudWatch log group to publish to. Required if you enable log publishing for the domain.
            :param enabled: If ``true`` , enables the publishing of logs to CloudWatch. Default: ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                log_publishing_option_property = elasticsearch.CfnDomain.LogPublishingOptionProperty(
                    cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn",
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e7d124e6174f5352d66bdbb642c851ec6bf4aba9f8fcb6bf19e34809e37f6a9)
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

            Required if you enable log publishing for the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html#cfn-elasticsearch-domain-logpublishingoption-cloudwatchlogsloggrouparn
            '''
            result = self._values.get("cloud_watch_logs_log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , enables the publishing of logs to CloudWatch.

            Default: ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html#cfn-elasticsearch-domain-logpublishingoption-enabled
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.MasterUserOptionsProperty",
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
            '''Specifies information about the master user. Required if you enabled the internal user database.

            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param master_user_arn: ARN for the master user. Only specify if ``InternalUserDatabaseEnabled`` is false in ``AdvancedSecurityOptions`` .
            :param master_user_name: Username for the master user. Only specify if ``InternalUserDatabaseEnabled`` is true in ``AdvancedSecurityOptions`` .
            :param master_user_password: Password for the master user. Only specify if ``InternalUserDatabaseEnabled`` is true in ``AdvancedSecurityOptions`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                master_user_options_property = elasticsearch.CfnDomain.MasterUserOptionsProperty(
                    master_user_arn="masterUserArn",
                    master_user_name="masterUserName",
                    master_user_password="masterUserPassword"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86df1024036528c38c1cc3918e4413fdd5adee94c59ff0dba9e2625c1f7f6735)
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
            '''ARN for the master user.

            Only specify if ``InternalUserDatabaseEnabled`` is false in ``AdvancedSecurityOptions`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masteruserarn
            '''
            result = self._values.get("master_user_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def master_user_name(self) -> typing.Optional[builtins.str]:
            '''Username for the master user.

            Only specify if ``InternalUserDatabaseEnabled`` is true in ``AdvancedSecurityOptions`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masterusername
            '''
            result = self._values.get("master_user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def master_user_password(self) -> typing.Optional[builtins.str]:
            '''Password for the master user.

            Only specify if ``InternalUserDatabaseEnabled`` is true in ``AdvancedSecurityOptions`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masteruserpassword
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.NodeToNodeEncryptionOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class NodeToNodeEncryptionOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies whether node-to-node encryption is enabled.

            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param enabled: Specifies whether node-to-node encryption is enabled, as a Boolean.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                node_to_node_encryption_options_property = elasticsearch.CfnDomain.NodeToNodeEncryptionOptionsProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__79b4e8cc645055321e0aea8e7724655ea101aae985769f93812bc6db0624eb53)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether node-to-node encryption is enabled, as a Boolean.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html#cfn-elasticsearch-domain-nodetonodeencryptionoptions-enabled
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.SnapshotOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"automated_snapshot_start_hour": "automatedSnapshotStartHour"},
    )
    class SnapshotOptionsProperty:
        def __init__(
            self,
            *,
            automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''.. epigraph::

   The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            *DEPRECATED* . For domains running Elasticsearch 5.3 and later, OpenSearch Service takes hourly automated snapshots, making this setting irrelevant. For domains running earlier versions of Elasticsearch, OpenSearch Service takes daily automated snapshots.

            The automated snapshot configuration for the OpenSearch Service domain indices.

            :param automated_snapshot_start_hour: The hour in UTC during which the service takes an automated daily snapshot of the indices in the OpenSearch Service domain. For example, if you specify 0, OpenSearch Service takes an automated snapshot everyday between midnight and 1 am. You can specify a value between 0 and 23.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                snapshot_options_property = elasticsearch.CfnDomain.SnapshotOptionsProperty(
                    automated_snapshot_start_hour=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd199cc313b4bdbae2613aaf1084d93eab6fb227123efcd5eccb919a3c431497)
                check_type(argname="argument automated_snapshot_start_hour", value=automated_snapshot_start_hour, expected_type=type_hints["automated_snapshot_start_hour"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automated_snapshot_start_hour is not None:
                self._values["automated_snapshot_start_hour"] = automated_snapshot_start_hour

        @builtins.property
        def automated_snapshot_start_hour(self) -> typing.Optional[jsii.Number]:
            '''The hour in UTC during which the service takes an automated daily snapshot of the indices in the OpenSearch Service domain.

            For example, if you specify 0, OpenSearch Service takes an automated snapshot everyday between midnight and 1 am. You can specify a value between 0 and 23.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html#cfn-elasticsearch-domain-snapshotoptions-automatedsnapshotstarthour
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.VPCOptionsProperty",
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
            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param security_group_ids: The list of security group IDs that are associated with the VPC endpoints for the domain. If you don't provide a security group ID, OpenSearch Service uses the default security group for the VPC. To learn more, see `Security groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ in the *Amazon VPC User Guide* .
            :param subnet_ids: Provide one subnet ID for each Availability Zone that your domain uses. For example, you must specify three subnet IDs for a three Availability Zone domain. To learn more, see `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon VPC User Guide* . Required if you're creating your domain inside a VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                v_pCOptions_property = elasticsearch.CfnDomain.VPCOptionsProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__931aa1b11d25d7c92725f2e141ddba7562e992b6b38363844ccfcbd524041b69)
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html#cfn-elasticsearch-domain-vpcoptions-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Provide one subnet ID for each Availability Zone that your domain uses.

            For example, you must specify three subnet IDs for a three Availability Zone domain. To learn more, see `VPCs and subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ in the *Amazon VPC User Guide* .

            Required if you're creating your domain inside a VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html#cfn-elasticsearch-domain-vpcoptions-subnetids
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
        jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomain.ZoneAwarenessConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"availability_zone_count": "availabilityZoneCount"},
    )
    class ZoneAwarenessConfigProperty:
        def __init__(
            self,
            *,
            availability_zone_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies zone awareness configuration options. Only use if ``ZoneAwarenessEnabled`` is ``true`` .

            .. epigraph::

               The ``AWS::Elasticsearch::Domain`` resource is being replaced by the `AWS::OpenSearchService::Domain <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html>`_ resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see `New resource types <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource>`_ in the *Amazon OpenSearch Service Developer Guide* .

            :param availability_zone_count: If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use. Valid values are ``2`` and ``3`` . Default is 2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-zoneawarenessconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elasticsearch as elasticsearch
                
                zone_awareness_config_property = elasticsearch.CfnDomain.ZoneAwarenessConfigProperty(
                    availability_zone_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ee73d0667237b38d27f617dfe56f8c57182f358686fa721ebadbe9d9730d747)
                check_type(argname="argument availability_zone_count", value=availability_zone_count, expected_type=type_hints["availability_zone_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone_count is not None:
                self._values["availability_zone_count"] = availability_zone_count

        @builtins.property
        def availability_zone_count(self) -> typing.Optional[jsii.Number]:
            '''If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use.

            Valid values are ``2`` and ``3`` . Default is 2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-zoneawarenessconfig.html#cfn-elasticsearch-domain-zoneawarenessconfig-availabilityzonecount
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_policies": "accessPolicies",
        "advanced_options": "advancedOptions",
        "advanced_security_options": "advancedSecurityOptions",
        "cognito_options": "cognitoOptions",
        "domain_arn": "domainArn",
        "domain_endpoint_options": "domainEndpointOptions",
        "domain_name": "domainName",
        "ebs_options": "ebsOptions",
        "elasticsearch_cluster_config": "elasticsearchClusterConfig",
        "elasticsearch_version": "elasticsearchVersion",
        "encryption_at_rest_options": "encryptionAtRestOptions",
        "log_publishing_options": "logPublishingOptions",
        "node_to_node_encryption_options": "nodeToNodeEncryptionOptions",
        "snapshot_options": "snapshotOptions",
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
        cognito_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.CognitoOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        domain_arn: typing.Optional[builtins.str] = None,
        domain_endpoint_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.DomainEndpointOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        ebs_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EBSOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_cluster_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ElasticsearchClusterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_version: typing.Optional[builtins.str] = None,
        encryption_at_rest_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EncryptionAtRestOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.LogPublishingOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        node_to_node_encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.NodeToNodeEncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        snapshot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SnapshotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.VPCOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param access_policies: An AWS Identity and Access Management ( IAM ) policy document that specifies who can access the OpenSearch Service domain and their permissions. For more information, see `Configuring access policies <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-creating>`_ in the *Amazon OpenSearch Service Developer Guid* e.
        :param advanced_options: Additional options to specify for the OpenSearch Service domain. For more information, see `Advanced cluster parameters <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options>`_ in the *Amazon OpenSearch Service Developer Guide* .
        :param advanced_security_options: Specifies options for fine-grained access control.
        :param cognito_options: Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.
        :param domain_arn: 
        :param domain_endpoint_options: Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.
        :param domain_name: A name for the OpenSearch Service domain. For valid values, see the `DomainName <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configuration-api.html#configuration-api-datatypes-domainname>`_ data type in the *Amazon OpenSearch Service Developer Guide* . If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the domain name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param ebs_options: The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain. For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .
        :param elasticsearch_cluster_config: ElasticsearchClusterConfig is a property of the AWS::Elasticsearch::Domain resource that configures the cluster of an Amazon OpenSearch Service domain.
        :param elasticsearch_version: The version of Elasticsearch to use, such as 2.3. If not specified, 1.5 is used as the default. For information about the versions that OpenSearch Service supports, see `Supported versions of OpenSearch and Elasticsearch <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#choosing-version>`_ in the *Amazon OpenSearch Service Developer Guide* . If you set the `EnableVersionUpgrade <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-upgradeopensearchdomain>`_ update policy to ``true`` , you can update ``ElasticsearchVersion`` without interruption. When ``EnableVersionUpgrade`` is set to ``false`` , or is not specified, updating ``ElasticsearchVersion`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .
        :param encryption_at_rest_options: Whether the domain should encrypt data at rest, and if so, the AWS Key Management Service key to use. See `Encryption of data at rest for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html>`_ .
        :param log_publishing_options: An object with one or more of the following keys: ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , ``AUDIT_LOGS`` , depending on the types of logs you want to publish. Each key needs a valid ``LogPublishingOption`` value.
        :param node_to_node_encryption_options: Specifies whether node-to-node encryption is enabled. See `Node-to-node encryption for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html>`_ .
        :param snapshot_options: *DEPRECATED* . The automated snapshot configuration for the OpenSearch Service domain indices.
        :param tags: An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Service domain.
        :param vpc_options: The virtual private cloud (VPC) configuration for the OpenSearch Service domain. For more information, see `Launching your Amazon OpenSearch Service domains within a VPC <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html>`_ in the *Amazon OpenSearch Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticsearch as elasticsearch
            
            # access_policies: Any
            
            cfn_domain_props = elasticsearch.CfnDomainProps(
                access_policies=access_policies,
                advanced_options={
                    "advanced_options_key": "advancedOptions"
                },
                advanced_security_options=elasticsearch.CfnDomain.AdvancedSecurityOptionsInputProperty(
                    anonymous_auth_enabled=False,
                    enabled=False,
                    internal_user_database_enabled=False,
                    master_user_options=elasticsearch.CfnDomain.MasterUserOptionsProperty(
                        master_user_arn="masterUserArn",
                        master_user_name="masterUserName",
                        master_user_password="masterUserPassword"
                    )
                ),
                cognito_options=elasticsearch.CfnDomain.CognitoOptionsProperty(
                    enabled=False,
                    identity_pool_id="identityPoolId",
                    role_arn="roleArn",
                    user_pool_id="userPoolId"
                ),
                domain_arn="domainArn",
                domain_endpoint_options=elasticsearch.CfnDomain.DomainEndpointOptionsProperty(
                    custom_endpoint="customEndpoint",
                    custom_endpoint_certificate_arn="customEndpointCertificateArn",
                    custom_endpoint_enabled=False,
                    enforce_https=False,
                    tls_security_policy="tlsSecurityPolicy"
                ),
                domain_name="domainName",
                ebs_options=elasticsearch.CfnDomain.EBSOptionsProperty(
                    ebs_enabled=False,
                    iops=123,
                    volume_size=123,
                    volume_type="volumeType"
                ),
                elasticsearch_cluster_config=elasticsearch.CfnDomain.ElasticsearchClusterConfigProperty(
                    cold_storage_options=elasticsearch.CfnDomain.ColdStorageOptionsProperty(
                        enabled=False
                    ),
                    dedicated_master_count=123,
                    dedicated_master_enabled=False,
                    dedicated_master_type="dedicatedMasterType",
                    instance_count=123,
                    instance_type="instanceType",
                    warm_count=123,
                    warm_enabled=False,
                    warm_type="warmType",
                    zone_awareness_config=elasticsearch.CfnDomain.ZoneAwarenessConfigProperty(
                        availability_zone_count=123
                    ),
                    zone_awareness_enabled=False
                ),
                elasticsearch_version="elasticsearchVersion",
                encryption_at_rest_options=elasticsearch.CfnDomain.EncryptionAtRestOptionsProperty(
                    enabled=False,
                    kms_key_id="kmsKeyId"
                ),
                log_publishing_options={
                    "log_publishing_options_key": elasticsearch.CfnDomain.LogPublishingOptionProperty(
                        cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn",
                        enabled=False
                    )
                },
                node_to_node_encryption_options=elasticsearch.CfnDomain.NodeToNodeEncryptionOptionsProperty(
                    enabled=False
                ),
                snapshot_options=elasticsearch.CfnDomain.SnapshotOptionsProperty(
                    automated_snapshot_start_hour=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_options=elasticsearch.CfnDomain.VPCOptionsProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9cf4a1cacc663baa0bc99c7e4784f1bb4a208a6851dceb6a846d215d5062938)
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
            check_type(argname="argument advanced_options", value=advanced_options, expected_type=type_hints["advanced_options"])
            check_type(argname="argument advanced_security_options", value=advanced_security_options, expected_type=type_hints["advanced_security_options"])
            check_type(argname="argument cognito_options", value=cognito_options, expected_type=type_hints["cognito_options"])
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument domain_endpoint_options", value=domain_endpoint_options, expected_type=type_hints["domain_endpoint_options"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument ebs_options", value=ebs_options, expected_type=type_hints["ebs_options"])
            check_type(argname="argument elasticsearch_cluster_config", value=elasticsearch_cluster_config, expected_type=type_hints["elasticsearch_cluster_config"])
            check_type(argname="argument elasticsearch_version", value=elasticsearch_version, expected_type=type_hints["elasticsearch_version"])
            check_type(argname="argument encryption_at_rest_options", value=encryption_at_rest_options, expected_type=type_hints["encryption_at_rest_options"])
            check_type(argname="argument log_publishing_options", value=log_publishing_options, expected_type=type_hints["log_publishing_options"])
            check_type(argname="argument node_to_node_encryption_options", value=node_to_node_encryption_options, expected_type=type_hints["node_to_node_encryption_options"])
            check_type(argname="argument snapshot_options", value=snapshot_options, expected_type=type_hints["snapshot_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_options", value=vpc_options, expected_type=type_hints["vpc_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_policies is not None:
            self._values["access_policies"] = access_policies
        if advanced_options is not None:
            self._values["advanced_options"] = advanced_options
        if advanced_security_options is not None:
            self._values["advanced_security_options"] = advanced_security_options
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
        if elasticsearch_cluster_config is not None:
            self._values["elasticsearch_cluster_config"] = elasticsearch_cluster_config
        if elasticsearch_version is not None:
            self._values["elasticsearch_version"] = elasticsearch_version
        if encryption_at_rest_options is not None:
            self._values["encryption_at_rest_options"] = encryption_at_rest_options
        if log_publishing_options is not None:
            self._values["log_publishing_options"] = log_publishing_options
        if node_to_node_encryption_options is not None:
            self._values["node_to_node_encryption_options"] = node_to_node_encryption_options
        if snapshot_options is not None:
            self._values["snapshot_options"] = snapshot_options
        if tags is not None:
            self._values["tags"] = tags
        if vpc_options is not None:
            self._values["vpc_options"] = vpc_options

    @builtins.property
    def access_policies(self) -> typing.Any:
        '''An AWS Identity and Access Management ( IAM ) policy document that specifies who can access the OpenSearch Service domain and their permissions.

        For more information, see `Configuring access policies <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-creating>`_ in the *Amazon OpenSearch Service Developer Guid* e.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-accesspolicies
        '''
        result = self._values.get("access_policies")
        return typing.cast(typing.Any, result)

    @builtins.property
    def advanced_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional options to specify for the OpenSearch Service domain.

        For more information, see `Advanced cluster parameters <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options>`_ in the *Amazon OpenSearch Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedoptions
        '''
        result = self._values.get("advanced_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def advanced_security_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.AdvancedSecurityOptionsInputProperty]]:
        '''Specifies options for fine-grained access control.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedsecurityoptions
        '''
        result = self._values.get("advanced_security_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.AdvancedSecurityOptionsInputProperty]], result)

    @builtins.property
    def cognito_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.CognitoOptionsProperty]]:
        '''Configures OpenSearch Service to use Amazon Cognito authentication for OpenSearch Dashboards.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-cognitooptions
        '''
        result = self._values.get("cognito_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.CognitoOptionsProperty]], result)

    @builtins.property
    def domain_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainarn
        '''
        result = self._values.get("domain_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_endpoint_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.DomainEndpointOptionsProperty]]:
        '''Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainendpointoptions
        '''
        result = self._values.get("domain_endpoint_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.DomainEndpointOptionsProperty]], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''A name for the OpenSearch Service domain.

        For valid values, see the `DomainName <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configuration-api.html#configuration-api-datatypes-domainname>`_ data type in the *Amazon OpenSearch Service Developer Guide* . If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the domain name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainname
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EBSOptionsProperty]]:
        '''The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the OpenSearch Service domain.

        For more information, see `EBS volume size limits <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html#ebsresource>`_ in the *Amazon OpenSearch Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-ebsoptions
        '''
        result = self._values.get("ebs_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EBSOptionsProperty]], result)

    @builtins.property
    def elasticsearch_cluster_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.ElasticsearchClusterConfigProperty]]:
        '''ElasticsearchClusterConfig is a property of the AWS::Elasticsearch::Domain resource that configures the cluster of an Amazon OpenSearch Service domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchclusterconfig
        '''
        result = self._values.get("elasticsearch_cluster_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.ElasticsearchClusterConfigProperty]], result)

    @builtins.property
    def elasticsearch_version(self) -> typing.Optional[builtins.str]:
        '''The version of Elasticsearch to use, such as 2.3. If not specified, 1.5 is used as the default. For information about the versions that OpenSearch Service supports, see `Supported versions of OpenSearch and Elasticsearch <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html#choosing-version>`_ in the *Amazon OpenSearch Service Developer Guide* .

        If you set the `EnableVersionUpgrade <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-upgradeopensearchdomain>`_ update policy to ``true`` , you can update ``ElasticsearchVersion`` without interruption. When ``EnableVersionUpgrade`` is set to ``false`` , or is not specified, updating ``ElasticsearchVersion`` results in `replacement <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchversion
        '''
        result = self._values.get("elasticsearch_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_at_rest_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EncryptionAtRestOptionsProperty]]:
        '''Whether the domain should encrypt data at rest, and if so, the AWS Key Management Service key to use.

        See `Encryption of data at rest for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-encryptionatrestoptions
        '''
        result = self._values.get("encryption_at_rest_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EncryptionAtRestOptionsProperty]], result)

    @builtins.property
    def log_publishing_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDomain.LogPublishingOptionProperty]]]]:
        '''An object with one or more of the following keys: ``SEARCH_SLOW_LOGS`` , ``ES_APPLICATION_LOGS`` , ``INDEX_SLOW_LOGS`` , ``AUDIT_LOGS`` , depending on the types of logs you want to publish.

        Each key needs a valid ``LogPublishingOption`` value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-logpublishingoptions
        '''
        result = self._values.get("log_publishing_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDomain.LogPublishingOptionProperty]]]], result)

    @builtins.property
    def node_to_node_encryption_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.NodeToNodeEncryptionOptionsProperty]]:
        '''Specifies whether node-to-node encryption is enabled.

        See `Node-to-node encryption for Amazon OpenSearch Service <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-nodetonodeencryptionoptions
        '''
        result = self._values.get("node_to_node_encryption_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.NodeToNodeEncryptionOptionsProperty]], result)

    @builtins.property
    def snapshot_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SnapshotOptionsProperty]]:
        '''*DEPRECATED* .

        The automated snapshot configuration for the OpenSearch Service domain indices.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-snapshotoptions
        '''
        result = self._values.get("snapshot_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SnapshotOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Service domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.VPCOptionsProperty]]:
        '''The virtual private cloud (VPC) configuration for the OpenSearch Service domain.

        For more information, see `Launching your Amazon OpenSearch Service domains within a VPC <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html>`_ in the *Amazon OpenSearch Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-vpcoptions
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.CognitoOptions",
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
        '''(deprecated) Configures Amazon ES to use Amazon Cognito authentication for Kibana.

        :param identity_pool_id: (deprecated) The Amazon Cognito identity pool ID that you want Amazon ES to use for Kibana authentication.
        :param role: (deprecated) A role that allows Amazon ES to configure your user pool and identity pool. It must have the ``AmazonESCognitoAccess`` policy attached to it.
        :param user_pool_id: (deprecated) The Amazon Cognito user pool ID that you want Amazon ES to use for Kibana authentication.

        :deprecated: use opensearchservice module instead

        :see: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html
        :stability: deprecated
        :exampleMetadata: fixture=migrate-opensearch infused

        Example::

            es.Domain(self, "Domain",
                cognito_kibana_auth=es.CognitoOptions(
                    identity_pool_id="test-identity-pool-id",
                    user_pool_id="test-user-pool-id",
                    role=role
                ),
                version=elasticsearch_version
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b524e8e96dadc613c3ade2864195ce643f52df86cc22205eeea1f5a1b04715fa)
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
        '''(deprecated) The Amazon Cognito identity pool ID that you want Amazon ES to use for Kibana authentication.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("identity_pool_id")
        assert result is not None, "Required property 'identity_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> _IRole_235f5d8e:
        '''(deprecated) A role that allows Amazon ES to configure your user pool and identity pool.

        It must have the ``AmazonESCognitoAccess`` policy attached to it.

        :deprecated: use opensearchservice module instead

        :see: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html#es-cognito-auth-prereq
        :stability: deprecated
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''(deprecated) The Amazon Cognito user pool ID that you want Amazon ES to use for Kibana authentication.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.CustomEndpointOptions",
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
        '''(deprecated) Configures a custom domain endpoint for the ES domain.

        :param domain_name: (deprecated) The custom domain name to assign.
        :param certificate: (deprecated) The certificate to use. Default: - create a new one
        :param hosted_zone: (deprecated) The hosted zone in Route53 to create the CNAME record in. Default: - do not create a CNAME

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            es.Domain(self, "Domain",
                version=es.ElasticsearchVersion.V7_7,
                custom_endpoint=es.CustomEndpointOptions(
                    domain_name="search.example.com"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea711a6b742c02c3c27fa537028f874f857943b01e96d2167b14a0d27de9a54)
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
        '''(deprecated) The custom domain name to assign.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[_ICertificate_c194c70b]:
        '''(deprecated) The certificate to use.

        :default: - create a new one

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[_ICertificate_c194c70b], result)

    @builtins.property
    def hosted_zone(self) -> typing.Optional[_IHostedZone_9a6907ad]:
        '''(deprecated) The hosted zone in Route53 to create the CNAME record in.

        :default: - do not create a CNAME

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.DomainAttributes",
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
        '''(deprecated) Reference to an Elasticsearch domain.

        :param domain_arn: (deprecated) The ARN of the Elasticsearch domain.
        :param domain_endpoint: (deprecated) The domain endpoint of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elasticsearch as elasticsearch
            
            domain_attributes = elasticsearch.DomainAttributes(
                domain_arn="domainArn",
                domain_endpoint="domainEndpoint"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72419130e136fdde5577319d89e912d0d4cabd7e160115eb7fb1c0f589469870)
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument domain_endpoint", value=domain_endpoint, expected_type=type_hints["domain_endpoint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_arn": domain_arn,
            "domain_endpoint": domain_endpoint,
        }

    @builtins.property
    def domain_arn(self) -> builtins.str:
        '''(deprecated) The ARN of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("domain_arn")
        assert result is not None, "Required property 'domain_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_endpoint(self) -> builtins.str:
        '''(deprecated) The domain endpoint of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.DomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "version": "version",
        "access_policies": "accessPolicies",
        "advanced_options": "advancedOptions",
        "automated_snapshot_start_hour": "automatedSnapshotStartHour",
        "capacity": "capacity",
        "cognito_kibana_auth": "cognitoKibanaAuth",
        "custom_endpoint": "customEndpoint",
        "domain_name": "domainName",
        "ebs": "ebs",
        "enable_version_upgrade": "enableVersionUpgrade",
        "encryption_at_rest": "encryptionAtRest",
        "enforce_https": "enforceHttps",
        "fine_grained_access_control": "fineGrainedAccessControl",
        "logging": "logging",
        "node_to_node_encryption": "nodeToNodeEncryption",
        "removal_policy": "removalPolicy",
        "security_groups": "securityGroups",
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
        version: "ElasticsearchVersion",
        access_policies: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
        capacity: typing.Optional[typing.Union[CapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        cognito_kibana_auth: typing.Optional[typing.Union[CognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_endpoint: typing.Optional[typing.Union[CustomEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        ebs: typing.Optional[typing.Union["EbsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_version_upgrade: typing.Optional[builtins.bool] = None,
        encryption_at_rest: typing.Optional[typing.Union["EncryptionAtRestOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        enforce_https: typing.Optional[builtins.bool] = None,
        fine_grained_access_control: typing.Optional[typing.Union[AdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["LoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        node_to_node_encryption: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        tls_security_policy: typing.Optional["TLSSecurityPolicy"] = None,
        use_unsigned_basic_auth: typing.Optional[builtins.bool] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
        zone_awareness: typing.Optional[typing.Union["ZoneAwarenessConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(deprecated) Properties for an AWS Elasticsearch Domain.

        :param version: (deprecated) The Elasticsearch version that your domain will leverage.
        :param access_policies: (deprecated) Domain Access policies. Default: - No access policies.
        :param advanced_options: (deprecated) Additional options to specify for the Amazon ES domain. Default: - no advanced options are specified
        :param automated_snapshot_start_hour: (deprecated) The hour in UTC during which the service takes an automated daily snapshot of the indices in the Amazon ES domain. Only applies for Elasticsearch versions below 5.3. Default: - Hourly automated snapshots not used
        :param capacity: (deprecated) The cluster capacity configuration for the Amazon ES domain. Default: - 1 r5.large.elasticsearch data node; no dedicated master nodes.
        :param cognito_kibana_auth: (deprecated) Configures Amazon ES to use Amazon Cognito authentication for Kibana. Default: - Cognito not used for authentication to Kibana.
        :param custom_endpoint: (deprecated) To configure a custom domain configure these options. If you specify a Route53 hosted zone it will create a CNAME record and use DNS validation for the certificate Default: - no custom domain endpoint will be configured
        :param domain_name: (deprecated) Enforces a particular physical domain name. Default: - A name will be auto-generated.
        :param ebs: (deprecated) The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the Amazon ES domain. For more information, see [Configuring EBS-based Storage] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs) in the Amazon Elasticsearch Service Developer Guide. Default: - 10 GiB General Purpose (SSD) volumes per node.
        :param enable_version_upgrade: (deprecated) To upgrade an Amazon ES domain to a new version of Elasticsearch rather than replacing the entire domain resource, use the EnableVersionUpgrade update policy. Default: - false
        :param encryption_at_rest: (deprecated) Encryption at rest options for the cluster. Default: - No encryption at rest
        :param enforce_https: (deprecated) True to require that all traffic to the domain arrive over HTTPS. Default: - false
        :param fine_grained_access_control: (deprecated) Specifies options for fine-grained access control. Requires Elasticsearch version 6.7 or later. Enabling fine-grained access control also requires encryption of data at rest and node-to-node encryption, along with enforced HTTPS. Default: - fine-grained access control is disabled
        :param logging: (deprecated) Configuration log publishing configuration options. Default: - No logs are published
        :param node_to_node_encryption: (deprecated) Specify true to enable node to node encryption. Requires Elasticsearch version 6.0 or later. Default: - Node to node encryption is not enabled.
        :param removal_policy: (deprecated) Policy to apply when the domain is removed from the stack. Default: RemovalPolicy.RETAIN
        :param security_groups: (deprecated) The list of security groups that are associated with the VPC endpoints for the domain. Only used if ``vpc`` is specified. Default: - One new security group is created.
        :param tls_security_policy: (deprecated) The minimum TLS version required for traffic to the domain. Default: - TLSSecurityPolicy.TLS_1_0
        :param use_unsigned_basic_auth: (deprecated) Configures the domain so that unsigned basic auth is enabled. If no master user is provided a default master user with username ``admin`` and a dynamically generated password stored in KMS is created. The password can be retrieved by getting ``masterUserPassword`` from the domain instance. Setting this to true will also add an access policy that allows unsigned access, enable node to node encryption, encryption at rest. If conflicting settings are encountered (like disabling encryption at rest) enabling this setting will cause a failure. Default: - false
        :param vpc: (deprecated) Place the domain inside this VPC. Default: - Domain is not placed in a VPC.
        :param vpc_subnets: (deprecated) The specific vpc subnets the domain will be placed in. You must provide one subnet for each Availability Zone that your domain uses. For example, you must specify three subnet IDs for a three Availability Zone domain. Only used if ``vpc`` is specified. Default: - All private subnets.
        :param zone_awareness: (deprecated) The cluster zone awareness configuration for the Amazon ES domain. Default: - no zone awareness (1 AZ)

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            domain = es.Domain(self, "Domain",
                version=es.ElasticsearchVersion.V7_4,
                ebs=es.EbsOptions(
                    volume_size=100,
                    volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
                ),
                node_to_node_encryption=True,
                encryption_at_rest=es.EncryptionAtRestOptions(
                    enabled=True
                )
            )
        '''
        if isinstance(capacity, dict):
            capacity = CapacityConfig(**capacity)
        if isinstance(cognito_kibana_auth, dict):
            cognito_kibana_auth = CognitoOptions(**cognito_kibana_auth)
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
        if isinstance(zone_awareness, dict):
            zone_awareness = ZoneAwarenessConfig(**zone_awareness)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572eb3999b8c38b39f33fa525daa95c090ed063b8212bb3a0e6f1f533bb2064e)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
            check_type(argname="argument advanced_options", value=advanced_options, expected_type=type_hints["advanced_options"])
            check_type(argname="argument automated_snapshot_start_hour", value=automated_snapshot_start_hour, expected_type=type_hints["automated_snapshot_start_hour"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument cognito_kibana_auth", value=cognito_kibana_auth, expected_type=type_hints["cognito_kibana_auth"])
            check_type(argname="argument custom_endpoint", value=custom_endpoint, expected_type=type_hints["custom_endpoint"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
            check_type(argname="argument enable_version_upgrade", value=enable_version_upgrade, expected_type=type_hints["enable_version_upgrade"])
            check_type(argname="argument encryption_at_rest", value=encryption_at_rest, expected_type=type_hints["encryption_at_rest"])
            check_type(argname="argument enforce_https", value=enforce_https, expected_type=type_hints["enforce_https"])
            check_type(argname="argument fine_grained_access_control", value=fine_grained_access_control, expected_type=type_hints["fine_grained_access_control"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument node_to_node_encryption", value=node_to_node_encryption, expected_type=type_hints["node_to_node_encryption"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
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
        if cognito_kibana_auth is not None:
            self._values["cognito_kibana_auth"] = cognito_kibana_auth
        if custom_endpoint is not None:
            self._values["custom_endpoint"] = custom_endpoint
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if ebs is not None:
            self._values["ebs"] = ebs
        if enable_version_upgrade is not None:
            self._values["enable_version_upgrade"] = enable_version_upgrade
        if encryption_at_rest is not None:
            self._values["encryption_at_rest"] = encryption_at_rest
        if enforce_https is not None:
            self._values["enforce_https"] = enforce_https
        if fine_grained_access_control is not None:
            self._values["fine_grained_access_control"] = fine_grained_access_control
        if logging is not None:
            self._values["logging"] = logging
        if node_to_node_encryption is not None:
            self._values["node_to_node_encryption"] = node_to_node_encryption
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_groups is not None:
            self._values["security_groups"] = security_groups
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
    def version(self) -> "ElasticsearchVersion":
        '''(deprecated) The Elasticsearch version that your domain will leverage.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast("ElasticsearchVersion", result)

    @builtins.property
    def access_policies(
        self,
    ) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''(deprecated) Domain Access policies.

        :default: - No access policies.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("access_policies")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    @builtins.property
    def advanced_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(deprecated) Additional options to specify for the Amazon ES domain.

        :default: - no advanced options are specified

        :deprecated: use opensearchservice module instead

        :see: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options
        :stability: deprecated
        '''
        result = self._values.get("advanced_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def automated_snapshot_start_hour(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) The hour in UTC during which the service takes an automated daily snapshot of the indices in the Amazon ES domain.

        Only applies for Elasticsearch
        versions below 5.3.

        :default: - Hourly automated snapshots not used

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("automated_snapshot_start_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def capacity(self) -> typing.Optional[CapacityConfig]:
        '''(deprecated) The cluster capacity configuration for the Amazon ES domain.

        :default: - 1 r5.large.elasticsearch data node; no dedicated master nodes.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[CapacityConfig], result)

    @builtins.property
    def cognito_kibana_auth(self) -> typing.Optional[CognitoOptions]:
        '''(deprecated) Configures Amazon ES to use Amazon Cognito authentication for Kibana.

        :default: - Cognito not used for authentication to Kibana.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("cognito_kibana_auth")
        return typing.cast(typing.Optional[CognitoOptions], result)

    @builtins.property
    def custom_endpoint(self) -> typing.Optional[CustomEndpointOptions]:
        '''(deprecated) To configure a custom domain configure these options.

        If you specify a Route53 hosted zone it will create a CNAME record and use DNS validation for the certificate

        :default: - no custom domain endpoint will be configured

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("custom_endpoint")
        return typing.cast(typing.Optional[CustomEndpointOptions], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Enforces a particular physical domain name.

        :default: - A name will be auto-generated.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs(self) -> typing.Optional["EbsOptions"]:
        '''(deprecated) The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the Amazon ES domain.

        For more information, see
        [Configuring EBS-based Storage]
        (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs)
        in the Amazon Elasticsearch Service Developer Guide.

        :default: - 10 GiB General Purpose (SSD) volumes per node.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["EbsOptions"], result)

    @builtins.property
    def enable_version_upgrade(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) To upgrade an Amazon ES domain to a new version of Elasticsearch rather than replacing the entire domain resource, use the EnableVersionUpgrade update policy.

        :default: - false

        :deprecated: use opensearchservice module instead

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-upgradeelasticsearchdomain
        :stability: deprecated
        '''
        result = self._values.get("enable_version_upgrade")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_at_rest(self) -> typing.Optional["EncryptionAtRestOptions"]:
        '''(deprecated) Encryption at rest options for the cluster.

        :default: - No encryption at rest

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("encryption_at_rest")
        return typing.cast(typing.Optional["EncryptionAtRestOptions"], result)

    @builtins.property
    def enforce_https(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) True to require that all traffic to the domain arrive over HTTPS.

        :default: - false

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("enforce_https")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def fine_grained_access_control(self) -> typing.Optional[AdvancedSecurityOptions]:
        '''(deprecated) Specifies options for fine-grained access control.

        Requires Elasticsearch version 6.7 or later. Enabling fine-grained access control
        also requires encryption of data at rest and node-to-node encryption, along with
        enforced HTTPS.

        :default: - fine-grained access control is disabled

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("fine_grained_access_control")
        return typing.cast(typing.Optional[AdvancedSecurityOptions], result)

    @builtins.property
    def logging(self) -> typing.Optional["LoggingOptions"]:
        '''(deprecated) Configuration log publishing configuration options.

        :default: - No logs are published

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["LoggingOptions"], result)

    @builtins.property
    def node_to_node_encryption(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Specify true to enable node to node encryption.

        Requires Elasticsearch version 6.0 or later.

        :default: - Node to node encryption is not enabled.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("node_to_node_encryption")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''(deprecated) Policy to apply when the domain is removed from the stack.

        :default: RemovalPolicy.RETAIN

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''(deprecated) The list of security groups that are associated with the VPC endpoints for the domain.

        Only used if ``vpc`` is specified.

        :default: - One new security group is created.

        :deprecated: use opensearchservice module instead

        :see: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html
        :stability: deprecated
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def tls_security_policy(self) -> typing.Optional["TLSSecurityPolicy"]:
        '''(deprecated) The minimum TLS version required for traffic to the domain.

        :default: - TLSSecurityPolicy.TLS_1_0

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("tls_security_policy")
        return typing.cast(typing.Optional["TLSSecurityPolicy"], result)

    @builtins.property
    def use_unsigned_basic_auth(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Configures the domain so that unsigned basic auth is enabled.

        If no master user is provided a default master user
        with username ``admin`` and a dynamically generated password stored in KMS is created. The password can be retrieved
        by getting ``masterUserPassword`` from the domain instance.

        Setting this to true will also add an access policy that allows unsigned
        access, enable node to node encryption, encryption at rest. If conflicting
        settings are encountered (like disabling encryption at rest) enabling this
        setting will cause a failure.

        :default: - false

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("use_unsigned_basic_auth")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''(deprecated) Place the domain inside this VPC.

        :default: - Domain is not placed in a VPC.

        :deprecated: use opensearchservice module instead

        :see: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html
        :stability: deprecated
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[typing.List[_SubnetSelection_e57d76df]]:
        '''(deprecated) The specific vpc subnets the domain will be placed in.

        You must provide one subnet for each Availability Zone
        that your domain uses. For example, you must specify three subnet IDs for a three Availability Zone
        domain.

        Only used if ``vpc`` is specified.

        :default: - All private subnets.

        :deprecated: use opensearchservice module instead

        :see: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html
        :stability: deprecated
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[typing.List[_SubnetSelection_e57d76df]], result)

    @builtins.property
    def zone_awareness(self) -> typing.Optional["ZoneAwarenessConfig"]:
        '''(deprecated) The cluster zone awareness configuration for the Amazon ES domain.

        :default: - no zone awareness (1 AZ)

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.EbsOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "iops": "iops",
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
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[_EbsDeviceVolumeType_6792555b] = None,
    ) -> None:
        '''(deprecated) The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the Amazon ES domain.

        For more information, see
        [Configuring EBS-based Storage]
        (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs)
        in the Amazon Elasticsearch Service Developer Guide.

        :param enabled: (deprecated) Specifies whether Amazon EBS volumes are attached to data nodes in the Amazon ES domain. Default: - true
        :param iops: (deprecated) The number of I/O operations per second (IOPS) that the volume supports. This property applies only to the Provisioned IOPS (SSD) EBS volume type. Default: - iops are not set.
        :param volume_size: (deprecated) The size (in GiB) of the EBS volume for each data node. The minimum and maximum size of an EBS volume depends on the EBS volume type and the instance type to which it is attached. For more information, see [Configuring EBS-based Storage] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs) in the Amazon Elasticsearch Service Developer Guide. Default: 10
        :param volume_type: (deprecated) The EBS volume type to use with the Amazon ES domain, such as standard, gp2, io1. For more information, see[Configuring EBS-based Storage] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs) in the Amazon Elasticsearch Service Developer Guide. Default: gp2

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            prod_domain = es.Domain(self, "Domain",
                version=es.ElasticsearchVersion.V7_1,
                capacity=es.CapacityConfig(
                    master_nodes=5,
                    data_nodes=20
                ),
                ebs=es.EbsOptions(
                    volume_size=20
                ),
                zone_awareness=es.ZoneAwarenessConfig(
                    availability_zone_count=3
                ),
                logging=es.LoggingOptions(
                    slow_search_log_enabled=True,
                    app_log_enabled=True,
                    slow_index_log_enabled=True
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__653b4b977dd3a1aabb16baf6f32203c90668a1bdcac85452086445b36c330954)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if iops is not None:
            self._values["iops"] = iops
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Specifies whether Amazon EBS volumes are attached to data nodes in the Amazon ES domain.

        :default: - true

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) The number of I/O operations per second (IOPS) that the volume supports.

        This property applies only to the Provisioned IOPS (SSD) EBS
        volume type.

        :default: - iops are not set.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) The size (in GiB) of the EBS volume for each data node.

        The minimum and
        maximum size of an EBS volume depends on the EBS volume type and the
        instance type to which it is attached.  For more information, see
        [Configuring EBS-based Storage]
        (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs)
        in the Amazon Elasticsearch Service Developer Guide.

        :default: 10

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[_EbsDeviceVolumeType_6792555b]:
        '''(deprecated) The EBS volume type to use with the Amazon ES domain, such as standard, gp2, io1.

        For more information, see[Configuring EBS-based Storage]
        (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs)
        in the Amazon Elasticsearch Service Developer Guide.

        :default: gp2

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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


class ElasticsearchVersion(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticsearch.ElasticsearchVersion",
):
    '''Elasticsearch version.

    :exampleMetadata: infused

    Example::

        domain = es.Domain(self, "Domain",
            version=es.ElasticsearchVersion.V7_4,
            ebs=es.EbsOptions(
                volume_size=100,
                volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
            ),
            node_to_node_encryption=True,
            encryption_at_rest=es.EncryptionAtRestOptions(
                enabled=True
            )
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, version: builtins.str) -> "ElasticsearchVersion":
        '''Custom Elasticsearch version.

        :param version: custom version number.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94cee41a2246511ec77c9b6a556875c250b85ee87cddd5b0cc76dea112a4625f)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast("ElasticsearchVersion", jsii.sinvoke(cls, "of", [version]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_5")
    def V1_5(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 1.5.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V1_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_3")
    def V2_3(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 2.3.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V2_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V5_1")
    def V5_1(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 5.1.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V5_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V5_3")
    def V5_3(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 5.3.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V5_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V5_5")
    def V5_5(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 5.5.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V5_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V5_6")
    def V5_6(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 5.6.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V5_6"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V6_0")
    def V6_0(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 6.0.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V6_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V6_2")
    def V6_2(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 6.2.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V6_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V6_3")
    def V6_3(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 6.3.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V6_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V6_4")
    def V6_4(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 6.4.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V6_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V6_5")
    def V6_5(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 6.5.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V6_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V6_7")
    def V6_7(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 6.7.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V6_7"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V6_8")
    def V6_8(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 6.8.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V6_8"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V7_1")
    def V7_1(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 7.1.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V7_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V7_10")
    def V7_10(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 7.10.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V7_10"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V7_4")
    def V7_4(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 7.4.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V7_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V7_7")
    def V7_7(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 7.7.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V7_7"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V7_8")
    def V7_8(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 7.8.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V7_8"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V7_9")
    def V7_9(cls) -> "ElasticsearchVersion":
        '''AWS Elasticsearch 7.9.'''
        return typing.cast("ElasticsearchVersion", jsii.sget(cls, "V7_9"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''Elasticsearch version number.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticsearch.EncryptionAtRestOptions",
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
        '''(deprecated) Whether the domain should encrypt data at rest, and if so, the AWS Key Management Service (KMS) key to use.

        Can only be used to create a new domain,
        not update an existing one. Requires Elasticsearch version 5.1 or later.

        :param enabled: (deprecated) Specify true to enable encryption at rest. Default: - encryption at rest is disabled.
        :param kms_key: (deprecated) Supply if using KMS key for encryption at rest. Default: - uses default aws/es KMS key.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            domain = es.Domain(self, "Domain",
                version=es.ElasticsearchVersion.V7_1,
                enforce_https=True,
                node_to_node_encryption=True,
                encryption_at_rest=es.EncryptionAtRestOptions(
                    enabled=True
                ),
                fine_grained_access_control=es.AdvancedSecurityOptions(
                    master_user_name="master-user"
                )
            )
            
            master_user_password = domain.master_user_password
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a0566221450862dc46d961944b4613c299ea2ba900c19e9652b8e47501e1b0a)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if kms_key is not None:
            self._values["kms_key"] = kms_key

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Specify true to enable encryption at rest.

        :default: - encryption at rest is disabled.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''(deprecated) Supply if using KMS key for encryption at rest.

        :default: - uses default aws/es KMS key.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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


@jsii.interface(jsii_type="aws-cdk-lib.aws_elasticsearch.IDomain")
class IDomain(_IResource_c80c4260, typing_extensions.Protocol):
    '''(deprecated) An interface that represents an Elasticsearch domain - either created with the CDK, or an existing one.

    :deprecated: use opensearchservice module instead

    :stability: deprecated
    '''

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> builtins.str:
        '''(deprecated) Arn of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="domainEndpoint")
    def domain_endpoint(self) -> builtins.str:
        '''(deprecated) Endpoint of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''(deprecated) Domain name of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantIndexRead")
    def grant_index_read(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="grantIndexReadWrite")
    def grant_index_read_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="grantIndexWrite")
    def grant_index_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="grantPathRead")
    def grant_path_read(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="grantPathReadWrite")
    def grant_path_read_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="grantPathWrite")
    def grant_path_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Return the given named metric for this Domain.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for automated snapshot failures.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the cluster blocking index writes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 1 minute

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the time the cluster status is red.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the time the cluster status is yellow.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the storage space of nodes in the cluster.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for indexing latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for KMS key errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for KMS key being inaccessible.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for master CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for master JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the number of nodes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 1 hour

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for number of searchable documents.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for search latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        ...


class _IDomainProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''(deprecated) An interface that represents an Elasticsearch domain - either created with the CDK, or an existing one.

    :deprecated: use opensearchservice module instead

    :stability: deprecated
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_elasticsearch.IDomain"

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> builtins.str:
        '''(deprecated) Arn of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainArn"))

    @builtins.property
    @jsii.member(jsii_name="domainEndpoint")
    def domain_endpoint(self) -> builtins.str:
        '''(deprecated) Endpoint of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''(deprecated) Domain name of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @jsii.member(jsii_name="grantIndexRead")
    def grant_index_read(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ccaeb238f7b30786401c2827c04ce6111825e522dfae29b740cdd37dfe6cbdc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexRead", [index, identity]))

    @jsii.member(jsii_name="grantIndexReadWrite")
    def grant_index_read_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f9c08c3a8f02f3fa1bf1576162ae32dca8f3f784605722c4965e4db438431d7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexReadWrite", [index, identity]))

    @jsii.member(jsii_name="grantIndexWrite")
    def grant_index_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02ff8227a073e4e0bbfef61ac9a5f0106e87d5f21bfb7388d80fc97728c78f8f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexWrite", [index, identity]))

    @jsii.member(jsii_name="grantPathRead")
    def grant_path_read(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11b70f21de6a644862e1a9d9fb04c077e840536e44a77dc6b752a309e6fea5e9)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathRead", [path, identity]))

    @jsii.member(jsii_name="grantPathReadWrite")
    def grant_path_read_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3407a57df41c3c7228d78915f438b58ac3d079382524e1727d81cb9836a823cc)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathReadWrite", [path, identity]))

    @jsii.member(jsii_name="grantPathWrite")
    def grant_path_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__909088dd22e53a68a48b32ef1075f5f1624d5086e79fe28cc31ce5b5641f8c0e)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathWrite", [path, identity]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__826cd495c921e8d66ca83b7c48850a58a1663c9d03417a086568dd8c28203c26)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [identity]))

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f32909cfa0ecc236577c82eef5f45436aa6ff604ae5e26615268e050526fc541)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantReadWrite", [identity]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60413c39e0553f4a8e7c63645adcfd98e0ecac2f73913f52489bbdb210fea003)
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
        '''(deprecated) Return the given named metric for this Domain.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d57eb3601bc759c24057dad569672fc2cb9079f04ceb6aebc5be032bb2452f54)
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
        '''(deprecated) Metric for automated snapshot failures.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the cluster blocking index writes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 1 minute

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the time the cluster status is red.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the time the cluster status is yellow.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the storage space of nodes in the cluster.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for indexing latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for KMS key errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for KMS key being inaccessible.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for master CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for master JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the number of nodes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 1 hour

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for number of searchable documents.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for search latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticsearch.LoggingOptions",
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
        '''(deprecated) Configures log settings for the domain.

        :param app_log_enabled: (deprecated) Specify if Elasticsearch application logging should be set up. Requires Elasticsearch version 5.1 or later. Default: - false
        :param app_log_group: (deprecated) Log Elasticsearch application logs to this log group. Default: - a new log group is created if app logging is enabled
        :param audit_log_enabled: (deprecated) Specify if Elasticsearch audit logging should be set up. Requires Elasticsearch version 6.7 or later and fine grained access control to be enabled. Default: - false
        :param audit_log_group: (deprecated) Log Elasticsearch audit logs to this log group. Default: - a new log group is created if audit logging is enabled
        :param slow_index_log_enabled: (deprecated) Specify if slow index logging should be set up. Requires Elasticsearch version 5.1 or later. Default: - false
        :param slow_index_log_group: (deprecated) Log slow indices to this log group. Default: - a new log group is created if slow index logging is enabled
        :param slow_search_log_enabled: (deprecated) Specify if slow search logging should be set up. Requires Elasticsearch version 5.1 or later. Default: - false
        :param slow_search_log_group: (deprecated) Log slow searches to this log group. Default: - a new log group is created if slow search logging is enabled

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            prod_domain = es.Domain(self, "Domain",
                version=es.ElasticsearchVersion.V7_1,
                capacity=es.CapacityConfig(
                    master_nodes=5,
                    data_nodes=20
                ),
                ebs=es.EbsOptions(
                    volume_size=20
                ),
                zone_awareness=es.ZoneAwarenessConfig(
                    availability_zone_count=3
                ),
                logging=es.LoggingOptions(
                    slow_search_log_enabled=True,
                    app_log_enabled=True,
                    slow_index_log_enabled=True
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dda0d8a76f54b8392ae9f0570bfa9e5b2abb8a42412783d369ed3f3a3648d67)
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
        '''(deprecated) Specify if Elasticsearch application logging should be set up.

        Requires Elasticsearch version 5.1 or later.

        :default: - false

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("app_log_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def app_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''(deprecated) Log Elasticsearch application logs to this log group.

        :default: - a new log group is created if app logging is enabled

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("app_log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def audit_log_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Specify if Elasticsearch audit logging should be set up.

        Requires Elasticsearch version 6.7 or later and fine grained access control to be enabled.

        :default: - false

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("audit_log_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def audit_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''(deprecated) Log Elasticsearch audit logs to this log group.

        :default: - a new log group is created if audit logging is enabled

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("audit_log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def slow_index_log_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Specify if slow index logging should be set up.

        Requires Elasticsearch version 5.1 or later.

        :default: - false

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("slow_index_log_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def slow_index_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''(deprecated) Log slow indices to this log group.

        :default: - a new log group is created if slow index logging is enabled

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("slow_index_log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def slow_search_log_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Specify if slow search logging should be set up.

        Requires Elasticsearch version 5.1 or later.

        :default: - false

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("slow_search_log_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def slow_search_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''(deprecated) Log slow searches to this log group.

        :default: - a new log group is created if slow search logging is enabled

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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


@jsii.enum(jsii_type="aws-cdk-lib.aws_elasticsearch.TLSSecurityPolicy")
class TLSSecurityPolicy(enum.Enum):
    '''(deprecated) The minimum TLS version required for traffic to the domain.

    :deprecated: use opensearchservice module instead

    :stability: deprecated
    '''

    TLS_1_0 = "TLS_1_0"
    '''(deprecated) Cipher suite TLS 1.0.

    :stability: deprecated
    '''
    TLS_1_2 = "TLS_1_2"
    '''(deprecated) Cipher suite TLS 1.2.

    :stability: deprecated
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticsearch.ZoneAwarenessConfig",
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
        '''(deprecated) Specifies zone awareness configuration options.

        :param availability_zone_count: (deprecated) If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use. Valid values are 2 and 3. Default: - 2 if zone awareness is enabled.
        :param enabled: (deprecated) Indicates whether to enable zone awareness for the Amazon ES domain. When you enable zone awareness, Amazon ES allocates the nodes and replica index shards that belong to a cluster across two Availability Zones (AZs) in the same region to prevent data loss and minimize downtime in the event of node or data center failure. Don't enable zone awareness if your cluster has no replica index shards or is a single-node cluster. For more information, see [Configuring a Multi-AZ Domain] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-managedomains-multiaz) in the Amazon Elasticsearch Service Developer Guide. Default: - false

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            prod_domain = es.Domain(self, "Domain",
                version=es.ElasticsearchVersion.V7_1,
                capacity=es.CapacityConfig(
                    master_nodes=5,
                    data_nodes=20
                ),
                ebs=es.EbsOptions(
                    volume_size=20
                ),
                zone_awareness=es.ZoneAwarenessConfig(
                    availability_zone_count=3
                ),
                logging=es.LoggingOptions(
                    slow_search_log_enabled=True,
                    app_log_enabled=True,
                    slow_index_log_enabled=True
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9faeff8741d3083b95e5e5ad11c13dcf9b4880459b57a225fd03f80709d2bc91)
            check_type(argname="argument availability_zone_count", value=availability_zone_count, expected_type=type_hints["availability_zone_count"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zone_count is not None:
            self._values["availability_zone_count"] = availability_zone_count
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def availability_zone_count(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) If you enabled multiple Availability Zones (AZs), the number of AZs that you want the domain to use.

        Valid values are 2 and 3.

        :default: - 2 if zone awareness is enabled.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        result = self._values.get("availability_zone_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Indicates whether to enable zone awareness for the Amazon ES domain.

        When you enable zone awareness, Amazon ES allocates the nodes and replica
        index shards that belong to a cluster across two Availability Zones (AZs)
        in the same region to prevent data loss and minimize downtime in the event
        of node or data center failure. Don't enable zone awareness if your cluster
        has no replica index shards or is a single-node cluster. For more information,
        see [Configuring a Multi-AZ Domain]
        (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-managedomains-multiaz)
        in the Amazon Elasticsearch Service Developer Guide.

        :default: - false

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
    jsii_type="aws-cdk-lib.aws_elasticsearch.Domain",
):
    '''(deprecated) Provides an Elasticsearch domain.

    :deprecated: use opensearchservice module instead

    :stability: deprecated
    :exampleMetadata: infused

    Example::

        domain = es.Domain(self, "Domain",
            version=es.ElasticsearchVersion.V7_4,
            ebs=es.EbsOptions(
                volume_size=100,
                volume_type=ec2.EbsDeviceVolumeType.GENERAL_PURPOSE_SSD
            ),
            node_to_node_encryption=True,
            encryption_at_rest=es.EncryptionAtRestOptions(
                enabled=True
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        version: ElasticsearchVersion,
        access_policies: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
        capacity: typing.Optional[typing.Union[CapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        cognito_kibana_auth: typing.Optional[typing.Union[CognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_endpoint: typing.Optional[typing.Union[CustomEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        ebs: typing.Optional[typing.Union[EbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        enable_version_upgrade: typing.Optional[builtins.bool] = None,
        encryption_at_rest: typing.Optional[typing.Union[EncryptionAtRestOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        enforce_https: typing.Optional[builtins.bool] = None,
        fine_grained_access_control: typing.Optional[typing.Union[AdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union[LoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        node_to_node_encryption: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        tls_security_policy: typing.Optional[TLSSecurityPolicy] = None,
        use_unsigned_basic_auth: typing.Optional[builtins.bool] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
        zone_awareness: typing.Optional[typing.Union[ZoneAwarenessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param version: (deprecated) The Elasticsearch version that your domain will leverage.
        :param access_policies: (deprecated) Domain Access policies. Default: - No access policies.
        :param advanced_options: (deprecated) Additional options to specify for the Amazon ES domain. Default: - no advanced options are specified
        :param automated_snapshot_start_hour: (deprecated) The hour in UTC during which the service takes an automated daily snapshot of the indices in the Amazon ES domain. Only applies for Elasticsearch versions below 5.3. Default: - Hourly automated snapshots not used
        :param capacity: (deprecated) The cluster capacity configuration for the Amazon ES domain. Default: - 1 r5.large.elasticsearch data node; no dedicated master nodes.
        :param cognito_kibana_auth: (deprecated) Configures Amazon ES to use Amazon Cognito authentication for Kibana. Default: - Cognito not used for authentication to Kibana.
        :param custom_endpoint: (deprecated) To configure a custom domain configure these options. If you specify a Route53 hosted zone it will create a CNAME record and use DNS validation for the certificate Default: - no custom domain endpoint will be configured
        :param domain_name: (deprecated) Enforces a particular physical domain name. Default: - A name will be auto-generated.
        :param ebs: (deprecated) The configurations of Amazon Elastic Block Store (Amazon EBS) volumes that are attached to data nodes in the Amazon ES domain. For more information, see [Configuring EBS-based Storage] (https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs) in the Amazon Elasticsearch Service Developer Guide. Default: - 10 GiB General Purpose (SSD) volumes per node.
        :param enable_version_upgrade: (deprecated) To upgrade an Amazon ES domain to a new version of Elasticsearch rather than replacing the entire domain resource, use the EnableVersionUpgrade update policy. Default: - false
        :param encryption_at_rest: (deprecated) Encryption at rest options for the cluster. Default: - No encryption at rest
        :param enforce_https: (deprecated) True to require that all traffic to the domain arrive over HTTPS. Default: - false
        :param fine_grained_access_control: (deprecated) Specifies options for fine-grained access control. Requires Elasticsearch version 6.7 or later. Enabling fine-grained access control also requires encryption of data at rest and node-to-node encryption, along with enforced HTTPS. Default: - fine-grained access control is disabled
        :param logging: (deprecated) Configuration log publishing configuration options. Default: - No logs are published
        :param node_to_node_encryption: (deprecated) Specify true to enable node to node encryption. Requires Elasticsearch version 6.0 or later. Default: - Node to node encryption is not enabled.
        :param removal_policy: (deprecated) Policy to apply when the domain is removed from the stack. Default: RemovalPolicy.RETAIN
        :param security_groups: (deprecated) The list of security groups that are associated with the VPC endpoints for the domain. Only used if ``vpc`` is specified. Default: - One new security group is created.
        :param tls_security_policy: (deprecated) The minimum TLS version required for traffic to the domain. Default: - TLSSecurityPolicy.TLS_1_0
        :param use_unsigned_basic_auth: (deprecated) Configures the domain so that unsigned basic auth is enabled. If no master user is provided a default master user with username ``admin`` and a dynamically generated password stored in KMS is created. The password can be retrieved by getting ``masterUserPassword`` from the domain instance. Setting this to true will also add an access policy that allows unsigned access, enable node to node encryption, encryption at rest. If conflicting settings are encountered (like disabling encryption at rest) enabling this setting will cause a failure. Default: - false
        :param vpc: (deprecated) Place the domain inside this VPC. Default: - Domain is not placed in a VPC.
        :param vpc_subnets: (deprecated) The specific vpc subnets the domain will be placed in. You must provide one subnet for each Availability Zone that your domain uses. For example, you must specify three subnet IDs for a three Availability Zone domain. Only used if ``vpc`` is specified. Default: - All private subnets.
        :param zone_awareness: (deprecated) The cluster zone awareness configuration for the Amazon ES domain. Default: - no zone awareness (1 AZ)

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbdbf226e2baf01ef42124d519bb303c1fcf8cf699542d2fe9de51d9f05267eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DomainProps(
            version=version,
            access_policies=access_policies,
            advanced_options=advanced_options,
            automated_snapshot_start_hour=automated_snapshot_start_hour,
            capacity=capacity,
            cognito_kibana_auth=cognito_kibana_auth,
            custom_endpoint=custom_endpoint,
            domain_name=domain_name,
            ebs=ebs,
            enable_version_upgrade=enable_version_upgrade,
            encryption_at_rest=encryption_at_rest,
            enforce_https=enforce_https,
            fine_grained_access_control=fine_grained_access_control,
            logging=logging,
            node_to_node_encryption=node_to_node_encryption,
            removal_policy=removal_policy,
            security_groups=security_groups,
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
        '''(deprecated) Creates a Domain construct that represents an external domain.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param domain_arn: (deprecated) The ARN of the Elasticsearch domain.
        :param domain_endpoint: (deprecated) The domain endpoint of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1578237197975d297e75ac31d44eb072631ae3dfdd50f24f9cf586ef7940e8ff)
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
        '''(deprecated) Creates a Domain construct that represents an external domain via domain endpoint.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param domain_endpoint: The domain's endpoint.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42273fd9811855dcd93d5e7b9f75b23736f6c39244632fa223065305fa21df2c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain_endpoint", value=domain_endpoint, expected_type=type_hints["domain_endpoint"])
        return typing.cast(IDomain, jsii.sinvoke(cls, "fromDomainEndpoint", [scope, id, domain_endpoint]))

    @jsii.member(jsii_name="addAccessPolicies")
    def add_access_policies(
        self,
        *access_policy_statements: _PolicyStatement_0fe33853,
    ) -> None:
        '''(deprecated) Add policy statements to the domain access policy.

        :param access_policy_statements: -

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5c984bd8b8cde913a3957a04e50dca902c00fe1f9b7f0e01aae20bf3903a297)
            check_type(argname="argument access_policy_statements", value=access_policy_statements, expected_type=typing.Tuple[type_hints["access_policy_statements"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addAccessPolicies", [*access_policy_statements]))

    @jsii.member(jsii_name="grantIndexRead")
    def grant_index_read(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1f1e2f573a5144de46ffbe432c1cdaaecca9fccc5ba231f8e2c495dd4d27ee7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexRead", [index, identity]))

    @jsii.member(jsii_name="grantIndexReadWrite")
    def grant_index_read_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2be83a0f10059d07d54d215f92253686c1a357106cfb651c82ced564c1d9d3f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexReadWrite", [index, identity]))

    @jsii.member(jsii_name="grantIndexWrite")
    def grant_index_write(
        self,
        index: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for an index in this domain to an IAM principal (Role/Group/User).

        :param index: The index to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a732cffdcdbf78512f23387e81387383bca7d1a6f59e3cc89a7b7247f19571dc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantIndexWrite", [index, identity]))

    @jsii.member(jsii_name="grantPathRead")
    def grant_path_read(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de89ad22608fda131eb6cfb8c9280a70a2aeb9425d3287a9a6f78b3a1828d74)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathRead", [path, identity]))

    @jsii.member(jsii_name="grantPathReadWrite")
    def grant_path_read_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__893763408b1d73a810961240921a66095c453b6bdb08a47365f43945a1e6e323)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathReadWrite", [path, identity]))

    @jsii.member(jsii_name="grantPathWrite")
    def grant_path_write(
        self,
        path: builtins.str,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for a specific path in this domain to an IAM principal (Role/Group/User).

        :param path: The path to grant permissions for.
        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db02cf727b46d136f09bb49c57c75dcc33b77da86777792d1d20aa36aa2933cb)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPathWrite", [path, identity]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8467027a310ea82622abe2b5039879d2718127253c411a2c81aade7cbb2b46e3)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [identity]))

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant read/write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c79151855e153615bdb47cb5fd414a1186ac8edd2fc05ea62193b107e9f712a)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantReadWrite", [identity]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(deprecated) Grant write permissions for this domain and its contents to an IAM principal (Role/Group/User).

        :param identity: The principal.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4e5fe2d36d21e989452bbfe4a2528b536b9889bc7907cf4969e1d40bee4946e)
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
        '''(deprecated) Return the given named metric for this Domain.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5543e4b1f496b09cc4a434231d283ad21ff49080e145c70f79d585e68858818)
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
        '''(deprecated) Metric for automated snapshot failures.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the cluster blocking index writes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 1 minute

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the time the cluster status is red.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the time the cluster status is yellow.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the storage space of nodes in the cluster.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for indexing latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for KMS key errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for KMS key being inaccessible.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for master CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for master JVM memory pressure.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for the number of nodes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: minimum over 1 hour

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for number of searchable documents.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: maximum over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Metric for search latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: p99 over 5 minutes

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
        '''(deprecated) Manages network connections to the domain.

        This will throw an error in case the domain
        is not placed inside a VPC.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> builtins.str:
        '''(deprecated) Arn of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainArn"))

    @builtins.property
    @jsii.member(jsii_name="domainEndpoint")
    def domain_endpoint(self) -> builtins.str:
        '''(deprecated) Endpoint of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''(deprecated) Domain name of the Elasticsearch domain.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @builtins.property
    @jsii.member(jsii_name="appLogGroup")
    def app_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''(deprecated) Log group that application logs are logged to.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "appLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="auditLogGroup")
    def audit_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''(deprecated) Log group that audit logs are logged to.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "auditLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> typing.Optional[_SecretValue_3dd0ddae]:
        '''(deprecated) Master user password if fine grained access control is configured.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[_SecretValue_3dd0ddae], jsii.get(self, "masterUserPassword"))

    @builtins.property
    @jsii.member(jsii_name="slowIndexLogGroup")
    def slow_index_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''(deprecated) Log group that slow indices are logged to.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "slowIndexLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="slowSearchLogGroup")
    def slow_search_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''(deprecated) Log group that slow searches are logged to.

        :deprecated: use opensearchservice module instead

        :stability: deprecated
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
    "ElasticsearchVersion",
    "EncryptionAtRestOptions",
    "IDomain",
    "LoggingOptions",
    "TLSSecurityPolicy",
    "ZoneAwarenessConfig",
]

publication.publish()

def _typecheckingstub__bdc9b40ba6fb43b768fc771b2453634a195e8312344879b8f85c37c34d026712(
    *,
    master_user_arn: typing.Optional[builtins.str] = None,
    master_user_name: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[_SecretValue_3dd0ddae] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d904c51cccabe441d3da72a1444303ff901ccd33acf1e26faf7fc107055a594a(
    *,
    data_node_instance_type: typing.Optional[builtins.str] = None,
    data_nodes: typing.Optional[jsii.Number] = None,
    master_node_instance_type: typing.Optional[builtins.str] = None,
    master_nodes: typing.Optional[jsii.Number] = None,
    warm_instance_type: typing.Optional[builtins.str] = None,
    warm_nodes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63b7f3680a648547d6da1f542a01684f9c4d84033f4c9aee8eaecae81537b8f4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_policies: typing.Any = None,
    advanced_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    advanced_security_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.AdvancedSecurityOptionsInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cognito_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.CognitoOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    domain_endpoint_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.DomainEndpointOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_name: typing.Optional[builtins.str] = None,
    ebs_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EBSOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_cluster_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ElasticsearchClusterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_version: typing.Optional[builtins.str] = None,
    encryption_at_rest_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EncryptionAtRestOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.LogPublishingOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    node_to_node_encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.NodeToNodeEncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snapshot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SnapshotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.VPCOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd2d18eaac7c83ff0634d3cb6e2c71e76889773e8b7a399c0dd5aa637bd6ae89(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f966c6cd4c4c0e8fc1b00589d54a432ec5b02208b1097ed5e485a3deaa1a3737(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e88303355599d25861730b061f1bc223b85a3768dad89b9fe895dcb0acbb018(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eccb4465105fe2d68c634cb9897defc7a979b09c5873770bdb861cc3cf9f6050(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9970ee48d4d95c4a50fba27f7ecf5d29a7799901a417a50d5ea2d80bb2a7da73(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.AdvancedSecurityOptionsInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee253fc130f6145a5f54d7b09ff1166a449bd9ecc8b1142d2cd799fd8c3e8122(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.CognitoOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8adbdde3df8afce52a188616c8a9ed40b29c6c6ea3a14493572b5169a4bbcaaf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff33eeb03219f470f43d7c038ac4ad48acfa3561168de4acd90068625c223f8f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.DomainEndpointOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__547819c192aff9b477504559c5f7c768a4e9c9606b6bcb8fed954fa8a2f967c5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92aff95c5a4b46939639f06cb47d5cb23bc8cce780233b7fed861d0a33b21b3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EBSOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e4164981f0950c083faf5427ec43d8fa41b58062af5ea5e2be947066d05721(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.ElasticsearchClusterConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e2effedbe60ffc2fb8fe65b2cdddd9a29cfdcb61eef184721846e6b028414da(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2f6f3e7bbcfd1c4ed35e1ea39cf14fc7af68d4b175db0fd18d69c66b89ad9d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.EncryptionAtRestOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b68ea5f4731e0bc02f7a196cd4b14d0ac22f6e22a661283031c3be761ff5c610(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnDomain.LogPublishingOptionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a665cc917a112af2348ce54c28aa2743e93ef9dabf60cfbee200092f3bb7c6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.NodeToNodeEncryptionOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ceb39ec0c3dca28571cbfbe9689bd6457a60fd17d054c9abf0a2c09165aef74(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SnapshotOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9076d2462cf49a948d9ea5d30b6392387174b389efc4e1dda4e4789f95edc66(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff64c1f5c7bb8053ed4408ea633c0472baa0e83f0f43be1e87eb569f30f6739(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.VPCOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20207c85ae0a336344b4986652cfbfc4af27b1a56d54ba31ff6505ea1db70a1b(
    *,
    anonymous_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    master_user_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.MasterUserOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595a6b3cdf3d5b32c86feb7dca3af8642c7eda687b4fb444faedfa8415028e7d(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    identity_pool_id: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    user_pool_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b29fbd709c231836e96b61f6b1dd17e4b87fdbcd26d4ec292f768b17478c922f(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a315182feb03d4b11e7632eea35a2f35d8b19b801ecb799c3744b2ed0bc11a76(
    *,
    custom_endpoint: typing.Optional[builtins.str] = None,
    custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
    custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enforce_https: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tls_security_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0a4bb0d03dd89e8279b9e57e4a68e7f2fce71595722dbad5fada43cc1b15616(
    *,
    ebs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36ac2eb43dd2dc644b88b3f9db0f58ead2dbb47ffc23f3d8fc546f53bfcefb4a(
    *,
    cold_storage_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ColdStorageOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dedicated_master_count: typing.Optional[jsii.Number] = None,
    dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    dedicated_master_type: typing.Optional[builtins.str] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    instance_type: typing.Optional[builtins.str] = None,
    warm_count: typing.Optional[jsii.Number] = None,
    warm_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    warm_type: typing.Optional[builtins.str] = None,
    zone_awareness_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ZoneAwarenessConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee9f0aff26691f651a27c328864208a5480af26681c2baa3afdcc6b1f8cb27b(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e7d124e6174f5352d66bdbb642c851ec6bf4aba9f8fcb6bf19e34809e37f6a9(
    *,
    cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86df1024036528c38c1cc3918e4413fdd5adee94c59ff0dba9e2625c1f7f6735(
    *,
    master_user_arn: typing.Optional[builtins.str] = None,
    master_user_name: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79b4e8cc645055321e0aea8e7724655ea101aae985769f93812bc6db0624eb53(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd199cc313b4bdbae2613aaf1084d93eab6fb227123efcd5eccb919a3c431497(
    *,
    automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931aa1b11d25d7c92725f2e141ddba7562e992b6b38363844ccfcbd524041b69(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee73d0667237b38d27f617dfe56f8c57182f358686fa721ebadbe9d9730d747(
    *,
    availability_zone_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9cf4a1cacc663baa0bc99c7e4784f1bb4a208a6851dceb6a846d215d5062938(
    *,
    access_policies: typing.Any = None,
    advanced_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    advanced_security_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.AdvancedSecurityOptionsInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cognito_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.CognitoOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    domain_endpoint_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.DomainEndpointOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_name: typing.Optional[builtins.str] = None,
    ebs_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EBSOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_cluster_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ElasticsearchClusterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_version: typing.Optional[builtins.str] = None,
    encryption_at_rest_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.EncryptionAtRestOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.LogPublishingOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    node_to_node_encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.NodeToNodeEncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snapshot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SnapshotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.VPCOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b524e8e96dadc613c3ade2864195ce643f52df86cc22205eeea1f5a1b04715fa(
    *,
    identity_pool_id: builtins.str,
    role: _IRole_235f5d8e,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea711a6b742c02c3c27fa537028f874f857943b01e96d2167b14a0d27de9a54(
    *,
    domain_name: builtins.str,
    certificate: typing.Optional[_ICertificate_c194c70b] = None,
    hosted_zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72419130e136fdde5577319d89e912d0d4cabd7e160115eb7fb1c0f589469870(
    *,
    domain_arn: builtins.str,
    domain_endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572eb3999b8c38b39f33fa525daa95c090ed063b8212bb3a0e6f1f533bb2064e(
    *,
    version: ElasticsearchVersion,
    access_policies: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
    capacity: typing.Optional[typing.Union[CapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    cognito_kibana_auth: typing.Optional[typing.Union[CognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_endpoint: typing.Optional[typing.Union[CustomEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[EbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_version_upgrade: typing.Optional[builtins.bool] = None,
    encryption_at_rest: typing.Optional[typing.Union[EncryptionAtRestOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enforce_https: typing.Optional[builtins.bool] = None,
    fine_grained_access_control: typing.Optional[typing.Union[AdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    logging: typing.Optional[typing.Union[LoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    node_to_node_encryption: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    tls_security_policy: typing.Optional[TLSSecurityPolicy] = None,
    use_unsigned_basic_auth: typing.Optional[builtins.bool] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
    zone_awareness: typing.Optional[typing.Union[ZoneAwarenessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__653b4b977dd3a1aabb16baf6f32203c90668a1bdcac85452086445b36c330954(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    iops: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[_EbsDeviceVolumeType_6792555b] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94cee41a2246511ec77c9b6a556875c250b85ee87cddd5b0cc76dea112a4625f(
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0566221450862dc46d961944b4613c299ea2ba900c19e9652b8e47501e1b0a(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    kms_key: typing.Optional[_IKey_5f11635f] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ccaeb238f7b30786401c2827c04ce6111825e522dfae29b740cdd37dfe6cbdc(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f9c08c3a8f02f3fa1bf1576162ae32dca8f3f784605722c4965e4db438431d7(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ff8227a073e4e0bbfef61ac9a5f0106e87d5f21bfb7388d80fc97728c78f8f(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11b70f21de6a644862e1a9d9fb04c077e840536e44a77dc6b752a309e6fea5e9(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3407a57df41c3c7228d78915f438b58ac3d079382524e1727d81cb9836a823cc(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__909088dd22e53a68a48b32ef1075f5f1624d5086e79fe28cc31ce5b5641f8c0e(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__826cd495c921e8d66ca83b7c48850a58a1663c9d03417a086568dd8c28203c26(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f32909cfa0ecc236577c82eef5f45436aa6ff604ae5e26615268e050526fc541(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60413c39e0553f4a8e7c63645adcfd98e0ecac2f73913f52489bbdb210fea003(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d57eb3601bc759c24057dad569672fc2cb9079f04ceb6aebc5be032bb2452f54(
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

def _typecheckingstub__1dda0d8a76f54b8392ae9f0570bfa9e5b2abb8a42412783d369ed3f3a3648d67(
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

def _typecheckingstub__9faeff8741d3083b95e5e5ad11c13dcf9b4880459b57a225fd03f80709d2bc91(
    *,
    availability_zone_count: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbdbf226e2baf01ef42124d519bb303c1fcf8cf699542d2fe9de51d9f05267eb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    version: ElasticsearchVersion,
    access_policies: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    automated_snapshot_start_hour: typing.Optional[jsii.Number] = None,
    capacity: typing.Optional[typing.Union[CapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    cognito_kibana_auth: typing.Optional[typing.Union[CognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_endpoint: typing.Optional[typing.Union[CustomEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[EbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_version_upgrade: typing.Optional[builtins.bool] = None,
    encryption_at_rest: typing.Optional[typing.Union[EncryptionAtRestOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enforce_https: typing.Optional[builtins.bool] = None,
    fine_grained_access_control: typing.Optional[typing.Union[AdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    logging: typing.Optional[typing.Union[LoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    node_to_node_encryption: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    tls_security_policy: typing.Optional[TLSSecurityPolicy] = None,
    use_unsigned_basic_auth: typing.Optional[builtins.bool] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Sequence[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]]] = None,
    zone_awareness: typing.Optional[typing.Union[ZoneAwarenessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1578237197975d297e75ac31d44eb072631ae3dfdd50f24f9cf586ef7940e8ff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_arn: builtins.str,
    domain_endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42273fd9811855dcd93d5e7b9f75b23736f6c39244632fa223065305fa21df2c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    domain_endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c984bd8b8cde913a3957a04e50dca902c00fe1f9b7f0e01aae20bf3903a297(
    *access_policy_statements: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1f1e2f573a5144de46ffbe432c1cdaaecca9fccc5ba231f8e2c495dd4d27ee7(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2be83a0f10059d07d54d215f92253686c1a357106cfb651c82ced564c1d9d3f(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a732cffdcdbf78512f23387e81387383bca7d1a6f59e3cc89a7b7247f19571dc(
    index: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de89ad22608fda131eb6cfb8c9280a70a2aeb9425d3287a9a6f78b3a1828d74(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__893763408b1d73a810961240921a66095c453b6bdb08a47365f43945a1e6e323(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db02cf727b46d136f09bb49c57c75dcc33b77da86777792d1d20aa36aa2933cb(
    path: builtins.str,
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8467027a310ea82622abe2b5039879d2718127253c411a2c81aade7cbb2b46e3(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c79151855e153615bdb47cb5fd414a1186ac8edd2fc05ea62193b107e9f712a(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4e5fe2d36d21e989452bbfe4a2528b536b9889bc7907cf4969e1d40bee4946e(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5543e4b1f496b09cc4a434231d283ad21ff49080e145c70f79d585e68858818(
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
