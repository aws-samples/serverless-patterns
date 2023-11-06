'''
# AWS AppSync Construct Library

The `aws-cdk-lib/aws-appsync` package contains constructs for building flexible
APIs that use GraphQL.

```python
import aws_cdk.aws_appsync as appsync
```

## Example

### DynamoDB

Example of a GraphQL API with `AWS_IAM` [authorization](#authorization) resolving into a DynamoDb
backend data source.

GraphQL schema file `schema.graphql`:

```gql
type demo {
  id: String!
  version: String!
}
type Query {
  getDemos: [ demo! ]
}
input DemoInput {
  version: String!
}
type Mutation {
  addDemo(input: DemoInput!): demo
}
```

CDK stack file `app-stack.ts`:

```python
api = appsync.GraphqlApi(self, "Api",
    name="demo",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
    authorization_config=appsync.AuthorizationConfig(
        default_authorization=appsync.AuthorizationMode(
            authorization_type=appsync.AuthorizationType.IAM
        )
    ),
    xray_enabled=True
)

demo_table = dynamodb.Table(self, "DemoTable",
    partition_key=dynamodb.Attribute(
        name="id",
        type=dynamodb.AttributeType.STRING
    )
)

demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)

# Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
# Resolver Mapping Template Reference:
# https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
demo_dS.create_resolver("QueryGetDemosResolver",
    type_name="Query",
    field_name="getDemos",
    request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
    response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
)

# Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
demo_dS.create_resolver("MutationAddDemoResolver",
    type_name="Mutation",
    field_name="addDemo",
    request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
        appsync.PrimaryKey.partition("id").auto(),
        appsync.Values.projecting("input")),
    response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
)

# To enable DynamoDB read consistency with the `MappingTemplate`:
demo_dS.create_resolver("QueryGetDemosConsistentResolver",
    type_name="Query",
    field_name="getDemosConsistent",
    request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
    response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
)
```

### Aurora Serverless

AppSync provides a data source for executing SQL commands against Amazon Aurora
Serverless clusters. You can use AppSync resolvers to execute SQL statements
against the Data API with GraphQL queries, mutations, and subscriptions.

```python
# Build a data source for AppSync to access the database.
# api: appsync.GraphqlApi
# Create username and password secret for DB Cluster
secret = rds.DatabaseSecret(self, "AuroraSecret",
    username="clusteradmin"
)

# The VPC to place the cluster in
vpc = ec2.Vpc(self, "AuroraVpc")

# Create the serverless cluster, provide all values needed to customise the database.
cluster = rds.ServerlessCluster(self, "AuroraCluster",
    engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
    vpc=vpc,
    credentials={"username": "clusteradmin"},
    cluster_identifier="db-endpoint-test",
    default_database_name="demos"
)
rds_dS = api.add_rds_data_source("rds", cluster, secret, "demos")

# Set up a resolver for an RDS query.
rds_dS.create_resolver("QueryGetDemosRdsResolver",
    type_name="Query",
    field_name="getDemosRds",
    request_mapping_template=appsync.MappingTemplate.from_string("""
          {
            "version": "2018-05-29",
            "statements": [
              "SELECT * FROM demos"
            ]
          }
          """),
    response_mapping_template=appsync.MappingTemplate.from_string("""
            $utils.toJson($utils.rds.toJsonObject($ctx.result)[0])
          """)
)

# Set up a resolver for an RDS mutation.
rds_dS.create_resolver("MutationAddDemoRdsResolver",
    type_name="Mutation",
    field_name="addDemoRds",
    request_mapping_template=appsync.MappingTemplate.from_string("""
          {
            "version": "2018-05-29",
            "statements": [
              "INSERT INTO demos VALUES (:id, :version)",
              "SELECT * WHERE id = :id"
            ],
            "variableMap": {
              ":id": $util.toJson($util.autoId()),
              ":version": $util.toJson($ctx.args.version)
            }
          }
          """),
    response_mapping_template=appsync.MappingTemplate.from_string("""
            $utils.toJson($utils.rds.toJsonObject($ctx.result)[1][0])
          """)
)
```

### HTTP Endpoints

GraphQL schema file `schema.graphql`:

```gql
type job {
  id: String!
  version: String!
}

input DemoInput {
  version: String!
}

type Mutation {
  callStepFunction(input: DemoInput!): job
}
```

GraphQL request mapping template `request.vtl`:

```json
{
  "version": "2018-05-29",
  "method": "POST",
  "resourcePath": "/",
  "params": {
    "headers": {
      "content-type": "application/x-amz-json-1.0",
      "x-amz-target":"AWSStepFunctions.StartExecution"
    },
    "body": {
      "stateMachineArn": "<your step functions arn>",
      "input": "{ \"id\": \"$context.arguments.id\" }"
    }
  }
}
```

GraphQL response mapping template `response.vtl`:

```json
{
  "id": "${context.result.id}"
}
```

CDK stack file `app-stack.ts`:

```python
api = appsync.GraphqlApi(self, "api",
    name="api",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
)

http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
    name="httpDsWithStepF",
    description="from appsync to StepFunctions Workflow",
    authorization_config=appsync.AwsIamConfig(
        signing_region="us-east-1",
        signing_service_name="states"
    )
)

http_ds.create_resolver("MutationCallStepFunctionResolver",
    type_name="Mutation",
    field_name="callStepFunction",
    request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
    response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
)
```

### EventBridge

Integrating AppSync with EventBridge enables developers to use EventBridge rules to route commands for GraphQl mutations
that need to perform any one of a variety of asynchronous tasks. More broadly, it enables teams to expose an event bus
as a part of a GraphQl schema.

GraphQL schema file `schema.graphql`:

```gql
schema {
    query: Query
    mutation: Mutation
}

type Query {
    event(id:ID!): Event
}

type Mutation {
    emitEvent(id: ID!, name: String): PutEventsResult!
}

type Event {
    id: ID!
    name: String!
}

type Entry {
    ErrorCode: String
    ErrorMessage: String
    EventId: String
}

type PutEventsResult {
    Entries: [Entry!]
    FailedEntry: Int
}
```

GraphQL request mapping template `request.vtl`:

```
{
    "version" : "2018-05-29",
    "operation": "PutEvents",
    "events" : [
        {
            "source": "integ.appsync.eventbridge",
            "detailType": "Mutation.emitEvent",
            "detail": $util.toJson($context.arguments)
        }
    ]
}
```

GraphQL response mapping template `response.vtl`:

```
$util.toJson($ctx.result)'
```

This response mapping template simply converts the EventBridge PutEvents result to JSON.
For details about the response see the
[documentation](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html).
Additional logic can be added to the response template to map the response type, or to error in the event of failed
events. More information can be found
[here](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-eventbridge.html).

CDK stack file `app-stack.ts`:

```python
import aws_cdk.aws_events as events


api = appsync.GraphqlApi(self, "EventBridgeApi",
    name="EventBridgeApi",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.eventbridge.graphql"))
)

bus = events.EventBus(self, "DestinationEventBus")

data_source = api.add_event_bridge_data_source("NoneDS", bus)

data_source.create_resolver("EventResolver",
    type_name="Mutation",
    field_name="emitEvent",
    request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
    response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
)
```

### Amazon OpenSearch Service

AppSync has builtin support for Amazon OpenSearch Service (successor to Amazon
Elasticsearch Service) from domains that are provisioned through your AWS account. You can
use AppSync resolvers to perform GraphQL operations such as queries, mutations, and
subscriptions.

```python
import aws_cdk.aws_opensearchservice as opensearch

# api: appsync.GraphqlApi


user = iam.User(self, "User")
domain = opensearch.Domain(self, "Domain",
    version=opensearch.EngineVersion.OPENSEARCH_2_3,
    removal_policy=RemovalPolicy.DESTROY,
    fine_grained_access_control=opensearch.AdvancedSecurityOptions(master_user_arn=user.user_arn),
    encryption_at_rest=opensearch.EncryptionAtRestOptions(enabled=True),
    node_to_node_encryption=True,
    enforce_https=True
)
ds = api.add_open_search_data_source("ds", domain)

ds.create_resolver("QueryGetTestsResolver",
    type_name="Query",
    field_name="getTests",
    request_mapping_template=appsync.MappingTemplate.from_string(JSON.stringify({
        "version": "2017-02-28",
        "operation": "GET",
        "path": "/id/post/_search",
        "params": {
            "headers": {},
            "query_string": {},
            "body": {"from": 0, "size": 50}
        }
    })),
    response_mapping_template=appsync.MappingTemplate.from_string("""[
            #foreach($entry in $context.result.hits.hits)
            #if( $velocityCount > 1 ) , #end
            $utils.toJson($entry.get("_source"))
            #end
          ]""")
)
```

## Custom Domain Names

For many use cases you may want to associate a custom domain name with your
GraphQL API. This can be done during the API creation.

```python
import aws_cdk.aws_certificatemanager as acm
import aws_cdk.aws_route53 as route53

# hosted zone and route53 features
# hosted_zone_id: str
zone_name = "example.com"


my_domain_name = "api.example.com"
certificate = acm.Certificate(self, "cert", domain_name=my_domain_name)
schema = appsync.SchemaFile(file_path="mySchemaFile")
api = appsync.GraphqlApi(self, "api",
    name="myApi",
    schema=schema,
    domain_name=appsync.DomainOptions(
        certificate=certificate,
        domain_name=my_domain_name
    )
)

# hosted zone for adding appsync domain
zone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
    hosted_zone_id=hosted_zone_id,
    zone_name=zone_name
)

# create a cname to the appsync domain. will map to something like xxxx.cloudfront.net
route53.CnameRecord(self, "CnameApiRecord",
    record_name="api",
    zone=zone,
    domain_name=api.app_sync_domain_name
)
```

## Log Group

AppSync automatically create a log group with the name `/aws/appsync/apis/<graphql_api_id>` upon deployment with
log data set to never expire. If you want to set a different expiration period, use the `logConfig.retention` property.

To obtain the GraphQL API's log group as a `logs.ILogGroup` use the `logGroup` property of the
`GraphqlApi` construct.

```python
import aws_cdk.aws_logs as logs


log_config = appsync.LogConfig(
    retention=logs.RetentionDays.ONE_WEEK
)

appsync.GraphqlApi(self, "api",
    authorization_config=appsync.AuthorizationConfig(),
    name="myApi",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "myApi.graphql")),
    log_config=log_config
)
```

## Schema

You can define a schema using from a local file using `SchemaFile.fromAsset`

```python
api = appsync.GraphqlApi(self, "api",
    name="myApi",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphl"))
)
```

### ISchema

Alternative schema sources can be defined by implementing the `ISchema`
interface. An example of this is the `CodeFirstSchema` class provided in
[awscdk-appsync-utils](https://github.com/cdklabs/awscdk-appsync-utils)

## Imports

Any GraphQL Api that has been created outside the stack can be imported from
another stack into your CDK app. Utilizing the `fromXxx` function, you have
the ability to add data sources and resolvers through a `IGraphqlApi` interface.

```python
# api: appsync.GraphqlApi
# table: dynamodb.Table

imported_api = appsync.GraphqlApi.from_graphql_api_attributes(self, "IApi",
    graphql_api_id=api.api_id,
    graphql_api_arn=api.arn
)
imported_api.add_dynamo_db_data_source("TableDataSource", table)
```

If you don't specify `graphqlArn` in `fromXxxAttributes`, CDK will autogenerate
the expected `arn` for the imported api, given the `apiId`. For creating data
sources and resolvers, an `apiId` is sufficient.

## Private APIs

By default all AppSync GraphQL APIs are public and can be accessed from the internet.
For customers that want to limit access to be from their VPC, the optional API `visibility` property can be set to `Visibility.PRIVATE`
at creation time. To explicitly create a public API, the `visibility` property should be set to `Visibility.GLOBAL`.
If visibility is not set, the service will default to `GLOBAL`.

CDK stack file `app-stack.ts`:

```python
api = appsync.GraphqlApi(self, "api",
    name="MyPrivateAPI",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.schema.graphql")),
    visibility=appsync.Visibility.PRIVATE
)
```

See [documentation](https://docs.aws.amazon.com/appsync/latest/devguide/using-private-apis.html)
for more details about Private APIs

## Authorization

There are multiple authorization types available for GraphQL API to cater to different
access use cases. They are:

* API Keys (`AuthorizationType.API_KEY`)
* Amazon Cognito User Pools (`AuthorizationType.USER_POOL`)
* OpenID Connect (`AuthorizationType.OPENID_CONNECT`)
* AWS Identity and Access Management (`AuthorizationType.AWS_IAM`)
* AWS Lambda (`AuthorizationType.AWS_LAMBDA`)

These types can be used simultaneously in a single API, allowing different types of clients to
access data. When you specify an authorization type, you can also specify the corresponding
authorization mode to finish defining your authorization. For example, this is a GraphQL API
with AWS Lambda Authorization.

```python
import aws_cdk.aws_lambda as lambda_
# auth_function: lambda.Function


appsync.GraphqlApi(self, "api",
    name="api",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.test.graphql")),
    authorization_config=appsync.AuthorizationConfig(
        default_authorization=appsync.AuthorizationMode(
            authorization_type=appsync.AuthorizationType.LAMBDA,
            lambda_authorizer_config=appsync.LambdaAuthorizerConfig(
                handler=auth_function
            )
        )
    )
)
```

## Permissions

When using `AWS_IAM` as the authorization type for GraphQL API, an IAM Role
with correct permissions must be used for access to API.

When configuring permissions, you can specify specific resources to only be
accessible by `IAM` authorization. For example, if you want to only allow mutability
for `IAM` authorized access you would configure the following.

In `schema.graphql`:

```gql
type Mutation {
  updateExample(...): ...
    @aws_iam
}
```

In `IAM`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "appsync:GraphQL"
      ],
      "Resource": [
        "arn:aws:appsync:REGION:ACCOUNT_ID:apis/GRAPHQL_ID/types/Mutation/fields/updateExample"
      ]
    }
  ]
}
```

See [documentation](https://docs.aws.amazon.com/appsync/latest/devguide/security.html#aws-iam-authorization) for more details.

To make this easier, CDK provides `grant` API.

Use the `grant` function for more granular authorization.

```python
# api: appsync.GraphqlApi
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)

api.grant(role, appsync.IamResource.custom("types/Mutation/fields/updateExample"), "appsync:GraphQL")
```

### IamResource

In order to use the `grant` functions, you need to use the class `IamResource`.

* `IamResource.custom(...arns)` permits custom ARNs and requires an argument.
* `IamResouce.ofType(type, ...fields)` permits ARNs for types and their fields.
* `IamResource.all()` permits ALL resources.

### Generic Permissions

Alternatively, you can use more generic `grant` functions to accomplish the same usage.

These include:

* grantMutation (use to grant access to Mutation fields)
* grantQuery (use to grant access to Query fields)
* grantSubscription (use to grant access to Subscription fields)

```python
# api: appsync.GraphqlApi
# role: iam.Role


# For generic types
api.grant_mutation(role, "updateExample")

# For custom types and granular design
api.grant(role, appsync.IamResource.of_type("Mutation", "updateExample"), "appsync:GraphQL")
```

## Pipeline Resolvers and AppSync Functions

AppSync Functions are local functions that perform certain operations onto a
backend data source. Developers can compose operations (Functions) and execute
them in sequence with Pipeline Resolvers.

```python
# api: appsync.GraphqlApi


appsync_function = appsync.AppsyncFunction(self, "function",
    name="appsync_function",
    api=api,
    data_source=api.add_none_data_source("none"),
    request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
    response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
)
```

AppSync Functions are used in tandem with pipeline resolvers to compose multiple
operations.

```python
# api: appsync.GraphqlApi
# appsync_function: appsync.AppsyncFunction


pipeline_resolver = appsync.Resolver(self, "pipeline",
    api=api,
    data_source=api.add_none_data_source("none"),
    type_name="typeName",
    field_name="fieldName",
    request_mapping_template=appsync.MappingTemplate.from_file("beforeRequest.vtl"),
    pipeline_config=[appsync_function],
    response_mapping_template=appsync.MappingTemplate.from_file("afterResponse.vtl")
)
```

### JS Functions and Resolvers

JS Functions and resolvers are also supported. You can use a `.js` file within your CDK project, or specify your function code inline.

```python
# api: appsync.GraphqlApi


my_js_function = appsync.AppsyncFunction(self, "function",
    name="my_js_function",
    api=api,
    data_source=api.add_none_data_source("none"),
    code=appsync.Code.from_asset("directory/function_code.js"),
    runtime=appsync.FunctionRuntime.JS_1_0_0
)

appsync.Resolver(self, "PipelineResolver",
    api=api,
    type_name="typeName",
    field_name="fieldName",
    code=appsync.Code.from_inline("""
            // The before step
            export function request(...args) {
              console.log(args);
              return {}
            }

            // The after step
            export function response(ctx) {
              return ctx.prev.result
            }
          """),
    runtime=appsync.FunctionRuntime.JS_1_0_0,
    pipeline_config=[my_js_function]
)
```

Learn more about Pipeline Resolvers and AppSync Functions [here](https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html).
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
    AssetHashType as _AssetHashType_05b67f2d,
    BundlingOptions as _BundlingOptions_588cc936,
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    Duration as _Duration_4839e8c3,
    Expiration as _Expiration_059d47d0,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    IgnoreMode as _IgnoreMode_655a98e8,
    Resource as _Resource_45bc6135,
    ResourceProps as _ResourceProps_15a65b4e,
    SymlinkFollowMode as _SymlinkFollowMode_047ec1f6,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_certificatemanager import ICertificate as _ICertificate_c194c70b
from ..aws_cognito import IUserPool as _IUserPool_1f1029e2
from ..aws_dynamodb import ITable as _ITable_504fd401
from ..aws_elasticsearch import IDomain as _IDomain_0c9006b4
from ..aws_events import IEventBus as _IEventBus_88d13111
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
)
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_logs import (
    ILogGroup as _ILogGroup_3c4fa718, RetentionDays as _RetentionDays_070f99f0
)
from ..aws_opensearchservice import IDomain as _IDomain_3c13cbdd
from ..aws_rds import IServerlessCluster as _IServerlessCluster_adbbb720
from ..aws_s3_assets import AssetOptions as _AssetOptions_2aa69621
from ..aws_secretsmanager import ISecret as _ISecret_6e020e6a


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.ApiKeyConfig",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "expires": "expires", "name": "name"},
)
class ApiKeyConfig:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[_Expiration_059d47d0] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration for API Key authorization in AppSync.

        :param description: Description of API key. Default: - 'Default API Key created by CDK'
        :param expires: The time from creation time after which the API key expires. It must be a minimum of 1 day and a maximum of 365 days from date of creation. Rounded down to the nearest hour. Default: - 7 days rounded down to nearest hour
        :param name: Unique name of the API Key. Default: - 'DefaultAPIKey'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_appsync as appsync
            
            # expiration: cdk.Expiration
            
            api_key_config = appsync.ApiKeyConfig(
                description="description",
                expires=expiration,
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93430f25b9bddda38ab6ed4aef73a01d531a0771aae76b4cfb91f728f6bf481)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expires", value=expires, expected_type=type_hints["expires"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if expires is not None:
            self._values["expires"] = expires
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of API key.

        :default: - 'Default API Key created by CDK'
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires(self) -> typing.Optional[_Expiration_059d47d0]:
        '''The time from creation time after which the API key expires.

        It must be a minimum of 1 day and a maximum of 365 days from date of creation.
        Rounded down to the nearest hour.

        :default: - 7 days rounded down to nearest hour
        '''
        result = self._values.get("expires")
        return typing.cast(typing.Optional[_Expiration_059d47d0], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Unique name of the API Key.

        :default: - 'DefaultAPIKey'
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.AppsyncFunctionAttributes",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class AppsyncFunctionAttributes:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''The attributes for imported AppSync Functions.

        :param function_arn: the ARN of the AppSync function.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            appsync_function_attributes = appsync.AppsyncFunctionAttributes(
                function_arn="functionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c51d586a70a9312cc6dc1bcaca432f8e4313a345a99746b530ac39c8c1a0b1e9)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''the ARN of the AppSync function.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Assign(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_appsync.Assign"):
    '''Utility class representing the assigment of a value to an attribute.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        assign = appsync.Assign("attr", "arg")
    '''

    def __init__(self, attr: builtins.str, arg: builtins.str) -> None:
        '''
        :param attr: -
        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47a3a190d436a13eb112207de457ad9f7fd2e55f6583487ccf52156a53c1d722)
            check_type(argname="argument attr", value=attr, expected_type=type_hints["attr"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        jsii.create(self.__class__, self, [attr, arg])

    @jsii.member(jsii_name="putInMap")
    def put_in_map(self, map: builtins.str) -> builtins.str:
        '''Renders the assignment as a map element.

        :param map: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e61f1f15d49fba8455a2391e89ab0bf2272bdaccb9f4a3f46553b6dc028a6906)
            check_type(argname="argument map", value=map, expected_type=type_hints["map"])
        return typing.cast(builtins.str, jsii.invoke(self, "putInMap", [map]))

    @jsii.member(jsii_name="renderAsAssignment")
    def render_as_assignment(self) -> builtins.str:
        '''Renders the assignment as a VTL string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderAsAssignment", []))


class AttributeValues(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.AttributeValues",
):
    '''Specifies the attribute value assignments.

    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    def __init__(
        self,
        container: builtins.str,
        assignments: typing.Optional[typing.Sequence[Assign]] = None,
    ) -> None:
        '''
        :param container: -
        :param assignments: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cd6bac98a2ebc52d96453f79a721a0c363c5fc6df8ea75a47fa176faa7777ee)
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument assignments", value=assignments, expected_type=type_hints["assignments"])
        jsii.create(self.__class__, self, [container, assignments])

    @jsii.member(jsii_name="attribute")
    def attribute(self, attr: builtins.str) -> "AttributeValuesStep":
        '''Allows assigning a value to the specified attribute.

        :param attr: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__348b35818af6fe397d44e0c92f06b11e8fd640ebd03a9ab3bcfffac868848b75)
            check_type(argname="argument attr", value=attr, expected_type=type_hints["attr"])
        return typing.cast("AttributeValuesStep", jsii.invoke(self, "attribute", [attr]))

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        '''Renders the attribute value assingments to a VTL string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderTemplate", []))

    @jsii.member(jsii_name="renderVariables")
    def render_variables(self) -> builtins.str:
        '''Renders the variables required for ``renderTemplate``.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderVariables", []))


class AttributeValuesStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.AttributeValuesStep",
):
    '''Utility class to allow assigning a value to an attribute.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        # assign: appsync.Assign
        
        attribute_values_step = appsync.AttributeValuesStep("attr", "container", [assign])
    '''

    def __init__(
        self,
        attr: builtins.str,
        container: builtins.str,
        assignments: typing.Sequence[Assign],
    ) -> None:
        '''
        :param attr: -
        :param container: -
        :param assignments: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b74367d2b39a3674c17cec74e25e06759911e6f340e5fdd2523bbbf0757dbe9)
            check_type(argname="argument attr", value=attr, expected_type=type_hints["attr"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument assignments", value=assignments, expected_type=type_hints["assignments"])
        jsii.create(self.__class__, self, [attr, container, assignments])

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> AttributeValues:
        '''Assign the value to the current attribute.

        :param val: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64a719217ebf2092e4a0c549e44dc18cc9048616951d288cac498e6fad568460)
            check_type(argname="argument val", value=val, expected_type=type_hints["val"])
        return typing.cast(AttributeValues, jsii.invoke(self, "is", [val]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.AuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "additional_authorization_modes": "additionalAuthorizationModes",
        "default_authorization": "defaultAuthorization",
    },
)
class AuthorizationConfig:
    def __init__(
        self,
        *,
        additional_authorization_modes: typing.Optional[typing.Sequence[typing.Union["AuthorizationMode", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_authorization: typing.Optional[typing.Union["AuthorizationMode", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Configuration of the API authorization modes.

        :param additional_authorization_modes: Additional authorization modes. Default: - No other modes
        :param default_authorization: Optional authorization configuration. Default: - API Key authorization

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # auth_function: lambda.Function
            
            
            appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.test.graphql")),
                authorization_config=appsync.AuthorizationConfig(
                    default_authorization=appsync.AuthorizationMode(
                        authorization_type=appsync.AuthorizationType.LAMBDA,
                        lambda_authorizer_config=appsync.LambdaAuthorizerConfig(
                            handler=auth_function
                        )
                    )
                )
            )
        '''
        if isinstance(default_authorization, dict):
            default_authorization = AuthorizationMode(**default_authorization)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9412a3d926721362a9a66e6d3efd8ded83f98dac5a7e8438d94370bd2b8ba60)
            check_type(argname="argument additional_authorization_modes", value=additional_authorization_modes, expected_type=type_hints["additional_authorization_modes"])
            check_type(argname="argument default_authorization", value=default_authorization, expected_type=type_hints["default_authorization"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_authorization_modes is not None:
            self._values["additional_authorization_modes"] = additional_authorization_modes
        if default_authorization is not None:
            self._values["default_authorization"] = default_authorization

    @builtins.property
    def additional_authorization_modes(
        self,
    ) -> typing.Optional[typing.List["AuthorizationMode"]]:
        '''Additional authorization modes.

        :default: - No other modes
        '''
        result = self._values.get("additional_authorization_modes")
        return typing.cast(typing.Optional[typing.List["AuthorizationMode"]], result)

    @builtins.property
    def default_authorization(self) -> typing.Optional["AuthorizationMode"]:
        '''Optional authorization configuration.

        :default: - API Key authorization
        '''
        result = self._values.get("default_authorization")
        return typing.cast(typing.Optional["AuthorizationMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.AuthorizationMode",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_type": "authorizationType",
        "api_key_config": "apiKeyConfig",
        "lambda_authorizer_config": "lambdaAuthorizerConfig",
        "open_id_connect_config": "openIdConnectConfig",
        "user_pool_config": "userPoolConfig",
    },
)
class AuthorizationMode:
    def __init__(
        self,
        *,
        authorization_type: "AuthorizationType",
        api_key_config: typing.Optional[typing.Union[ApiKeyConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_authorizer_config: typing.Optional[typing.Union["LambdaAuthorizerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        open_id_connect_config: typing.Optional[typing.Union["OpenIdConnectConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        user_pool_config: typing.Optional[typing.Union["UserPoolConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Interface to specify default or additional authorization(s).

        :param authorization_type: One of possible four values AppSync supports. Default: - ``AuthorizationType.API_KEY``
        :param api_key_config: If authorizationType is ``AuthorizationType.API_KEY``, this option can be configured. Default: - name: 'DefaultAPIKey' | description: 'Default API Key created by CDK'
        :param lambda_authorizer_config: If authorizationType is ``AuthorizationType.LAMBDA``, this option is required. Default: - none
        :param open_id_connect_config: If authorizationType is ``AuthorizationType.OIDC``, this option is required. Default: - none
        :param user_pool_config: If authorizationType is ``AuthorizationType.USER_POOL``, this option is required. Default: - none

        :exampleMetadata: infused

        Example::

            api = appsync.GraphqlApi(self, "Api",
                name="demo",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
                authorization_config=appsync.AuthorizationConfig(
                    default_authorization=appsync.AuthorizationMode(
                        authorization_type=appsync.AuthorizationType.IAM
                    )
                ),
                xray_enabled=True
            )
            
            demo_table = dynamodb.Table(self, "DemoTable",
                partition_key=dynamodb.Attribute(
                    name="id",
                    type=dynamodb.AttributeType.STRING
                )
            )
            
            demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
            
            # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
            # Resolver Mapping Template Reference:
            # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
            demo_dS.create_resolver("QueryGetDemosResolver",
                type_name="Query",
                field_name="getDemos",
                request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
                response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
            )
            
            # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
            demo_dS.create_resolver("MutationAddDemoResolver",
                type_name="Mutation",
                field_name="addDemo",
                request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                    appsync.PrimaryKey.partition("id").auto(),
                    appsync.Values.projecting("input")),
                response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
            )
            
            # To enable DynamoDB read consistency with the `MappingTemplate`:
            demo_dS.create_resolver("QueryGetDemosConsistentResolver",
                type_name="Query",
                field_name="getDemosConsistent",
                request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
                response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
            )
        '''
        if isinstance(api_key_config, dict):
            api_key_config = ApiKeyConfig(**api_key_config)
        if isinstance(lambda_authorizer_config, dict):
            lambda_authorizer_config = LambdaAuthorizerConfig(**lambda_authorizer_config)
        if isinstance(open_id_connect_config, dict):
            open_id_connect_config = OpenIdConnectConfig(**open_id_connect_config)
        if isinstance(user_pool_config, dict):
            user_pool_config = UserPoolConfig(**user_pool_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d567ebb81cf9cc165ffbb174514dfd4819c43b13e22fccb43f780087025e6328)
            check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
            check_type(argname="argument api_key_config", value=api_key_config, expected_type=type_hints["api_key_config"])
            check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
            check_type(argname="argument open_id_connect_config", value=open_id_connect_config, expected_type=type_hints["open_id_connect_config"])
            check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorization_type": authorization_type,
        }
        if api_key_config is not None:
            self._values["api_key_config"] = api_key_config
        if lambda_authorizer_config is not None:
            self._values["lambda_authorizer_config"] = lambda_authorizer_config
        if open_id_connect_config is not None:
            self._values["open_id_connect_config"] = open_id_connect_config
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config

    @builtins.property
    def authorization_type(self) -> "AuthorizationType":
        '''One of possible four values AppSync supports.

        :default: - ``AuthorizationType.API_KEY``

        :see: https://docs.aws.amazon.com/appsync/latest/devguide/security.html
        '''
        result = self._values.get("authorization_type")
        assert result is not None, "Required property 'authorization_type' is missing"
        return typing.cast("AuthorizationType", result)

    @builtins.property
    def api_key_config(self) -> typing.Optional[ApiKeyConfig]:
        '''If authorizationType is ``AuthorizationType.API_KEY``, this option can be configured.

        :default: - name: 'DefaultAPIKey' | description: 'Default API Key created by CDK'
        '''
        result = self._values.get("api_key_config")
        return typing.cast(typing.Optional[ApiKeyConfig], result)

    @builtins.property
    def lambda_authorizer_config(self) -> typing.Optional["LambdaAuthorizerConfig"]:
        '''If authorizationType is ``AuthorizationType.LAMBDA``, this option is required.

        :default: - none
        '''
        result = self._values.get("lambda_authorizer_config")
        return typing.cast(typing.Optional["LambdaAuthorizerConfig"], result)

    @builtins.property
    def open_id_connect_config(self) -> typing.Optional["OpenIdConnectConfig"]:
        '''If authorizationType is ``AuthorizationType.OIDC``, this option is required.

        :default: - none
        '''
        result = self._values.get("open_id_connect_config")
        return typing.cast(typing.Optional["OpenIdConnectConfig"], result)

    @builtins.property
    def user_pool_config(self) -> typing.Optional["UserPoolConfig"]:
        '''If authorizationType is ``AuthorizationType.USER_POOL``, this option is required.

        :default: - none
        '''
        result = self._values.get("user_pool_config")
        return typing.cast(typing.Optional["UserPoolConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationMode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_appsync.AuthorizationType")
class AuthorizationType(enum.Enum):
    '''enum with all possible values for AppSync authorization type.

    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    API_KEY = "API_KEY"
    '''API Key authorization type.'''
    IAM = "IAM"
    '''AWS IAM authorization type.

    Can be used with Cognito Identity Pool federated credentials
    '''
    USER_POOL = "USER_POOL"
    '''Cognito User Pool authorization type.'''
    OIDC = "OIDC"
    '''OpenID Connect authorization type.'''
    LAMBDA = "LAMBDA"
    '''Lambda authorization type.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.AwsIamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "signing_region": "signingRegion",
        "signing_service_name": "signingServiceName",
    },
)
class AwsIamConfig:
    def __init__(
        self,
        *,
        signing_region: builtins.str,
        signing_service_name: builtins.str,
    ) -> None:
        '''The authorization config in case the HTTP endpoint requires authorization.

        :param signing_region: The signing region for AWS IAM authorization.
        :param signing_service_name: The signing service name for AWS IAM authorization.

        :exampleMetadata: infused

        Example::

            api = appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
            )
            
            http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
                name="httpDsWithStepF",
                description="from appsync to StepFunctions Workflow",
                authorization_config=appsync.AwsIamConfig(
                    signing_region="us-east-1",
                    signing_service_name="states"
                )
            )
            
            http_ds.create_resolver("MutationCallStepFunctionResolver",
                type_name="Mutation",
                field_name="callStepFunction",
                request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
                response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9ee7c043bccdcf612d17f9ba452092af17fda0b30d98fab02fc5a652b9a6d7)
            check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
            check_type(argname="argument signing_service_name", value=signing_service_name, expected_type=type_hints["signing_service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "signing_region": signing_region,
            "signing_service_name": signing_service_name,
        }

    @builtins.property
    def signing_region(self) -> builtins.str:
        '''The signing region for AWS IAM authorization.'''
        result = self._values.get("signing_region")
        assert result is not None, "Required property 'signing_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_service_name(self) -> builtins.str:
        '''The signing service name for AWS IAM authorization.'''
        result = self._values.get("signing_service_name")
        assert result is not None, "Required property 'signing_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsIamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.BaseAppsyncFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "code": "code",
        "description": "description",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "runtime": "runtime",
    },
)
class BaseAppsyncFunctionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        code: typing.Optional["Code"] = None,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        runtime: typing.Optional["FunctionRuntime"] = None,
    ) -> None:
        '''the base properties for AppSync Functions.

        :param name: the name of the AppSync Function.
        :param code: The function code. Default: - no code is used
        :param description: the description for this AppSync Function. Default: - no description
        :param request_mapping_template: the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: the response mapping template for the AppSync Function. Default: - no response mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            # code: appsync.Code
            # function_runtime: appsync.FunctionRuntime
            # mapping_template: appsync.MappingTemplate
            
            base_appsync_function_props = appsync.BaseAppsyncFunctionProps(
                name="name",
            
                # the properties below are optional
                code=code,
                description="description",
                request_mapping_template=mapping_template,
                response_mapping_template=mapping_template,
                runtime=function_runtime
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2edba60cc5d74f665d36e54af7d66189cc66d09566e817ef416a2e8fc0de2b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if code is not None:
            self._values["code"] = code
        if description is not None:
            self._values["description"] = description
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if runtime is not None:
            self._values["runtime"] = runtime

    @builtins.property
    def name(self) -> builtins.str:
        '''the name of the AppSync Function.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(self) -> typing.Optional["Code"]:
        '''The function code.

        :default: - no code is used
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional["Code"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description for this AppSync Function.

        :default: - no description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''the request mapping template for the AppSync Function.

        :default: - no request mapping template
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''the response mapping template for the AppSync Function.

        :default: - no response mapping template
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def runtime(self) -> typing.Optional["FunctionRuntime"]:
        '''The functions runtime.

        :default: - no function runtime, VTL mapping templates used
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional["FunctionRuntime"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseAppsyncFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BaseDataSource(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appsync.BaseDataSource",
):
    '''Abstract AppSync datasource implementation.

    Do not use directly but use subclasses for concrete datasources

    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        # appsync_function: appsync.AppsyncFunction
        
        
        pipeline_resolver = appsync.Resolver(self, "pipeline",
            api=api,
            data_source=api.add_none_data_source("none"),
            type_name="typeName",
            field_name="fieldName",
            request_mapping_template=appsync.MappingTemplate.from_file("beforeRequest.vtl"),
            pipeline_config=[appsync_function],
            response_mapping_template=appsync.MappingTemplate.from_file("afterResponse.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        props: typing.Union["BackedDataSourceProps", typing.Dict[builtins.str, typing.Any]],
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DynamoDBConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.ElasticsearchConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.EventBridgeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.HttpConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.LambdaConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.OpenSearchServiceConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        :param type: the type of the AppSync datasource.
        :param dynamo_db_config: configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (deprecated) configuration for Elasticsearch data source. Default: - No config
        :param event_bridge_config: configuration for EventBridge Datasource. Default: - No config
        :param http_config: configuration for HTTP Datasource. Default: - No config
        :param lambda_config: configuration for Lambda Datasource. Default: - No config
        :param open_search_service_config: configuration for OpenSearch data source. Default: - No config
        :param relational_database_config: configuration for RDS Datasource. Default: - No config
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccef8522d3c5565fafba1e5a9b621b9169239e6ce41ea1275f6a59935927b401)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        extended = ExtendedDataSourceProps(
            type=type,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            event_bridge_config=event_bridge_config,
            http_config=http_config,
            lambda_config=lambda_config,
            open_search_service_config=open_search_service_config,
            relational_database_config=relational_database_config,
        )

        jsii.create(self.__class__, self, [scope, id, props, extended])

    @jsii.member(jsii_name="createFunction")
    def create_function(
        self,
        id: builtins.str,
        *,
        name: builtins.str,
        code: typing.Optional["Code"] = None,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        runtime: typing.Optional["FunctionRuntime"] = None,
    ) -> "AppsyncFunction":
        '''creates a new appsync function for this datasource and API using the given properties.

        :param id: -
        :param name: the name of the AppSync Function.
        :param code: The function code. Default: - no code is used
        :param description: the description for this AppSync Function. Default: - no description
        :param request_mapping_template: the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: the response mapping template for the AppSync Function. Default: - no response mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4fc8f5bee0df00790320083fe0cca74ef85fb43651df9418be27e2a1ee3eaf1)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BaseAppsyncFunctionProps(
            name=name,
            code=code,
            description=description,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            runtime=runtime,
        )

        return typing.cast("AppsyncFunction", jsii.invoke(self, "createFunction", [id, props]))

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        id: builtins.str,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union["CachingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional["Code"] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        runtime: typing.Optional["FunctionRuntime"] = None,
    ) -> "Resolver":
        '''creates a new resolver for this datasource and API using the given properties.

        :param id: -
        :param field_name: name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param caching_config: The caching configuration for this resolver. Default: - No caching configuration
        :param code: The function code. Default: - no code is used
        :param max_batch_size: The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18da570994550f3efc007c557f3b52f15c9a82fb4ef611b37d526d983c934ec6)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BaseResolverProps(
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            code=code,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            runtime=runtime,
        )

        return typing.cast("Resolver", jsii.invoke(self, "createResolver", [id, props]))

    @builtins.property
    @jsii.member(jsii_name="ds")
    def ds(self) -> "CfnDataSource":
        '''the underlying CFN data source resource.'''
        return typing.cast("CfnDataSource", jsii.get(self, "ds"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''the name of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="api")
    def _api(self) -> "IGraphqlApi":
        return typing.cast("IGraphqlApi", jsii.get(self, "api"))

    @_api.setter
    def _api(self, value: "IGraphqlApi") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0fdd82cd5eb579a9b83ebfabb3938ef1f107e8210133366c4dfd46d6b05adb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "api", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def _service_role(self) -> typing.Optional[_IRole_235f5d8e]:
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "serviceRole"))

    @_service_role.setter
    def _service_role(self, value: typing.Optional[_IRole_235f5d8e]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f22d536d795f0e6c3516e56fbc4183ece0daab0d19c19d86752c9fd35a21d310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)


class _BaseDataSourceProxy(BaseDataSource):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BaseDataSource).__jsii_proxy_class__ = lambda : _BaseDataSourceProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.BaseDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={"api": "api", "description": "description", "name": "name"},
)
class BaseDataSourceProps:
    def __init__(
        self,
        *,
        api: "IGraphqlApi",
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Base properties for an AppSync datasource.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            # graphql_api: appsync.GraphqlApi
            
            base_data_source_props = appsync.BaseDataSourceProps(
                api=graphql_api,
            
                # the properties below are optional
                description="description",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cb5694e7bccdac081c0d35fee8d239110cc5fb8b7eefac7866144f6deac2d9d)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def api(self) -> "IGraphqlApi":
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast("IGraphqlApi", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.BaseResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "code": "code",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "runtime": "runtime",
    },
)
class BaseResolverProps:
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union["CachingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional["Code"] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        runtime: typing.Optional["FunctionRuntime"] = None,
    ) -> None:
        '''Basic properties for an AppSync resolver.

        :param field_name: name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param caching_config: The caching configuration for this resolver. Default: - No caching configuration
        :param code: The function code. Default: - no code is used
        :param max_batch_size: The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used

        :exampleMetadata: infused

        Example::

            # Build a data source for AppSync to access the database.
            # api: appsync.GraphqlApi
            # Create username and password secret for DB Cluster
            secret = rds.DatabaseSecret(self, "AuroraSecret",
                username="clusteradmin"
            )
            
            # The VPC to place the cluster in
            vpc = ec2.Vpc(self, "AuroraVpc")
            
            # Create the serverless cluster, provide all values needed to customise the database.
            cluster = rds.ServerlessCluster(self, "AuroraCluster",
                engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
                vpc=vpc,
                credentials={"username": "clusteradmin"},
                cluster_identifier="db-endpoint-test",
                default_database_name="demos"
            )
            rds_dS = api.add_rds_data_source("rds", cluster, secret, "demos")
            
            # Set up a resolver for an RDS query.
            rds_dS.create_resolver("QueryGetDemosRdsResolver",
                type_name="Query",
                field_name="getDemosRds",
                request_mapping_template=appsync.MappingTemplate.from_string("""
                      {
                        "version": "2018-05-29",
                        "statements": [
                          "SELECT * FROM demos"
                        ]
                      }
                      """),
                response_mapping_template=appsync.MappingTemplate.from_string("""
                        $utils.toJson($utils.rds.toJsonObject($ctx.result)[0])
                      """)
            )
            
            # Set up a resolver for an RDS mutation.
            rds_dS.create_resolver("MutationAddDemoRdsResolver",
                type_name="Mutation",
                field_name="addDemoRds",
                request_mapping_template=appsync.MappingTemplate.from_string("""
                      {
                        "version": "2018-05-29",
                        "statements": [
                          "INSERT INTO demos VALUES (:id, :version)",
                          "SELECT * WHERE id = :id"
                        ],
                        "variableMap": {
                          ":id": $util.toJson($util.autoId()),
                          ":version": $util.toJson($ctx.args.version)
                        }
                      }
                      """),
                response_mapping_template=appsync.MappingTemplate.from_string("""
                        $utils.toJson($utils.rds.toJsonObject($ctx.result)[1][0])
                      """)
            )
        '''
        if isinstance(caching_config, dict):
            caching_config = CachingConfig(**caching_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57bca2ee49335be042ebfd66ab492a766a7dcba63ae9692b50ecab067c20e80f)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if code is not None:
            self._values["code"] = code
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if runtime is not None:
            self._values["runtime"] = runtime

    @builtins.property
    def field_name(self) -> builtins.str:
        '''name of the GraphQL field in the given type this resolver is attached to.'''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''name of the GraphQL type this resolver is attached to.'''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(self) -> typing.Optional["CachingConfig"]:
        '''The caching configuration for this resolver.

        :default: - No caching configuration
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional["CachingConfig"], result)

    @builtins.property
    def code(self) -> typing.Optional["Code"]:
        '''The function code.

        :default: - no code is used
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional["Code"], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of elements per batch, when using batch invoke.

        :default: - No max batch size
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List["IAppsyncFunction"]]:
        '''configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional[typing.List["IAppsyncFunction"]], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''The request mapping template for this resolver.

        :default: - No mapping template
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''The response mapping template for this resolver.

        :default: - No mapping template
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def runtime(self) -> typing.Optional["FunctionRuntime"]:
        '''The functions runtime.

        :default: - no function runtime, VTL mapping templates used
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional["FunctionRuntime"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CachingConfig",
    jsii_struct_bases=[],
    name_mapping={"ttl": "ttl", "caching_keys": "cachingKeys"},
)
class CachingConfig:
    def __init__(
        self,
        *,
        ttl: _Duration_4839e8c3,
        caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''CachingConfig for AppSync resolvers.

        :param ttl: The TTL in seconds for a resolver that has caching enabled. Valid values are between 1 and 3600 seconds.
        :param caching_keys: The caching keys for a resolver that has caching enabled. Valid values are entries from the $context.arguments, $context.source, and $context.identity maps. Default: - No caching keys

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_appsync as appsync
            
            caching_config = appsync.CachingConfig(
                ttl=cdk.Duration.minutes(30),
            
                # the properties below are optional
                caching_keys=["cachingKeys"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16c48e7a47c60140291c83d5eea69a6e25ec7462e7a0080eaf553e500e9ac06e)
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument caching_keys", value=caching_keys, expected_type=type_hints["caching_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ttl": ttl,
        }
        if caching_keys is not None:
            self._values["caching_keys"] = caching_keys

    @builtins.property
    def ttl(self) -> _Duration_4839e8c3:
        '''The TTL in seconds for a resolver that has caching enabled.

        Valid values are between 1 and 3600 seconds.
        '''
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def caching_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The caching keys for a resolver that has caching enabled.

        Valid values are entries from the $context.arguments, $context.source, and $context.identity maps.

        :default: - No caching keys
        '''
        result = self._values.get("caching_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CachingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnApiCache(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnApiCache",
):
    '''The ``AWS::AppSync::ApiCache`` resource represents the input of a ``CreateApiCache`` operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_api_cache = appsync.CfnApiCache(self, "MyCfnApiCache",
            api_caching_behavior="apiCachingBehavior",
            api_id="apiId",
            ttl=123,
            type="type",
        
            # the properties below are optional
            at_rest_encryption_enabled=False,
            transit_encryption_enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_caching_behavior: builtins.str,
        api_id: builtins.str,
        ttl: jsii.Number,
        type: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_caching_behavior: Caching behavior. - *FULL_REQUEST_CACHING* : All requests are fully cached. - *PER_RESOLVER_CACHING* : Individual resolvers that you specify are cached.
        :param api_id: The GraphQL API ID.
        :param ttl: TTL in seconds for cache entries. Valid values are 1–3,600 seconds.
        :param type: The cache instance type. Valid values are. - ``SMALL`` - ``MEDIUM`` - ``LARGE`` - ``XLARGE`` - ``LARGE_2X`` - ``LARGE_4X`` - ``LARGE_8X`` (not available in all regions) - ``LARGE_12X`` Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used. The following legacy instance types are available, but their use is discouraged: - *T2_SMALL* : A t2.small instance type. - *T2_MEDIUM* : A t2.medium instance type. - *R4_LARGE* : A r4.large instance type. - *R4_XLARGE* : A r4.xlarge instance type. - *R4_2XLARGE* : A r4.2xlarge instance type. - *R4_4XLARGE* : A r4.4xlarge instance type. - *R4_8XLARGE* : A r4.8xlarge instance type.
        :param at_rest_encryption_enabled: At-rest encryption flag for cache. You cannot update this setting after creation.
        :param transit_encryption_enabled: Transit encryption flag when connecting to cache. You cannot update this setting after creation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9d92b7b2abdac7341eb92f7ac10d2d67dd2700af68eaf42c72c47ffdaacc344)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiCacheProps(
            api_caching_behavior=api_caching_behavior,
            api_id=api_id,
            ttl=ttl,
            type=type,
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            transit_encryption_enabled=transit_encryption_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142193172b7ee1304f3b8fd949531b4cfa950ea62d0dc10f9ed5a184a603132d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ce863b5f21a86ce886458054cd4de0550269c18eb7c4f3fb37884dc2869845e)
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
    @jsii.member(jsii_name="apiCachingBehavior")
    def api_caching_behavior(self) -> builtins.str:
        '''Caching behavior.'''
        return typing.cast(builtins.str, jsii.get(self, "apiCachingBehavior"))

    @api_caching_behavior.setter
    def api_caching_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aee6b3576fbf654864dae4f55fe292d210bf01534f16f80af0ac225f8fa338c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiCachingBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The GraphQL API ID.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c2fdac623dbaddb2a0226d75e6f3ca84c058f3f46b9c9a1289820c1cf0827e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        '''TTL in seconds for cache entries.'''
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1893b7ba08236941b8e5bb4704e7fe53f8819086085796443b5d68f513e66eaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The cache instance type.

        Valid values are.
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45dc491e21920c6cd0ddecd9aada80283ac759d9eaca52c45a6ce35197166e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''At-rest encryption flag for cache.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "atRestEncryptionEnabled"))

    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93a4abe242f634763c1f128b7e17017d1176924c9b032d5536f4caa3b3fc3bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "atRestEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Transit encryption flag when connecting to cache.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "transitEncryptionEnabled"))

    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb39499095e917401c885f7c77781744d09df071b1ed62c6f2c32cbbc6fbdb33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionEnabled", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnApiCacheProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_caching_behavior": "apiCachingBehavior",
        "api_id": "apiId",
        "ttl": "ttl",
        "type": "type",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "transit_encryption_enabled": "transitEncryptionEnabled",
    },
)
class CfnApiCacheProps:
    def __init__(
        self,
        *,
        api_caching_behavior: builtins.str,
        api_id: builtins.str,
        ttl: jsii.Number,
        type: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApiCache``.

        :param api_caching_behavior: Caching behavior. - *FULL_REQUEST_CACHING* : All requests are fully cached. - *PER_RESOLVER_CACHING* : Individual resolvers that you specify are cached.
        :param api_id: The GraphQL API ID.
        :param ttl: TTL in seconds for cache entries. Valid values are 1–3,600 seconds.
        :param type: The cache instance type. Valid values are. - ``SMALL`` - ``MEDIUM`` - ``LARGE`` - ``XLARGE`` - ``LARGE_2X`` - ``LARGE_4X`` - ``LARGE_8X`` (not available in all regions) - ``LARGE_12X`` Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used. The following legacy instance types are available, but their use is discouraged: - *T2_SMALL* : A t2.small instance type. - *T2_MEDIUM* : A t2.medium instance type. - *R4_LARGE* : A r4.large instance type. - *R4_XLARGE* : A r4.xlarge instance type. - *R4_2XLARGE* : A r4.2xlarge instance type. - *R4_4XLARGE* : A r4.4xlarge instance type. - *R4_8XLARGE* : A r4.8xlarge instance type.
        :param at_rest_encryption_enabled: At-rest encryption flag for cache. You cannot update this setting after creation.
        :param transit_encryption_enabled: Transit encryption flag when connecting to cache. You cannot update this setting after creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_api_cache_props = appsync.CfnApiCacheProps(
                api_caching_behavior="apiCachingBehavior",
                api_id="apiId",
                ttl=123,
                type="type",
            
                # the properties below are optional
                at_rest_encryption_enabled=False,
                transit_encryption_enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f054fa3186eb5f122c20e523bed485713c72511ee3ee94be25733ecad9a348c)
            check_type(argname="argument api_caching_behavior", value=api_caching_behavior, expected_type=type_hints["api_caching_behavior"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument at_rest_encryption_enabled", value=at_rest_encryption_enabled, expected_type=type_hints["at_rest_encryption_enabled"])
            check_type(argname="argument transit_encryption_enabled", value=transit_encryption_enabled, expected_type=type_hints["transit_encryption_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_caching_behavior": api_caching_behavior,
            "api_id": api_id,
            "ttl": ttl,
            "type": type,
        }
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled

    @builtins.property
    def api_caching_behavior(self) -> builtins.str:
        '''Caching behavior.

        - *FULL_REQUEST_CACHING* : All requests are fully cached.
        - *PER_RESOLVER_CACHING* : Individual resolvers that you specify are cached.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apicachingbehavior
        '''
        result = self._values.get("api_caching_behavior")
        assert result is not None, "Required property 'api_caching_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The GraphQL API ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ttl(self) -> jsii.Number:
        '''TTL in seconds for cache entries.

        Valid values are 1–3,600 seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-ttl
        '''
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The cache instance type. Valid values are.

        - ``SMALL``
        - ``MEDIUM``
        - ``LARGE``
        - ``XLARGE``
        - ``LARGE_2X``
        - ``LARGE_4X``
        - ``LARGE_8X`` (not available in all regions)
        - ``LARGE_12X``

        Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.

        The following legacy instance types are available, but their use is discouraged:

        - *T2_SMALL* : A t2.small instance type.
        - *T2_MEDIUM* : A t2.medium instance type.
        - *R4_LARGE* : A r4.large instance type.
        - *R4_XLARGE* : A r4.xlarge instance type.
        - *R4_2XLARGE* : A r4.2xlarge instance type.
        - *R4_4XLARGE* : A r4.4xlarge instance type.
        - *R4_8XLARGE* : A r4.8xlarge instance type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''At-rest encryption flag for cache.

        You cannot update this setting after creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-atrestencryptionenabled
        '''
        result = self._values.get("at_rest_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Transit encryption flag when connecting to cache.

        You cannot update this setting after creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-transitencryptionenabled
        '''
        result = self._values.get("transit_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiCacheProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnApiKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnApiKey",
):
    '''The ``AWS::AppSync::ApiKey`` resource creates a unique key that you can distribute to clients who are executing GraphQL operations with AWS AppSync that require an API key.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_api_key = appsync.CfnApiKey(self, "MyCfnApiKey",
            api_id="apiId",
        
            # the properties below are optional
            api_key_id="apiKeyId",
            description="description",
            expires=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        api_key_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: Unique AWS AppSync GraphQL API ID for this API key.
        :param api_key_id: The API key ID.
        :param description: Unique description of your API key.
        :param expires: The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6065dd18c9d420fd4fcd70aced8416006f044f82aecff54150165e832539a8e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiKeyProps(
            api_id=api_id,
            api_key_id=api_key_id,
            description=description,
            expires=expires,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8f02bc91fc0b32c990b8d08a5d7a0ef78a88363920fa69d4196dcc7f2ecfb3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a844b496712966f29aae49f2f831e6a85c7acf03c2ce61c94162ccf13c5efd6d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiKey")
    def attr_api_key(self) -> builtins.str:
        '''The API key.

        :cloudformationAttribute: ApiKey
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiKey"))

    @builtins.property
    @jsii.member(jsii_name="attrApiKeyId")
    def attr_api_key_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApiKeyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiKeyId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the API key, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/apikey/apikeya1bzhi`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API ID for this API key.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c1cce5f76a6037620e1cc2e57750c81cc5161ff526ce78123f0cd9f25c8e856)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="apiKeyId")
    def api_key_id(self) -> typing.Optional[builtins.str]:
        '''The API key ID.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyId"))

    @api_key_id.setter
    def api_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f5d6818eefb673237292bb9320e2134ad0c799f70d17a7cba2de3f4298ccf5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Unique description of your API key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08afa042939638da41f04c7165f811f5081bd3c8943f787591f098aa4a3b8699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expires")
    def expires(self) -> typing.Optional[jsii.Number]:
        '''The time after which the API key expires.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expires"))

    @expires.setter
    def expires(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b034facb88dea82241969fd1a22a5bbaccf03068403021106e073c92112ab45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expires", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnApiKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "api_key_id": "apiKeyId",
        "description": "description",
        "expires": "expires",
    },
)
class CfnApiKeyProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        api_key_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnApiKey``.

        :param api_id: Unique AWS AppSync GraphQL API ID for this API key.
        :param api_key_id: The API key ID.
        :param description: Unique description of your API key.
        :param expires: The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_api_key_props = appsync.CfnApiKeyProps(
                api_id="apiId",
            
                # the properties below are optional
                api_key_id="apiKeyId",
                description="description",
                expires=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1688db2b7835c85b4e2cd69655b5d25321ff2aa2ea9e1b2a0612caff34184549)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument api_key_id", value=api_key_id, expected_type=type_hints["api_key_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expires", value=expires, expected_type=type_hints["expires"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
        }
        if api_key_id is not None:
            self._values["api_key_id"] = api_key_id
        if description is not None:
            self._values["description"] = description
        if expires is not None:
            self._values["expires"] = expires

    @builtins.property
    def api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API ID for this API key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_key_id(self) -> typing.Optional[builtins.str]:
        '''The API key ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apikeyid
        '''
        result = self._values.get("api_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Unique description of your API key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires(self) -> typing.Optional[jsii.Number]:
        '''The time after which the API key expires.

        The date is represented as seconds since the epoch, rounded down to the nearest hour.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires
        '''
        result = self._values.get("expires")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDataSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource",
):
    '''The ``AWS::AppSync::DataSource`` resource creates data sources for resolvers in AWS AppSync to connect to, such as Amazon DynamoDB , AWS Lambda , and Amazon OpenSearch Service .

    Resolvers use these data sources to fetch data when clients make GraphQL calls.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_data_source = appsync.CfnDataSource(self, "MyCfnDataSource",
            api_id="apiId",
            name="name",
            type="type",
        
            # the properties below are optional
            description="description",
            dynamo_db_config=appsync.CfnDataSource.DynamoDBConfigProperty(
                aws_region="awsRegion",
                table_name="tableName",
        
                # the properties below are optional
                delta_sync_config=appsync.CfnDataSource.DeltaSyncConfigProperty(
                    base_table_ttl="baseTableTtl",
                    delta_sync_table_name="deltaSyncTableName",
                    delta_sync_table_ttl="deltaSyncTableTtl"
                ),
                use_caller_credentials=False,
                versioned=False
            ),
            elasticsearch_config=appsync.CfnDataSource.ElasticsearchConfigProperty(
                aws_region="awsRegion",
                endpoint="endpoint"
            ),
            event_bridge_config=appsync.CfnDataSource.EventBridgeConfigProperty(
                event_bus_arn="eventBusArn"
            ),
            http_config=appsync.CfnDataSource.HttpConfigProperty(
                endpoint="endpoint",
        
                # the properties below are optional
                authorization_config=appsync.CfnDataSource.AuthorizationConfigProperty(
                    authorization_type="authorizationType",
        
                    # the properties below are optional
                    aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                        signing_region="signingRegion",
                        signing_service_name="signingServiceName"
                    )
                )
            ),
            lambda_config=appsync.CfnDataSource.LambdaConfigProperty(
                lambda_function_arn="lambdaFunctionArn"
            ),
            open_search_service_config=appsync.CfnDataSource.OpenSearchServiceConfigProperty(
                aws_region="awsRegion",
                endpoint="endpoint"
            ),
            relational_database_config=appsync.CfnDataSource.RelationalDatabaseConfigProperty(
                relational_database_source_type="relationalDatabaseSourceType",
        
                # the properties below are optional
                rds_http_endpoint_config=appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                    aws_region="awsRegion",
                    aws_secret_store_arn="awsSecretStoreArn",
                    db_cluster_identifier="dbClusterIdentifier",
        
                    # the properties below are optional
                    database_name="databaseName",
                    schema="schema"
                )
            ),
            service_role_arn="serviceRoleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DynamoDBConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.ElasticsearchConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.EventBridgeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.HttpConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.LambdaConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.OpenSearchServiceConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: Unique AWS AppSync GraphQL API identifier where this data source will be created.
        :param name: Friendly name for you to identify your AppSync data source after creation.
        :param type: The type of the data source. - *AWS_LAMBDA* : The data source is an AWS Lambda function. - *AMAZON_DYNAMODB* : The data source is an Amazon DynamoDB table. - *AMAZON_ELASTICSEARCH* : The data source is an Amazon OpenSearch Service domain. - *AMAZON_EVENTBRIDGE* : The data source is an Amazon EventBridge event bus. - *AMAZON_OPENSEARCH_SERVICE* : The data source is an Amazon OpenSearch Service domain. - *NONE* : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation. - *HTTP* : The data source is an HTTP endpoint. - *RELATIONAL_DATABASE* : The data source is a relational database.
        :param description: The description of the data source.
        :param dynamo_db_config: AWS Region and TableName for an Amazon DynamoDB table in your account.
        :param elasticsearch_config: AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account. As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.
        :param event_bridge_config: An EventBridge configuration that contains a valid ARN of an event bus.
        :param http_config: Endpoints for an HTTP data source.
        :param lambda_config: An ARN of a Lambda function in valid ARN format. This can be the ARN of a Lambda function that exists in the current account or in another account.
        :param open_search_service_config: AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.
        :param relational_database_config: Relational Database configuration of the relational database data source.
        :param service_role_arn: The AWS Identity and Access Management service role ARN for the data source. The system assumes this role when accessing the data source. Required if ``Type`` is specified as ``AWS_LAMBDA`` , ``AMAZON_DYNAMODB`` , ``AMAZON_ELASTICSEARCH`` , ``AMAZON_EVENTBRIDGE`` , or ``AMAZON_OPENSEARCH_SERVICE`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2dc8968068d09d9cb599cea5efad1a18016c4eca4fcc6c15e6169a0891e2678)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataSourceProps(
            api_id=api_id,
            name=name,
            type=type,
            description=description,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            event_bridge_config=event_bridge_config,
            http_config=http_config,
            lambda_config=lambda_config,
            open_search_service_config=open_search_service_config,
            relational_database_config=relational_database_config,
            service_role_arn=service_role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844d45e22564aca7d878e00ff3e6a39f30d70312a9d2fcf8bb2f587b070069f7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb33982b2405feec8337a5b841ef30f58e28ed8058a2e3d003d09ee8aac516a9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDataSourceArn")
    def attr_data_source_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the API key, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/datasources/datasourcename`` .

        :cloudformationAttribute: DataSourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataSourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Friendly name for you to identify your AWS AppSync data source after creation.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API identifier where this data source will be created.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7863787830eb114a9c03188cb3a3bfd0b865645dac5dd0d3cf0b374c0a1af6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Friendly name for you to identify your AppSync data source after creation.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba82e0d60919163b242fed29c81421c4160f75a79249e58ce74b20f6b7d0f03d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aae6a5f086f2d2c36e8dff3cce5906d962da71d7148d7feec996abb025fb8f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29cebb36b12bc9cd3423d5991aeea26c635c2541d63fc9c3309a2177c24f1118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dynamoDbConfig")
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DynamoDBConfigProperty"]]:
        '''AWS Region and TableName for an Amazon DynamoDB table in your account.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DynamoDBConfigProperty"]], jsii.get(self, "dynamoDbConfig"))

    @dynamo_db_config.setter
    def dynamo_db_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DynamoDBConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffaca3e4a18d434a01277621d6792259ab70047809af34a6cb0bab3eb7886a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamoDbConfig", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ElasticsearchConfigProperty"]]:
        '''AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ElasticsearchConfigProperty"]], jsii.get(self, "elasticsearchConfig"))

    @elasticsearch_config.setter
    def elasticsearch_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ElasticsearchConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5323c0bb4d330a2f6b24616dd2b47847aa913d75611ddeae3cc451eda7ebb774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchConfig", value)

    @builtins.property
    @jsii.member(jsii_name="eventBridgeConfig")
    def event_bridge_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.EventBridgeConfigProperty"]]:
        '''An EventBridge configuration that contains a valid ARN of an event bus.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.EventBridgeConfigProperty"]], jsii.get(self, "eventBridgeConfig"))

    @event_bridge_config.setter
    def event_bridge_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.EventBridgeConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9aedfd6520add851a257d524d2bcb0a45552a7b99af805456bde2779e658d15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBridgeConfig", value)

    @builtins.property
    @jsii.member(jsii_name="httpConfig")
    def http_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.HttpConfigProperty"]]:
        '''Endpoints for an HTTP data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.HttpConfigProperty"]], jsii.get(self, "httpConfig"))

    @http_config.setter
    def http_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.HttpConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2b1129f048e5b946eceb4eb9c372f68c9a28e32ebe6091b611c3b1b82e3e83d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpConfig", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.LambdaConfigProperty"]]:
        '''An ARN of a Lambda function in valid ARN format.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.LambdaConfigProperty"]], jsii.get(self, "lambdaConfig"))

    @lambda_config.setter
    def lambda_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.LambdaConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ff8b510d0035620c1325857ec673c802695c9f3c8dd8fa109d1b44e652a641)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaConfig", value)

    @builtins.property
    @jsii.member(jsii_name="openSearchServiceConfig")
    def open_search_service_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.OpenSearchServiceConfigProperty"]]:
        '''AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.OpenSearchServiceConfigProperty"]], jsii.get(self, "openSearchServiceConfig"))

    @open_search_service_config.setter
    def open_search_service_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.OpenSearchServiceConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__876dd6f7515f1b03442f4aa7a0d78d1d6e5eef401db8d851e96b713bd30f989e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openSearchServiceConfig", value)

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalDatabaseConfigProperty"]]:
        '''Relational Database configuration of the relational database data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalDatabaseConfigProperty"]], jsii.get(self, "relationalDatabaseConfig"))

    @relational_database_config.setter
    def relational_database_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalDatabaseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72a1c504ec56f95938bf0b2a05d96acc7eb4b1190dc7285e9c33b6b194318386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relationalDatabaseConfig", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''The AWS Identity and Access Management service role ARN for the data source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8d23554bf1b07da4d8bb262596b409805d205b461615d34726f3323315abb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.AuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_type": "authorizationType",
            "aws_iam_config": "awsIamConfig",
        },
    )
    class AuthorizationConfigProperty:
        def __init__(
            self,
            *,
            authorization_type: builtins.str,
            aws_iam_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.AwsIamConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``AuthorizationConfig`` property type specifies the authorization type and configuration for an AWS AppSync http data source.

            ``AuthorizationConfig`` is a property of the `AWS AppSync DataSource HttpConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html>`_ property type.

            :param authorization_type: The authorization type that the HTTP endpoint requires. - *AWS_IAM* : The authorization type is Signature Version 4 (SigV4).
            :param aws_iam_config: The AWS Identity and Access Management settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                authorization_config_property = appsync.CfnDataSource.AuthorizationConfigProperty(
                    authorization_type="authorizationType",
                
                    # the properties below are optional
                    aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                        signing_region="signingRegion",
                        signing_service_name="signingServiceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b40b2b6b828a39a91cb37d699b9dccbe36d457b235d0c89f8d63a8c926a5443)
                check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
                check_type(argname="argument aws_iam_config", value=aws_iam_config, expected_type=type_hints["aws_iam_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorization_type": authorization_type,
            }
            if aws_iam_config is not None:
                self._values["aws_iam_config"] = aws_iam_config

        @builtins.property
        def authorization_type(self) -> builtins.str:
            '''The authorization type that the HTTP endpoint requires.

            - *AWS_IAM* : The authorization type is Signature Version 4 (SigV4).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-authorizationtype
            '''
            result = self._values.get("authorization_type")
            assert result is not None, "Required property 'authorization_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_iam_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.AwsIamConfigProperty"]]:
            '''The AWS Identity and Access Management settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-awsiamconfig
            '''
            result = self._values.get("aws_iam_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.AwsIamConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.AwsIamConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "signing_region": "signingRegion",
            "signing_service_name": "signingServiceName",
        },
    )
    class AwsIamConfigProperty:
        def __init__(
            self,
            *,
            signing_region: typing.Optional[builtins.str] = None,
            signing_service_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the ``AwsIamConfig`` property type to specify ``AwsIamConfig`` for a AWS AppSync authorizaton.

            ``AwsIamConfig`` is a property of the `AWS AppSync DataSource AuthorizationConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig-authorizationconfig.html>`_ resource.

            :param signing_region: The signing Region for AWS Identity and Access Management authorization.
            :param signing_service_name: The signing service name for AWS Identity and Access Management authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                aws_iam_config_property = appsync.CfnDataSource.AwsIamConfigProperty(
                    signing_region="signingRegion",
                    signing_service_name="signingServiceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63d3d6847bbd8b570bb51728b12402301a578fc159522a9bb797a8042b7c43dd)
                check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
                check_type(argname="argument signing_service_name", value=signing_service_name, expected_type=type_hints["signing_service_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if signing_region is not None:
                self._values["signing_region"] = signing_region
            if signing_service_name is not None:
                self._values["signing_service_name"] = signing_service_name

        @builtins.property
        def signing_region(self) -> typing.Optional[builtins.str]:
            '''The signing Region for AWS Identity and Access Management authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingregion
            '''
            result = self._values.get("signing_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def signing_service_name(self) -> typing.Optional[builtins.str]:
            '''The signing service name for AWS Identity and Access Management authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingservicename
            '''
            result = self._values.get("signing_service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsIamConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.DeltaSyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_table_ttl": "baseTableTtl",
            "delta_sync_table_name": "deltaSyncTableName",
            "delta_sync_table_ttl": "deltaSyncTableTtl",
        },
    )
    class DeltaSyncConfigProperty:
        def __init__(
            self,
            *,
            base_table_ttl: builtins.str,
            delta_sync_table_name: builtins.str,
            delta_sync_table_ttl: builtins.str,
        ) -> None:
            '''Describes a Delta Sync configuration.

            :param base_table_ttl: The number of minutes that an Item is stored in the data source.
            :param delta_sync_table_name: The Delta Sync table name.
            :param delta_sync_table_ttl: The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                delta_sync_config_property = appsync.CfnDataSource.DeltaSyncConfigProperty(
                    base_table_ttl="baseTableTtl",
                    delta_sync_table_name="deltaSyncTableName",
                    delta_sync_table_ttl="deltaSyncTableTtl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d8409bee2e379adfba84b9eedc28876ceca73a2b15ec9ad3045f33dc08a849c)
                check_type(argname="argument base_table_ttl", value=base_table_ttl, expected_type=type_hints["base_table_ttl"])
                check_type(argname="argument delta_sync_table_name", value=delta_sync_table_name, expected_type=type_hints["delta_sync_table_name"])
                check_type(argname="argument delta_sync_table_ttl", value=delta_sync_table_ttl, expected_type=type_hints["delta_sync_table_ttl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "base_table_ttl": base_table_ttl,
                "delta_sync_table_name": delta_sync_table_name,
                "delta_sync_table_ttl": delta_sync_table_ttl,
            }

        @builtins.property
        def base_table_ttl(self) -> builtins.str:
            '''The number of minutes that an Item is stored in the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-basetablettl
            '''
            result = self._values.get("base_table_ttl")
            assert result is not None, "Required property 'base_table_ttl' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def delta_sync_table_name(self) -> builtins.str:
            '''The Delta Sync table name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablename
            '''
            result = self._values.get("delta_sync_table_name")
            assert result is not None, "Required property 'delta_sync_table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def delta_sync_table_ttl(self) -> builtins.str:
            '''The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablettl
            '''
            result = self._values.get("delta_sync_table_ttl")
            assert result is not None, "Required property 'delta_sync_table_ttl' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaSyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.DynamoDBConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "table_name": "tableName",
            "delta_sync_config": "deltaSyncConfig",
            "use_caller_credentials": "useCallerCredentials",
            "versioned": "versioned",
        },
    )
    class DynamoDBConfigProperty:
        def __init__(
            self,
            *,
            aws_region: builtins.str,
            table_name: builtins.str,
            delta_sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DeltaSyncConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            use_caller_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            versioned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``DynamoDBConfig`` property type specifies the ``AwsRegion`` and ``TableName`` for an Amazon DynamoDB table in your account for an AWS AppSync data source.

            ``DynamoDBConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            :param aws_region: The AWS Region.
            :param table_name: The table name.
            :param delta_sync_config: The ``DeltaSyncConfig`` for a versioned datasource.
            :param use_caller_credentials: Set to ``TRUE`` to use AWS Identity and Access Management with this data source.
            :param versioned: Set to TRUE to use Conflict Detection and Resolution with this data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                dynamo_dBConfig_property = appsync.CfnDataSource.DynamoDBConfigProperty(
                    aws_region="awsRegion",
                    table_name="tableName",
                
                    # the properties below are optional
                    delta_sync_config=appsync.CfnDataSource.DeltaSyncConfigProperty(
                        base_table_ttl="baseTableTtl",
                        delta_sync_table_name="deltaSyncTableName",
                        delta_sync_table_ttl="deltaSyncTableTtl"
                    ),
                    use_caller_credentials=False,
                    versioned=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__66016c117898c1cc0dc84bb648ce56335f475ea29f1590882ca3229c1e8ffe3f)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument delta_sync_config", value=delta_sync_config, expected_type=type_hints["delta_sync_config"])
                check_type(argname="argument use_caller_credentials", value=use_caller_credentials, expected_type=type_hints["use_caller_credentials"])
                check_type(argname="argument versioned", value=versioned, expected_type=type_hints["versioned"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "table_name": table_name,
            }
            if delta_sync_config is not None:
                self._values["delta_sync_config"] = delta_sync_config
            if use_caller_credentials is not None:
                self._values["use_caller_credentials"] = use_caller_credentials
            if versioned is not None:
                self._values["versioned"] = versioned

        @builtins.property
        def aws_region(self) -> builtins.str:
            '''The AWS Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The table name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def delta_sync_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DeltaSyncConfigProperty"]]:
            '''The ``DeltaSyncConfig`` for a versioned datasource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-deltasyncconfig
            '''
            result = self._values.get("delta_sync_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DeltaSyncConfigProperty"]], result)

        @builtins.property
        def use_caller_credentials(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set to ``TRUE`` to use AWS Identity and Access Management with this data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-usecallercredentials
            '''
            result = self._values.get("use_caller_credentials")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def versioned(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set to TRUE to use Conflict Detection and Resolution with this data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-versioned
            '''
            result = self._values.get("versioned")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.ElasticsearchConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_region": "awsRegion", "endpoint": "endpoint"},
    )
    class ElasticsearchConfigProperty:
        def __init__(self, *, aws_region: builtins.str, endpoint: builtins.str) -> None:
            '''The ``ElasticsearchConfig`` property type specifies the ``AwsRegion`` and ``Endpoints`` for an Amazon OpenSearch Service domain in your account for an AWS AppSync data source.

            ElasticsearchConfig is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.

            :param aws_region: The AWS Region.
            :param endpoint: The endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                elasticsearch_config_property = appsync.CfnDataSource.ElasticsearchConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7385ec04703540fe726bf7efc36f7ea05ba851b02e63ee657ec6cba21c5e805)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "endpoint": endpoint,
            }

        @builtins.property
        def aws_region(self) -> builtins.str:
            '''The AWS Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.EventBridgeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"event_bus_arn": "eventBusArn"},
    )
    class EventBridgeConfigProperty:
        def __init__(self, *, event_bus_arn: builtins.str) -> None:
            '''The data source.

            This can be an API destination, resource, or AWS service.

            :param event_bus_arn: The event bus pipeline's ARN. For more information about event buses, see `EventBridge event buses <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-eventbridgeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                event_bridge_config_property = appsync.CfnDataSource.EventBridgeConfigProperty(
                    event_bus_arn="eventBusArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__659279c711a228092290e57ba8e5c0b54e147a7101bfeed551b80c8e7bcdb985)
                check_type(argname="argument event_bus_arn", value=event_bus_arn, expected_type=type_hints["event_bus_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_bus_arn": event_bus_arn,
            }

        @builtins.property
        def event_bus_arn(self) -> builtins.str:
            '''The event bus pipeline's ARN.

            For more information about event buses, see `EventBridge event buses <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-eventbridgeconfig.html#cfn-appsync-datasource-eventbridgeconfig-eventbusarn
            '''
            result = self._values.get("event_bus_arn")
            assert result is not None, "Required property 'event_bus_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventBridgeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.HttpConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "authorization_config": "authorizationConfig",
        },
    )
    class HttpConfigProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            authorization_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.AuthorizationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Use the ``HttpConfig`` property type to specify ``HttpConfig`` for an AWS AppSync data source.

            ``HttpConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ resource.

            :param endpoint: The endpoint.
            :param authorization_config: The authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                http_config_property = appsync.CfnDataSource.HttpConfigProperty(
                    endpoint="endpoint",
                
                    # the properties below are optional
                    authorization_config=appsync.CfnDataSource.AuthorizationConfigProperty(
                        authorization_type="authorizationType",
                
                        # the properties below are optional
                        aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                            signing_region="signingRegion",
                            signing_service_name="signingServiceName"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d4a6ece9757475b2fd78d8a95bd18c7fd68758c889cf5d07cea125e31a32258)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
            }
            if authorization_config is not None:
                self._values["authorization_config"] = authorization_config

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.AuthorizationConfigProperty"]]:
            '''The authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.AuthorizationConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.LambdaConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_function_arn": "lambdaFunctionArn"},
    )
    class LambdaConfigProperty:
        def __init__(self, *, lambda_function_arn: builtins.str) -> None:
            '''The ``LambdaConfig`` property type specifies the Lambda function ARN for an AWS AppSync data source.

            ``LambdaConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            :param lambda_function_arn: The ARN for the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                lambda_config_property = appsync.CfnDataSource.LambdaConfigProperty(
                    lambda_function_arn="lambdaFunctionArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47ae7467c676f94be4511c7fb68e47ed5c3c90dde218c9a12592924c98f7837e)
                check_type(argname="argument lambda_function_arn", value=lambda_function_arn, expected_type=type_hints["lambda_function_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_function_arn": lambda_function_arn,
            }

        @builtins.property
        def lambda_function_arn(self) -> builtins.str:
            '''The ARN for the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html#cfn-appsync-datasource-lambdaconfig-lambdafunctionarn
            '''
            result = self._values.get("lambda_function_arn")
            assert result is not None, "Required property 'lambda_function_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.OpenSearchServiceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_region": "awsRegion", "endpoint": "endpoint"},
    )
    class OpenSearchServiceConfigProperty:
        def __init__(self, *, aws_region: builtins.str, endpoint: builtins.str) -> None:
            '''The ``OpenSearchServiceConfig`` property type specifies the ``AwsRegion`` and ``Endpoints`` for an Amazon OpenSearch Service domain in your account for an AWS AppSync data source.

            ``OpenSearchServiceConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            :param aws_region: The AWS Region.
            :param endpoint: The endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                open_search_service_config_property = appsync.CfnDataSource.OpenSearchServiceConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fecf5845831a0e0a203174a1662e533c942ecf67ea1e85e246e7a029865de49)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "endpoint": endpoint,
            }

        @builtins.property
        def aws_region(self) -> builtins.str:
            '''The AWS Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html#cfn-appsync-datasource-opensearchserviceconfig-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html#cfn-appsync-datasource-opensearchserviceconfig-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenSearchServiceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.RdsHttpEndpointConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "aws_secret_store_arn": "awsSecretStoreArn",
            "db_cluster_identifier": "dbClusterIdentifier",
            "database_name": "databaseName",
            "schema": "schema",
        },
    )
    class RdsHttpEndpointConfigProperty:
        def __init__(
            self,
            *,
            aws_region: builtins.str,
            aws_secret_store_arn: builtins.str,
            db_cluster_identifier: builtins.str,
            database_name: typing.Optional[builtins.str] = None,
            schema: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the ``RdsHttpEndpointConfig`` property type to specify the ``RdsHttpEndpoint`` for an AWS AppSync relational database.

            ``RdsHttpEndpointConfig`` is a property of the `AWS AppSync DataSource RelationalDatabaseConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html>`_ resource.

            :param aws_region: AWS Region for RDS HTTP endpoint.
            :param aws_secret_store_arn: The ARN for database credentials stored in AWS Secrets Manager .
            :param db_cluster_identifier: Amazon RDS cluster Amazon Resource Name (ARN).
            :param database_name: Logical database name.
            :param schema: Logical schema name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                rds_http_endpoint_config_property = appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                    aws_region="awsRegion",
                    aws_secret_store_arn="awsSecretStoreArn",
                    db_cluster_identifier="dbClusterIdentifier",
                
                    # the properties below are optional
                    database_name="databaseName",
                    schema="schema"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__348849422fd4d08e7490da175f7a5ffa84cad62dcd8d49557a3436740b3dffd5)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument aws_secret_store_arn", value=aws_secret_store_arn, expected_type=type_hints["aws_secret_store_arn"])
                check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "aws_secret_store_arn": aws_secret_store_arn,
                "db_cluster_identifier": db_cluster_identifier,
            }
            if database_name is not None:
                self._values["database_name"] = database_name
            if schema is not None:
                self._values["schema"] = schema

        @builtins.property
        def aws_region(self) -> builtins.str:
            '''AWS Region for RDS HTTP endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_secret_store_arn(self) -> builtins.str:
            '''The ARN for database credentials stored in AWS Secrets Manager .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awssecretstorearn
            '''
            result = self._values.get("aws_secret_store_arn")
            assert result is not None, "Required property 'aws_secret_store_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def db_cluster_identifier(self) -> builtins.str:
            '''Amazon RDS cluster Amazon Resource Name (ARN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-dbclusteridentifier
            '''
            result = self._values.get("db_cluster_identifier")
            assert result is not None, "Required property 'db_cluster_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''Logical database name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema(self) -> typing.Optional[builtins.str]:
            '''Logical schema name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-schema
            '''
            result = self._values.get("schema")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RdsHttpEndpointConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnDataSource.RelationalDatabaseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "relational_database_source_type": "relationalDatabaseSourceType",
            "rds_http_endpoint_config": "rdsHttpEndpointConfig",
        },
    )
    class RelationalDatabaseConfigProperty:
        def __init__(
            self,
            *,
            relational_database_source_type: builtins.str,
            rds_http_endpoint_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RdsHttpEndpointConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Use the ``RelationalDatabaseConfig`` property type to specify ``RelationalDatabaseConfig`` for an AWS AppSync data source.

            ``RelationalDatabaseConfig`` is a property of the `AWS::AppSync::DataSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`_ property type.

            :param relational_database_source_type: The type of relational data source.
            :param rds_http_endpoint_config: Information about the Amazon RDS resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                relational_database_config_property = appsync.CfnDataSource.RelationalDatabaseConfigProperty(
                    relational_database_source_type="relationalDatabaseSourceType",
                
                    # the properties below are optional
                    rds_http_endpoint_config=appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                        aws_region="awsRegion",
                        aws_secret_store_arn="awsSecretStoreArn",
                        db_cluster_identifier="dbClusterIdentifier",
                
                        # the properties below are optional
                        database_name="databaseName",
                        schema="schema"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4357a1467126648487c710ab6683bf4d3954927d7c54c51b699c6f185a943236)
                check_type(argname="argument relational_database_source_type", value=relational_database_source_type, expected_type=type_hints["relational_database_source_type"])
                check_type(argname="argument rds_http_endpoint_config", value=rds_http_endpoint_config, expected_type=type_hints["rds_http_endpoint_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "relational_database_source_type": relational_database_source_type,
            }
            if rds_http_endpoint_config is not None:
                self._values["rds_http_endpoint_config"] = rds_http_endpoint_config

        @builtins.property
        def relational_database_source_type(self) -> builtins.str:
            '''The type of relational data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-relationaldatabasesourcetype
            '''
            result = self._values.get("relational_database_source_type")
            assert result is not None, "Required property 'relational_database_source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rds_http_endpoint_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RdsHttpEndpointConfigProperty"]]:
            '''Information about the Amazon RDS resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-rdshttpendpointconfig
            '''
            result = self._values.get("rds_http_endpoint_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RdsHttpEndpointConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalDatabaseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "name": "name",
        "type": "type",
        "description": "description",
        "dynamo_db_config": "dynamoDbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "event_bridge_config": "eventBridgeConfig",
        "http_config": "httpConfig",
        "lambda_config": "lambdaConfig",
        "open_search_service_config": "openSearchServiceConfig",
        "relational_database_config": "relationalDatabaseConfig",
        "service_role_arn": "serviceRoleArn",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.EventBridgeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataSource``.

        :param api_id: Unique AWS AppSync GraphQL API identifier where this data source will be created.
        :param name: Friendly name for you to identify your AppSync data source after creation.
        :param type: The type of the data source. - *AWS_LAMBDA* : The data source is an AWS Lambda function. - *AMAZON_DYNAMODB* : The data source is an Amazon DynamoDB table. - *AMAZON_ELASTICSEARCH* : The data source is an Amazon OpenSearch Service domain. - *AMAZON_EVENTBRIDGE* : The data source is an Amazon EventBridge event bus. - *AMAZON_OPENSEARCH_SERVICE* : The data source is an Amazon OpenSearch Service domain. - *NONE* : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation. - *HTTP* : The data source is an HTTP endpoint. - *RELATIONAL_DATABASE* : The data source is a relational database.
        :param description: The description of the data source.
        :param dynamo_db_config: AWS Region and TableName for an Amazon DynamoDB table in your account.
        :param elasticsearch_config: AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account. As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.
        :param event_bridge_config: An EventBridge configuration that contains a valid ARN of an event bus.
        :param http_config: Endpoints for an HTTP data source.
        :param lambda_config: An ARN of a Lambda function in valid ARN format. This can be the ARN of a Lambda function that exists in the current account or in another account.
        :param open_search_service_config: AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.
        :param relational_database_config: Relational Database configuration of the relational database data source.
        :param service_role_arn: The AWS Identity and Access Management service role ARN for the data source. The system assumes this role when accessing the data source. Required if ``Type`` is specified as ``AWS_LAMBDA`` , ``AMAZON_DYNAMODB`` , ``AMAZON_ELASTICSEARCH`` , ``AMAZON_EVENTBRIDGE`` , or ``AMAZON_OPENSEARCH_SERVICE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_data_source_props = appsync.CfnDataSourceProps(
                api_id="apiId",
                name="name",
                type="type",
            
                # the properties below are optional
                description="description",
                dynamo_db_config=appsync.CfnDataSource.DynamoDBConfigProperty(
                    aws_region="awsRegion",
                    table_name="tableName",
            
                    # the properties below are optional
                    delta_sync_config=appsync.CfnDataSource.DeltaSyncConfigProperty(
                        base_table_ttl="baseTableTtl",
                        delta_sync_table_name="deltaSyncTableName",
                        delta_sync_table_ttl="deltaSyncTableTtl"
                    ),
                    use_caller_credentials=False,
                    versioned=False
                ),
                elasticsearch_config=appsync.CfnDataSource.ElasticsearchConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                ),
                event_bridge_config=appsync.CfnDataSource.EventBridgeConfigProperty(
                    event_bus_arn="eventBusArn"
                ),
                http_config=appsync.CfnDataSource.HttpConfigProperty(
                    endpoint="endpoint",
            
                    # the properties below are optional
                    authorization_config=appsync.CfnDataSource.AuthorizationConfigProperty(
                        authorization_type="authorizationType",
            
                        # the properties below are optional
                        aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                            signing_region="signingRegion",
                            signing_service_name="signingServiceName"
                        )
                    )
                ),
                lambda_config=appsync.CfnDataSource.LambdaConfigProperty(
                    lambda_function_arn="lambdaFunctionArn"
                ),
                open_search_service_config=appsync.CfnDataSource.OpenSearchServiceConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                ),
                relational_database_config=appsync.CfnDataSource.RelationalDatabaseConfigProperty(
                    relational_database_source_type="relationalDatabaseSourceType",
            
                    # the properties below are optional
                    rds_http_endpoint_config=appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                        aws_region="awsRegion",
                        aws_secret_store_arn="awsSecretStoreArn",
                        db_cluster_identifier="dbClusterIdentifier",
            
                        # the properties below are optional
                        database_name="databaseName",
                        schema="schema"
                    )
                ),
                service_role_arn="serviceRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a27321db4878d92375c672ad2fd1de24e61150d04b9a9b7f544b60bf81d6d7)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamo_db_config", value=dynamo_db_config, expected_type=type_hints["dynamo_db_config"])
            check_type(argname="argument elasticsearch_config", value=elasticsearch_config, expected_type=type_hints["elasticsearch_config"])
            check_type(argname="argument event_bridge_config", value=event_bridge_config, expected_type=type_hints["event_bridge_config"])
            check_type(argname="argument http_config", value=http_config, expected_type=type_hints["http_config"])
            check_type(argname="argument lambda_config", value=lambda_config, expected_type=type_hints["lambda_config"])
            check_type(argname="argument open_search_service_config", value=open_search_service_config, expected_type=type_hints["open_search_service_config"])
            check_type(argname="argument relational_database_config", value=relational_database_config, expected_type=type_hints["relational_database_config"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if dynamo_db_config is not None:
            self._values["dynamo_db_config"] = dynamo_db_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if event_bridge_config is not None:
            self._values["event_bridge_config"] = event_bridge_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if open_search_service_config is not None:
            self._values["open_search_service_config"] = open_search_service_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn

    @builtins.property
    def api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API identifier where this data source will be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Friendly name for you to identify your AppSync data source after creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the data source.

        - *AWS_LAMBDA* : The data source is an AWS Lambda function.
        - *AMAZON_DYNAMODB* : The data source is an Amazon DynamoDB table.
        - *AMAZON_ELASTICSEARCH* : The data source is an Amazon OpenSearch Service domain.
        - *AMAZON_EVENTBRIDGE* : The data source is an Amazon EventBridge event bus.
        - *AMAZON_OPENSEARCH_SERVICE* : The data source is an Amazon OpenSearch Service domain.
        - *NONE* : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
        - *HTTP* : The data source is an HTTP endpoint.
        - *RELATIONAL_DATABASE* : The data source is a relational database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DynamoDBConfigProperty]]:
        '''AWS Region and TableName for an Amazon DynamoDB table in your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-dynamodbconfig
        '''
        result = self._values.get("dynamo_db_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DynamoDBConfigProperty]], result)

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ElasticsearchConfigProperty]]:
        '''AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.

        As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service . This property is deprecated. For new data sources, use *OpenSearchServiceConfig* to specify an OpenSearch Service data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-elasticsearchconfig
        '''
        result = self._values.get("elasticsearch_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ElasticsearchConfigProperty]], result)

    @builtins.property
    def event_bridge_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.EventBridgeConfigProperty]]:
        '''An EventBridge configuration that contains a valid ARN of an event bus.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-eventbridgeconfig
        '''
        result = self._values.get("event_bridge_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.EventBridgeConfigProperty]], result)

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.HttpConfigProperty]]:
        '''Endpoints for an HTTP data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-httpconfig
        '''
        result = self._values.get("http_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.HttpConfigProperty]], result)

    @builtins.property
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.LambdaConfigProperty]]:
        '''An ARN of a Lambda function in valid ARN format.

        This can be the ARN of a Lambda function that exists in the current account or in another account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-lambdaconfig
        '''
        result = self._values.get("lambda_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.LambdaConfigProperty]], result)

    @builtins.property
    def open_search_service_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.OpenSearchServiceConfigProperty]]:
        '''AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-opensearchserviceconfig
        '''
        result = self._values.get("open_search_service_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.OpenSearchServiceConfigProperty]], result)

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RelationalDatabaseConfigProperty]]:
        '''Relational Database configuration of the relational database data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-relationaldatabaseconfig
        '''
        result = self._values.get("relational_database_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RelationalDatabaseConfigProperty]], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''The AWS Identity and Access Management service role ARN for the data source.

        The system assumes this role when accessing the data source.

        Required if ``Type`` is specified as ``AWS_LAMBDA`` , ``AMAZON_DYNAMODB`` , ``AMAZON_ELASTICSEARCH`` , ``AMAZON_EVENTBRIDGE`` , or ``AMAZON_OPENSEARCH_SERVICE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDomainName(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnDomainName",
):
    '''The ``AWS::AppSync::DomainName`` resource creates a ``DomainNameConfig`` object to configure a custom domain.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_domain_name = appsync.CfnDomainName(self, "MyCfnDomainName",
            certificate_arn="certificateArn",
            domain_name="domainName",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        certificate_arn: builtins.str,
        domain_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate. This will be an AWS Certificate Manager certificate.
        :param domain_name: The domain name.
        :param description: The decription for your domain name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678693553586e835af6ffdc6ac5860f81ffd96791de73368d44d41d3a220fa5b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainNameProps(
            certificate_arn=certificate_arn,
            domain_name=domain_name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1bb36f58b6037c649f6de5b27bf9555b52f554bb5fe4108f80d1e6143cb6f24)
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
            type_hints = typing.get_type_hints(_typecheckingstub__45a3cf8beadfc199c9c9d148139af66f311d5dbd310ca59a7062e7f26c40c037)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAppSyncDomainName")
    def attr_app_sync_domain_name(self) -> builtins.str:
        '''The domain name provided by AWS AppSync .

        :cloudformationAttribute: AppSyncDomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppSyncDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''The domain name.

        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrHostedZoneId")
    def attr_hosted_zone_id(self) -> builtins.str:
        '''The ID of your Amazon Route 53 hosted zone.

        :cloudformationAttribute: HostedZoneId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21881e6a0cbde3bc434364c90ea094d149b2b6df42d7fc1beaa6dc2b7dfe9eca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d87464e3fb9b21e5511a8f5b32d36667e3c9d7faaf4d9cd05b6f5a75145649f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The decription for your domain name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc72a5388fe698c3e3240ed821a6e614471584c2ffb80f06028269bf9d78d46e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.implements(_IInspectable_c2943556)
class CfnDomainNameApiAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnDomainNameApiAssociation",
):
    '''The ``AWS::AppSync::DomainNameApiAssociation`` resource represents the mapping of your custom domain name to the assigned API URL.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_domain_name_api_association = appsync.CfnDomainNameApiAssociation(self, "MyCfnDomainNameApiAssociation",
            api_id="apiId",
            domain_name="domainName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        domain_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API ID.
        :param domain_name: The domain name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053707dba2452392a89bf081ac7d866beeff7c348bacbfe351a815a6372a43d5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainNameApiAssociationProps(
            api_id=api_id, domain_name=domain_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__942757d7ea72d07c8e5e78524b0a4e08dae920c7a26e14bfd77a565345201d36)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03652b1dc4a3294dad3ea732f92fa774dc0eda1cb1fe6263bac9fe9718f6e63b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiAssociationIdentifier")
    def attr_api_association_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApiAssociationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiAssociationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API ID.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1373752dfc88f0800245faefb7696b22aadcc994b58e7c2c57cd7f058ad814b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dd7f18cf3cb236d2ffa804f6505477d416e7b844f92f9ba86f74aea18663216)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnDomainNameApiAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"api_id": "apiId", "domain_name": "domainName"},
)
class CfnDomainNameApiAssociationProps:
    def __init__(self, *, api_id: builtins.str, domain_name: builtins.str) -> None:
        '''Properties for defining a ``CfnDomainNameApiAssociation``.

        :param api_id: The API ID.
        :param domain_name: The domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_domain_name_api_association_props = appsync.CfnDomainNameApiAssociationProps(
                api_id="apiId",
                domain_name="domainName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a899ca55570211a5da411a83f28448dd1e54a82a4e83cb8d8ca2b1f292ebf5)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "domain_name": domain_name,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html#cfn-appsync-domainnameapiassociation-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html#cfn-appsync-domainnameapiassociation-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainNameApiAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnDomainNameProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_arn": "certificateArn",
        "domain_name": "domainName",
        "description": "description",
    },
)
class CfnDomainNameProps:
    def __init__(
        self,
        *,
        certificate_arn: builtins.str,
        domain_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomainName``.

        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate. This will be an AWS Certificate Manager certificate.
        :param domain_name: The domain name.
        :param description: The decription for your domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_domain_name_props = appsync.CfnDomainNameProps(
                certificate_arn="certificateArn",
                domain_name="domainName",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b0d09d8c1a97bdb5c0b0b95b798fbeb11f45abb25769bdb71d1903471361a5c)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
            "domain_name": domain_name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate.

        This will be an AWS Certificate Manager certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-certificatearn
        '''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The decription for your domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainNameProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFunctionConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfiguration",
):
    '''The ``AWS::AppSync::FunctionConfiguration`` resource defines the functions in GraphQL APIs to perform certain operations.

    You can use pipeline resolvers to attach functions. For more information, see `Pipeline Resolvers <https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html>`_ in the *AWS AppSync Developer Guide* .
    .. epigraph::

       When you submit an update, AWS CloudFormation updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the AWS CloudFormation template. Changing the Amazon S3 file content without changing a property value will not result in an update operation.

       See `Update Behaviors of Stack Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html>`_ in the *AWS CloudFormation User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_function_configuration = appsync.CfnFunctionConfiguration(self, "MyCfnFunctionConfiguration",
            api_id="apiId",
            data_source_name="dataSourceName",
            name="name",
        
            # the properties below are optional
            code="code",
            code_s3_location="codeS3Location",
            description="description",
            function_version="functionVersion",
            max_batch_size=123,
            request_mapping_template="requestMappingTemplate",
            request_mapping_template_s3_location="requestMappingTemplateS3Location",
            response_mapping_template="responseMappingTemplate",
            response_mapping_template_s3_location="responseMappingTemplateS3Location",
            runtime=appsync.CfnFunctionConfiguration.AppSyncRuntimeProperty(
                name="name",
                runtime_version="runtimeVersion"
            ),
            sync_config=appsync.CfnFunctionConfiguration.SyncConfigProperty(
                conflict_detection="conflictDetection",
        
                # the properties below are optional
                conflict_handler="conflictHandler",
                lambda_conflict_handler_config=appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty(
                    lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        data_source_name: builtins.str,
        name: builtins.str,
        code: typing.Optional[builtins.str] = None,
        code_s3_location: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        function_version: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionConfiguration.AppSyncRuntimeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionConfiguration.SyncConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The AWS AppSync GraphQL API that you want to attach using this function.
        :param data_source_name: The name of data source this function will attach.
        :param name: The name of the function.
        :param code: The ``resolver`` code that contains the request and response functions. When code is used, the ``runtime`` is required. The runtime value must be ``APPSYNC_JS`` .
        :param code_s3_location: The Amazon S3 endpoint.
        :param description: The ``Function`` description.
        :param function_version: The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.
        :param max_batch_size: The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.
        :param request_mapping_template: The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
        :param request_mapping_template_s3_location: Describes a Sync configuration for a resolver. Contains information on which Conflict Detection, as well as Resolution strategy, should be performed when the resolver is invoked.
        :param response_mapping_template: The ``Function`` response mapping template.
        :param response_mapping_template_s3_location: The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param runtime: Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.
        :param sync_config: Describes a Sync configuration for a resolver. Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a4866dafc094db4e3a18f26e71e3f210828f39f8958d47fe2d4c085adc6ff8f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFunctionConfigurationProps(
            api_id=api_id,
            data_source_name=data_source_name,
            name=name,
            code=code,
            code_s3_location=code_s3_location,
            description=description,
            function_version=function_version,
            max_batch_size=max_batch_size,
            request_mapping_template=request_mapping_template,
            request_mapping_template_s3_location=request_mapping_template_s3_location,
            response_mapping_template=response_mapping_template,
            response_mapping_template_s3_location=response_mapping_template_s3_location,
            runtime=runtime,
            sync_config=sync_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b5daa219cb13e40ed1b20203fde593fe20c2c92bd36d7a071b49bcec839439b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__36f15942d1b688b5a1072d376a057d8302c1e87743f5a5200ad9fc3b45987f7a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDataSourceName")
    def attr_data_source_name(self) -> builtins.str:
        '''The name of data source this function will attach.

        :cloudformationAttribute: DataSourceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataSourceName"))

    @builtins.property
    @jsii.member(jsii_name="attrFunctionArn")
    def attr_function_arn(self) -> builtins.str:
        '''ARN of the function, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/functions/functionId`` .

        :cloudformationAttribute: FunctionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFunctionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFunctionId")
    def attr_function_id(self) -> builtins.str:
        '''The unique ID of this function.

        :cloudformationAttribute: FunctionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFunctionId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the function.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API that you want to attach using this function.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddada6f46239ab33eec4921b4ac0cf9484ba0c89258d9ca8117a0ecf69c7631a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> builtins.str:
        '''The name of data source this function will attach.'''
        return typing.cast(builtins.str, jsii.get(self, "dataSourceName"))

    @data_source_name.setter
    def data_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9493c684f0dde1a9223d5146974c138d33dbf89e0c56ed8d6d23f69b357bcde1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the function.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bcf772bf0a6d98d280769ee4b3e0c374a4881be9dfcc56425285f343d8c9a87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Optional[builtins.str]:
        '''The ``resolver`` code that contains the request and response functions.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "code"))

    @code.setter
    def code(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f176cd8f4e930d504d5f35fb87b141d2a2d197149a0763d630b94186516de330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="codeS3Location")
    def code_s3_location(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeS3Location"))

    @code_s3_location.setter
    def code_s3_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e20f51155c39c20c83124659b8133fc87948adf8035794534cadf37a3e7265e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e87fe0dd6ec9c662347f3659e76d0bd6308df654c93fd61f384e0c29e5eb24b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> typing.Optional[builtins.str]:
        '''The version of the request mapping template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionVersion"))

    @function_version.setter
    def function_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b218cd4f3808007654247768d1242189a48a8632f1621b5b37ab5e4ccc0f4a9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionVersion", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchSize")
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchSize"))

    @max_batch_size.setter
    def max_batch_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9abf526bb6e39ee9360616d137b1625f90523f036a39b05e1cf79037baad4f63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchSize", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` request mapping template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplate"))

    @request_mapping_template.setter
    def request_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96a54d609ccde1c57b832776c4db93d393395273ac718e900a8503eaeb43283e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''Describes a Sync configuration for a resolver.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplateS3Location"))

    @request_mapping_template_s3_location.setter
    def request_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1031c7b0aa54c899315716446946b7d1e3385d7b3fb6f6d1d31ea4f653ad3cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` response mapping template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplate"))

    @response_mapping_template.setter
    def response_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45788eaccf27f4038c701605c623bce576d7990af5337245691eb20581091c26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a response mapping template in an Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplateS3Location"))

    @response_mapping_template_s3_location.setter
    def response_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b40fcc0e01043cbd9cdf55c416d462b00a65d35ca5fdef3bfa9d0b412afbb19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionConfiguration.AppSyncRuntimeProperty"]]:
        '''Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionConfiguration.AppSyncRuntimeProperty"]], jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionConfiguration.AppSyncRuntimeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__143abf7cef16b0a5749a28fb00575ff2cb3a1f027e142a59f5e914c1776d09fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionConfiguration.SyncConfigProperty"]]:
        '''Describes a Sync configuration for a resolver.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionConfiguration.SyncConfigProperty"]], jsii.get(self, "syncConfig"))

    @sync_config.setter
    def sync_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionConfiguration.SyncConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d1624e61da41b1be885253dc0b667a61deba82d80481d4d6a6b5430b507b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfiguration.AppSyncRuntimeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "runtime_version": "runtimeVersion"},
    )
    class AppSyncRuntimeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            runtime_version: builtins.str,
        ) -> None:
            '''Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function.

            Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.

            :param name: The ``name`` of the runtime to use. Currently, the only allowed value is ``APPSYNC_JS`` .
            :param runtime_version: The ``version`` of the runtime to use. Currently, the only allowed version is ``1.0.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                app_sync_runtime_property = appsync.CfnFunctionConfiguration.AppSyncRuntimeProperty(
                    name="name",
                    runtime_version="runtimeVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b82405295f439f31600277f9055bf514ac45e79afd73f5b14450b84beac6e5c)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "runtime_version": runtime_version,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The ``name`` of the runtime to use.

            Currently, the only allowed value is ``APPSYNC_JS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html#cfn-appsync-functionconfiguration-appsyncruntime-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def runtime_version(self) -> builtins.str:
            '''The ``version`` of the runtime to use.

            Currently, the only allowed version is ``1.0.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html#cfn-appsync-functionconfiguration-appsyncruntime-runtimeversion
            '''
            result = self._values.get("runtime_version")
            assert result is not None, "Required property 'runtime_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppSyncRuntimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
    )
    class LambdaConflictHandlerConfigProperty:
        def __init__(
            self,
            *,
            lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LambdaConflictHandlerConfig`` object when configuring ``LAMBDA`` as the Conflict Handler.

            :param lambda_conflict_handler_arn: The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                lambda_conflict_handler_config_property = appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty(
                    lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e67576fdd79515010563035ffc15df29a57e00be079931631598d07f7178f0c3)
                check_type(argname="argument lambda_conflict_handler_arn", value=lambda_conflict_handler_arn, expected_type=type_hints["lambda_conflict_handler_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_conflict_handler_arn is not None:
                self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

        @builtins.property
        def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html#cfn-appsync-functionconfiguration-lambdaconflicthandlerconfig-lambdaconflicthandlerarn
            '''
            result = self._values.get("lambda_conflict_handler_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConflictHandlerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfiguration.SyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conflict_detection": "conflictDetection",
            "conflict_handler": "conflictHandler",
            "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
        },
    )
    class SyncConfigProperty:
        def __init__(
            self,
            *,
            conflict_detection: builtins.str,
            conflict_handler: typing.Optional[builtins.str] = None,
            lambda_conflict_handler_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a Sync configuration for a resolver.

            Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

            :param conflict_detection: The Conflict Detection strategy to use. - *VERSION* : Detect conflicts based on object versions for this resolver. - *NONE* : Do not detect conflicts when invoking this resolver.
            :param conflict_handler: The Conflict Resolution strategy to perform in the event of a conflict. - *OPTIMISTIC_CONCURRENCY* : Resolve conflicts by rejecting mutations when versions don't match the latest version at the server. - *AUTOMERGE* : Resolve conflicts with the Automerge conflict resolution strategy. - *LAMBDA* : Resolve conflicts with an AWS Lambda function supplied in the ``LambdaConflictHandlerConfig`` .
            :param lambda_conflict_handler_config: The ``LambdaConflictHandlerConfig`` when configuring ``LAMBDA`` as the Conflict Handler.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                sync_config_property = appsync.CfnFunctionConfiguration.SyncConfigProperty(
                    conflict_detection="conflictDetection",
                
                    # the properties below are optional
                    conflict_handler="conflictHandler",
                    lambda_conflict_handler_config=appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty(
                        lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__441bd762beaec70fd67cf86d84e674beae78bf0e9f78d94f1b683b403e7b47f1)
                check_type(argname="argument conflict_detection", value=conflict_detection, expected_type=type_hints["conflict_detection"])
                check_type(argname="argument conflict_handler", value=conflict_handler, expected_type=type_hints["conflict_handler"])
                check_type(argname="argument lambda_conflict_handler_config", value=lambda_conflict_handler_config, expected_type=type_hints["lambda_conflict_handler_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "conflict_detection": conflict_detection,
            }
            if conflict_handler is not None:
                self._values["conflict_handler"] = conflict_handler
            if lambda_conflict_handler_config is not None:
                self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

        @builtins.property
        def conflict_detection(self) -> builtins.str:
            '''The Conflict Detection strategy to use.

            - *VERSION* : Detect conflicts based on object versions for this resolver.
            - *NONE* : Do not detect conflicts when invoking this resolver.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-conflictdetection
            '''
            result = self._values.get("conflict_detection")
            assert result is not None, "Required property 'conflict_detection' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def conflict_handler(self) -> typing.Optional[builtins.str]:
            '''The Conflict Resolution strategy to perform in the event of a conflict.

            - *OPTIMISTIC_CONCURRENCY* : Resolve conflicts by rejecting mutations when versions don't match the latest version at the server.
            - *AUTOMERGE* : Resolve conflicts with the Automerge conflict resolution strategy.
            - *LAMBDA* : Resolve conflicts with an AWS Lambda function supplied in the ``LambdaConflictHandlerConfig`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-conflicthandler
            '''
            result = self._values.get("conflict_handler")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lambda_conflict_handler_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty"]]:
            '''The ``LambdaConflictHandlerConfig`` when configuring ``LAMBDA`` as the Conflict Handler.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-lambdaconflicthandlerconfig
            '''
            result = self._values.get("lambda_conflict_handler_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnFunctionConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "data_source_name": "dataSourceName",
        "name": "name",
        "code": "code",
        "code_s3_location": "codeS3Location",
        "description": "description",
        "function_version": "functionVersion",
        "max_batch_size": "maxBatchSize",
        "request_mapping_template": "requestMappingTemplate",
        "request_mapping_template_s3_location": "requestMappingTemplateS3Location",
        "response_mapping_template": "responseMappingTemplate",
        "response_mapping_template_s3_location": "responseMappingTemplateS3Location",
        "runtime": "runtime",
        "sync_config": "syncConfig",
    },
)
class CfnFunctionConfigurationProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        data_source_name: builtins.str,
        name: builtins.str,
        code: typing.Optional[builtins.str] = None,
        code_s3_location: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        function_version: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionConfiguration.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFunctionConfiguration``.

        :param api_id: The AWS AppSync GraphQL API that you want to attach using this function.
        :param data_source_name: The name of data source this function will attach.
        :param name: The name of the function.
        :param code: The ``resolver`` code that contains the request and response functions. When code is used, the ``runtime`` is required. The runtime value must be ``APPSYNC_JS`` .
        :param code_s3_location: The Amazon S3 endpoint.
        :param description: The ``Function`` description.
        :param function_version: The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.
        :param max_batch_size: The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.
        :param request_mapping_template: The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
        :param request_mapping_template_s3_location: Describes a Sync configuration for a resolver. Contains information on which Conflict Detection, as well as Resolution strategy, should be performed when the resolver is invoked.
        :param response_mapping_template: The ``Function`` response mapping template.
        :param response_mapping_template_s3_location: The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param runtime: Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.
        :param sync_config: Describes a Sync configuration for a resolver. Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_function_configuration_props = appsync.CfnFunctionConfigurationProps(
                api_id="apiId",
                data_source_name="dataSourceName",
                name="name",
            
                # the properties below are optional
                code="code",
                code_s3_location="codeS3Location",
                description="description",
                function_version="functionVersion",
                max_batch_size=123,
                request_mapping_template="requestMappingTemplate",
                request_mapping_template_s3_location="requestMappingTemplateS3Location",
                response_mapping_template="responseMappingTemplate",
                response_mapping_template_s3_location="responseMappingTemplateS3Location",
                runtime=appsync.CfnFunctionConfiguration.AppSyncRuntimeProperty(
                    name="name",
                    runtime_version="runtimeVersion"
                ),
                sync_config=appsync.CfnFunctionConfiguration.SyncConfigProperty(
                    conflict_detection="conflictDetection",
            
                    # the properties below are optional
                    conflict_handler="conflictHandler",
                    lambda_conflict_handler_config=appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty(
                        lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68fb3836c61478b4bf652995d052fa027e6b2f6b9606529969b49a74037c3061)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument data_source_name", value=data_source_name, expected_type=type_hints["data_source_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument code_s3_location", value=code_s3_location, expected_type=type_hints["code_s3_location"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument function_version", value=function_version, expected_type=type_hints["function_version"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument request_mapping_template_s3_location", value=request_mapping_template_s3_location, expected_type=type_hints["request_mapping_template_s3_location"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument response_mapping_template_s3_location", value=response_mapping_template_s3_location, expected_type=type_hints["response_mapping_template_s3_location"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument sync_config", value=sync_config, expected_type=type_hints["sync_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "data_source_name": data_source_name,
            "name": name,
        }
        if code is not None:
            self._values["code"] = code
        if code_s3_location is not None:
            self._values["code_s3_location"] = code_s3_location
        if description is not None:
            self._values["description"] = description
        if function_version is not None:
            self._values["function_version"] = function_version
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if request_mapping_template_s3_location is not None:
            self._values["request_mapping_template_s3_location"] = request_mapping_template_s3_location
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if response_mapping_template_s3_location is not None:
            self._values["response_mapping_template_s3_location"] = response_mapping_template_s3_location
        if runtime is not None:
            self._values["runtime"] = runtime
        if sync_config is not None:
            self._values["sync_config"] = sync_config

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API that you want to attach using this function.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_name(self) -> builtins.str:
        '''The name of data source this function will attach.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename
        '''
        result = self._values.get("data_source_name")
        assert result is not None, "Required property 'data_source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the function.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''The ``resolver`` code that contains the request and response functions.

        When code is used, the ``runtime`` is required. The runtime value must be ``APPSYNC_JS`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-code
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_s3_location(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-codes3location
        '''
        result = self._values.get("code_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_version(self) -> typing.Optional[builtins.str]:
        '''The version of the request mapping template.

        Currently, only the 2018-05-29 version of the template is supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-functionversion
        '''
        result = self._values.get("function_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-maxbatchsize
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` request mapping template.

        Functions support only the 2018-05-29 version of the request mapping template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplate
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''Describes a Sync configuration for a resolver.

        Contains information on which Conflict Detection, as well as Resolution strategy, should be performed when the resolver is invoked.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplates3location
        '''
        result = self._values.get("request_mapping_template_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The ``Function`` response mapping template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplate
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a response mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplates3location
        '''
        result = self._values.get("response_mapping_template_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionConfiguration.AppSyncRuntimeProperty]]:
        '''Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function.

        Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-runtime
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionConfiguration.AppSyncRuntimeProperty]], result)

    @builtins.property
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionConfiguration.SyncConfigProperty]]:
        '''Describes a Sync configuration for a resolver.

        Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-syncconfig
        '''
        result = self._values.get("sync_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionConfiguration.SyncConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGraphQLApi(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi",
):
    '''The ``AWS::AppSync::GraphQLApi`` resource creates a new AWS AppSync GraphQL API.

    This is the top-level construct for your application. For more information, see `Quick Start <https://docs.aws.amazon.com/appsync/latest/devguide/quickstart.html>`_ in the *AWS AppSync Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_graph_qLApi = appsync.CfnGraphQLApi(self, "MyCfnGraphQLApi",
            authentication_type="authenticationType",
            name="name",
        
            # the properties below are optional
            additional_authentication_providers=[appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty(
                authentication_type="authenticationType",
        
                # the properties below are optional
                lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                    authorizer_result_ttl_in_seconds=123,
                    authorizer_uri="authorizerUri",
                    identity_validation_expression="identityValidationExpression"
                ),
                open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                    auth_ttl=123,
                    client_id="clientId",
                    iat_ttl=123,
                    issuer="issuer"
                ),
                user_pool_config=appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty(
                    app_id_client_regex="appIdClientRegex",
                    aws_region="awsRegion",
                    user_pool_id="userPoolId"
                )
            )],
            api_type="apiType",
            lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                authorizer_result_ttl_in_seconds=123,
                authorizer_uri="authorizerUri",
                identity_validation_expression="identityValidationExpression"
            ),
            log_config=appsync.CfnGraphQLApi.LogConfigProperty(
                cloud_watch_logs_role_arn="cloudWatchLogsRoleArn",
                exclude_verbose_content=False,
                field_log_level="fieldLogLevel"
            ),
            merged_api_execution_role_arn="mergedApiExecutionRoleArn",
            open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                auth_ttl=123,
                client_id="clientId",
                iat_ttl=123,
                issuer="issuer"
            ),
            owner_contact="ownerContact",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_pool_config=appsync.CfnGraphQLApi.UserPoolConfigProperty(
                app_id_client_regex="appIdClientRegex",
                aws_region="awsRegion",
                default_action="defaultAction",
                user_pool_id="userPoolId"
            ),
            visibility="visibility",
            xray_enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraphQLApi.AdditionalAuthenticationProviderProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        api_type: typing.Optional[builtins.str] = None,
        lambda_authorizer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraphQLApi.LogConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        merged_api_execution_role_arn: typing.Optional[builtins.str] = None,
        open_id_connect_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        owner_contact: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_pool_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraphQLApi.UserPoolConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        visibility: typing.Optional[builtins.str] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authentication_type: Security configuration for your GraphQL API. For allowed values (such as ``API_KEY`` , ``AWS_IAM`` , ``AMAZON_COGNITO_USER_POOLS`` , ``OPENID_CONNECT`` , or ``AWS_LAMBDA`` ), see `Security <https://docs.aws.amazon.com/appsync/latest/devguide/security.html>`_ in the *AWS AppSync Developer Guide* .
        :param name: The API name.
        :param additional_authentication_providers: A list of additional authentication providers for the ``GraphqlApi`` API.
        :param api_type: The value that indicates whether the GraphQL API is a standard API ( ``GRAPHQL`` ) or merged API ( ``MERGED`` ). *WARNING* : If the ``ApiType`` has not been defined, *explicitly* setting it to ``GRAPHQL`` in a template/stack update will result in an API replacement and new DNS values. The following values are valid: ``GRAPHQL | MERGED``
        :param lambda_authorizer_config: A ``LambdaAuthorizerConfig`` holds configuration on how to authorize AWS AppSync API access when using the ``AWS_LAMBDA`` authorizer mode. Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.
        :param log_config: The Amazon CloudWatch Logs configuration.
        :param merged_api_execution_role_arn: The AWS Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the ``AUTO_MERGE`` to update the merged API endpoint with the source API changes automatically.
        :param open_id_connect_config: The OpenID Connect configuration.
        :param owner_contact: The owner contact information for an API resource. This field accepts any string input with a length of 0 - 256 characters.
        :param tags: An arbitrary set of tags (key-value pairs) for this GraphQL API.
        :param user_pool_config: Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.
        :param visibility: Sets the scope of the GraphQL API to public ( ``GLOBAL`` ) or private ( ``PRIVATE`` ). By default, the scope is set to ``Global`` if no value is provided. *WARNING* : If ``Visibility`` has not been defined, *explicitly* setting it to ``GLOBAL`` in a template/stack update will result in an API replacement and new DNS values.
        :param xray_enabled: A flag indicating whether to use AWS X-Ray tracing for this ``GraphqlApi`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54e0e0488820e5a410f75b28895d4271db1e58bd6c71e17fd04fcf3fad8696a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphQLApiProps(
            authentication_type=authentication_type,
            name=name,
            additional_authentication_providers=additional_authentication_providers,
            api_type=api_type,
            lambda_authorizer_config=lambda_authorizer_config,
            log_config=log_config,
            merged_api_execution_role_arn=merged_api_execution_role_arn,
            open_id_connect_config=open_id_connect_config,
            owner_contact=owner_contact,
            tags=tags,
            user_pool_config=user_pool_config,
            visibility=visibility,
            xray_enabled=xray_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef4f44613a72787cd83e4ceef509edefaabdb020300442c1eeb53ff3e20f525)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea2cc823b2c4f8c7f428fa2f0fe71c624a069d90ef8d4385d598404adbc586eb)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiId")
    def attr_api_id(self) -> builtins.str:
        '''Unique AWS AppSync GraphQL API identifier.

        :cloudformationAttribute: ApiId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the API key, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGraphQlDns")
    def attr_graph_ql_dns(self) -> builtins.str:
        '''The fully qualified domain name (FQDN) of the endpoint URL of your GraphQL API.

        :cloudformationAttribute: GraphQLDns
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGraphQlDns"))

    @builtins.property
    @jsii.member(jsii_name="attrGraphQlUrl")
    def attr_graph_ql_url(self) -> builtins.str:
        '''The Endpoint URL of your GraphQL API.

        :cloudformationAttribute: GraphQLUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGraphQlUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRealtimeDns")
    def attr_realtime_dns(self) -> builtins.str:
        '''The fully qualified domain name (FQDN) of the real-time endpoint URL of your GraphQL API.

        :cloudformationAttribute: RealtimeDns
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRealtimeDns"))

    @builtins.property
    @jsii.member(jsii_name="attrRealtimeUrl")
    def attr_realtime_url(self) -> builtins.str:
        '''The GraphQL API real-time endpoint URL.

        For more information, see `Discovering the real-time endpoint from the GraphQL endpoint <https://docs.aws.amazon.com/appsync/latest/devguide/real-time-websocket-client.html#handshake-details-to-establish-the-websocket-connection>`_ .

        :cloudformationAttribute: RealtimeUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRealtimeUrl"))

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
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        '''Security configuration for your GraphQL API.'''
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddf538537f9f940e10be3bb6aba02fdfaf8dc4a1cd2d9271f52eb0cc89a879de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The API name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6a61daae035f26bd4c76cf79a3d576be1077bd308cfbd0ecde402238ce095e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticationProviders")
    def additional_authentication_providers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.AdditionalAuthenticationProviderProperty"]]]]:
        '''A list of additional authentication providers for the ``GraphqlApi`` API.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.AdditionalAuthenticationProviderProperty"]]]], jsii.get(self, "additionalAuthenticationProviders"))

    @additional_authentication_providers.setter
    def additional_authentication_providers(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.AdditionalAuthenticationProviderProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d98241da3432e0393c78db49e66414c7e91e9bfc9e19f06380f6b18215ab489)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalAuthenticationProviders", value)

    @builtins.property
    @jsii.member(jsii_name="apiType")
    def api_type(self) -> typing.Optional[builtins.str]:
        '''The value that indicates whether the GraphQL API is a standard API ( ``GRAPHQL`` ) or merged API ( ``MERGED`` ).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiType"))

    @api_type.setter
    def api_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__368741733832ba6f2bd8963ff6065a1471cd003f84d5567a1b4ac4e31f866fa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiType", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.LambdaAuthorizerConfigProperty"]]:
        '''A ``LambdaAuthorizerConfig`` holds configuration on how to authorize AWS AppSync API access when using the ``AWS_LAMBDA`` authorizer mode.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.LambdaAuthorizerConfigProperty"]], jsii.get(self, "lambdaAuthorizerConfig"))

    @lambda_authorizer_config.setter
    def lambda_authorizer_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.LambdaAuthorizerConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ceade9d24f423834d3485476af5c7e3bd2e0ea0899583af5ac44f01e70b244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaAuthorizerConfig", value)

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.LogConfigProperty"]]:
        '''The Amazon CloudWatch Logs configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.LogConfigProperty"]], jsii.get(self, "logConfig"))

    @log_config.setter
    def log_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.LogConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c0d15f646c5975aec4d344a5e6150a6fec6655df6d4354b817aef3ce9053464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logConfig", value)

    @builtins.property
    @jsii.member(jsii_name="mergedApiExecutionRoleArn")
    def merged_api_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The AWS Identity and Access Management service role ARN for a merged API.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergedApiExecutionRoleArn"))

    @merged_api_execution_role_arn.setter
    def merged_api_execution_role_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a871b44b3bee02deb37b3334dce3879c119dd687537efd2eea807744ffb2d34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergedApiExecutionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="openIdConnectConfig")
    def open_id_connect_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.OpenIDConnectConfigProperty"]]:
        '''The OpenID Connect configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.OpenIDConnectConfigProperty"]], jsii.get(self, "openIdConnectConfig"))

    @open_id_connect_config.setter
    def open_id_connect_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.OpenIDConnectConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf051032d1109f154a4b02f8368044e2e1266c9008da417ccef7aa84293cc125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openIdConnectConfig", value)

    @builtins.property
    @jsii.member(jsii_name="ownerContact")
    def owner_contact(self) -> typing.Optional[builtins.str]:
        '''The owner contact information for an API resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerContact"))

    @owner_contact.setter
    def owner_contact(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76e99145104b4c7d697f40bb2242cf89f15fb4638f7c19d492e1c5813994e82d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerContact", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key-value pairs) for this GraphQL API.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b6bd673e24289c51e9fb96c96f3ee2bf2f7af27ef9ebcc4ae16d3cdee34b6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.UserPoolConfigProperty"]]:
        '''Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.UserPoolConfigProperty"]], jsii.get(self, "userPoolConfig"))

    @user_pool_config.setter
    def user_pool_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.UserPoolConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1d04f36c4d7d5f26bce761153a8d93212a34634f3833d3080b56cdd7a05e70b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolConfig", value)

    @builtins.property
    @jsii.member(jsii_name="visibility")
    def visibility(self) -> typing.Optional[builtins.str]:
        '''Sets the scope of the GraphQL API to public ( ``GLOBAL`` ) or private ( ``PRIVATE`` ).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibility"))

    @visibility.setter
    def visibility(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f56ad4ee938b5ce91c10b6490094e6f1986e84540a95b138577851adf6e569a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibility", value)

    @builtins.property
    @jsii.member(jsii_name="xrayEnabled")
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag indicating whether to use AWS X-Ray tracing for this ``GraphqlApi`` .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "xrayEnabled"))

    @xray_enabled.setter
    def xray_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__863eb629614a817210cd5e0eb8ae7d3264658e2121ad2529a6090b38cd038199)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xrayEnabled", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_type": "authenticationType",
            "lambda_authorizer_config": "lambdaAuthorizerConfig",
            "open_id_connect_config": "openIdConnectConfig",
            "user_pool_config": "userPoolConfig",
        },
    )
    class AdditionalAuthenticationProviderProperty:
        def __init__(
            self,
            *,
            authentication_type: builtins.str,
            lambda_authorizer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraphQLApi.LambdaAuthorizerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            open_id_connect_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user_pool_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGraphQLApi.CognitoUserPoolConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes an additional authentication provider.

            :param authentication_type: The authentication type for API key, AWS Identity and Access Management , OIDC, Amazon Cognito user pools , or AWS Lambda . Valid Values: ``API_KEY`` | ``AWS_IAM`` | ``OPENID_CONNECT`` | ``AMAZON_COGNITO_USER_POOLS`` | ``AWS_LAMBDA``
            :param lambda_authorizer_config: Configuration for AWS Lambda function authorization.
            :param open_id_connect_config: The OIDC configuration.
            :param user_pool_config: The Amazon Cognito user pool configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                additional_authentication_provider_property = appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty(
                    authentication_type="authenticationType",
                
                    # the properties below are optional
                    lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                        authorizer_result_ttl_in_seconds=123,
                        authorizer_uri="authorizerUri",
                        identity_validation_expression="identityValidationExpression"
                    ),
                    open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                        auth_ttl=123,
                        client_id="clientId",
                        iat_ttl=123,
                        issuer="issuer"
                    ),
                    user_pool_config=appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty(
                        app_id_client_regex="appIdClientRegex",
                        aws_region="awsRegion",
                        user_pool_id="userPoolId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f8233eaa1ce5aeb807b7fe9374215f842f67afc12ed29dcbdf6773df7cd328a4)
                check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
                check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
                check_type(argname="argument open_id_connect_config", value=open_id_connect_config, expected_type=type_hints["open_id_connect_config"])
                check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authentication_type": authentication_type,
            }
            if lambda_authorizer_config is not None:
                self._values["lambda_authorizer_config"] = lambda_authorizer_config
            if open_id_connect_config is not None:
                self._values["open_id_connect_config"] = open_id_connect_config
            if user_pool_config is not None:
                self._values["user_pool_config"] = user_pool_config

        @builtins.property
        def authentication_type(self) -> builtins.str:
            '''The authentication type for API key, AWS Identity and Access Management , OIDC, Amazon Cognito user pools , or AWS Lambda .

            Valid Values: ``API_KEY`` | ``AWS_IAM`` | ``OPENID_CONNECT`` | ``AMAZON_COGNITO_USER_POOLS`` | ``AWS_LAMBDA``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype
            '''
            result = self._values.get("authentication_type")
            assert result is not None, "Required property 'authentication_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def lambda_authorizer_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.LambdaAuthorizerConfigProperty"]]:
            '''Configuration for AWS Lambda function authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-lambdaauthorizerconfig
            '''
            result = self._values.get("lambda_authorizer_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.LambdaAuthorizerConfigProperty"]], result)

        @builtins.property
        def open_id_connect_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.OpenIDConnectConfigProperty"]]:
            '''The OIDC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-openidconnectconfig
            '''
            result = self._values.get("open_id_connect_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.OpenIDConnectConfigProperty"]], result)

        @builtins.property
        def user_pool_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.CognitoUserPoolConfigProperty"]]:
            '''The Amazon Cognito user pool configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-userpoolconfig
            '''
            result = self._values.get("user_pool_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGraphQLApi.CognitoUserPoolConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdditionalAuthenticationProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_id_client_regex": "appIdClientRegex",
            "aws_region": "awsRegion",
            "user_pool_id": "userPoolId",
        },
    )
    class CognitoUserPoolConfigProperty:
        def __init__(
            self,
            *,
            app_id_client_regex: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
            user_pool_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an Amazon Cognito user pool configuration.

            :param app_id_client_regex: A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.
            :param aws_region: The AWS Region in which the user pool was created.
            :param user_pool_id: The user pool ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                cognito_user_pool_config_property = appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty(
                    app_id_client_regex="appIdClientRegex",
                    aws_region="awsRegion",
                    user_pool_id="userPoolId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05b5c78d0d6cf8f2e5de126a1b379f17cb44634afea4439cb4b2b3c893dee502)
                check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_id_client_regex is not None:
                self._values["app_id_client_regex"] = app_id_client_regex
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def app_id_client_regex(self) -> typing.Optional[builtins.str]:
            '''A regular expression for validating the incoming Amazon Cognito user pool app client ID.

            If this value isn't set, no filtering is applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-appidclientregex
            '''
            result = self._values.get("app_id_client_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region in which the user pool was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_pool_id(self) -> typing.Optional[builtins.str]:
            '''The user pool ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-userpoolid
            '''
            result = self._values.get("user_pool_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoUserPoolConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
            "authorizer_uri": "authorizerUri",
            "identity_validation_expression": "identityValidationExpression",
        },
    )
    class LambdaAuthorizerConfigProperty:
        def __init__(
            self,
            *,
            authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
            authorizer_uri: typing.Optional[builtins.str] = None,
            identity_validation_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for AWS Lambda function authorization.

            :param authorizer_result_ttl_in_seconds: The number of seconds a response should be cached for. The default is 0 seconds, which disables caching. If you don't specify a value for ``authorizerResultTtlInSeconds`` , the default value is used. The maximum value is one hour (3600 seconds). The Lambda function can override this by returning a ``ttlOverride`` key in its response.
            :param authorizer_uri: The ARN of the Lambda function to be called for authorization. This may be a standard Lambda ARN, a version ARN ( ``.../v3`` ) or alias ARN. *Note* : This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To do so with the AWS CLI , run the following: ``aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction``
            :param identity_validation_expression: A regular expression for validation of tokens before the Lambda function is called.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                lambda_authorizer_config_property = appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                    authorizer_result_ttl_in_seconds=123,
                    authorizer_uri="authorizerUri",
                    identity_validation_expression="identityValidationExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f9291a235c0bd7ecea6f37d1aa830ec180ae9518e0555f8a98722d8088b1895)
                check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
                check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
                check_type(argname="argument identity_validation_expression", value=identity_validation_expression, expected_type=type_hints["identity_validation_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorizer_result_ttl_in_seconds is not None:
                self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
            if authorizer_uri is not None:
                self._values["authorizer_uri"] = authorizer_uri
            if identity_validation_expression is not None:
                self._values["identity_validation_expression"] = identity_validation_expression

        @builtins.property
        def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds a response should be cached for.

            The default is 0 seconds, which disables caching. If you don't specify a value for ``authorizerResultTtlInSeconds`` , the default value is used. The maximum value is one hour (3600 seconds). The Lambda function can override this by returning a ``ttlOverride`` key in its response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-authorizerresultttlinseconds
            '''
            result = self._values.get("authorizer_result_ttl_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def authorizer_uri(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Lambda function to be called for authorization.

            This may be a standard Lambda ARN, a version ARN ( ``.../v3`` ) or alias ARN.

            *Note* : This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To do so with the AWS CLI , run the following:

            ``aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-authorizeruri
            '''
            result = self._values.get("authorizer_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def identity_validation_expression(self) -> typing.Optional[builtins.str]:
            '''A regular expression for validation of tokens before the Lambda function is called.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-identityvalidationexpression
            '''
            result = self._values.get("identity_validation_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaAuthorizerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.LogConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_role_arn": "cloudWatchLogsRoleArn",
            "exclude_verbose_content": "excludeVerboseContent",
            "field_log_level": "fieldLogLevel",
        },
    )
    class LogConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
            exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            field_log_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LogConfig`` property type specifies the logging configuration when writing GraphQL operations and tracing to Amazon CloudWatch for an AWS AppSync GraphQL API.

            ``LogConfig`` is a property of the `AWS::AppSync::GraphQLApi <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html>`_ property type.

            :param cloud_watch_logs_role_arn: The service role that AWS AppSync will assume to publish to Amazon CloudWatch Logs in your account.
            :param exclude_verbose_content: Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.
            :param field_log_level: The field logging level. Values can be NONE, ERROR, or ALL. - *NONE* : No field-level logs are captured. - *ERROR* : Logs the following information only for the fields that are in error: - The error section in the server response. - Field-level errors. - The generated request/response functions that got resolved for error fields. - *ALL* : The following information is logged for all fields in the query: - Field-level tracing information. - The generated request/response functions that got resolved for each field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                log_config_property = appsync.CfnGraphQLApi.LogConfigProperty(
                    cloud_watch_logs_role_arn="cloudWatchLogsRoleArn",
                    exclude_verbose_content=False,
                    field_log_level="fieldLogLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9ff7e1cb756f4b27770bf07bfb18b0936eea6dc27410d5c20b3b259d960d7a3)
                check_type(argname="argument cloud_watch_logs_role_arn", value=cloud_watch_logs_role_arn, expected_type=type_hints["cloud_watch_logs_role_arn"])
                check_type(argname="argument exclude_verbose_content", value=exclude_verbose_content, expected_type=type_hints["exclude_verbose_content"])
                check_type(argname="argument field_log_level", value=field_log_level, expected_type=type_hints["field_log_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs_role_arn is not None:
                self._values["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
            if exclude_verbose_content is not None:
                self._values["exclude_verbose_content"] = exclude_verbose_content
            if field_log_level is not None:
                self._values["field_log_level"] = field_log_level

        @builtins.property
        def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
            '''The service role that AWS AppSync will assume to publish to Amazon CloudWatch Logs in your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-cloudwatchlogsrolearn
            '''
            result = self._values.get("cloud_watch_logs_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclude_verbose_content(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-excludeverbosecontent
            '''
            result = self._values.get("exclude_verbose_content")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def field_log_level(self) -> typing.Optional[builtins.str]:
            '''The field logging level. Values can be NONE, ERROR, or ALL.

            - *NONE* : No field-level logs are captured.
            - *ERROR* : Logs the following information only for the fields that are in error:
            - The error section in the server response.
            - Field-level errors.
            - The generated request/response functions that got resolved for error fields.
            - *ALL* : The following information is logged for all fields in the query:
            - Field-level tracing information.
            - The generated request/response functions that got resolved for each field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-fieldloglevel
            '''
            result = self._values.get("field_log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.OpenIDConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_ttl": "authTtl",
            "client_id": "clientId",
            "iat_ttl": "iatTtl",
            "issuer": "issuer",
        },
    )
    class OpenIDConnectConfigProperty:
        def __init__(
            self,
            *,
            auth_ttl: typing.Optional[jsii.Number] = None,
            client_id: typing.Optional[builtins.str] = None,
            iat_ttl: typing.Optional[jsii.Number] = None,
            issuer: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``OpenIDConnectConfig`` property type specifies the optional authorization configuration for using an OpenID Connect compliant service with your GraphQL endpoint for an AWS AppSync GraphQL API.

            ``OpenIDConnectConfig`` is a property of the `AWS::AppSync::GraphQLApi <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html>`_ property type.

            :param auth_ttl: The number of milliseconds that a token is valid after being authenticated.
            :param client_id: The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.
            :param iat_ttl: The number of milliseconds that a token is valid after it's issued to a user.
            :param issuer: The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                open_iDConnect_config_property = appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                    auth_ttl=123,
                    client_id="clientId",
                    iat_ttl=123,
                    issuer="issuer"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07e62ce520030272762ccf6169ce5673be0610bd412fd2d9b9a3a7c7963d4853)
                check_type(argname="argument auth_ttl", value=auth_ttl, expected_type=type_hints["auth_ttl"])
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument iat_ttl", value=iat_ttl, expected_type=type_hints["iat_ttl"])
                check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auth_ttl is not None:
                self._values["auth_ttl"] = auth_ttl
            if client_id is not None:
                self._values["client_id"] = client_id
            if iat_ttl is not None:
                self._values["iat_ttl"] = iat_ttl
            if issuer is not None:
                self._values["issuer"] = issuer

        @builtins.property
        def auth_ttl(self) -> typing.Optional[jsii.Number]:
            '''The number of milliseconds that a token is valid after being authenticated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-authttl
            '''
            result = self._values.get("auth_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def client_id(self) -> typing.Optional[builtins.str]:
            '''The client identifier of the Relying party at the OpenID identity provider.

            This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-clientid
            '''
            result = self._values.get("client_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iat_ttl(self) -> typing.Optional[jsii.Number]:
            '''The number of milliseconds that a token is valid after it's issued to a user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-iatttl
            '''
            result = self._values.get("iat_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def issuer(self) -> typing.Optional[builtins.str]:
            '''The issuer for the OIDC configuration.

            The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-issuer
            '''
            result = self._values.get("issuer")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenIDConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApi.UserPoolConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_id_client_regex": "appIdClientRegex",
            "aws_region": "awsRegion",
            "default_action": "defaultAction",
            "user_pool_id": "userPoolId",
        },
    )
    class UserPoolConfigProperty:
        def __init__(
            self,
            *,
            app_id_client_regex: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
            default_action: typing.Optional[builtins.str] = None,
            user_pool_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``UserPoolConfig`` property type specifies the optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint for an AWS AppSync GraphQL API.

            :param app_id_client_regex: A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.
            :param aws_region: The AWS Region in which the user pool was created.
            :param default_action: The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration. When specifying Amazon Cognito user pools as the default authentication, you must set the value for ``DefaultAction`` to ``ALLOW`` if specifying ``AdditionalAuthenticationProviders`` .
            :param user_pool_id: The user pool ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                user_pool_config_property = appsync.CfnGraphQLApi.UserPoolConfigProperty(
                    app_id_client_regex="appIdClientRegex",
                    aws_region="awsRegion",
                    default_action="defaultAction",
                    user_pool_id="userPoolId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f0d0849f2d6ffc2b4b6a4eabed8e631f4ae22772572c4eae3d63c7ec6f2a4a4)
                check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
                check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_id_client_regex is not None:
                self._values["app_id_client_regex"] = app_id_client_regex
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if default_action is not None:
                self._values["default_action"] = default_action
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def app_id_client_regex(self) -> typing.Optional[builtins.str]:
            '''A regular expression for validating the incoming Amazon Cognito user pool app client ID.

            If this value isn't set, no filtering is applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-appidclientregex
            '''
            result = self._values.get("app_id_client_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region in which the user pool was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_action(self) -> typing.Optional[builtins.str]:
            '''The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.

            When specifying Amazon Cognito user pools as the default authentication, you must set the value for ``DefaultAction`` to ``ALLOW`` if specifying ``AdditionalAuthenticationProviders`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-defaultaction
            '''
            result = self._values.get("default_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_pool_id(self) -> typing.Optional[builtins.str]:
            '''The user pool ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-userpoolid
            '''
            result = self._values.get("user_pool_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPoolConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "name": "name",
        "additional_authentication_providers": "additionalAuthenticationProviders",
        "api_type": "apiType",
        "lambda_authorizer_config": "lambdaAuthorizerConfig",
        "log_config": "logConfig",
        "merged_api_execution_role_arn": "mergedApiExecutionRoleArn",
        "open_id_connect_config": "openIdConnectConfig",
        "owner_contact": "ownerContact",
        "tags": "tags",
        "user_pool_config": "userPoolConfig",
        "visibility": "visibility",
        "xray_enabled": "xrayEnabled",
    },
)
class CfnGraphQLApiProps:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        api_type: typing.Optional[builtins.str] = None,
        lambda_authorizer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        log_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.LogConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        merged_api_execution_role_arn: typing.Optional[builtins.str] = None,
        open_id_connect_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        owner_contact: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_pool_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.UserPoolConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        visibility: typing.Optional[builtins.str] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraphQLApi``.

        :param authentication_type: Security configuration for your GraphQL API. For allowed values (such as ``API_KEY`` , ``AWS_IAM`` , ``AMAZON_COGNITO_USER_POOLS`` , ``OPENID_CONNECT`` , or ``AWS_LAMBDA`` ), see `Security <https://docs.aws.amazon.com/appsync/latest/devguide/security.html>`_ in the *AWS AppSync Developer Guide* .
        :param name: The API name.
        :param additional_authentication_providers: A list of additional authentication providers for the ``GraphqlApi`` API.
        :param api_type: The value that indicates whether the GraphQL API is a standard API ( ``GRAPHQL`` ) or merged API ( ``MERGED`` ). *WARNING* : If the ``ApiType`` has not been defined, *explicitly* setting it to ``GRAPHQL`` in a template/stack update will result in an API replacement and new DNS values. The following values are valid: ``GRAPHQL | MERGED``
        :param lambda_authorizer_config: A ``LambdaAuthorizerConfig`` holds configuration on how to authorize AWS AppSync API access when using the ``AWS_LAMBDA`` authorizer mode. Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.
        :param log_config: The Amazon CloudWatch Logs configuration.
        :param merged_api_execution_role_arn: The AWS Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the ``AUTO_MERGE`` to update the merged API endpoint with the source API changes automatically.
        :param open_id_connect_config: The OpenID Connect configuration.
        :param owner_contact: The owner contact information for an API resource. This field accepts any string input with a length of 0 - 256 characters.
        :param tags: An arbitrary set of tags (key-value pairs) for this GraphQL API.
        :param user_pool_config: Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.
        :param visibility: Sets the scope of the GraphQL API to public ( ``GLOBAL`` ) or private ( ``PRIVATE`` ). By default, the scope is set to ``Global`` if no value is provided. *WARNING* : If ``Visibility`` has not been defined, *explicitly* setting it to ``GLOBAL`` in a template/stack update will result in an API replacement and new DNS values.
        :param xray_enabled: A flag indicating whether to use AWS X-Ray tracing for this ``GraphqlApi`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_graph_qLApi_props = appsync.CfnGraphQLApiProps(
                authentication_type="authenticationType",
                name="name",
            
                # the properties below are optional
                additional_authentication_providers=[appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty(
                    authentication_type="authenticationType",
            
                    # the properties below are optional
                    lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                        authorizer_result_ttl_in_seconds=123,
                        authorizer_uri="authorizerUri",
                        identity_validation_expression="identityValidationExpression"
                    ),
                    open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                        auth_ttl=123,
                        client_id="clientId",
                        iat_ttl=123,
                        issuer="issuer"
                    ),
                    user_pool_config=appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty(
                        app_id_client_regex="appIdClientRegex",
                        aws_region="awsRegion",
                        user_pool_id="userPoolId"
                    )
                )],
                api_type="apiType",
                lambda_authorizer_config=appsync.CfnGraphQLApi.LambdaAuthorizerConfigProperty(
                    authorizer_result_ttl_in_seconds=123,
                    authorizer_uri="authorizerUri",
                    identity_validation_expression="identityValidationExpression"
                ),
                log_config=appsync.CfnGraphQLApi.LogConfigProperty(
                    cloud_watch_logs_role_arn="cloudWatchLogsRoleArn",
                    exclude_verbose_content=False,
                    field_log_level="fieldLogLevel"
                ),
                merged_api_execution_role_arn="mergedApiExecutionRoleArn",
                open_id_connect_config=appsync.CfnGraphQLApi.OpenIDConnectConfigProperty(
                    auth_ttl=123,
                    client_id="clientId",
                    iat_ttl=123,
                    issuer="issuer"
                ),
                owner_contact="ownerContact",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_pool_config=appsync.CfnGraphQLApi.UserPoolConfigProperty(
                    app_id_client_regex="appIdClientRegex",
                    aws_region="awsRegion",
                    default_action="defaultAction",
                    user_pool_id="userPoolId"
                ),
                visibility="visibility",
                xray_enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c30fb6e2b0bf2994b166c6091173ca1bbdf2a226ff26da5bfc0c35067fc8cc07)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_authentication_providers", value=additional_authentication_providers, expected_type=type_hints["additional_authentication_providers"])
            check_type(argname="argument api_type", value=api_type, expected_type=type_hints["api_type"])
            check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument merged_api_execution_role_arn", value=merged_api_execution_role_arn, expected_type=type_hints["merged_api_execution_role_arn"])
            check_type(argname="argument open_id_connect_config", value=open_id_connect_config, expected_type=type_hints["open_id_connect_config"])
            check_type(argname="argument owner_contact", value=owner_contact, expected_type=type_hints["owner_contact"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
            check_type(argname="argument xray_enabled", value=xray_enabled, expected_type=type_hints["xray_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
            "name": name,
        }
        if additional_authentication_providers is not None:
            self._values["additional_authentication_providers"] = additional_authentication_providers
        if api_type is not None:
            self._values["api_type"] = api_type
        if lambda_authorizer_config is not None:
            self._values["lambda_authorizer_config"] = lambda_authorizer_config
        if log_config is not None:
            self._values["log_config"] = log_config
        if merged_api_execution_role_arn is not None:
            self._values["merged_api_execution_role_arn"] = merged_api_execution_role_arn
        if open_id_connect_config is not None:
            self._values["open_id_connect_config"] = open_id_connect_config
        if owner_contact is not None:
            self._values["owner_contact"] = owner_contact
        if tags is not None:
            self._values["tags"] = tags
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config
        if visibility is not None:
            self._values["visibility"] = visibility
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''Security configuration for your GraphQL API.

        For allowed values (such as ``API_KEY`` , ``AWS_IAM`` , ``AMAZON_COGNITO_USER_POOLS`` , ``OPENID_CONNECT`` , or ``AWS_LAMBDA`` ), see `Security <https://docs.aws.amazon.com/appsync/latest/devguide/security.html>`_ in the *AWS AppSync Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype
        '''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The API name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_authentication_providers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.AdditionalAuthenticationProviderProperty]]]]:
        '''A list of additional authentication providers for the ``GraphqlApi`` API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-additionalauthenticationproviders
        '''
        result = self._values.get("additional_authentication_providers")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.AdditionalAuthenticationProviderProperty]]]], result)

    @builtins.property
    def api_type(self) -> typing.Optional[builtins.str]:
        '''The value that indicates whether the GraphQL API is a standard API ( ``GRAPHQL`` ) or merged API ( ``MERGED`` ).

        *WARNING* : If the ``ApiType`` has not been defined, *explicitly* setting it to ``GRAPHQL`` in a template/stack update will result in an API replacement and new DNS values.

        The following values are valid:

        ``GRAPHQL | MERGED``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-apitype
        '''
        result = self._values.get("api_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_authorizer_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.LambdaAuthorizerConfigProperty]]:
        '''A ``LambdaAuthorizerConfig`` holds configuration on how to authorize AWS AppSync API access when using the ``AWS_LAMBDA`` authorizer mode.

        Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig
        '''
        result = self._values.get("lambda_authorizer_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.LambdaAuthorizerConfigProperty]], result)

    @builtins.property
    def log_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.LogConfigProperty]]:
        '''The Amazon CloudWatch Logs configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.LogConfigProperty]], result)

    @builtins.property
    def merged_api_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The AWS Identity and Access Management service role ARN for a merged API.

        The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the ``AUTO_MERGE`` to update the merged API endpoint with the source API changes automatically.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-mergedapiexecutionrolearn
        '''
        result = self._values.get("merged_api_execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def open_id_connect_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.OpenIDConnectConfigProperty]]:
        '''The OpenID Connect configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig
        '''
        result = self._values.get("open_id_connect_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.OpenIDConnectConfigProperty]], result)

    @builtins.property
    def owner_contact(self) -> typing.Optional[builtins.str]:
        '''The owner contact information for an API resource.

        This field accepts any string input with a length of 0 - 256 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-ownercontact
        '''
        result = self._values.get("owner_contact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key-value pairs) for this GraphQL API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_pool_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.UserPoolConfigProperty]]:
        '''Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig
        '''
        result = self._values.get("user_pool_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.UserPoolConfigProperty]], result)

    @builtins.property
    def visibility(self) -> typing.Optional[builtins.str]:
        '''Sets the scope of the GraphQL API to public ( ``GLOBAL`` ) or private ( ``PRIVATE`` ).

        By default, the scope is set to ``Global`` if no value is provided.

        *WARNING* : If ``Visibility`` has not been defined, *explicitly* setting it to ``GLOBAL`` in a template/stack update will result in an API replacement and new DNS values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-visibility
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A flag indicating whether to use AWS X-Ray tracing for this ``GraphqlApi`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled
        '''
        result = self._values.get("xray_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphQLApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGraphQLSchema(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLSchema",
):
    '''The ``AWS::AppSync::GraphQLSchema`` resource is used for your AWS AppSync GraphQL schema that controls the data model for your API.

    Schema files are text written in Schema Definition Language (SDL) format. For more information about schema authoring, see `Designing a GraphQL API <https://docs.aws.amazon.com/appsync/latest/devguide/designing-a-graphql-api.html>`_ in the *AWS AppSync Developer Guide* .
    .. epigraph::

       When you submit an update, AWS CloudFormation updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the CloudFormation template. Changing the Amazon S3 file content without changing a property value will not result in an update operation.

       See `Update Behaviors of Stack Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html>`_ in the *AWS CloudFormation User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_graph_qLSchema = appsync.CfnGraphQLSchema(self, "MyCfnGraphQLSchema",
            api_id="apiId",
        
            # the properties below are optional
            definition="definition",
            definition_s3_location="definitionS3Location"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        definition: typing.Optional[builtins.str] = None,
        definition_s3_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The AWS AppSync GraphQL API identifier to which you want to apply this schema.
        :param definition: The text representation of a GraphQL schema in SDL format. For more information about using the ``Ref`` function, see `Ref <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref>`_ .
        :param definition_s3_location: The location of a GraphQL schema file in an Amazon S3 bucket. Use this if you want to provision with the schema living in Amazon S3 rather than embedding it in your CloudFormation template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86eeb90bbb1ca5a453f08cfb90f5fb16cf4842431fc90d63f3ee21972f1be243)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphQLSchemaProps(
            api_id=api_id,
            definition=definition,
            definition_s3_location=definition_s3_location,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6052290b218f085df44320d030dc5da2a656bc2dfb652a6e8997c198d7360074)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5e7b1316522ac1b9a93d87179eb23379f7762341da46fd001056a8704a20b2c)
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
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API identifier to which you want to apply this schema.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__555a23d4ba449beaaf98ed745a155165b6830286b0aeae2a45d326885e8eddef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Optional[builtins.str]:
        '''The text representation of a GraphQL schema in SDL format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "definition"))

    @definition.setter
    def definition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29a3a5e0c95af4007408f43ded6d8b16b50975200325f9066820c3302d03398)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="definitionS3Location")
    def definition_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a GraphQL schema file in an Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "definitionS3Location"))

    @definition_s3_location.setter
    def definition_s3_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4848140e56b16e4736cedb1aa2fb1ca3fd82aeca7e977c876274b365740b08de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionS3Location", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnGraphQLSchemaProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "definition": "definition",
        "definition_s3_location": "definitionS3Location",
    },
)
class CfnGraphQLSchemaProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        definition: typing.Optional[builtins.str] = None,
        definition_s3_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraphQLSchema``.

        :param api_id: The AWS AppSync GraphQL API identifier to which you want to apply this schema.
        :param definition: The text representation of a GraphQL schema in SDL format. For more information about using the ``Ref`` function, see `Ref <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref>`_ .
        :param definition_s3_location: The location of a GraphQL schema file in an Amazon S3 bucket. Use this if you want to provision with the schema living in Amazon S3 rather than embedding it in your CloudFormation template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_graph_qLSchema_props = appsync.CfnGraphQLSchemaProps(
                api_id="apiId",
            
                # the properties below are optional
                definition="definition",
                definition_s3_location="definitionS3Location"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20c7b2f1eadba8a608fdb8a0a590a3907eb9c891f22a7385f17ef74294ca1d0c)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument definition_s3_location", value=definition_s3_location, expected_type=type_hints["definition_s3_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
        }
        if definition is not None:
            self._values["definition"] = definition
        if definition_s3_location is not None:
            self._values["definition_s3_location"] = definition_s3_location

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API identifier to which you want to apply this schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def definition(self) -> typing.Optional[builtins.str]:
        '''The text representation of a GraphQL schema in SDL format.

        For more information about using the ``Ref`` function, see `Ref <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition
        '''
        result = self._values.get("definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def definition_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a GraphQL schema file in an Amazon S3 bucket.

        Use this if you want to provision with the schema living in Amazon S3 rather than embedding it in your CloudFormation template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location
        '''
        result = self._values.get("definition_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphQLSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResolver(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnResolver",
):
    '''The ``AWS::AppSync::Resolver`` resource defines the logical GraphQL resolver that you attach to fields in a schema.

    Request and response templates for resolvers are written in Apache Velocity Template Language (VTL) format. For more information about resolvers, see `Resolver Mapping Template Reference <https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference.html>`_ .
    .. epigraph::

       When you submit an update, AWS CloudFormation updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the CloudFormation template. Changing the Amazon S3 file content without changing a property value will not result in an update operation.

       See `Update Behaviors of Stack Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html>`_ in the *AWS CloudFormation User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_resolver = appsync.CfnResolver(self, "MyCfnResolver",
            api_id="apiId",
            field_name="fieldName",
            type_name="typeName",
        
            # the properties below are optional
            caching_config=appsync.CfnResolver.CachingConfigProperty(
                ttl=123,
        
                # the properties below are optional
                caching_keys=["cachingKeys"]
            ),
            code="code",
            code_s3_location="codeS3Location",
            data_source_name="dataSourceName",
            kind="kind",
            max_batch_size=123,
            pipeline_config=appsync.CfnResolver.PipelineConfigProperty(
                functions=["functions"]
            ),
            request_mapping_template="requestMappingTemplate",
            request_mapping_template_s3_location="requestMappingTemplateS3Location",
            response_mapping_template="responseMappingTemplate",
            response_mapping_template_s3_location="responseMappingTemplateS3Location",
            runtime=appsync.CfnResolver.AppSyncRuntimeProperty(
                name="name",
                runtime_version="runtimeVersion"
            ),
            sync_config=appsync.CfnResolver.SyncConfigProperty(
                conflict_detection="conflictDetection",
        
                # the properties below are optional
                conflict_handler="conflictHandler",
                lambda_conflict_handler_config=appsync.CfnResolver.LambdaConflictHandlerConfigProperty(
                    lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResolver.CachingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        code: typing.Optional[builtins.str] = None,
        code_s3_location: typing.Optional[builtins.str] = None,
        data_source_name: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResolver.PipelineConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResolver.AppSyncRuntimeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResolver.SyncConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The AWS AppSync GraphQL API to which you want to attach this resolver.
        :param field_name: The GraphQL field on a type that invokes the resolver.
        :param type_name: The GraphQL type that invokes this resolver.
        :param caching_config: The caching configuration for the resolver.
        :param code: The ``resolver`` code that contains the request and response functions. When code is used, the ``runtime`` is required. The runtime value must be ``APPSYNC_JS`` .
        :param code_s3_location: The Amazon S3 endpoint.
        :param data_source_name: The resolver data source name.
        :param kind: The resolver type. - *UNIT* : A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source. - *PIPELINE* : A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of ``Function`` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.
        :param max_batch_size: The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.
        :param pipeline_config: Functions linked with the pipeline resolver.
        :param request_mapping_template: The request mapping template. Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.
        :param request_mapping_template_s3_location: The location of a request mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param response_mapping_template: The response mapping template.
        :param response_mapping_template_s3_location: The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param runtime: Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.
        :param sync_config: The ``SyncConfig`` for a resolver attached to a versioned data source.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45a19b37f9f570b32d81c1e70bfcb51be048fdffa3df94ad801e69b812f746f8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResolverProps(
            api_id=api_id,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            code=code,
            code_s3_location=code_s3_location,
            data_source_name=data_source_name,
            kind=kind,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            request_mapping_template_s3_location=request_mapping_template_s3_location,
            response_mapping_template=response_mapping_template,
            response_mapping_template_s3_location=response_mapping_template_s3_location,
            runtime=runtime,
            sync_config=sync_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95aca731304382cdf3dcd502764afa9c3fa4887077a0e30a6874db561995ccfa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__313f8d86637162de96ee41aad99883afe32469196f904fb4309e0e9e33fc98ba)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrFieldName")
    def attr_field_name(self) -> builtins.str:
        '''The GraphQL field on a type that invokes the resolver.

        :cloudformationAttribute: FieldName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFieldName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrResolverArn")
    def attr_resolver_arn(self) -> builtins.str:
        '''ARN of the resolver, such as ``arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/types/typename/resolvers/resolvername`` .

        :cloudformationAttribute: ResolverArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTypeName")
    def attr_type_name(self) -> builtins.str:
        '''The GraphQL type that invokes this resolver.

        :cloudformationAttribute: TypeName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API to which you want to attach this resolver.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__472e69750f14de2abe38ed65522399a06e502ba89a0b921571c0b2746c638e5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="fieldName")
    def field_name(self) -> builtins.str:
        '''The GraphQL field on a type that invokes the resolver.'''
        return typing.cast(builtins.str, jsii.get(self, "fieldName"))

    @field_name.setter
    def field_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2233218403900cf6b8a69c999e792511fca483ed05d2fa4306e0d7b2535010)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldName", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        '''The GraphQL type that invokes this resolver.'''
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c08751b4795b139490b95abf3b3d0f17260bfea4a916f1afbaf08d435cfa21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="cachingConfig")
    def caching_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.CachingConfigProperty"]]:
        '''The caching configuration for the resolver.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.CachingConfigProperty"]], jsii.get(self, "cachingConfig"))

    @caching_config.setter
    def caching_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.CachingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6b9e8b849504be748695ce685546b844451460e25485772ca066bc2b65f61b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingConfig", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Optional[builtins.str]:
        '''The ``resolver`` code that contains the request and response functions.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "code"))

    @code.setter
    def code(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0dd83b21d0fde771732f3fdf63588b717c979c6ab095248970576c0a297e97d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="codeS3Location")
    def code_s3_location(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeS3Location"))

    @code_s3_location.setter
    def code_s3_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd67bb7c14d4f8040b88b7d1c29031ed6038b21c10f80e4f0fcfd6c31af45cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> typing.Optional[builtins.str]:
        '''The resolver data source name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceName"))

    @data_source_name.setter
    def data_source_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d90421590c8dc3a0c283260b096db2cd054cf3d6852e741d1bfaf1bf52bbe597)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> typing.Optional[builtins.str]:
        '''The resolver type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf560aa0e5a28a8ed71b1579e183bb6fb81cf53b398565d4fe06e8b7cfb4b31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchSize")
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchSize"))

    @max_batch_size.setter
    def max_batch_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66d0a40a93385979fce12d901f6a195637584cfcb71b3a04c20d8333f0a582bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchSize", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineConfig")
    def pipeline_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.PipelineConfigProperty"]]:
        '''Functions linked with the pipeline resolver.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.PipelineConfigProperty"]], jsii.get(self, "pipelineConfig"))

    @pipeline_config.setter
    def pipeline_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.PipelineConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c6c98074ee2ebbe5b451fe5513433aa3557366ed040722d6e61328ab781da16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineConfig", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The request mapping template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplate"))

    @request_mapping_template.setter
    def request_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd82effb0edb94da2492c911c5aecbe1fa5f2d88b6066513bb7f2a5713fdca7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a request mapping template in an Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplateS3Location"))

    @request_mapping_template_s3_location.setter
    def request_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd52da508686e9da63db3673bad91680eaa1eb468984c1b4f57757668dcaed40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The response mapping template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplate"))

    @response_mapping_template.setter
    def response_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f24f835e9a5b9af73089ccb61dfcf176cc230bb0feddf60b73360bab083e3f46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a response mapping template in an Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplateS3Location"))

    @response_mapping_template_s3_location.setter
    def response_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a067b0164755508220ca8ad5f24cbd5ac6d6c57fb44d8404b14392f12d372f0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.AppSyncRuntimeProperty"]]:
        '''Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.AppSyncRuntimeProperty"]], jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.AppSyncRuntimeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a14449468f6ed96319993479a0ae9b3feacd27ec17e068d4d17ce598a964715)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.SyncConfigProperty"]]:
        '''The ``SyncConfig`` for a resolver attached to a versioned data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.SyncConfigProperty"]], jsii.get(self, "syncConfig"))

    @sync_config.setter
    def sync_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.SyncConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a111110922e122a02d7d649fe2daaa4c4d7cf1709e2078b92fe101fd93d8e4f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.AppSyncRuntimeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "runtime_version": "runtimeVersion"},
    )
    class AppSyncRuntimeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            runtime_version: builtins.str,
        ) -> None:
            '''Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function.

            Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.

            :param name: The ``name`` of the runtime to use. Currently, the only allowed value is ``APPSYNC_JS`` .
            :param runtime_version: The ``version`` of the runtime to use. Currently, the only allowed version is ``1.0.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                app_sync_runtime_property = appsync.CfnResolver.AppSyncRuntimeProperty(
                    name="name",
                    runtime_version="runtimeVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d69cd55f1989ce956af7a1058706bfd4aaeba608d00146e50a90c1d3521cee0)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "runtime_version": runtime_version,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The ``name`` of the runtime to use.

            Currently, the only allowed value is ``APPSYNC_JS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html#cfn-appsync-resolver-appsyncruntime-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def runtime_version(self) -> builtins.str:
            '''The ``version`` of the runtime to use.

            Currently, the only allowed version is ``1.0.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html#cfn-appsync-resolver-appsyncruntime-runtimeversion
            '''
            result = self._values.get("runtime_version")
            assert result is not None, "Required property 'runtime_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppSyncRuntimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.CachingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"ttl": "ttl", "caching_keys": "cachingKeys"},
    )
    class CachingConfigProperty:
        def __init__(
            self,
            *,
            ttl: jsii.Number,
            caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The caching configuration for a resolver that has caching activated.

            :param ttl: The TTL in seconds for a resolver that has caching activated. Valid values are 1–3,600 seconds.
            :param caching_keys: The caching keys for a resolver that has caching activated. Valid values are entries from the ``$context.arguments`` , ``$context.source`` , and ``$context.identity`` maps.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                caching_config_property = appsync.CfnResolver.CachingConfigProperty(
                    ttl=123,
                
                    # the properties below are optional
                    caching_keys=["cachingKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5089c8cac20eb98ddb2d855ec469e09dc0f7b1141ddaf4de8fd19eaaadac7891)
                check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
                check_type(argname="argument caching_keys", value=caching_keys, expected_type=type_hints["caching_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ttl": ttl,
            }
            if caching_keys is not None:
                self._values["caching_keys"] = caching_keys

        @builtins.property
        def ttl(self) -> jsii.Number:
            '''The TTL in seconds for a resolver that has caching activated.

            Valid values are 1–3,600 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-ttl
            '''
            result = self._values.get("ttl")
            assert result is not None, "Required property 'ttl' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def caching_keys(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The caching keys for a resolver that has caching activated.

            Valid values are entries from the ``$context.arguments`` , ``$context.source`` , and ``$context.identity`` maps.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-cachingkeys
            '''
            result = self._values.get("caching_keys")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CachingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.LambdaConflictHandlerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
    )
    class LambdaConflictHandlerConfigProperty:
        def __init__(
            self,
            *,
            lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LambdaConflictHandlerConfig`` when configuring LAMBDA as the Conflict Handler.

            :param lambda_conflict_handler_arn: The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                lambda_conflict_handler_config_property = appsync.CfnResolver.LambdaConflictHandlerConfigProperty(
                    lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8760098edd4885448deb6a9ceb1ba3eb5367683995fadd12b5e5f3bf1e2fdd7e)
                check_type(argname="argument lambda_conflict_handler_arn", value=lambda_conflict_handler_arn, expected_type=type_hints["lambda_conflict_handler_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_conflict_handler_arn is not None:
                self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

        @builtins.property
        def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html#cfn-appsync-resolver-lambdaconflicthandlerconfig-lambdaconflicthandlerarn
            '''
            result = self._values.get("lambda_conflict_handler_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConflictHandlerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.PipelineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"functions": "functions"},
    )
    class PipelineConfigProperty:
        def __init__(
            self,
            *,
            functions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Use the ``PipelineConfig`` property type to specify ``PipelineConfig`` for an AWS AppSync resolver.

            ``PipelineConfig`` is a property of the `AWS::AppSync::Resolver <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html>`_ resource.

            :param functions: A list of ``Function`` objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                pipeline_config_property = appsync.CfnResolver.PipelineConfigProperty(
                    functions=["functions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2907a70554c3df66e94c41c4e36342a2860e214a5b7da358efbe204221066961)
                check_type(argname="argument functions", value=functions, expected_type=type_hints["functions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if functions is not None:
                self._values["functions"] = functions

        @builtins.property
        def functions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of ``Function`` objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html#cfn-appsync-resolver-pipelineconfig-functions
            '''
            result = self._values.get("functions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipelineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnResolver.SyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conflict_detection": "conflictDetection",
            "conflict_handler": "conflictHandler",
            "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
        },
    )
    class SyncConfigProperty:
        def __init__(
            self,
            *,
            conflict_detection: builtins.str,
            conflict_handler: typing.Optional[builtins.str] = None,
            lambda_conflict_handler_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResolver.LambdaConflictHandlerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a Sync configuration for a resolver.

            Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

            :param conflict_detection: The Conflict Detection strategy to use. - *VERSION* : Detect conflicts based on object versions for this resolver. - *NONE* : Do not detect conflicts when invoking this resolver.
            :param conflict_handler: The Conflict Resolution strategy to perform in the event of a conflict. - *OPTIMISTIC_CONCURRENCY* : Resolve conflicts by rejecting mutations when versions don't match the latest version at the server. - *AUTOMERGE* : Resolve conflicts with the Automerge conflict resolution strategy. - *LAMBDA* : Resolve conflicts with an AWS Lambda function supplied in the ``LambdaConflictHandlerConfig`` .
            :param lambda_conflict_handler_config: The ``LambdaConflictHandlerConfig`` when configuring ``LAMBDA`` as the Conflict Handler.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                sync_config_property = appsync.CfnResolver.SyncConfigProperty(
                    conflict_detection="conflictDetection",
                
                    # the properties below are optional
                    conflict_handler="conflictHandler",
                    lambda_conflict_handler_config=appsync.CfnResolver.LambdaConflictHandlerConfigProperty(
                        lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd8efb0c43d72e5061a7c9c3de6483787260ccff8a3dff5a5152ca959d6af6a3)
                check_type(argname="argument conflict_detection", value=conflict_detection, expected_type=type_hints["conflict_detection"])
                check_type(argname="argument conflict_handler", value=conflict_handler, expected_type=type_hints["conflict_handler"])
                check_type(argname="argument lambda_conflict_handler_config", value=lambda_conflict_handler_config, expected_type=type_hints["lambda_conflict_handler_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "conflict_detection": conflict_detection,
            }
            if conflict_handler is not None:
                self._values["conflict_handler"] = conflict_handler
            if lambda_conflict_handler_config is not None:
                self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

        @builtins.property
        def conflict_detection(self) -> builtins.str:
            '''The Conflict Detection strategy to use.

            - *VERSION* : Detect conflicts based on object versions for this resolver.
            - *NONE* : Do not detect conflicts when invoking this resolver.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflictdetection
            '''
            result = self._values.get("conflict_detection")
            assert result is not None, "Required property 'conflict_detection' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def conflict_handler(self) -> typing.Optional[builtins.str]:
            '''The Conflict Resolution strategy to perform in the event of a conflict.

            - *OPTIMISTIC_CONCURRENCY* : Resolve conflicts by rejecting mutations when versions don't match the latest version at the server.
            - *AUTOMERGE* : Resolve conflicts with the Automerge conflict resolution strategy.
            - *LAMBDA* : Resolve conflicts with an AWS Lambda function supplied in the ``LambdaConflictHandlerConfig`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflicthandler
            '''
            result = self._values.get("conflict_handler")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lambda_conflict_handler_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.LambdaConflictHandlerConfigProperty"]]:
            '''The ``LambdaConflictHandlerConfig`` when configuring ``LAMBDA`` as the Conflict Handler.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-lambdaconflicthandlerconfig
            '''
            result = self._values.get("lambda_conflict_handler_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResolver.LambdaConflictHandlerConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "code": "code",
        "code_s3_location": "codeS3Location",
        "data_source_name": "dataSourceName",
        "kind": "kind",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "request_mapping_template_s3_location": "requestMappingTemplateS3Location",
        "response_mapping_template": "responseMappingTemplate",
        "response_mapping_template_s3_location": "responseMappingTemplateS3Location",
        "runtime": "runtime",
        "sync_config": "syncConfig",
    },
)
class CfnResolverProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.CachingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        code: typing.Optional[builtins.str] = None,
        code_s3_location: typing.Optional[builtins.str] = None,
        data_source_name: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.PipelineConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResolver``.

        :param api_id: The AWS AppSync GraphQL API to which you want to attach this resolver.
        :param field_name: The GraphQL field on a type that invokes the resolver.
        :param type_name: The GraphQL type that invokes this resolver.
        :param caching_config: The caching configuration for the resolver.
        :param code: The ``resolver`` code that contains the request and response functions. When code is used, the ``runtime`` is required. The runtime value must be ``APPSYNC_JS`` .
        :param code_s3_location: The Amazon S3 endpoint.
        :param data_source_name: The resolver data source name.
        :param kind: The resolver type. - *UNIT* : A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source. - *PIPELINE* : A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of ``Function`` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.
        :param max_batch_size: The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.
        :param pipeline_config: Functions linked with the pipeline resolver.
        :param request_mapping_template: The request mapping template. Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.
        :param request_mapping_template_s3_location: The location of a request mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param response_mapping_template: The response mapping template.
        :param response_mapping_template_s3_location: The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.
        :param runtime: Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.
        :param sync_config: The ``SyncConfig`` for a resolver attached to a versioned data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_resolver_props = appsync.CfnResolverProps(
                api_id="apiId",
                field_name="fieldName",
                type_name="typeName",
            
                # the properties below are optional
                caching_config=appsync.CfnResolver.CachingConfigProperty(
                    ttl=123,
            
                    # the properties below are optional
                    caching_keys=["cachingKeys"]
                ),
                code="code",
                code_s3_location="codeS3Location",
                data_source_name="dataSourceName",
                kind="kind",
                max_batch_size=123,
                pipeline_config=appsync.CfnResolver.PipelineConfigProperty(
                    functions=["functions"]
                ),
                request_mapping_template="requestMappingTemplate",
                request_mapping_template_s3_location="requestMappingTemplateS3Location",
                response_mapping_template="responseMappingTemplate",
                response_mapping_template_s3_location="responseMappingTemplateS3Location",
                runtime=appsync.CfnResolver.AppSyncRuntimeProperty(
                    name="name",
                    runtime_version="runtimeVersion"
                ),
                sync_config=appsync.CfnResolver.SyncConfigProperty(
                    conflict_detection="conflictDetection",
            
                    # the properties below are optional
                    conflict_handler="conflictHandler",
                    lambda_conflict_handler_config=appsync.CfnResolver.LambdaConflictHandlerConfigProperty(
                        lambda_conflict_handler_arn="lambdaConflictHandlerArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b1ba8346de8783ad38f1a2377fd50bdd7577d903f4b68402c7b5ab604f16e5)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument code_s3_location", value=code_s3_location, expected_type=type_hints["code_s3_location"])
            check_type(argname="argument data_source_name", value=data_source_name, expected_type=type_hints["data_source_name"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument request_mapping_template_s3_location", value=request_mapping_template_s3_location, expected_type=type_hints["request_mapping_template_s3_location"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument response_mapping_template_s3_location", value=response_mapping_template_s3_location, expected_type=type_hints["response_mapping_template_s3_location"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument sync_config", value=sync_config, expected_type=type_hints["sync_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "field_name": field_name,
            "type_name": type_name,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if code is not None:
            self._values["code"] = code
        if code_s3_location is not None:
            self._values["code_s3_location"] = code_s3_location
        if data_source_name is not None:
            self._values["data_source_name"] = data_source_name
        if kind is not None:
            self._values["kind"] = kind
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if request_mapping_template_s3_location is not None:
            self._values["request_mapping_template_s3_location"] = request_mapping_template_s3_location
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if response_mapping_template_s3_location is not None:
            self._values["response_mapping_template_s3_location"] = response_mapping_template_s3_location
        if runtime is not None:
            self._values["runtime"] = runtime
        if sync_config is not None:
            self._values["sync_config"] = sync_config

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The AWS AppSync GraphQL API to which you want to attach this resolver.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_name(self) -> builtins.str:
        '''The GraphQL field on a type that invokes the resolver.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-fieldname
        '''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''The GraphQL type that invokes this resolver.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-typename
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.CachingConfigProperty]]:
        '''The caching configuration for the resolver.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-cachingconfig
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.CachingConfigProperty]], result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''The ``resolver`` code that contains the request and response functions.

        When code is used, the ``runtime`` is required. The runtime value must be ``APPSYNC_JS`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-code
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_s3_location(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-codes3location
        '''
        result = self._values.get("code_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_name(self) -> typing.Optional[builtins.str]:
        '''The resolver data source name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-datasourcename
        '''
        result = self._values.get("data_source_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The resolver type.

        - *UNIT* : A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.
        - *PIPELINE* : A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of ``Function`` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a ``BatchInvoke`` operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-maxbatchsize
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.PipelineConfigProperty]]:
        '''Functions linked with the pipeline resolver.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-pipelineconfig
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.PipelineConfigProperty]], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The request mapping template.

        Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplate
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a request mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplates3location
        '''
        result = self._values.get("request_mapping_template_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''The response mapping template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplate
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of a response mapping template in an Amazon S3 bucket.

        Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplates3location
        '''
        result = self._values.get("response_mapping_template_s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.AppSyncRuntimeProperty]]:
        '''Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function.

        Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-runtime
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.AppSyncRuntimeProperty]], result)

    @builtins.property
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.SyncConfigProperty]]:
        '''The ``SyncConfig`` for a resolver attached to a versioned data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-syncconfig
        '''
        result = self._values.get("sync_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.SyncConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSourceApiAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.CfnSourceApiAssociation",
):
    '''Describes the configuration of a source API.

    A source API is a GraphQL API that is linked to a merged API. There can be multiple source APIs attached to each merged API. When linked to a merged API, the source API's schema, data sources, and resolvers will be combined with other linked source API data to form a new, singular API. Source APIs can originate from your account or from other accounts via Resource Access Manager.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        cfn_source_api_association = appsync.CfnSourceApiAssociation(self, "MyCfnSourceApiAssociation",
            description="description",
            merged_api_identifier="mergedApiIdentifier",
            source_api_association_config=appsync.CfnSourceApiAssociation.SourceApiAssociationConfigProperty(
                merge_type="mergeType"
            ),
            source_api_identifier="sourceApiIdentifier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        merged_api_identifier: typing.Optional[builtins.str] = None,
        source_api_association_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSourceApiAssociation.SourceApiAssociationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_api_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: The description field of the association configuration.
        :param merged_api_identifier: The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.
        :param source_api_association_config: The ``SourceApiAssociationConfig`` object data.
        :param source_api_identifier: The identifier of the AppSync Source API. This is generated by the AppSync service. In most cases, source APIs (especially in your account) only require the API ID value or ARN of the source API. However, source APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the source API.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a3927d7055c6f07f6fda98012e654caed4acd1cc6ba02f45817c51587aaea2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSourceApiAssociationProps(
            description=description,
            merged_api_identifier=merged_api_identifier,
            source_api_association_config=source_api_association_config,
            source_api_identifier=source_api_identifier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8118984adcd2c3e9c43587a073297de4bd1e174d46854dc5e69d06013b9c2c97)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3e97069634a5275cdcce711a054061c3991a3588f8b476f3a6c300a0062016c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationArn")
    def attr_association_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the source API association.

        :cloudformationAttribute: AssociationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> builtins.str:
        '''The ID generated by the AppSync service for the source API association.

        :cloudformationAttribute: AssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastSuccessfulMergeDate")
    def attr_last_successful_merge_date(self) -> builtins.str:
        '''The datetime value of the last successful merge of the source API association.

        The result will be in UTC format and your local time zone.

        :cloudformationAttribute: LastSuccessfulMergeDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastSuccessfulMergeDate"))

    @builtins.property
    @jsii.member(jsii_name="attrMergedApiArn")
    def attr_merged_api_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the merged API.

        :cloudformationAttribute: MergedApiArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMergedApiArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMergedApiId")
    def attr_merged_api_id(self) -> builtins.str:
        '''The ID of the merged API.

        :cloudformationAttribute: MergedApiId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMergedApiId"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceApiArn")
    def attr_source_api_arn(self) -> builtins.str:
        '''The source API's Amazon Resource Name (ARN) value.

        :cloudformationAttribute: SourceApiArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceApiArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceApiAssociationStatus")
    def attr_source_api_association_status(self) -> builtins.str:
        '''The state of the source API association.

        The following values are valid:

        ``MERGE_SCHEDULED | MERGE_FAILED | MERGE_SUCCESS | MERGE_IN_PROGRESS | AUTO_MERGE_SCHEDULE_FAILED | DELETION_SCHEDULED | DELETION_IN_PROGRESS | DELETION_FAILED``

        :cloudformationAttribute: SourceApiAssociationStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceApiAssociationStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceApiAssociationStatusDetail")
    def attr_source_api_association_status_detail(self) -> builtins.str:
        '''The message describing the state of the source API association.

        :cloudformationAttribute: SourceApiAssociationStatusDetail
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceApiAssociationStatusDetail"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceApiId")
    def attr_source_api_id(self) -> builtins.str:
        '''The ID of the source API.

        :cloudformationAttribute: SourceApiId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceApiId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description field of the association configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c33f6c1609e5ea2fea0dc3149db2bb427e4e90e05aebc176b6f270f52a7f880c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="mergedApiIdentifier")
    def merged_api_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AppSync Merged API.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergedApiIdentifier"))

    @merged_api_identifier.setter
    def merged_api_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37d248fdd83c372d8504ccedc8ceeff98fd9085da37f45ffdc582051a1c82aab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergedApiIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="sourceApiAssociationConfig")
    def source_api_association_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSourceApiAssociation.SourceApiAssociationConfigProperty"]]:
        '''The ``SourceApiAssociationConfig`` object data.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSourceApiAssociation.SourceApiAssociationConfigProperty"]], jsii.get(self, "sourceApiAssociationConfig"))

    @source_api_association_config.setter
    def source_api_association_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSourceApiAssociation.SourceApiAssociationConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a343d8ede31db66fa4c54360086ddf77c88c05a902c3cdd250198db59eb0ee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceApiAssociationConfig", value)

    @builtins.property
    @jsii.member(jsii_name="sourceApiIdentifier")
    def source_api_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AppSync Source API.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceApiIdentifier"))

    @source_api_identifier.setter
    def source_api_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce9bcd8d95a3bc0ef84a2eb38f1500af0d6743e3f33026a5037a1af930c33d30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceApiIdentifier", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appsync.CfnSourceApiAssociation.SourceApiAssociationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"merge_type": "mergeType"},
    )
    class SourceApiAssociationConfigProperty:
        def __init__(self, *, merge_type: typing.Optional[builtins.str] = None) -> None:
            '''Describes properties used to specify configurations related to a source API.

            This is a property of the ``AWS:AppSync:SourceApiAssociation`` type.

            :param merge_type: The property that indicates which merging option is enabled in the source API association. Valid merge types are ``MANUAL_MERGE`` (default) and ``AUTO_MERGE`` . Manual merges are the default behavior and require the user to trigger any changes from the source APIs to the merged API manually. Auto merges subscribe the merged API to the changes performed on the source APIs so that any change in the source APIs are also made to the merged API. Auto merges use ``MergedApiExecutionRoleArn`` to perform merge operations. The following values are valid: ``MANUAL_MERGE | AUTO_MERGE``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-sourceapiassociation-sourceapiassociationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appsync as appsync
                
                source_api_association_config_property = appsync.CfnSourceApiAssociation.SourceApiAssociationConfigProperty(
                    merge_type="mergeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__62f3cd07f6e7086711e43c45ec65e051608b1d33e97dcfb24df40b8772736964)
                check_type(argname="argument merge_type", value=merge_type, expected_type=type_hints["merge_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if merge_type is not None:
                self._values["merge_type"] = merge_type

        @builtins.property
        def merge_type(self) -> typing.Optional[builtins.str]:
            '''The property that indicates which merging option is enabled in the source API association.

            Valid merge types are ``MANUAL_MERGE`` (default) and ``AUTO_MERGE`` . Manual merges are the default behavior and require the user to trigger any changes from the source APIs to the merged API manually. Auto merges subscribe the merged API to the changes performed on the source APIs so that any change in the source APIs are also made to the merged API. Auto merges use ``MergedApiExecutionRoleArn`` to perform merge operations.

            The following values are valid:

            ``MANUAL_MERGE | AUTO_MERGE``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-sourceapiassociation-sourceapiassociationconfig.html#cfn-appsync-sourceapiassociation-sourceapiassociationconfig-mergetype
            '''
            result = self._values.get("merge_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceApiAssociationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CfnSourceApiAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "merged_api_identifier": "mergedApiIdentifier",
        "source_api_association_config": "sourceApiAssociationConfig",
        "source_api_identifier": "sourceApiIdentifier",
    },
)
class CfnSourceApiAssociationProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        merged_api_identifier: typing.Optional[builtins.str] = None,
        source_api_association_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSourceApiAssociation.SourceApiAssociationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        source_api_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSourceApiAssociation``.

        :param description: The description field of the association configuration.
        :param merged_api_identifier: The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.
        :param source_api_association_config: The ``SourceApiAssociationConfig`` object data.
        :param source_api_identifier: The identifier of the AppSync Source API. This is generated by the AppSync service. In most cases, source APIs (especially in your account) only require the API ID value or ARN of the source API. However, source APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the source API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            cfn_source_api_association_props = appsync.CfnSourceApiAssociationProps(
                description="description",
                merged_api_identifier="mergedApiIdentifier",
                source_api_association_config=appsync.CfnSourceApiAssociation.SourceApiAssociationConfigProperty(
                    merge_type="mergeType"
                ),
                source_api_identifier="sourceApiIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c56eff105c0c6b1b0bd618bef1559d9327ee250f666604ae39798783d3370a3a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument merged_api_identifier", value=merged_api_identifier, expected_type=type_hints["merged_api_identifier"])
            check_type(argname="argument source_api_association_config", value=source_api_association_config, expected_type=type_hints["source_api_association_config"])
            check_type(argname="argument source_api_identifier", value=source_api_identifier, expected_type=type_hints["source_api_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if merged_api_identifier is not None:
            self._values["merged_api_identifier"] = merged_api_identifier
        if source_api_association_config is not None:
            self._values["source_api_association_config"] = source_api_association_config
        if source_api_identifier is not None:
            self._values["source_api_identifier"] = source_api_identifier

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description field of the association configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html#cfn-appsync-sourceapiassociation-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merged_api_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AppSync Merged API.

        This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html#cfn-appsync-sourceapiassociation-mergedapiidentifier
        '''
        result = self._values.get("merged_api_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_api_association_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSourceApiAssociation.SourceApiAssociationConfigProperty]]:
        '''The ``SourceApiAssociationConfig`` object data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html#cfn-appsync-sourceapiassociation-sourceapiassociationconfig
        '''
        result = self._values.get("source_api_association_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSourceApiAssociation.SourceApiAssociationConfigProperty]], result)

    @builtins.property
    def source_api_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AppSync Source API.

        This is generated by the AppSync service. In most cases, source APIs (especially in your account) only require the API ID value or ARN of the source API. However, source APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the source API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html#cfn-appsync-sourceapiassociation-sourceapiidentifier
        '''
        result = self._values.get("source_api_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSourceApiAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Code(metaclass=jsii.JSIIAbstractClass, jsii_type="aws-cdk-lib.aws_appsync.Code"):
    '''Represents source code for an AppSync Function or Resolver.

    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        
        
        my_js_function = appsync.AppsyncFunction(self, "function",
            name="my_js_function",
            api=api,
            data_source=api.add_none_data_source("none"),
            code=appsync.Code.from_asset("directory/function_code.js"),
            runtime=appsync.FunctionRuntime.JS_1_0_0
        )
        
        appsync.Resolver(self, "PipelineResolver",
            api=api,
            type_name="typeName",
            field_name="fieldName",
            code=appsync.Code.from_inline("""
                    // The before step
                    export function request(...args) {
                      console.log(args);
                      return {}
                    }
        
                    // The after step
                    export function response(ctx) {
                      return ctx.prev.result
                    }
                  """),
            runtime=appsync.FunctionRuntime.JS_1_0_0,
            pipeline_config=[my_js_function]
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    ) -> "AssetCode":
        '''Loads the function code from a local disk path.

        :param path: The path to the source code file.
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eafa9f4fd31cdfcc23e497d115c1733ce980674eb036dad379eb9102290ec01)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = _AssetOptions_2aa69621(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("AssetCode", jsii.sinvoke(cls, "fromAsset", [path, options]))

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(cls, code: builtins.str) -> "InlineCode":
        '''Inline code for AppSync function.

        :param code: The actual handler code (limited to 4KiB).

        :return: ``InlineCode`` with inline code.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d01668387a22003f3b94de6761b2ee76842b637cecef060a14da2befa820605d)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
        return typing.cast("InlineCode", jsii.sinvoke(cls, "fromInline", [code]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "CodeConfig":
        '''Bind source code to an AppSync Function or resolver.

        :param scope: -
        '''
        ...


class _CodeProxy(Code):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "CodeConfig":
        '''Bind source code to an AppSync Function or resolver.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999382669090951c71805838301c048a01730773d994c4fbcc12cee3d8666cf6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("CodeConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Code).__jsii_proxy_class__ = lambda : _CodeProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.CodeConfig",
    jsii_struct_bases=[],
    name_mapping={"inline_code": "inlineCode", "s3_location": "s3Location"},
)
class CodeConfig:
    def __init__(
        self,
        *,
        inline_code: typing.Optional[builtins.str] = None,
        s3_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Result of binding ``Code`` into a ``Function``.

        :param inline_code: Inline code (mutually exclusive with ``s3Location``). Default: - code is not inline code
        :param s3_location: The location of the code in S3 (mutually exclusive with ``inlineCode``. Default: - code is not an s3 location

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            code_config = appsync.CodeConfig(
                inline_code="inlineCode",
                s3_location="s3Location"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5abf436f692efcaed424f8bc2738e56e16abc84b9ca36c4963add4e94cf6449)
            check_type(argname="argument inline_code", value=inline_code, expected_type=type_hints["inline_code"])
            check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if inline_code is not None:
            self._values["inline_code"] = inline_code
        if s3_location is not None:
            self._values["s3_location"] = s3_location

    @builtins.property
    def inline_code(self) -> typing.Optional[builtins.str]:
        '''Inline code (mutually exclusive with ``s3Location``).

        :default: - code is not inline code
        '''
        result = self._values.get("inline_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_location(self) -> typing.Optional[builtins.str]:
        '''The location of the code in S3 (mutually exclusive with ``inlineCode``.

        :default: - code is not an s3 location
        '''
        result = self._values.get("s3_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.DataSourceOptions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "name": "name"},
)
class DataSourceOptions:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Optional configuration for data sources.

        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            data_source_options = appsync.DataSourceOptions(
                description="description",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__931a67471fe69ef52bd3bdb1d3123eda90d2919ed8b825ab147e1db8ee9b4607)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source, overrides the id given by cdk.

        :default: - generated by cdk given the id
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.DomainOptions",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "domain_name": "domainName"},
)
class DomainOptions:
    def __init__(
        self,
        *,
        certificate: _ICertificate_c194c70b,
        domain_name: builtins.str,
    ) -> None:
        '''Domain name configuration for AppSync.

        :param certificate: The certificate to use with the domain name.
        :param domain_name: The actual domain name. For example, ``api.example.com``.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_certificatemanager as acm
            import aws_cdk.aws_route53 as route53
            
            # hosted zone and route53 features
            # hosted_zone_id: str
            zone_name = "example.com"
            
            
            my_domain_name = "api.example.com"
            certificate = acm.Certificate(self, "cert", domain_name=my_domain_name)
            schema = appsync.SchemaFile(file_path="mySchemaFile")
            api = appsync.GraphqlApi(self, "api",
                name="myApi",
                schema=schema,
                domain_name=appsync.DomainOptions(
                    certificate=certificate,
                    domain_name=my_domain_name
                )
            )
            
            # hosted zone for adding appsync domain
            zone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
                hosted_zone_id=hosted_zone_id,
                zone_name=zone_name
            )
            
            # create a cname to the appsync domain. will map to something like xxxx.cloudfront.net
            route53.CnameRecord(self, "CnameApiRecord",
                record_name="api",
                zone=zone,
                domain_name=api.app_sync_domain_name
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__666cedee7b74b7e32381dd1603bff8d92b24dd381d5f493f478126fb394ef687)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "domain_name": domain_name,
        }

    @builtins.property
    def certificate(self) -> _ICertificate_c194c70b:
        '''The certificate to use with the domain name.'''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(_ICertificate_c194c70b, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The actual domain name.

        For example, ``api.example.com``.
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.ExtendedDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "dynamo_db_config": "dynamoDbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "event_bridge_config": "eventBridgeConfig",
        "http_config": "httpConfig",
        "lambda_config": "lambdaConfig",
        "open_search_service_config": "openSearchServiceConfig",
        "relational_database_config": "relationalDatabaseConfig",
    },
)
class ExtendedDataSourceProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.EventBridgeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''props used by implementations of BaseDataSource to provide configuration.

        Should not be used directly.

        :param type: the type of the AppSync datasource.
        :param dynamo_db_config: configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (deprecated) configuration for Elasticsearch data source. Default: - No config
        :param event_bridge_config: configuration for EventBridge Datasource. Default: - No config
        :param http_config: configuration for HTTP Datasource. Default: - No config
        :param lambda_config: configuration for Lambda Datasource. Default: - No config
        :param open_search_service_config: configuration for OpenSearch data source. Default: - No config
        :param relational_database_config: configuration for RDS Datasource. Default: - No config

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            extended_data_source_props = appsync.ExtendedDataSourceProps(
                type="type",
            
                # the properties below are optional
                dynamo_db_config=appsync.CfnDataSource.DynamoDBConfigProperty(
                    aws_region="awsRegion",
                    table_name="tableName",
            
                    # the properties below are optional
                    delta_sync_config=appsync.CfnDataSource.DeltaSyncConfigProperty(
                        base_table_ttl="baseTableTtl",
                        delta_sync_table_name="deltaSyncTableName",
                        delta_sync_table_ttl="deltaSyncTableTtl"
                    ),
                    use_caller_credentials=False,
                    versioned=False
                ),
                elasticsearch_config=appsync.CfnDataSource.ElasticsearchConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                ),
                event_bridge_config=appsync.CfnDataSource.EventBridgeConfigProperty(
                    event_bus_arn="eventBusArn"
                ),
                http_config=appsync.CfnDataSource.HttpConfigProperty(
                    endpoint="endpoint",
            
                    # the properties below are optional
                    authorization_config=appsync.CfnDataSource.AuthorizationConfigProperty(
                        authorization_type="authorizationType",
            
                        # the properties below are optional
                        aws_iam_config=appsync.CfnDataSource.AwsIamConfigProperty(
                            signing_region="signingRegion",
                            signing_service_name="signingServiceName"
                        )
                    )
                ),
                lambda_config=appsync.CfnDataSource.LambdaConfigProperty(
                    lambda_function_arn="lambdaFunctionArn"
                ),
                open_search_service_config=appsync.CfnDataSource.OpenSearchServiceConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                ),
                relational_database_config=appsync.CfnDataSource.RelationalDatabaseConfigProperty(
                    relational_database_source_type="relationalDatabaseSourceType",
            
                    # the properties below are optional
                    rds_http_endpoint_config=appsync.CfnDataSource.RdsHttpEndpointConfigProperty(
                        aws_region="awsRegion",
                        aws_secret_store_arn="awsSecretStoreArn",
                        db_cluster_identifier="dbClusterIdentifier",
            
                        # the properties below are optional
                        database_name="databaseName",
                        schema="schema"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea6d91c7460c0aa163c28990cc189d68d54dd762bf2b0c703c347e80a74f98a)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument dynamo_db_config", value=dynamo_db_config, expected_type=type_hints["dynamo_db_config"])
            check_type(argname="argument elasticsearch_config", value=elasticsearch_config, expected_type=type_hints["elasticsearch_config"])
            check_type(argname="argument event_bridge_config", value=event_bridge_config, expected_type=type_hints["event_bridge_config"])
            check_type(argname="argument http_config", value=http_config, expected_type=type_hints["http_config"])
            check_type(argname="argument lambda_config", value=lambda_config, expected_type=type_hints["lambda_config"])
            check_type(argname="argument open_search_service_config", value=open_search_service_config, expected_type=type_hints["open_search_service_config"])
            check_type(argname="argument relational_database_config", value=relational_database_config, expected_type=type_hints["relational_database_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if dynamo_db_config is not None:
            self._values["dynamo_db_config"] = dynamo_db_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if event_bridge_config is not None:
            self._values["event_bridge_config"] = event_bridge_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if open_search_service_config is not None:
            self._values["open_search_service_config"] = open_search_service_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config

    @builtins.property
    def type(self) -> builtins.str:
        '''the type of the AppSync datasource.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DynamoDBConfigProperty]]:
        '''configuration for DynamoDB Datasource.

        :default: - No config
        '''
        result = self._values.get("dynamo_db_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DynamoDBConfigProperty]], result)

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ElasticsearchConfigProperty]]:
        '''(deprecated) configuration for Elasticsearch data source.

        :default: - No config

        :deprecated: - use ``openSearchConfig``

        :stability: deprecated
        '''
        result = self._values.get("elasticsearch_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ElasticsearchConfigProperty]], result)

    @builtins.property
    def event_bridge_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.EventBridgeConfigProperty]]:
        '''configuration for EventBridge Datasource.

        :default: - No config
        '''
        result = self._values.get("event_bridge_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.EventBridgeConfigProperty]], result)

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.HttpConfigProperty]]:
        '''configuration for HTTP Datasource.

        :default: - No config
        '''
        result = self._values.get("http_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.HttpConfigProperty]], result)

    @builtins.property
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.LambdaConfigProperty]]:
        '''configuration for Lambda Datasource.

        :default: - No config
        '''
        result = self._values.get("lambda_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.LambdaConfigProperty]], result)

    @builtins.property
    def open_search_service_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.OpenSearchServiceConfigProperty]]:
        '''configuration for OpenSearch data source.

        :default: - No config
        '''
        result = self._values.get("open_search_service_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.OpenSearchServiceConfigProperty]], result)

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RelationalDatabaseConfigProperty]]:
        '''configuration for RDS Datasource.

        :default: - No config
        '''
        result = self._values.get("relational_database_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RelationalDatabaseConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtendedDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.ExtendedResolverProps",
    jsii_struct_bases=[BaseResolverProps],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "code": "code",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "runtime": "runtime",
        "data_source": "dataSource",
    },
)
class ExtendedResolverProps(BaseResolverProps):
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[Code] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        runtime: typing.Optional["FunctionRuntime"] = None,
        data_source: typing.Optional[BaseDataSource] = None,
    ) -> None:
        '''Additional property for an AppSync resolver for data source reference.

        :param field_name: name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param caching_config: The caching configuration for this resolver. Default: - No caching configuration
        :param code: The function code. Default: - no code is used
        :param max_batch_size: The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        :param data_source: The data source this resolver is using. Default: - No datasource

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_appsync as appsync
            
            # appsync_function: appsync.AppsyncFunction
            # base_data_source: appsync.BaseDataSource
            # code: appsync.Code
            # function_runtime: appsync.FunctionRuntime
            # mapping_template: appsync.MappingTemplate
            
            extended_resolver_props = appsync.ExtendedResolverProps(
                field_name="fieldName",
                type_name="typeName",
            
                # the properties below are optional
                caching_config=appsync.CachingConfig(
                    ttl=cdk.Duration.minutes(30),
            
                    # the properties below are optional
                    caching_keys=["cachingKeys"]
                ),
                code=code,
                data_source=base_data_source,
                max_batch_size=123,
                pipeline_config=[appsync_function],
                request_mapping_template=mapping_template,
                response_mapping_template=mapping_template,
                runtime=function_runtime
            )
        '''
        if isinstance(caching_config, dict):
            caching_config = CachingConfig(**caching_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dc3b87bcc5a5c4f72f5701decf293d0da2caba80281cf58c26e7a4d9ed20fd7)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if code is not None:
            self._values["code"] = code
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if runtime is not None:
            self._values["runtime"] = runtime
        if data_source is not None:
            self._values["data_source"] = data_source

    @builtins.property
    def field_name(self) -> builtins.str:
        '''name of the GraphQL field in the given type this resolver is attached to.'''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''name of the GraphQL type this resolver is attached to.'''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(self) -> typing.Optional[CachingConfig]:
        '''The caching configuration for this resolver.

        :default: - No caching configuration
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional[CachingConfig], result)

    @builtins.property
    def code(self) -> typing.Optional[Code]:
        '''The function code.

        :default: - no code is used
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[Code], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of elements per batch, when using batch invoke.

        :default: - No max batch size
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List["IAppsyncFunction"]]:
        '''configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional[typing.List["IAppsyncFunction"]], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''The request mapping template for this resolver.

        :default: - No mapping template
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''The response mapping template for this resolver.

        :default: - No mapping template
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def runtime(self) -> typing.Optional["FunctionRuntime"]:
        '''The functions runtime.

        :default: - no function runtime, VTL mapping templates used
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional["FunctionRuntime"], result)

    @builtins.property
    def data_source(self) -> typing.Optional[BaseDataSource]:
        '''The data source this resolver is using.

        :default: - No datasource
        '''
        result = self._values.get("data_source")
        return typing.cast(typing.Optional[BaseDataSource], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtendedResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_appsync.FieldLogLevel")
class FieldLogLevel(enum.Enum):
    '''log-level for fields in AppSync.'''

    NONE = "NONE"
    '''No logging.'''
    ERROR = "ERROR"
    '''Error logging.'''
    ALL = "ALL"
    '''All logging.'''


class FunctionRuntime(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.FunctionRuntime",
):
    '''Utility class for specifying specific appsync runtime versions.

    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        
        
        my_js_function = appsync.AppsyncFunction(self, "function",
            name="my_js_function",
            api=api,
            data_source=api.add_none_data_source("none"),
            code=appsync.Code.from_asset("directory/function_code.js"),
            runtime=appsync.FunctionRuntime.JS_1_0_0
        )
        
        appsync.Resolver(self, "PipelineResolver",
            api=api,
            type_name="typeName",
            field_name="fieldName",
            code=appsync.Code.from_inline("""
                    // The before step
                    export function request(...args) {
                      console.log(args);
                      return {}
                    }
        
                    // The after step
                    export function response(ctx) {
                      return ctx.prev.result
                    }
                  """),
            runtime=appsync.FunctionRuntime.JS_1_0_0,
            pipeline_config=[my_js_function]
        )
    '''

    def __init__(self, family: "FunctionRuntimeFamily", version: builtins.str) -> None:
        '''
        :param family: -
        :param version: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89b62634a47ff9294fb4979bf7d3b55dfb2f791b9cad75a7193946ff54e2953c)
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        jsii.create(self.__class__, self, [family, version])

    @jsii.member(jsii_name="toProperties")
    def to_properties(self) -> "RuntimeConfig":
        '''Convert to Cfn runtime configuration property format.'''
        return typing.cast("RuntimeConfig", jsii.invoke(self, "toProperties", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="JS_1_0_0")
    def JS_1_0_0(cls) -> "FunctionRuntime":
        '''APPSYNC_JS v1.0.0 runtime.'''
        return typing.cast("FunctionRuntime", jsii.sget(cls, "JS_1_0_0"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the runtime.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The runtime version.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_appsync.FunctionRuntimeFamily")
class FunctionRuntimeFamily(enum.Enum):
    '''Appsync supported runtimes.

    Only JavaScript as of now
    '''

    JS = "JS"
    '''AppSync JavaScript runtime.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.GraphqlApiAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "graphql_api_id": "graphqlApiId",
        "graphql_api_arn": "graphqlApiArn",
    },
)
class GraphqlApiAttributes:
    def __init__(
        self,
        *,
        graphql_api_id: builtins.str,
        graphql_api_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Attributes for GraphQL imports.

        :param graphql_api_id: an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.
        :param graphql_api_arn: the arn for the GraphQL Api. Default: - autogenerated arn

        :exampleMetadata: infused

        Example::

            # api: appsync.GraphqlApi
            # table: dynamodb.Table
            
            imported_api = appsync.GraphqlApi.from_graphql_api_attributes(self, "IApi",
                graphql_api_id=api.api_id,
                graphql_api_arn=api.arn
            )
            imported_api.add_dynamo_db_data_source("TableDataSource", table)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1fc91e210b45240155885dae82dd53ddc084048aae2724cd942ec7c5202c10)
            check_type(argname="argument graphql_api_id", value=graphql_api_id, expected_type=type_hints["graphql_api_id"])
            check_type(argname="argument graphql_api_arn", value=graphql_api_arn, expected_type=type_hints["graphql_api_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graphql_api_id": graphql_api_id,
        }
        if graphql_api_arn is not None:
            self._values["graphql_api_arn"] = graphql_api_arn

    @builtins.property
    def graphql_api_id(self) -> builtins.str:
        '''an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.'''
        result = self._values.get("graphql_api_id")
        assert result is not None, "Required property 'graphql_api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def graphql_api_arn(self) -> typing.Optional[builtins.str]:
        '''the arn for the GraphQL Api.

        :default: - autogenerated arn
        '''
        result = self._values.get("graphql_api_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphqlApiAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.GraphqlApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schema": "schema",
        "authorization_config": "authorizationConfig",
        "domain_name": "domainName",
        "log_config": "logConfig",
        "visibility": "visibility",
        "xray_enabled": "xrayEnabled",
    },
)
class GraphqlApiProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        schema: "ISchema",
        authorization_config: typing.Optional[typing.Union[AuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_name: typing.Optional[typing.Union[DomainOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        log_config: typing.Optional[typing.Union["LogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        visibility: typing.Optional["Visibility"] = None,
        xray_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for an AppSync GraphQL API.

        :param name: the name of the GraphQL API.
        :param schema: GraphQL schema definition. Specify how you want to define your schema. SchemaFile.fromAsset(filePath: string) allows schema definition through schema.graphql file Default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)
        :param authorization_config: Optional authorization configuration. Default: - API Key authorization
        :param domain_name: The domain name configuration for the GraphQL API. The Route 53 hosted zone and CName DNS record must be configured in addition to this setting to enable custom domain URL Default: - no domain name
        :param log_config: Logging configuration for this api. Default: - None
        :param visibility: A value indicating whether the API is accessible from anywhere (GLOBAL) or can only be access from a VPC (PRIVATE). Default: - GLOBAL
        :param xray_enabled: A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API. Default: - false

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_events as events
            
            
            api = appsync.GraphqlApi(self, "EventBridgeApi",
                name="EventBridgeApi",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.eventbridge.graphql"))
            )
            
            bus = events.EventBus(self, "DestinationEventBus")
            
            data_source = api.add_event_bridge_data_source("NoneDS", bus)
            
            data_source.create_resolver("EventResolver",
                type_name="Mutation",
                field_name="emitEvent",
                request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
                response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
            )
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AuthorizationConfig(**authorization_config)
        if isinstance(domain_name, dict):
            domain_name = DomainOptions(**domain_name)
        if isinstance(log_config, dict):
            log_config = LogConfig(**log_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ac2113ba86b3a60344e56ee0c5bb6cdf1bc20cd0d5aa52f9a94709feb99e1b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
            check_type(argname="argument xray_enabled", value=xray_enabled, expected_type=type_hints["xray_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "schema": schema,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if log_config is not None:
            self._values["log_config"] = log_config
        if visibility is not None:
            self._values["visibility"] = visibility
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

    @builtins.property
    def name(self) -> builtins.str:
        '''the name of the GraphQL API.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> "ISchema":
        '''GraphQL schema definition. Specify how you want to define your schema.

        SchemaFile.fromAsset(filePath: string) allows schema definition through schema.graphql file

        :default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast("ISchema", result)

    @builtins.property
    def authorization_config(self) -> typing.Optional[AuthorizationConfig]:
        '''Optional authorization configuration.

        :default: - API Key authorization
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional[AuthorizationConfig], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[DomainOptions]:
        '''The domain name configuration for the GraphQL API.

        The Route 53 hosted zone and CName DNS record must be configured in addition to this setting to
        enable custom domain URL

        :default: - no domain name
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[DomainOptions], result)

    @builtins.property
    def log_config(self) -> typing.Optional["LogConfig"]:
        '''Logging configuration for this api.

        :default: - None
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional["LogConfig"], result)

    @builtins.property
    def visibility(self) -> typing.Optional["Visibility"]:
        '''A value indicating whether the API is accessible from anywhere (GLOBAL) or can only be access from a VPC (PRIVATE).

        :default: - GLOBAL
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional["Visibility"], result)

    @builtins.property
    def xray_enabled(self) -> typing.Optional[builtins.bool]:
        '''A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API.

        :default: - false
        '''
        result = self._values.get("xray_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphqlApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.HttpDataSourceOptions",
    jsii_struct_bases=[DataSourceOptions],
    name_mapping={
        "description": "description",
        "name": "name",
        "authorization_config": "authorizationConfig",
    },
)
class HttpDataSourceOptions(DataSourceOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Optional configuration for Http data sources.

        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        :param authorization_config: The authorization config in case the HTTP endpoint requires authorization. Default: - none

        :exampleMetadata: infused

        Example::

            api = appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
            )
            
            http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
                name="httpDsWithStepF",
                description="from appsync to StepFunctions Workflow",
                authorization_config=appsync.AwsIamConfig(
                    signing_region="us-east-1",
                    signing_service_name="states"
                )
            )
            
            http_ds.create_resolver("MutationCallStepFunctionResolver",
                type_name="Mutation",
                field_name="callStepFunction",
                request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
                response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
            )
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AwsIamConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__892de8c32b5ee5c6cb5e65bc4b597f67297f1f675b608821b733eb9599975405)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source, overrides the id given by cdk.

        :default: - generated by cdk given the id
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorization_config(self) -> typing.Optional[AwsIamConfig]:
        '''The authorization config in case the HTTP endpoint requires authorization.

        :default: - none
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional[AwsIamConfig], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpDataSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.HttpDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "endpoint": "endpoint",
        "authorization_config": "authorizationConfig",
    },
)
class HttpDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: "IGraphqlApi",
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for an AppSync http datasource.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        :param endpoint: The http endpoint.
        :param authorization_config: The authorization config in case the HTTP endpoint requires authorization. Default: - none

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            # graphql_api: appsync.GraphqlApi
            
            http_data_source_props = appsync.HttpDataSourceProps(
                api=graphql_api,
                endpoint="endpoint",
            
                # the properties below are optional
                authorization_config=appsync.AwsIamConfig(
                    signing_region="signingRegion",
                    signing_service_name="signingServiceName"
                ),
                description="description",
                name="name"
            )
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AwsIamConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91183bd6fd5a10b6ae91fe2450b1ca1b99e291ac5b272e3c6ccfffaa26a2b05a)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "endpoint": endpoint,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def api(self) -> "IGraphqlApi":
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast("IGraphqlApi", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The http endpoint.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_config(self) -> typing.Optional[AwsIamConfig]:
        '''The authorization config in case the HTTP endpoint requires authorization.

        :default: - none
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional[AwsIamConfig], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_appsync.IAppsyncFunction")
class IAppsyncFunction(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface for AppSync Functions.'''

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        '''the ARN of the AppSync function.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        '''the name of this AppSync Function.

        :attribute: true
        '''
        ...


class _IAppsyncFunctionProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Interface for AppSync Functions.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appsync.IAppsyncFunction"

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        '''the ARN of the AppSync function.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @builtins.property
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        '''the name of this AppSync Function.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppsyncFunction).__jsii_proxy_class__ = lambda : _IAppsyncFunctionProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appsync.IGraphqlApi")
class IGraphqlApi(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface for GraphQL.'''

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''the ARN of the API.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _ITable_504fd401,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "DynamoDbDataSource":
        '''add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        ...

    @jsii.member(jsii_name="addElasticsearchDataSource")
    def add_elasticsearch_data_source(
        self,
        id: builtins.str,
        domain: _IDomain_0c9006b4,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "ElasticsearchDataSource":
        '''(deprecated) add a new elasticsearch data source to this API.

        :param id: The data source's id.
        :param domain: The elasticsearch domain for this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :deprecated: - use ``addOpenSearchDataSource``

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="addEventBridgeDataSource")
    def add_event_bridge_data_source(
        self,
        id: builtins.str,
        event_bus: _IEventBus_88d13111,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "EventBridgeDataSource":
        '''Add an EventBridge data source to this api.

        :param id: The data source's id.
        :param event_bus: The EventBridge EventBus on which to put events.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        ...

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        '''add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        ...

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _IFunction_6adb0ab8,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        '''add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        ...

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "NoneDataSource":
        '''add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        ...

    @jsii.member(jsii_name="addOpenSearchDataSource")
    def add_open_search_data_source(
        self,
        id: builtins.str,
        domain: _IDomain_3c13cbdd,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "OpenSearchDataSource":
        '''Add a new OpenSearch data source to this API.

        :param id: The data source's id.
        :param domain: The OpenSearch domain for this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        ...

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        serverless_cluster: _IServerlessCluster_adbbb720,
        secret_store: _ISecret_6e020e6a,
        database_name: typing.Optional[builtins.str] = None,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        '''add a new Rds data source to this API.

        :param id: The data source's id.
        :param serverless_cluster: The serverless cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the serverless cluster.
        :param database_name: The optional name of the database to use within the cluster.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        ...

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(self, construct: _CfnResource_9df397a6) -> builtins.bool:
        '''Add schema dependency if not imported.

        :param construct: the dependee.
        '''
        ...

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        id: builtins.str,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[Code] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        runtime: typing.Optional[FunctionRuntime] = None,
    ) -> "Resolver":
        '''creates a new resolver for this datasource and API using the given properties.

        :param id: -
        :param data_source: The data source this resolver is using. Default: - No datasource
        :param field_name: name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param caching_config: The caching configuration for this resolver. Default: - No caching configuration
        :param code: The function code. Default: - no code is used
        :param max_batch_size: The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        '''
        ...


class _IGraphqlApiProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Interface for GraphQL.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appsync.IGraphqlApi"

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''the ARN of the API.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _ITable_504fd401,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "DynamoDbDataSource":
        '''add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43da9ca276f601968eabc2575ce6745ba4152bbf47201270933feda5452ce68a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("DynamoDbDataSource", jsii.invoke(self, "addDynamoDbDataSource", [id, table, options]))

    @jsii.member(jsii_name="addElasticsearchDataSource")
    def add_elasticsearch_data_source(
        self,
        id: builtins.str,
        domain: _IDomain_0c9006b4,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "ElasticsearchDataSource":
        '''(deprecated) add a new elasticsearch data source to this API.

        :param id: The data source's id.
        :param domain: The elasticsearch domain for this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :deprecated: - use ``addOpenSearchDataSource``

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d976a6c9cea09ad6131d004dd38bbab6c2059e80a1a41697431f21da733851ef)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("ElasticsearchDataSource", jsii.invoke(self, "addElasticsearchDataSource", [id, domain, options]))

    @jsii.member(jsii_name="addEventBridgeDataSource")
    def add_event_bridge_data_source(
        self,
        id: builtins.str,
        event_bus: _IEventBus_88d13111,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "EventBridgeDataSource":
        '''Add an EventBridge data source to this api.

        :param id: The data source's id.
        :param event_bus: The EventBridge EventBus on which to put events.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7f859036563760af3f55f190f35d263357d6df8725cd3d3990a639dc02796df)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument event_bus", value=event_bus, expected_type=type_hints["event_bus"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("EventBridgeDataSource", jsii.invoke(self, "addEventBridgeDataSource", [id, event_bus, options]))

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        '''add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a5ae312823194eb5a4a37d99f965046bb8750ad62c67b536c7378744591071)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        options = HttpDataSourceOptions(
            authorization_config=authorization_config,
            description=description,
            name=name,
        )

        return typing.cast("HttpDataSource", jsii.invoke(self, "addHttpDataSource", [id, endpoint, options]))

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _IFunction_6adb0ab8,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        '''add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49c24df9542a2559af242eb252634947ce0ed3aa9d4e4efca32b6db37271ef48)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("LambdaDataSource", jsii.invoke(self, "addLambdaDataSource", [id, lambda_function, options]))

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "NoneDataSource":
        '''add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aa2890745bf86976bff5a0152fe1757b4534eabb56973b08a45c2c539adc58d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("NoneDataSource", jsii.invoke(self, "addNoneDataSource", [id, options]))

    @jsii.member(jsii_name="addOpenSearchDataSource")
    def add_open_search_data_source(
        self,
        id: builtins.str,
        domain: _IDomain_3c13cbdd,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "OpenSearchDataSource":
        '''Add a new OpenSearch data source to this API.

        :param id: The data source's id.
        :param domain: The OpenSearch domain for this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e51c29583b8567298ff7b528e3996298135787d4fbe5dfe686b388500e8ce53)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("OpenSearchDataSource", jsii.invoke(self, "addOpenSearchDataSource", [id, domain, options]))

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        serverless_cluster: _IServerlessCluster_adbbb720,
        secret_store: _ISecret_6e020e6a,
        database_name: typing.Optional[builtins.str] = None,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        '''add a new Rds data source to this API.

        :param id: The data source's id.
        :param serverless_cluster: The serverless cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the serverless cluster.
        :param database_name: The optional name of the database to use within the cluster.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00411b1875c06ea0450c7cb3f4f4dbd07f2f28986d7180e3a06f5ea235641679)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument serverless_cluster", value=serverless_cluster, expected_type=type_hints["serverless_cluster"])
            check_type(argname="argument secret_store", value=secret_store, expected_type=type_hints["secret_store"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("RdsDataSource", jsii.invoke(self, "addRdsDataSource", [id, serverless_cluster, secret_store, database_name, options]))

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(self, construct: _CfnResource_9df397a6) -> builtins.bool:
        '''Add schema dependency if not imported.

        :param construct: the dependee.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7845da8546318a24ccdcc5b7669f4273b997f01e1807a63aae7beabbe99b178b)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addSchemaDependency", [construct]))

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        id: builtins.str,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[Code] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        runtime: typing.Optional[FunctionRuntime] = None,
    ) -> "Resolver":
        '''creates a new resolver for this datasource and API using the given properties.

        :param id: -
        :param data_source: The data source this resolver is using. Default: - No datasource
        :param field_name: name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param caching_config: The caching configuration for this resolver. Default: - No caching configuration
        :param code: The function code. Default: - no code is used
        :param max_batch_size: The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1231d659a3d5f86849b39ea5e3924e5d6867178b9b48617ec80686588387ac)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ExtendedResolverProps(
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            code=code,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            runtime=runtime,
        )

        return typing.cast("Resolver", jsii.invoke(self, "createResolver", [id, props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphqlApi).__jsii_proxy_class__ = lambda : _IGraphqlApiProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appsync.ISchema")
class ISchema(typing_extensions.Protocol):
    '''Interface for implementing your own schema.

    Useful for providing schema's from sources other than assets
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, api: IGraphqlApi) -> "ISchemaConfig":
        '''Binds a schema string to a GraphQlApi.

        :param api: the api to bind the schema to.

        :return: ISchemaConfig with apiId and schema definition string
        '''
        ...


class _ISchemaProxy:
    '''Interface for implementing your own schema.

    Useful for providing schema's from sources other than assets
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appsync.ISchema"

    @jsii.member(jsii_name="bind")
    def bind(self, api: IGraphqlApi) -> "ISchemaConfig":
        '''Binds a schema string to a GraphQlApi.

        :param api: the api to bind the schema to.

        :return: ISchemaConfig with apiId and schema definition string
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ab7bd2a4f271f294370de26c1f7a13edd4a7e586c474d1ce0d7c4b532ad79a5)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        options = SchemaBindOptions()

        return typing.cast("ISchemaConfig", jsii.invoke(self, "bind", [api, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchema).__jsii_proxy_class__ = lambda : _ISchemaProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appsync.ISchemaConfig")
class ISchemaConfig(typing_extensions.Protocol):
    '''Configuration for bound graphql schema.

    Returned from ISchema.bind allowing late binding of schemas to graphqlapi-base
    '''

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The ID of the api the schema is bound to.'''
        ...

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> builtins.str:
        '''The schema definition string.'''
        ...

    @definition.setter
    def definition(self, value: builtins.str) -> None:
        ...


class _ISchemaConfigProxy:
    '''Configuration for bound graphql schema.

    Returned from ISchema.bind allowing late binding of schemas to graphqlapi-base
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appsync.ISchemaConfig"

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The ID of the api the schema is bound to.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7394e47c73f9dbf60d57fa33fdbf7af98d828fabd51c4670bd5acc1cd4b653b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> builtins.str:
        '''The schema definition string.'''
        return typing.cast(builtins.str, jsii.get(self, "definition"))

    @definition.setter
    def definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a58b3bfbb8f3147e1915d76419b3d10f5232745190dda75c89309c09daa598df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaConfig).__jsii_proxy_class__ = lambda : _ISchemaConfigProxy


class IamResource(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.IamResource",
):
    '''A class used to generate resource arns for AppSync.

    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )
        
        api.grant(role, appsync.IamResource.custom("types/Mutation/fields/updateExample"), "appsync:GraphQL")
    '''

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(cls) -> "IamResource":
        '''Generate the resource names that accepts all types: ``*``.'''
        return typing.cast("IamResource", jsii.sinvoke(cls, "all", []))

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, *arns: builtins.str) -> "IamResource":
        '''Generate the resource names given custom arns.

        :param arns: The custom arns that need to be permissioned. Example: custom('/types/Query/fields/getExample')
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__486fba677a06e1d2f86de3d1bfebdc816a08fdb75280a8c7778fcb2d186723db)
            check_type(argname="argument arns", value=arns, expected_type=typing.Tuple[type_hints["arns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IamResource", jsii.sinvoke(cls, "custom", [*arns]))

    @jsii.member(jsii_name="ofType")
    @builtins.classmethod
    def of_type(cls, type: builtins.str, *fields: builtins.str) -> "IamResource":
        '''Generate the resource names given a type and fields.

        :param type: The type that needs to be allowed.
        :param fields: The fields that need to be allowed, if empty grant permissions to ALL fields. Example: ofType('Query', 'GetExample')
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ef3ffd4a7e1a514f99330034c53323b9d1884fe72b84846ee2c9b3bd34ce84)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument fields", value=fields, expected_type=typing.Tuple[type_hints["fields"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IamResource", jsii.sinvoke(cls, "ofType", [type, *fields]))

    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self, api: "GraphqlApi") -> typing.List[builtins.str]:
        '''Return the Resource ARN.

        :param api: The GraphQL API to give permissions.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd39c5d442ee7ade433a10992f6a94e24818b16e448af33f399f02d21d4532a6)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "resourceArns", [api]))


class InlineCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.InlineCode",
):
    '''AppSync function code from an inline string.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        inline_code = appsync.InlineCode("code")
    '''

    def __init__(self, code: builtins.str) -> None:
        '''
        :param code: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e00df94df91e7d536755d93e1e2969ac7ef87855b860cb5fc2d4ad7545f013)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
        jsii.create(self.__class__, self, [code])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: _constructs_77d1e7e8.Construct) -> CodeConfig:
        '''Bind source code to an AppSync Function or resolver.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83acb173a79e10774f37e4699441474aba7a06c89753cc8bbc811841fb968a5a)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(CodeConfig, jsii.invoke(self, "bind", [_scope]))


class KeyCondition(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.KeyCondition",
):
    '''Factory class for DynamoDB key conditions.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        key_condition = appsync.KeyCondition.begins_with("keyName", "arg")
    '''

    @jsii.member(jsii_name="beginsWith")
    @builtins.classmethod
    def begins_with(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''Condition (k, arg).

        True if the key attribute k begins with the Query argument.

        :param key_name: -
        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be31cec85c5d6e8d84a1ff6120f28763539905417cd2f90518c2486794627fd)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "beginsWith", [key_name, arg]))

    @jsii.member(jsii_name="between")
    @builtins.classmethod
    def between(
        cls,
        key_name: builtins.str,
        arg1: builtins.str,
        arg2: builtins.str,
    ) -> "KeyCondition":
        '''Condition k BETWEEN arg1 AND arg2, true if k >= arg1 and k <= arg2.

        :param key_name: -
        :param arg1: -
        :param arg2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f36a295e481a13f223776e0fc0091431083d5103e086745aac3a7742a3f266c)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg1", value=arg1, expected_type=type_hints["arg1"])
            check_type(argname="argument arg2", value=arg2, expected_type=type_hints["arg2"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "between", [key_name, arg1, arg2]))

    @jsii.member(jsii_name="eq")
    @builtins.classmethod
    def eq(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''Condition k = arg, true if the key attribute k is equal to the Query argument.

        :param key_name: -
        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c3d89a9e0dfcb30290ceb9cf53e14011e8b3847ee2ddff39ec1455d377c466)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "eq", [key_name, arg]))

    @jsii.member(jsii_name="ge")
    @builtins.classmethod
    def ge(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''Condition k >= arg, true if the key attribute k is greater or equal to the Query argument.

        :param key_name: -
        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ae3f2f70bd8308fde66d04db7159818ce15f3d5eb9bdceffafe033ad76263fe)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "ge", [key_name, arg]))

    @jsii.member(jsii_name="gt")
    @builtins.classmethod
    def gt(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''Condition k > arg, true if the key attribute k is greater than the the Query argument.

        :param key_name: -
        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e58baab7b37668816dd9d41eab697b6f94271aba9923b84d3423efe91daa733e)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "gt", [key_name, arg]))

    @jsii.member(jsii_name="le")
    @builtins.classmethod
    def le(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''Condition k <= arg, true if the key attribute k is less than or equal to the Query argument.

        :param key_name: -
        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c12ca3fbbf83507d43081a8b4c0321290e7c340883b8919107e08ee2d500856b)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "le", [key_name, arg]))

    @jsii.member(jsii_name="lt")
    @builtins.classmethod
    def lt(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''Condition k < arg, true if the key attribute k is less than the Query argument.

        :param key_name: -
        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f32b8919c697477f7851076a245af3b8d4d8b30d2661db1ade267c92ddc6866a)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "lt", [key_name, arg]))

    @jsii.member(jsii_name="and")
    def and_(self, key_cond: "KeyCondition") -> "KeyCondition":
        '''Conjunction between two conditions.

        :param key_cond: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__841cb23f43ce7bfe91ae9e27a40b958f6c4d4c8a01a675d5e452889ba1c5639d)
            check_type(argname="argument key_cond", value=key_cond, expected_type=type_hints["key_cond"])
        return typing.cast("KeyCondition", jsii.invoke(self, "and", [key_cond]))

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        '''Renders the key condition to a VTL string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderTemplate", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.LambdaAuthorizerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "handler": "handler",
        "results_cache_ttl": "resultsCacheTtl",
        "validation_regex": "validationRegex",
    },
)
class LambdaAuthorizerConfig:
    def __init__(
        self,
        *,
        handler: _IFunction_6adb0ab8,
        results_cache_ttl: typing.Optional[_Duration_4839e8c3] = None,
        validation_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration for Lambda authorization in AppSync.

        Note that you can only have a single AWS Lambda function configured to authorize your API.

        :param handler: The authorizer lambda function.
        :param results_cache_ttl: How long the results are cached. Disable caching by setting this to 0. Default: Duration.minutes(5)
        :param validation_regex: A regular expression for validation of tokens before the Lambda function is called. Default: - no regex filter will be applied.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # auth_function: lambda.Function
            
            
            appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.test.graphql")),
                authorization_config=appsync.AuthorizationConfig(
                    default_authorization=appsync.AuthorizationMode(
                        authorization_type=appsync.AuthorizationType.LAMBDA,
                        lambda_authorizer_config=appsync.LambdaAuthorizerConfig(
                            handler=auth_function
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85bd76d9345653fd1813036904e3edadb83b6c1c51d38e8234237345dc3773dd)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument results_cache_ttl", value=results_cache_ttl, expected_type=type_hints["results_cache_ttl"])
            check_type(argname="argument validation_regex", value=validation_regex, expected_type=type_hints["validation_regex"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "handler": handler,
        }
        if results_cache_ttl is not None:
            self._values["results_cache_ttl"] = results_cache_ttl
        if validation_regex is not None:
            self._values["validation_regex"] = validation_regex

    @builtins.property
    def handler(self) -> _IFunction_6adb0ab8:
        '''The authorizer lambda function.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html
        '''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(_IFunction_6adb0ab8, result)

    @builtins.property
    def results_cache_ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''How long the results are cached.

        Disable caching by setting this to 0.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("results_cache_ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def validation_regex(self) -> typing.Optional[builtins.str]:
        '''A regular expression for validation of tokens before the Lambda function is called.

        :default: - no regex filter will be applied.
        '''
        result = self._values.get("validation_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaAuthorizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.LogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_verbose_content": "excludeVerboseContent",
        "field_log_level": "fieldLogLevel",
        "retention": "retention",
        "role": "role",
    },
)
class LogConfig:
    def __init__(
        self,
        *,
        exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        field_log_level: typing.Optional[FieldLogLevel] = None,
        retention: typing.Optional[_RetentionDays_070f99f0] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Logging configuration for AppSync.

        :param exclude_verbose_content: exclude verbose content. Default: false
        :param field_log_level: log level for fields. Default: - Use AppSync default
        :param retention: The number of days log events are kept in CloudWatch Logs. By default AppSync keeps the logs infinitely. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE`` Default: RetentionDays.INFINITE
        :param role: The role for CloudWatch Logs. Default: - None

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_logs as logs
            
            
            log_config = appsync.LogConfig(
                retention=logs.RetentionDays.ONE_WEEK
            )
            
            appsync.GraphqlApi(self, "api",
                authorization_config=appsync.AuthorizationConfig(),
                name="myApi",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "myApi.graphql")),
                log_config=log_config
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d73860e597bcfca4336f77cac0c6ce67113883e4171d802987f80c349fd909d1)
            check_type(argname="argument exclude_verbose_content", value=exclude_verbose_content, expected_type=type_hints["exclude_verbose_content"])
            check_type(argname="argument field_log_level", value=field_log_level, expected_type=type_hints["field_log_level"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude_verbose_content is not None:
            self._values["exclude_verbose_content"] = exclude_verbose_content
        if field_log_level is not None:
            self._values["field_log_level"] = field_log_level
        if retention is not None:
            self._values["retention"] = retention
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def exclude_verbose_content(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''exclude verbose content.

        :default: false
        '''
        result = self._values.get("exclude_verbose_content")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def field_log_level(self) -> typing.Optional[FieldLogLevel]:
        '''log level for fields.

        :default: - Use AppSync default
        '''
        result = self._values.get("field_log_level")
        return typing.cast(typing.Optional[FieldLogLevel], result)

    @builtins.property
    def retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''The number of days log events are kept in CloudWatch Logs.

        By default AppSync keeps the logs infinitely. When updating this property,
        unsetting it doesn't remove the log retention policy.
        To remove the retention policy, set the value to ``INFINITE``

        :default: RetentionDays.INFINITE
        '''
        result = self._values.get("retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role for CloudWatch Logs.

        :default: - None
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MappingTemplate(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appsync.MappingTemplate",
):
    '''MappingTemplates for AppSync resolvers.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_events as events
        
        
        api = appsync.GraphqlApi(self, "EventBridgeApi",
            name="EventBridgeApi",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.eventbridge.graphql"))
        )
        
        bus = events.EventBus(self, "DestinationEventBus")
        
        data_source = api.add_event_bridge_data_source("NoneDS", bus)
        
        data_source.create_resolver("EventResolver",
            type_name="Mutation",
            field_name="emitEvent",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="dynamoDbDeleteItem")
    @builtins.classmethod
    def dynamo_db_delete_item(
        cls,
        key_name: builtins.str,
        id_arg: builtins.str,
    ) -> "MappingTemplate":
        '''Mapping template to delete a single item from a DynamoDB table.

        :param key_name: the name of the hash key field.
        :param id_arg: the name of the Mutation argument.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8039f0676302cd6a9ab028032df416cedee74a1e034ef40aa741c05a635901f)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument id_arg", value=id_arg, expected_type=type_hints["id_arg"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbDeleteItem", [key_name, id_arg]))

    @jsii.member(jsii_name="dynamoDbGetItem")
    @builtins.classmethod
    def dynamo_db_get_item(
        cls,
        key_name: builtins.str,
        id_arg: builtins.str,
        consistent_read: typing.Optional[builtins.bool] = None,
    ) -> "MappingTemplate":
        '''Mapping template to get a single item from a DynamoDB table.

        :param key_name: the name of the hash key field.
        :param id_arg: the name of the Query argument.
        :param consistent_read: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ed2d1bc991a539021943757343be2d737ab814fed8178ebe300c8db10b0987b)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument id_arg", value=id_arg, expected_type=type_hints["id_arg"])
            check_type(argname="argument consistent_read", value=consistent_read, expected_type=type_hints["consistent_read"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbGetItem", [key_name, id_arg, consistent_read]))

    @jsii.member(jsii_name="dynamoDbPutItem")
    @builtins.classmethod
    def dynamo_db_put_item(
        cls,
        key: "PrimaryKey",
        values: AttributeValues,
    ) -> "MappingTemplate":
        '''Mapping template to save a single item to a DynamoDB table.

        :param key: the assigment of Mutation values to the primary key.
        :param values: the assignment of Mutation values to the table attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f6e0c226f78611f34b78ab0e1d8991442c728d76763ffe43986e41363e71217)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbPutItem", [key, values]))

    @jsii.member(jsii_name="dynamoDbQuery")
    @builtins.classmethod
    def dynamo_db_query(
        cls,
        cond: KeyCondition,
        index_name: typing.Optional[builtins.str] = None,
        consistent_read: typing.Optional[builtins.bool] = None,
    ) -> "MappingTemplate":
        '''Mapping template to query a set of items from a DynamoDB table.

        :param cond: the key condition for the query.
        :param index_name: -
        :param consistent_read: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c051303dcbf7aca274ccea310cfa57f3f39591bfc2b9d5833a2a6a135af6394d)
            check_type(argname="argument cond", value=cond, expected_type=type_hints["cond"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument consistent_read", value=consistent_read, expected_type=type_hints["consistent_read"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbQuery", [cond, index_name, consistent_read]))

    @jsii.member(jsii_name="dynamoDbResultItem")
    @builtins.classmethod
    def dynamo_db_result_item(cls) -> "MappingTemplate":
        '''Mapping template for a single result item from DynamoDB.'''
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbResultItem", []))

    @jsii.member(jsii_name="dynamoDbResultList")
    @builtins.classmethod
    def dynamo_db_result_list(cls) -> "MappingTemplate":
        '''Mapping template for a result list from DynamoDB.'''
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbResultList", []))

    @jsii.member(jsii_name="dynamoDbScanTable")
    @builtins.classmethod
    def dynamo_db_scan_table(
        cls,
        consistent_read: typing.Optional[builtins.bool] = None,
    ) -> "MappingTemplate":
        '''Mapping template to scan a DynamoDB table to fetch all entries.

        :param consistent_read: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6a8a228010e1e6327b0d1f8956027d8ff0cb28b0f4fb4c95753b3aaea58f729)
            check_type(argname="argument consistent_read", value=consistent_read, expected_type=type_hints["consistent_read"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbScanTable", [consistent_read]))

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(cls, file_name: builtins.str) -> "MappingTemplate":
        '''Create a mapping template from the given file.

        :param file_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e01baf3340cd576c62786da8e2ad0c983ebdbad06b932b7de57a46f6e48fd0)
            check_type(argname="argument file_name", value=file_name, expected_type=type_hints["file_name"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "fromFile", [file_name]))

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(cls, template: builtins.str) -> "MappingTemplate":
        '''Create a mapping template from the given string.

        :param template: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bac5b3ede51565e6835fed423e0a1e7f8e87f0cf2454f06ff0c5aa9c3bcd804)
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "fromString", [template]))

    @jsii.member(jsii_name="lambdaRequest")
    @builtins.classmethod
    def lambda_request(
        cls,
        payload: typing.Optional[builtins.str] = None,
        operation: typing.Optional[builtins.str] = None,
    ) -> "MappingTemplate":
        '''Mapping template to invoke a Lambda function.

        :param payload: the VTL template snippet of the payload to send to the lambda. If no payload is provided all available context fields are sent to the Lambda function
        :param operation: the type of operation AppSync should perform on the data source.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b43f41b3eaa9c822ef11e6a8987a60daa66f2982d2ea77dfae0ce5eaec49c0)
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "lambdaRequest", [payload, operation]))

    @jsii.member(jsii_name="lambdaResult")
    @builtins.classmethod
    def lambda_result(cls) -> "MappingTemplate":
        '''Mapping template to return the Lambda result to the caller.'''
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "lambdaResult", []))

    @jsii.member(jsii_name="renderTemplate")
    @abc.abstractmethod
    def render_template(self) -> builtins.str:
        '''this is called to render the mapping template to a VTL string.'''
        ...


class _MappingTemplateProxy(MappingTemplate):
    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        '''this is called to render the mapping template to a VTL string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderTemplate", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, MappingTemplate).__jsii_proxy_class__ = lambda : _MappingTemplateProxy


class NoneDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.NoneDataSource",
):
    '''An AppSync dummy datasource.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        # graphql_api: appsync.GraphqlApi
        
        none_data_source = appsync.NoneDataSource(self, "MyNoneDataSource",
            api=graphql_api,
        
            # the properties below are optional
            description="description",
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1611db7d560b46fd4ac561a4c80f0c620482391b0a4b50a2e95caca4f5e07e31)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = NoneDataSourceProps(api=api, description=description, name=name)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.NoneDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={"api": "api", "description": "description", "name": "name"},
)
class NoneDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for an AppSync dummy datasource.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            # graphql_api: appsync.GraphqlApi
            
            none_data_source_props = appsync.NoneDataSourceProps(
                api=graphql_api,
            
                # the properties below are optional
                description="description",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f714cd165303e3c7148f1ca4c53fe5e7abe0f744c242bcdbb8dc5817bd63ecda)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NoneDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.OpenIdConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "oidc_provider": "oidcProvider",
        "client_id": "clientId",
        "token_expiry_from_auth": "tokenExpiryFromAuth",
        "token_expiry_from_issue": "tokenExpiryFromIssue",
    },
)
class OpenIdConnectConfig:
    def __init__(
        self,
        *,
        oidc_provider: builtins.str,
        client_id: typing.Optional[builtins.str] = None,
        token_expiry_from_auth: typing.Optional[jsii.Number] = None,
        token_expiry_from_issue: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Configuration for OpenID Connect authorization in AppSync.

        :param oidc_provider: The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the OIDC token.
        :param client_id: The client identifier of the Relying party at the OpenID identity provider. A regular expression can be specified so AppSync can validate against multiple client identifiers at a time. Default: - - (All)
        :param token_expiry_from_auth: The number of milliseconds an OIDC token is valid after being authenticated by OIDC provider. ``auth_time`` claim in OIDC token is required for this validation to work. Default: - no validation
        :param token_expiry_from_issue: The number of milliseconds an OIDC token is valid after being issued to a user. This validation uses ``iat`` claim of OIDC token. Default: - no validation

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            open_id_connect_config = appsync.OpenIdConnectConfig(
                oidc_provider="oidcProvider",
            
                # the properties below are optional
                client_id="clientId",
                token_expiry_from_auth=123,
                token_expiry_from_issue=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e8ab4c6015808cd4bb9ca15d799fa7c987da055820136f0a938859823c20863)
            check_type(argname="argument oidc_provider", value=oidc_provider, expected_type=type_hints["oidc_provider"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument token_expiry_from_auth", value=token_expiry_from_auth, expected_type=type_hints["token_expiry_from_auth"])
            check_type(argname="argument token_expiry_from_issue", value=token_expiry_from_issue, expected_type=type_hints["token_expiry_from_issue"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "oidc_provider": oidc_provider,
        }
        if client_id is not None:
            self._values["client_id"] = client_id
        if token_expiry_from_auth is not None:
            self._values["token_expiry_from_auth"] = token_expiry_from_auth
        if token_expiry_from_issue is not None:
            self._values["token_expiry_from_issue"] = token_expiry_from_issue

    @builtins.property
    def oidc_provider(self) -> builtins.str:
        '''The issuer for the OIDC configuration.

        The issuer returned by discovery must exactly match the value of ``iss`` in the OIDC token.
        '''
        result = self._values.get("oidc_provider")
        assert result is not None, "Required property 'oidc_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''The client identifier of the Relying party at the OpenID identity provider.

        A regular expression can be specified so AppSync can validate against multiple client identifiers at a time.

        :default:

        -
        - (All)

        Example::

            -"ABCD|CDEF"
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_expiry_from_auth(self) -> typing.Optional[jsii.Number]:
        '''The number of milliseconds an OIDC token is valid after being authenticated by OIDC provider.

        ``auth_time`` claim in OIDC token is required for this validation to work.

        :default: - no validation
        '''
        result = self._values.get("token_expiry_from_auth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_expiry_from_issue(self) -> typing.Optional[jsii.Number]:
        '''The number of milliseconds an OIDC token is valid after being issued to a user.

        This validation uses ``iat`` claim of OIDC token.

        :default: - no validation
        '''
        result = self._values.get("token_expiry_from_issue")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenIdConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartitionKeyStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.PartitionKeyStep",
):
    '''Utility class to allow assigning a value or an auto-generated id to a partition key.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        partition_key_step = appsync.PartitionKeyStep("key")
    '''

    def __init__(self, key: builtins.str) -> None:
        '''
        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bab0c247e74b70c09f0c524751991f49de1721941f7cfa97e954c8901f221f2d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        jsii.create(self.__class__, self, [key])

    @jsii.member(jsii_name="auto")
    def auto(self) -> "PartitionKey":
        '''Assign an auto-generated value to the partition key.'''
        return typing.cast("PartitionKey", jsii.invoke(self, "auto", []))

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> "PartitionKey":
        '''Assign an auto-generated value to the partition key.

        :param val: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbc9c7177fa8eaaac3f78a5985704f2e0b65afdc9ef98e9fcebb628b16844e52)
            check_type(argname="argument val", value=val, expected_type=type_hints["val"])
        return typing.cast("PartitionKey", jsii.invoke(self, "is", [val]))


class PrimaryKey(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.PrimaryKey",
):
    '''Specifies the assignment to the primary key.

    It either
    contains the full primary key or only the partition key.

    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    def __init__(self, pkey: Assign, skey: typing.Optional[Assign] = None) -> None:
        '''
        :param pkey: -
        :param skey: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894e920ca7d06b2f6f8f782c7af5bcd4e290f7c5ab0076004a253c04d6cfaec0)
            check_type(argname="argument pkey", value=pkey, expected_type=type_hints["pkey"])
            check_type(argname="argument skey", value=skey, expected_type=type_hints["skey"])
        jsii.create(self.__class__, self, [pkey, skey])

    @jsii.member(jsii_name="partition")
    @builtins.classmethod
    def partition(cls, key: builtins.str) -> PartitionKeyStep:
        '''Allows assigning a value to the partition key.

        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__331614f70c4957ba245389adda042d248e85ee7b1e7ca5531863245ae9efa42b)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(PartitionKeyStep, jsii.sinvoke(cls, "partition", [key]))

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        '''Renders the key assignment to a VTL string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="pkey")
    def _pkey(self) -> Assign:
        return typing.cast(Assign, jsii.get(self, "pkey"))


class Resolver(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.Resolver",
):
    '''An AppSync resolver.

    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        # appsync_function: appsync.AppsyncFunction
        
        
        pipeline_resolver = appsync.Resolver(self, "pipeline",
            api=api,
            data_source=api.add_none_data_source("none"),
            type_name="typeName",
            field_name="fieldName",
            request_mapping_template=appsync.MappingTemplate.from_file("beforeRequest.vtl"),
            pipeline_config=[appsync_function],
            response_mapping_template=appsync.MappingTemplate.from_file("afterResponse.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[Code] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        runtime: typing.Optional[FunctionRuntime] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param api: The API this resolver is attached to.
        :param data_source: The data source this resolver is using. Default: - No datasource
        :param field_name: name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param caching_config: The caching configuration for this resolver. Default: - No caching configuration
        :param code: The function code. Default: - no code is used
        :param max_batch_size: The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dac7c0ed89396d7f29c7903e2a718a49bfb552b89c6e4aba2bf132b53179d5a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ResolverProps(
            api=api,
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            code=code,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            runtime=runtime,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''the ARN of the resolver.'''
        return typing.cast(builtins.str, jsii.get(self, "arn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.ResolverProps",
    jsii_struct_bases=[ExtendedResolverProps],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "code": "code",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "runtime": "runtime",
        "data_source": "dataSource",
        "api": "api",
    },
)
class ResolverProps(ExtendedResolverProps):
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[Code] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        runtime: typing.Optional[FunctionRuntime] = None,
        data_source: typing.Optional[BaseDataSource] = None,
        api: IGraphqlApi,
    ) -> None:
        '''Additional property for an AppSync resolver for GraphQL API reference.

        :param field_name: name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param caching_config: The caching configuration for this resolver. Default: - No caching configuration
        :param code: The function code. Default: - no code is used
        :param max_batch_size: The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        :param data_source: The data source this resolver is using. Default: - No datasource
        :param api: The API this resolver is attached to.

        :exampleMetadata: infused

        Example::

            # api: appsync.GraphqlApi
            # appsync_function: appsync.AppsyncFunction
            
            
            pipeline_resolver = appsync.Resolver(self, "pipeline",
                api=api,
                data_source=api.add_none_data_source("none"),
                type_name="typeName",
                field_name="fieldName",
                request_mapping_template=appsync.MappingTemplate.from_file("beforeRequest.vtl"),
                pipeline_config=[appsync_function],
                response_mapping_template=appsync.MappingTemplate.from_file("afterResponse.vtl")
            )
        '''
        if isinstance(caching_config, dict):
            caching_config = CachingConfig(**caching_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe6f3e60857395308a8a844c5a41064caae65e42a2597bef9b2139e42f0c5550)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
            "api": api,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if code is not None:
            self._values["code"] = code
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if runtime is not None:
            self._values["runtime"] = runtime
        if data_source is not None:
            self._values["data_source"] = data_source

    @builtins.property
    def field_name(self) -> builtins.str:
        '''name of the GraphQL field in the given type this resolver is attached to.'''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''name of the GraphQL type this resolver is attached to.'''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(self) -> typing.Optional[CachingConfig]:
        '''The caching configuration for this resolver.

        :default: - No caching configuration
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional[CachingConfig], result)

    @builtins.property
    def code(self) -> typing.Optional[Code]:
        '''The function code.

        :default: - no code is used
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[Code], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of elements per batch, when using batch invoke.

        :default: - No max batch size
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List[IAppsyncFunction]]:
        '''configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional[typing.List[IAppsyncFunction]], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[MappingTemplate]:
        '''The request mapping template for this resolver.

        :default: - No mapping template
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[MappingTemplate], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[MappingTemplate]:
        '''The response mapping template for this resolver.

        :default: - No mapping template
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[MappingTemplate], result)

    @builtins.property
    def runtime(self) -> typing.Optional[FunctionRuntime]:
        '''The functions runtime.

        :default: - no function runtime, VTL mapping templates used
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[FunctionRuntime], result)

    @builtins.property
    def data_source(self) -> typing.Optional[BaseDataSource]:
        '''The data source this resolver is using.

        :default: - No datasource
        '''
        result = self._values.get("data_source")
        return typing.cast(typing.Optional[BaseDataSource], result)

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API this resolver is attached to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.RuntimeConfig",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "runtime_version": "runtimeVersion"},
)
class RuntimeConfig:
    def __init__(self, *, name: builtins.str, runtime_version: builtins.str) -> None:
        '''Config for binding runtime to a function or resolver.

        :param name: The name of the runtime.
        :param runtime_version: The version string of the runtime.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            runtime_config = appsync.RuntimeConfig(
                name="name",
                runtime_version="runtimeVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49869076912d34bbcf8b6ff9fda046f1ab0998a982c178c6a23b70ae322f278c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "runtime_version": runtime_version,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the runtime.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime_version(self) -> builtins.str:
        '''The version string of the runtime.'''
        result = self._values.get("runtime_version")
        assert result is not None, "Required property 'runtime_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuntimeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.SchemaBindOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class SchemaBindOptions:
    def __init__(self) -> None:
        '''Used for configuring schema bind behavior.

        This is intended to prevent breaking changes to implementors of ISchema
        if needing to add new behavior.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            
            schema_bind_options = appsync.SchemaBindOptions()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISchema)
class SchemaFile(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.SchemaFile",
):
    '''The Schema for a GraphQL Api.

    If no options are configured, schema will be generated
    code-first.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_events as events
        
        
        api = appsync.GraphqlApi(self, "EventBridgeApi",
            name="EventBridgeApi",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.eventbridge.graphql"))
        )
        
        bus = events.EventBus(self, "DestinationEventBus")
        
        data_source = api.add_event_bridge_data_source("NoneDS", bus)
        
        data_source.create_resolver("EventResolver",
            type_name="Mutation",
            field_name="emitEvent",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(self, *, file_path: builtins.str) -> None:
        '''
        :param file_path: The file path for the schema. When this option is configured, then the schema will be generated from an existing file from disk.
        '''
        options = SchemaProps(file_path=file_path)

        jsii.create(self.__class__, self, [options])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(cls, file_path: builtins.str) -> "SchemaFile":
        '''Generate a Schema from file.

        :param file_path: the file path of the schema file.

        :return: ``SchemaAsset`` with immutable schema defintion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40565593cb0b74633173faf6f073987b024d4b7af8c07e296173c630a61b972a)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        return typing.cast("SchemaFile", jsii.sinvoke(cls, "fromAsset", [file_path]))

    @jsii.member(jsii_name="bind")
    def bind(self, api: IGraphqlApi) -> ISchemaConfig:
        '''Called when the GraphQL Api is initialized to allow this object to bind to the stack.

        :param api: The binding GraphQL Api.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045c4bbd28d6b47aba2e105fffdc95a54744a147dd39c45d3bda36713099050d)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        _options = SchemaBindOptions()

        return typing.cast(ISchemaConfig, jsii.invoke(self, "bind", [api, _options]))

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> builtins.str:
        '''The definition for this schema.'''
        return typing.cast(builtins.str, jsii.get(self, "definition"))

    @definition.setter
    def definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3adee49b1627eaa29eddfbecd2e0b4178976610eae08b6d3f86587aac2bc086b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.SchemaProps",
    jsii_struct_bases=[],
    name_mapping={"file_path": "filePath"},
)
class SchemaProps:
    def __init__(self, *, file_path: builtins.str) -> None:
        '''The options for configuring a schema from an existing file.

        :param file_path: The file path for the schema. When this option is configured, then the schema will be generated from an existing file from disk.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_certificatemanager as acm
            import aws_cdk.aws_route53 as route53
            
            # hosted zone and route53 features
            # hosted_zone_id: str
            zone_name = "example.com"
            
            
            my_domain_name = "api.example.com"
            certificate = acm.Certificate(self, "cert", domain_name=my_domain_name)
            schema = appsync.SchemaFile(file_path="mySchemaFile")
            api = appsync.GraphqlApi(self, "api",
                name="myApi",
                schema=schema,
                domain_name=appsync.DomainOptions(
                    certificate=certificate,
                    domain_name=my_domain_name
                )
            )
            
            # hosted zone for adding appsync domain
            zone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
                hosted_zone_id=hosted_zone_id,
                zone_name=zone_name
            )
            
            # create a cname to the appsync domain. will map to something like xxxx.cloudfront.net
            route53.CnameRecord(self, "CnameApiRecord",
                record_name="api",
                zone=zone,
                domain_name=api.app_sync_domain_name
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebec24f4f2651b34bbc2b330a1662502003c499847aaa673f0f8c02bfb1da189)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_path": file_path,
        }

    @builtins.property
    def file_path(self) -> builtins.str:
        '''The file path for the schema.

        When this option is
        configured, then the schema will be generated from an
        existing file from disk.
        '''
        result = self._values.get("file_path")
        assert result is not None, "Required property 'file_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SortKeyStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.SortKeyStep",
):
    '''Utility class to allow assigning a value or an auto-generated id to a sort key.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        # assign: appsync.Assign
        
        sort_key_step = appsync.SortKeyStep(assign, "skey")
    '''

    def __init__(self, pkey: Assign, skey: builtins.str) -> None:
        '''
        :param pkey: -
        :param skey: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bbf95d843c3b959000a5a0fb88e2cdd71e7f4d434ed1dc1bbee3af5ad4eebb7)
            check_type(argname="argument pkey", value=pkey, expected_type=type_hints["pkey"])
            check_type(argname="argument skey", value=skey, expected_type=type_hints["skey"])
        jsii.create(self.__class__, self, [pkey, skey])

    @jsii.member(jsii_name="auto")
    def auto(self) -> PrimaryKey:
        '''Assign an auto-generated value to the sort key.'''
        return typing.cast(PrimaryKey, jsii.invoke(self, "auto", []))

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> PrimaryKey:
        '''Assign an auto-generated value to the sort key.

        :param val: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__684d8cf05e18cc8e70df256c4f02edd1174c86389940b94860ac8d3c8a646450)
            check_type(argname="argument val", value=val, expected_type=type_hints["val"])
        return typing.cast(PrimaryKey, jsii.invoke(self, "is", [val]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.UserPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool": "userPool",
        "app_id_client_regex": "appIdClientRegex",
        "default_action": "defaultAction",
    },
)
class UserPoolConfig:
    def __init__(
        self,
        *,
        user_pool: _IUserPool_1f1029e2,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        default_action: typing.Optional["UserPoolDefaultAction"] = None,
    ) -> None:
        '''Configuration for Cognito user-pools in AppSync.

        :param user_pool: The Cognito user pool to use as identity source.
        :param app_id_client_regex: the optional app id regex. Default: - None
        :param default_action: Default auth action. Default: ALLOW

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            from aws_cdk import aws_cognito as cognito
            
            # user_pool: cognito.UserPool
            
            user_pool_config = appsync.UserPoolConfig(
                user_pool=user_pool,
            
                # the properties below are optional
                app_id_client_regex="appIdClientRegex",
                default_action=appsync.UserPoolDefaultAction.ALLOW
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d26723deaef4a15fbf75b125939130cfcede962718693a41cf9fd2453a608f62)
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool": user_pool,
        }
        if app_id_client_regex is not None:
            self._values["app_id_client_regex"] = app_id_client_regex
        if default_action is not None:
            self._values["default_action"] = default_action

    @builtins.property
    def user_pool(self) -> _IUserPool_1f1029e2:
        '''The Cognito user pool to use as identity source.'''
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_IUserPool_1f1029e2, result)

    @builtins.property
    def app_id_client_regex(self) -> typing.Optional[builtins.str]:
        '''the optional app id regex.

        :default: - None
        '''
        result = self._values.get("app_id_client_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_action(self) -> typing.Optional["UserPoolDefaultAction"]:
        '''Default auth action.

        :default: ALLOW
        '''
        result = self._values.get("default_action")
        return typing.cast(typing.Optional["UserPoolDefaultAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_appsync.UserPoolDefaultAction")
class UserPoolDefaultAction(enum.Enum):
    '''enum with all possible values for Cognito user-pool default actions.'''

    ALLOW = "ALLOW"
    '''ALLOW access to API.'''
    DENY = "DENY"
    '''DENY access to API.'''


class Values(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_appsync.Values"):
    '''Factory class for attribute value assignments.

    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="attribute")
    @builtins.classmethod
    def attribute(cls, attr: builtins.str) -> AttributeValuesStep:
        '''Allows assigning a value to the specified attribute.

        :param attr: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44bb77a68dfd2f3750592928a447287f6d2eb9f026200de390e4380494e5cb8)
            check_type(argname="argument attr", value=attr, expected_type=type_hints["attr"])
        return typing.cast(AttributeValuesStep, jsii.sinvoke(cls, "attribute", [attr]))

    @jsii.member(jsii_name="projecting")
    @builtins.classmethod
    def projecting(cls, arg: typing.Optional[builtins.str] = None) -> AttributeValues:
        '''Treats the specified object as a map of assignments, where the property names represent attribute names.

        It’s opinionated about how it represents
        some of the nested objects: e.g., it will use lists (“L”) rather than sets
        (“SS”, “NS”, “BS”). By default it projects the argument container ("$ctx.args").

        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f92cb836df619fb1d6788b3bf1522a2affe1a32cec29860d2b16e8bc69fa92ba)
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast(AttributeValues, jsii.sinvoke(cls, "projecting", [arg]))


@jsii.enum(jsii_type="aws-cdk-lib.aws_appsync.Visibility")
class Visibility(enum.Enum):
    '''Visibility type for a GraphQL API.

    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "api",
            name="MyPrivateAPI",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.schema.graphql")),
            visibility=appsync.Visibility.PRIVATE
        )
    '''

    GLOBAL = "GLOBAL"
    '''Public, open to the internet.'''
    PRIVATE = "PRIVATE"
    '''Only accessible through a VPC.'''


@jsii.implements(IAppsyncFunction)
class AppsyncFunction(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.AppsyncFunction",
):
    '''AppSync Functions are local functions that perform certain operations onto a backend data source.

    Developers can compose operations (Functions)
    and execute them in sequence with Pipeline Resolvers.

    :resource: AWS::AppSync::FunctionConfiguration
    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        
        
        appsync_function = appsync.AppsyncFunction(self, "function",
            name="appsync_function",
            api=api,
            data_source=api.add_none_data_source("none"),
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        data_source: BaseDataSource,
        name: builtins.str,
        code: typing.Optional[Code] = None,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        runtime: typing.Optional[FunctionRuntime] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param api: the GraphQL Api linked to this AppSync Function.
        :param data_source: the data source linked to this AppSync Function.
        :param name: the name of the AppSync Function.
        :param code: The function code. Default: - no code is used
        :param description: the description for this AppSync Function. Default: - no description
        :param request_mapping_template: the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: the response mapping template for the AppSync Function. Default: - no response mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a23d4ed33443e24250ebba07a891e2279c2fad90dd6bdb7c0b41b485078d87f1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AppsyncFunctionProps(
            api=api,
            data_source=data_source,
            name=name,
            code=code,
            description=description,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            runtime=runtime,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAppsyncFunctionAttributes")
    @builtins.classmethod
    def from_appsync_function_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        function_arn: builtins.str,
    ) -> IAppsyncFunction:
        '''Import Appsync Function from arn.

        :param scope: -
        :param id: -
        :param function_arn: the ARN of the AppSync function.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4ba394d6181e77cbec9abe16b3e72b648a9b70fd79591b401a435e4394321b0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = AppsyncFunctionAttributes(function_arn=function_arn)

        return typing.cast(IAppsyncFunction, jsii.sinvoke(cls, "fromAppsyncFunctionAttributes", [scope, id, attrs]))

    @builtins.property
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> BaseDataSource:
        '''the data source of this AppSync Function.

        :attribute: DataSourceName
        '''
        return typing.cast(BaseDataSource, jsii.get(self, "dataSource"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        '''the ARN of the AppSync function.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @builtins.property
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        '''the ID of the AppSync function.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionId"))

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        '''the name of this AppSync Function.

        :attribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.AppsyncFunctionProps",
    jsii_struct_bases=[BaseAppsyncFunctionProps],
    name_mapping={
        "name": "name",
        "code": "code",
        "description": "description",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "runtime": "runtime",
        "api": "api",
        "data_source": "dataSource",
    },
)
class AppsyncFunctionProps(BaseAppsyncFunctionProps):
    def __init__(
        self,
        *,
        name: builtins.str,
        code: typing.Optional[Code] = None,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        runtime: typing.Optional[FunctionRuntime] = None,
        api: IGraphqlApi,
        data_source: BaseDataSource,
    ) -> None:
        '''the CDK properties for AppSync Functions.

        :param name: the name of the AppSync Function.
        :param code: The function code. Default: - no code is used
        :param description: the description for this AppSync Function. Default: - no description
        :param request_mapping_template: the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: the response mapping template for the AppSync Function. Default: - no response mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        :param api: the GraphQL Api linked to this AppSync Function.
        :param data_source: the data source linked to this AppSync Function.

        :exampleMetadata: infused

        Example::

            # api: appsync.GraphqlApi
            
            
            appsync_function = appsync.AppsyncFunction(self, "function",
                name="appsync_function",
                api=api,
                data_source=api.add_none_data_source("none"),
                request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
                response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3af0670f4f09a616138962b9570f4bdf3dbddf35d8cf64897cb6240039a9af35)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "api": api,
            "data_source": data_source,
        }
        if code is not None:
            self._values["code"] = code
        if description is not None:
            self._values["description"] = description
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if runtime is not None:
            self._values["runtime"] = runtime

    @builtins.property
    def name(self) -> builtins.str:
        '''the name of the AppSync Function.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(self) -> typing.Optional[Code]:
        '''The function code.

        :default: - no code is used
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[Code], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description for this AppSync Function.

        :default: - no description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[MappingTemplate]:
        '''the request mapping template for the AppSync Function.

        :default: - no request mapping template
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[MappingTemplate], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[MappingTemplate]:
        '''the response mapping template for the AppSync Function.

        :default: - no response mapping template
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[MappingTemplate], result)

    @builtins.property
    def runtime(self) -> typing.Optional[FunctionRuntime]:
        '''The functions runtime.

        :default: - no function runtime, VTL mapping templates used
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[FunctionRuntime], result)

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''the GraphQL Api linked to this AppSync Function.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def data_source(self) -> BaseDataSource:
        '''the data source linked to this AppSync Function.'''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(BaseDataSource, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AssetCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.AssetCode",
):
    '''Represents a local file with source code used for an AppSync Function or Resolver.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_appsync as appsync
        from aws_cdk import aws_iam as iam
        
        # docker_image: cdk.DockerImage
        # grantable: iam.IGrantable
        # local_bundling: cdk.ILocalBundling
        
        asset_code = appsync.AssetCode("path",
            asset_hash="assetHash",
            asset_hash_type=cdk.AssetHashType.SOURCE,
            bundling=cdk.BundlingOptions(
                image=docker_image,
        
                # the properties below are optional
                bundling_file_access=cdk.BundlingFileAccess.VOLUME_COPY,
                command=["command"],
                entrypoint=["entrypoint"],
                environment={
                    "environment_key": "environment"
                },
                local=local_bundling,
                network="network",
                output_type=cdk.BundlingOutput.ARCHIVED,
                platform="platform",
                security_opt="securityOpt",
                user="user",
                volumes=[cdk.DockerVolume(
                    container_path="containerPath",
                    host_path="hostPath",
        
                    # the properties below are optional
                    consistency=cdk.DockerVolumeConsistency.CONSISTENT
                )],
                volumes_from=["volumesFrom"],
                working_directory="workingDirectory"
            ),
            deploy_time=False,
            exclude=["exclude"],
            follow_symlinks=cdk.SymlinkFollowMode.NEVER,
            ignore_mode=cdk.IgnoreMode.GLOB,
            readers=[grantable]
        )
    '''

    def __init__(
        self,
        path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    ) -> None:
        '''
        :param path: The path to the asset file.
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64c3b5b60096d2f072c0237f4540425eb18b7539e311bcd346760100ef39b3f)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = _AssetOptions_2aa69621(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        jsii.create(self.__class__, self, [path, options])

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> CodeConfig:
        '''Bind source code to an AppSync Function or resolver.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9565c14ceaf744c92526f1e68f77253854c13aa006a825537bf468bbb035ecbb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(CodeConfig, jsii.invoke(self, "bind", [scope]))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''The path to the asset file.'''
        return typing.cast(builtins.str, jsii.get(self, "path"))


@jsii.implements(_IGrantable_71c4f5de)
class BackedDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appsync.BackedDataSource",
):
    '''Abstract AppSync datasource implementation.

    Do not use directly but use subclasses for resource backed datasources
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        props: typing.Union["BackedDataSourceProps", typing.Dict[builtins.str, typing.Any]],
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.EventBridgeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        :param type: the type of the AppSync datasource.
        :param dynamo_db_config: configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (deprecated) configuration for Elasticsearch data source. Default: - No config
        :param event_bridge_config: configuration for EventBridge Datasource. Default: - No config
        :param http_config: configuration for HTTP Datasource. Default: - No config
        :param lambda_config: configuration for Lambda Datasource. Default: - No config
        :param open_search_service_config: configuration for OpenSearch data source. Default: - No config
        :param relational_database_config: configuration for RDS Datasource. Default: - No config
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42501afdb54f6472ab998a801568e1b317b9ee60d07481b1c90ef88e5338ba46)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        extended = ExtendedDataSourceProps(
            type=type,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            event_bridge_config=event_bridge_config,
            http_config=http_config,
            lambda_config=lambda_config,
            open_search_service_config=open_search_service_config,
            relational_database_config=relational_database_config,
        )

        jsii.create(self.__class__, self, [scope, id, props, extended])

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_539bb2fd:
        '''the principal of the data source to be IGrantable.'''
        return typing.cast(_IPrincipal_539bb2fd, jsii.get(self, "grantPrincipal"))


class _BackedDataSourceProxy(
    BackedDataSource,
    jsii.proxy_for(BaseDataSource), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BackedDataSource).__jsii_proxy_class__ = lambda : _BackedDataSourceProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.BackedDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
    },
)
class BackedDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''properties for an AppSync datasource backed by a resource.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            from aws_cdk import aws_iam as iam
            
            # graphql_api: appsync.GraphqlApi
            # role: iam.Role
            
            backed_data_source_props = appsync.BackedDataSourceProps(
                api=graphql_api,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bea2d00276bc1b45e9a26da67eba934f53db82f49e29640aa05289870be94f55)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackedDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamoDbDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.DynamoDbDataSource",
):
    '''An AppSync datasource backed by a DynamoDB table.

    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        table: _ITable_504fd401,
        read_only_access: typing.Optional[builtins.bool] = None,
        use_caller_credentials: typing.Optional[builtins.bool] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param table: The DynamoDB table backing this data source.
        :param read_only_access: Specify whether this DS is read only or has read and write permissions to the DynamoDB table. Default: false
        :param use_caller_credentials: use credentials of caller to access DynamoDB. Default: false
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb501305798213be783a45c59d39c261a182cd09ad0d40d480253e28a2e2438d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DynamoDbDataSourceProps(
            table=table,
            read_only_access=read_only_access,
            use_caller_credentials=use_caller_credentials,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.DynamoDbDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "table": "table",
        "read_only_access": "readOnlyAccess",
        "use_caller_credentials": "useCallerCredentials",
    },
)
class DynamoDbDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        table: _ITable_504fd401,
        read_only_access: typing.Optional[builtins.bool] = None,
        use_caller_credentials: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for an AppSync DynamoDB datasource.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param table: The DynamoDB table backing this data source.
        :param read_only_access: Specify whether this DS is read only or has read and write permissions to the DynamoDB table. Default: false
        :param use_caller_credentials: use credentials of caller to access DynamoDB. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            from aws_cdk import aws_dynamodb as dynamodb
            from aws_cdk import aws_iam as iam
            
            # graphql_api: appsync.GraphqlApi
            # role: iam.Role
            # table: dynamodb.Table
            
            dynamo_db_data_source_props = appsync.DynamoDbDataSourceProps(
                api=graphql_api,
                table=table,
            
                # the properties below are optional
                description="description",
                name="name",
                read_only_access=False,
                service_role=role,
                use_caller_credentials=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2cd0eab2d8bf885992981b7b491d32e73f943353d4564c2a504d3154462a65)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument read_only_access", value=read_only_access, expected_type=type_hints["read_only_access"])
            check_type(argname="argument use_caller_credentials", value=use_caller_credentials, expected_type=type_hints["use_caller_credentials"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "table": table,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role
        if read_only_access is not None:
            self._values["read_only_access"] = read_only_access
        if use_caller_credentials is not None:
            self._values["use_caller_credentials"] = use_caller_credentials

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def table(self) -> _ITable_504fd401:
        '''The DynamoDB table backing this data source.'''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(_ITable_504fd401, result)

    @builtins.property
    def read_only_access(self) -> typing.Optional[builtins.bool]:
        '''Specify whether this DS is read only or has read and write permissions to the DynamoDB table.

        :default: false
        '''
        result = self._values.get("read_only_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_caller_credentials(self) -> typing.Optional[builtins.bool]:
        '''use credentials of caller to access DynamoDB.

        :default: false
        '''
        result = self._values.get("use_caller_credentials")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamoDbDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.ElasticsearchDataSource",
):
    '''(deprecated) An Appsync datasource backed by Elasticsearch.

    :deprecated: - use ``OpenSearchDataSource``

    :stability: deprecated
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        from aws_cdk import aws_elasticsearch as elasticsearch
        from aws_cdk import aws_iam as iam
        
        # domain: elasticsearch.Domain
        # graphql_api: appsync.GraphqlApi
        # role: iam.Role
        
        elasticsearch_data_source = appsync.ElasticsearchDataSource(self, "MyElasticsearchDataSource",
            api=graphql_api,
            domain=domain,
        
            # the properties below are optional
            description="description",
            name="name",
            service_role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain: _IDomain_0c9006b4,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain: (deprecated) The elasticsearch domain containing the endpoint for the data source.
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e54d95c1db8116ebc9ebacf3e6a8c3fa0a47859bc0f72493b58e89411daa904)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ElasticsearchDataSourceProps(
            domain=domain,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.ElasticsearchDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "domain": "domain",
    },
)
class ElasticsearchDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        domain: _IDomain_0c9006b4,
    ) -> None:
        '''(deprecated) Properties for the Elasticsearch Data Source.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param domain: (deprecated) The elasticsearch domain containing the endpoint for the data source.

        :deprecated: - use ``OpenSearchDataSourceProps`` with ``OpenSearchDataSource``

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            from aws_cdk import aws_elasticsearch as elasticsearch
            from aws_cdk import aws_iam as iam
            
            # domain: elasticsearch.Domain
            # graphql_api: appsync.GraphqlApi
            # role: iam.Role
            
            elasticsearch_data_source_props = appsync.ElasticsearchDataSourceProps(
                api=graphql_api,
                domain=domain,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6153bccef60ecdf62438c139adee9ab9afb1c0361813760bad95eae9e5f43975)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "domain": domain,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def domain(self) -> _IDomain_0c9006b4:
        '''(deprecated) The elasticsearch domain containing the endpoint for the data source.

        :stability: deprecated
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(_IDomain_0c9006b4, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventBridgeDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.EventBridgeDataSource",
):
    '''An AppSync datasource backed by EventBridge.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_events as events
        
        
        api = appsync.GraphqlApi(self, "EventBridgeApi",
            name="EventBridgeApi",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.eventbridge.graphql"))
        )
        
        bus = events.EventBus(self, "DestinationEventBus")
        
        data_source = api.add_event_bridge_data_source("NoneDS", bus)
        
        data_source.create_resolver("EventResolver",
            type_name="Mutation",
            field_name="emitEvent",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        event_bus: _IEventBus_88d13111,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param event_bus: The EventBridge EventBus.
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac2aea20ec487bb19cfbb1a301369050ec488bf91096759b3fb3c226c30926c1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EventBridgeDataSourceProps(
            event_bus=event_bus,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.EventBridgeDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "event_bus": "eventBus",
    },
)
class EventBridgeDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        event_bus: _IEventBus_88d13111,
    ) -> None:
        '''Properties for an AppSync EventBridge datasource.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param event_bus: The EventBridge EventBus.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            from aws_cdk import aws_events as events
            from aws_cdk import aws_iam as iam
            
            # event_bus: events.EventBus
            # graphql_api: appsync.GraphqlApi
            # role: iam.Role
            
            event_bridge_data_source_props = appsync.EventBridgeDataSourceProps(
                api=graphql_api,
                event_bus=event_bus,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e00da245f6e9b76ee0cfe04414b7bce864ba4a2790c154b23dc47e4ee33a9f8a)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument event_bus", value=event_bus, expected_type=type_hints["event_bus"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "event_bus": event_bus,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def event_bus(self) -> _IEventBus_88d13111:
        '''The EventBridge EventBus.'''
        result = self._values.get("event_bus")
        assert result is not None, "Required property 'event_bus' is missing"
        return typing.cast(_IEventBus_88d13111, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBridgeDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IGraphqlApi)
class GraphqlApiBase(
    _Resource_45bc6135,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appsync.GraphqlApiBase",
):
    '''Base Class for GraphQL API.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff11ad61ab69f000dc327a3d454c95573a39bc2e7da1972aa306a513e0346484)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _ResourceProps_15a65b4e(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _ITable_504fd401,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> DynamoDbDataSource:
        '''add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5231a54be88b667c5a5a1bc5329dbbb64c8799d82120069adc12366c521a0d7)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast(DynamoDbDataSource, jsii.invoke(self, "addDynamoDbDataSource", [id, table, options]))

    @jsii.member(jsii_name="addElasticsearchDataSource")
    def add_elasticsearch_data_source(
        self,
        id: builtins.str,
        domain: _IDomain_0c9006b4,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> ElasticsearchDataSource:
        '''(deprecated) add a new elasticsearch data source to this API.

        :param id: The data source's id.
        :param domain: The elasticsearch domain for this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :deprecated: - use ``addOpenSearchDataSource``

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72f496dfc677644fac1f40399c0372134a286d0cd64c4afc8c8506b52c9c6842)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast(ElasticsearchDataSource, jsii.invoke(self, "addElasticsearchDataSource", [id, domain, options]))

    @jsii.member(jsii_name="addEventBridgeDataSource")
    def add_event_bridge_data_source(
        self,
        id: builtins.str,
        event_bus: _IEventBus_88d13111,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> EventBridgeDataSource:
        '''Add an EventBridge data source to this api.

        :param id: The data source's id.
        :param event_bus: The EventBridge EventBus on which to put events.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a520f759496ebb7823d10727dc78034711f5090c53ba71c8d7a1dc1848b96e01)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument event_bus", value=event_bus, expected_type=type_hints["event_bus"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast(EventBridgeDataSource, jsii.invoke(self, "addEventBridgeDataSource", [id, event_bus, options]))

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        '''add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0deca16db4175c13560dbb7b3c4aa8cf9a8d20110a58f0ac2ce906dafcc01764)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        options = HttpDataSourceOptions(
            authorization_config=authorization_config,
            description=description,
            name=name,
        )

        return typing.cast("HttpDataSource", jsii.invoke(self, "addHttpDataSource", [id, endpoint, options]))

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _IFunction_6adb0ab8,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        '''add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82b9734a5029f4e20ff30bb852586ba9b413700a9b7453b7113bf1db1efaf29f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("LambdaDataSource", jsii.invoke(self, "addLambdaDataSource", [id, lambda_function, options]))

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> NoneDataSource:
        '''add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41813b6c71fbc2a0901dfef0dd1b464af643898b532103ddead5829c10187ab1)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast(NoneDataSource, jsii.invoke(self, "addNoneDataSource", [id, options]))

    @jsii.member(jsii_name="addOpenSearchDataSource")
    def add_open_search_data_source(
        self,
        id: builtins.str,
        domain: _IDomain_3c13cbdd,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "OpenSearchDataSource":
        '''add a new OpenSearch data source to this API.

        :param id: The data source's id.
        :param domain: The OpenSearch domain for this data source.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e2a17558b2960e621e2eca90fe762c3ea77844a8d87d843ffdbbad8247baaf8)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("OpenSearchDataSource", jsii.invoke(self, "addOpenSearchDataSource", [id, domain, options]))

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        serverless_cluster: _IServerlessCluster_adbbb720,
        secret_store: _ISecret_6e020e6a,
        database_name: typing.Optional[builtins.str] = None,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        '''add a new Rds data source to this API.

        :param id: The data source's id.
        :param serverless_cluster: The serverless cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the serverless cluster.
        :param database_name: The optional name of the database to use within the cluster.
        :param description: The description of the data source. Default: - No description
        :param name: The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c5e408fa29227d2c0f12593dd86151b649a2b97300fea604c91973afef4ab55)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument serverless_cluster", value=serverless_cluster, expected_type=type_hints["serverless_cluster"])
            check_type(argname="argument secret_store", value=secret_store, expected_type=type_hints["secret_store"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("RdsDataSource", jsii.invoke(self, "addRdsDataSource", [id, serverless_cluster, secret_store, database_name, options]))

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(self, construct: _CfnResource_9df397a6) -> builtins.bool:
        '''Add schema dependency if not imported.

        :param construct: the dependee.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3519600d64431e6297911193398dcc136af3b4dd3ec5511d0601a8cbf274f4c)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addSchemaDependency", [construct]))

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        id: builtins.str,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[Code] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        runtime: typing.Optional[FunctionRuntime] = None,
    ) -> Resolver:
        '''creates a new resolver for this datasource and API using the given properties.

        :param id: -
        :param data_source: The data source this resolver is using. Default: - No datasource
        :param field_name: name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param caching_config: The caching configuration for this resolver. Default: - No caching configuration
        :param code: The function code. Default: - no code is used
        :param max_batch_size: The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param runtime: The functions runtime. Default: - no function runtime, VTL mapping templates used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8efe28cf6861260ad6e47a65b8be5e006016a7c27a4ee3f2cac0e898d7f256b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ExtendedResolverProps(
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            code=code,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            runtime=runtime,
        )

        return typing.cast(Resolver, jsii.invoke(self, "createResolver", [id, props]))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    @abc.abstractmethod
    def api_id(self) -> builtins.str:
        '''an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="arn")
    @abc.abstractmethod
    def arn(self) -> builtins.str:
        '''the ARN of the API.'''
        ...


class _GraphqlApiBaseProxy(
    GraphqlApiBase,
    jsii.proxy_for(_Resource_45bc6135), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''the ARN of the API.'''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, GraphqlApiBase).__jsii_proxy_class__ = lambda : _GraphqlApiBaseProxy


class HttpDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.HttpDataSource",
):
    '''An AppSync datasource backed by a http endpoint.

    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "api",
            name="api",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
        )
        
        http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
            name="httpDsWithStepF",
            description="from appsync to StepFunctions Workflow",
            authorization_config=appsync.AwsIamConfig(
                signing_region="us-east-1",
                signing_service_name="states"
            )
        )
        
        http_ds.create_resolver("MutationCallStepFunctionResolver",
            type_name="Mutation",
            field_name="callStepFunction",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param endpoint: The http endpoint.
        :param authorization_config: The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08c251fa7555c0770f24a577dcd59d2f51898cf46299807eda335998d735f187)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HttpDataSourceProps(
            endpoint=endpoint,
            authorization_config=authorization_config,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


class LambdaDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.LambdaDataSource",
):
    '''An AppSync datasource backed by a Lambda function.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_lambda as lambda_
        
        # function_: lambda.Function
        # graphql_api: appsync.GraphqlApi
        # role: iam.Role
        
        lambda_data_source = appsync.LambdaDataSource(self, "MyLambdaDataSource",
            api=graphql_api,
            lambda_function=function_,
        
            # the properties below are optional
            description="description",
            name="name",
            service_role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        lambda_function: _IFunction_6adb0ab8,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e9eb5236f193b30b614aad3d73de37944e1dc26e925a87b1683e07749c2d81)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaDataSourceProps(
            lambda_function=lambda_function,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.LambdaDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "lambda_function": "lambdaFunction",
    },
)
class LambdaDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        lambda_function: _IFunction_6adb0ab8,
    ) -> None:
        '''Properties for an AppSync Lambda datasource.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param lambda_function: The Lambda function to call to interact with this data source.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_lambda as lambda_
            
            # function_: lambda.Function
            # graphql_api: appsync.GraphqlApi
            # role: iam.Role
            
            lambda_data_source_props = appsync.LambdaDataSourceProps(
                api=graphql_api,
                lambda_function=function_,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd360baebe2cc73f8afb0301b4c78dd7e9c49ef5e7f543f97d3ca94cc7c49d3f)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "lambda_function": lambda_function,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def lambda_function(self) -> _IFunction_6adb0ab8:
        '''The Lambda function to call to interact with this data source.'''
        result = self._values.get("lambda_function")
        assert result is not None, "Required property 'lambda_function' is missing"
        return typing.cast(_IFunction_6adb0ab8, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenSearchDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.OpenSearchDataSource",
):
    '''An Appsync datasource backed by OpenSearch.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_opensearchservice as opensearch
        
        # api: appsync.GraphqlApi
        
        
        user = iam.User(self, "User")
        domain = opensearch.Domain(self, "Domain",
            version=opensearch.EngineVersion.OPENSEARCH_2_3,
            removal_policy=RemovalPolicy.DESTROY,
            fine_grained_access_control=opensearch.AdvancedSecurityOptions(master_user_arn=user.user_arn),
            encryption_at_rest=opensearch.EncryptionAtRestOptions(enabled=True),
            node_to_node_encryption=True,
            enforce_https=True
        )
        ds = api.add_open_search_data_source("ds", domain)
        
        ds.create_resolver("QueryGetTestsResolver",
            type_name="Query",
            field_name="getTests",
            request_mapping_template=appsync.MappingTemplate.from_string(JSON.stringify({
                "version": "2017-02-28",
                "operation": "GET",
                "path": "/id/post/_search",
                "params": {
                    "headers": {},
                    "query_string": {},
                    "body": {"from": 0, "size": 50}
                }
            })),
            response_mapping_template=appsync.MappingTemplate.from_string("""[
                    #foreach($entry in $context.result.hits.hits)
                    #if( $velocityCount > 1 ) , #end
                    $utils.toJson($entry.get("_source"))
                    #end
                  ]""")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain: _IDomain_3c13cbdd,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain: The OpenSearch domain containing the endpoint for the data source.
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf111cfb617596222f7a6819bc86667f0aa3335d65397549bc520d302ed052c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = OpenSearchDataSourceProps(
            domain=domain,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.OpenSearchDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "domain": "domain",
    },
)
class OpenSearchDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        domain: _IDomain_3c13cbdd,
    ) -> None:
        '''Properties for the OpenSearch Data Source.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param domain: The OpenSearch domain containing the endpoint for the data source.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_opensearchservice as opensearchservice
            
            # domain: opensearchservice.Domain
            # graphql_api: appsync.GraphqlApi
            # role: iam.Role
            
            open_search_data_source_props = appsync.OpenSearchDataSourceProps(
                api=graphql_api,
                domain=domain,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d43f1439475200e8855550373e564cf774bcfb1c24a9ca37182ca3143b83a31)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "domain": domain,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def domain(self) -> _IDomain_3c13cbdd:
        '''The OpenSearch domain containing the endpoint for the data source.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(_IDomain_3c13cbdd, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenSearchDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartitionKey(
    PrimaryKey,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.PartitionKey",
):
    '''Specifies the assignment to the partition key.

    It can be
    enhanced with the assignment of the sort key.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appsync as appsync
        
        # assign: appsync.Assign
        
        partition_key = appsync.PartitionKey(assign)
    '''

    def __init__(self, pkey: Assign) -> None:
        '''
        :param pkey: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__354d74fae67acb83d442133dee432ed59e1dfd493ad0bee02c5d1b21de9e647d)
            check_type(argname="argument pkey", value=pkey, expected_type=type_hints["pkey"])
        jsii.create(self.__class__, self, [pkey])

    @jsii.member(jsii_name="sort")
    def sort(self, key: builtins.str) -> SortKeyStep:
        '''Allows assigning a value to the sort key.

        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e39eb491b2b69c3a845d6a2414560f3ccf3cf72641d3a92468e82bf545bcf3)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(SortKeyStep, jsii.invoke(self, "sort", [key]))


class RdsDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.RdsDataSource",
):
    '''An AppSync datasource backed by RDS.

    :exampleMetadata: infused

    Example::

        # Build a data source for AppSync to access the database.
        # api: appsync.GraphqlApi
        # Create username and password secret for DB Cluster
        secret = rds.DatabaseSecret(self, "AuroraSecret",
            username="clusteradmin"
        )
        
        # The VPC to place the cluster in
        vpc = ec2.Vpc(self, "AuroraVpc")
        
        # Create the serverless cluster, provide all values needed to customise the database.
        cluster = rds.ServerlessCluster(self, "AuroraCluster",
            engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
            vpc=vpc,
            credentials={"username": "clusteradmin"},
            cluster_identifier="db-endpoint-test",
            default_database_name="demos"
        )
        rds_dS = api.add_rds_data_source("rds", cluster, secret, "demos")
        
        # Set up a resolver for an RDS query.
        rds_dS.create_resolver("QueryGetDemosRdsResolver",
            type_name="Query",
            field_name="getDemosRds",
            request_mapping_template=appsync.MappingTemplate.from_string("""
                  {
                    "version": "2018-05-29",
                    "statements": [
                      "SELECT * FROM demos"
                    ]
                  }
                  """),
            response_mapping_template=appsync.MappingTemplate.from_string("""
                    $utils.toJson($utils.rds.toJsonObject($ctx.result)[0])
                  """)
        )
        
        # Set up a resolver for an RDS mutation.
        rds_dS.create_resolver("MutationAddDemoRdsResolver",
            type_name="Mutation",
            field_name="addDemoRds",
            request_mapping_template=appsync.MappingTemplate.from_string("""
                  {
                    "version": "2018-05-29",
                    "statements": [
                      "INSERT INTO demos VALUES (:id, :version)",
                      "SELECT * WHERE id = :id"
                    ],
                    "variableMap": {
                      ":id": $util.toJson($util.autoId()),
                      ":version": $util.toJson($ctx.args.version)
                    }
                  }
                  """),
            response_mapping_template=appsync.MappingTemplate.from_string("""
                    $utils.toJson($utils.rds.toJsonObject($ctx.result)[1][0])
                  """)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        secret_store: _ISecret_6e020e6a,
        serverless_cluster: _IServerlessCluster_adbbb720,
        database_name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param secret_store: The secret containing the credentials for the database.
        :param serverless_cluster: The serverless cluster to call to interact with this data source.
        :param database_name: The name of the database to use within the cluster. Default: - None
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__568b99c9d3f9eb137243f7121761a99603a4994f00bae5826acff0b7a70dbb25)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RdsDataSourceProps(
            secret_store=secret_store,
            serverless_cluster=serverless_cluster,
            database_name=database_name,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appsync.RdsDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "secret_store": "secretStore",
        "serverless_cluster": "serverlessCluster",
        "database_name": "databaseName",
    },
)
class RdsDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_235f5d8e] = None,
        secret_store: _ISecret_6e020e6a,
        serverless_cluster: _IServerlessCluster_adbbb720,
        database_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for an AppSync RDS datasource.

        :param api: The API to attach this data source to.
        :param description: the description of the data source. Default: - None
        :param name: The name of the data source. Default: - id of data source
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param secret_store: The secret containing the credentials for the database.
        :param serverless_cluster: The serverless cluster to call to interact with this data source.
        :param database_name: The name of the database to use within the cluster. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appsync as appsync
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_rds as rds
            from aws_cdk import aws_secretsmanager as secretsmanager
            
            # graphql_api: appsync.GraphqlApi
            # role: iam.Role
            # secret: secretsmanager.Secret
            # serverless_cluster: rds.ServerlessCluster
            
            rds_data_source_props = appsync.RdsDataSourceProps(
                api=graphql_api,
                secret_store=secret,
                serverless_cluster=serverless_cluster,
            
                # the properties below are optional
                database_name="databaseName",
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c062ac22fbaef687d5273408a83f4b49e1466d504c5d1d22aa7e464c31ce4e9d)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument secret_store", value=secret_store, expected_type=type_hints["secret_store"])
            check_type(argname="argument serverless_cluster", value=serverless_cluster, expected_type=type_hints["serverless_cluster"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "secret_store": secret_store,
            "serverless_cluster": serverless_cluster,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role
        if database_name is not None:
            self._values["database_name"] = database_name

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''The API to attach this data source to.'''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''the description of the data source.

        :default: - None
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data source.

        :default: - id of data source
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def secret_store(self) -> _ISecret_6e020e6a:
        '''The secret containing the credentials for the database.'''
        result = self._values.get("secret_store")
        assert result is not None, "Required property 'secret_store' is missing"
        return typing.cast(_ISecret_6e020e6a, result)

    @builtins.property
    def serverless_cluster(self) -> _IServerlessCluster_adbbb720:
        '''The serverless cluster to call to interact with this data source.'''
        result = self._values.get("serverless_cluster")
        assert result is not None, "Required property 'serverless_cluster' is missing"
        return typing.cast(_IServerlessCluster_adbbb720, result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the database to use within the cluster.

        :default: - None
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GraphqlApi(
    GraphqlApiBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appsync.GraphqlApi",
):
    '''An AppSync GraphQL API.

    :resource: AWS::AppSync::GraphQLApi
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_events as events
        
        
        api = appsync.GraphqlApi(self, "EventBridgeApi",
            name="EventBridgeApi",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.eventbridge.graphql"))
        )
        
        bus = events.EventBus(self, "DestinationEventBus")
        
        data_source = api.add_event_bridge_data_source("NoneDS", bus)
        
        data_source.create_resolver("EventResolver",
            type_name="Mutation",
            field_name="emitEvent",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        schema: ISchema,
        authorization_config: typing.Optional[typing.Union[AuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_name: typing.Optional[typing.Union[DomainOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        log_config: typing.Optional[typing.Union[LogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        visibility: typing.Optional[Visibility] = None,
        xray_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param name: the name of the GraphQL API.
        :param schema: GraphQL schema definition. Specify how you want to define your schema. SchemaFile.fromAsset(filePath: string) allows schema definition through schema.graphql file Default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)
        :param authorization_config: Optional authorization configuration. Default: - API Key authorization
        :param domain_name: The domain name configuration for the GraphQL API. The Route 53 hosted zone and CName DNS record must be configured in addition to this setting to enable custom domain URL Default: - no domain name
        :param log_config: Logging configuration for this api. Default: - None
        :param visibility: A value indicating whether the API is accessible from anywhere (GLOBAL) or can only be access from a VPC (PRIVATE). Default: - GLOBAL
        :param xray_enabled: A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API. Default: - false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdc21261f45618890d843fff7978e6e8e4f4cfe7884c4fffbff6b8dad98036d4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GraphqlApiProps(
            name=name,
            schema=schema,
            authorization_config=authorization_config,
            domain_name=domain_name,
            log_config=log_config,
            visibility=visibility,
            xray_enabled=xray_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromGraphqlApiAttributes")
    @builtins.classmethod
    def from_graphql_api_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        graphql_api_id: builtins.str,
        graphql_api_arn: typing.Optional[builtins.str] = None,
    ) -> IGraphqlApi:
        '''Import a GraphQL API through this function.

        :param scope: scope.
        :param id: id.
        :param graphql_api_id: an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.
        :param graphql_api_arn: the arn for the GraphQL Api. Default: - autogenerated arn
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cefbac91e5bf4b599b8cb612f2e49280f0cab47fab8b476b11f991f6c9f42f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = GraphqlApiAttributes(
            graphql_api_id=graphql_api_id, graphql_api_arn=graphql_api_arn
        )

        return typing.cast(IGraphqlApi, jsii.sinvoke(cls, "fromGraphqlApiAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(self, construct: _CfnResource_9df397a6) -> builtins.bool:
        '''Add schema dependency to a given construct.

        :param construct: the dependee.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fca5d6afc67603703e938a4f127d82a052b1172c6c07cab72c6e3bded9ccd8e9)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addSchemaDependency", [construct]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        resources: IamResource,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Adds an IAM policy statement associated with this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param resources: The set of resources to allow (i.e. ...:[region]:[accountId]:apis/GraphQLId/...).
        :param actions: The actions that should be granted to the principal (i.e. appsync:graphql ).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104e94b5f084bee63e12022802003206eb0917369d9714c4bd16b6175830d883)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, resources, *actions]))

    @jsii.member(jsii_name="grantMutation")
    def grant_mutation(
        self,
        grantee: _IGrantable_71c4f5de,
        *fields: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Adds an IAM policy statement for Mutation access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Mutations (leave blank for all).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a4ce004c83ea63a70a24d83e7decd2ca533063652cd621858a247a616ce82c)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument fields", value=fields, expected_type=typing.Tuple[type_hints["fields"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantMutation", [grantee, *fields]))

    @jsii.member(jsii_name="grantQuery")
    def grant_query(
        self,
        grantee: _IGrantable_71c4f5de,
        *fields: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Adds an IAM policy statement for Query access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Queries (leave blank for all).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__425954c633cc79cdb87065e43764a32551571cca0bdaf65a67a4170d25a651ff)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument fields", value=fields, expected_type=typing.Tuple[type_hints["fields"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantQuery", [grantee, *fields]))

    @jsii.member(jsii_name="grantSubscription")
    def grant_subscription(
        self,
        grantee: _IGrantable_71c4f5de,
        *fields: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Adds an IAM policy statement for Subscription access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Subscriptions (leave blank for all).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__980d951a731ee0c5da0e5b32e9e2870ea1adf06571f857a693decc31a0e959e5)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument fields", value=fields, expected_type=typing.Tuple[type_hints["fields"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantSubscription", [grantee, *fields]))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @builtins.property
    @jsii.member(jsii_name="appSyncDomainName")
    def app_sync_domain_name(self) -> builtins.str:
        '''The AppSyncDomainName of the associated custom domain.'''
        return typing.cast(builtins.str, jsii.get(self, "appSyncDomainName"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''the ARN of the API.'''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="graphqlUrl")
    def graphql_url(self) -> builtins.str:
        '''the URL of the endpoint created by AppSync.

        :attribute: GraphQlUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "graphqlUrl"))

    @builtins.property
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> _ILogGroup_3c4fa718:
        '''the CloudWatch Log Group for this API.'''
        return typing.cast(_ILogGroup_3c4fa718, jsii.get(self, "logGroup"))

    @builtins.property
    @jsii.member(jsii_name="modes")
    def modes(self) -> typing.List[AuthorizationType]:
        '''The Authorization Types for this GraphQL Api.'''
        return typing.cast(typing.List[AuthorizationType], jsii.get(self, "modes"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''the name of the API.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> ISchema:
        '''the schema attached to this api.'''
        return typing.cast(ISchema, jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        '''the configured API key, if present.

        :default: - no api key
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))


__all__ = [
    "ApiKeyConfig",
    "AppsyncFunction",
    "AppsyncFunctionAttributes",
    "AppsyncFunctionProps",
    "AssetCode",
    "Assign",
    "AttributeValues",
    "AttributeValuesStep",
    "AuthorizationConfig",
    "AuthorizationMode",
    "AuthorizationType",
    "AwsIamConfig",
    "BackedDataSource",
    "BackedDataSourceProps",
    "BaseAppsyncFunctionProps",
    "BaseDataSource",
    "BaseDataSourceProps",
    "BaseResolverProps",
    "CachingConfig",
    "CfnApiCache",
    "CfnApiCacheProps",
    "CfnApiKey",
    "CfnApiKeyProps",
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnDomainName",
    "CfnDomainNameApiAssociation",
    "CfnDomainNameApiAssociationProps",
    "CfnDomainNameProps",
    "CfnFunctionConfiguration",
    "CfnFunctionConfigurationProps",
    "CfnGraphQLApi",
    "CfnGraphQLApiProps",
    "CfnGraphQLSchema",
    "CfnGraphQLSchemaProps",
    "CfnResolver",
    "CfnResolverProps",
    "CfnSourceApiAssociation",
    "CfnSourceApiAssociationProps",
    "Code",
    "CodeConfig",
    "DataSourceOptions",
    "DomainOptions",
    "DynamoDbDataSource",
    "DynamoDbDataSourceProps",
    "ElasticsearchDataSource",
    "ElasticsearchDataSourceProps",
    "EventBridgeDataSource",
    "EventBridgeDataSourceProps",
    "ExtendedDataSourceProps",
    "ExtendedResolverProps",
    "FieldLogLevel",
    "FunctionRuntime",
    "FunctionRuntimeFamily",
    "GraphqlApi",
    "GraphqlApiAttributes",
    "GraphqlApiBase",
    "GraphqlApiProps",
    "HttpDataSource",
    "HttpDataSourceOptions",
    "HttpDataSourceProps",
    "IAppsyncFunction",
    "IGraphqlApi",
    "ISchema",
    "ISchemaConfig",
    "IamResource",
    "InlineCode",
    "KeyCondition",
    "LambdaAuthorizerConfig",
    "LambdaDataSource",
    "LambdaDataSourceProps",
    "LogConfig",
    "MappingTemplate",
    "NoneDataSource",
    "NoneDataSourceProps",
    "OpenIdConnectConfig",
    "OpenSearchDataSource",
    "OpenSearchDataSourceProps",
    "PartitionKey",
    "PartitionKeyStep",
    "PrimaryKey",
    "RdsDataSource",
    "RdsDataSourceProps",
    "Resolver",
    "ResolverProps",
    "RuntimeConfig",
    "SchemaBindOptions",
    "SchemaFile",
    "SchemaProps",
    "SortKeyStep",
    "UserPoolConfig",
    "UserPoolDefaultAction",
    "Values",
    "Visibility",
]

publication.publish()

def _typecheckingstub__c93430f25b9bddda38ab6ed4aef73a01d531a0771aae76b4cfb91f728f6bf481(
    *,
    description: typing.Optional[builtins.str] = None,
    expires: typing.Optional[_Expiration_059d47d0] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c51d586a70a9312cc6dc1bcaca432f8e4313a345a99746b530ac39c8c1a0b1e9(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a3a190d436a13eb112207de457ad9f7fd2e55f6583487ccf52156a53c1d722(
    attr: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e61f1f15d49fba8455a2391e89ab0bf2272bdaccb9f4a3f46553b6dc028a6906(
    map: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cd6bac98a2ebc52d96453f79a721a0c363c5fc6df8ea75a47fa176faa7777ee(
    container: builtins.str,
    assignments: typing.Optional[typing.Sequence[Assign]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348b35818af6fe397d44e0c92f06b11e8fd640ebd03a9ab3bcfffac868848b75(
    attr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b74367d2b39a3674c17cec74e25e06759911e6f340e5fdd2523bbbf0757dbe9(
    attr: builtins.str,
    container: builtins.str,
    assignments: typing.Sequence[Assign],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64a719217ebf2092e4a0c549e44dc18cc9048616951d288cac498e6fad568460(
    val: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9412a3d926721362a9a66e6d3efd8ded83f98dac5a7e8438d94370bd2b8ba60(
    *,
    additional_authorization_modes: typing.Optional[typing.Sequence[typing.Union[AuthorizationMode, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_authorization: typing.Optional[typing.Union[AuthorizationMode, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d567ebb81cf9cc165ffbb174514dfd4819c43b13e22fccb43f780087025e6328(
    *,
    authorization_type: AuthorizationType,
    api_key_config: typing.Optional[typing.Union[ApiKeyConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_authorizer_config: typing.Optional[typing.Union[LambdaAuthorizerConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    open_id_connect_config: typing.Optional[typing.Union[OpenIdConnectConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    user_pool_config: typing.Optional[typing.Union[UserPoolConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9ee7c043bccdcf612d17f9ba452092af17fda0b30d98fab02fc5a652b9a6d7(
    *,
    signing_region: builtins.str,
    signing_service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2edba60cc5d74f665d36e54af7d66189cc66d09566e817ef416a2e8fc0de2b(
    *,
    name: builtins.str,
    code: typing.Optional[Code] = None,
    description: typing.Optional[builtins.str] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccef8522d3c5565fafba1e5a9b621b9169239e6ce41ea1275f6a59935927b401(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    props: typing.Union[BackedDataSourceProps, typing.Dict[builtins.str, typing.Any]],
    *,
    type: builtins.str,
    dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.EventBridgeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4fc8f5bee0df00790320083fe0cca74ef85fb43651df9418be27e2a1ee3eaf1(
    id: builtins.str,
    *,
    name: builtins.str,
    code: typing.Optional[Code] = None,
    description: typing.Optional[builtins.str] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18da570994550f3efc007c557f3b52f15c9a82fb4ef611b37d526d983c934ec6(
    id: builtins.str,
    *,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[Code] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0fdd82cd5eb579a9b83ebfabb3938ef1f107e8210133366c4dfd46d6b05adb4(
    value: IGraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f22d536d795f0e6c3516e56fbc4183ece0daab0d19c19d86752c9fd35a21d310(
    value: typing.Optional[_IRole_235f5d8e],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cb5694e7bccdac081c0d35fee8d239110cc5fb8b7eefac7866144f6deac2d9d(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57bca2ee49335be042ebfd66ab492a766a7dcba63ae9692b50ecab067c20e80f(
    *,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[Code] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16c48e7a47c60140291c83d5eea69a6e25ec7462e7a0080eaf553e500e9ac06e(
    *,
    ttl: _Duration_4839e8c3,
    caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9d92b7b2abdac7341eb92f7ac10d2d67dd2700af68eaf42c72c47ffdaacc344(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_caching_behavior: builtins.str,
    api_id: builtins.str,
    ttl: jsii.Number,
    type: builtins.str,
    at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142193172b7ee1304f3b8fd949531b4cfa950ea62d0dc10f9ed5a184a603132d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce863b5f21a86ce886458054cd4de0550269c18eb7c4f3fb37884dc2869845e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee6b3576fbf654864dae4f55fe292d210bf01534f16f80af0ac225f8fa338c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2fdac623dbaddb2a0226d75e6f3ca84c058f3f46b9c9a1289820c1cf0827e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1893b7ba08236941b8e5bb4704e7fe53f8819086085796443b5d68f513e66eaa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45dc491e21920c6cd0ddecd9aada80283ac759d9eaca52c45a6ce35197166e9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a4abe242f634763c1f128b7e17017d1176924c9b032d5536f4caa3b3fc3bd6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb39499095e917401c885f7c77781744d09df071b1ed62c6f2c32cbbc6fbdb33(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f054fa3186eb5f122c20e523bed485713c72511ee3ee94be25733ecad9a348c(
    *,
    api_caching_behavior: builtins.str,
    api_id: builtins.str,
    ttl: jsii.Number,
    type: builtins.str,
    at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6065dd18c9d420fd4fcd70aced8416006f044f82aecff54150165e832539a8e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    api_key_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    expires: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8f02bc91fc0b32c990b8d08a5d7a0ef78a88363920fa69d4196dcc7f2ecfb3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a844b496712966f29aae49f2f831e6a85c7acf03c2ce61c94162ccf13c5efd6d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1cce5f76a6037620e1cc2e57750c81cc5161ff526ce78123f0cd9f25c8e856(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5d6818eefb673237292bb9320e2134ad0c799f70d17a7cba2de3f4298ccf5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08afa042939638da41f04c7165f811f5081bd3c8943f787591f098aa4a3b8699(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b034facb88dea82241969fd1a22a5bbaccf03068403021106e073c92112ab45(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1688db2b7835c85b4e2cd69655b5d25321ff2aa2ea9e1b2a0612caff34184549(
    *,
    api_id: builtins.str,
    api_key_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    expires: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2dc8968068d09d9cb599cea5efad1a18016c4eca4fcc6c15e6169a0891e2678(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.EventBridgeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844d45e22564aca7d878e00ff3e6a39f30d70312a9d2fcf8bb2f587b070069f7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb33982b2405feec8337a5b841ef30f58e28ed8058a2e3d003d09ee8aac516a9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7863787830eb114a9c03188cb3a3bfd0b865645dac5dd0d3cf0b374c0a1af6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba82e0d60919163b242fed29c81421c4160f75a79249e58ce74b20f6b7d0f03d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aae6a5f086f2d2c36e8dff3cce5906d962da71d7148d7feec996abb025fb8f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29cebb36b12bc9cd3423d5991aeea26c635c2541d63fc9c3309a2177c24f1118(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffaca3e4a18d434a01277621d6792259ab70047809af34a6cb0bab3eb7886a2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DynamoDBConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5323c0bb4d330a2f6b24616dd2b47847aa913d75611ddeae3cc451eda7ebb774(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ElasticsearchConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9aedfd6520add851a257d524d2bcb0a45552a7b99af805456bde2779e658d15(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.EventBridgeConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b1129f048e5b946eceb4eb9c372f68c9a28e32ebe6091b611c3b1b82e3e83d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.HttpConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ff8b510d0035620c1325857ec673c802695c9f3c8dd8fa109d1b44e652a641(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.LambdaConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__876dd6f7515f1b03442f4aa7a0d78d1d6e5eef401db8d851e96b713bd30f989e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.OpenSearchServiceConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72a1c504ec56f95938bf0b2a05d96acc7eb4b1190dc7285e9c33b6b194318386(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RelationalDatabaseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8d23554bf1b07da4d8bb262596b409805d205b461615d34726f3323315abb2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b40b2b6b828a39a91cb37d699b9dccbe36d457b235d0c89f8d63a8c926a5443(
    *,
    authorization_type: builtins.str,
    aws_iam_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.AwsIamConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d3d6847bbd8b570bb51728b12402301a578fc159522a9bb797a8042b7c43dd(
    *,
    signing_region: typing.Optional[builtins.str] = None,
    signing_service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d8409bee2e379adfba84b9eedc28876ceca73a2b15ec9ad3045f33dc08a849c(
    *,
    base_table_ttl: builtins.str,
    delta_sync_table_name: builtins.str,
    delta_sync_table_ttl: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66016c117898c1cc0dc84bb648ce56335f475ea29f1590882ca3229c1e8ffe3f(
    *,
    aws_region: builtins.str,
    table_name: builtins.str,
    delta_sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DeltaSyncConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_caller_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    versioned: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7385ec04703540fe726bf7efc36f7ea05ba851b02e63ee657ec6cba21c5e805(
    *,
    aws_region: builtins.str,
    endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659279c711a228092290e57ba8e5c0b54e147a7101bfeed551b80c8e7bcdb985(
    *,
    event_bus_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4a6ece9757475b2fd78d8a95bd18c7fd68758c889cf5d07cea125e31a32258(
    *,
    endpoint: builtins.str,
    authorization_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.AuthorizationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ae7467c676f94be4511c7fb68e47ed5c3c90dde218c9a12592924c98f7837e(
    *,
    lambda_function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fecf5845831a0e0a203174a1662e533c942ecf67ea1e85e246e7a029865de49(
    *,
    aws_region: builtins.str,
    endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348849422fd4d08e7490da175f7a5ffa84cad62dcd8d49557a3436740b3dffd5(
    *,
    aws_region: builtins.str,
    aws_secret_store_arn: builtins.str,
    db_cluster_identifier: builtins.str,
    database_name: typing.Optional[builtins.str] = None,
    schema: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4357a1467126648487c710ab6683bf4d3954927d7c54c51b699c6f185a943236(
    *,
    relational_database_source_type: builtins.str,
    rds_http_endpoint_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RdsHttpEndpointConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a27321db4878d92375c672ad2fd1de24e61150d04b9a9b7f544b60bf81d6d7(
    *,
    api_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.EventBridgeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678693553586e835af6ffdc6ac5860f81ffd96791de73368d44d41d3a220fa5b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_arn: builtins.str,
    domain_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1bb36f58b6037c649f6de5b27bf9555b52f554bb5fe4108f80d1e6143cb6f24(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a3cf8beadfc199c9c9d148139af66f311d5dbd310ca59a7062e7f26c40c037(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21881e6a0cbde3bc434364c90ea094d149b2b6df42d7fc1beaa6dc2b7dfe9eca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d87464e3fb9b21e5511a8f5b32d36667e3c9d7faaf4d9cd05b6f5a75145649f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc72a5388fe698c3e3240ed821a6e614471584c2ffb80f06028269bf9d78d46e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053707dba2452392a89bf081ac7d866beeff7c348bacbfe351a815a6372a43d5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__942757d7ea72d07c8e5e78524b0a4e08dae920c7a26e14bfd77a565345201d36(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03652b1dc4a3294dad3ea732f92fa774dc0eda1cb1fe6263bac9fe9718f6e63b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1373752dfc88f0800245faefb7696b22aadcc994b58e7c2c57cd7f058ad814b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dd7f18cf3cb236d2ffa804f6505477d416e7b844f92f9ba86f74aea18663216(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a899ca55570211a5da411a83f28448dd1e54a82a4e83cb8d8ca2b1f292ebf5(
    *,
    api_id: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b0d09d8c1a97bdb5c0b0b95b798fbeb11f45abb25769bdb71d1903471361a5c(
    *,
    certificate_arn: builtins.str,
    domain_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a4866dafc094db4e3a18f26e71e3f210828f39f8958d47fe2d4c085adc6ff8f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    data_source_name: builtins.str,
    name: builtins.str,
    code: typing.Optional[builtins.str] = None,
    code_s3_location: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    function_version: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionConfiguration.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b5daa219cb13e40ed1b20203fde593fe20c2c92bd36d7a071b49bcec839439b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f15942d1b688b5a1072d376a057d8302c1e87743f5a5200ad9fc3b45987f7a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddada6f46239ab33eec4921b4ac0cf9484ba0c89258d9ca8117a0ecf69c7631a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9493c684f0dde1a9223d5146974c138d33dbf89e0c56ed8d6d23f69b357bcde1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bcf772bf0a6d98d280769ee4b3e0c374a4881be9dfcc56425285f343d8c9a87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f176cd8f4e930d504d5f35fb87b141d2a2d197149a0763d630b94186516de330(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e20f51155c39c20c83124659b8133fc87948adf8035794534cadf37a3e7265e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e87fe0dd6ec9c662347f3659e76d0bd6308df654c93fd61f384e0c29e5eb24b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b218cd4f3808007654247768d1242189a48a8632f1621b5b37ab5e4ccc0f4a9c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9abf526bb6e39ee9360616d137b1625f90523f036a39b05e1cf79037baad4f63(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96a54d609ccde1c57b832776c4db93d393395273ac718e900a8503eaeb43283e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1031c7b0aa54c899315716446946b7d1e3385d7b3fb6f6d1d31ea4f653ad3cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45788eaccf27f4038c701605c623bce576d7990af5337245691eb20581091c26(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b40fcc0e01043cbd9cdf55c416d462b00a65d35ca5fdef3bfa9d0b412afbb19(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143abf7cef16b0a5749a28fb00575ff2cb3a1f027e142a59f5e914c1776d09fc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionConfiguration.AppSyncRuntimeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d1624e61da41b1be885253dc0b667a61deba82d80481d4d6a6b5430b507b05(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunctionConfiguration.SyncConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b82405295f439f31600277f9055bf514ac45e79afd73f5b14450b84beac6e5c(
    *,
    name: builtins.str,
    runtime_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e67576fdd79515010563035ffc15df29a57e00be079931631598d07f7178f0c3(
    *,
    lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__441bd762beaec70fd67cf86d84e674beae78bf0e9f78d94f1b683b403e7b47f1(
    *,
    conflict_detection: builtins.str,
    conflict_handler: typing.Optional[builtins.str] = None,
    lambda_conflict_handler_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68fb3836c61478b4bf652995d052fa027e6b2f6b9606529969b49a74037c3061(
    *,
    api_id: builtins.str,
    data_source_name: builtins.str,
    name: builtins.str,
    code: typing.Optional[builtins.str] = None,
    code_s3_location: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    function_version: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionConfiguration.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunctionConfiguration.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54e0e0488820e5a410f75b28895d4271db1e58bd6c71e17fd04fcf3fad8696a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authentication_type: builtins.str,
    name: builtins.str,
    additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    api_type: typing.Optional[builtins.str] = None,
    lambda_authorizer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.LogConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    merged_api_execution_role_arn: typing.Optional[builtins.str] = None,
    open_id_connect_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    owner_contact: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_pool_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.UserPoolConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    visibility: typing.Optional[builtins.str] = None,
    xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef4f44613a72787cd83e4ceef509edefaabdb020300442c1eeb53ff3e20f525(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea2cc823b2c4f8c7f428fa2f0fe71c624a069d90ef8d4385d598404adbc586eb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf538537f9f940e10be3bb6aba02fdfaf8dc4a1cd2d9271f52eb0cc89a879de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6a61daae035f26bd4c76cf79a3d576be1077bd308cfbd0ecde402238ce095e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d98241da3432e0393c78db49e66414c7e91e9bfc9e19f06380f6b18215ab489(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.AdditionalAuthenticationProviderProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__368741733832ba6f2bd8963ff6065a1471cd003f84d5567a1b4ac4e31f866fa4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ceade9d24f423834d3485476af5c7e3bd2e0ea0899583af5ac44f01e70b244(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.LambdaAuthorizerConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c0d15f646c5975aec4d344a5e6150a6fec6655df6d4354b817aef3ce9053464(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.LogConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a871b44b3bee02deb37b3334dce3879c119dd687537efd2eea807744ffb2d34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf051032d1109f154a4b02f8368044e2e1266c9008da417ccef7aa84293cc125(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.OpenIDConnectConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e99145104b4c7d697f40bb2242cf89f15fb4638f7c19d492e1c5813994e82d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b6bd673e24289c51e9fb96c96f3ee2bf2f7af27ef9ebcc4ae16d3cdee34b6d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d04f36c4d7d5f26bce761153a8d93212a34634f3833d3080b56cdd7a05e70b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGraphQLApi.UserPoolConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f56ad4ee938b5ce91c10b6490094e6f1986e84540a95b138577851adf6e569a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__863eb629614a817210cd5e0eb8ae7d3264658e2121ad2529a6090b38cd038199(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8233eaa1ce5aeb807b7fe9374215f842f67afc12ed29dcbdf6773df7cd328a4(
    *,
    authentication_type: builtins.str,
    lambda_authorizer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_id_connect_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_pool_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.CognitoUserPoolConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b5c78d0d6cf8f2e5de126a1b379f17cb44634afea4439cb4b2b3c893dee502(
    *,
    app_id_client_regex: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    user_pool_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f9291a235c0bd7ecea6f37d1aa830ec180ae9518e0555f8a98722d8088b1895(
    *,
    authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
    authorizer_uri: typing.Optional[builtins.str] = None,
    identity_validation_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9ff7e1cb756f4b27770bf07bfb18b0936eea6dc27410d5c20b3b259d960d7a3(
    *,
    cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
    exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    field_log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e62ce520030272762ccf6169ce5673be0610bd412fd2d9b9a3a7c7963d4853(
    *,
    auth_ttl: typing.Optional[jsii.Number] = None,
    client_id: typing.Optional[builtins.str] = None,
    iat_ttl: typing.Optional[jsii.Number] = None,
    issuer: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f0d0849f2d6ffc2b4b6a4eabed8e631f4ae22772572c4eae3d63c7ec6f2a4a4(
    *,
    app_id_client_regex: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    default_action: typing.Optional[builtins.str] = None,
    user_pool_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c30fb6e2b0bf2994b166c6091173ca1bbdf2a226ff26da5bfc0c35067fc8cc07(
    *,
    authentication_type: builtins.str,
    name: builtins.str,
    additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    api_type: typing.Optional[builtins.str] = None,
    lambda_authorizer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.LambdaAuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.LogConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    merged_api_execution_role_arn: typing.Optional[builtins.str] = None,
    open_id_connect_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    owner_contact: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_pool_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGraphQLApi.UserPoolConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    visibility: typing.Optional[builtins.str] = None,
    xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86eeb90bbb1ca5a453f08cfb90f5fb16cf4842431fc90d63f3ee21972f1be243(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    definition: typing.Optional[builtins.str] = None,
    definition_s3_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6052290b218f085df44320d030dc5da2a656bc2dfb652a6e8997c198d7360074(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e7b1316522ac1b9a93d87179eb23379f7762341da46fd001056a8704a20b2c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__555a23d4ba449beaaf98ed745a155165b6830286b0aeae2a45d326885e8eddef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29a3a5e0c95af4007408f43ded6d8b16b50975200325f9066820c3302d03398(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4848140e56b16e4736cedb1aa2fb1ca3fd82aeca7e977c876274b365740b08de(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20c7b2f1eadba8a608fdb8a0a590a3907eb9c891f22a7385f17ef74294ca1d0c(
    *,
    api_id: builtins.str,
    definition: typing.Optional[builtins.str] = None,
    definition_s3_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a19b37f9f570b32d81c1e70bfcb51be048fdffa3df94ad801e69b812f746f8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.CachingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    code: typing.Optional[builtins.str] = None,
    code_s3_location: typing.Optional[builtins.str] = None,
    data_source_name: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.PipelineConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95aca731304382cdf3dcd502764afa9c3fa4887077a0e30a6874db561995ccfa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313f8d86637162de96ee41aad99883afe32469196f904fb4309e0e9e33fc98ba(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472e69750f14de2abe38ed65522399a06e502ba89a0b921571c0b2746c638e5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2233218403900cf6b8a69c999e792511fca483ed05d2fa4306e0d7b2535010(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c08751b4795b139490b95abf3b3d0f17260bfea4a916f1afbaf08d435cfa21d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6b9e8b849504be748695ce685546b844451460e25485772ca066bc2b65f61b1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.CachingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0dd83b21d0fde771732f3fdf63588b717c979c6ab095248970576c0a297e97d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd67bb7c14d4f8040b88b7d1c29031ed6038b21c10f80e4f0fcfd6c31af45cbd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d90421590c8dc3a0c283260b096db2cd054cf3d6852e741d1bfaf1bf52bbe597(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf560aa0e5a28a8ed71b1579e183bb6fb81cf53b398565d4fe06e8b7cfb4b31(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66d0a40a93385979fce12d901f6a195637584cfcb71b3a04c20d8333f0a582bf(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6c98074ee2ebbe5b451fe5513433aa3557366ed040722d6e61328ab781da16(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.PipelineConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd82effb0edb94da2492c911c5aecbe1fa5f2d88b6066513bb7f2a5713fdca7d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd52da508686e9da63db3673bad91680eaa1eb468984c1b4f57757668dcaed40(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f24f835e9a5b9af73089ccb61dfcf176cc230bb0feddf60b73360bab083e3f46(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a067b0164755508220ca8ad5f24cbd5ac6d6c57fb44d8404b14392f12d372f0c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a14449468f6ed96319993479a0ae9b3feacd27ec17e068d4d17ce598a964715(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.AppSyncRuntimeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a111110922e122a02d7d649fe2daaa4c4d7cf1709e2078b92fe101fd93d8e4f5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResolver.SyncConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d69cd55f1989ce956af7a1058706bfd4aaeba608d00146e50a90c1d3521cee0(
    *,
    name: builtins.str,
    runtime_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5089c8cac20eb98ddb2d855ec469e09dc0f7b1141ddaf4de8fd19eaaadac7891(
    *,
    ttl: jsii.Number,
    caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8760098edd4885448deb6a9ceb1ba3eb5367683995fadd12b5e5f3bf1e2fdd7e(
    *,
    lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2907a70554c3df66e94c41c4e36342a2860e214a5b7da358efbe204221066961(
    *,
    functions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd8efb0c43d72e5061a7c9c3de6483787260ccff8a3dff5a5152ca959d6af6a3(
    *,
    conflict_detection: builtins.str,
    conflict_handler: typing.Optional[builtins.str] = None,
    lambda_conflict_handler_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.LambdaConflictHandlerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b1ba8346de8783ad38f1a2377fd50bdd7577d903f4b68402c7b5ab604f16e5(
    *,
    api_id: builtins.str,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.CachingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    code: typing.Optional[builtins.str] = None,
    code_s3_location: typing.Optional[builtins.str] = None,
    data_source_name: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.PipelineConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.AppSyncRuntimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sync_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResolver.SyncConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a3927d7055c6f07f6fda98012e654caed4acd1cc6ba02f45817c51587aaea2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    merged_api_identifier: typing.Optional[builtins.str] = None,
    source_api_association_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSourceApiAssociation.SourceApiAssociationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_api_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8118984adcd2c3e9c43587a073297de4bd1e174d46854dc5e69d06013b9c2c97(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3e97069634a5275cdcce711a054061c3991a3588f8b476f3a6c300a0062016c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c33f6c1609e5ea2fea0dc3149db2bb427e4e90e05aebc176b6f270f52a7f880c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37d248fdd83c372d8504ccedc8ceeff98fd9085da37f45ffdc582051a1c82aab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a343d8ede31db66fa4c54360086ddf77c88c05a902c3cdd250198db59eb0ee5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSourceApiAssociation.SourceApiAssociationConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce9bcd8d95a3bc0ef84a2eb38f1500af0d6743e3f33026a5037a1af930c33d30(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62f3cd07f6e7086711e43c45ec65e051608b1d33e97dcfb24df40b8772736964(
    *,
    merge_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c56eff105c0c6b1b0bd618bef1559d9327ee250f666604ae39798783d3370a3a(
    *,
    description: typing.Optional[builtins.str] = None,
    merged_api_identifier: typing.Optional[builtins.str] = None,
    source_api_association_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSourceApiAssociation.SourceApiAssociationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_api_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eafa9f4fd31cdfcc23e497d115c1733ce980674eb036dad379eb9102290ec01(
    path: builtins.str,
    *,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
    bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d01668387a22003f3b94de6761b2ee76842b637cecef060a14da2befa820605d(
    code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999382669090951c71805838301c048a01730773d994c4fbcc12cee3d8666cf6(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5abf436f692efcaed424f8bc2738e56e16abc84b9ca36c4963add4e94cf6449(
    *,
    inline_code: typing.Optional[builtins.str] = None,
    s3_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931a67471fe69ef52bd3bdb1d3123eda90d2919ed8b825ab147e1db8ee9b4607(
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__666cedee7b74b7e32381dd1603bff8d92b24dd381d5f493f478126fb394ef687(
    *,
    certificate: _ICertificate_c194c70b,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea6d91c7460c0aa163c28990cc189d68d54dd762bf2b0c703c347e80a74f98a(
    *,
    type: builtins.str,
    dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.EventBridgeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dc3b87bcc5a5c4f72f5701decf293d0da2caba80281cf58c26e7a4d9ed20fd7(
    *,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[Code] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
    data_source: typing.Optional[BaseDataSource] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b62634a47ff9294fb4979bf7d3b55dfb2f791b9cad75a7193946ff54e2953c(
    family: FunctionRuntimeFamily,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1fc91e210b45240155885dae82dd53ddc084048aae2724cd942ec7c5202c10(
    *,
    graphql_api_id: builtins.str,
    graphql_api_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ac2113ba86b3a60344e56ee0c5bb6cdf1bc20cd0d5aa52f9a94709feb99e1b(
    *,
    name: builtins.str,
    schema: ISchema,
    authorization_config: typing.Optional[typing.Union[AuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_name: typing.Optional[typing.Union[DomainOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    log_config: typing.Optional[typing.Union[LogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    visibility: typing.Optional[Visibility] = None,
    xray_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__892de8c32b5ee5c6cb5e65bc4b597f67297f1f675b608821b733eb9599975405(
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91183bd6fd5a10b6ae91fe2450b1ca1b99e291ac5b272e3c6ccfffaa26a2b05a(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    endpoint: builtins.str,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43da9ca276f601968eabc2575ce6745ba4152bbf47201270933feda5452ce68a(
    id: builtins.str,
    table: _ITable_504fd401,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d976a6c9cea09ad6131d004dd38bbab6c2059e80a1a41697431f21da733851ef(
    id: builtins.str,
    domain: _IDomain_0c9006b4,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f859036563760af3f55f190f35d263357d6df8725cd3d3990a639dc02796df(
    id: builtins.str,
    event_bus: _IEventBus_88d13111,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a5ae312823194eb5a4a37d99f965046bb8750ad62c67b536c7378744591071(
    id: builtins.str,
    endpoint: builtins.str,
    *,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49c24df9542a2559af242eb252634947ce0ed3aa9d4e4efca32b6db37271ef48(
    id: builtins.str,
    lambda_function: _IFunction_6adb0ab8,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa2890745bf86976bff5a0152fe1757b4534eabb56973b08a45c2c539adc58d(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e51c29583b8567298ff7b528e3996298135787d4fbe5dfe686b388500e8ce53(
    id: builtins.str,
    domain: _IDomain_3c13cbdd,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00411b1875c06ea0450c7cb3f4f4dbd07f2f28986d7180e3a06f5ea235641679(
    id: builtins.str,
    serverless_cluster: _IServerlessCluster_adbbb720,
    secret_store: _ISecret_6e020e6a,
    database_name: typing.Optional[builtins.str] = None,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7845da8546318a24ccdcc5b7669f4273b997f01e1807a63aae7beabbe99b178b(
    construct: _CfnResource_9df397a6,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1231d659a3d5f86849b39ea5e3924e5d6867178b9b48617ec80686588387ac(
    id: builtins.str,
    *,
    data_source: typing.Optional[BaseDataSource] = None,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[Code] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ab7bd2a4f271f294370de26c1f7a13edd4a7e586c474d1ce0d7c4b532ad79a5(
    api: IGraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7394e47c73f9dbf60d57fa33fdbf7af98d828fabd51c4670bd5acc1cd4b653b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a58b3bfbb8f3147e1915d76419b3d10f5232745190dda75c89309c09daa598df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__486fba677a06e1d2f86de3d1bfebdc816a08fdb75280a8c7778fcb2d186723db(
    *arns: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ef3ffd4a7e1a514f99330034c53323b9d1884fe72b84846ee2c9b3bd34ce84(
    type: builtins.str,
    *fields: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd39c5d442ee7ade433a10992f6a94e24818b16e448af33f399f02d21d4532a6(
    api: GraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e00df94df91e7d536755d93e1e2969ac7ef87855b860cb5fc2d4ad7545f013(
    code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83acb173a79e10774f37e4699441474aba7a06c89753cc8bbc811841fb968a5a(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be31cec85c5d6e8d84a1ff6120f28763539905417cd2f90518c2486794627fd(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f36a295e481a13f223776e0fc0091431083d5103e086745aac3a7742a3f266c(
    key_name: builtins.str,
    arg1: builtins.str,
    arg2: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c3d89a9e0dfcb30290ceb9cf53e14011e8b3847ee2ddff39ec1455d377c466(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ae3f2f70bd8308fde66d04db7159818ce15f3d5eb9bdceffafe033ad76263fe(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e58baab7b37668816dd9d41eab697b6f94271aba9923b84d3423efe91daa733e(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c12ca3fbbf83507d43081a8b4c0321290e7c340883b8919107e08ee2d500856b(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f32b8919c697477f7851076a245af3b8d4d8b30d2661db1ade267c92ddc6866a(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__841cb23f43ce7bfe91ae9e27a40b958f6c4d4c8a01a675d5e452889ba1c5639d(
    key_cond: KeyCondition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85bd76d9345653fd1813036904e3edadb83b6c1c51d38e8234237345dc3773dd(
    *,
    handler: _IFunction_6adb0ab8,
    results_cache_ttl: typing.Optional[_Duration_4839e8c3] = None,
    validation_regex: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d73860e597bcfca4336f77cac0c6ce67113883e4171d802987f80c349fd909d1(
    *,
    exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    field_log_level: typing.Optional[FieldLogLevel] = None,
    retention: typing.Optional[_RetentionDays_070f99f0] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8039f0676302cd6a9ab028032df416cedee74a1e034ef40aa741c05a635901f(
    key_name: builtins.str,
    id_arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed2d1bc991a539021943757343be2d737ab814fed8178ebe300c8db10b0987b(
    key_name: builtins.str,
    id_arg: builtins.str,
    consistent_read: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f6e0c226f78611f34b78ab0e1d8991442c728d76763ffe43986e41363e71217(
    key: PrimaryKey,
    values: AttributeValues,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c051303dcbf7aca274ccea310cfa57f3f39591bfc2b9d5833a2a6a135af6394d(
    cond: KeyCondition,
    index_name: typing.Optional[builtins.str] = None,
    consistent_read: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6a8a228010e1e6327b0d1f8956027d8ff0cb28b0f4fb4c95753b3aaea58f729(
    consistent_read: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e01baf3340cd576c62786da8e2ad0c983ebdbad06b932b7de57a46f6e48fd0(
    file_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bac5b3ede51565e6835fed423e0a1e7f8e87f0cf2454f06ff0c5aa9c3bcd804(
    template: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3b43f41b3eaa9c822ef11e6a8987a60daa66f2982d2ea77dfae0ce5eaec49c0(
    payload: typing.Optional[builtins.str] = None,
    operation: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1611db7d560b46fd4ac561a4c80f0c620482391b0a4b50a2e95caca4f5e07e31(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f714cd165303e3c7148f1ca4c53fe5e7abe0f744c242bcdbb8dc5817bd63ecda(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e8ab4c6015808cd4bb9ca15d799fa7c987da055820136f0a938859823c20863(
    *,
    oidc_provider: builtins.str,
    client_id: typing.Optional[builtins.str] = None,
    token_expiry_from_auth: typing.Optional[jsii.Number] = None,
    token_expiry_from_issue: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab0c247e74b70c09f0c524751991f49de1721941f7cfa97e954c8901f221f2d(
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc9c7177fa8eaaac3f78a5985704f2e0b65afdc9ef98e9fcebb628b16844e52(
    val: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894e920ca7d06b2f6f8f782c7af5bcd4e290f7c5ab0076004a253c04d6cfaec0(
    pkey: Assign,
    skey: typing.Optional[Assign] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__331614f70c4957ba245389adda042d248e85ee7b1e7ca5531863245ae9efa42b(
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dac7c0ed89396d7f29c7903e2a718a49bfb552b89c6e4aba2bf132b53179d5a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api: IGraphqlApi,
    data_source: typing.Optional[BaseDataSource] = None,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[Code] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe6f3e60857395308a8a844c5a41064caae65e42a2597bef9b2139e42f0c5550(
    *,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[Code] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
    data_source: typing.Optional[BaseDataSource] = None,
    api: IGraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49869076912d34bbcf8b6ff9fda046f1ab0998a982c178c6a23b70ae322f278c(
    *,
    name: builtins.str,
    runtime_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40565593cb0b74633173faf6f073987b024d4b7af8c07e296173c630a61b972a(
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045c4bbd28d6b47aba2e105fffdc95a54744a147dd39c45d3bda36713099050d(
    api: IGraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3adee49b1627eaa29eddfbecd2e0b4178976610eae08b6d3f86587aac2bc086b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebec24f4f2651b34bbc2b330a1662502003c499847aaa673f0f8c02bfb1da189(
    *,
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bbf95d843c3b959000a5a0fb88e2cdd71e7f4d434ed1dc1bbee3af5ad4eebb7(
    pkey: Assign,
    skey: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__684d8cf05e18cc8e70df256c4f02edd1174c86389940b94860ac8d3c8a646450(
    val: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d26723deaef4a15fbf75b125939130cfcede962718693a41cf9fd2453a608f62(
    *,
    user_pool: _IUserPool_1f1029e2,
    app_id_client_regex: typing.Optional[builtins.str] = None,
    default_action: typing.Optional[UserPoolDefaultAction] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44bb77a68dfd2f3750592928a447287f6d2eb9f026200de390e4380494e5cb8(
    attr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f92cb836df619fb1d6788b3bf1522a2affe1a32cec29860d2b16e8bc69fa92ba(
    arg: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a23d4ed33443e24250ebba07a891e2279c2fad90dd6bdb7c0b41b485078d87f1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api: IGraphqlApi,
    data_source: BaseDataSource,
    name: builtins.str,
    code: typing.Optional[Code] = None,
    description: typing.Optional[builtins.str] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4ba394d6181e77cbec9abe16b3e72b648a9b70fd79591b401a435e4394321b0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3af0670f4f09a616138962b9570f4bdf3dbddf35d8cf64897cb6240039a9af35(
    *,
    name: builtins.str,
    code: typing.Optional[Code] = None,
    description: typing.Optional[builtins.str] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
    api: IGraphqlApi,
    data_source: BaseDataSource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64c3b5b60096d2f072c0237f4540425eb18b7539e311bcd346760100ef39b3f(
    path: builtins.str,
    *,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
    bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9565c14ceaf744c92526f1e68f77253854c13aa006a825537bf468bbb035ecbb(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42501afdb54f6472ab998a801568e1b317b9ee60d07481b1c90ef88e5338ba46(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    props: typing.Union[BackedDataSourceProps, typing.Dict[builtins.str, typing.Any]],
    *,
    type: builtins.str,
    dynamo_db_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_bridge_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.EventBridgeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_search_service_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relational_database_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea2d00276bc1b45e9a26da67eba934f53db82f49e29640aa05289870be94f55(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb501305798213be783a45c59d39c261a182cd09ad0d40d480253e28a2e2438d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    table: _ITable_504fd401,
    read_only_access: typing.Optional[builtins.bool] = None,
    use_caller_credentials: typing.Optional[builtins.bool] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2cd0eab2d8bf885992981b7b491d32e73f943353d4564c2a504d3154462a65(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    table: _ITable_504fd401,
    read_only_access: typing.Optional[builtins.bool] = None,
    use_caller_credentials: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e54d95c1db8116ebc9ebacf3e6a8c3fa0a47859bc0f72493b58e89411daa904(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain: _IDomain_0c9006b4,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6153bccef60ecdf62438c139adee9ab9afb1c0361813760bad95eae9e5f43975(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    domain: _IDomain_0c9006b4,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac2aea20ec487bb19cfbb1a301369050ec488bf91096759b3fb3c226c30926c1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    event_bus: _IEventBus_88d13111,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00da245f6e9b76ee0cfe04414b7bce864ba4a2790c154b23dc47e4ee33a9f8a(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    event_bus: _IEventBus_88d13111,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff11ad61ab69f000dc327a3d454c95573a39bc2e7da1972aa306a513e0346484(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5231a54be88b667c5a5a1bc5329dbbb64c8799d82120069adc12366c521a0d7(
    id: builtins.str,
    table: _ITable_504fd401,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f496dfc677644fac1f40399c0372134a286d0cd64c4afc8c8506b52c9c6842(
    id: builtins.str,
    domain: _IDomain_0c9006b4,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a520f759496ebb7823d10727dc78034711f5090c53ba71c8d7a1dc1848b96e01(
    id: builtins.str,
    event_bus: _IEventBus_88d13111,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0deca16db4175c13560dbb7b3c4aa8cf9a8d20110a58f0ac2ce906dafcc01764(
    id: builtins.str,
    endpoint: builtins.str,
    *,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82b9734a5029f4e20ff30bb852586ba9b413700a9b7453b7113bf1db1efaf29f(
    id: builtins.str,
    lambda_function: _IFunction_6adb0ab8,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41813b6c71fbc2a0901dfef0dd1b464af643898b532103ddead5829c10187ab1(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2a17558b2960e621e2eca90fe762c3ea77844a8d87d843ffdbbad8247baaf8(
    id: builtins.str,
    domain: _IDomain_3c13cbdd,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5e408fa29227d2c0f12593dd86151b649a2b97300fea604c91973afef4ab55(
    id: builtins.str,
    serverless_cluster: _IServerlessCluster_adbbb720,
    secret_store: _ISecret_6e020e6a,
    database_name: typing.Optional[builtins.str] = None,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3519600d64431e6297911193398dcc136af3b4dd3ec5511d0601a8cbf274f4c(
    construct: _CfnResource_9df397a6,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8efe28cf6861260ad6e47a65b8be5e006016a7c27a4ee3f2cac0e898d7f256b(
    id: builtins.str,
    *,
    data_source: typing.Optional[BaseDataSource] = None,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[Code] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    runtime: typing.Optional[FunctionRuntime] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c251fa7555c0770f24a577dcd59d2f51898cf46299807eda335998d735f187(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    endpoint: builtins.str,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e9eb5236f193b30b614aad3d73de37944e1dc26e925a87b1683e07749c2d81(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lambda_function: _IFunction_6adb0ab8,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd360baebe2cc73f8afb0301b4c78dd7e9c49ef5e7f543f97d3ca94cc7c49d3f(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    lambda_function: _IFunction_6adb0ab8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf111cfb617596222f7a6819bc86667f0aa3335d65397549bc520d302ed052c0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain: _IDomain_3c13cbdd,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d43f1439475200e8855550373e564cf774bcfb1c24a9ca37182ca3143b83a31(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    domain: _IDomain_3c13cbdd,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__354d74fae67acb83d442133dee432ed59e1dfd493ad0bee02c5d1b21de9e647d(
    pkey: Assign,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e39eb491b2b69c3a845d6a2414560f3ccf3cf72641d3a92468e82bf545bcf3(
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__568b99c9d3f9eb137243f7121761a99603a4994f00bae5826acff0b7a70dbb25(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    secret_store: _ISecret_6e020e6a,
    serverless_cluster: _IServerlessCluster_adbbb720,
    database_name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c062ac22fbaef687d5273408a83f4b49e1466d504c5d1d22aa7e464c31ce4e9d(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_IRole_235f5d8e] = None,
    secret_store: _ISecret_6e020e6a,
    serverless_cluster: _IServerlessCluster_adbbb720,
    database_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdc21261f45618890d843fff7978e6e8e4f4cfe7884c4fffbff6b8dad98036d4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    schema: ISchema,
    authorization_config: typing.Optional[typing.Union[AuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_name: typing.Optional[typing.Union[DomainOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    log_config: typing.Optional[typing.Union[LogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    visibility: typing.Optional[Visibility] = None,
    xray_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cefbac91e5bf4b599b8cb612f2e49280f0cab47fab8b476b11f991f6c9f42f4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    graphql_api_id: builtins.str,
    graphql_api_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca5d6afc67603703e938a4f127d82a052b1172c6c07cab72c6e3bded9ccd8e9(
    construct: _CfnResource_9df397a6,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104e94b5f084bee63e12022802003206eb0917369d9714c4bd16b6175830d883(
    grantee: _IGrantable_71c4f5de,
    resources: IamResource,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a4ce004c83ea63a70a24d83e7decd2ca533063652cd621858a247a616ce82c(
    grantee: _IGrantable_71c4f5de,
    *fields: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__425954c633cc79cdb87065e43764a32551571cca0bdaf65a67a4170d25a651ff(
    grantee: _IGrantable_71c4f5de,
    *fields: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980d951a731ee0c5da0e5b32e9e2870ea1adf06571f857a693decc31a0e959e5(
    grantee: _IGrantable_71c4f5de,
    *fields: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
