'''
# AWS CDK Custom Resources

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Provider Framework

AWS CloudFormation [custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) are extension points to the provisioning
engine. When CloudFormation needs to create, update or delete a custom resource,
it sends a lifecycle event notification to a **custom resource provider**. The provider
handles the event (e.g. creates a resource) and sends back a response to CloudFormation.

The `@aws-cdk/custom-resources.Provider` construct is a "mini-framework" for
implementing providers for AWS CloudFormation custom resources. The framework offers a high-level API which makes it easier to implement robust
and powerful custom resources. If you are looking to implement a custom resource provider, we recommend
you use this module unless you have good reasons not to. For an overview of different provider types you
could be using, see the [Custom Resource Providers section in the core library documentation](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib-readme.html#custom-resource-providers).

> **N.B.**: if you use the provider framework in this module you will write AWS Lambda Functions that look a lot like, but aren't exactly the same as the Lambda Functions you would write if you wrote CloudFormation Custom Resources directly, without this framework.
>
> Specifically, to report success or failure, have your Lambda Function exit in the right way: return data for success, or throw an
> exception for failure. *Do not* post the success or failure of your custom resource to an HTTPS URL as the CloudFormation
> documentation tells you to do.

The framework has the following capabilities:

* Handles responses to AWS CloudFormation and protects against blocked
  deployments
* Validates handler return values to help with correct handler implementation
* Supports asynchronous handlers to enable operations that require a long waiting period for a resource, which can exceed the AWS Lambda timeout
* Implements default behavior for physical resource IDs.

The following code shows how the `Provider` construct is used in conjunction
with a `CustomResource` and a user-provided AWS Lambda function which implements
the actual handler.

```python
# on_event: lambda.Function
# is_complete: lambda.Function
# my_role: iam.Role


my_provider = cr.Provider(self, "MyProvider",
    on_event_handler=on_event,
    is_complete_handler=is_complete,  # optional async "waiter"
    log_group=logs.LogGroup(self, "MyProviderLogs",
        retention=logs.RetentionDays.ONE_DAY
    ),
    role=my_role
)

CustomResource(self, "Resource1", service_token=my_provider.service_token)
CustomResource(self, "Resource2", service_token=my_provider.service_token)
```

Providers are implemented through AWS Lambda functions that are triggered by the
provider framework in response to lifecycle events.

At the minimum, users must define the `onEvent` handler, which is invoked by the
framework for all resource lifecycle events (`Create`, `Update` and `Delete`)
and returns a result which is then submitted to CloudFormation.

The following example is a skeleton for a Python implementation of `onEvent`:

```py
def on_event(event, context):
  print(event)
  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event)
  if request_type == 'Update': return on_update(event)
  if request_type == 'Delete': return on_delete(event)
  raise Exception("Invalid request type: %s" % request_type)

def on_create(event):
  props = event["ResourceProperties"]
  print("create new resource with props %s" % props)

  # add your create code here...
  physical_id = ...

  return { 'PhysicalResourceId': physical_id }

def on_update(event):
  physical_id = event["PhysicalResourceId"]
  props = event["ResourceProperties"]
  print("update resource %s with props %s" % (physical_id, props))
  # ...

def on_delete(event):
  physical_id = event["PhysicalResourceId"]
  print("delete resource %s" % physical_id)
  # ...
```

> When writing your handlers, there are a couple of non-obvious corner cases you need to
> pay attention to. See the [important cases to handle](#important-cases-to-handle) section for more information.

Users may also provide an additional handler called `isComplete`, for cases
where the lifecycle operation cannot be completed immediately. The
`isComplete` handler will be retried asynchronously after `onEvent` until it
returns `IsComplete: true`, or until the total provider timeout has expired.

The following example is a skeleton for a Python implementation of `isComplete`:

```py
def is_complete(event, context):
  physical_id = event["PhysicalResourceId"]
  request_type = event["RequestType"]

  # check if resource is stable based on request_type
  is_ready = ...

  return { 'IsComplete': is_ready }
```

> **Security Note**: the Custom Resource Provider Framework will write the value of `ResponseURL`,
> which is a pre-signed S3 URL used to report the success or failure of the Custom Resource execution
> back to CloudFormation, in a readable form to the AWS Step Functions execution history.
>
> Anybody who can list and read AWS StepFunction executions in your account will be able to write
> a fake response to this URL and make your CloudFormation deployments fail.
>
> Do not use this library if your threat model requires that you cannot trust actors who are able
> to list StepFunction executions in your account.

### Handling Lifecycle Events: onEvent

The user-defined `onEvent` AWS Lambda function is invoked whenever a resource
lifecycle event occurs. The function is expected to handle the event and return
a response to the framework that, at least, includes the physical resource ID.

If `onEvent` returns successfully, the framework will submit a "SUCCESS" response
to AWS CloudFormation for this resource operation.  If the provider is
[asynchronous](#asynchronous-providers-iscomplete) (`isCompleteHandler` is
defined), the framework will only submit a response based on the result of
`isComplete`.

If `onEvent` throws an error, the framework will submit a "FAILED" response to
AWS CloudFormation.

The input event includes the following fields derived from the [Custom Resource
Provider Request](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requests.html#crpg-ref-request-fields):

| Field                   | Type   | Description                                                                                                                                         |
| ----------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RequestType`           | String | The type of lifecycle event: `Create`, `Update` or `Delete`.                                                                                        |
| `LogicalResourceId`     | String | The template developer-chosen name (logical ID) of the custom resource in the AWS CloudFormation template.                                          |
| `PhysicalResourceId`    | String | This field will only be present for `Update` and `Delete` events and includes the value returned in `PhysicalResourceId` of the previous operation. |
| `ResourceProperties`    | JSON   | This field contains the properties defined in the template for this custom resource.                                                                |
| `OldResourceProperties` | JSON   | This field will only be present for `Update` events and contains the resource properties that were declared previous to the update request.         |
| `ResourceType`          | String | The resource type defined for this custom resource in the template. A provider may handle any number of custom resource types.                      |
| `RequestId`             | String | A unique ID for the request.                                                                                                                        |
| `StackId`               | String | The ARN that identifies the stack that contains the custom resource.                                                                                |

The return value from `onEvent` must be a JSON object with the following fields:

| Field                | Type    | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PhysicalResourceId` | String  | No       | The allocated/assigned physical ID of the resource. If omitted for `Create` events, the event's `RequestId` will be used. For `Update`, the current physical ID will be used. If a different value is returned, CloudFormation will follow with a subsequent `Delete` for the previous ID (resource replacement). For `Delete`, it will always return the current physical resource ID, and if the user returns a different one, an error will occur. |
| `Data`               | JSON    | No       | Resource attributes, which can later be retrieved through `Fn::GetAtt` on the custom resource object.                                                                                                                                                                                                                                                                                                                                                 |
| `NoEcho`             | Boolean | No       | Whether to mask the output of the custom resource when retrieved by using the `Fn::GetAtt` function.                                                                                                                                                                                                                                                                                                                                                  |
| *any*                | *any*   | No       | Any other field included in the response will be passed through to `isComplete`. This can sometimes be useful to pass state between the handlers.                                                                                                                                                                                                                                                                                                     |

### Asynchronous Providers: isComplete

It is not uncommon for the provisioning of resources to be an asynchronous
operation, which means that the operation does not immediately finish, and we
need to "wait" until the resource stabilizes.

The provider framework makes it easy to implement "waiters" by allowing users to
specify an additional AWS Lambda function in `isCompleteHandler`.

The framework will repeatedly invoke the handler every `queryInterval`. When
`isComplete` returns with `IsComplete: true`, the framework will submit a
"SUCCESS" response to AWS CloudFormation. If `totalTimeout` expires and the
operation has not yet completed, the framework will submit a "FAILED" response
with the message "Operation timed out".

If an error is thrown, the framework will submit a "FAILED" response to AWS
CloudFormation.

The input event to `isComplete` includes all request fields, combined with all
fields returned from `onEvent`. If `PhysicalResourceId` has not been explicitly
returned from `onEvent`, it's value will be calculated based on the heuristics
described above.

The return value must be a JSON object with the following fields:

| Field        | Type    | Required | Description                                                                                                                                                       |
| ------------ | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IsComplete` | Boolean | Yes      | Indicates if the operation has finished or not.                                                                                                                   |
| `Data`       | JSON    | No       | May only be sent if `IsComplete` is `true` and includes additional resource attributes. These attributes will be **merged** with the ones returned from `onEvent` |

### Physical Resource IDs

Every resource in CloudFormation has a physical resource ID. When a resource is
created, the `PhysicalResourceId` returned from the `Create` operation is stored
by AWS CloudFormation and assigned to the logical ID defined for this resource
in the template. If a `Create` operation returns without a `PhysicalResourceId`,
the framework will use `RequestId` as the default. This is sufficient for
various cases such as "pseudo-resources" which only query data.

For `Update` and `Delete` operations, the resource event will always include the
current `PhysicalResourceId` of the resource.

When an `Update` operation occurs, the default behavior is to return the current
physical resource ID. if the `onEvent` returns a `PhysicalResourceId` which is
different from the current one, AWS CloudFormation will treat this as a
**resource replacement**, and it will issue a subsequent `Delete` operation for
the old resource.

As a rule of thumb, if your custom resource supports configuring a physical name
(e.g. you can specify a `BucketName` when you define an `AWS::S3::Bucket`), you
must return this name in `PhysicalResourceId` and make sure to handle
replacement properly. The `S3File` example demonstrates this
through the `objectKey` property.

### When there are errors

As mentioned above, if any of the user handlers fail (i.e. throws an exception)
or times out (due to their AWS Lambda timing out), the framework will trap these
errors and submit a "FAILED" response to AWS CloudFormation, along with the error
message.

Since errors can occur in multiple places in the provider (framework, `onEvent`,
`isComplete`), it is important to know that there could situations where a
resource operation fails even though the operation technically succeeded (i.e.
isComplete throws an error).

When AWS CloudFormation receives a "FAILED" response, it will attempt to roll
back the stack to it's last state. This has different meanings for different
lifecycle events:

* If a `Create` event fails, the resource provider framework will automatically
  ignore the subsequent `Delete` operation issued by AWS CloudFormation. The
  framework currently does not support customizing this behavior (see
  https://github.com/aws/aws-cdk/issues/5524).
* If an `Update` event fails, CloudFormation will issue an additional `Update`
  with the previous properties.
* If a `Delete` event fails, CloudFormation will abandon this resource.

### Important cases to handle

You should keep the following list in mind when writing custom resources to
make sure your custom resource behaves correctly in all cases:

* During `Create`:

  * If the create fails, the *provider framework* will make sure you
    don't get a subsequent `Delete` event. If your create involves multiple distinct
    operations, it is your responsibility to catch and rethrow and clean up
    any partial updates that have already been performed. Make sure your
    API call timeouts and Lambda timeouts allow for this.
* During `Update`:

  * If the update fails, you will get a subsequent `Update` event
    to roll back to the previous state (with `ResourceProperties` and
    `OldResourceProperties` reversed).
  * If you return a different `PhysicalResourceId`, you will subsequently
    receive a `Delete` event to clean up the previous state of the resource.
* During `Delete`:

  * If the behavior of your custom resource is tied to another AWS resource
    (for example, it exists to clean the contents of a stateful resource), keep
    in mind that your custom resource may be deleted independently of the other
    resource and you must confirm that it is appropriate to perform the action.
  * (only if you are *not* using the provider framework) a `Delete` event
    may be caused by a failed `Create`. You must be able to handle the case
    where the resource you are trying to delete hasn't even been created yet.
* If you update the code of your custom resource and change the format of the
  resource properties, be aware that there may still be already-deployed
  instances of your custom resource out there, and you may still receive
  the *old* property format in `ResourceProperties` (during `Delete` and
  rollback `Updates`) or in `OldResourceProperties` (during rollforward
  `Update`). You must continue to handle all possible sets of properties
  your custom resource could have ever been created with in the past.

### Provider Framework Execution Policy

Similarly to any AWS Lambda function, if the user-defined handlers require
access to AWS resources, you will have to define these permissions
by calling "grant" methods such as `myBucket.grantRead(myHandler)`), using `myHandler.addToRolePolicy`
or specifying an `initialPolicy` when defining the function.

Bear in mind that in most cases, a single provider will be used for multiple
resource instances. This means that the execution policy of the provider must
have the appropriate privileges.

The following example grants the `onEvent` handler `s3:GetObject*` permissions
to all buckets:

```python
lambda_.Function(self, "OnEventHandler",
    runtime=lambda_.Runtime.NODEJS_LATEST,
    handler="index.handler",
    code=lambda_.Code.from_inline("my code"),
    initial_policy=[
        iam.PolicyStatement(actions=["s3:GetObject*"], resources=["*"])
    ]
)
```

### Timeouts

Users are responsible to define the timeouts for the AWS Lambda functions for
user-defined handlers. It is recommended not to exceed a **14 minutes** timeout,
since all framework functions are configured to time out after 15 minutes, which
is the maximal AWS Lambda timeout.

If your operation takes over **14 minutes**, the recommended approach is to
implement an [asynchronous provider](#asynchronous-providers-iscomplete), and
then configure the timeouts for the asynchronous retries through the
`queryInterval` and the `totalTimeout` options.

### Provider Framework Examples

This module includes a few examples for custom resource implementations:

#### S3File

Provisions an object in an S3 bucket with textual contents. See the source code
for the
[construct](https://github.com/aws/aws-cdk/blob/main/packages/%40aws-cdk-testing/framework-integ/test/custom-resources/test/provider-framework/integration-test-fixtures/s3-file.ts) and
[handler](https://github.com/aws/aws-cdk/blob/main/packages/%40aws-cdk-testing/framework-integ/test/custom-resources/test/provider-framework/integration-test-fixtures/s3-file-handler/index.ts).

The following example will create the file `folder/file1.txt` inside `myBucket`
with the contents `hello!`.

```plaintext
// This example exists only for TypeScript

declare const myBucket: s3.Bucket;
new cr.S3File(this, 'MyFile', {
  bucket: myBucket,
  objectKey: 'folder/file1.txt', // optional
  content: 'hello!',
  public: true, // optional
});
```

This sample demonstrates the following concepts:

* Synchronous implementation (`isComplete` is not defined)
* Automatically generates the physical name if `objectKey` is not defined
* Handles physical name changes
* Returns resource attributes
* Handles deletions
* Implemented in TypeScript

#### S3Assert

Checks that the textual contents of an S3 object matches a certain value. The check will be retried
for 5 minutes as long as the object is not found or the value is different. See the source code for the
[construct](https://github.com/aws/aws-cdk/blob/main/packages/%40aws-cdk-testing/framework-integ/test/custom-resources/test/provider-framework/integration-test-fixtures/s3-assert.ts)
and [handler](https://github.com/aws/aws-cdk/blob/main/packages/%40aws-cdk-testing/framework-integ/test/custom-resources/test/provider-framework/integration-test-fixtures/s3-assert-handler/index.py).

The following example defines an `S3Assert` resource which waits until
`myfile.txt` in `myBucket` exists and includes the contents `foo bar`:

```plaintext
// This example exists only for TypeScript

declare const myBucket: s3.Bucket;
new cr.S3Assert(this, 'AssertMyFile', {
  bucket: myBucket,
  objectKey: 'myfile.txt',
  expectedContent: 'foo bar',
});
```

This sample demonstrates the following concepts:

* Asynchronous implementation
* Non-intrinsic physical IDs
* Implemented in Python

### Customizing Provider Function name

In multi-account environments or when the custom resource may be re-utilized across several
stacks it may be useful to manually set a name for the Provider Function Lambda and therefore
have a predefined service token ARN.

```python
# on_event: lambda.Function
# is_complete: lambda.Function
# my_role: iam.Role

my_provider = cr.Provider(self, "MyProvider",
    on_event_handler=on_event,
    is_complete_handler=is_complete,
    log_group=logs.LogGroup(self, "MyProviderLogs",
        retention=logs.RetentionDays.ONE_DAY
    ),
    role=my_role,
    provider_function_name="the-lambda-name"
)
```

### Customizing Provider Function environment encryption key

Sometimes it may be useful to manually set a AWS KMS key for the Provider Function Lambda and therefore
be able to view, manage and audit the key usage.

```python
import aws_cdk.aws_kms as kms

# on_event: lambda.Function
# is_complete: lambda.Function
# my_role: iam.Role


key = kms.Key(self, "MyKey")
my_provider = cr.Provider(self, "MyProvider",
    on_event_handler=on_event,
    is_complete_handler=is_complete,
    log_group=logs.LogGroup(self, "MyProviderLogs",
        retention=logs.RetentionDays.ONE_DAY
    ),
    role=my_role,
    provider_function_env_encryption=key
)
```

## Custom Resources for AWS APIs

Sometimes a single API call can fill the gap in the CloudFormation coverage. In
this case you can use the `AwsCustomResource` construct. This construct creates
a custom resource that can be customized to make specific API calls for the
`CREATE`, `UPDATE` and `DELETE` events. Additionally, data returned by the API
call can be extracted and used in other constructs/resources (creating a real
CloudFormation dependency using `Fn::GetAtt` under the hood).

The physical id of the custom resource can be specified or derived from the data
returned by the API call.

The `AwsCustomResource` uses the AWS SDK for JavaScript. Services, actions and
parameters can be found in the [API documentation](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html).

Path to data must be specified using a dot notation, e.g. to get the string value
of the `Title` attribute for the first item returned by `dynamodb.query` it should
be `Items.0.Title.S`.

To make sure that the newest API calls are available the latest AWS SDK v3 is installed
in the Lambda function implementing the custom resource. The installation takes around 60
seconds. If you prefer to optimize for speed, you can disable the installation by setting
the `installLatestAwsSdk` prop to `false`.

### Custom Resource Execution Policy

The `policy` property defines the IAM Policy that will be applied to the API calls. This must be provided
if an existing `role` is not specified and is optional otherwise. The library provides two factory methods
to quickly configure this:

* **`AwsCustomResourcePolicy.fromSdkCalls`** - Use this to auto-generate IAM
  Policy statements based on the configured SDK calls. Keep two things in mind
  when using this policy:

  * This policy variant assumes the IAM policy name has the same name as the API
    call. This is true in 99% of cases, but there are exceptions (for example,
    S3's `PutBucketLifecycleConfiguration` requires
    `s3:PutLifecycleConfiguration` permissions, Lambda's `Invoke` requires
    `lambda:InvokeFunction` permissions). Use `fromStatements` if you want to
    do a call that requires different IAM action names.
  * You will have to either provide specific ARNs, or explicitly use
    `AwsCustomResourcePolicy.ANY_RESOURCE` to allow access to any resource.
* **`AwsCustomResourcePolicy.fromStatements`** - Use this to specify your own
  custom statements.

The custom resource also implements `iam.IGrantable`, making it possible to use the `grantXxx()` methods.

As this custom resource uses a singleton Lambda function, it's important to note
that the function's role will eventually accumulate the permissions/grants from all
resources.

Chained API calls can be achieved by creating dependencies:

```python
aws_custom1 = cr.AwsCustomResource(self, "API1",
    on_create=cr.AwsSdkCall(
        service="...",
        action="...",
        physical_resource_id=cr.PhysicalResourceId.of("...")
    ),
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)

aws_custom2 = cr.AwsCustomResource(self, "API2",
    on_create=cr.AwsSdkCall(
        service="...",
        action="...",
        parameters={
            "text": aws_custom1.get_response_field("Items.0.text")
        },
        physical_resource_id=cr.PhysicalResourceId.of("...")
    ),
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)
```

### Physical Resource Id Parameter

Some AWS APIs may require passing the physical resource id in as a parameter for doing updates and deletes. You can pass it by using `PhysicalResourceIdReference`.

```python
aws_custom = cr.AwsCustomResource(self, "aws-custom",
    on_create=cr.AwsSdkCall(
        service="...",
        action="...",
        parameters={
            "text": "..."
        },
        physical_resource_id=cr.PhysicalResourceId.of("...")
    ),
    on_update=cr.AwsSdkCall(
        service="...",
        action="...",
        parameters={
            "text": "...",
            "resource_id": cr.PhysicalResourceIdReference()
        }
    ),
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)
```

You can omit `PhysicalResourceId` property in `onUpdate` to passthrough the value in `onCreate`. This behavior is useful when using Update APIs that response with an empty body.

> AwsCustomResource.getResponseField() and .getResponseFieldReference() will not work if the Create and Update APIs don't consistently return the same fields.

### Handling Custom Resource Errors

Every error produced by the API call is treated as is and will cause a "FAILED" response to be submitted to CloudFormation.
You can ignore some errors by specifying the `ignoreErrorCodesMatching` property, which accepts a regular expression that is
tested against the `code` property of the response. If matched, a "SUCCESS" response is submitted.
Note that in such a case, the call response data and the `Data` key submitted to CloudFormation would both be an empty JSON object.
Since a successful resource provisioning might or might not produce outputs, this presents us with some limitations:

* `PhysicalResourceId.fromResponse` - Since the call response data might be empty, we cannot use it to extract the physical id.
* `getResponseField` and `getResponseFieldReference` - Since the `Data` key is empty, the resource will not have any attributes, and therefore, invoking these functions will result in an error.

In both the cases, you will get a synth time error if you attempt to use it in conjunction with `ignoreErrorCodesMatching`.

### Customizing the Lambda function implementing the custom resource

Use the `role`, `timeout`, `memorySize`, `logGroup`, `functionName` and `removalPolicy` properties to customize
the Lambda function implementing the custom resource:

```python
# my_role: iam.Role

cr.AwsCustomResource(self, "Customized",
    role=my_role,  # must be assumable by the `lambda.amazonaws.com` service principal
    timeout=Duration.minutes(10),  # defaults to 2 minutes
    memory_size=1025,  # defaults to 512 if installLatestAwsSdk is true
    log_group=logs.LogGroup(self, "AwsCustomResourceLogs",
        retention=logs.RetentionDays.ONE_DAY
    ),
    function_name="my-custom-name",  # defaults to a CloudFormation generated name
    removal_policy=RemovalPolicy.RETAIN,  # defaults to `RemovalPolicy.DESTROY`
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)
```

Additionally, the Lambda function can be placed in a private VPC by using the `vpc`
and `vpcSubnets` properties.

```python
# vpc: ec2.Vpc

cr.AwsCustomResource(self, "CustomizedInVpc",
    vpc=vpc,
    vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)
```

Note that Lambda functions in a VPC
[require Network Address Translation (NAT) in order to access the internet](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-internet).
The subnets specified in `vpcSubnets` must be private subnets.

### Restricting the output of the Custom Resource

CloudFormation imposes a hard limit of 4096 bytes for custom resources response
objects. If your API call returns an object that exceeds this limit, you can restrict
the data returned by the custom resource to specific paths in the API response:

```python
cr.AwsCustomResource(self, "ListObjects",
    on_create=cr.AwsSdkCall(
        service="s3",
        action="ListObjectsV2",
        parameters={
            "Bucket": "my-bucket"
        },
        physical_resource_id=cr.PhysicalResourceId.of("id"),
        output_paths=["Contents.0.Key", "Contents.1.Key"]
    ),
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)
```

Note that even if you restrict the output of your custom resource you can still use any
path in `PhysicalResourceId.fromResponse()`.

### Custom Resource Logging for SDK Calls

By default, logging occurs during execution of the singleton Lambda used by a custom resource. The data being logged includes:

* The event object that is received by the Lambda handler
* The response received after making an API call
* The response object that the Lambda handler will return
* SDK versioning information
* Caught and uncaught errors

The `logging` property defined on the `AwsSdkCall` interface allows control over what data is being logged on a per SDK call basis. This is configurable via an instance of the `Logging` class. The `Logging` class exposes two options that can be used to configure logging:

1. `Logging.all()` which enables logging of all data. This is the default `logging` configuration.
2. `Logging.withDataHidden()` which prevents logging of all data associated with the API call response, including logging the raw API call response and the `Data` field on the Lambda handler response object. This configuration option is particularly useful for situations where the API call response may contain sensitive information.

For further context about `Logging.withDataHidden()`, consider a user who might be making an API call that is returning sensitive information that they may want to keep hidden. To do this, they would configure `logging` with `Logging.withDataHidden()`:

```python
get_parameter = cr.AwsCustomResource(self, "GetParameter",
    on_update=cr.AwsSdkCall(
        service="SSM",
        action="GetParameter",
        parameters={
            "Name": "my-parameter",
            "WithDecryption": True
        },
        physical_resource_id=cr.PhysicalResourceId.of(Date.now().to_string()),
        logging=cr.Logging.with_data_hidden()
    ),
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)
```

With this configuration option set, the raw API call response would not be logged and the `Data` field of the response object would be hidden:

```
{
  "Status": "SUCCESS",
  "Reason": "OK",
  "PhysicalResourceId": "1234567890123",
  "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/Test/043tyub2-194e-4cy2-a969-9891ghj6cd0d",
  "RequestId": "a16y677a-a8b6-41a6-bf7b-7644586861a5",
  "LogicalResourceId": "Sercret",
  "NoEcho": false,
}
```

For comparison, configuring `logging` with `Logging.all()` would result in the raw API call response being logged, as well as the full response object:

```
{
  "Status": "SUCCESS",
  "Reason": "OK",
  "PhysicalResourceId": "1234567890123",
  "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/Test/043tyub2-194e-4cy2-a969-9891ghj6cd0d",
  "RequestId": "a16y677a-a8b6-41a6-bf7b-7644586861a5",
  "LogicalResourceId": "Sercret",
  "NoEcho": false,
  "Data": {
    "region": "us-west-2",
    "Parameter.ARN": "arn:aws:ssm:us-west-2:123456789012:parameter/Test/Parameter",
    "Parameter.DataType": "text",
    "Parameter.Name": "/Test/Parameter",
    "Parameter.Type": "SecureString",
    "Parameter.Value": "ThisIsSecret!123",
    "Parameter.Version": 1
  }
}
```

### Custom Resource Examples

#### Get the latest version of a secure SSM parameter

```python
get_parameter = cr.AwsCustomResource(self, "GetParameter",
    on_update=cr.AwsSdkCall( # will also be called for a CREATE event
        service="SSM",
        action="GetParameter",
        parameters={
            "Name": "my-parameter",
            "WithDecryption": True
        },
        physical_resource_id=cr.PhysicalResourceId.of(Date.now().to_string())),
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)

# Use the value in another construct with
get_parameter.get_response_field("Parameter.Value")
```

#### Associate a PrivateHostedZone with VPC shared from another account

```python
get_parameter = cr.AwsCustomResource(self, "AssociateVPCWithHostedZone",
    on_create=cr.AwsSdkCall(
        assumed_role_arn="arn:aws:iam::OTHERACCOUNT:role/CrossAccount/ManageHostedZoneConnections",
        service="Route53",
        action="AssociateVPCWithHostedZone",
        parameters={
            "HostedZoneId": "hz-123",
            "VPC": {
                "VPCId": "vpc-123",
                "VPCRegion": "region-for-vpc"
            }
        },
        physical_resource_id=cr.PhysicalResourceId.of("${vpcStack.SharedVpc.VpcId}-${vpcStack.Region}-${PrivateHostedZone.HostedZoneId}")
    ),
    # Will ignore any resource and use the assumedRoleArn as resource and 'sts:AssumeRole' for service:action
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
)
```

#### Using AWS SDK for JavaScript v3

`AwsCustomResource` uses Node 18 and AWS SDK v3 by default. You can specify the service as either the name of the SDK module, or just the service name. Using API Gateway as an example, the following formats are all accepted for `service`:

* The SDKv3 service name: `api-gateway` (recommended)
* The full SDKv3 package name: `@aws-sdk/client-api-gateway`
* The SDKv2 constructor name: `APIGateway`
* The SDKv2 constructor name in all lower case: `apigateway`

The following formats are accepted for `action`:

* The API call name: `GetRestApi` (recommended)
* The API call name with a lowercase starting letter method name: `getRestApi`
* The SDKv3 command class name: `GetRestApiCommand`

For readability, we recommend using the short forms going forward:

```python
cr.AwsCustomResource(self, "GetParameter",
    resource_type="Custom::SSMParameter",
    on_update=cr.AwsSdkCall(
        service="ssm",  # 'SSM' in v2
        action="GetParameter",  # 'getParameter' in v2
        parameters={
            "Name": "foo",
            "WithDecryption": True
        },
        physical_resource_id=cr.PhysicalResourceId.from_response("Parameter.ARN")
    )
)
```

#### Making Cross Account Calls

Example of making a cross account call using an assumed role. If deploying the custom resource in a region where the cross account role is not defined (i.e. an opt-in region that is not enabled in the account owning the role), set the region parameter to a region enabled in that account.

```python
cross_account_role_arn = "arn:aws:iam::OTHERACCOUNT:role/CrossAccountRoleName" # arn of role deployed in separate account

call_region = "us-west-1" # sdk call to be made in specified region (optional)

cr.AwsCustomResource(self, "CrossAccount",
    on_create=cr.AwsSdkCall(
        assumed_role_arn=cross_account_role_arn,
        region=call_region,  # optional
        service="sts",
        action="GetCallerIdentity",
        physical_resource_id=cr.PhysicalResourceId.of("id")
    ),
    policy=cr.AwsCustomResourcePolicy.from_statements([iam.PolicyStatement.from_json({
        "Effect": "Allow",
        "Action": "sts:AssumeRole",
        "Resource": cross_account_role_arn
    })])
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
    Duration as _Duration_4839e8c3,
    IResolvable as _IResolvable_da3f097b,
    IResolveContext as _IResolveContext_b2df1921,
    Reference as _Reference_6ab8bd04,
    RemovalPolicy as _RemovalPolicy_9f93c814,
)
from ..aws_ec2 import (
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_logs import (
    ILogGroup as _ILogGroup_3c4fa718, RetentionDays as _RetentionDays_070f99f0
)
from ..aws_stepfunctions import LogLevel as _LogLevel_be1990fe


@jsii.implements(_IGrantable_71c4f5de)
class AwsCustomResource(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.custom_resources.AwsCustomResource",
):
    '''Defines a custom resource that is materialized using specific AWS API calls.

    These calls are created using
    a singleton Lambda function.

    Use this to bridge any gap that might exist in the CloudFormation Coverage.
    You can specify exactly which calls are invoked for the 'CREATE', 'UPDATE' and 'DELETE' life cycle events.

    :exampleMetadata: infused

    Example::

        get_parameter = cr.AwsCustomResource(self, "GetParameter",
            on_update=cr.AwsSdkCall( # will also be called for a CREATE event
                service="SSM",
                action="GetParameter",
                parameters={
                    "Name": "my-parameter",
                    "WithDecryption": True
                },
                physical_resource_id=cr.PhysicalResourceId.of(Date.now().to_string())),
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
            )
        )
        
        # Use the value in another construct with
        get_parameter.get_response_field("Parameter.Value")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        function_name: typing.Optional[builtins.str] = None,
        install_latest_aws_sdk: typing.Optional[builtins.bool] = None,
        log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        on_create: typing.Optional[typing.Union["AwsSdkCall", typing.Dict[builtins.str, typing.Any]]] = None,
        on_delete: typing.Optional[typing.Union["AwsSdkCall", typing.Dict[builtins.str, typing.Any]]] = None,
        on_update: typing.Optional[typing.Union["AwsSdkCall", typing.Dict[builtins.str, typing.Any]]] = None,
        policy: typing.Optional["AwsCustomResourcePolicy"] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        resource_type: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param function_name: A name for the singleton Lambda function implementing this custom resource. The function name will remain the same after the first AwsCustomResource is created in a stack. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param install_latest_aws_sdk: Whether to install the latest AWS SDK v2. If not specified, this uses whatever JavaScript SDK version is the default in AWS Lambda at the time of execution. Otherwise, installs the latest version from 'npmjs.com'. The installation takes around 60 seconds and requires internet connectivity. The default can be controlled using the context key ``@aws-cdk/customresources:installLatestAwsSdkDefault`` is. Default: - The value of ``@aws-cdk/customresources:installLatestAwsSdkDefault``, otherwise ``true``
        :param log_group: The Log Group used for logging of events emitted by the custom resource's lambda function. Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16. If you are deploying to another type of region, please check regional availability first. Default: - a default log group created by AWS Lambda
        :param log_retention: The number of days log events of the singleton Lambda function implementing this custom resource are kept in CloudWatch Logs. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: logs.RetentionDays.INFINITE
        :param memory_size: The memory size for the singleton Lambda function implementing this custom resource. Default: 512 mega in case if installLatestAwsSdk is false.
        :param on_create: The AWS SDK call to make when the resource is created. Default: - the call when the resource is updated
        :param on_delete: The AWS SDK call to make when the resource is deleted. Default: - no call
        :param on_update: The AWS SDK call to make when the resource is updated. Default: - no call
        :param policy: The policy that will be added to the execution role of the Lambda function implementing this custom resource provider. The custom resource also implements ``iam.IGrantable``, making it possible to use the ``grantXxx()`` methods. As this custom resource uses a singleton Lambda function, it's important to note the that function's role will eventually accumulate the permissions/grants from all resources. Note that a policy must be specified if ``role`` is not provided, as by default a new role is created which requires policy changes to access resources. Default: - no policy added
        :param removal_policy: The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy
        :param resource_type: Cloudformation Resource type. Default: - Custom::AWS
        :param role: The execution role for the singleton Lambda function implementing this custom resource provider. This role will apply to all ``AwsCustomResource`` instances in the stack. The role must be assumable by the ``lambda.amazonaws.com`` service principal. Default: - a new role is created
        :param timeout: The timeout for the singleton Lambda function implementing this custom resource. Default: Duration.minutes(2)
        :param vpc: The vpc to provision the lambda function in. Default: - the function is not provisioned inside a vpc.
        :param vpc_subnets: Which subnets from the VPC to place the lambda function in. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b163f566913e92c7adaa1ea97e50050b801bd514d3b2f5e3ddf86c11297e862)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AwsCustomResourceProps(
            function_name=function_name,
            install_latest_aws_sdk=install_latest_aws_sdk,
            log_group=log_group,
            log_retention=log_retention,
            memory_size=memory_size,
            on_create=on_create,
            on_delete=on_delete,
            on_update=on_update,
            policy=policy,
            removal_policy=removal_policy,
            resource_type=resource_type,
            role=role,
            timeout=timeout,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getResponseField")
    def get_response_field(self, data_path: builtins.str) -> builtins.str:
        '''Returns response data for the AWS SDK call as string.

        Example for S3 / listBucket : 'Buckets.0.Name'

        Note that you cannot use this method if ``ignoreErrorCodesMatching``
        is configured for any of the SDK calls. This is because in such a case,
        the response data might not exist, and will cause a CloudFormation deploy time error.

        :param data_path: the path to the data.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a62242b1380cc5a46c343b8beb355b12ad4bead7d218dff7533f32ef95535dc)
            check_type(argname="argument data_path", value=data_path, expected_type=type_hints["data_path"])
        return typing.cast(builtins.str, jsii.invoke(self, "getResponseField", [data_path]))

    @jsii.member(jsii_name="getResponseFieldReference")
    def get_response_field_reference(
        self,
        data_path: builtins.str,
    ) -> _Reference_6ab8bd04:
        '''Returns response data for the AWS SDK call.

        Example for S3 / listBucket : 'Buckets.0.Name'

        Use ``Token.asXxx`` to encode the returned ``Reference`` as a specific type or
        use the convenience ``getDataString`` for string attributes.

        Note that you cannot use this method if ``ignoreErrorCodesMatching``
        is configured for any of the SDK calls. This is because in such a case,
        the response data might not exist, and will cause a CloudFormation deploy time error.

        :param data_path: the path to the data.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a3cb7c74c2f60a8f1c2cfe429816d6751f4abf9bd7f2fccca230d2e342d4c5e)
            check_type(argname="argument data_path", value=data_path, expected_type=type_hints["data_path"])
        return typing.cast(_Reference_6ab8bd04, jsii.invoke(self, "getResponseFieldReference", [data_path]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROVIDER_FUNCTION_UUID")
    def PROVIDER_FUNCTION_UUID(cls) -> builtins.str:
        '''The uuid of the custom resource provider singleton lambda function.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROVIDER_FUNCTION_UUID"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_539bb2fd:
        '''The principal to grant permissions to.'''
        return typing.cast(_IPrincipal_539bb2fd, jsii.get(self, "grantPrincipal"))


class AwsCustomResourcePolicy(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.custom_resources.AwsCustomResourcePolicy",
):
    '''The IAM Policy that will be applied to the different calls.

    :exampleMetadata: infused

    Example::

        get_parameter = cr.AwsCustomResource(self, "GetParameter",
            on_update=cr.AwsSdkCall( # will also be called for a CREATE event
                service="SSM",
                action="GetParameter",
                parameters={
                    "Name": "my-parameter",
                    "WithDecryption": True
                },
                physical_resource_id=cr.PhysicalResourceId.of(Date.now().to_string())),
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
            )
        )
        
        # Use the value in another construct with
        get_parameter.get_response_field("Parameter.Value")
    '''

    @jsii.member(jsii_name="fromSdkCalls")
    @builtins.classmethod
    def from_sdk_calls(
        cls,
        *,
        resources: typing.Sequence[builtins.str],
    ) -> "AwsCustomResourcePolicy":
        '''Generate IAM Policy Statements from the configured SDK calls.

        Each SDK call with be translated to an IAM Policy Statement in the form of: ``call.service:call.action`` (e.g ``s3:PutObject``).

        This policy generator assumes the IAM policy name has the same name as the API
        call. This is true in 99% of cases, but there are exceptions (for example,
        S3's ``PutBucketLifecycleConfiguration`` requires
        ``s3:PutLifecycleConfiguration`` permissions, Lambda's ``Invoke`` requires
        ``lambda:InvokeFunction`` permissions). Use ``fromStatements`` if you want to
        do a call that requires different IAM action names.

        :param resources: The resources that the calls will have access to. It is best to use specific resource ARN's when possible. However, you can also use ``AwsCustomResourcePolicy.ANY_RESOURCE`` to allow access to all resources. For example, when ``onCreate`` is used to create a resource which you don't know the physical name of in advance. Note that will apply to ALL SDK calls.
        '''
        options = SdkCallsPolicyOptions(resources=resources)

        return typing.cast("AwsCustomResourcePolicy", jsii.sinvoke(cls, "fromSdkCalls", [options]))

    @jsii.member(jsii_name="fromStatements")
    @builtins.classmethod
    def from_statements(
        cls,
        statements: typing.Sequence[_PolicyStatement_0fe33853],
    ) -> "AwsCustomResourcePolicy":
        '''Explicit IAM Policy Statements.

        :param statements: the statements to propagate to the SDK calls.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__267132a8dbe09112fac8abcec56b61816ca5265080c0657023e152ec4eff48b1)
            check_type(argname="argument statements", value=statements, expected_type=type_hints["statements"])
        return typing.cast("AwsCustomResourcePolicy", jsii.sinvoke(cls, "fromStatements", [statements]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ANY_RESOURCE")
    def ANY_RESOURCE(cls) -> typing.List[builtins.str]:
        '''Use this constant to configure access to any resource.'''
        return typing.cast(typing.List[builtins.str], jsii.sget(cls, "ANY_RESOURCE"))

    @builtins.property
    @jsii.member(jsii_name="statements")
    def statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''statements for explicit policy.'''
        return typing.cast(typing.List[_PolicyStatement_0fe33853], jsii.get(self, "statements"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''resources for auto-generated from SDK calls.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resources"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.custom_resources.AwsCustomResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_name": "functionName",
        "install_latest_aws_sdk": "installLatestAwsSdk",
        "log_group": "logGroup",
        "log_retention": "logRetention",
        "memory_size": "memorySize",
        "on_create": "onCreate",
        "on_delete": "onDelete",
        "on_update": "onUpdate",
        "policy": "policy",
        "removal_policy": "removalPolicy",
        "resource_type": "resourceType",
        "role": "role",
        "timeout": "timeout",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class AwsCustomResourceProps:
    def __init__(
        self,
        *,
        function_name: typing.Optional[builtins.str] = None,
        install_latest_aws_sdk: typing.Optional[builtins.bool] = None,
        log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        on_create: typing.Optional[typing.Union["AwsSdkCall", typing.Dict[builtins.str, typing.Any]]] = None,
        on_delete: typing.Optional[typing.Union["AwsSdkCall", typing.Dict[builtins.str, typing.Any]]] = None,
        on_update: typing.Optional[typing.Union["AwsSdkCall", typing.Dict[builtins.str, typing.Any]]] = None,
        policy: typing.Optional[AwsCustomResourcePolicy] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        resource_type: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for AwsCustomResource.

        Note that at least onCreate, onUpdate or onDelete must be specified.

        :param function_name: A name for the singleton Lambda function implementing this custom resource. The function name will remain the same after the first AwsCustomResource is created in a stack. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param install_latest_aws_sdk: Whether to install the latest AWS SDK v2. If not specified, this uses whatever JavaScript SDK version is the default in AWS Lambda at the time of execution. Otherwise, installs the latest version from 'npmjs.com'. The installation takes around 60 seconds and requires internet connectivity. The default can be controlled using the context key ``@aws-cdk/customresources:installLatestAwsSdkDefault`` is. Default: - The value of ``@aws-cdk/customresources:installLatestAwsSdkDefault``, otherwise ``true``
        :param log_group: The Log Group used for logging of events emitted by the custom resource's lambda function. Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16. If you are deploying to another type of region, please check regional availability first. Default: - a default log group created by AWS Lambda
        :param log_retention: The number of days log events of the singleton Lambda function implementing this custom resource are kept in CloudWatch Logs. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: logs.RetentionDays.INFINITE
        :param memory_size: The memory size for the singleton Lambda function implementing this custom resource. Default: 512 mega in case if installLatestAwsSdk is false.
        :param on_create: The AWS SDK call to make when the resource is created. Default: - the call when the resource is updated
        :param on_delete: The AWS SDK call to make when the resource is deleted. Default: - no call
        :param on_update: The AWS SDK call to make when the resource is updated. Default: - no call
        :param policy: The policy that will be added to the execution role of the Lambda function implementing this custom resource provider. The custom resource also implements ``iam.IGrantable``, making it possible to use the ``grantXxx()`` methods. As this custom resource uses a singleton Lambda function, it's important to note the that function's role will eventually accumulate the permissions/grants from all resources. Note that a policy must be specified if ``role`` is not provided, as by default a new role is created which requires policy changes to access resources. Default: - no policy added
        :param removal_policy: The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy
        :param resource_type: Cloudformation Resource type. Default: - Custom::AWS
        :param role: The execution role for the singleton Lambda function implementing this custom resource provider. This role will apply to all ``AwsCustomResource`` instances in the stack. The role must be assumable by the ``lambda.amazonaws.com`` service principal. Default: - a new role is created
        :param timeout: The timeout for the singleton Lambda function implementing this custom resource. Default: Duration.minutes(2)
        :param vpc: The vpc to provision the lambda function in. Default: - the function is not provisioned inside a vpc.
        :param vpc_subnets: Which subnets from the VPC to place the lambda function in. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified

        :exampleMetadata: infused

        Example::

            get_parameter = cr.AwsCustomResource(self, "GetParameter",
                on_update=cr.AwsSdkCall( # will also be called for a CREATE event
                    service="SSM",
                    action="GetParameter",
                    parameters={
                        "Name": "my-parameter",
                        "WithDecryption": True
                    },
                    physical_resource_id=cr.PhysicalResourceId.of(Date.now().to_string())),
                policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                    resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
                )
            )
            
            # Use the value in another construct with
            get_parameter.get_response_field("Parameter.Value")
        '''
        if isinstance(on_create, dict):
            on_create = AwsSdkCall(**on_create)
        if isinstance(on_delete, dict):
            on_delete = AwsSdkCall(**on_delete)
        if isinstance(on_update, dict):
            on_update = AwsSdkCall(**on_update)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b5a9dace9a09081edfef936656f2d5670f198fb300a32c31957c93e5bb08c2f)
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument install_latest_aws_sdk", value=install_latest_aws_sdk, expected_type=type_hints["install_latest_aws_sdk"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument on_create", value=on_create, expected_type=type_hints["on_create"])
            check_type(argname="argument on_delete", value=on_delete, expected_type=type_hints["on_delete"])
            check_type(argname="argument on_update", value=on_update, expected_type=type_hints["on_update"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if function_name is not None:
            self._values["function_name"] = function_name
        if install_latest_aws_sdk is not None:
            self._values["install_latest_aws_sdk"] = install_latest_aws_sdk
        if log_group is not None:
            self._values["log_group"] = log_group
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if on_create is not None:
            self._values["on_create"] = on_create
        if on_delete is not None:
            self._values["on_delete"] = on_delete
        if on_update is not None:
            self._values["on_update"] = on_update
        if policy is not None:
            self._values["policy"] = policy
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if role is not None:
            self._values["role"] = role
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''A name for the singleton Lambda function implementing this custom resource.

        The function name will remain the same after the first AwsCustomResource is created in a stack.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_latest_aws_sdk(self) -> typing.Optional[builtins.bool]:
        '''Whether to install the latest AWS SDK v2.

        If not specified, this uses whatever JavaScript SDK version is the default in
        AWS Lambda at the time of execution.

        Otherwise, installs the latest version from 'npmjs.com'. The installation takes
        around 60 seconds and requires internet connectivity.

        The default can be controlled using the context key
        ``@aws-cdk/customresources:installLatestAwsSdkDefault`` is.

        :default: - The value of ``@aws-cdk/customresources:installLatestAwsSdkDefault``, otherwise ``true``
        '''
        result = self._values.get("install_latest_aws_sdk")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''The Log Group used for logging of events emitted by the custom resource's lambda function.

        Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16.
        If you are deploying to another type of region, please check regional availability first.

        :default: - a default log group created by AWS Lambda
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''The number of days log events of the singleton Lambda function implementing this custom resource are kept in CloudWatch Logs.

        This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can.
        ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it.

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''The memory size for the singleton Lambda function implementing this custom resource.

        :default: 512 mega in case if installLatestAwsSdk is false.
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def on_create(self) -> typing.Optional["AwsSdkCall"]:
        '''The AWS SDK call to make when the resource is created.

        :default: - the call when the resource is updated
        '''
        result = self._values.get("on_create")
        return typing.cast(typing.Optional["AwsSdkCall"], result)

    @builtins.property
    def on_delete(self) -> typing.Optional["AwsSdkCall"]:
        '''The AWS SDK call to make when the resource is deleted.

        :default: - no call
        '''
        result = self._values.get("on_delete")
        return typing.cast(typing.Optional["AwsSdkCall"], result)

    @builtins.property
    def on_update(self) -> typing.Optional["AwsSdkCall"]:
        '''The AWS SDK call to make when the resource is updated.

        :default: - no call
        '''
        result = self._values.get("on_update")
        return typing.cast(typing.Optional["AwsSdkCall"], result)

    @builtins.property
    def policy(self) -> typing.Optional[AwsCustomResourcePolicy]:
        '''The policy that will be added to the execution role of the Lambda function implementing this custom resource provider.

        The custom resource also implements ``iam.IGrantable``, making it possible
        to use the ``grantXxx()`` methods.

        As this custom resource uses a singleton Lambda function, it's important
        to note the that function's role will eventually accumulate the
        permissions/grants from all resources.

        Note that a policy must be specified if ``role`` is not provided, as
        by default a new role is created which requires policy changes to access
        resources.

        :default: - no policy added

        :see: Policy.fromSdkCalls
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[AwsCustomResourcePolicy], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The policy to apply when this resource is removed from the application.

        :default: cdk.RemovalPolicy.Destroy
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''Cloudformation Resource type.

        :default: - Custom::AWS
        '''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The execution role for the singleton Lambda function implementing this custom resource provider.

        This role will apply to all ``AwsCustomResource``
        instances in the stack. The role must be assumable by the
        ``lambda.amazonaws.com`` service principal.

        :default: - a new role is created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The timeout for the singleton Lambda function implementing this custom resource.

        :default: Duration.minutes(2)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''The vpc to provision the lambda function in.

        :default: - the function is not provisioned inside a vpc.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Which subnets from the VPC to place the lambda function in.

        Only used if 'vpc' is supplied. Note: internet access for Lambdas
        requires a NAT gateway, so picking Public subnets is not allowed.

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsCustomResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.custom_resources.AwsSdkCall",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "service": "service",
        "api_version": "apiVersion",
        "assumed_role_arn": "assumedRoleArn",
        "ignore_error_codes_matching": "ignoreErrorCodesMatching",
        "logging": "logging",
        "output_paths": "outputPaths",
        "parameters": "parameters",
        "physical_resource_id": "physicalResourceId",
        "region": "region",
    },
)
class AwsSdkCall:
    def __init__(
        self,
        *,
        action: builtins.str,
        service: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        assumed_role_arn: typing.Optional[builtins.str] = None,
        ignore_error_codes_matching: typing.Optional[builtins.str] = None,
        logging: typing.Optional["Logging"] = None,
        output_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Any = None,
        physical_resource_id: typing.Optional["PhysicalResourceId"] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''An AWS SDK call.

        :param action: The service action to call. This is the name of an AWS API call, in one of the following forms: - An API call name as found in the API Reference documentation (``GetObject``) - The API call name starting with a lowercase letter (``getObject``) - The AWS SDK for JavaScript v3 command class name (``GetObjectCommand``)
        :param service: The service to call. This is the name of an AWS service, in one of the following forms: - An AWS SDK for JavaScript v3 package name (``@aws-sdk/client-api-gateway``) - An AWS SDK for JavaScript v3 client name (``api-gateway``) - An AWS SDK for JavaScript v2 constructor name (``APIGateway``) - A lowercase AWS SDK for JavaScript v2 constructor name (``apigateway``)
        :param api_version: API version to use for the service. Default: - use latest available API version
        :param assumed_role_arn: Used for running the SDK calls in underlying lambda with a different role. Can be used primarily for cross-account requests to for example connect hostedzone with a shared vpc. Region controls where assumeRole call is made. Example for Route53 / associateVPCWithHostedZone Default: - run without assuming role
        :param ignore_error_codes_matching: The regex pattern to use to catch API errors. The ``code`` property of the ``Error`` object will be tested against this pattern. If there is a match an error will not be thrown. Default: - do not catch errors
        :param logging: A property used to configure logging during lambda function execution. Note: The default Logging configuration is all. This configuration will enable logging on all logged data in the lambda handler. This includes: - The event object that is received by the lambda handler - The response received after making a API call - The response object that the lambda handler will return - SDK versioning information - Caught and uncaught errors Default: Logging.all()
        :param output_paths: Restrict the data returned by the custom resource to specific paths in the API response. Use this to limit the data returned by the custom resource if working with API calls that could potentially result in custom response objects exceeding the hard limit of 4096 bytes. Example for ECS / updateService: ['service.deploymentConfiguration.maximumPercent'] Default: - return all data
        :param parameters: The parameters for the service action. Default: - no parameters
        :param physical_resource_id: The physical resource id of the custom resource for this call. Mandatory for onCreate call. In onUpdate, you can omit this to passthrough it from request. Default: - no physical resource id
        :param region: The region to send service requests to. **Note: Cross-region operations are generally considered an anti-pattern.** **Consider first deploying a stack in that region.** Default: - the region where this custom resource is deployed

        Example::

            cr.AwsCustomResource(self, "GetParameterCustomResource",
                on_update=cr.AwsSdkCall( # will also be called for a CREATE event
                    service="SSM",
                    action="getParameter",
                    parameters={
                        "Name": "my-parameter",
                        "WithDecryption": True
                    },
                    physical_resource_id=cr.PhysicalResourceId.from_response("Parameter.ARN")),
                policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                    resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af7bb124668b93c6ce7d641df2daeabfe424e271742385a76e7e56ec91c39dc9)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument assumed_role_arn", value=assumed_role_arn, expected_type=type_hints["assumed_role_arn"])
            check_type(argname="argument ignore_error_codes_matching", value=ignore_error_codes_matching, expected_type=type_hints["ignore_error_codes_matching"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument output_paths", value=output_paths, expected_type=type_hints["output_paths"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument physical_resource_id", value=physical_resource_id, expected_type=type_hints["physical_resource_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "service": service,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if assumed_role_arn is not None:
            self._values["assumed_role_arn"] = assumed_role_arn
        if ignore_error_codes_matching is not None:
            self._values["ignore_error_codes_matching"] = ignore_error_codes_matching
        if logging is not None:
            self._values["logging"] = logging
        if output_paths is not None:
            self._values["output_paths"] = output_paths
        if parameters is not None:
            self._values["parameters"] = parameters
        if physical_resource_id is not None:
            self._values["physical_resource_id"] = physical_resource_id
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def action(self) -> builtins.str:
        '''The service action to call.

        This is the name of an AWS API call, in one of the following forms:

        - An API call name as found in the API Reference documentation (``GetObject``)
        - The API call name starting with a lowercase letter (``getObject``)
        - The AWS SDK for JavaScript v3 command class name (``GetObjectCommand``)

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The service to call.

        This is the name of an AWS service, in one of the following forms:

        - An AWS SDK for JavaScript v3 package name (``@aws-sdk/client-api-gateway``)
        - An AWS SDK for JavaScript v3 client name (``api-gateway``)
        - An AWS SDK for JavaScript v2 constructor name (``APIGateway``)
        - A lowercase AWS SDK for JavaScript v2 constructor name (``apigateway``)

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version to use for the service.

        :default: - use latest available API version

        :see: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/locking-api-versions.html
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assumed_role_arn(self) -> typing.Optional[builtins.str]:
        '''Used for running the SDK calls in underlying lambda with a different role.

        Can be used primarily for cross-account requests to for example connect
        hostedzone with a shared vpc.
        Region controls where assumeRole call is made.

        Example for Route53 / associateVPCWithHostedZone

        :default: - run without assuming role
        '''
        result = self._values.get("assumed_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_error_codes_matching(self) -> typing.Optional[builtins.str]:
        '''The regex pattern to use to catch API errors.

        The ``code`` property of the
        ``Error`` object will be tested against this pattern. If there is a match an
        error will not be thrown.

        :default: - do not catch errors
        '''
        result = self._values.get("ignore_error_codes_matching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging(self) -> typing.Optional["Logging"]:
        '''A property used to configure logging during lambda function execution.

        Note: The default Logging configuration is all. This configuration will enable logging on all logged data
        in the lambda handler. This includes:

        - The event object that is received by the lambda handler
        - The response received after making a API call
        - The response object that the lambda handler will return
        - SDK versioning information
        - Caught and uncaught errors

        :default: Logging.all()
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["Logging"], result)

    @builtins.property
    def output_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Restrict the data returned by the custom resource to specific paths in the API response.

        Use this to limit the data returned by the custom
        resource if working with API calls that could potentially result in custom
        response objects exceeding the hard limit of 4096 bytes.

        Example for ECS / updateService: ['service.deploymentConfiguration.maximumPercent']

        :default: - return all data
        '''
        result = self._values.get("output_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''The parameters for the service action.

        :default: - no parameters

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def physical_resource_id(self) -> typing.Optional["PhysicalResourceId"]:
        '''The physical resource id of the custom resource for this call.

        Mandatory for onCreate call.
        In onUpdate, you can omit this to passthrough it from request.

        :default: - no physical resource id
        '''
        result = self._values.get("physical_resource_id")
        return typing.cast(typing.Optional["PhysicalResourceId"], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region to send service requests to.

        **Note: Cross-region operations are generally considered an anti-pattern.**
        **Consider first deploying a stack in that region.**

        :default: - the region where this custom resource is deployed
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsSdkCall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.custom_resources.LogOptions",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "include_execution_data": "includeExecutionData",
        "level": "level",
    },
)
class LogOptions:
    def __init__(
        self,
        *,
        destination: typing.Optional[_ILogGroup_3c4fa718] = None,
        include_execution_data: typing.Optional[builtins.bool] = None,
        level: typing.Optional[_LogLevel_be1990fe] = None,
    ) -> None:
        '''Log Options for the state machine.

        :param destination: The log group where the execution history events will be logged. Default: - a new log group will be created
        :param include_execution_data: Determines whether execution data is included in your log. Default: - false
        :param level: Defines which category of execution history events are logged. Default: - ERROR

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            from aws_cdk import aws_stepfunctions as stepfunctions
            from aws_cdk import custom_resources
            
            # log_group: logs.LogGroup
            
            log_options = custom_resources.LogOptions(
                destination=log_group,
                include_execution_data=False,
                level=stepfunctions.LogLevel.OFF
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2622296f61199d2b10825c21d976c0578e9488ad1b2b7635565f604c598734b7)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument include_execution_data", value=include_execution_data, expected_type=type_hints["include_execution_data"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if include_execution_data is not None:
            self._values["include_execution_data"] = include_execution_data
        if level is not None:
            self._values["level"] = level

    @builtins.property
    def destination(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''The log group where the execution history events will be logged.

        :default: - a new log group will be created
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def include_execution_data(self) -> typing.Optional[builtins.bool]:
        '''Determines whether execution data is included in your log.

        :default: - false
        '''
        result = self._values.get("include_execution_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def level(self) -> typing.Optional[_LogLevel_be1990fe]:
        '''Defines which category of execution history events are logged.

        :default: - ERROR
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[_LogLevel_be1990fe], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Logging(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.custom_resources.Logging",
):
    '''A class used to configure Logging during AwsCustomResource SDK calls.

    :exampleMetadata: infused

    Example::

        get_parameter = cr.AwsCustomResource(self, "GetParameter",
            on_update=cr.AwsSdkCall(
                service="SSM",
                action="GetParameter",
                parameters={
                    "Name": "my-parameter",
                    "WithDecryption": True
                },
                physical_resource_id=cr.PhysicalResourceId.of(Date.now().to_string()),
                logging=cr.Logging.with_data_hidden()
            ),
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
            )
        )
    '''

    def __init__(
        self,
        *,
        log_api_response_data: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param log_api_response_data: Whether or not to log data associated with the API call response. Default: true
        '''
        props = LoggingProps(log_api_response_data=log_api_response_data)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(cls) -> "Logging":
        '''Enables logging of all logged data in the lambda handler.

        This includes the event object, the API call response, all fields in the response object
        returned by the lambda, and any errors encountered.
        '''
        return typing.cast("Logging", jsii.sinvoke(cls, "all", []))

    @jsii.member(jsii_name="withDataHidden")
    @builtins.classmethod
    def with_data_hidden(cls) -> "Logging":
        '''Hides logging of data associated with the API call response.

        This includes hiding the raw API
        call response and the ``Data`` field associated with the lambda handler response.
        '''
        return typing.cast("Logging", jsii.sinvoke(cls, "withDataHidden", []))


class _LoggingProxy(Logging):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Logging).__jsii_proxy_class__ = lambda : _LoggingProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.custom_resources.LoggingProps",
    jsii_struct_bases=[],
    name_mapping={"log_api_response_data": "logApiResponseData"},
)
class LoggingProps:
    def __init__(
        self,
        *,
        log_api_response_data: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties used to initialize Logging.

        :param log_api_response_data: Whether or not to log data associated with the API call response. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import custom_resources
            
            logging_props = custom_resources.LoggingProps(
                log_api_response_data=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da0d46a1eb4b059395d06daee7dcb9417dffd0b4cf8e8942cbe0a6549f0faf4b)
            check_type(argname="argument log_api_response_data", value=log_api_response_data, expected_type=type_hints["log_api_response_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if log_api_response_data is not None:
            self._values["log_api_response_data"] = log_api_response_data

    @builtins.property
    def log_api_response_data(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to log data associated with the API call response.

        :default: true
        '''
        result = self._values.get("log_api_response_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PhysicalResourceId(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.custom_resources.PhysicalResourceId",
):
    '''Physical ID of the custom resource.

    :exampleMetadata: infused

    Example::

        get_parameter = cr.AwsCustomResource(self, "AssociateVPCWithHostedZone",
            on_create=cr.AwsSdkCall(
                assumed_role_arn="arn:aws:iam::OTHERACCOUNT:role/CrossAccount/ManageHostedZoneConnections",
                service="Route53",
                action="AssociateVPCWithHostedZone",
                parameters={
                    "HostedZoneId": "hz-123",
                    "VPC": {
                        "VPCId": "vpc-123",
                        "VPCRegion": "region-for-vpc"
                    }
                },
                physical_resource_id=cr.PhysicalResourceId.of("${vpcStack.SharedVpc.VpcId}-${vpcStack.Region}-${PrivateHostedZone.HostedZoneId}")
            ),
            # Will ignore any resource and use the assumedRoleArn as resource and 'sts:AssumeRole' for service:action
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
            )
        )
    '''

    @jsii.member(jsii_name="fromResponse")
    @builtins.classmethod
    def from_response(cls, response_path: builtins.str) -> "PhysicalResourceId":
        '''Extract the physical resource id from the path (dot notation) to the data in the API call response.

        :param response_path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6baa8764ccdf77f11bd8f80af9fafec69f56b719c1a237caae55c7f988e174b6)
            check_type(argname="argument response_path", value=response_path, expected_type=type_hints["response_path"])
        return typing.cast("PhysicalResourceId", jsii.sinvoke(cls, "fromResponse", [response_path]))

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, id: builtins.str) -> "PhysicalResourceId":
        '''Explicit physical resource id.

        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdca735a77f74ade2070f6a3cbaf95d939ee16657cec7f53ec60b2df0a096bd2)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast("PhysicalResourceId", jsii.sinvoke(cls, "of", [id]))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> typing.Optional[builtins.str]:
        '''Literal string to be used as the physical id.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="responsePath")
    def response_path(self) -> typing.Optional[builtins.str]:
        '''Path to a response data element to be used as the physical id.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responsePath"))


@jsii.implements(_IResolvable_da3f097b)
class PhysicalResourceIdReference(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.custom_resources.PhysicalResourceIdReference",
):
    '''Reference to the physical resource id that can be passed to the AWS operation as a parameter.

    :exampleMetadata: infused

    Example::

        aws_custom = cr.AwsCustomResource(self, "aws-custom",
            on_create=cr.AwsSdkCall(
                service="...",
                action="...",
                parameters={
                    "text": "..."
                },
                physical_resource_id=cr.PhysicalResourceId.of("...")
            ),
            on_update=cr.AwsSdkCall(
                service="...",
                action="...",
                parameters={
                    "text": "...",
                    "resource_id": cr.PhysicalResourceIdReference()
                }
            ),
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
            )
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="resolve")
    def resolve(self, _context: _IResolveContext_b2df1921) -> typing.Any:
        '''Produce the Token's value at resolution time.

        :param _context: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784d4e05d144bc71f705b7f70440a6f66fee012cf9cf6f0bea5bbf88c7b49fd7)
            check_type(argname="argument _context", value=_context, expected_type=type_hints["_context"])
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [_context]))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> builtins.str:
        '''toJSON serialization to replace ``PhysicalResourceIdReference`` with a magic string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toJSON", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Return a string representation of this resolvable object.

        Returns a reversible string representation.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''The creation stack of this resolvable which will be appended to errors thrown during resolution.

        This may return an array with a single informational element indicating how
        to get this property populated, if it was skipped for performance reasons.
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creationStack"))


class Provider(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.custom_resources.Provider",
):
    '''Defines an AWS CloudFormation custom resource provider.

    :exampleMetadata: infused

    Example::

        # on_event: lambda.Function
        # is_complete: lambda.Function
        # my_role: iam.Role
        
        my_provider = cr.Provider(self, "MyProvider",
            on_event_handler=on_event,
            is_complete_handler=is_complete,
            log_group=logs.LogGroup(self, "MyProviderLogs",
                retention=logs.RetentionDays.ONE_DAY
            ),
            role=my_role,
            provider_function_name="the-lambda-name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        on_event_handler: _IFunction_6adb0ab8,
        disable_waiter_state_machine_logging: typing.Optional[builtins.bool] = None,
        is_complete_handler: typing.Optional[_IFunction_6adb0ab8] = None,
        log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        provider_function_env_encryption: typing.Optional[_IKey_5f11635f] = None,
        provider_function_name: typing.Optional[builtins.str] = None,
        query_interval: typing.Optional[_Duration_4839e8c3] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        total_timeout: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        waiter_state_machine_log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param on_event_handler: The AWS Lambda function to invoke for all resource lifecycle operations (CREATE/UPDATE/DELETE). This function is responsible to begin the requested resource operation (CREATE/UPDATE/DELETE) and return any additional properties to add to the event, which will later be passed to ``isComplete``. The ``PhysicalResourceId`` property must be included in the response.
        :param disable_waiter_state_machine_logging: Whether logging for the waiter state machine is disabled. Default: - false
        :param is_complete_handler: The AWS Lambda function to invoke in order to determine if the operation is complete. This function will be called immediately after ``onEvent`` and then periodically based on the configured query interval as long as it returns ``false``. If the function still returns ``false`` and the alloted timeout has passed, the operation will fail. Default: - provider is synchronous. This means that the ``onEvent`` handler is expected to finish all lifecycle operations within the initial invocation.
        :param log_group: The Log Group used for logging of events emitted by the custom resource's lambda function. Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16. If you are deploying to another type of region, please check regional availability first. Default: - a default log group created by AWS Lambda
        :param log_retention: The number of days framework log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: logs.RetentionDays.INFINITE
        :param provider_function_env_encryption: AWS KMS key used to encrypt provider lambda's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK)
        :param provider_function_name: Provider Lambda name. The provider lambda function name. Default: - CloudFormation default name from unique physical ID
        :param query_interval: Time between calls to the ``isComplete`` handler which determines if the resource has been stabilized. The first ``isComplete`` will be called immediately after ``handler`` and then every ``queryInterval`` seconds, and until ``timeout`` has been reached or until ``isComplete`` returns ``true``. Default: Duration.seconds(5)
        :param role: AWS Lambda execution role. The role that will be assumed by the AWS Lambda. Must be assumable by the 'lambda.amazonaws.com' service principal. Default: - A default role will be created.
        :param security_groups: Security groups to attach to the provider functions. Only used if 'vpc' is supplied Default: - If ``vpc`` is not supplied, no security groups are attached. Otherwise, a dedicated security group is created for each function.
        :param total_timeout: Total timeout for the entire operation. The maximum timeout is 1 hour (yes, it can exceed the AWS Lambda 15 minutes) Default: Duration.minutes(30)
        :param vpc: The vpc to provision the lambda functions in. Default: - functions are not provisioned inside a vpc.
        :param vpc_subnets: Which subnets from the VPC to place the lambda functions in. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param waiter_state_machine_log_options: Defines what execution history events of the waiter state machine are logged and where they are logged. Default: - A default log group will be created if logging for the waiter state machine is enabled.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29415d7bf7977fcf110b77ce69cec309dcf0404601944735020770ddfe2b01a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ProviderProps(
            on_event_handler=on_event_handler,
            disable_waiter_state_machine_logging=disable_waiter_state_machine_logging,
            is_complete_handler=is_complete_handler,
            log_group=log_group,
            log_retention=log_retention,
            provider_function_env_encryption=provider_function_env_encryption,
            provider_function_name=provider_function_name,
            query_interval=query_interval,
            role=role,
            security_groups=security_groups,
            total_timeout=total_timeout,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            waiter_state_machine_log_options=waiter_state_machine_log_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="onEventHandler")
    def on_event_handler(self) -> _IFunction_6adb0ab8:
        '''The user-defined AWS Lambda function which is invoked for all resource lifecycle operations (CREATE/UPDATE/DELETE).'''
        return typing.cast(_IFunction_6adb0ab8, jsii.get(self, "onEventHandler"))

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> builtins.str:
        '''The service token to use in order to define custom resources that are backed by this provider.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceToken"))

    @builtins.property
    @jsii.member(jsii_name="isCompleteHandler")
    def is_complete_handler(self) -> typing.Optional[_IFunction_6adb0ab8]:
        '''The user-defined AWS Lambda function which is invoked asynchronously in order to determine if the operation is complete.'''
        return typing.cast(typing.Optional[_IFunction_6adb0ab8], jsii.get(self, "isCompleteHandler"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.custom_resources.ProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "on_event_handler": "onEventHandler",
        "disable_waiter_state_machine_logging": "disableWaiterStateMachineLogging",
        "is_complete_handler": "isCompleteHandler",
        "log_group": "logGroup",
        "log_retention": "logRetention",
        "provider_function_env_encryption": "providerFunctionEnvEncryption",
        "provider_function_name": "providerFunctionName",
        "query_interval": "queryInterval",
        "role": "role",
        "security_groups": "securityGroups",
        "total_timeout": "totalTimeout",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "waiter_state_machine_log_options": "waiterStateMachineLogOptions",
    },
)
class ProviderProps:
    def __init__(
        self,
        *,
        on_event_handler: _IFunction_6adb0ab8,
        disable_waiter_state_machine_logging: typing.Optional[builtins.bool] = None,
        is_complete_handler: typing.Optional[_IFunction_6adb0ab8] = None,
        log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        provider_function_env_encryption: typing.Optional[_IKey_5f11635f] = None,
        provider_function_name: typing.Optional[builtins.str] = None,
        query_interval: typing.Optional[_Duration_4839e8c3] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        total_timeout: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        waiter_state_machine_log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Initialization properties for the ``Provider`` construct.

        :param on_event_handler: The AWS Lambda function to invoke for all resource lifecycle operations (CREATE/UPDATE/DELETE). This function is responsible to begin the requested resource operation (CREATE/UPDATE/DELETE) and return any additional properties to add to the event, which will later be passed to ``isComplete``. The ``PhysicalResourceId`` property must be included in the response.
        :param disable_waiter_state_machine_logging: Whether logging for the waiter state machine is disabled. Default: - false
        :param is_complete_handler: The AWS Lambda function to invoke in order to determine if the operation is complete. This function will be called immediately after ``onEvent`` and then periodically based on the configured query interval as long as it returns ``false``. If the function still returns ``false`` and the alloted timeout has passed, the operation will fail. Default: - provider is synchronous. This means that the ``onEvent`` handler is expected to finish all lifecycle operations within the initial invocation.
        :param log_group: The Log Group used for logging of events emitted by the custom resource's lambda function. Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16. If you are deploying to another type of region, please check regional availability first. Default: - a default log group created by AWS Lambda
        :param log_retention: The number of days framework log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: logs.RetentionDays.INFINITE
        :param provider_function_env_encryption: AWS KMS key used to encrypt provider lambda's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK)
        :param provider_function_name: Provider Lambda name. The provider lambda function name. Default: - CloudFormation default name from unique physical ID
        :param query_interval: Time between calls to the ``isComplete`` handler which determines if the resource has been stabilized. The first ``isComplete`` will be called immediately after ``handler`` and then every ``queryInterval`` seconds, and until ``timeout`` has been reached or until ``isComplete`` returns ``true``. Default: Duration.seconds(5)
        :param role: AWS Lambda execution role. The role that will be assumed by the AWS Lambda. Must be assumable by the 'lambda.amazonaws.com' service principal. Default: - A default role will be created.
        :param security_groups: Security groups to attach to the provider functions. Only used if 'vpc' is supplied Default: - If ``vpc`` is not supplied, no security groups are attached. Otherwise, a dedicated security group is created for each function.
        :param total_timeout: Total timeout for the entire operation. The maximum timeout is 1 hour (yes, it can exceed the AWS Lambda 15 minutes) Default: Duration.minutes(30)
        :param vpc: The vpc to provision the lambda functions in. Default: - functions are not provisioned inside a vpc.
        :param vpc_subnets: Which subnets from the VPC to place the lambda functions in. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param waiter_state_machine_log_options: Defines what execution history events of the waiter state machine are logged and where they are logged. Default: - A default log group will be created if logging for the waiter state machine is enabled.

        :exampleMetadata: infused

        Example::

            # on_event: lambda.Function
            # is_complete: lambda.Function
            # my_role: iam.Role
            
            my_provider = cr.Provider(self, "MyProvider",
                on_event_handler=on_event,
                is_complete_handler=is_complete,
                log_group=logs.LogGroup(self, "MyProviderLogs",
                    retention=logs.RetentionDays.ONE_DAY
                ),
                role=my_role,
                provider_function_name="the-lambda-name"
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if isinstance(waiter_state_machine_log_options, dict):
            waiter_state_machine_log_options = LogOptions(**waiter_state_machine_log_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b03803ee02437d8d83814282c700ede5633030e4d9f7ebdaf3b9d075b0cbdb)
            check_type(argname="argument on_event_handler", value=on_event_handler, expected_type=type_hints["on_event_handler"])
            check_type(argname="argument disable_waiter_state_machine_logging", value=disable_waiter_state_machine_logging, expected_type=type_hints["disable_waiter_state_machine_logging"])
            check_type(argname="argument is_complete_handler", value=is_complete_handler, expected_type=type_hints["is_complete_handler"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument provider_function_env_encryption", value=provider_function_env_encryption, expected_type=type_hints["provider_function_env_encryption"])
            check_type(argname="argument provider_function_name", value=provider_function_name, expected_type=type_hints["provider_function_name"])
            check_type(argname="argument query_interval", value=query_interval, expected_type=type_hints["query_interval"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument total_timeout", value=total_timeout, expected_type=type_hints["total_timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument waiter_state_machine_log_options", value=waiter_state_machine_log_options, expected_type=type_hints["waiter_state_machine_log_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "on_event_handler": on_event_handler,
        }
        if disable_waiter_state_machine_logging is not None:
            self._values["disable_waiter_state_machine_logging"] = disable_waiter_state_machine_logging
        if is_complete_handler is not None:
            self._values["is_complete_handler"] = is_complete_handler
        if log_group is not None:
            self._values["log_group"] = log_group
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if provider_function_env_encryption is not None:
            self._values["provider_function_env_encryption"] = provider_function_env_encryption
        if provider_function_name is not None:
            self._values["provider_function_name"] = provider_function_name
        if query_interval is not None:
            self._values["query_interval"] = query_interval
        if role is not None:
            self._values["role"] = role
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if total_timeout is not None:
            self._values["total_timeout"] = total_timeout
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if waiter_state_machine_log_options is not None:
            self._values["waiter_state_machine_log_options"] = waiter_state_machine_log_options

    @builtins.property
    def on_event_handler(self) -> _IFunction_6adb0ab8:
        '''The AWS Lambda function to invoke for all resource lifecycle operations (CREATE/UPDATE/DELETE).

        This function is responsible to begin the requested resource operation
        (CREATE/UPDATE/DELETE) and return any additional properties to add to the
        event, which will later be passed to ``isComplete``. The ``PhysicalResourceId``
        property must be included in the response.
        '''
        result = self._values.get("on_event_handler")
        assert result is not None, "Required property 'on_event_handler' is missing"
        return typing.cast(_IFunction_6adb0ab8, result)

    @builtins.property
    def disable_waiter_state_machine_logging(self) -> typing.Optional[builtins.bool]:
        '''Whether logging for the waiter state machine is disabled.

        :default: - false
        '''
        result = self._values.get("disable_waiter_state_machine_logging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_complete_handler(self) -> typing.Optional[_IFunction_6adb0ab8]:
        '''The AWS Lambda function to invoke in order to determine if the operation is complete.

        This function will be called immediately after ``onEvent`` and then
        periodically based on the configured query interval as long as it returns
        ``false``. If the function still returns ``false`` and the alloted timeout has
        passed, the operation will fail.

        :default:

        - provider is synchronous. This means that the ``onEvent`` handler
        is expected to finish all lifecycle operations within the initial invocation.
        '''
        result = self._values.get("is_complete_handler")
        return typing.cast(typing.Optional[_IFunction_6adb0ab8], result)

    @builtins.property
    def log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''The Log Group used for logging of events emitted by the custom resource's lambda function.

        Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16.
        If you are deploying to another type of region, please check regional availability first.

        :default: - a default log group created by AWS Lambda
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''The number of days framework log events are kept in CloudWatch Logs.

        When
        updating this property, unsetting it doesn't remove the log retention policy.
        To remove the retention policy, set the value to ``INFINITE``.

        This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can.
        ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it.

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def provider_function_env_encryption(self) -> typing.Optional[_IKey_5f11635f]:
        '''AWS KMS key used to encrypt provider lambda's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK)
        '''
        result = self._values.get("provider_function_env_encryption")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def provider_function_name(self) -> typing.Optional[builtins.str]:
        '''Provider Lambda name.

        The provider lambda function name.

        :default: - CloudFormation default name from unique physical ID
        '''
        result = self._values.get("provider_function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Time between calls to the ``isComplete`` handler which determines if the resource has been stabilized.

        The first ``isComplete`` will be called immediately after ``handler`` and then
        every ``queryInterval`` seconds, and until ``timeout`` has been reached or until
        ``isComplete`` returns ``true``.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("query_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''AWS Lambda execution role.

        The role that will be assumed by the AWS Lambda.
        Must be assumable by the 'lambda.amazonaws.com' service principal.

        :default: - A default role will be created.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''Security groups to attach to the provider functions.

        Only used if 'vpc' is supplied

        :default:

        - If ``vpc`` is not supplied, no security groups are attached. Otherwise, a dedicated security
        group is created for each function.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def total_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Total timeout for the entire operation.

        The maximum timeout is 1 hour (yes, it can exceed the AWS Lambda 15 minutes)

        :default: Duration.minutes(30)
        '''
        result = self._values.get("total_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''The vpc to provision the lambda functions in.

        :default: - functions are not provisioned inside a vpc.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Which subnets from the VPC to place the lambda functions in.

        Only used if 'vpc' is supplied. Note: internet access for Lambdas
        requires a NAT gateway, so picking Public subnets is not allowed.

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def waiter_state_machine_log_options(self) -> typing.Optional[LogOptions]:
        '''Defines what execution history events of the waiter state machine are logged and where they are logged.

        :default: - A default log group will be created if logging for the waiter state machine is enabled.
        '''
        result = self._values.get("waiter_state_machine_log_options")
        return typing.cast(typing.Optional[LogOptions], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.custom_resources.SdkCallsPolicyOptions",
    jsii_struct_bases=[],
    name_mapping={"resources": "resources"},
)
class SdkCallsPolicyOptions:
    def __init__(self, *, resources: typing.Sequence[builtins.str]) -> None:
        '''Options for the auto-generation of policies based on the configured SDK calls.

        :param resources: The resources that the calls will have access to. It is best to use specific resource ARN's when possible. However, you can also use ``AwsCustomResourcePolicy.ANY_RESOURCE`` to allow access to all resources. For example, when ``onCreate`` is used to create a resource which you don't know the physical name of in advance. Note that will apply to ALL SDK calls.

        :exampleMetadata: infused

        Example::

            get_parameter = cr.AwsCustomResource(self, "GetParameter",
                on_update=cr.AwsSdkCall( # will also be called for a CREATE event
                    service="SSM",
                    action="GetParameter",
                    parameters={
                        "Name": "my-parameter",
                        "WithDecryption": True
                    },
                    physical_resource_id=cr.PhysicalResourceId.of(Date.now().to_string())),
                policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
                    resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
                )
            )
            
            # Use the value in another construct with
            get_parameter.get_response_field("Parameter.Value")
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cd00e8add38e42b6c4d7db0390a899ccaf5bbe0367bfb387986125dacc7a297)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resources": resources,
        }

    @builtins.property
    def resources(self) -> typing.List[builtins.str]:
        '''The resources that the calls will have access to.

        It is best to use specific resource ARN's when possible. However, you can also use ``AwsCustomResourcePolicy.ANY_RESOURCE``
        to allow access to all resources. For example, when ``onCreate`` is used to create a resource which you don't
        know the physical name of in advance.

        Note that will apply to ALL SDK calls.
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SdkCallsPolicyOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WaiterStateMachine(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.custom_resources.WaiterStateMachine",
):
    '''A very simple StateMachine construct highly customized to the provider framework.

    We previously used ``CfnResource`` instead of ``CfnStateMachine`` to avoid depending
    on ``aws-stepfunctions`` module, but now it is okay.

    The state machine continuously calls the isCompleteHandler, until it succeeds or times out.
    The handler is called ``maxAttempts`` times with an ``interval`` duration and a ``backoffRate`` rate.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_lambda as lambda_
        from aws_cdk import aws_logs as logs
        from aws_cdk import aws_stepfunctions as stepfunctions
        from aws_cdk import custom_resources
        
        # function_: lambda.Function
        # log_group: logs.LogGroup
        
        waiter_state_machine = custom_resources.WaiterStateMachine(self, "MyWaiterStateMachine",
            backoff_rate=123,
            interval=cdk.Duration.minutes(30),
            is_complete_handler=function_,
            max_attempts=123,
            timeout_handler=function_,
        
            # the properties below are optional
            disable_logging=False,
            log_options=custom_resources.LogOptions(
                destination=log_group,
                include_execution_data=False,
                level=stepfunctions.LogLevel.OFF
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        backoff_rate: jsii.Number,
        interval: _Duration_4839e8c3,
        is_complete_handler: _IFunction_6adb0ab8,
        max_attempts: jsii.Number,
        timeout_handler: _IFunction_6adb0ab8,
        disable_logging: typing.Optional[builtins.bool] = None,
        log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param backoff_rate: Backoff between attempts.
        :param interval: The interval to wait between attempts.
        :param is_complete_handler: The main handler that notifies if the waiter to decide 'complete' or 'incomplete'.
        :param max_attempts: Number of attempts.
        :param timeout_handler: The handler to call if the waiter times out and is incomplete.
        :param disable_logging: Whether logging for the state machine is disabled. Default: - false
        :param log_options: Defines what execution history events are logged and where they are logged. Default: - A default log group will be created if logging is enabled.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12427b739f326cdb535d2aaf4a70f10977eec5711902d4e5e395f0b8c9bb184e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = WaiterStateMachineProps(
            backoff_rate=backoff_rate,
            interval=interval,
            is_complete_handler=is_complete_handler,
            max_attempts=max_attempts,
            timeout_handler=timeout_handler,
            disable_logging=disable_logging,
            log_options=log_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="grantStartExecution")
    def grant_start_execution(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions on StartExecution of the state machine.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c3d1c306ca04ebd1194ce4f97bed6aa9510a02067654b39f43a1ecef601e3db)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantStartExecution", [identity]))

    @builtins.property
    @jsii.member(jsii_name="stateMachineArn")
    def state_machine_arn(self) -> builtins.str:
        '''The ARN of the state machine.'''
        return typing.cast(builtins.str, jsii.get(self, "stateMachineArn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.custom_resources.WaiterStateMachineProps",
    jsii_struct_bases=[],
    name_mapping={
        "backoff_rate": "backoffRate",
        "interval": "interval",
        "is_complete_handler": "isCompleteHandler",
        "max_attempts": "maxAttempts",
        "timeout_handler": "timeoutHandler",
        "disable_logging": "disableLogging",
        "log_options": "logOptions",
    },
)
class WaiterStateMachineProps:
    def __init__(
        self,
        *,
        backoff_rate: jsii.Number,
        interval: _Duration_4839e8c3,
        is_complete_handler: _IFunction_6adb0ab8,
        max_attempts: jsii.Number,
        timeout_handler: _IFunction_6adb0ab8,
        disable_logging: typing.Optional[builtins.bool] = None,
        log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Initialization properties for the ``WaiterStateMachine`` construct.

        :param backoff_rate: Backoff between attempts.
        :param interval: The interval to wait between attempts.
        :param is_complete_handler: The main handler that notifies if the waiter to decide 'complete' or 'incomplete'.
        :param max_attempts: Number of attempts.
        :param timeout_handler: The handler to call if the waiter times out and is incomplete.
        :param disable_logging: Whether logging for the state machine is disabled. Default: - false
        :param log_options: Defines what execution history events are logged and where they are logged. Default: - A default log group will be created if logging is enabled.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_lambda as lambda_
            from aws_cdk import aws_logs as logs
            from aws_cdk import aws_stepfunctions as stepfunctions
            from aws_cdk import custom_resources
            
            # function_: lambda.Function
            # log_group: logs.LogGroup
            
            waiter_state_machine_props = custom_resources.WaiterStateMachineProps(
                backoff_rate=123,
                interval=cdk.Duration.minutes(30),
                is_complete_handler=function_,
                max_attempts=123,
                timeout_handler=function_,
            
                # the properties below are optional
                disable_logging=False,
                log_options=custom_resources.LogOptions(
                    destination=log_group,
                    include_execution_data=False,
                    level=stepfunctions.LogLevel.OFF
                )
            )
        '''
        if isinstance(log_options, dict):
            log_options = LogOptions(**log_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__569ff1333551048ad82f7261bcf43cbefe118e974cba179165c355fc9347fc13)
            check_type(argname="argument backoff_rate", value=backoff_rate, expected_type=type_hints["backoff_rate"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument is_complete_handler", value=is_complete_handler, expected_type=type_hints["is_complete_handler"])
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument timeout_handler", value=timeout_handler, expected_type=type_hints["timeout_handler"])
            check_type(argname="argument disable_logging", value=disable_logging, expected_type=type_hints["disable_logging"])
            check_type(argname="argument log_options", value=log_options, expected_type=type_hints["log_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backoff_rate": backoff_rate,
            "interval": interval,
            "is_complete_handler": is_complete_handler,
            "max_attempts": max_attempts,
            "timeout_handler": timeout_handler,
        }
        if disable_logging is not None:
            self._values["disable_logging"] = disable_logging
        if log_options is not None:
            self._values["log_options"] = log_options

    @builtins.property
    def backoff_rate(self) -> jsii.Number:
        '''Backoff between attempts.'''
        result = self._values.get("backoff_rate")
        assert result is not None, "Required property 'backoff_rate' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> _Duration_4839e8c3:
        '''The interval to wait between attempts.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def is_complete_handler(self) -> _IFunction_6adb0ab8:
        '''The main handler that notifies if the waiter to decide 'complete' or 'incomplete'.'''
        result = self._values.get("is_complete_handler")
        assert result is not None, "Required property 'is_complete_handler' is missing"
        return typing.cast(_IFunction_6adb0ab8, result)

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Number of attempts.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def timeout_handler(self) -> _IFunction_6adb0ab8:
        '''The handler to call if the waiter times out and is incomplete.'''
        result = self._values.get("timeout_handler")
        assert result is not None, "Required property 'timeout_handler' is missing"
        return typing.cast(_IFunction_6adb0ab8, result)

    @builtins.property
    def disable_logging(self) -> typing.Optional[builtins.bool]:
        '''Whether logging for the state machine is disabled.

        :default: - false
        '''
        result = self._values.get("disable_logging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def log_options(self) -> typing.Optional[LogOptions]:
        '''Defines what execution history events are logged and where they are logged.

        :default: - A default log group will be created if logging is enabled.
        '''
        result = self._values.get("log_options")
        return typing.cast(typing.Optional[LogOptions], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WaiterStateMachineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsCustomResource",
    "AwsCustomResourcePolicy",
    "AwsCustomResourceProps",
    "AwsSdkCall",
    "LogOptions",
    "Logging",
    "LoggingProps",
    "PhysicalResourceId",
    "PhysicalResourceIdReference",
    "Provider",
    "ProviderProps",
    "SdkCallsPolicyOptions",
    "WaiterStateMachine",
    "WaiterStateMachineProps",
]

publication.publish()

def _typecheckingstub__4b163f566913e92c7adaa1ea97e50050b801bd514d3b2f5e3ddf86c11297e862(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    function_name: typing.Optional[builtins.str] = None,
    install_latest_aws_sdk: typing.Optional[builtins.bool] = None,
    log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    on_create: typing.Optional[typing.Union[AwsSdkCall, typing.Dict[builtins.str, typing.Any]]] = None,
    on_delete: typing.Optional[typing.Union[AwsSdkCall, typing.Dict[builtins.str, typing.Any]]] = None,
    on_update: typing.Optional[typing.Union[AwsSdkCall, typing.Dict[builtins.str, typing.Any]]] = None,
    policy: typing.Optional[AwsCustomResourcePolicy] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    resource_type: typing.Optional[builtins.str] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a62242b1380cc5a46c343b8beb355b12ad4bead7d218dff7533f32ef95535dc(
    data_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3cb7c74c2f60a8f1c2cfe429816d6751f4abf9bd7f2fccca230d2e342d4c5e(
    data_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__267132a8dbe09112fac8abcec56b61816ca5265080c0657023e152ec4eff48b1(
    statements: typing.Sequence[_PolicyStatement_0fe33853],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5a9dace9a09081edfef936656f2d5670f198fb300a32c31957c93e5bb08c2f(
    *,
    function_name: typing.Optional[builtins.str] = None,
    install_latest_aws_sdk: typing.Optional[builtins.bool] = None,
    log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    on_create: typing.Optional[typing.Union[AwsSdkCall, typing.Dict[builtins.str, typing.Any]]] = None,
    on_delete: typing.Optional[typing.Union[AwsSdkCall, typing.Dict[builtins.str, typing.Any]]] = None,
    on_update: typing.Optional[typing.Union[AwsSdkCall, typing.Dict[builtins.str, typing.Any]]] = None,
    policy: typing.Optional[AwsCustomResourcePolicy] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    resource_type: typing.Optional[builtins.str] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7bb124668b93c6ce7d641df2daeabfe424e271742385a76e7e56ec91c39dc9(
    *,
    action: builtins.str,
    service: builtins.str,
    api_version: typing.Optional[builtins.str] = None,
    assumed_role_arn: typing.Optional[builtins.str] = None,
    ignore_error_codes_matching: typing.Optional[builtins.str] = None,
    logging: typing.Optional[Logging] = None,
    output_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Any = None,
    physical_resource_id: typing.Optional[PhysicalResourceId] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2622296f61199d2b10825c21d976c0578e9488ad1b2b7635565f604c598734b7(
    *,
    destination: typing.Optional[_ILogGroup_3c4fa718] = None,
    include_execution_data: typing.Optional[builtins.bool] = None,
    level: typing.Optional[_LogLevel_be1990fe] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da0d46a1eb4b059395d06daee7dcb9417dffd0b4cf8e8942cbe0a6549f0faf4b(
    *,
    log_api_response_data: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6baa8764ccdf77f11bd8f80af9fafec69f56b719c1a237caae55c7f988e174b6(
    response_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdca735a77f74ade2070f6a3cbaf95d939ee16657cec7f53ec60b2df0a096bd2(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784d4e05d144bc71f705b7f70440a6f66fee012cf9cf6f0bea5bbf88c7b49fd7(
    _context: _IResolveContext_b2df1921,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29415d7bf7977fcf110b77ce69cec309dcf0404601944735020770ddfe2b01a8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    on_event_handler: _IFunction_6adb0ab8,
    disable_waiter_state_machine_logging: typing.Optional[builtins.bool] = None,
    is_complete_handler: typing.Optional[_IFunction_6adb0ab8] = None,
    log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    provider_function_env_encryption: typing.Optional[_IKey_5f11635f] = None,
    provider_function_name: typing.Optional[builtins.str] = None,
    query_interval: typing.Optional[_Duration_4839e8c3] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    total_timeout: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    waiter_state_machine_log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b03803ee02437d8d83814282c700ede5633030e4d9f7ebdaf3b9d075b0cbdb(
    *,
    on_event_handler: _IFunction_6adb0ab8,
    disable_waiter_state_machine_logging: typing.Optional[builtins.bool] = None,
    is_complete_handler: typing.Optional[_IFunction_6adb0ab8] = None,
    log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    provider_function_env_encryption: typing.Optional[_IKey_5f11635f] = None,
    provider_function_name: typing.Optional[builtins.str] = None,
    query_interval: typing.Optional[_Duration_4839e8c3] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    total_timeout: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    waiter_state_machine_log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cd00e8add38e42b6c4d7db0390a899ccaf5bbe0367bfb387986125dacc7a297(
    *,
    resources: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12427b739f326cdb535d2aaf4a70f10977eec5711902d4e5e395f0b8c9bb184e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    backoff_rate: jsii.Number,
    interval: _Duration_4839e8c3,
    is_complete_handler: _IFunction_6adb0ab8,
    max_attempts: jsii.Number,
    timeout_handler: _IFunction_6adb0ab8,
    disable_logging: typing.Optional[builtins.bool] = None,
    log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c3d1c306ca04ebd1194ce4f97bed6aa9510a02067654b39f43a1ecef601e3db(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569ff1333551048ad82f7261bcf43cbefe118e974cba179165c355fc9347fc13(
    *,
    backoff_rate: jsii.Number,
    interval: _Duration_4839e8c3,
    is_complete_handler: _IFunction_6adb0ab8,
    max_attempts: jsii.Number,
    timeout_handler: _IFunction_6adb0ab8,
    disable_logging: typing.Optional[builtins.bool] = None,
    log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
